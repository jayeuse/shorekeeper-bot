# Service Guidelines

- Services encapsulate RAG, embeddings, LLM providers, and memory coordination. Keep Discord objects out of this layer.
- Provider clients must use configured models, base URLs, timeouts, and normalized response shapes.
- Retrieval changes must preserve metadata/embedding index alignment and deterministic fallbacks.
- Treat provider output and retrieved text as untrusted; redact sensitive request data from logs.
- Add focused tests for scoring, fallback, parsing, retries, and provider failures.

