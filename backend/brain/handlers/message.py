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
    ROUTER_MAX_QUERY_CHARS,
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
from services.search import SearchBundle, SearchError, SearchProvider, build_search_provider
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
_PUNCTUATION_TRIM_RE = re.compile(r"^[\s\"'`]+|[\s\"'`?!.,:;]+$")
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
class SearchExecution:
    used: bool
    reason: str
    query: str
    provider: str
    result_count: int
    duration: float
    error: str | None
    bundles: list[SearchBundle] | None = None


@dataclass(slots=True)
class SearchQueryPlan:
    label: str
    query: str
    purpose: str = ""
    target_entity: str = ""
    requested_fact: str = ""
    question_type: str = ""
    freshness_required: bool = False
    subject_domain: str = ""
    confidence: float = 0.0


@dataclass(slots=True)
class AnalysisDecision:
    time_sensitive: bool
    search_query: str
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
    search_plans: list[SearchQueryPlan] | None = None
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


def _normalize_query_text(text: str, *, max_chars: int | None = None) -> str:
    normalized = " ".join(text.strip().split())
    normalized = _PUNCTUATION_TRIM_RE.sub("", normalized)
    if max_chars is not None:
        normalized = normalized[:max_chars].rstrip()
    return normalized


def _rewrite_search_query(query: str) -> str:
    normalized = _normalize_query_text(query, max_chars=ROUTER_MAX_QUERY_CHARS)
    lowered = normalized.lower()
    for prefix in ("search for ", "search ", "look up ", "find ", "check "):
        if lowered.startswith(prefix):
            lowered = lowered[len(prefix) :].strip()
    return lowered or normalized


def _infer_target_entity(text: str) -> str:
    normalized = _normalize_query_text(text)
    lowered = normalized.lower()
    if "wuthering waves" in lowered:
        return "Wuthering Waves"
    if "genshin impact" in lowered:
        return "Genshin Impact"
    if "nvidia" in lowered:
        return "NVIDIA"
    if "tesla" in lowered:
        return "Tesla"
    if "shorekeeper" in lowered:
        return "Shorekeeper"
    return ""


def _infer_requested_fact(text: str) -> str:
    lowered = _normalize_query_text(text).lower()
    if any(term in lowered for term in ("stock price", "share price", "stock pricing", "price per share")):
        return "price per share"
    if any(term in lowered for term in ("latest version", "current version", "latest patch", "latest update")):
        return "latest version"
    if "banner" in lowered:
        return "current banners"
    if any(term in lowered for term in ("your name", "what is your name", "whats your name", "who are you")):
        return "identity"
    if any(term in lowered for term in ("meaning of", "what does", "definition")):
        return "definition"
    if any(term in lowered for term in ("news", "what happened", "event", "status")):
        return "status update"
    return ""


def _infer_question_type(*, requested_fact: str, time_sensitive: bool, text: str = "") -> str:
    lowered = _normalize_query_text(text).lower()
    if requested_fact == "price per share":
        return "current_metric"
    if requested_fact == "latest version":
        return "latest_release"
    if requested_fact == "current banners":
        return "current_availability"
    if requested_fact == "identity":
        return "identity"
    if requested_fact == "definition":
        return "definition"
    if requested_fact == "status update":
        return "event_status"
    if any(term in lowered for term in ("tell me about", "who is", "what is black shores", "shorekeeper lore", "story of")):
        return "background_fact"
    return "generic" if time_sensitive else "background_fact"


def _infer_subject_domain(text: str) -> str:
    lowered = _normalize_query_text(text).lower()
    if any(term in lowered for term in ("stock", "share price", "price per share", "market")):
        return "finance"
    if any(term in lowered for term in ("wuthering waves", "genshin impact")):
        return "game"
    if any(term in lowered for term in ("meaning", "definition", "word")):
        return "language"
    if any(term in lowered for term in ("your name", "who are you")):
        return "identity"
    return "general"


def _rag_is_eligible(question_type: str, user_content: str, rag_query: str) -> bool:
    lowered = _normalize_query_text(f"{user_content} {rag_query}").lower()
    if question_type in {"definition", "identity", "current_metric", "latest_release", "current_availability", "event_status"}:
        return False
    if any(term in lowered for term in ("meaning of", "what does", "define", "dictionary", "your name", "who are you")):
        return False
    if any(term in lowered for term in ("tell me about", "lore", "story", "black shores", "resonator", "faction")):
        return True
    return question_type in {"background_fact"}


def _extract_recent_user_queries(chat_history: list[dict], *, limit: int | None = None) -> list[str]:
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
    lowered = _normalize_query_text(query).lower()
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
    prefix = SEARCH_EXPLICIT_PREFIX.strip()
    lowered = cleaned.lower()

    if prefix and lowered.startswith(prefix.lower()):
        if not SEARCH_ENABLED:
            return RoutePlan(
                path="general",
                query_type="general",
                query_text=cleaned,
                reason="search_disabled",
                deterministic_gate="explicit_search_disabled",
            )
        stripped_query = _normalize_query_text(cleaned[len(prefix) :], max_chars=ROUTER_MAX_QUERY_CHARS)
        if len(stripped_query) < SEARCH_MIN_QUERY_LENGTH:
            return RoutePlan(
                path="general",
                query_type="general",
                query_text=cleaned,
                reason="search_explicit_too_short",
                deterministic_gate="explicit_search_short",
            )
        return RoutePlan(
            path="search",
            query_type="general",
            query_text=stripped_query,
            reason="search_explicit",
            deterministic_gate="explicit_search",
            search_plans=[
                SearchQueryPlan(
                    label="explicit",
                    query=stripped_query,
                    purpose="user-controlled explicit search",
                    target_entity=_infer_target_entity(stripped_query),
                    requested_fact=_infer_requested_fact(stripped_query),
                    question_type=_infer_question_type(
                        requested_fact=_infer_requested_fact(stripped_query),
                        time_sensitive=True,
                        text=stripped_query,
                    ),
                    freshness_required=True,
                    subject_domain=_infer_subject_domain(stripped_query),
                    confidence=1.0,
                )
            ],
            target_entity=_infer_target_entity(stripped_query),
            requested_fact=_infer_requested_fact(stripped_query),
            question_type_hint=_infer_question_type(
                requested_fact=_infer_requested_fact(stripped_query),
                time_sensitive=True,
                text=stripped_query,
            ),
            subject_domain=_infer_subject_domain(stripped_query),
        )

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
    history_lines = [f"{index}. {query}" for index, query in enumerate(reversed(recent_user_queries), start=1)]
    history_block = "\n".join(history_lines) if history_lines else "None"
    system_prompt = (
        "You are a routing and query-analysis component for a Discord bot. "
        "Do not roleplay. Do not answer the user. Return strict JSON only.\n"
        "Available knowledge sources:\n"
        "- local datetime for date/time questions\n"
        "- local RAG knowledge base for stable in-repo knowledge and lore\n"
        "- web search for current, latest, live, ongoing, external, changing, or real-world factual questions\n"
        "- general model knowledge only for stable non-time-sensitive questions when safe\n"
        "Return JSON with keys: time_sensitive, search_query, rag_query, can_answer_from_general_knowledge, general_knowledge_confidence, reason.\n"
        "Rules:\n"
        "- If the question is current/latest/live/price/news/update/event status, set time_sensitive=true.\n"
        "- Do not assume Wuthering Waves automatically means RAG-only.\n"
        "- Do not treat current/latest/live/price/news/update questions as stable.\n"
        "- Use recent user turns only to resolve elliptical follow-ups.\n"
        "- Reconstruct a standalone search_query when time_sensitive=true.\n"
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
    normalized = _normalize_query_text(user_content, max_chars=ROUTER_MAX_QUERY_CHARS)
    time_sensitive = any(
        term in normalized.lower()
        for term in ("current", "latest", "live", "today", "price", "stock", "news", "update")
    )
    search_query = _rewrite_search_query(normalized)
    if _looks_elliptical_followup(normalized) and recent_user_queries:
        search_query = f"{search_query} {_normalize_query_text(recent_user_queries[0]).lower()}".strip()
    return AnalysisDecision(
        time_sensitive=time_sensitive,
        search_query=search_query,
        rag_query=normalized or user_content,
        can_answer_from_general_knowledge=False,
        general_knowledge_confidence=0.0,
        reason="analysis_fallback",
        raw_payload={"fallback": True},
    )


def _validate_analysis_decision(payload: dict[str, Any]) -> AnalysisDecision | None:
    time_sensitive = payload.get("time_sensitive")
    search_query = payload.get("search_query", "")
    rag_query = payload.get("rag_query", "")
    can_answer_from_general_knowledge = payload.get("can_answer_from_general_knowledge", False)
    general_knowledge_confidence = payload.get("general_knowledge_confidence", 0.0)
    reason = payload.get("reason", "")

    if not isinstance(time_sensitive, bool):
        return None
    if not isinstance(search_query, str) or not isinstance(rag_query, str) or not isinstance(reason, str):
        return None
    if not isinstance(can_answer_from_general_knowledge, bool):
        return None

    normalized_search_query = _normalize_query_text(search_query, max_chars=ROUTER_MAX_QUERY_CHARS)
    normalized_rag_query = _normalize_query_text(rag_query, max_chars=ROUTER_MAX_QUERY_CHARS)
    normalized_reason = " ".join(reason.strip().split())[:200]

    try:
        normalized_general_confidence = max(0.0, min(float(general_knowledge_confidence), 1.0))
    except Exception:
        normalized_general_confidence = 0.0

    if time_sensitive and len(normalized_search_query) < SEARCH_MIN_QUERY_LENGTH:
        return None
    if not normalized_rag_query:
        return None

    return AnalysisDecision(
        time_sensitive=time_sensitive,
        search_query=normalized_search_query,
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
        response = await asyncio.wait_for(llm_client.chat(messages), timeout=ANALYSIS_TIMEOUT_SECONDS)
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
    if analysis.time_sensitive:
        query_text = analysis.rag_query or user_content
        search_plan = _build_search_plan(
            analysis.search_query,
            label="primary",
            purpose="analysis-reconstructed search query",
        )
        requested_fact = _infer_requested_fact(query_text)
        question_type = _infer_question_type(
            requested_fact=requested_fact,
            time_sensitive=False,
            text=query_text,
        )
        return RoutePlan(
            path="general",
            query_type="general",
            query_text=query_text,
            reason=analysis.reason,
            analysis_used=True,
            analysis_payload=analysis.raw_payload,
            analysis_decision=analysis,
            search_plans=[search_plan] if search_plan is not None else None,
            target_entity=_infer_target_entity(query_text),
            requested_fact=requested_fact,
            question_type_hint=question_type,
            subject_domain=_infer_subject_domain(query_text),
        )

    requested_fact = _infer_requested_fact(analysis.rag_query or user_content)
    question_type = _infer_question_type(
        requested_fact=requested_fact,
        time_sensitive=False,
        text=analysis.rag_query or user_content,
    )
    return RoutePlan(
        path="rag" if _rag_is_eligible(question_type, user_content, analysis.rag_query) else "general",
        query_type="general",
        query_text=analysis.rag_query,
        reason=analysis.reason,
        analysis_used=True,
        analysis_payload=analysis.raw_payload,
        analysis_decision=analysis,
        target_entity=_infer_target_entity(analysis.rag_query or user_content),
        requested_fact=requested_fact,
        question_type_hint=question_type,
        subject_domain=_infer_subject_domain(analysis.rag_query or user_content),
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


def _build_search_disabled_response() -> str:
    return "Live search is currently disabled in my records, so I cannot look that up for you right now."


def _build_search_plan(query: str, *, label: str, purpose: str) -> SearchQueryPlan | None:
    normalized_query = _normalize_query_text(query, max_chars=ROUTER_MAX_QUERY_CHARS)
    if len(normalized_query) < SEARCH_MIN_QUERY_LENGTH:
        return None
    requested_fact = _infer_requested_fact(normalized_query)
    return SearchQueryPlan(
        label=label,
        query=normalized_query,
        purpose=purpose,
        target_entity=_infer_target_entity(normalized_query),
        requested_fact=requested_fact,
        question_type=_infer_question_type(
            requested_fact=requested_fact,
            time_sensitive=True,
            text=normalized_query,
        ),
        freshness_required=True,
        subject_domain=_infer_subject_domain(normalized_query),
        confidence=1.0,
    )


async def _execute_search_plans(plans: list[SearchQueryPlan], *, reason: str) -> SearchExecution:
    provider_name = SEARCH_PROVIDER if search_provider is not None else "disabled"
    if search_provider is None or not plans:
        return SearchExecution(
            used=False,
            reason=reason if plans else "search_not_needed",
            query="",
            provider=provider_name,
            result_count=0,
            duration=0.0,
            error=None,
            bundles=[],
        )

    start = time.time()
    bundles: list[SearchBundle] = []
    errors: list[str] = []
    for plan in plans:
        try:
            bundle = await search_provider.search(
                plan.query,
                SEARCH_MAX_RESULTS,
                target_entity=plan.target_entity,
                requested_fact=plan.requested_fact,
                question_type=plan.question_type,
                freshness_required=plan.freshness_required,
                topic=plan.subject_domain,
                label=plan.label,
            )
        except SearchError as exc:
            errors.append(str(exc))
            continue
        except Exception as exc:
            errors.append(f"Unexpected search error: {exc}")
            continue
        if bundle.results:
            bundles.append(bundle)
            break
        errors.append("Search returned no results")

    duration = time.time() - start
    query_summary = " | ".join(plan.query for plan in plans)
    if not bundles:
        return SearchExecution(
            used=False,
            reason="search_failed_continue_without_results",
            query=query_summary,
            provider=provider_name,
            result_count=0,
            duration=duration,
            error="; ".join(errors) if errors else "Search returned no results",
            bundles=[],
        )
    return SearchExecution(
        used=True,
        reason=reason,
        query=bundles[0].query,
        provider=bundles[0].provider,
        result_count=len(bundles[0].results),
        duration=duration,
        error="; ".join(errors) if errors else None,
        bundles=bundles,
    )


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
            token in _normalize_query_text(chunks[0].get("text", "")).lower()
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
    return {token for token in re.findall(r"[a-z0-9]+", text.lower()) if len(token) > 3 and token not in stopwords}


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


def _format_search_context(bundles: list[SearchBundle]) -> str:
    sections = [
        "=== LIVE SEARCH RESULTS ===",
        "Use these grouped results only for current or time-sensitive facts.",
    ]
    for bundle in bundles:
        sections.append(
            f"--- Search Group: {bundle.label or 'general'} ---\n"
            f"Standalone query: {bundle.query}\n"
            f"Evidence confidence: {bundle.confidence_summary}\n"
            f"Exact claims allowed: {bundle.exact_claim_allowed}\n"
            f"Agreement status: {bundle.agreement_status}\n"
            f"Exact claim reason: {bundle.exact_claim_reason}\n"
            f"Response mode: {bundle.response_mode}\n"
            f"Evidence summary: {bundle.evidence_summary}"
        )
        for index, result in enumerate(bundle.results, start=1):
            sections.append(
                f"[Result {index}]\n"
                f"Title: {result.title}\n"
                f"Source: {result.source}\n"
                f"URL: {result.url}\n"
                f"Trust: {result.source_class} | Surface: {result.surface_class} | Freshness: {result.freshness_bucket}\n"
                f"Rank reason: {result.rank_reason}\n"
                f"Penalties: stale={result.stale_penalty_applied} preview={result.preview_penalty_applied} agreement={result.agreement_participant}\n"
                f"Evidence: quality={result.evidence_quality} exact={result.supports_exact_answer}\n"
                f"Snippet: {result.snippet}"
            )
    sections.append(
        "Instructions:\n"
        "- Use live search results only for fresh or external facts.\n"
        "- If exact claims are not allowed, avoid precise numeric/date/current claims.\n"
        "- If evidence is weak or conflicting, answer cautiously and acknowledge uncertainty.\n"
        "- Do not mention citations or URLs unless the user explicitly asks for sources."
    )
    return "\n\n".join(sections)


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
    system_sections = [SYSTEM_PROMPT, f"=== PERSONALITY & BACKSTORY ===\n{personalization}", manifest]
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
        system_sections.append(_format_search_context(search_execution.bundles))
        if not _search_execution_exact_claims_allowed(search_execution):
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


def _flatten_search_results(search_execution: SearchExecution) -> list[dict[str, str]] | None:
    if not search_execution.bundles:
        return None
    flattened: list[dict[str, str]] = []
    for bundle in search_execution.bundles:
        for result in bundle.results:
            flattened.append(
                {
                    "title": result.title,
                    "source": result.source,
                    "url": result.url,
                    "published_at": result.published_at or "",
                    "snippet": result.snippet,
                    "source_class": result.source_class,
                    "surface_class": result.surface_class,
                    "freshness_bucket": result.freshness_bucket,
                    "rank_reason": result.rank_reason,
                    "evidence_quality": result.evidence_quality,
                    "stale_penalty_applied": str(result.stale_penalty_applied),
                    "preview_penalty_applied": str(result.preview_penalty_applied),
                    "agreement_participant": str(result.agreement_participant),
                    "supports_exact_answer": str(result.supports_exact_answer),
                    "label": bundle.label,
                    "query": bundle.query,
                    "bundle_confidence": bundle.confidence_summary,
                    "bundle_exact_claim_allowed": str(bundle.exact_claim_allowed),
                }
            )
    return flattened


def _flatten_search_evidence_summary(search_execution: SearchExecution) -> list[dict[str, str]] | None:
    if not search_execution.bundles:
        return None
    return [
        {
            "label": bundle.label,
            "confidence_summary": bundle.confidence_summary,
            "exact_claim_allowed": str(bundle.exact_claim_allowed),
            "evidence_summary": bundle.evidence_summary,
            "agreement_status": bundle.agreement_status,
            "trusted_result_count": str(bundle.trusted_result_count),
            "fallback_result_count": str(bundle.fallback_result_count),
            "exact_claim_reason": bundle.exact_claim_reason,
            "response_mode": bundle.response_mode,
        }
        for bundle in search_execution.bundles
    ]


def _search_execution_exact_claims_allowed(search_execution: SearchExecution) -> bool:
    if not search_execution.bundles:
        return False
    return all(bundle.exact_claim_allowed for bundle in search_execution.bundles)


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
    is_reply_to_bot = msg.reference and msg.reference.resolved and msg.reference.resolved.author == bot.user
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
                provider=SEARCH_PROVIDER if search_provider is not None else "disabled",
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

            if route_plan.deterministic_gate == "explicit_search_disabled":
                reply_content = _build_search_disabled_response()
                response = {
                    "model": "search-disabled",
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
                    search_reason="search_disabled",
                    search_provider=search_execution.provider,
                    deterministic_gate=route_plan.deterministic_gate,
                    analysis_used=False,
                    final_path="search-disabled",
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
                    relevant_memories, memory_scanned = memory_service.retrieve_relevant_with_metrics(
                        query=route_plan.query_text,
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

            if route_plan.path == "search":
                search_execution = await _execute_search_plans(
                    route_plan.search_plans or [],
                    reason="search_explicit" if route_plan.deterministic_gate == "explicit_search" else "analysis_time_sensitive",
                )
                final_path = "explicit-search" if route_plan.deterministic_gate == "explicit_search" else "search-grounded"
            elif route_plan.path == "rag":
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
                        and analysis.general_knowledge_confidence >= GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD
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
                            analysis_time_sensitive=analysis.time_sensitive if analysis else None,
                            analysis_search_query=analysis.search_query if analysis else "",
                            analysis_rag_query=analysis.rag_query if analysis else route_plan.query_text,
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
                auto_search_enabled = SEARCH_TRIGGER_MODE not in {"explicit", "manual", "off", "disabled"}
                general_safe = (
                    analysis is not None
                    and analysis.can_answer_from_general_knowledge
                    and analysis.general_knowledge_confidence >= GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD
                )
                if analysis is not None and analysis.time_sensitive and auto_search_enabled and not general_safe:
                    search_execution = await _execute_search_plans(
                        route_plan.search_plans or [],
                        reason="analysis_time_sensitive_fallback",
                    )
                    if search_execution.used:
                        final_path = "search-grounded"
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
                            search_used=search_execution.used,
                            search_reason=search_execution.reason,
                            search_query=search_execution.query,
                            search_provider=search_execution.provider,
                            search_result_count=search_execution.result_count,
                            search_results=_flatten_search_results(search_execution),
                            search_duration=search_execution.duration,
                            search_error=search_execution.error,
                            search_query_plans=(
                                [{"label": plan.label, "query": plan.query, "purpose": plan.purpose} for plan in (route_plan.search_plans or [])]
                                or None
                            ),
                            search_evidence_summary=_flatten_search_evidence_summary(search_execution),
                            exact_claims_allowed=_search_execution_exact_claims_allowed(search_execution),
                            deterministic_gate=route_plan.deterministic_gate,
                            analysis_used=route_plan.analysis_used,
                            analysis_time_sensitive=analysis.time_sensitive,
                            analysis_search_query=analysis.search_query,
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
                elif analysis is not None and not general_safe:
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
                        analysis_time_sensitive=analysis.time_sensitive,
                        analysis_search_query=analysis.search_query,
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
                source_path="memory" if route_plan.path == "memory" else (
                    "search" if final_path in {"search-grounded", "explicit-search"} else (
                        "rag" if final_path == "rag-grounded" else "general"
                    )
                ),
                personalization=personalization,
                manifest=manifest,
                resolved_query=resolved_query,
                relevant_memories=relevant_memories,
                rag_decision=rag_decision,
                search_execution=search_execution,
            )
            if (
                final_path == "search-grounded"
                and search_execution.bundles
                and all(bundle.response_mode == "uncertain" for bundle in search_execution.bundles)
            ):
                reply_content = "Current reports are too mixed or weak for me to state that confidently. I would rather leave it uncertain than offer you a false exact answer."
                response = {
                    "model": "uncertainty-guard",
                    "message": {"content": reply_content},
                    "prompt_eval_count": 0,
                    "eval_count": 0,
                    "prompt_eval_duration": 0,
                    "eval_duration": 0,
                }
                elapsed = time.time() - start_time
                analysis = route_plan.analysis_decision
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
                    search_used=search_execution.used,
                    search_reason=search_execution.reason,
                    search_query=search_execution.query,
                    search_provider=search_execution.provider,
                    search_result_count=search_execution.result_count,
                    search_results=_flatten_search_results(search_execution),
                    search_duration=search_execution.duration,
                    search_error=search_execution.error,
                    search_query_plans=(
                        [{"label": plan.label, "query": plan.query, "purpose": plan.purpose} for plan in (route_plan.search_plans or [])]
                        or None
                    ),
                    search_evidence_summary=_flatten_search_evidence_summary(search_execution),
                    exact_claims_allowed=_search_execution_exact_claims_allowed(search_execution),
                    deterministic_gate=route_plan.deterministic_gate,
                    analysis_used=route_plan.analysis_used,
                    analysis_time_sensitive=analysis.time_sensitive if analysis else None,
                    analysis_search_query=analysis.search_query if analysis else "",
                    analysis_rag_query=analysis.rag_query if analysis else resolved_query,
                    can_answer_from_general_knowledge=analysis.can_answer_from_general_knowledge if analysis else False,
                    general_knowledge_confidence=analysis.general_knowledge_confidence if analysis else 0.0,
                    analysis_reason=analysis.reason if analysis else route_plan.reason,
                    final_path="uncertain",
                    rag_top_score=rag_decision.top_score if rag_decision else 0.0,
                    rag_accepted=rag_decision.accepted if rag_decision else False,
                    rag_rejection_reason=rag_decision.rejection_reason if rag_decision else "",
                    analysis_payload=route_plan.analysis_payload,
                )
                await msg.reply(reply_content)
                return

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
                search_results=_flatten_search_results(search_execution),
                search_duration=search_execution.duration,
                search_error=search_execution.error,
                search_query_plans=(
                    [
                        {
                            "label": plan.label,
                            "query": plan.query,
                            "purpose": plan.purpose,
                        }
                        for plan in (route_plan.search_plans or [])
                    ]
                    or None
                ),
                search_evidence_summary=_flatten_search_evidence_summary(search_execution),
                exact_claims_allowed=_search_execution_exact_claims_allowed(search_execution),
                deterministic_gate=route_plan.deterministic_gate,
                analysis_used=route_plan.analysis_used,
                analysis_time_sensitive=analysis.time_sensitive if analysis else None,
                analysis_search_query=analysis.search_query if analysis else "",
                analysis_rag_query=analysis.rag_query if analysis else resolved_query,
                can_answer_from_general_knowledge=analysis.can_answer_from_general_knowledge if analysis else False,
                general_knowledge_confidence=analysis.general_knowledge_confidence if analysis else 0.0,
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
