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
    MEMORY_COMPACTION_ENABLED,
    MEMORY_COMPACTION_TIMEOUT_SECONDS,
    MEMORY_DB_PATH,
    MEMORY_SHORT_TERM_TURN_LIMIT,
    RAG_ANSWER_SCORE_THRESHOLD,
    ROUTER_HISTORY_TURNS,
    SYSTEM_PROMPT,
)
from handlers.conversation_context import (
    format_chat_for_llm,
    get_chat,
    is_compacting,
    mark_compacting,
    snapshot_and_clear,
    store_turn,
    unmark_compacting,
)
from services.llm import LLMClient
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
from services.user_memory import (
    UserMemoryRepository,
    build_compaction_messages,
    parse_compaction_response,
)
from utils.logger import log_response

rag = RAG()
llm_client = LLMClient()


def _resolve_memory_db_path() -> str:
    if MEMORY_DB_PATH.startswith(("postgresql://", "postgres://")):
        return MEMORY_DB_PATH
    if Path(MEMORY_DB_PATH).is_absolute():
        return MEMORY_DB_PATH
    project_root = Path(__file__).resolve().parents[3]
    return str((project_root / MEMORY_DB_PATH).resolve())


user_memory_repo: UserMemoryRepository | None = None
if MEMORY_COMPACTION_ENABLED:
    try:
        user_memory_repo = UserMemoryRepository(db_path=_resolve_memory_db_path())
    except Exception as exc:
        print(f"⚠️ User memory repository initialization failed: {exc}")
        user_memory_repo = None

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
    reason: str
    query_type: str = "general"
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
        role = message.get("role")
        if role != "user":
            continue
        content = message.get("content", "")
        if isinstance(content, str) and content.strip():
            cleaned = _DISCORD_MENTION_RE.sub("", content).strip()
            if cleaned:
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


def _build_analysis_messages(
    user_content: str, recent_user_queries: list[str], *, user_context_str: str = ""
) -> list[dict]:
    history_lines = [
        f"{index}. {query}" for index, query in enumerate(reversed(recent_user_queries), start=1)
    ]
    history_block = "\n".join(history_lines) if history_lines else "None"
    context_note = (
        f" The current user is identified as: {user_context_str}." if user_context_str else ""
    )
    system_prompt = (
        "You are a routing and query-analysis component for a Discord bot. "
        "Do not roleplay. Do not answer the user. Return strict JSON only.\n"
        "Return JSON with keys: rag_query, reason, query_type.\n"
        "query_type must be one of: datetime, casual, meta, memory, general.\n"
        "Rules:\n"
        "- Use recent user turns only to resolve elliptical follow-ups.\n"
        "- Always provide a standalone rag_query.\n"
        "- datetime: the user is asking about the current date, time, day, month, or year.\n"
        '- casual: greeting, small talk, simple social exchange (e.g. "hello", "how are you").\n'
        "- meta: the user is referencing past conversation or asking about the bot itself.\n"
        "- memory: the user is asking about someone's identity or what you remember about them — could be themselves or another Discord user.\n"
        "- general: everything else — questions about lore, characters, abilities, facts, etc."
        f"{context_note}"
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
        reason="analysis_fallback",
        raw_payload={"fallback": True},
    )


def _validate_analysis_decision(payload: dict[str, Any]) -> AnalysisDecision | None:
    rag_query = payload.get("rag_query", "")
    reason = payload.get("reason", "")
    query_type = payload.get("query_type", "general")

    if not isinstance(rag_query, str) or not isinstance(reason, str):
        return None

    normalized_rag_query = normalize_search_query(rag_query)
    normalized_reason = " ".join(reason.strip().split())[:200]

    if not normalized_rag_query:
        return None

    valid_types = {"datetime", "casual", "meta", "memory", "general"}
    if not isinstance(query_type, str) or query_type not in valid_types:
        query_type = "general"

    return AnalysisDecision(
        rag_query=normalized_rag_query,
        reason=normalized_reason,
        query_type=query_type,
        raw_payload=payload,
    )


async def _run_analysis_pass(
    user_content: str, chat_history: list[dict], *, user_context_str: str = ""
) -> AnalysisDecision:
    recent_user_queries = _extract_recent_user_queries(chat_history)
    if not ANALYSIS_ENABLED:
        return _analysis_fallback(user_content, recent_user_queries)

    messages = _build_analysis_messages(
        user_content, recent_user_queries, user_context_str=user_context_str
    )
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


async def _build_route_plan(
    user_content: str, chat_history: list[dict], *, user_context_str: str = ""
) -> RoutePlan:
    analysis = await _run_analysis_pass(
        user_content, chat_history, user_context_str=user_context_str
    )

    if analysis.query_type == "datetime":
        return RoutePlan(
            path="datetime",
            query_type="datetime",
            query_text=user_content.strip(),
            reason="datetime",
            deterministic_gate="datetime",
        )
    if analysis.query_type == "casual":
        return RoutePlan(
            path="general",
            query_type="casual",
            query_text=user_content.strip(),
            reason="casual_direct",
            deterministic_gate="casual",
        )
    if analysis.query_type == "meta":
        return RoutePlan(
            path="general",
            query_type="meta",
            query_text=user_content.strip(),
            reason="meta_direct",
            deterministic_gate="meta",
        )
    if analysis.query_type == "memory":
        return RoutePlan(
            path="memory",
            query_type="memory",
            query_text=user_content.strip(),
            reason="memory_direct",
            deterministic_gate="memory",
            use_memory=True,
            analysis_used=True if analysis.raw_payload else False,
            analysis_payload=analysis.raw_payload,
            analysis_decision=analysis,
        )

    # general or rag
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


def _format_knowledge_context(context_chunks: list[dict[str, Any]]) -> str:
    return "\n\n".join(f"[{c['source']} - {c['heading']}]\n{c['text']}" for c in context_chunks)


def _build_system_prompt(
    *,
    source_path: str,
    personalization: str,
    manifest: str,
    resolved_query: str,
    rag_decision: RagDecision | None,
    search_execution: SearchExecution,
    compacted_memory: str | None = None,
    memory_subject_name: str | None = None,
    asking_user_name: str = "",
    user_context_str: str = "",
) -> str:
    system_sections = [
        SYSTEM_PROMPT,
        f"=== PERSONALITY & BACKSTORY ===\n{personalization}",
        manifest,
    ]
    if user_context_str:
        system_sections.insert(1, f"[Current user context: {user_context_str}]")
    if compacted_memory:
        if memory_subject_name and asking_user_name:
            system_sections.append(
                "=== WHAT I REMEMBER ===\n"
                f"{compacted_memory}\n\n"
                f'NOTE: This describes another user named "{memory_subject_name}". '
                f'It does NOT describe "{asking_user_name}" who is currently speaking. '
                f"Answer {asking_user_name}'s questions about {memory_subject_name}."
            )
        else:
            system_sections.append(
                "=== WHAT I REMEMBER ===\n"
                f"{compacted_memory}\n\n"
                "Use these notes to recall their identity, interests, and past topics naturally."
            )
    system_sections.append(
        "Resolved interpretation of the current user message:\n"
        f"{resolved_query}\n"
        "Use this only to interpret the user's current intent."
    )

    if source_path == "rag" and rag_decision and rag_decision.context_chunks:
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
    elif source_path == "memory":
        system_sections.append(
            "I recalled what I remember about this user below. Use that personal context naturally without announcing the memory explicitly. "
            "Do not change your personality or pretend to have a different relationship than what the memory describes."
        )
    elif source_path == "general":
        system_sections.append(
            "No accepted live-search or RAG grounding was available. Answer only if you are genuinely confident. If uncertain, say you do not know rather than improvising."
        )

    system_sections.append(
        "Path-specific rules:\n"
        "- search: use only live search context for current facts.\n"
        "- rag: use only accepted knowledge context for lore and stable repository knowledge.\n"
        "- general: answer conservatively and allow explicit uncertainty.\n"
        "- memory: use only what I remember about you and the conversation history. Do not invent personal details."
    )
    return "\n\n".join(system_sections)


def _scope_ids(msg) -> tuple[str, str, str]:
    server_id = str(msg.guild.id) if msg.guild else "dm"
    channel_id = str(msg.channel.id)
    user_id = str(msg.author.id)
    return server_id, channel_id, user_id


def _clean_user_content(content: str, bot_user_id: int) -> str:
    return content.replace(f"<@{bot_user_id}>", "").strip()


async def _compact_memory_background(
    user_id: str,
    server_id: str,
    channel_id: str,
) -> None:
    if user_memory_repo is None:
        return
    mark_compacting(user_id, server_id)
    try:
        snapshot = snapshot_and_clear(user_id, server_id)
        if not snapshot:
            unmark_compacting(user_id, server_id)
            return
        existing = user_memory_repo.get_by_user(user_id, server_id)
        messages = build_compaction_messages(existing, snapshot)
        response = await asyncio.wait_for(
            llm_client.chat(messages),
            timeout=MEMORY_COMPACTION_TIMEOUT_SECONDS,
        )
        reply = response.get("message", {}).get("content", "")
        parsed = parse_compaction_response(reply)
        if parsed is not None:
            user_memory_repo.upsert(
                user_id=user_id,
                server_id=server_id,
                channel_id=channel_id,
                memory_content=parsed.memory_content,
                topic=parsed.topic,
                importance_score=parsed.importance_score,
                tags=",".join(parsed.tags),
                existing=existing,
            )
            new_ver = (existing.memory_version + 1) if existing else 1
            print(f"Memory compacted for user {user_id} (v{new_ver})")
        else:
            print(f"Memory compaction parse failed for {user_id}")
    except Exception as exc:
        print(f"Memory compaction failed for {user_id}: {exc}")
    finally:
        unmark_compacting(user_id, server_id)


def _maybe_compact_memory(user_id: str, server_id: str, channel_id: str) -> None:
    if not (
        MEMORY_COMPACTION_ENABLED
        and user_memory_repo is not None
        and not is_compacting(user_id, server_id)
        and len(get_chat(user_id, server_id)) >= MEMORY_SHORT_TERM_TURN_LIMIT
    ):
        return
    asyncio.create_task(_compact_memory_background(user_id, server_id, channel_id))


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
        user_display_name = getattr(msg.author, "display_name", None) or str(msg.author)
        user_content = _clean_user_content(msg.content, bot.user.id)

        start_time = time.time()
        chat_history = list(get_chat(user_id, server_id))

        # Build user context for analysis and system prompt
        user_context_str = ""
        if user_memory_repo is not None:
            record = user_memory_repo.get_by_user(user_id, server_id)
            if record is not None and record.memory_content:
                first_line = record.memory_content.split("\n")[0]
                ident = (
                    first_line.replace("Identifier: ", "").strip()
                    if first_line.startswith("Identifier: ")
                    else ""
                )
                if ident:
                    user_context_str = f"{ident} ({record.topic or 'known visitor'})"

        async with msg.channel.typing():
            route_plan = await _build_route_plan(
                user_content, chat_history, user_context_str=user_context_str
            )
            query_type = route_plan.query_type
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
                    search_used=False,
                    search_reason="search_not_needed",
                    search_provider=search_execution.provider,
                    deterministic_gate=route_plan.deterministic_gate,
                    analysis_used=False,
                    final_path="local-datetime",
                    rag_top_score=0.0,
                    rag_accepted=False,
                )
                store_turn(user_id, server_id, msg.content, "user", author=user_display_name)
                store_turn(user_id, server_id, reply_content, "assistant")
                await msg.reply(reply_content)
                return

            compacted_memory: str | None = None
            compacted_version = 0
            compacted_topic = ""
            compacted_importance = 0.0
            memory_subject_name: str | None = None
            if user_memory_repo is not None:
                record = user_memory_repo.get_by_user(user_id, server_id)
                if record is not None and record.memory_content:
                    compacted_memory = record.memory_content
                    compacted_version = record.memory_version
                    compacted_topic = record.topic
                    compacted_importance = record.importance_score

                # Cross-user matching: detect known identifiers and load cross-user memory
                all_records = user_memory_repo.get_all_by_server(server_id)
                for rec in all_records:
                    if not rec.memory_content:
                        continue
                    first_line = rec.memory_content.split("\n")[0]
                    ident = (
                        first_line.replace("Identifier: ", "").strip()
                        if first_line.startswith("Identifier: ")
                        else ""
                    )
                    if ident and ident.lower() in user_content.lower():
                        if rec.user_id != user_id:
                            compacted_memory = rec.memory_content
                            compacted_version = rec.memory_version
                            compacted_topic = rec.topic
                            compacted_importance = rec.importance_score
                            memory_subject_name = ident
                        if query_type != "memory":
                            query_type = "memory"
                            route_plan.query_type = "memory"
                            route_plan.path = "memory"
                            route_plan.deterministic_gate = "memory"
                            route_plan.use_memory = True
                        break

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
                elif compacted_memory is not None:
                    final_path = "memory-personal"
                else:
                    final_path = "general"
            else:
                rag_duration = 0.0

            if route_plan.path != "rag":
                rag_duration = 0.0

            personalization = rag.get_personalization_context()
            manifest = rag.get_manifest()
            resolved_query = route_plan.query_text or user_content
            source_path_label = (
                "memory"
                if final_path == "memory-personal"
                else ("rag" if final_path == "rag-grounded" else "general")
            )
            full_system_prompt = _build_system_prompt(
                source_path=source_path_label,
                personalization=personalization,
                manifest=manifest,
                resolved_query=resolved_query,
                rag_decision=rag_decision,
                search_execution=search_execution,
                compacted_memory=compacted_memory,
                memory_subject_name=memory_subject_name,
                asking_user_name=user_display_name or "",
                user_context_str=user_context_str,
            )

            messages = [{"role": "system", "content": full_system_prompt}] + format_chat_for_llm(
                chat_history
            )
            store_turn(user_id, server_id, msg.content, "user", author=user_display_name)
            messages.append(
                {
                    "role": "user",
                    "content": f"[{user_display_name}] {user_content}"
                    if user_display_name
                    else user_content,
                }
            )

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
                analysis_reason=analysis.reason if analysis else route_plan.reason,
                final_path=final_path,
                compacted_found=compacted_memory is not None,
                compacted_version=compacted_version,
                compacted_topic=compacted_topic,
                compacted_importance=compacted_importance,
                rag_top_score=rag_decision.top_score if rag_decision else 0.0,
                rag_accepted=rag_decision.accepted if rag_decision else False,
                rag_rejection_reason=rag_decision.rejection_reason if rag_decision else "",
                analysis_payload=route_plan.analysis_payload,
            )

            reply_content = response["message"]["content"]
            store_turn(user_id, server_id, reply_content, "assistant")
            _maybe_compact_memory(user_id, server_id, channel_id)

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
