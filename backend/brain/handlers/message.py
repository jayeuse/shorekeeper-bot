import time
from pathlib import Path
from core.config import (
    MEMORY_CANDIDATE_POOL,
    MEMORY_DB_PATH,
    MEMORY_ENABLED,
    MEMORY_RECALL_LIMIT,
    MEMORY_RECENCY_HALFLIFE_DAYS,
    MEMORY_RELEVANCE_THRESHOLD,
    SYSTEM_PROMPT,
)
from utils.logger import log_response
from services.rag import RAG
from services.llm import LLMClient
from services.memory import MemoryRecord, MemoryService
from handlers.conversation_context import store_chat, get_chat

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

_META_PATTERNS = [
    "what topics do you have", "what's in your database", "list your knowledge",
    "what factions are in your records", "what groups do you know",
]
_CASUAL_PATTERNS = [
    "how are you", "how do you feel", "tell me about yourself", "what do you think",
    "what's your opinion", "do you like", "are you okay", "how have you been",
    "good morning", "good night", "hello", "hi ", "hey ",
]


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
            (
                f"[Memory {index} | scope={memory.scope} | time={timestamp} | "
                f"topics={topics} | score={memory.score:.3f}]\n"
                f"User: {clip(memory.user_message)}\n"
                f"Assistant: {clip(memory.assistant_message)}"
            )
        )
    return "\n\n".join(sections)


async def on_message(bot, msg):
    if msg.author == bot.user:
        return

    is_mentioned = bot.user in msg.mentions

    is_reply_to_bot = (
        msg.reference
        and msg.reference.resolved
        and msg.reference.resolved.author == bot.user
    )

    if not (is_mentioned or is_reply_to_bot):
        return

    print(f"📩 Received message from {msg.author}: {msg.content}")

    try:
        server_id, channel_id, user_id = _scope_ids(msg)
        user_content = msg.content.replace(f"<@{bot.user.id}>", "").strip()

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

            context_text = ""
            if context_chunks:
                context_text = "\n\n".join(
                    f"[{c['source']} - {c['heading']}]\n{c['text']}"
                    for c in context_chunks
                )

            personalization = rag.get_personalization_context()
            manifest = rag.get_manifest()
            system_sections = [
                SYSTEM_PROMPT,
                f"=== PERSONALITY & BACKSTORY ===\n{personalization}",
                manifest,
            ]

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

            full_system_prompt = "\n\n".join(system_sections)
            messages = [
                {"role": "system", "content": full_system_prompt},
            ] + get_chat(server_id, channel_id)

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

    except Exception as e:
        print(f"❌ Critical Error in on_message: {e}")
        await msg.reply(f"⚠️ Calculation error: {e}")


def split_message(text, limit=2000):
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
