from typing import Any


def log_response(
    msg: Any,
    user_content: str,
    model: str,
    response: dict,
    elapsed: float,
    rag_duration: float = 0.0,
    llm_duration: float = 0.0,
    query_type: str = "general",
    memory_scanned: int = 0,
    memory_selected: int = 0,
    memory_top_score: float = 0.0,
    memory_duration: float = 0.0,
    search_used: bool = False,
    search_reason: str = "search_not_needed",
    search_query: str = "",
    search_provider: str = "",
    search_result_count: int = 0,
    search_results: list[dict[str, str]] | None = None,
    search_duration: float = 0.0,
    search_error: str | None = None,
    search_query_plans: list[dict[str, str]] | None = None,
    search_evidence_summary: list[dict[str, str]] | None = None,
    exact_claims_allowed: bool = False,
    deterministic_gate: str = "",
    analysis_used: bool = False,
    analysis_time_sensitive: bool | None = None,
    analysis_search_query: str = "",
    analysis_rag_query: str = "",
    can_answer_from_general_knowledge: bool = False,
    general_knowledge_confidence: float = 0.0,
    analysis_reason: str = "",
    final_path: str = "general-knowledge",
    rag_top_score: float = 0.0,
    rag_accepted: bool = False,
    rag_rejection_reason: str = "",
    analysis_payload: dict[str, Any] | None = None,
) -> None:
    reply_content = response["message"]["content"]

    prompt_tokens = response.get("prompt_eval_count", 0)
    eval_tokens = response.get("eval_count", 0)
    prompt_dur = response.get("prompt_eval_duration", 0) / 1e9
    eval_dur = response.get("eval_duration", 0) / 1e9
    prompt_rate = prompt_tokens / prompt_dur if prompt_dur > 0 else 0
    eval_rate = eval_tokens / eval_dur if eval_dur > 0 else 0

    print(f"\n{'=' * 50}")
    print(f"📩 {msg.author} in #{msg.channel}")
    print(f'📝 "{user_content[:80]}{"..." if len(user_content) > 80 else ""}"')
    print(f"user: {user_content}")
    print(f"bot: {reply_content}")
    print(f"🤖 Model: {model}")
    print(f"🧭 Mode: {final_path}")
    print(f"🔍 Query: {query_type}")
    print(f"⏱️  Total: {elapsed:.2f}s (RAG: {rag_duration:.2f}s, LLM: {llm_duration:.2f}s)")
    print(
        f"🧠 Memory: scanned={memory_scanned}, selected={memory_selected}, "
        f"top_score={memory_top_score:.3f}, duration={memory_duration:.2f}s"
    )
    print(
        f"🌐 Search: used={search_used}, reason={search_reason}, provider={search_provider or '-'}, "
        f"results={search_result_count}, duration={search_duration:.2f}s"
    )
    print(
        f"🧩 Analysis: used={analysis_used}, time_sensitive={analysis_time_sensitive}, "
        f"general_ok={can_answer_from_general_knowledge}, general_conf={general_knowledge_confidence:.2f}"
    )
    if deterministic_gate:
        print(f"🧩 Deterministic Gate: {deterministic_gate}")
    if analysis_search_query:
        print(f"🧩 Analysis Search Query: {analysis_search_query}")
    if analysis_rag_query:
        print(f"🧩 Analysis RAG Query: {analysis_rag_query}")
    if analysis_reason:
        print(f"🧩 Analysis Reason: {analysis_reason}")
    if analysis_payload:
        print(f"🧩 Analysis Payload: {analysis_payload}")
    print(
        f"📚 RAG: top_score={rag_top_score:.3f}, accepted={rag_accepted}, rejection={rag_rejection_reason or '-'}"
    )
    if search_query:
        print(f"🔎 Search Query: {search_query}")
    if search_query_plans:
        print("🗺️ Search Plans:")
        for index, plan in enumerate(search_query_plans, start=1):
            print(f"   [{index}] {plan.get('label', 'general')} -> {plan.get('query', '')}")
            if plan.get("purpose"):
                print(f"       purpose={plan.get('purpose', '-')}")
    if search_evidence_summary:
        print("🧪 Evidence Summary:")
        for index, summary in enumerate(search_evidence_summary, start=1):
            print(
                f"   [{index}] {summary.get('label', 'general')} | confidence={summary.get('confidence_summary', '-')}"
                f" | exact={summary.get('exact_claim_allowed', '-')}"
            )
            print(
                f"       agreement={summary.get('agreement_status', '-')}, trusted={summary.get('trusted_result_count', '-')}, "
                f"fallback={summary.get('fallback_result_count', '-')}, mode={summary.get('response_mode', '-')}"
            )
            if summary.get("exact_claim_reason"):
                print(f"       exact-reason: {summary.get('exact_claim_reason')}")
            if summary.get("evidence_summary"):
                print(f"       {summary.get('evidence_summary')}")
    print(f"🎯 Exact Claims Allowed: {exact_claims_allowed}")
    if search_results:
        print("🔎 Search Results:")
        for index, result in enumerate(search_results, start=1):
            title = result.get("title", "")
            source = result.get("source", "")
            url = result.get("url", "")
            published_at = result.get("published_at", "")
            snippet = result.get("snippet", "")
            source_class = result.get("source_class", "")
            surface_class = result.get("surface_class", "")
            freshness_bucket = result.get("freshness_bucket", "")
            rank_reason = result.get("rank_reason", "")
            evidence_quality = result.get("evidence_quality", "")
            stale_penalty_applied = result.get("stale_penalty_applied", "")
            preview_penalty_applied = result.get("preview_penalty_applied", "")
            agreement_participant = result.get("agreement_participant", "")
            exact_answer = result.get("supports_exact_answer", "")
            published_suffix = f" | {published_at}" if published_at else ""
            source_suffix = f" | {source_class}" if source_class else ""
            quality_suffix = f" | {evidence_quality}" if evidence_quality else ""
            surface_suffix = f" | {surface_class}" if surface_class else ""
            freshness_suffix = f" | {freshness_bucket}" if freshness_bucket else ""
            print(
                f"   [{index}] {title} | {source}{source_suffix}{surface_suffix}{freshness_suffix}{quality_suffix}{published_suffix}"
            )
            if url:
                print(f"       {url}")
            if snippet:
                print(f"       {snippet}")
            if rank_reason:
                print(f"       rank: {rank_reason}")
            if stale_penalty_applied or preview_penalty_applied or agreement_participant:
                print(
                    f"       flags: stale={stale_penalty_applied or 'False'} preview={preview_penalty_applied or 'False'} "
                    f"agreement={agreement_participant or 'False'}"
                )
            if exact_answer:
                print(f"       exact: {exact_answer}")
    if search_error:
        print(f"⚠️ Search Error: {search_error}")
    print(f"📊 Prompt: {prompt_tokens} tokens @ {prompt_rate:.1f} t/s")
    print(f"📊 Eval:   {eval_tokens} tokens @ {eval_rate:.1f} t/s")
    print(f"📏 Reply:  {len(reply_content)} chars")
    print(f"{'=' * 50}")
