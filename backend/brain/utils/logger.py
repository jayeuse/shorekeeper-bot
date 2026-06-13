from typing import Any


def log_response(
    msg: Any,
    user_content: str,
    model: str,
    response: dict,
    elapsed: float,
    rag_duration: float = 0.0,
    llm_duration: float = 0.0,
    query_type: str = "lore",
    top_k: int = 5,
    memory_scanned: int = 0,
    memory_selected: int = 0,
    memory_top_score: float = 0.0,
    memory_duration: float = 0.0,
    search_used: bool = False,
    search_reason: str = "search_not_needed",
    search_query: str = "",
    search_provider: str = "",
    search_result_count: int = 0,
    search_duration: float = 0.0,
    search_error: str | None = None,
) -> None:
    reply_content = response["message"]["content"]

    prompt_tokens = response.get("prompt_eval_count", 0)
    eval_tokens = response.get("eval_count", 0)
    prompt_dur = response.get("prompt_eval_duration", 0) / 1e9
    eval_dur = response.get("eval_duration", 0) / 1e9
    prompt_rate = prompt_tokens / prompt_dur if prompt_dur > 0 else 0
    eval_rate = eval_tokens / eval_dur if eval_dur > 0 else 0
    if search_used:
        response_mode = "live-search grounded"
    elif search_reason == "search_failed_continue_without_results":
        response_mode = "degraded after search failure"
    elif memory_selected > 0 and top_k > 0:
        response_mode = "memory + RAG"
    elif top_k > 0:
        response_mode = "RAG-only"
    else:
        response_mode = "chat-only"

    print(f"\n{'=' * 50}")
    print(f"📩 {msg.author} in #{msg.channel}")
    print(f'📝 "{user_content[:80]}{"..." if len(user_content) > 80 else ""}"')
    print(f"🤖 Model: {model}")
    print(f"🧭 Mode: {response_mode}")
    print(f"🔍 Query: {query_type} (top_k={top_k})")
    print(f"⏱️  Total: {elapsed:.2f}s (RAG: {rag_duration:.2f}s, LLM: {llm_duration:.2f}s)")
    print(
        f"🧠 Memory: scanned={memory_scanned}, selected={memory_selected}, "
        f"top_score={memory_top_score:.3f}, duration={memory_duration:.2f}s"
    )
    print(
        f"🌐 Search: used={search_used}, reason={search_reason}, provider={search_provider or '-'}, "
        f"results={search_result_count}, duration={search_duration:.2f}s"
    )
    if search_query:
        print(f"🔎 Search Query: {search_query}")
    if search_error:
        print(f"⚠️ Search Error: {search_error}")
    print(f"📊 Prompt: {prompt_tokens} tokens @ {prompt_rate:.1f} t/s")
    print(f"📊 Eval:   {eval_tokens} tokens @ {eval_rate:.1f} t/s")
    print(f"📏 Reply:  {len(reply_content)} chars")
    print(f"{'=' * 50}")
