import time
import ollama
from core.config import MODEL, SYSTEM_PROMPT
from utils.logger import log_response
from services.rag import RAG
from services.llm import LLMClient
from handlers.conversation_context import store_chat, get_chat

rag = RAG()
llm_client = LLMClient()


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

    user_content = msg.content.replace(f"<@{bot.user.id}>", "").strip()

    start_time = time.time()

    async with msg.channel.typing():
        rag_start = time.time()
        context_chunks = rag.search(user_content)
        rag_duration = time.time() - rag_start

        context_text = ""
        if context_chunks:
            context_text = "\n\n".join(
                f"[{c['source']} - {c['heading']}]\n{c['text']}"
                for c in context_chunks
            )

        personalization = rag.get_personalization_context()
        full_system_prompt = f"{SYSTEM_PROMPT}\n\n=== PERSONALITY & BACKSTORY ===\n{personalization}"

        messages = [
            {"role": "system", "content": full_system_prompt},
        ] + get_chat(str(msg.guild.id), str(msg.channel.id)) #get conversation history

        if context_text:
            messages.append({
                "role": "system",
                "content": f"Here is relevant knowledge to inform your response:\n\n{context_text}"
            })

        store_chat(str(msg.guild.id), str(msg.channel.id), msg.content, "user") #save conversation history

        messages.append({"role": "user", "content": user_content})

        llm_start = time.time()
        
        # Unified LLM Service Call
        # Returns full response object (dict) with metrics
        response = await llm_client.chat(messages)
        
        llm_duration = time.time() - llm_start

    elapsed = time.time() - start_time
    log_response(msg, user_content, MODEL or "unknown", response, elapsed, rag_duration=rag_duration, llm_duration=llm_duration)

    reply_content = response["message"]["content"]
    store_chat(str(msg.guild.id), str(msg.channel.id), reply_content, "assistant")
    chunks = split_message(reply_content)

    await msg.reply(chunks[0])
    for chunk in chunks[1:]:
        await msg.channel.send(chunk)


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
