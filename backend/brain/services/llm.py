import asyncio
import inspect
import re
import time
from datetime import UTC, datetime
from typing import Any

from core.config import (
    LLM_PROVIDER,
    LOCAL_API_KEY,
    LOCAL_BASE_URL,
    LOCAL_CONTEXT_WINDOW,
    LOCAL_KV_CACHE_KEEP,
    LOCAL_MODEL,
    MODE,
    ONLINE_BASE_URL,
    ONLINE_LLM_API_KEY,
    ONLINE_LLM_MODEL,
    ONLINE_MODEL,
)
from openai import AsyncOpenAI

_ollama: Any | None
try:
    import ollama as _ollama
except ImportError:  # pragma: no cover - optional when using llama.cpp/OpenAI-compatible servers
    _ollama = None

ollama: Any | None = _ollama


def _normalize_provider(name: str) -> str:
    value = name.strip().lower()
    aliases = {
        "server": "openai",
        "openai-compatible": "openai",
        "llama.cpp": "llamacpp",
        "llama-cpp": "llamacpp",
    }
    return aliases.get(value, value)


_THINK_BLOCK_RE = re.compile(r"^\s*<think>\s*.*?\s*</think>\s*", re.DOTALL)


def _strip_think_block(text: str) -> str:
    stripped = _THINK_BLOCK_RE.sub("", text, count=1)
    return stripped.lstrip()


class LLMClient:
    def __init__(self):
        self.provider = _normalize_provider(LLM_PROVIDER)
        self.model = LOCAL_MODEL
        self.context_window = LOCAL_CONTEXT_WINDOW
        self.kv_cache_keep = LOCAL_KV_CACHE_KEEP
        self.client: AsyncOpenAI | None = None

        if self.provider == "openai":
            effective_key = ONLINE_LLM_API_KEY
            effective_model = ONLINE_LLM_MODEL or ONLINE_MODEL
            if not effective_key or not effective_model:
                print(
                    "❌ ONLINE_LLM_API_KEY or ONLINE_MODEL missing. Falling back to local llama.cpp server."
                )
                self.provider = "llamacpp"
            else:
                self.client = AsyncOpenAI(api_key=effective_key, base_url=ONLINE_BASE_URL)
                self.model = effective_model
                mode_tag = "remote" if MODE == "online" else "OpenAI-compatible"
                print(f"✨ Using {mode_tag} model: {self.model} ({ONLINE_BASE_URL})")

        if self.provider == "llamacpp":
            self.client = AsyncOpenAI(api_key=LOCAL_API_KEY, base_url=LOCAL_BASE_URL)
            self.model = LOCAL_MODEL
            print(f"🦙 Using local llama.cpp server: {self.model} ({LOCAL_BASE_URL})")

        if self.provider == "ollama":
            if ollama is None:
                print("❌ Ollama package is not installed. Falling back to local llama.cpp server.")
                self.provider = "llamacpp"
                self.client = AsyncOpenAI(api_key=LOCAL_API_KEY, base_url=LOCAL_BASE_URL)
                self.model = LOCAL_MODEL
            else:
                self.model = LOCAL_MODEL
                print(f"🖥️  Using local Ollama: {self.model}")

    async def chat(self, messages):
        if self.provider == "ollama":
            return await self._chat_ollama(messages)
        return await self._chat_openai_compatible(messages)

    async def _chat_ollama(self, messages):
        if ollama is None:
            raise RuntimeError("Ollama provider selected but the ollama package is not installed.")

        client = ollama.AsyncClient()
        chat_fn = client.chat

        if inspect.iscoroutinefunction(chat_fn):
            try:
                return await chat_fn(
                    model=self.model,
                    messages=messages,
                    think=False,
                    options={
                        "num_ctx": self.context_window,
                        "num_keep": self.kv_cache_keep,
                    },
                )
            except Exception:
                pass

        # Fallback for sync variants
        def call_variant(*args, **kwargs):
            return chat_fn(*args, **kwargs)

        try:
            return await asyncio.to_thread(
                call_variant, model=self.model, messages=messages, think=False
            )
        except Exception as e:
            raise RuntimeError(f"Ollama chat call failed: {e}") from e

    async def _chat_openai_compatible(self, messages):
        start_time = time.time()

        if self.client is None:
            raise RuntimeError("OpenAI-compatible client is not initialized.")

        try:
            request_kwargs = {
                "model": self.model,
                "messages": messages,
                "stream": False,
            }
            if self.provider == "llamacpp":
                request_kwargs["extra_body"] = {
                    "chat_template_kwargs": {"enable_thinking": False},
                    "reasoning_format": "none",
                }

            response = await self.client.chat.completions.create(**request_kwargs)

            assistant_text = response.choices[0].message.content or ""
            assistant_text = _strip_think_block(assistant_text)
            usage = getattr(response, "usage", None)
            prompt_tokens = usage.prompt_tokens if usage else 0
            completion_tokens = usage.completion_tokens if usage else 0
            duration_ns = int((time.time() - start_time) * 1e9)

            return {
                "model": self.model,
                "created_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
                "message": {"role": "assistant", "content": assistant_text},
                "done": True,
                "eval_count": completion_tokens,
                "eval_duration": duration_ns,
                "prompt_eval_count": prompt_tokens,
                "prompt_eval_duration": 0,
            }
        except Exception as e:
            resp = getattr(e, "response", None)
            status = getattr(e, "status_code", None) or (resp.status_code if resp else None)
            body = resp.text if resp else getattr(e, "body", None) or str(e)
            prefix = f" (HTTP {status})" if status else ""
            raise RuntimeError(f"OpenAI-compatible model call failed{prefix}: {body}") from e
