# Shorekeeper Bot

Shorekeeper Bot is a specialized **orchestration wrapper** that wraps local and online Large Language Models (LLMs) with a layer of structured prompting, context grounding, and routing logic to make them act consistently as **The Shorekeeper** — a character from *Wuthering Waves*. 

Instead of treating the AI model as an opaque black box, Shorekeeper Bot acts as a control plane around it. It intercepts every interaction, runs classification and routing passes, dynamically gathers context from a curated knowledge base or user memories, and constructs a highly structured prompt environment. This forces the underlying model—whether running locally via `llama.cpp` or through an external API—to maintain a precise persona, retrieve factual lore, and recall user details without relying on external hosted companion services.

## Why This Exists

Most Discord LLM integrations are simple, stateless API pass-throughs that result in generic, forgetful chat experiences, while dedicated "AI companion" platforms lock your data and configuration into proprietary cloud services. 

Shorekeeper Bot is designed as a **self-hosted, model-agnostic orchestration wrapper** that provides:

- **Model Agnosticism** — The wrapper sits in front of any OpenAI-compatible API (local `llama.cpp` / Ollama servers or remote endpoints like DeepSeek or OpenRouter), allowing you to swap the underlying model backend at any time while preserving the character logic.
- **Curated Knowledge Wrapper (RAG)** — Rather than hoping the model has memorized game lore, a retrieval-augmented generation pipeline extracts context from hand-written markdown files (about characters, lore, and abilities) and wraps the user prompt with explicit source-grounding instructions.
- **Persistent Memory Context** — A background memory system captures and compacts conversation history into structured user profiles stored in PostgreSQL, dynamically injecting this information back into the LLM context so the character "remembers" users across sessions.
- **Verified Search Grounding** — Live web search through a private SearXNG instance is exposed via a dedicated `/search` command, passing results through a multi-stage evidence evaluation pipeline to constrain what the model is allowed to claim before it answers.

## System Architecture

The project is organized as a monorepo with three main surfaces:

```
shorekeeper_bot/
├── backend/
│   ├── brain/                      Discord bot runtime + RAG + memory
│   │   ├── main.py                 Bot entrypoint
│   │   ├── core/                   Config parsing, Discord client wiring
│   │   ├── handlers/               Message orchestration, routing, /search command
│   │   ├── services/               RAG engine, LLM client, embedder, search, memory
│   │   ├── database/               SQLModel models, migrations, engine setup
│   │   ├── knowledge/              Markdown knowledge corpus (characters, lore, persona)
│   │   ├── data/                   Generated vectors.json + embeddings.npz
│   │   ├── commands/               Maintenance CLIs (rebuild index, verify connectivity)
│   │   ├── utils/                  Structured logging
│   │   └── tests/                  Retrieval regression and smoke tests
│   ├── server/                     FastAPI service scaffold (routes, schemas, models)
│   ├── alembic/                    Database migration versions
│   └── pyproject.toml              Python dependencies (managed with uv)
├── frontend/                       Vite + React 19 + TypeScript client scaffold
├── config/
│   ├── runtime.config.yml          Provider selection, model settings, memory tuning
│   └── search.config.yml           SearXNG provider, domain trust lists, extraction rules
├── infra/
│   ├── searxng/                    Local SearXNG Docker Compose stack
│   └── postgres/                   Local PostgreSQL Docker Compose stack
├── scripts/
│   └── start.sh                    One-command launcher for all local services
├── .env.example                    Environment variable template
└── .env.local                      Local runtime secrets (not committed)
```

### Runtime Components

The bot runtime requires four services running together:

| Service | Default Address | Purpose |
|---|---|---|
| **llama.cpp chat server** | `127.0.0.1:8081` | Serves the fine-tuned/quantized chat model via OpenAI-compatible API |
| **llama.cpp embed server** | `127.0.0.1:8082` | Serves the embedding model (Nomic Embed Text) for RAG queries |
| **PostgreSQL** | `127.0.0.1:5432` | Stores user memories and knowledge vectors |
| **SearXNG** | `127.0.0.1:8083` | Private meta-search engine for live web grounding (optional) |

All four can be started together with `./scripts/start.sh`, which reads `.env.local` and `config/runtime.config.yml`, launches both llama servers, and brings up the Docker Compose stacks. It stops everything cleanly on `Ctrl-C`.

## Core Features

### Message Pipeline

The core wrapper logic is driven by the [message handler](backend/brain/handlers/message.py), which orchestrates every incoming Discord message through a multi-stage control pipeline to safely construct the LLM's prompt context:

```
User message → Analysis Router → Route Plan → Source Resolution → System Prompt Assembly → LLM → Reply
```

**1. Analysis Router** — The user's message is sent to the LLM itself as a lightweight classification pass. It produces a JSON object with three fields: a standalone `rag_query` (resolving elliptical follow-ups like "what about her?"), a `reason`, and a `query_type`. This runs with a configurable timeout (default 6s) and falls back to heuristic normalization on failure.

**2. Query Classification** — Messages are classified into one of five types:

| Type | Behavior |
|---|---|
| `datetime` | Answered deterministically from the system clock — no LLM call |
| `casual` | Greetings and small talk — routed directly to the LLM with no retrieval |
| `meta` | Questions about the bot itself or past conversation |
| `memory` | Questions about a user's identity or what the bot remembers about them |
| `general` | Everything else — triggers RAG eligibility checks and knowledge retrieval |

**3. RAG Evaluation** — For `general` queries, the system checks whether the question is eligible for RAG retrieval based on the inferred question type. Questions about definitions, identity, current metrics, or latest releases are excluded. Eligible queries go through semantic + keyword search, and the top score is compared against a configurable threshold (default `0.62`). If accepted, the retrieved knowledge chunks are injected into the system prompt as the sole source of truth.

**4. Memory Injection** — If long-term memory exists for the current user (or a mentioned user), the compacted memory profile is injected into the system prompt. The bot also performs **cross-user matching**: if user A asks "what do you know about CeeJay?", the system searches all server memory records for an identifier match and loads that user's memory profile, clearly annotating in the prompt that the memory describes someone else.

**5. System Prompt Assembly** — The final system prompt is composed from multiple sections: the core character prompt (Shorekeeper identity, voice rules, grounding rules), personalization context (backstory, personality, relationships from the knowledge corpus), the knowledge manifest (enumeration of all known characters and topics), the resolved query interpretation, and any source-specific context (RAG chunks, search results, or memory).

**6. Reply** — The assembled message list is sent to the LLM. Responses are split at 2000-character Discord boundaries with intelligent line-break splitting. After replying, the system checks whether memory compaction should be triggered.

### RAG Pipeline

The [RAG service](backend/brain/services/rag.py) provides retrieval-augmented generation from a curated Markdown knowledge corpus:

- **Knowledge corpus** (`backend/brain/knowledge/`) is organized into `characters/` (grouped by faction), `lore/` (regions and world-building), and `personalization/` (backstory, personality, relationships that define the bot's persona).
- **Chunking** — Each markdown file is split on `## ` headings. YAML frontmatter (character name, group, region, importance, tags) is parsed and preserved as metadata per chunk.
- **Embedding** — Chunks are embedded using a dedicated embedding model (default: Nomic Embed Text v1.5) served via a separate llama.cpp instance. Embeddings are stored as compressed float16 NumPy arrays (`embeddings.npz`) for disk efficiency and upcast to float32 at query time.
- **Hybrid search** — Retrieval uses a weighted combination of cosine similarity (70%) and keyword boost (30%). Keyword scoring considers matches in headings, source paths, labels, and metadata fields (character, region, group, tags) with graduated weights.
- **Entity rescue** — When the top semantic results don't mention the entity the user asked about (e.g., asking about "Camellya" but getting generic lore chunks), an entity rescue pass re-scores all chunks with a boost for entity name matches in headings, text, source, labels, and metadata. This fires when the top score is below `0.62` or when the top-K chunks fail to mention the target entity.
- **Manifest generation** — The RAG builds a structured manifest listing every character and lore topic in the knowledge base, grouped by faction/category. This manifest is injected into every system prompt so the bot can accurately enumerate what it knows without fabricating names.
- **Database persistence** — On rebuild, vectors are also written to PostgreSQL via SQLModel for potential future server-side retrieval.

### Memory System

The [user memory service](backend/brain/services/user_memory.py) gives the bot persistent, evolving knowledge about individual users:

- **Short-term context** — Conversation turns are stored in-memory per user per server, capped at a configurable limit (default 16 turns). This provides immediate conversational context.
- **Long-term compaction** — When the short-term buffer fills, a background task snapshots the conversation and sends it to the LLM with a structured compaction prompt. The LLM extracts a structured profile with fields for `Identifier`, `Interests` (subject + reason), `Personality` (3–8 word bot impression), and `Facts` (pipe-delimited traits). The result is stored in PostgreSQL with versioning, topic labels, importance scores, and tags.
- **Memory evolution** — Each compaction merges the new conversation with any existing memory, resolving contradictions in favor of more recent data. The memory version increments on each compaction.
- **Cross-user recall** — Users can ask the bot about other users. The system scans all server memory records for identifier matches in the user's message and injects the matching record into the system prompt with clear annotation distinguishing "who the memory describes" from "who is asking."
- **Concurrency safety** — A per-user compaction lock prevents overlapping compaction tasks for the same user.

### Live Web Search

The [search service](backend/brain/services/search.py) provides grounded, evidence-evaluated web search through a private SearXNG instance:

- **Slash command interface** — Search is exposed as a `/search` Discord slash command, not as automatic behavior on regular messages. This is intentional: the bot should answer lore from its knowledge base and remember users from memory, not reflexively web-search every question.
- **Search planning** — Queries are analyzed to extract a target entity, requested fact type, question type (current metric, latest release, background fact, etc.), and subject domain (finance, game, language). This metadata drives result scoring.
- **Result classification** — Each search result is classified by source trust tier (official → reference → news → community → fallback → demoted → blocked), surface type (wiki page, patch notes, store page, news post, guide, etc.), and freshness bucket (recent ≤14d, aging ≤90d, stale >180d). Scoring weights entity match, fact match, specificity, source trust, and freshness into a composite rank.
- **Page extraction** — The top results can have their full page content extracted using `trafilatura`, with extensive safety controls: domain allowlisting, private IP blocking, DNS resolution verification, redirect limits, response byte caps, and content-type filtering.
- **Evidence evaluation** — After ranking and extraction, the system evaluates the overall evidence bundle: agreement status across sources (agree/disagree/single), confidence level, and whether the evidence is strong enough to allow exact claims (specific numbers, dates, versions). This evaluation drives the `response_mode` (exact/summary/uncertain) and constrains what the LLM is allowed to assert.
- **Domain trust configuration** — `config/search.config.yml` defines tiered domain trust lists (official sources, reference sources, news sources), demoted domains (social media, app stores), and per-topic overrides (e.g., finance queries prefer NASDAQ and Yahoo Finance; game queries prefer official game sites).

### Configuration System

Configuration is split between environment variables and YAML files:

- **`.env.local`** — Secrets and feature toggles: Discord token, API keys, `SEARCH_ENABLED`, `MEMORY_ENABLED`.
- **`config/runtime.config.yml`** — Provider selection (`llamacpp`/`openai`/`ollama`), llama.cpp server URLs and model aliases, launcher settings (GPU layers, threads, sampling parameters), memory tuning (turn limits, compaction timeout), analysis thresholds, and router limits.
- **`config/search.config.yml`** — SearXNG endpoint, timeouts, result limits, page extraction settings, domain trust tiers, demoted domains, and per-topic domain overrides.

The [config loader](backend/brain/core/config_loaders.py) merges environment variables with YAML file values, with environment variables taking precedence. This allows the same YAML files to work across environments while secrets stay in `.env.local`.

### LLM Client

The [LLM client](backend/brain/services/llm.py) supports three provider backends:

| Provider | Backend | Use Case |
|---|---|---|
| `llamacpp` | Local llama.cpp via OpenAI-compatible API | Default — fully local inference |
| `openai` | Remote OpenAI-compatible endpoint (OpenRouter, DeepSeek, etc.) | Cloud fallback or higher-capability models |
| `ollama` | Local Ollama server | Legacy compatibility path |

The client auto-strips `<think>` blocks from reasoning models and normalizes responses into a consistent internal format regardless of provider.

---

## Prerequisites

- **Python 3.14+** & **`uv`** (Python package & dependency manager)
- **Node.js 20+** (for the frontend web client)
- **Docker & Docker Compose** (for PostgreSQL and SearXNG database/search containers)
- **`llama-server`** (compiled executable from the `llama.cpp` project)
- **GGUF Models** (a chat model and a text embedding model like Nomic Embed)

## Setup

### 1. Install Dependencies
```bash
# Backend dependencies
cd backend
uv sync --dev
cd ..

# Frontend dependencies
cd frontend
npm ci
cd ..

# Pre-commit hooks (optional)
cd backend
uv run pre-commit install --config ../.pre-commit-config.yaml --hook-type pre-commit
cd ..
```

### 2. Configure Environment Variables
Copy the template `.env.example` to `.env.local` and fill in your local system details:
```bash
cp .env.example .env.local
```
Key paths to specify include:
- `LLAMA_BIN_DIR`: Absolute path to the folder containing your compiled `llama-server` binary.
- `CHAT_MODEL_PATH` and `EMBED_MODEL_PATH`: Absolute paths to your chat and embedding `.gguf` model files.
- Discord token (`DISCORD_TOKEN`) and optional feature keys.

Fine-grained runtime configurations (e.g. GPU layer offloading, prompt parameters, context sizes, search engine overrides) are managed in [config/runtime.config.yml](file:///mnt/sdb4/Programming/Python/AI/Local-AI/shorekeeper_bot/config/runtime.config.yml) and [config/search.config.yml](file:///mnt/sdb4/Programming/Python/AI/Local-AI/shorekeeper_bot/config/search.config.yml).

### 3. Launch Local Infrastructure
Instead of starting each service manually, use the unified launcher script, [start.sh](file:///mnt/sdb4/Programming/Python/AI/Local-AI/shorekeeper_bot/scripts/start.sh), which spins up the entire local environment in a single command:
```bash
./scripts/start.sh
```

This script reads `.env.local` and your configuration files to automatically:
1. Start **PostgreSQL** (Docker Compose) for persistent user memory.
2. Start **SearXNG** (Docker Compose) for live web search capabilities.
3. Start the **`llama-server` Chat Server** (configured context length, GPU offloading, temperature, etc.).
4. Start the **`llama-server` Embedding Server** (running parallel embedding calls).

To tear down all local infrastructure (shutting down Docker containers and stopping background llama servers), press `Ctrl-C` in that terminal.

## Running

### Run Discord bot runtime

```bash
cd backend
uv run python brain/main.py
```

### Run FastAPI backend

```bash
cd backend
uv run uvicorn server.main:app --host 127.0.0.1 --port 8001 --reload
```

Health check:

```bash
curl http://127.0.0.1:8001/health
```

### Run frontend

```bash
cd frontend
npm run dev
```

## Common Backend Commands

```bash
cd backend/brain

# Knowledge stats
python commands/check_knowledge.py

# Update vector metadata
python commands/update_vectors_with_metadata.py

# Rebuild vectors/embeddings from knowledge files
python -c "from services.rag import RAG; RAG().build()"

# Verify chat connectivity
python commands/verify_online_model.py

# Verify live search connectivity
python commands/verify_search.py

# RAG regression scripts
python tests/rag_smoke.py
python tests/phrolova_lore_smoke.py
python tests/test_rag_entity_fallback.py
```

## Local Startup Order

Bring the local runtime up in this order:

1. Run `./scripts/start.sh` to start PostgreSQL, SearXNG, and the llama.cpp chat and embedding servers together.
2. Run `cd backend && uv run python brain/commands/verify_online_model.py`.
3. Run `cd backend && uv run python brain/commands/verify_search.py`.
4. Start the Discord bot with `cd backend && uv run python brain/main.py`.

Shorekeeper live search is considered ready only when `verify_search.py` succeeds against `SEARCH_BASE_URL`.

## Quality Gates

The installed pre-commit hook runs the backend and frontend validation suites before each commit.
Run the same dispatcher manually from the repo root with:

```bash
cd backend
uv run pre-commit run --config ../.pre-commit-config.yaml --all-files
```

Equivalent manual commands are:

```bash
cd backend
uv run ruff format --check .
uv run ruff check .
uv run mypy
uv run pytest

cd ../frontend
npm run audit
npm run check
```

Model-backed retrieval smoke scripts remain manual because they require local chat and embedding servers.

## Security Reminder

- Keep `.env.local` out of version control.
- If any token/key is ever exposed, rotate it immediately.
