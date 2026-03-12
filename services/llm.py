import os
import time
import asyncio
import inspect
from typing import Any
from google import genai
from google.genai import types

import ollama

from core.config import USE_ONLINE_MODEL, GOOGLE_GEMINI_API_KEY, ONLINE_MODEL, LOCAL_MODEL

class LLMClient:
    def __init__(self):
        self.use_online = USE_ONLINE_MODEL
        # Validate local model is set
        if not LOCAL_MODEL:
            raise RuntimeError("LOCAL_MODEL must be set in core.config to use the local Ollama backend")

        # Narrow config values to instance attributes for type checkers and runtime use
        assert LOCAL_MODEL is not None
        self.local_model: str = LOCAL_MODEL

        if self.use_online:
            if not GOOGLE_GEMINI_API_KEY or not ONLINE_MODEL:
                print("❌ Error: GOOGLE_GEMINI_API_KEY or ONLINE_MODEL missing. Falling back to local model.")
                self.use_online = False
            elif genai is None:
                print("❌ Error: google.generativeai SDK not available. Falling back to local model.")
                self.use_online = False
            else:
                # Configure Gemini API if available
                configure_fn = getattr(genai, "configure", None)
                if callable(configure_fn):
                    try:
                        configure_fn(api_key=GOOGLE_GEMINI_API_KEY)
                    except Exception as e:
                        print(f"❌ Error configuring Gemini SDK: {e}. Falling back to local model.")
                        self.use_online = False
                else:
                    # Some SDK versions use different initialization; warn and attempt best-effort
                    print("⚠️  google.generativeai.configure not available in this SDK version.")

                # Try to construct a model handle if the SDK provides one
                ModelCls = getattr(genai, "GenerativeModel", None)
                if ModelCls is not None:
                    try:
                        # Narrow type: ensure ONLINE_MODEL is str
                        assert ONLINE_MODEL is not None
                        self.online_model: str = ONLINE_MODEL
                        self.model = ModelCls(self.online_model)
                        print(f"✨ Using Online Model: {self.online_model}")
                    except Exception as e:
                        print(f"❌ Failed to initialize Gemini model: {e}. Falling back to local model.")
                        self.use_online = False
                else:
                    # If we can't build a model object, fall back to local but keep SDK available for ad-hoc calls
                    print("⚠️  google.generativeai.GenerativeModel unavailable; using local model instead.")
                    self.use_online = False

        if not self.use_online:
            print(f"🖥️ Using Local Model: {self.local_model}")

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
        if ollama is None:
            raise RuntimeError("Ollama SDK is not installed; cannot use local model")

        client = ollama.AsyncClient()

        # Try common call signatures to be compatible with different ollama versions
        chat_fn = getattr(client, "chat")

        # Preferred: coroutine function
        if inspect.iscoroutinefunction(chat_fn):
            try:
                return await chat_fn(model=self.local_model, messages=messages, think=False)
            except Exception:
                pass

        # Fallback: call sync function in a thread to avoid blocking event loop
        def call_variant(*args, **kwargs):
            return chat_fn(*args, **kwargs)

        # Try keyword signature
        try:
            return await asyncio.to_thread(call_variant, model=self.local_model, messages=messages, think=False)
        except Exception:
            pass

        # Try positional signature (model, messages)
        try:
            return await asyncio.to_thread(call_variant, self.local_model, messages)
        except Exception:
            pass

        # Try messages-only signature
        try:
            return await asyncio.to_thread(call_variant, messages=messages)
        except Exception as e:
            raise RuntimeError(f"Ollama chat call failed with multiple signatures: {e}")

    def _response_to_text(self, response: Any) -> str:
        """Robustly extract assistant text from various SDK response shapes."""
        if response is None:
            return ""

        # If already a string
        if isinstance(response, str):
            return response

        # Common attribute names
        for attr in ("text", "content", "output_text", "output", "message", "response"):
            val = getattr(response, attr, None)
            if isinstance(val, str):
                return val
            if isinstance(val, dict) and "text" in val and isinstance(val["text"], str):
                return val["text"]
            if isinstance(val, list) and val and isinstance(val[0], str):
                return val[0]

            if hasattr(val, "text"):
                t = getattr(val, "text")
                if isinstance(t, str):
                    return t
            if hasattr(val, "content"):
                t = getattr(val, "content")
                if isinstance(t, str):
                    return t

        # Dict-like responses
        if isinstance(response, dict):
            for key in ("text", "content", "output", "message"):
                v = response.get(key)
                if isinstance(v, str):
                    return v
                if isinstance(v, dict) and isinstance(v.get("text"), str):
                    return v["text"]

            for list_key in ("generations", "choices", "outputs"):
                lst = response.get(list_key)
                if isinstance(lst, list) and lst:
                    first = lst[0]
                    if isinstance(first, str):
                        return first
                    if isinstance(first, dict):
                        for k in ("text", "content"):
                            vv = first.get(k)
                            if isinstance(vv, str):
                                return vv

        # Try common conversion method
        try:
            to_dict = getattr(response, "to_dict", None)
            if callable(to_dict):
                dd = to_dict()
                if isinstance(dd, dict):
                    return self._response_to_text(dd)
        except Exception:
            pass

        return str(response)

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

        if genai is None:
            raise RuntimeError("google.generativeai SDK not available at runtime")

        # If we have a model handle from initialization, try to use it. Otherwise attempt on-the-fly calls.
        model = getattr(self, "model", None)
        chat = None

        if model is not None:
            # Best-effort: some SDKs support start_chat on the model
            start_chat = getattr(model, "start_chat", None)
            if callable(start_chat):
                # start_chat may be sync or async; prefer not to call sync methods directly
                if inspect.iscoroutinefunction(start_chat):
                    chat = await start_chat(history=history)
                else:
                    chat = start_chat(history=history)

        if chat is None:
            # Attempt to construct a chat via higher-level SDK helpers if available
            ModelCls = getattr(genai, "GenerativeModel", None)
            if ModelCls is not None and ONLINE_MODEL is not None:
                try:
                    inst = ModelCls(self.online_model)
                    start_chat = getattr(inst, "start_chat", None)
                    if callable(start_chat):
                        if inspect.iscoroutinefunction(start_chat):
                            chat = await start_chat(history=history)
                        else:
                            chat = start_chat(history=history)
                except Exception:
                    chat = None

        if chat is None:
            raise RuntimeError("Unable to construct a Gemini chat object with the installed SDK")

        # Async generation (SDK may provide async send; try common names)
        send_async = getattr(chat, "send_message_async", None) or getattr(chat, "send_async", None)
        send_sync = getattr(chat, "send_message", None) or getattr(chat, "send", None)

        response = None

        if callable(send_async):
            if inspect.iscoroutinefunction(send_async):
                response = await send_async(last_user_message)
            else:
                # If it's a sync function that returns awaitable, call and await; otherwise run in thread
                result = send_async(last_user_message)
                if inspect.isawaitable(result):
                    response = await result
                else:
                    response = await asyncio.to_thread(send_async, last_user_message)
        elif callable(send_sync):
            if inspect.iscoroutinefunction(send_sync):
                response = await send_sync(last_user_message)
            else:
                response = await asyncio.to_thread(send_sync, last_user_message)
        else:
            raise RuntimeError("Gemini chat object does not support known send methods")
        
        # Construct a fake Ollama-style response object
        # Gemini doesn't easily give token counts in the exact same format without extra calls
        assistant_text = self._response_to_text(response)

        return {
            "model": ONLINE_MODEL,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%S.%fZ", time.gmtime()),
            "message": {
                "role": "assistant",
                "content": assistant_text
            },
            "done": True,
            "eval_count": 0,
            "eval_duration": 0,
            "prompt_eval_count": 0,
            "prompt_eval_duration": 0
        }
