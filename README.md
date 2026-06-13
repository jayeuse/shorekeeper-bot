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
└── uv.lock                         Locked Python dependency graph
```

## Prerequisites

- Python 3.14+
- `uv` (recommended dependency installer)
- Node.js 20+
- Two local `llama-server` instances: one for chat and one for embeddings

## Setup

### 1) Python environment (uv)

```bash
python -m venv .venv
source .venv/bin/activate

cd backend
uv pip install -r requirements.txt
cd ..
```

### 2) Frontend

```bash
cd frontend
npm install
cd ..
```

### 3) Environment variables

Copy `.env.example` to `.env.local` and adjust as needed:

```bash
cp .env.example .env.local
```

Default `.env.local` values for your local `llama.cpp` setup:

```env
DISCORD_TOKEN=your_discord_bot_token
ONLINE_API_KEY=your_deepseek_api_key
ONLINE_BASE_URL=https://api.deepseek.com
ONLINE_MODEL=deepseek-chat

LLM_PROVIDER=llamacpp
EMBEDDING_PROVIDER=llamacpp
LLAMA_BIN_DIR=$HOME/llama.cpp/build/bin
LOCAL_BASE_URL=http://127.0.0.1:8081/v1
LOCAL_API_KEY=no-key
LOCAL_MODEL=shorekeeper
CHAT_MODEL_PATH=/mnt/sdb4/models/shorekeeper.gguf

EMBED_BASE_URL=http://127.0.0.1:8082/v1
EMBED_API_KEY=no-key
EMBED_MODEL=nomic-embed-text
EMBED_MODEL_PATH=/mnt/sdb4/models/nomic-embed-text.gguf
```

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

If you want one command instead of two terminals, use the bundled launcher:

```bash
./scripts/start-llama-local.sh
```

It starts both `llama-server` processes in one terminal and stops both on `Ctrl-C`. It reads only `.env.local` and fails fast if any required launcher variable is missing, so config errors surface immediately instead of being hidden by script defaults.

## Running

### Run Discord bot runtime

```bash
source .venv/bin/activate
python backend/brain/main.py
```

### Run FastAPI backend

```bash
source .venv/bin/activate
uvicorn backend.server.main:app --host 127.0.0.1 --port 8001 --reload
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

# RAG regression scripts
python tests/test_rag.py
python tests/test_phrolova_lore.py
python tests/test_rag_entity_fallback.py
```

## Security Reminder

- Keep `.env.local` out of version control.
- If any token/key is ever exposed, rotate it immediately.
