# Shorekeeper Bot

Shorekeeper Bot is now organized as a small monorepo with:

- a Discord + RAG runtime in `backend/brain`
- a FastAPI service scaffold in `backend/server`
- a Vite + React + TypeScript app in `frontend`

The bot still uses local Ollama embeddings and can route generation to local or online providers.

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
- Ollama running locally (required for local embeddings)

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

Create `.env.local` in project root (do not commit real secrets):

```env
DISCORD_TOKEN=your_discord_bot_token
GOOGLE_GEMINI_API_KEY=your_gemini_api_key

LOCAL_MODEL=your_local_ollama_model
LOCAL_EMBED_MODEL=nomic-embed-text:latest

ONLINE_MODEL=gemini-2.5-flash-lite-preview-09-2025
ONLINE_EMBED_MODEL=gemini-embedding-2-preview
ONLINE_EMBED_DIMENSIONS=768
```

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

# RAG regression scripts
python tests/test_rag.py
python tests/test_phrolova_lore.py
python tests/test_rag_entity_fallback.py
```

## Security Reminder

- Keep `.env.local` out of version control.
- If any token/key is ever exposed, rotate it immediately.
