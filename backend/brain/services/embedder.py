from typing import Any

from core.config import (
    EMBED_API_KEY,
    EMBED_BASE_URL,
    EMBED_MODEL,
    EMBEDDING_PROVIDER,
    LOCAL_API_KEY,
    ONLINE_API_KEY,
)
from openai import OpenAI

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


class EmbedderClient:
    def __init__(self) -> None:
        self.provider = _normalize_provider(EMBEDDING_PROVIDER)
        self.client: OpenAI | None = None
        self.model = EMBED_MODEL

        if self.provider in {"llamacpp", "openai"}:
            try:
                api_key = (
                    EMBED_API_KEY
                    if self.provider == "llamacpp"
                    else (ONLINE_API_KEY or EMBED_API_KEY or "no-key")
                )
                self.client = OpenAI(api_key=api_key or LOCAL_API_KEY, base_url=EMBED_BASE_URL)
                print(
                    f"🧠 Using OpenAI-compatible embedding endpoint: {self.model} ({EMBED_BASE_URL})"
                )
            except Exception as e:
                print(f"❌ Failed to init embedding server at {EMBED_BASE_URL}: {e}")
                self.provider = "ollama"

        if self.provider == "ollama":
            if ollama is None:
                raise RuntimeError(
                    "Ollama embedding provider selected but the ollama package is not installed."
                )
            print(f"🖥️  Using local Ollama embeddings: {EMBED_MODEL}")

    def embed_document(self, text: str) -> list[float]:
        if self.provider in {"llamacpp", "openai"}:
            return self._embed_server(text)
        return self._embed_ollama(f"search_document: {text}")

    def embed_query(self, text: str) -> list[float]:
        if self.provider in {"llamacpp", "openai"}:
            return self._embed_server(text)
        return self._embed_ollama(f"search_query: {text}")

    def _embed_ollama(self, text: str) -> list[float]:
        if ollama is None:
            raise RuntimeError(
                "Ollama embedding provider selected but the ollama package is not installed."
            )
        try:
            response = ollama.embed(model=EMBED_MODEL, input=text)
            return response["embeddings"][0]
        except Exception as e:
            print(f"⚠️  Ollama Error: {e}")
            return []

    def _embed_server(self, text: str) -> list[float]:
        if self.client is None:
            raise RuntimeError("Embedding client is not initialized.")
        try:
            # llama.cpp truncation safety: 8000 chars is roughly 2000 tokens
            safe_text = text[:8000]
            response = self.client.embeddings.create(model=self.model, input=safe_text)
            return response.data[0].embedding
        except Exception as e:
            print(f"⚠️  Embedding Server Error: {e}")
            return []
