# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Discord bot for the Wuthering Waves game universe, embodying the "Shorekeeper" character. It uses RAG (Retrieval-Augmented Generation) to answer questions based on a structured knowledge base, with configurable LLM backends (local Ollama or online Google Gemini).

## Architecture

### Core Components

- **`core/config.py`**: Centralized configuration via environment variables. Defines `DISCORD_TOKEN`, `GOOGLE_GEMINI_API_KEY`, `USE_ONLINE_MODEL`, `ONLINE_MODEL`, `LOCAL_MODEL`, `MODEL`, and the `SYSTEM_PROMPT` establishing the Shorekeeper persona.
- **`core/bot.py`**: Discord.py client setup with message content intent. Delegates message handling to `handlers/message.py`.
- **`handlers/message.py`**: Main message handler. Filters mentions/replies, classifies queries (`meta`/`casual`/`lore`) to set `top_k`, retrieves RAG context, injects personalization + knowledge manifest into the system prompt, manages conversation history, calls LLM service, and splits long responses.
- **`services/rag.py`**: RAG system. Loads markdown files from `knowledge/`, chunks by `##` headings, embeds using Ollama's `nomic-embed-text` (always uses Ollama for embeddings, regardless of LLM choice), and performs hybrid semantic+keyword search. Stores metadata in `data/vectors.json` (JSON) and embeddings in `data/embeddings.npz` (float16 compressed NumPy). Includes a knowledge manifest builder (`get_manifest()`) that enumerates all characters/topics for the system prompt.
- **`services/llm.py`**: Unified LLM client. Routes to Ollama (local) or Gemini (online) based on `USE_ONLINE_MODEL`. Returns consistent Ollama-style response format from both backends.
- **`handlers/conversation_context.py`**: In-memory conversation history per server/channel with 16-message limit.
- **`utils/logger.py`**: Logs response metrics (timings, token counts, query classification).

### Query Classification

`handlers/message.py` classifies every incoming query before RAG retrieval:

| Type | Pattern | `top_k` | Behavior |
|------|---------|---------|----------|
| `meta` | "how many", "which characters", "list all", etc. | 0 | Skips RAG — relies on the knowledge manifest |
| `casual` | "hello", "how are you", "good morning", etc. | 2 | Light retrieval for conversational queries |
| `lore` | Everything else | 5 | Full retrieval for character/lore/ability queries |

### RAG Search Algorithm

The RAG system uses a **hybrid search** approach:
1. **Semantic similarity** (70% weight): Cosine similarity between query and chunk embeddings using `nomic-embed-text`
2. **Keyword matching** (30% weight): Stem-matching (first 4 chars) against source paths, headings, labels, body text, and metadata fields (character, region, group, tags)
3. **Metadata boosting**: Chunks with `importance: "high"` get 10% score boost, `importance: "low"` get 10% penalty
4. **Character disambiguation**: Strong weighting for character name matches in source paths and metadata

### Knowledge Manifest

`rag.get_manifest()` builds a structured index of all characters and lore topics in the knowledge base, grouped by faction/region. This manifest is injected into every system prompt so the bot can accurately answer "what do you know?" queries without RAG retrieval.

### Knowledge Base Structure

- `knowledge/characters/` – Character profiles, kits, stories (subdirectories by region/character)
  - `black_shores/` – Shorekeeper, Camellya, Chisa, Encore
  - `jinzhou/` – Changli, Jinhsi, Jiyan, Yinlin
  - `rinascita/` – Augusta, Brant, Cantarella, Carlotta, Cartethyia, Ciaccona, Galbrena, Iuno, Lupa, Phoebe, Phrolova, Zani (12 characters)
  - `new_federation/` – Verina
- `knowledge/lore/` – Game world lore
  - `regions/` – Black Shores, Huanglong, Rinascita
  - `solaris-iii/` – Entities, factions, history, world overview, metaphysics
- `knowledge/personalization/` – Shorekeeper personality, backstory, relationships (always fully injected, never retrieved by similarity)
- `knowledge/references/` – Format guides and reference materials (excluded from RAG entirely)

Files are markdown with YAML frontmatter metadata, chunked at `##` headings. The RAG system extracts human-readable labels from file paths and uses metadata for improved search accuracy.

### Dual Storage System

- **`data/vectors.json`**: Metadata-only JSON (chunk text, source, heading, label, metadata). No embeddings stored here.
- **`data/embeddings.npz`**: Binary NumPy file with all embeddings stored as float16 (compressed). Upcast to float32 at load time for computation accuracy.

### Bot Initialization Flow

1. `main.py` loads config, builds RAG knowledge base (`rag.build()`), prints knowledge manifest, starts Discord bot
2. RAG loads markdown files from `knowledge/`, embeds chunks, saves metadata to `data/vectors.json` and embeddings to `data/embeddings.npz`
3. LLM client initializes based on `USE_ONLINE_MODEL` (Gemini if online, Ollama if local)
4. Discord bot runs with token from config
5. On message: check mention/reply → classify query (`meta`/`casual`/`lore`) → RAG search (if not meta) → construct system prompt with personalization + manifest → get conversation history → call LLM → log → reply

## Common Commands

### Environment Setup

```bash
# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
echo "DISCORD_TOKEN=your_token_here
GOOGLE_GEMINI_API_KEY=your_key_here
ONLINE_MODEL=gemini-2.5-flash-lite-preview-09-2025
LOCAL_MODEL=your_local_model" > .env.local
```

### Running the Bot

```bash
# Main Discord bot (builds RAG on startup)
python main.py
```

### Testing & Validation

```bash
# Run comprehensive RAG tests across characters, mechanics, lore
python tests/test_rag.py

# Test specific character lore retrieval
python tests/test_phrolova_lore.py

# Analyze knowledge base statistics
python commands/check_knowledge.py

# Test RAG search for a specific query
python -c "from services.rag import RAG; r=RAG(); r.load(); print(r.search('your query'))"
```

### Knowledge Base Management

```bash
# Rebuild RAG vectors after modifying knowledge/ files
python -c "from services.rag import RAG; r=RAG(); r.build()"

# Add YAML frontmatter to existing markdown files (after adding new files)
python commands/add_frontmatter.py

# Update vectors.json with metadata without re-embedding
python commands/update_vectors_with_metadata.py

# Move .bak backup files from knowledge/ to knowledge_backups/
python commands/move_backups.py
```

## Configuration Notes

- **Model Switching**: Set `USE_ONLINE_MODEL = True` in `core/config.py` for Gemini, `False` for Ollama.
- **Embedding Requirement**: The RAG system always uses Ollama's `nomic-embed-text` for embeddings, even when using Gemini for LLM responses. Ensure Ollama is running.
- **Local Models**: Ensure Ollama is running with the model specified in `LOCAL_MODEL` (default from `.env.local`).
- **Discord Permissions**: Bot requires `message_content` intent enabled in Discord Developer Portal.
- **Environment**: All secrets are loaded from `.env.local` via `python-dotenv`.

## Development Patterns

- **Adding Knowledge**: Add markdown files to appropriate `knowledge/` subdirectory. Follow shared rules in `knowledge/references/FORMAT_GUIDE.md` and the specialized reference guides in `knowledge/references/` for character or region file structure. Use `##` headings for automatic chunking.
- **Extending LLM Support**: Add new backend methods in `services/llm.py` following the existing pattern. The `_response_to_text()` method robustly extracts text from various SDK response shapes.
- **Conversation Memory**: History is stored in memory only, reset on bot restart. Modify `conversation_context_limit` in `handlers/conversation_context.py` to adjust.
- **Response Formatting**: Long messages are split at line breaks or spaces under 2000 chars via `split_message()` in `handlers/message.py`.
- **Query Classification**: Edit `_META_PATTERNS`, `_CASUAL_PATTERNS`, and `_TOP_K` in `handlers/message.py` to tune retrieval behavior per query type.

## Key Files for Modification

- **Bot Personality**: `core/config.py` `SYSTEM_PROMPT` and `knowledge/personalization/`
- **RAG Behavior**: `services/rag.py` search scoring, chunking logic, manifest building
- **LLM Integration**: `services/llm.py` model configuration and response formatting
- **Message Handling**: `handlers/message.py` filtering, query classification, context construction, response processing

## Reference Documentation

- **`ROADMAP.md`**: Planned features and improvements (hot reload, slash commands, reranking)
- **`knowledge/references/FORMAT_GUIDE.md`**: Shared formatting rules for all knowledge files; see the specialized guides in the same folder for character and region templates
- **`commands/add_frontmatter.py`**: Script to add YAML metadata to markdown files
- **`commands/update_vectors_with_metadata.py`**: Update vector store with new metadata
- **`commands/move_backups.py`**: Move `.bak` backup files from `knowledge/` to `knowledge_backups/`