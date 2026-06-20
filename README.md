# Shorekeeper Bot

Shorekeeper Bot is now organized as a small monorepo with:

- a Discord + RAG runtime in `backend/brain`
- a FastAPI service scaffold in `backend/server`
- a Vite + React + TypeScript app in `frontend`

The bot now prefers a local `llama.cpp` server through its OpenAI-compatible API, with Ollama kept only as a legacy compatibility path.

## Current Architecture

```
shorekeeper_bot/
├── backend/
│   ├── pyproject.toml              Python dependencies (managed with uv)
│   ├── requirements.txt
│   ├── brain/                      Discord + RAG runtime
│   │   ├── main.py                 Bot entrypoint
│   │   ├── core/                   Config and Discord wiring
│   │   ├── handlers/               Message orchestration + chat history
│   │   ├── services/               RAG, embedder, LLM client
│   │   ├── knowledge/              Markdown knowledge corpus
│   │   ├── data/                   vectors.json + embeddings.npz
│   │   ├── commands/               Maintenance scripts
│   │   └── tests/                  Retrieval and regression tests
│   └── server/
│       └── main.py                 FastAPI app scaffold (`/` and `/health`)
├── frontend/                       Vite + React + TypeScript scaffold
├── .env.local                      Runtime environment variables
└── backend/uv.lock                 Locked Python dependency graph
```

## Prerequisites

- Python 3.14+
- `uv` (recommended dependency installer)
- Node.js 20+
- Two local `llama-server` instances: one for chat and one for embeddings
- Docker Compose for the local SearXNG runtime

## Setup

### 1) Python environment (uv)

```bash
cd backend
uv sync --dev
cd ..
```

### 2) Frontend

```bash
cd frontend
npm ci
cd ..
```

### 3) Pre-commit hooks

Install the repo-level hook after syncing backend dev dependencies:

```bash
cd backend
uv run pre-commit install --config ../.pre-commit-config.yaml --hook-type pre-commit
cd ..
```

The root hook dispatches to the backend and frontend pre-commit configs.

### 4) Environment variables

Copy `.env.example` to `.env.local` and adjust as needed:

```bash
cp .env.example .env.local
```

Default `.env.local` now keeps secrets and feature toggles:

```env
DISCORD_TOKEN=your_discord_bot_token
ONLINE_LLM_API_KEY=your_openrouter_api_key
LOCAL_API_KEY=no-key
EMBED_API_KEY=no-key

SEARCH_ENABLED=false
MEMORY_ENABLED=true
```

Grouped runtime settings now live in the YAML files:

- `config/runtime.config.yml`: provider selection, llama.cpp URLs, model aliases, model paths, launcher tuning, memory tuning, analysis thresholds, and router limits
- `config/search.config.yml`: SearXNG provider, limits, domain trust lists, and topic overrides

Example local startup with `llama.cpp`:

```bash
cd ~/llama.cpp/build/bin

# Chat model
./llama-server \
  -m /mnt/sdb4/models/shorekeeper.gguf \
  --alias shorekeeper \
  --host 127.0.0.1 \
  --port 8081 \
  -ngl 999 \
  --no-mmap \
  -c 65536 \
  --parallel 1 \
  -t 12 \
  -fa on \
  --cache-type-k q4_0 \
  --cache-type-v q4_0 \
  --temp 0.3 \
  --top-p 0.9 \
  --top-k 40 \
  --repeat-penalty 1.05 \
  --jinja \
  --metrics

# Dedicated embedding model
./llama-server \
  -m /mnt/sdb4/models/nomic-embed-text.gguf \
  --alias nomic-embed-text \
  --host 127.0.0.1 \
  --port 8082 \
  --embeddings \
  --pooling cls \
  -ngl 999 \
  --no-mmap \
  -t 12 \
  --metrics
```

The alias is important: the app sends whatever you set in `LOCAL_MODEL` to `LOCAL_BASE_URL`, and whatever you set in `EMBED_MODEL` to `EMBED_BASE_URL`.

Live search grounding expects a JSON-capable SearxNG instance at the `base_url` configured in `config/search.config.yml`. It is disabled by default and is intended for the Discord `/search` slash command when you explicitly turn it on.

### 4) Local SearXNG runtime

Create a local override file for the compose stack if you want to change the tracked defaults:

```bash
cp infra/searxng/.env.example infra/searxng/.env
```

The bot-facing local runtime is bound to `127.0.0.1:8083` only and uses the repo-owned config in `infra/searxng/core-config/settings.yml`.

Start, stop, and inspect it with:

```bash
docker compose -f infra/searxng/docker-compose.yml up -d
docker compose -f infra/searxng/docker-compose.yml down
docker compose -f infra/searxng/docker-compose.yml ps
docker compose -f infra/searxng/docker-compose.yml logs -f
```

SearXNG JSON verification:

```bash
curl "http://127.0.0.1:8083/search?q=latest%20Wuthering%20Waves%20update&format=json"
```

If you want one command instead of two terminals, use the bundled launcher:

```bash
./scripts/start-llama-local.sh
```

It starts both `llama-server` processes plus the local SearXNG Docker Compose stack, then stops all of them on `Ctrl-C`. It reads `.env.local`, uses `infra/searxng/docker-compose.yml`, and fails fast if any required launcher variable, binary, or compose file is missing.
The launcher reads grouped llama settings directly from `config/runtime.config.yml`.

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

## Bot Runtime Notes

- Query classes in `backend/brain/handlers/message.py`: `meta`, `casual`, `lore`
- Normal mention/reply chat no longer auto-searches the web for current facts.
- Live web search now runs through the Discord `/search` slash command when `SEARCH_ENABLED=true`.
- RAG data artifacts:
  - `backend/brain/data/vectors.json`
  - `backend/brain/data/embeddings.npz`
- Knowledge corpus location: `backend/brain/knowledge`

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

1. Run `./scripts/start-llama-local.sh` to start PostgreSQL, SearXNG, and the llama.cpp chat and embedding servers together.
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
