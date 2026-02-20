import os
import time
import google.generativeai as genai
import ollama
from core.config import USE_ONLINE_MODEL, GOOGLE_GEMINI_API_KEY, ONLINE_MODEL, LOCAL_MODEL

class LLMClient:
    def __init__(self):
        self.use_online = USE_ONLINE_MODEL
        
        if self.use_online:
            if not GOOGLE_GEMINI_API_KEY:
                print("❌ Error: GOOGLE_GEMINI_API_KEY missing. Falling back to local model.")
                self.use_online = False
            else:
                genai.configure(api_key=GOOGLE_GEMINI_API_KEY)
                self.model = genai.GenerativeModel(ONLINE_MODEL)
                print(f"✨ Using Online Model: {ONLINE_MODEL}")

        if not self.use_online:
            print(f"🖥️ Using Local Model: {LOCAL_MODEL}")

    async def chat(self, messages):
        """
        Unified chat interface.
        Returns a dict compatible with Ollama's response format:
        {
            "message": {"content": str, "role": "assistant"},
            "eval_count": int,
            "eval_duration": int (nanoseconds),
            "prompt_eval_count": int,
            "prompt_eval_duration": int (nanoseconds),
            "model": str,
            "created_at": str
        }
        """
        if self.use_online:
            return await self._chat_gemini(messages)
        else:
            return await self._chat_ollama(messages)

    async def _chat_ollama(self, messages):
        # Ollama returns the full object with metrics natively
        return await ollama.AsyncClient().chat(
            model=LOCAL_MODEL,
            messages=messages,
            think=False,
        )

    async def _chat_gemini(self, messages):
        # Convert standard messages to Gemini format
        system_instruction = None
        history = []
        last_user_message = ""

        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            
            if role == "system":
                if system_instruction is None:
                    system_instruction = content
                else:
                    system_instruction += f"\n\n{content}"
            elif role == "user":
                last_user_message = content
                if msg != messages[-1]:
                    history.append({"role": "user", "parts": [content]})
            elif role == "assistant":
                history.append({"role": "model", "parts": [content]})

        if system_instruction:
            model = genai.GenerativeModel(ONLINE_MODEL, system_instruction=system_instruction)
        else:
            model = self.model

        chat = model.start_chat(history=history)
        
        # Async generation
        response = await chat.send_message_async(last_user_message)
        
        # Construct a fake Ollama-style response object
        # Gemini doesn't easily give token counts in the exact same format without extra calls
        return {
            "model": ONLINE_MODEL,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%S.%fZ", time.gmtime()),
            "message": {
                "role": "assistant",
                "content": response.text
            },
            "done": True,
            "eval_count": 0,
            "eval_duration": 0,
            "prompt_eval_count": 0,
            "prompt_eval_duration": 0
        }
