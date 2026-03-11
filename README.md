# Shorekeeper Bot

A Discord bot that roleplays as **Shorekeeper** from the game *Wuthering Waves*. It uses a custom RAG (Retrieval-Augmented Generation) pipeline backed by a structured knowledge base to answer questions about game lore, character abilities, and story — while staying in character at all times.

Supports two LLM backends: a **local** Ollama model or **Google Gemini** online.

---

## Features

- In-character roleplay as Shorekeeper with a persistent persona
- RAG search over a rich knowledge base (21 characters, lore, game mechanics)
- Hybrid semantic + keyword retrieval with metadata-based scoring
- Smart query classification — adjusts retrieval depth per query type
- Knowledge manifest — auto-generated index injected into every prompt for accurate "what do you know?" answers
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
      ├── _classify_query()   → meta / casual / lore (sets top_k = 0 / 2 / 5)
      ├── services/rag.py     → retrieve top-k knowledge chunks (hybrid search)
      ├── rag.get_personalization_context() → always-injected persona
      ├── rag.get_manifest()  → structured character/topic index
      ├── handlers/conversation_context.py → sliding window history
      ├── Build prompt: [system + persona + manifest] + [history] + [RAG context] + [user msg]
      ├── services/llm.py     → call Ollama or Gemini
      └── utils/logger.py     → log timing, tokens, and query classification
```

### Key design decisions

- **Personalization is always injected** — `knowledge/personalization/` is fully prepended to every system prompt rather than retrieved by similarity, ensuring stable character behavior.
- **Knowledge manifest is always injected** — a structured index of all characters/topics is included in every prompt so the bot can accurately enumerate what it knows.
- **Embeddings are always local** — `nomic-embed-text` via Ollama is the sole embedding model; Gemini is used only for generation.
- **No RAG framework** — the pipeline is custom-built on NumPy + JSON with no LangChain or LlamaIndex dependency.
- **Dual storage** — metadata lives in JSON (`vectors.json`), embeddings in compressed float16 NumPy (`embeddings.npz`) for minimal disk usage.
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

On startup, `main.py` builds (or loads) the vector store from `data/vectors.json` + `data/embeddings.npz`. If the files don't exist, all knowledge files are embedded and cached automatically. The knowledge manifest is printed to the console on launch.

---

## Knowledge Base

All knowledge is stored as Markdown files under `knowledge/` with YAML frontmatter and `##` heading-based chunking.

```
knowledge/
├── characters/
│   ├── black_shores/     # Shorekeeper, Camellya, Chisa, Encore
│   ├── jinzhou/          # Changli, Jinhsi, Jiyan, Yinlin
│   ├── new_federation/   # Verina
│   └── rinascita/        # Augusta, Brant, Cantarella, Carlotta, Cartethyia,
│                         # Ciaccona, Galbrena, Iuno, Lupa, Phoebe,
│                         # Phrolova, Zani (12 characters)
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

### Query classification

Before retrieval, each query is classified to determine retrieval depth:

| Type | Triggers | `top_k` | Example |
|------|----------|---------|---------|
| `meta` | "how many", "which characters", "list all" | 0 | "Which characters do you know about?" |
| `casual` | "hello", "how are you", "good morning" | 2 | "Hey, how are you?" |
| `lore` | Everything else | 5 | "How does Shorekeeper's healing work?" |

### Hybrid search scoring

| Component | Weight | Description |
|-----------|--------|-------------|
| Semantic similarity | 70% | Cosine similarity of query vs chunk embedding |
| Keyword matching | 30% | Stem-matching against source, heading, label, body, metadata |
| Importance boost | ±10% | `×1.1` for `importance: high`, `×0.9` for `importance: low` |

### Vector cache

Embeddings are cached across two files in `data/`:

| File | Format | Contents |
|------|--------|----------|
| `vectors.json` | JSON | Chunk metadata (text, source, heading, labels) — no embeddings |
| `embeddings.npz` | Compressed NumPy | Float16 embedding vectors — upcast to float32 at load time |

Rebuild after modifying knowledge files:

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
| `python commands/move_backups.py` | Move `.bak` backup files from `knowledge/` to `knowledge_backups/` |

---

## Testing & Validation

```bash
# Comprehensive RAG evaluation (~35 queries across all topics)
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
| `numpy` | 2.4.2 | Cosine similarity and embedding storage |
| `pyyaml` | latest | YAML frontmatter parsing |
| `tabulate` | latest | Knowledge base statistics formatting |

---

## Project Structure

```
shorekeeper_bot/
├── main.py                   Entry point
├── core/
│   ├── bot.py                Discord client
│   └── config.py             Configuration and system prompt
├── handlers/
│   ├── message.py            Main message orchestrator + query classifier
│   └── conversation_context.py  Per-channel history
├── services/
│   ├── rag.py                RAG pipeline (build, search, personalization, manifest)
│   └── llm.py                Unified LLM client (Ollama / Gemini)
├── utils/
│   └── logger.py             Response metrics logging
├── knowledge/                Markdown knowledge base
├── data/
│   ├── vectors.json          Cached chunk metadata (JSON)
│   └── embeddings.npz        Cached embeddings (float16 NumPy)
├── commands/                 Maintenance scripts
├── tests/                    RAG evaluation scripts
└── knowledge_backups/        Backup files from frontmatter migration
```
