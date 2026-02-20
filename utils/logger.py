def log_response(msg, user_content, model, response, elapsed, rag_duration=0, llm_duration=0):
    reply_content = response["message"]["content"]

    prompt_tokens = response.get("prompt_eval_count", 0)
    eval_tokens = response.get("eval_count", 0)
    prompt_dur = response.get("prompt_eval_duration", 0) / 1e9
    eval_dur = response.get("eval_duration", 0) / 1e9
    prompt_rate = prompt_tokens / prompt_dur if prompt_dur > 0 else 0
    eval_rate = eval_tokens / eval_dur if eval_dur > 0 else 0

    print(f"\n{'='*50}")
    print(f"📩 {msg.author} in #{msg.channel}")
    print(f"📝 \"{user_content[:80]}{'...' if len(user_content) > 80 else ''}\"")
    print(f"🤖 Model: {model}")
    print(f"⏱️  Total: {elapsed:.2f}s (RAG: {rag_duration:.2f}s, LLM: {llm_duration:.2f}s)")
    print(f"📊 Prompt: {prompt_tokens} tokens @ {prompt_rate:.1f} t/s")
    print(f"📊 Eval:   {eval_tokens} tokens @ {eval_rate:.1f} t/s")
    print(f"📏 Reply:  {len(reply_content)} chars")
    print(f"{'='*50}")
