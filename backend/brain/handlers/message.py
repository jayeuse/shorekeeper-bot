from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path

from core.config import (
    MEMORY_CANDIDATE_POOL,
    MEMORY_DB_PATH,
    MEMORY_ENABLED,
    MEMORY_RECALL_LIMIT,
    MEMORY_RECENCY_HALFLIFE_DAYS,
    MEMORY_RELEVANCE_THRESHOLD,
    SEARCH_CURRENT_HINTS,
    SEARCH_ENABLED,
    SEARCH_EXPLICIT_PREFIX,
    SEARCH_MAX_RESULTS,
    SEARCH_MIN_QUERY_LENGTH,
    SEARCH_PROVIDER,
    SEARCH_TRIGGER_MODE,
    SYSTEM_PROMPT,
)
from handlers.conversation_context import get_chat, store_chat
from services.llm import LLMClient
from services.memory import MemoryRecord, MemoryService
from services.rag import RAG
from services.search import (
    SearchBundle,
    SearchError,
    SearchProvider,
    build_search_provider,
)
from utils.logger import log_response

rag = RAG()
llm_client = LLMClient()


def _resolve_memory_db_path() -> str:
    if Path(MEMORY_DB_PATH).is_absolute():
        return MEMORY_DB_PATH
    project_root = Path(__file__).resolve().parents[3]
    return str((project_root / MEMORY_DB_PATH).resolve())


if MEMORY_ENABLED:
    try:
        memory_service = MemoryService(
            db_path=_resolve_memory_db_path(),
            recency_half_life_days=MEMORY_RECENCY_HALFLIFE_DAYS,
        )
    except Exception as exc:
        print(f"⚠️ Memory initialization failed: {exc}")
        memory_service = None
else:
    memory_service = None

if SEARCH_ENABLED:
    try:
        search_provider: SearchProvider | None = build_search_provider()
    except Exception as exc:
        print(f"⚠️ Search provider initialization failed: {exc}")
        search_provider = None
else:
    search_provider = None

_META_PATTERNS = [
    "what topics do you have",
    "what's in your database",
    "list your knowledge",
    "what factions are in your records",
    "what groups do you know",
]
_CASUAL_PATTERNS = [
    "how are you",
    "how do you feel",
    "tell me about yourself",
    "what do you think",
    "what's your opinion",
    "do you like",
    "are you okay",
    "how have you been",
    "good morning",
    "good night",
    "hello",
    "hi ",
    "hey ",
]
_SEARCH_FRESHNESS_HINTS = set(SEARCH_CURRENT_HINTS) | {
    "recent",
    "search for",
    "what happened",
}
_SEARCH_BLOCK_PATTERNS = [
    *_META_PATTERNS,
    *_CASUAL_PATTERNS,
    "remember",
    "do you remember",
    "last time",
    "we talked",
    "who is ",
    "tell me about",
    "lore",
    "story",
    "ability",
    "abilities",
    "kit",
    "rotation",
    "resonator",
    "black shores",
    "rinascita",
    "huanglong",
    "jinzhou",
    "rover",
]


@dataclass(slots=True)
class SearchDecision:
    reason: str
    query: str
    should_search: bool


@dataclass(slots=True)
class SearchExecution:
    used: bool
    reason: str
    query: str
    provider: str
    result_count: int
    duration: float
    error: str | None
    bundle: SearchBundle | None = None


def _classify_query(query: str) -> str:
    """Classify query to determine how many RAG chunks are needed.

    Returns:
        "meta"   — query is about the knowledge base itself → skip RAG
        "casual" — light conversational query → top_k=2
        "lore"   — character/lore/ability query → top_k=5
    """
    q = query.lower()
    if any(p in q for p in _META_PATTERNS):
        return "meta"
    if any(p in q for p in _CASUAL_PATTERNS):
        return "casual"
    return "lore"


_TOP_K = {"meta": 0, "casual": 2, "lore": 5}


def _scope_ids(msg) -> tuple[str, str, str]:
    server_id = str(msg.guild.id) if msg.guild else "dm"
    channel_id = str(msg.channel.id)
    user_id = str(msg.author.id)
    return server_id, channel_id, user_id


def _clean_user_content(content: str, bot_user_id: int) -> str:
    return content.replace(f"<@{bot_user_id}>", "").strip()


def _format_memory_context(memories: list[MemoryRecord]) -> str:
    sections: list[str] = []

    def clip(text: str, max_len: int = 280) -> str:
        if len(text) <= max_len:
            return text
        return f"{text[:max_len].rstrip()}..."

    for index, memory in enumerate(memories, start=1):
        topics = ", ".join(memory.topics)
        timestamp = memory.created_at.replace("T", " ")[:19]
        sections.append(
            f"[Memory {index} | scope={memory.scope} | time={timestamp} | "
            f"topics={topics} | score={memory.score:.3f}]\n"
            f"User: {clip(memory.user_message)}\n"
            f"Assistant: {clip(memory.assistant_message)}"
        )
    return "\n\n".join(sections)


def _format_knowledge_context(context_chunks: list[dict]) -> str:
    return "\n\n".join(
        f"[{c['source']} - {c['heading']}]\n{c['text']}" for c in context_chunks
    )


def _contains_freshness_cue(query: str) -> bool:
    return any(hint.lower() in query for hint in _SEARCH_FRESHNESS_HINTS)


def _is_obvious_non_search_query(query: str) -> bool:
    if _classify_query(query) in {"meta", "casual"}:
        return True
    return any(pattern in query for pattern in _SEARCH_BLOCK_PATTERNS)


def _decide_search(user_content: str) -> SearchDecision:
    cleaned = user_content.strip()
    prefix = SEARCH_EXPLICIT_PREFIX.strip()

    if not SEARCH_ENABLED or search_provider is None:
        return SearchDecision(reason="search_disabled", query="", should_search=False)

    if prefix and cleaned.lower().startswith(prefix.lower()):
        stripped_query = cleaned[len(prefix) :].strip()
        if len(stripped_query) < SEARCH_MIN_QUERY_LENGTH:
            return SearchDecision(
                reason="search_not_needed",
                query=stripped_query,
                should_search=False,
            )
        return SearchDecision(reason="search_explicit", query=stripped_query, should_search=True)

    if SEARCH_TRIGGER_MODE != "hybrid":
        return SearchDecision(reason="search_not_needed", query="", should_search=False)

    lowered = cleaned.lower()
    if _is_obvious_non_search_query(lowered):
        return SearchDecision(reason="search_not_needed", query="", should_search=False)
    if not _contains_freshness_cue(lowered):
        return SearchDecision(reason="search_not_needed", query="", should_search=False)
    if len(cleaned) < SEARCH_MIN_QUERY_LENGTH:
        return SearchDecision(reason="search_not_needed", query=cleaned, should_search=False)
    return SearchDecision(reason="search_freshness", query=cleaned, should_search=True)


async def _execute_search(decision: SearchDecision) -> SearchExecution:
    provider_name = SEARCH_PROVIDER if search_provider is not None else "disabled"
    if not decision.should_search or search_provider is None:
        return SearchExecution(
            used=False,
            reason=decision.reason,
            query=decision.query,
            provider=provider_name,
            result_count=0,
            duration=0.0,
            error=None,
        )

    start = time.time()
    try:
        bundle = await search_provider.search(decision.query, SEARCH_MAX_RESULTS)
    except SearchError as exc:
        return SearchExecution(
            used=False,
            reason="search_failed_continue_without_results",
            query=decision.query,
            provider=provider_name,
            result_count=0,
            duration=time.time() - start,
            error=str(exc),
        )
    except Exception as exc:
        return SearchExecution(
            used=False,
            reason="search_failed_continue_without_results",
            query=decision.query,
            provider=provider_name,
            result_count=0,
            duration=time.time() - start,
            error=f"Unexpected search error: {exc}",
        )

    if not bundle.results:
        return SearchExecution(
            used=False,
            reason="search_failed_continue_without_results",
            query=decision.query,
            provider=bundle.provider,
            result_count=0,
            duration=time.time() - start,
            error="Search returned no results",
        )

    return SearchExecution(
        used=True,
        reason=decision.reason,
        query=decision.query,
        provider=bundle.provider,
        result_count=len(bundle.results),
        duration=time.time() - start,
        error=None,
        bundle=bundle,
    )


def _format_search_context(bundle: SearchBundle) -> str:
    sections = [
        "=== LIVE SEARCH RESULTS ===",
        "Use these results only for current or time-sensitive facts.",
    ]
    for index, result in enumerate(bundle.results, start=1):
        published_line = f"\nPublished: {result.published_at}" if result.published_at else ""
        snippet_line = f"\nSnippet: {result.snippet}" if result.snippet else ""
        sections.append(
            f"[Result {index}]\n"
            f"Title: {result.title}\n"
            f"Source: {result.source}\n"
            f"URL: {result.url}"
            f"{published_line}"
            f"{snippet_line}"
        )

    sections.append(
        "Instructions:\n"
        "- Use live search results only for fresh or external facts.\n"
        "- Prefer retrieved local knowledge for Wuthering Waves lore, character identity, "
        "and story grounding.\n"
        "- If the live search results are weak or conflicting, answer cautiously and avoid "
        "fabricated certainty.\n"
        "- Do not mention citations or URLs unless the user explicitly asks for sources.\n"
        "- Do not claim freshness unless live search results were provided in this response."
    )
    return "\n\n".join(sections)


def _build_system_prompt(
    *,
    personalization: str,
    manifest: str,
    context_text: str,
    relevant_memories: list[MemoryRecord],
    search_execution: SearchExecution,
) -> str:
    system_sections = [
        SYSTEM_PROMPT,
        f"=== PERSONALITY & BACKSTORY ===\n{personalization}",
        manifest,
    ]

    if context_text:
        system_sections.append(
            f"Here is relevant knowledge to ground your response:\n\n{context_text}"
        )

    if relevant_memories:
        memory_context = _format_memory_context(relevant_memories)
        system_sections.append(
            "Here are relevant conversation memories. "
            "Use them only when they are directly relevant to the current query:\n\n"
            f"{memory_context}"
        )

    if search_execution.used and search_execution.bundle is not None:
        system_sections.append(_format_search_context(search_execution.bundle))
    elif search_execution.reason == "search_failed_continue_without_results":
        system_sections.append(
            "Live search was unavailable for this response. "
            "Avoid claiming current facts as certain."
        )

    return "\n\n".join(system_sections)


async def on_message(bot, msg):
    if msg.author == bot.user:
        return

    is_mentioned = bot.user in msg.mentions
    is_reply_to_bot = (
        msg.reference and msg.reference.resolved and msg.reference.resolved.author == bot.user
    )
    if not (is_mentioned or is_reply_to_bot):
        return

    print(f"📩 Received message from {msg.author}: {msg.content}")

    try:
        server_id, channel_id, user_id = _scope_ids(msg)
        user_content = _clean_user_content(msg.content, bot.user.id)

        start_time = time.time()
        memory_duration = 0.0
        memory_scanned = 0
        memory_selected = 0
        memory_top_score = 0.0
        relevant_memories: list[MemoryRecord] = []

        async with msg.channel.typing():
            rag_start = time.time()
            query_type = _classify_query(user_content)
            top_k = _TOP_K[query_type]
            context_chunks = rag.search(user_content, top_k=top_k) if top_k > 0 else []
            rag_duration = time.time() - rag_start
            context_text = _format_knowledge_context(context_chunks) if context_chunks else ""

            personalization = rag.get_personalization_context()
            manifest = rag.get_manifest()

            if memory_service is not None and query_type != "meta":
                memory_start = time.time()
                try:
                    relevant_memories, memory_scanned = memory_service.retrieve_relevant_with_metrics(
                        query=user_content,
                        server_id=server_id,
                        channel_id=channel_id,
                        user_id=user_id,
                        limit=MEMORY_RECALL_LIMIT,
                        relevance_threshold=MEMORY_RELEVANCE_THRESHOLD,
                        candidate_pool=MEMORY_CANDIDATE_POOL,
                    )
                except Exception as exc:
                    print(f"⚠️ Memory retrieval failed: {exc}")
                    relevant_memories = []
                    memory_scanned = 0
                memory_duration = time.time() - memory_start
                memory_selected = len(relevant_memories)
                if relevant_memories:
                    memory_top_score = relevant_memories[0].score

            search_decision = _decide_search(user_content)
            search_execution = await _execute_search(search_decision)

            full_system_prompt = _build_system_prompt(
                personalization=personalization,
                manifest=manifest,
                context_text=context_text,
                relevant_memories=relevant_memories,
                search_execution=search_execution,
            )
            messages = [{"role": "system", "content": full_system_prompt}] + get_chat(
                server_id, channel_id
            )

            store_chat(server_id, channel_id, msg.content, "user")
            messages.append({"role": "user", "content": user_content})

            llm_start = time.time()
            response = await llm_client.chat(messages)
            llm_duration = time.time() - llm_start

            elapsed = time.time() - start_time
            log_response(
                msg,
                user_content,
                response.get("model") or llm_client.model or "unknown",
                response,
                elapsed,
                rag_duration=rag_duration,
                llm_duration=llm_duration,
                query_type=query_type,
                top_k=top_k,
                memory_scanned=memory_scanned,
                memory_selected=memory_selected,
                memory_top_score=memory_top_score,
                memory_duration=memory_duration,
                search_used=search_execution.used,
                search_reason=search_execution.reason,
                search_query=search_execution.query,
                search_provider=search_execution.provider,
                search_result_count=search_execution.result_count,
                search_duration=search_execution.duration,
                search_error=search_execution.error,
            )

            reply_content = response["message"]["content"]
            store_chat(server_id, channel_id, reply_content, "assistant")

            if memory_service is not None:
                try:
                    memory_service.store_exchange(
                        server_id=server_id,
                        channel_id=channel_id,
                        user_id=user_id,
                        user_message=user_content,
                        assistant_message=reply_content,
                    )
                except Exception as exc:
                    print(f"⚠️ Memory persistence failed: {exc}")

            chunks = split_message(reply_content)
            await msg.reply(chunks[0])
            for chunk in chunks[1:]:
                await msg.channel.send(chunk)

    except Exception as exc:
        print(f"❌ Critical Error in on_message: {exc}")
        await msg.reply(f"⚠️ Calculation error: {exc}")


def split_message(text: str, limit: int = 2000) -> list[str]:
    if len(text) <= limit:
        return [text]

    chunks = []
    while text:
        if len(text) <= limit:
            chunks.append(text)
            break

        split_at = text.rfind("\n", 0, limit)
        if split_at == -1:
            split_at = text.rfind(" ", 0, limit)
        if split_at == -1:
            split_at = limit

        chunks.append(text[:split_at])
        text = text[split_at:].lstrip("\n")

    return chunks
