from __future__ import annotations

import asyncio
import json
import re
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from core.config import (
    ANALYSIS_ENABLED,
    ANALYSIS_TIMEOUT_SECONDS,
    GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD,
    MEMORY_CANDIDATE_POOL,
    MEMORY_DB_PATH,
    MEMORY_ENABLED,
    MEMORY_RECALL_LIMIT,
    MEMORY_RECENCY_HALFLIFE_DAYS,
    MEMORY_RELEVANCE_THRESHOLD,
    RAG_ANSWER_SCORE_THRESHOLD,
    ROUTER_HISTORY_TURNS,
    SYSTEM_PROMPT,
)
from handlers.conversation_context import get_chat, store_chat
from services.llm import LLMClient
from services.memory import MemoryRecord, MemoryService
from services.rag import RAG
from services.search import (
    SearchExecution,
    build_search_context_block,
    infer_search_question_type,
    infer_search_requested_fact,
    infer_search_subject_domain,
    infer_search_target_entity,
    normalize_search_query,
    search_execution_allows_exact_claims,
    serialize_search_evidence_summary,
    serialize_search_results,
)
from utils.logger import log_response

rag = RAG()
llm_client = LLMClient()


def _resolve_memory_db_path() -> str:
    if Path(MEMORY_DB_PATH).is_absolute():
        return MEMORY_DB_PATH
    project_root = Path(__file__).resolve().parents[3]
    return str((project_root / MEMORY_DB_PATH).resolve())


memory_service: MemoryService | None
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
    "what topics do you have",
    "what's in your database",
    "list your knowledge",
    "what factions are in your records",
    "what groups do you know",
]
_MEMORY_PATTERNS = [
    "remember",
    "do you remember",
    "last time",
    "we talked",
    "you told me",
    "i told you",
    "earlier",
    "previously",
    "before this",
    "first question i asked",
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
    "who are you",
]
_DATETIME_PATTERNS = [
    "what's the date",
    "whats the date",
    "what is the date",
    "today's date",
    "todays date",
    "current date",
    "what day is it",
    "what day is today",
    "what time is it",
    "what time is it now",
    "current time",
    "what month is it",
    "what year is it",
]
_DISCORD_MENTION_RE = re.compile(r"<@!?\d+>")
_JSON_OBJECT_RE = re.compile(r"\{.*\}", re.DOTALL)
_DATE_HINTS = ("date", "day", "month", "year", "today")
_TIME_HINTS = ("time", "clock")
_ELLIPTICAL_FOLLOWUP_PREFIXES = (
    "what about",
    "how about",
    "and in ",
    "and what about",
    "what about in ",
    "yeah but",
    "that one",
    "there",
)
_TOP_K = {"meta": 0, "datetime": 0, "memory": 0, "casual": 0, "general": 5}


@dataclass(slots=True)
class AnalysisDecision:
    rag_query: str
    can_answer_from_general_knowledge: bool
    general_knowledge_confidence: float
    reason: str
    raw_payload: dict[str, Any] | None = None


@dataclass(slots=True)
class RoutePlan:
    path: str
    query_type: str
    query_text: str
    reason: str
    use_memory: bool = False
    deterministic_gate: str = ""
    analysis_used: bool = False
    analysis_payload: dict[str, Any] | None = None
    analysis_decision: AnalysisDecision | None = None
    target_entity: str = ""
    requested_fact: str = ""
    question_type_hint: str = ""
    subject_domain: str = ""


@dataclass(slots=True)
class RagDecision:
    accepted: bool
    top_score: float
    context_chunks: list[dict[str, Any]]
    query: str
    rejection_reason: str = ""


def _classify_query(query: str) -> str:
    q = " ".join(query.lower().split())
    if any(p in q for p in _META_PATTERNS):
        return "meta"
    if any(p in q for p in _DATETIME_PATTERNS):
        return "datetime"
    if any(p in q for p in _MEMORY_PATTERNS):
        return "memory"
    if any(p in q for p in _CASUAL_PATTERNS):
        return "casual"
    return "general"


def _rag_is_eligible(question_type: str, user_content: str, rag_query: str) -> bool:
    lowered = normalize_search_query(f"{user_content} {rag_query}").lower()
    if question_type in {
        "definition",
        "identity",
        "current_metric",
        "latest_release",
        "current_availability",
        "event_status",
    }:
        return False
    if any(
        term in lowered
        for term in ("meaning of", "what does", "define", "dictionary", "your name", "who are you")
    ):
        return False
    if any(
        term in lowered
        for term in ("tell me about", "lore", "story", "black shores", "resonator", "faction")
    ):
        return True
    return question_type in {"background_fact"}


def _extract_recent_user_queries(
    chat_history: list[dict], *, limit: int | None = None
) -> list[str]:
    user_messages: list[str] = []
    max_items = limit if limit is not None else ROUTER_HISTORY_TURNS
    for message in reversed(chat_history):
        if message.get("role") != "user":
            continue
        content = message.get("content")
        if isinstance(content, str) and content.strip():
            cleaned = _DISCORD_MENTION_RE.sub("", content).strip()
            if cleaned and _classify_query(cleaned) != "datetime":
                user_messages.append(cleaned)
        if len(user_messages) >= max_items:
            break
    return user_messages


def _looks_elliptical_followup(query: str) -> bool:
    lowered = normalize_search_query(query).lower()
    return lowered.startswith(_ELLIPTICAL_FOLLOWUP_PREFIXES)


def _extract_json_object(text: str) -> dict[str, Any] | None:
    match = _JSON_OBJECT_RE.search(text)
    if not match:
        return None
    try:
        parsed = json.loads(match.group(0))
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def _build_deterministic_route_plan(user_content: str) -> RoutePlan | None:
    cleaned = user_content.strip()
    query_type = _classify_query(cleaned)
    if query_type == "datetime":
        return RoutePlan(
            path="datetime",
            query_type=query_type,
            query_text=cleaned,
            reason="datetime",
            deterministic_gate="datetime",
        )
    if query_type == "meta":
        return RoutePlan(
            path="general",
            query_type=query_type,
            query_text=cleaned,
            reason="meta_direct",
            deterministic_gate="meta",
        )
    if query_type == "casual":
        return RoutePlan(
            path="general",
            query_type=query_type,
            query_text=cleaned,
            reason="casual_direct",
            deterministic_gate="casual",
        )
    if query_type == "memory":
        return RoutePlan(
            path="memory",
            query_type=query_type,
            query_text=cleaned,
            reason="memory_direct",
            deterministic_gate="memory",
            use_memory=True,
        )
    return None


def _build_analysis_messages(user_content: str, recent_user_queries: list[str]) -> list[dict]:
    history_lines = [
        f"{index}. {query}" for index, query in enumerate(reversed(recent_user_queries), start=1)
    ]
    history_block = "\n".join(history_lines) if history_lines else "None"
    system_prompt = (
        "You are a routing and query-analysis component for a Discord bot. "
        "Do not roleplay. Do not answer the user. Return strict JSON only.\n"
        "Available knowledge sources:\n"
        "- local datetime for date/time questions\n"
        "- local RAG knowledge base for stable in-repo knowledge and lore\n"
        "- general model knowledge only for stable non-time-sensitive questions when safe\n"
        "Return JSON with keys: rag_query, can_answer_from_general_knowledge, general_knowledge_confidence, reason.\n"
        "Rules:\n"
        "- Use recent user turns only to resolve elliptical follow-ups.\n"
        "- Always provide a standalone rag_query.\n"
        "- If the model would not be safe answering from general knowledge after weak RAG, set can_answer_from_general_knowledge=false."
    )
    user_prompt = (
        f"Recent user turns:\n{history_block}\n\n"
        f"Current user message:\n{user_content}\n\n"
        "Return strict JSON only."
    )
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def _analysis_fallback(user_content: str, recent_user_queries: list[str]) -> AnalysisDecision:
    normalized = normalize_search_query(user_content)
    if _looks_elliptical_followup(normalized) and recent_user_queries:
        normalized = (
            f"{normalized} {normalize_search_query(recent_user_queries[0]).lower()}".strip()
        )
    return AnalysisDecision(
        rag_query=normalized or user_content,
        can_answer_from_general_knowledge=False,
        general_knowledge_confidence=0.0,
        reason="analysis_fallback",
        raw_payload={"fallback": True},
    )


def _validate_analysis_decision(payload: dict[str, Any]) -> AnalysisDecision | None:
    rag_query = payload.get("rag_query", "")
    can_answer_from_general_knowledge = payload.get("can_answer_from_general_knowledge", False)
    general_knowledge_confidence = payload.get("general_knowledge_confidence", 0.0)
    reason = payload.get("reason", "")

    if not isinstance(rag_query, str) or not isinstance(reason, str):
        return None
    if not isinstance(can_answer_from_general_knowledge, bool):
        return None

    normalized_rag_query = normalize_search_query(rag_query)
    normalized_reason = " ".join(reason.strip().split())[:200]

    try:
        normalized_general_confidence = max(0.0, min(float(general_knowledge_confidence), 1.0))
    except Exception:
        normalized_general_confidence = 0.0

    if not normalized_rag_query:
        return None

    return AnalysisDecision(
        rag_query=normalized_rag_query,
        can_answer_from_general_knowledge=can_answer_from_general_knowledge,
        general_knowledge_confidence=normalized_general_confidence,
        reason=normalized_reason,
        raw_payload=payload,
    )


async def _run_analysis_pass(user_content: str, chat_history: list[dict]) -> AnalysisDecision:
    recent_user_queries = _extract_recent_user_queries(chat_history)
    if not ANALYSIS_ENABLED:
        return _analysis_fallback(user_content, recent_user_queries)

    messages = _build_analysis_messages(user_content, recent_user_queries)
    try:
        response = await asyncio.wait_for(
            llm_client.chat(messages), timeout=ANALYSIS_TIMEOUT_SECONDS
        )
    except Exception as exc:
        print(f"⚠️ Analysis failed: {exc}")
        return _analysis_fallback(user_content, recent_user_queries)

    analysis_text = response.get("message", {}).get("content", "")
    if not isinstance(analysis_text, str) or not analysis_text.strip():
        return _analysis_fallback(user_content, recent_user_queries)

    payload = _extract_json_object(analysis_text)
    if payload is None:
        return _analysis_fallback(user_content, recent_user_queries)

    validated = _validate_analysis_decision(payload)
    if validated is None:
        return _analysis_fallback(user_content, recent_user_queries)
    return validated


async def _build_route_plan(user_content: str, chat_history: list[dict]) -> RoutePlan:
    deterministic_plan = _build_deterministic_route_plan(user_content)
    if deterministic_plan is not None:
        return deterministic_plan

    analysis = await _run_analysis_pass(user_content, chat_history)
    resolved_query = analysis.rag_query or normalize_search_query(user_content) or user_content
    requested_fact = infer_search_requested_fact(resolved_query)
    question_type = infer_search_question_type(
        requested_fact=requested_fact,
        time_sensitive=False,
        text=resolved_query,
    )
    return RoutePlan(
        path="rag" if _rag_is_eligible(question_type, user_content, resolved_query) else "general",
        query_type="general",
        query_text=resolved_query,
        reason=analysis.reason,
        analysis_used=True,
        analysis_payload=analysis.raw_payload,
        analysis_decision=analysis,
        target_entity=infer_search_target_entity(resolved_query),
        requested_fact=requested_fact,
        question_type_hint=question_type,
        subject_domain=infer_search_subject_domain(resolved_query),
    )


def _build_datetime_response(user_content: str) -> str:
    now = datetime.now().astimezone()
    lowered = user_content.lower()
    date_text = now.strftime("%A, %B %-d, %Y")
    time_text = now.strftime("%I:%M %p").lstrip("0")
    tz_name = now.tzname() or "local time"
    asks_time = any(hint in lowered for hint in _TIME_HINTS)
    asks_date = any(hint in lowered for hint in _DATE_HINTS)
    if asks_time and asks_date:
        return f"My internal chronometers place us at {time_text} {tz_name} on {date_text}. The tides of this record remain steady."
    if asks_time:
        return f"My internal chronometers place the current time at {time_text} {tz_name}. The tides of this record remain steady."
    return f"My internal chronometers mark today as {date_text}. The tides of this record remain steady."


def _build_uncertainty_response() -> str:
    return "I do not know that accurately from my current records, and I would rather leave the answer uncertain than offer you a false one."


def _evaluate_rag(query: str, *, question_type: str, user_content: str) -> RagDecision:
    if not _rag_is_eligible(question_type, user_content, query):
        return RagDecision(
            accepted=False,
            top_score=0.0,
            context_chunks=[],
            query=query,
            rejection_reason="question_type_incompatible",
        )
    start_top_k = _TOP_K["general"]
    chunks = rag.search(query, top_k=start_top_k)
    top_score = float(chunks[0]["score"]) if chunks else 0.0
    accepted = bool(chunks) and top_score >= RAG_ANSWER_SCORE_THRESHOLD
    if question_type == "background_fact":
        accepted = accepted and any(
            token in normalize_search_query(chunks[0].get("text", "")).lower()
            for token in _meaningful_anchor_tokens(query)
        )
    return RagDecision(
        accepted=accepted,
        top_score=top_score,
        context_chunks=chunks if accepted else [],
        query=query,
        rejection_reason="" if accepted else ("score_below_threshold" if chunks else "no_chunks"),
    )


def _meaningful_anchor_tokens(text: str) -> set[str]:
    stopwords = {"the", "and", "what", "who", "tell", "about", "your", "name", "mean", "meaning"}
    return {
        token
        for token in re.findall(r"[a-z0-9]+", text.lower())
        if len(token) > 3 and token not in stopwords
    }


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
            f"[Memory {index} | scope={memory.scope} | time={timestamp} | topics={topics} | score={memory.score:.3f}]\n"
            f"User: {clip(memory.user_message)}\n"
            f"Assistant: {clip(memory.assistant_message)}"
        )
    return "\n\n".join(sections)


def _format_knowledge_context(context_chunks: list[dict[str, Any]]) -> str:
    return "\n\n".join(f"[{c['source']} - {c['heading']}]\n{c['text']}" for c in context_chunks)


def _build_system_prompt(
    *,
    source_path: str,
    personalization: str,
    manifest: str,
    resolved_query: str,
    relevant_memories: list[MemoryRecord],
    rag_decision: RagDecision | None,
    search_execution: SearchExecution,
) -> str:
    system_sections = [
        SYSTEM_PROMPT,
        f"=== PERSONALITY & BACKSTORY ===\n{personalization}",
        manifest,
    ]
    system_sections.append(
        "Resolved interpretation of the current user message:\n"
        f"{resolved_query}\n"
        "Use this only to interpret the user's current intent."
    )

    if source_path == "memory" and relevant_memories:
        system_sections.append(
            "Answer from relevant conversation memory when it directly supports the response:\n\n"
            f"{_format_memory_context(relevant_memories)}"
        )
    elif source_path == "rag" and rag_decision and rag_decision.context_chunks:
        system_sections.append(
            "Answer only from the accepted local knowledge context below. Do not invent unsupported lore or facts:\n\n"
            f"{_format_knowledge_context(rag_decision.context_chunks)}"
        )
    elif source_path == "search" and search_execution.used and search_execution.bundles:
        system_sections.append(build_search_context_block(search_execution.bundles))
        if not search_execution_allows_exact_claims(search_execution):
            system_sections.append(
                "Search evidence is not strong enough for precise current facts. Answer cautiously and do not state exact prices, dates, versions, or live-state claims as certain."
            )
        if any(bundle.agreement_status == "disagree" for bundle in search_execution.bundles):
            system_sections.append(
                "Trusted sources disagree. Explicitly acknowledge mixed reports and avoid merging incompatible details into one exact answer."
            )
        if any(bundle.response_mode == "uncertain" for bundle in search_execution.bundles):
            system_sections.append(
                "If the evidence is too weak, say that current reports are insufficient instead of inferring missing details."
            )
    elif source_path == "general":
        system_sections.append(
            "No accepted live-search or RAG grounding was available. Answer only if you are genuinely confident. If uncertain, say you do not know rather than improvising."
        )

    system_sections.append(
        "Path-specific rules:\n"
        "- search: use only live search context for current facts.\n"
        "- rag: use only accepted knowledge context for lore and stable repository knowledge.\n"
        "- memory: use memory only for prior conversation details.\n"
        "- general: answer conservatively and allow explicit uncertainty."
    )
    return "\n\n".join(system_sections)


def _scope_ids(msg) -> tuple[str, str, str]:
    server_id = str(msg.guild.id) if msg.guild else "dm"
    channel_id = str(msg.channel.id)
    user_id = str(msg.author.id)
    return server_id, channel_id, user_id


def _clean_user_content(content: str, bot_user_id: int) -> str:
    return content.replace(f"<@{bot_user_id}>", "").strip()


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
        chat_history = get_chat(server_id, channel_id)
        query_type = _classify_query(user_content)

        async with msg.channel.typing():
            route_plan = await _build_route_plan(user_content, chat_history)
            search_execution = SearchExecution(
                used=False,
                reason="search_not_needed",
                query="",
                provider="disabled",
                result_count=0,
                duration=0.0,
                error=None,
                bundles=[],
            )
            rag_decision: RagDecision | None = None
            final_path = route_plan.path
            if final_path == "general":
                final_path = "general-knowledge"

            if route_plan.path == "datetime":
                reply_content = _build_datetime_response(user_content)
                response = {
                    "model": "local-clock",
                    "message": {"content": reply_content},
                    "prompt_eval_count": 0,
                    "eval_count": 0,
                    "prompt_eval_duration": 0,
                    "eval_duration": 0,
                }
                elapsed = time.time() - start_time
                log_response(
                    msg,
                    user_content,
                    response["model"],
                    response,
                    elapsed,
                    query_type=query_type,
                    memory_scanned=memory_scanned,
                    memory_selected=memory_selected,
                    memory_top_score=memory_top_score,
                    memory_duration=memory_duration,
                    search_used=False,
                    search_reason="search_not_needed",
                    search_provider=search_execution.provider,
                    deterministic_gate=route_plan.deterministic_gate,
                    analysis_used=False,
                    final_path="local-datetime",
                    rag_top_score=0.0,
                    rag_accepted=False,
                )
                store_chat(server_id, channel_id, msg.content, "user")
                store_chat(server_id, channel_id, reply_content, "assistant")
                await msg.reply(reply_content)
                return

            if route_plan.path == "memory" and memory_service is not None:
                memory_start = time.time()
                try:
                    relevant_memories, memory_scanned = (
                        memory_service.retrieve_relevant_with_metrics(
                            query=route_plan.query_text,
                            server_id=server_id,
                            channel_id=channel_id,
                            user_id=user_id,
                            limit=MEMORY_RECALL_LIMIT,
                            relevance_threshold=MEMORY_RELEVANCE_THRESHOLD,
                            candidate_pool=MEMORY_CANDIDATE_POOL,
                        )
                    )
                except Exception as exc:
                    print(f"⚠️ Memory retrieval failed: {exc}")
                    relevant_memories = []
                    memory_scanned = 0
                memory_duration = time.time() - memory_start
                memory_selected = len(relevant_memories)
                if relevant_memories:
                    memory_top_score = relevant_memories[0].score

            if route_plan.path == "rag":
                rag_start = time.time()
                rag_decision = _evaluate_rag(
                    route_plan.query_text,
                    question_type=route_plan.question_type_hint,
                    user_content=user_content,
                )
                rag_duration = time.time() - rag_start
                if rag_decision.accepted:
                    final_path = "rag-grounded"
                else:
                    analysis = route_plan.analysis_decision
                    if (
                        analysis is not None
                        and analysis.can_answer_from_general_knowledge
                        and analysis.general_knowledge_confidence
                        >= GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD
                    ):
                        final_path = "general-knowledge"
                    else:
                        reply_content = _build_uncertainty_response()
                        response = {
                            "model": "uncertainty-guard",
                            "message": {"content": reply_content},
                            "prompt_eval_count": 0,
                            "eval_count": 0,
                            "prompt_eval_duration": 0,
                            "eval_duration": 0,
                        }
                        elapsed = time.time() - start_time
                        log_response(
                            msg,
                            user_content,
                            response["model"],
                            response,
                            elapsed,
                            rag_duration=rag_duration,
                            query_type=query_type,
                            memory_scanned=memory_scanned,
                            memory_selected=memory_selected,
                            memory_top_score=memory_top_score,
                            memory_duration=memory_duration,
                            search_used=False,
                            search_reason="search_not_needed",
                            search_provider=search_execution.provider,
                            deterministic_gate=route_plan.deterministic_gate,
                            analysis_used=route_plan.analysis_used,
                            analysis_rag_query=analysis.rag_query
                            if analysis
                            else route_plan.query_text,
                            can_answer_from_general_knowledge=(
                                analysis.can_answer_from_general_knowledge if analysis else False
                            ),
                            general_knowledge_confidence=(
                                analysis.general_knowledge_confidence if analysis else 0.0
                            ),
                            analysis_reason=analysis.reason if analysis else route_plan.reason,
                            final_path="uncertain",
                            rag_top_score=rag_decision.top_score,
                            rag_accepted=False,
                            rag_rejection_reason=rag_decision.rejection_reason,
                            analysis_payload=route_plan.analysis_payload,
                        )
                        await msg.reply(reply_content)
                        return
            else:
                rag_duration = 0.0
                analysis = route_plan.analysis_decision
                general_safe = (
                    analysis is not None
                    and analysis.can_answer_from_general_knowledge
                    and analysis.general_knowledge_confidence
                    >= GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD
                )
                if analysis is not None and not general_safe:
                    reply_content = _build_uncertainty_response()
                    response = {
                        "model": "uncertainty-guard",
                        "message": {"content": reply_content},
                        "prompt_eval_count": 0,
                        "eval_count": 0,
                        "prompt_eval_duration": 0,
                        "eval_duration": 0,
                    }
                    elapsed = time.time() - start_time
                    log_response(
                        msg,
                        user_content,
                        response["model"],
                        response,
                        elapsed,
                        rag_duration=rag_duration,
                        query_type=query_type,
                        memory_scanned=memory_scanned,
                        memory_selected=memory_selected,
                        memory_top_score=memory_top_score,
                        memory_duration=memory_duration,
                        search_used=False,
                        search_reason="search_not_needed",
                        search_provider=search_execution.provider,
                        deterministic_gate=route_plan.deterministic_gate,
                        analysis_used=route_plan.analysis_used,
                        analysis_rag_query=analysis.rag_query or route_plan.query_text,
                        can_answer_from_general_knowledge=analysis.can_answer_from_general_knowledge,
                        general_knowledge_confidence=analysis.general_knowledge_confidence,
                        analysis_reason=analysis.reason,
                        final_path="uncertain",
                        rag_top_score=0.0,
                        rag_accepted=False,
                        rag_rejection_reason="",
                        analysis_payload=route_plan.analysis_payload,
                    )
                    await msg.reply(reply_content)
                    return

            if route_plan.path != "rag":
                rag_duration = 0.0

            personalization = rag.get_personalization_context()
            manifest = rag.get_manifest()
            resolved_query = route_plan.query_text or user_content
            full_system_prompt = _build_system_prompt(
                source_path="memory"
                if route_plan.path == "memory"
                else ("rag" if final_path == "rag-grounded" else "general"),
                personalization=personalization,
                manifest=manifest,
                resolved_query=resolved_query,
                relevant_memories=relevant_memories,
                rag_decision=rag_decision,
                search_execution=search_execution,
            )

            messages = [{"role": "system", "content": full_system_prompt}] + chat_history
            store_chat(server_id, channel_id, msg.content, "user")
            messages.append({"role": "user", "content": user_content})

            llm_start = time.time()
            response = await llm_client.chat(messages)
            llm_duration = time.time() - llm_start
            elapsed = time.time() - start_time

            analysis = route_plan.analysis_decision
            log_response(
                msg,
                user_content,
                response.get("model") or llm_client.model or "unknown",
                response,
                elapsed,
                rag_duration=rag_duration,
                llm_duration=llm_duration,
                query_type=query_type,
                memory_scanned=memory_scanned,
                memory_selected=memory_selected,
                memory_top_score=memory_top_score,
                memory_duration=memory_duration,
                search_used=search_execution.used,
                search_reason=search_execution.reason,
                search_query=search_execution.query,
                search_provider=search_execution.provider,
                search_result_count=search_execution.result_count,
                search_results=serialize_search_results(search_execution),
                search_duration=search_execution.duration,
                search_error=search_execution.error,
                search_evidence_summary=serialize_search_evidence_summary(search_execution),
                exact_claims_allowed=search_execution_allows_exact_claims(search_execution),
                deterministic_gate=route_plan.deterministic_gate,
                analysis_used=route_plan.analysis_used,
                analysis_rag_query=analysis.rag_query if analysis else resolved_query,
                can_answer_from_general_knowledge=analysis.can_answer_from_general_knowledge
                if analysis
                else False,
                general_knowledge_confidence=analysis.general_knowledge_confidence
                if analysis
                else 0.0,
                analysis_reason=analysis.reason if analysis else route_plan.reason,
                final_path=final_path,
                rag_top_score=rag_decision.top_score if rag_decision else 0.0,
                rag_accepted=rag_decision.accepted if rag_decision else False,
                rag_rejection_reason=rag_decision.rejection_reason if rag_decision else "",
                analysis_payload=route_plan.analysis_payload,
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
    chunks: list[str] = []
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
