from typing import Optional

import ollama
from google import genai
from google.genai import types

from core.config import (
    USE_ONLINE_EMBEDDER,
    GOOGLE_GEMINI_API_KEY,
    ONLINE_EMBED_MODEL,
    LOCAL_EMBED_MODEL,
    ONLINE_EMBED_DIMENSIONS,
)


class EmbedderClient:
    """Abstraction over local (Ollama/nomic-embed-text) and online (Gemini Embedding 2) embedders.

    For local embeddings, the nomic-embed-text model uses a prefix convention:
      - Documents: "search_document: <text>"
      - Queries:   "search_query: <text>"

    For Gemini embeddings, the equivalent is expressed via EmbedContentConfig.task_type:
      - Documents: RETRIEVAL_DOCUMENT
      - Queries:   RETRIEVAL_QUERY

    Callers should pass plain text to embed_document() and embed_query(); this class
    handles the prefix/task_type internally.
    """

    def __init__(self) -> None:
        self.use_online = USE_ONLINE_EMBEDDER
        self._gemini_client: Optional[genai.Client] = None
        self._embed_model: str = ONLINE_EMBED_MODEL or "gemini-embedding-2-preview"
        self._embed_dimensions: int = ONLINE_EMBED_DIMENSIONS

        if self.use_online:
            if not GOOGLE_GEMINI_API_KEY or not ONLINE_EMBED_MODEL:
                print("❌ GOOGLE_GEMINI_API_KEY or ONLINE_EMBED_MODEL missing. Falling back to local embedder.")
                self.use_online = False
            else:
                try:
                    self._gemini_client = genai.Client(api_key=GOOGLE_GEMINI_API_KEY)
                    print(f"✨ Using Online Embedder: {self._embed_model} (dim={self._embed_dimensions})")
                except Exception as e:
                    print(f"❌ Failed to initialize Gemini embedder: {e}. Falling back to local embedder.")
                    self.use_online = False

        if not self.use_online:
            print(f"🖥️ Using Local Embedder: {LOCAL_EMBED_MODEL}")

    def embed_document(self, text: str) -> list[float]:
        """Embed a knowledge chunk for indexing."""
        if self.use_online and self._gemini_client is not None:
            return self._embed_gemini(text, task_type="RETRIEVAL_DOCUMENT")
        return self._embed_ollama(f"search_document: {text}")

    def embed_query(self, text: str) -> list[float]:
        """Embed a search query."""
        if self.use_online and self._gemini_client is not None:
            return self._embed_gemini(text, task_type="RETRIEVAL_QUERY")
        return self._embed_ollama(f"search_query: {text}")

    def _embed_gemini(self, text: str, task_type: str) -> list[float]:
        assert self._gemini_client is not None
        result = self._gemini_client.models.embed_content(
            model=self._embed_model,
            contents=text,
            config=types.EmbedContentConfig(
                task_type=task_type,
                output_dimensionality=self._embed_dimensions,
            ),
        )
        return list(result.embeddings[0].values)

    def _embed_ollama(self, text: str) -> list[float]:
        response = ollama.embed(model=LOCAL_EMBED_MODEL, input=text)
        return response["embeddings"][0]
