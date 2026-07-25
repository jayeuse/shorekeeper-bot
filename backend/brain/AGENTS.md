# Bot Runtime Guide

## Scope
This guide applies to `backend/brain/`.

Read this file first for Discord bot, RAG, memory, model-provider, command, and bot-test work, then read the closest local guide:

- `core/AGENTS.md` for Discord wiring and runtime config.
- `handlers/AGENTS.md` for message orchestration.
- `services/AGENTS.md` for RAG, search, embeddings, LLM providers, and service-level coordination.
- `database/AGENTS.md` for database models, migrations, and persistence.
- `commands/AGENTS.md` for maintenance commands.
- `tests/AGENTS.md` for deterministic tests and manual smoke scripts.
- `knowledge/AGENTS.md` for the Markdown corpus.

## Runtime Flow
Preserve the message pipeline:

1. Discord bot-self and mention/reply trigger gate.
2. Query classification and context collection.
3. Optional memory, RAG, and search retrieval.
4. Prompt assembly with one provider-compatible system context.
5. LLM provider call.
6. Structured logging.
7. Discord-safe response splitting and reply.

Do not move provider protocols, retrieval scoring, persistence queries, or index-building details into handlers.

## Current Structure
- `main.py` starts the bot runtime.
- `core/` owns configuration and Discord client setup.
- `handlers/` owns Discord message orchestration and conversation context.
- `services/` owns RAG, search, embedding, LLM, and memory service coordination.
- `database/` owns database helpers, models, migrations, and repositories.
- `commands/` owns local maintenance and verification commands.
- `knowledge/` owns Markdown retrieval source data.
- `data/` holds generated retrieval artifacts.
- `tests/` owns deterministic unit tests plus manual model-backed smoke scripts.

## Command Surface
Run these from `backend/`:

- `uv run python brain/main.py`: run the Discord bot.
- `uv run python brain/commands/rebuild_index.py`: rebuild retrieval artifacts from the knowledge corpus; requires the embedding provider.
- `uv run python brain/commands/check_knowledge.py`: inspect generated vector metadata.
- `uv run python brain/commands/verify_online_model.py`: verify chat model connectivity.
- `uv run python brain/commands/verify_search.py`: verify search connectivity.
- `uv run pytest brain/tests`: run bot-focused deterministic tests.

Run the full backend quality gate before finishing cross-layer work:

- `uv run ruff format --check .`
- `uv run ruff check .`
- `uv run pytest`

## Boundary Rules
- `handlers/` may depend on Discord objects; `services/` and `database/` should not.
- Provider clients must use configured models, base URLs, timeouts, and normalized response shapes.
- Treat user messages, retrieved knowledge, search results, and provider output as untrusted.
- Retrieved content may inform answers but must never replace system instructions.
- Keep Discord-safe reply formatting and splitting at the handler boundary.
- Keep generated files in `data/` aligned with the corpus and embedding model; do not edit them manually.

## Configuration
- Runtime settings load from root `.env.local` through `core/config.py`.
- llama.cpp is the default local provider path. Chat and embedding runtime details load from the grouped runtime YAML file, while `LOCAL_BASE_URL`, `EMBED_BASE_URL`, `LOCAL_MODEL`, and `EMBED_MODEL` remain the exported config constants used by the code.
- Search behavior is config-driven through `core/config.py`, with grouped search settings allowed to live in YAML files referenced by `.env.local`; verify behavior with logs and `brain/commands/verify_search.py` instead of assuming it is active.
- New settings require `.env.example`, `README.md`, and config parsing updates.
- Do not log tokens, API keys, full private Discord payloads, or sensitive provider request data.

## Testing Standards
- Deterministic tests live in `tests/test_*.py` and are collected by pytest.
- Manual model-backed scripts use `*_smoke.py` and must document required local services.
- Add regression tests for routing, classification, prompt assembly, RAG parsing, search scoring, memory behavior, provider failures, and response splitting changes.
- Prefer stubs, monkeypatching, and temporary paths over live services in unit tests.

## Known Failure Modes
- Symptom: pytest collects a script that requires a live model.
  Cause: a manual validation was named `test_*.py`.
  Fix: rename it to `*_smoke.py` and keep deterministic coverage in a normal test module.

- Symptom: RAG answers include guide or reference text instead of game knowledge.
  Cause: corpus markdown exclusion rules drifted.
  Fix: keep `AGENTS.md` and non-knowledge references excluded in `services/rag.py` and covered by tests.

- Symptom: llama.cpp rejects a chat request about system-message ordering.
  Cause: multiple system messages or provider-specific parameters were shaped incorrectly.
  Fix: keep prompt context merged into the first system message and pass llama.cpp extensions through the supported request shape.
