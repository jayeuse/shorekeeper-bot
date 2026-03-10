# Shorekeeper Bot

A Discord bot that roleplays as **Shorekeeper** from the game *Wuthering Waves*. It uses a custom RAG (Retrieval-Augmented Generation) pipeline backed by a structured knowledge base to answer questions about game lore, character abilities, and story — while staying in character at all times.

Supports two LLM backends: a **local** Ollama model or **Google Gemini** online.

---

## Features

- In-character roleplay as Shorekeeper with a persistent persona
- RAG search over a rich knowledge base (characters, lore, game mechanics)
- Hybrid semantic + keyword retrieval with metadata-based scoring
- Per-server/channel conversation memory (sliding window, in-memory)
- Configurable local (Ollama) or online (Gemini) LLM backends
- Embeddings always via `nomic-embed-text` through Ollama, even in Gemini mode

---

## Architecture

```
Discord Message
      │
      ▼
core/bot.py                   Discord client — routes messages to handler
      │
      ▼
handlers/message.py           Orchestrator:
      ├── Filter @mentions / replies
      ├── services/rag.py      → retrieve top-k knowledge chunks (hybrid search)
      ├── handlers/conversation_context.py → sliding window history
      ├── Build prompt: [system + persona] + [history] + [RAG context] + [user msg]
      ├── services/llm.py      → call Ollama or Gemini
      └── utils/logger.py      → log timing and token metrics
```

### Key design decisions

- **Personalization is always injected** — `knowledge/personalization/` is fully prepended to every system prompt rather than retrieved by similarity, ensuring stable character behavior.
- **Embeddings are always local** — `nomic-embed-text` via Ollama is the sole embedding model; Gemini is used only for generation.
- **No RAG framework** — the pipeline is custom-built on NumPy + JSON with no LangChain or LlamaIndex dependency.
- **In-memory conversation history** — resets on restart by design (simplicity over persistence).

---

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/) running locally (required even when using Gemini, for embeddings)
- `nomic-embed-text` model pulled in Ollama
- A Discord bot token with the `message_content` intent enabled
- *(Online mode only)* A Google Gemini API key

---

## Installation

```bash
# 1. Clone the repository and enter the directory
git clone <repo-url>
cd shorekeeper_bot

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the embedding model
ollama pull nomic-embed-text
```

---

## Configuration

Create a `.env.local` file in the project root:

```env
DISCORD_TOKEN=your_discord_bot_token

# Only needed for online (Gemini) mode:
GOOGLE_GEMINI_API_KEY=your_gemini_api_key
ONLINE_MODEL=gemini-2.5-flash-lite-preview-09-2025

# Ollama model for local mode:
LOCAL_MODEL=your_ollama_model_name
```

To switch between local and online LLM, edit `core/config.py`:

```python
USE_ONLINE_MODEL = False   # True → Gemini, False → Ollama
```

---

## Running

```bash
# Ensure Ollama is running
ollama serve

# Start the bot (builds RAG knowledge base on first run)
python main.py
```

On startup, `main.py` loads (or builds) the vector store from `data/vectors.json`. If the file doesn't exist, all knowledge files are embedded and cached automatically.

There is also a minimal CLI mode that uses Gemini only (no Discord, no RAG):

```bash
python online_bot.py
```

---

## Knowledge Base

All knowledge is stored as Markdown files under `knowledge/` with YAML frontmatter and `##` heading-based chunking.

```
knowledge/
├── characters/
│   ├── black_shores/     # Shorekeeper, Camellya, Chisa
│   ├── jinzhou/          # Changli, Jinhsi, Jiyan
│   └── rinascita/        # 14 characters (Augusta, Brant, Carlotta, ...)
│       Each character:   *_character.md, *_kit.md, *_story.md
├── lore/
│   ├── regions/          # Black Shores, Huanglong, Rinascita
│   └── solaris-iii/      # Entities, factions, history, metaphysics, world
├── personalization/      # personality.md, backstory.md, relationships.md
│                         # ← always fully injected, never retrieved by similarity
└── references/           # Format guides — excluded from RAG entirely
```

### File format

Every `.md` file starts with YAML frontmatter followed by `## Heading` sections. Each `##` section becomes a standalone RAG chunk.

```markdown
---
version: 1.0.0
chunk_strategy: heading_based
source_file: characters/black_shores/shorekeeper/shorekeeper_kit.md
character: Shorekeeper
group: Black Shores
document_type: character_kit
importance: high
tags: [character, kit, combat]
---

## Shorekeeper: Resonance Skill

...
```

See `knowledge/references/FORMAT_GUIDE.md` for the full authoring specification.

---

## RAG System

### Hybrid search scoring

| Component | Weight | Description |
|-----------|--------|-------------|
| Semantic similarity | 70% | Cosine similarity of query vs chunk embedding |
| Keyword matching | 30% | Stem-matching against source, heading, label, body, metadata |
| Importance boost | ±10% | `×1.1` for `importance: high`, `×0.9` for `importance: low` |

### Vector cache

Embeddings are cached in `data/vectors.json`. Rebuild after modifying knowledge files:

```bash
python -c "from services.rag import RAG; r=RAG(); r.build()"
```

---

## Utility Commands

| Command | Description |
|---------|-------------|
| `python commands/add_frontmatter.py` | Add YAML frontmatter to knowledge files (backs up originals first) |
| `python commands/update_vectors_with_metadata.py` | Patch vector cache with new metadata without re-embedding |
| `python commands/check_knowledge.py` | Print knowledge base statistics |

---

## Testing & Validation

```bash
# Comprehensive RAG evaluation (~50 queries across all topics)
python tests/test_rag.py

# Focused lore retrieval test for a specific character
python tests/test_phrolova_lore.py

# Ad-hoc RAG search
python -c "from services.rag import RAG; r=RAG(); r.load(); print(r.search('your query'))"
```

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `discord` | 2.3.2 | Discord API client |
| `ollama` | 0.6.1 | Local LLM and embeddings |
| `google-generativeai` | latest | Gemini online model |
| `python-dotenv` | 1.2.1 | `.env.local` loading |
| `numpy` | 2.4.2 | Cosine similarity |
| `pyyaml` | latest | YAML frontmatter parsing |

---

## Project Structure

```
shorekeeper_bot/
├── main.py                   Entry point
├── online_bot.py             CLI-only Gemini mode
├── core/
│   ├── bot.py                Discord client
│   └── config.py             Configuration and system prompt
├── handlers/
│   ├── message.py            Main message orchestrator
│   └── conversation_context.py  Per-channel history
├── services/
│   ├── rag.py                RAG pipeline (build, search, personalization)
│   └── llm.py                Unified LLM client (Ollama / Gemini)
├── utils/
│   └── logger.py             Response metrics logging
├── knowledge/                Markdown knowledge base
├── data/
│   └── vectors.json          Cached embeddings
├── commands/                 Maintenance scripts
└── tests/                    RAG evaluation scripts
```
