from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any

import discord
from core.config import SEARCH_ENABLED, SYSTEM_PROMPT
from handlers.message import split_message
from services.llm import LLMClient
from services.rag import RAG
from services.search import (
    SearchExecution,
    build_search_context_block,
    create_enabled_search_provider,
    create_search_plan,
    run_search_plans,
    search_execution_allows_exact_claims,
    serialize_search_evidence_summary,
    serialize_search_results,
)
from utils.logger import log_response

rag = RAG()
llm_client = LLMClient()
search_provider = create_enabled_search_provider(SEARCH_ENABLED)


@dataclass(slots=True)
class _InteractionLogContext:
    author: str
    channel: str


def _log_context_from_interaction(interaction: discord.Interaction) -> _InteractionLogContext:
    user = getattr(interaction, "user", None)
    channel = getattr(interaction, "channel", None)
    author_name = str(user) if user is not None else "unknown-user"
    channel_name = str(channel) if channel is not None else "slash-command"
    return _InteractionLogContext(author=author_name, channel=channel_name)


def _synthetic_response(*, model: str, content: str) -> dict[str, Any]:
    return {
        "model": model,
        "message": {"content": content},
        "prompt_eval_count": 0,
        "eval_count": 0,
        "prompt_eval_duration": 0,
        "eval_duration": 0,
    }


def _log_search_interaction(
    interaction: discord.Interaction,
    *,
    user_content: str,
    response: dict[str, Any],
    elapsed: float,
    llm_duration: float = 0.0,
    search_execution: SearchExecution | None = None,
    final_path: str,
) -> None:
    execution = search_execution or SearchExecution(
        used=False,
        reason="search_not_needed",
        query="",
        provider="disabled",
        result_count=0,
        duration=0.0,
        error=None,
        bundles=[],
    )
    log_response(
        _log_context_from_interaction(interaction),
        user_content,
        response.get("model") or llm_client.model or "unknown",
        response,
        elapsed,
        rag_duration=0.0,
        llm_duration=llm_duration,
        query_type="slash-search",
        search_used=execution.used,
        search_reason=execution.reason,
        search_query=execution.query,
        search_provider=execution.provider,
        search_result_count=execution.result_count,
        search_results=serialize_search_results(execution),
        search_duration=execution.duration,
        search_error=execution.error,
        search_evidence_summary=serialize_search_evidence_summary(execution),
        exact_claims_allowed=search_execution_allows_exact_claims(execution),
        analysis_used=False,
        final_path=final_path,
        rag_top_score=0.0,
        rag_accepted=False,
    )


def _build_search_disabled_response() -> str:
    return "Live search is currently disabled in my records, so I cannot look that up for you right now."


def _build_search_unavailable_response() -> str:
    return "Live search is not available in my current records, so I cannot look that up right now."


def _build_search_uncertain_response() -> str:
    return "Current reports are too mixed or weak for me to state that confidently. I would rather leave it uncertain than offer you a false exact answer."


def _build_search_runtime_error_response() -> str:
    return (
        "The signals beyond these shores have grown turbulent for a moment. I could not finish "
        "assembling a reliable answer just now."
    )


def _build_search_rate_limited_response() -> str:
    return (
        "I gathered the outside signals, but the final synthesis is being throttled for the moment. "
        "Give me a little time, and I shall try to weave those reports into something clearer for you."
    )


def _is_rate_limit_error(exc: Exception) -> bool:
    message = str(exc).lower()
    return "rate limit" in message or "429" in message or "too many requests" in message


def _build_rate_limited_search_fallback(search_execution: SearchExecution) -> str:
    if not search_execution.bundles:
        return _build_search_rate_limited_response()

    bundle = search_execution.bundles[0]
    results = bundle.results[:3]
    if not results:
        return _build_search_rate_limited_response()

    unique_sources = list(dict.fromkeys(result.source for result in results[:3]))
    source_list = ", ".join(unique_sources)

    top_result = results[0]
    top_evidence = (top_result.extracted_text or top_result.snippet).strip()
    if len(top_evidence) > 220:
        top_evidence = top_evidence[:217].rstrip() + "..."

    opening = "The archive holds little on this matter, so I listened beyond these shores for reliable reports."
    source_sentence = f"The clearest signals came through {source_list}."

    if bundle.exact_claim_allowed:
        conclusion = f"Their reports align strongly enough that the leading account points to this: {top_evidence}"
    elif bundle.response_mode == "summary":
        conclusion = (
            "Their signals are useful, but not aligned enough for a precise live claim. "
            f"The strongest lead I found says: {top_evidence}"
        )
    else:
        conclusion = (
            "Their signals are still too mixed for certainty. "
            f"The strongest lead I found says: {top_evidence}"
        )

    return " ".join((opening, source_sentence, conclusion))


def _build_search_system_prompt(*, resolved_query: str, search_execution: SearchExecution) -> str:
    personalization = rag.get_personalization_context()
    manifest = rag.get_manifest()
    system_sections = [
        SYSTEM_PROMPT,
        f"=== PERSONALITY & BACKSTORY ===\n{personalization}",
        manifest,
        "Resolved interpretation of the current user message:\n"
        f"{resolved_query}\n"
        "Use this only to interpret the user's current intent.",
    ]
    if search_execution.used and search_execution.bundles:
        system_sections.append(
            "Search-path behavior override:\n"
            "- The archive may not hold this subject as stable lore, but live search evidence is present below.\n"
            "- Do NOT say the information is outside your records, unavailable to you, or beyond your frequencies when live search evidence exists.\n"
            "- Instead, respond in character as though you briefly consulted the outside world for reliable signals before answering.\n"
            "- A natural framing is something like: 'The archive holds little on this matter, so I listened beyond these shores for reliable reports.'\n"
            "- After that transition, summarize the live evidence plainly and directly."
        )
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

    system_sections.append(
        "Path-specific rules:\n"
        "- search: use only live search context for current facts.\n"
        "- search: if live evidence exists, always answer from it instead of refusing on the basis that the topic is not in your archive.\n"
        "- search: keep the transition in character, then deliver the outside findings clearly.\n"
        "- Do not mention citations or URLs unless the user explicitly asks for sources."
    )
    return "\n\n".join(system_sections)


async def _send_interaction_chunks(interaction: discord.Interaction, text: str) -> None:
    chunks = split_message(text)
    await interaction.followup.send(chunks[0])
    for chunk in chunks[1:]:
        await interaction.followup.send(chunk)


async def handle_search_interaction(interaction: discord.Interaction, *, query: str) -> None:
    normalized_query = query.strip()
    user_content = f"/search {normalized_query}" if normalized_query else "/search"
    start_time = time.time()
    if not SEARCH_ENABLED:
        reply_content = _build_search_disabled_response()
        response = _synthetic_response(model="search-disabled", content=reply_content)
        _log_search_interaction(
            interaction,
            user_content=user_content,
            response=response,
            elapsed=time.time() - start_time,
            final_path="search-disabled",
        )
        await interaction.response.send_message(reply_content)
        return
    if search_provider is None:
        reply_content = _build_search_unavailable_response()
        response = _synthetic_response(model="search-unavailable", content=reply_content)
        _log_search_interaction(
            interaction,
            user_content=user_content,
            response=response,
            elapsed=time.time() - start_time,
            final_path="search-unavailable",
        )
        await interaction.response.send_message(reply_content)
        return

    search_plan = create_search_plan(
        normalized_query,
        label="slash",
        purpose="user-initiated slash command search",
    )
    if search_plan is None:
        reply_content = "That search query is too short for me to resolve safely. Please give me a little more detail."
        response = _synthetic_response(model="search-validation", content=reply_content)
        _log_search_interaction(
            interaction,
            user_content=user_content,
            response=response,
            elapsed=time.time() - start_time,
            final_path="search-too-short",
        )
        await interaction.response.send_message(reply_content)
        return

    await interaction.response.defer(thinking=True)
    search_execution = await run_search_plans(
        [search_plan],
        reason="slash_search",
        search_provider=search_provider,
    )

    if not search_execution.used or not search_execution.bundles:
        reply_content = _build_search_unavailable_response()
        response = _synthetic_response(model="search-unavailable", content=reply_content)
        _log_search_interaction(
            interaction,
            user_content=user_content,
            response=response,
            elapsed=time.time() - start_time,
            search_execution=search_execution,
            final_path="search-unavailable",
        )
        await interaction.followup.send(reply_content)
        return
    if all(bundle.response_mode == "uncertain" for bundle in search_execution.bundles):
        reply_content = _build_search_uncertain_response()
        response = _synthetic_response(model="uncertainty-guard", content=reply_content)
        _log_search_interaction(
            interaction,
            user_content=user_content,
            response=response,
            elapsed=time.time() - start_time,
            search_execution=search_execution,
            final_path="uncertain",
        )
        await interaction.followup.send(reply_content)
        return

    messages = [
        {
            "role": "system",
            "content": _build_search_system_prompt(
                resolved_query=search_plan.query,
                search_execution=search_execution,
            ),
        },
        {"role": "user", "content": normalized_query},
    ]
    try:
        llm_start = time.time()
        response = await llm_client.chat(messages)
        llm_duration = time.time() - llm_start
        reply_content = response["message"]["content"]
        elapsed = time.time() - start_time
        _log_search_interaction(
            interaction,
            user_content=user_content,
            response=response,
            elapsed=elapsed,
            llm_duration=llm_duration,
            search_execution=search_execution,
            final_path="search-grounded",
        )
        await _send_interaction_chunks(interaction, reply_content)
    except Exception as exc:
        if _is_rate_limit_error(exc):
            reply_content = _build_rate_limited_search_fallback(search_execution)
            response = _synthetic_response(model="search-rate-limited", content=reply_content)
            final_path = "search-rate-limited"
        else:
            reply_content = _build_search_runtime_error_response()
            response = _synthetic_response(model="search-runtime-error", content=reply_content)
            final_path = "search-runtime-error"
        _log_search_interaction(
            interaction,
            user_content=user_content,
            response=response,
            elapsed=time.time() - start_time,
            search_execution=search_execution,
            final_path=final_path,
        )
        print(f"⚠️ Search-grounded reply failed: {exc}")
        await interaction.followup.send(reply_content)


def register_search_command(tree: discord.app_commands.CommandTree) -> None:
    get_command = getattr(tree, "get_command", None)
    if callable(get_command) and get_command("search") is not None:
        return

    @tree.command(name="search", description="Search the live web for current information")
    @discord.app_commands.describe(query="What to search for")
    async def search(interaction: discord.Interaction, query: str) -> None:
        await handle_search_interaction(interaction, query=query)
