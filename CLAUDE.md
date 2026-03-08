# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Discord bot for the Wuthering Waves game universe, embodying the "Shorekeeper" character. It uses RAG (Retrieval-Augmented Generation) to answer questions based on a structured knowledge base, with configurable LLM backends (local Ollama or online Google Gemini).

## Architecture

### Core Components

- **`core/config.py`**: Centralized configuration via environment variables. Defines `DISCORD_TOKEN`, `GOOGLE_GEMINI_API_KEY`, `USE_ONLINE_MODEL`, `ONLINE_MODEL`, `LOCAL_MODEL`, `MODEL`, and the `SYSTEM_PROMPT` establishing the Shorekeeper persona.
- **`core/bot.py`**: Discord.py client setup with message content intent. Delegates message handling to `handlers/message.py`.
- **`handlers/message.py`**: Main message handler. Filters mentions/replies, retrieves RAG context, manages conversation history, calls LLM service, and splits long responses.
- **`services/rag.py`**: RAG system. Loads markdown files from `knowledge/`, chunks by `##` headings, embeds using Ollama's `nomic-embed-text` (always uses Ollama for embeddings, regardless of LLM choice), and performs hybrid semantic+keyword search. Caches embeddings in `data/vectors.json`.
- **`services/llm.py`**: Unified LLM client. Routes to Ollama (local) or Gemini (online) based on `USE_ONLINE_MODEL`. Returns consistent response format.
- **`handlers/conversation_context.py`**: In-memory conversation history per server/channel with 16-message limit.
- **`utils/logger.py`**: Logs response metrics (timings, token counts).

### RAG Search Algorithm

The RAG system uses a **hybrid search** approach:
1. **Semantic similarity** (70% weight): Cosine similarity between query and chunk embeddings using `nomic-embed-text`
2. **Keyword matching** (30% weight): Boosts scores for matches in source paths, headings, labels, and metadata fields
3. **Metadata boosting**: Chunks with `importance: "high"` get 10% score boost, `importance: "low"` get 10% penalty
4. **Character disambiguation**: Strong weighting for character name matches in source paths and metadata

### Knowledge Base Structure

- `knowledge/characters/` – Character profiles, kits, stories (subdirectories by region/character)
- `knowledge/lore/` – Game world lore, regions, history
- `knowledge/personalization/` – Shorekeeper personality, backstory, voice guidelines
- `knowledge/systems/` – Game mechanics
- `knowledge/references/` – Excluded from RAG (reference materials only)

Files are markdown with YAML frontmatter metadata, chunked at `##` headings. The RAG system extracts human-readable labels from file paths and uses metadata for improved search accuracy.

### Bot Initialization Flow

1. `main.py` loads config, builds RAG knowledge base (`rag.build()`), starts Discord bot
2. RAG loads markdown files from `knowledge/`, embeds chunks, saves to `data/vectors.json`
3. LLM client initializes based on `USE_ONLINE_MODEL` (Gemini if online, Ollama if local)
4. Discord bot runs with token from config
5. On message: check mention/reply → RAG search → construct system prompt with personalization → get conversation history → call LLM → log → reply

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

# Online CLI version (Gemini only, no Discord, no RAG)
python online_bot.py
```

### Testing & Validation

```bash
# Run comprehensive RAG tests across characters, mechanics, lore
python test_rag.py

# Test specific character lore retrieval
python test_phrolova_lore.py

# Analyze knowledge base statistics
python check_knowledge.py

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
```

## Configuration Notes

- **Model Switching**: Set `USE_ONLINE_MODEL = True` in `core/config.py` for Gemini, `False` for Ollama.
- **Embedding Requirement**: The RAG system always uses Ollama's `nomic-embed-text` for embeddings, even when using Gemini for LLM responses. Ensure Ollama is running.
- **Local Models**: Ensure Ollama is running with the model specified in `LOCAL_MODEL` (default from `.env.local`).
- **Discord Permissions**: Bot requires `message_content` intent enabled in Discord Developer Portal.
- **Environment**: All secrets are loaded from `.env.local` via `python-dotenv`.

## Development Patterns

- **Adding Knowledge**: Add markdown files to appropriate `knowledge/` subdirectory. Include YAML frontmatter (see `knowledge/references/FORMAT_GUIDE.md`). Use `##` headings for automatic chunking.
- **Extending LLM Support**: Add new backend methods in `services/llm.py` following the existing pattern.
- **Conversation Memory**: History is stored in memory only, reset on bot restart. Modify `conversation_context_limit` in `handlers/conversation_context.py` to adjust.
- **Response Formatting**: Long messages are split at line breaks or spaces under 2000 chars via `split_message()` in `handlers/message.py`.

## Key Files for Modification

- **Bot Personality**: `core/config.py` `SYSTEM_PROMPT` and `knowledge/personalization/`
- **RAG Behavior**: `services/rag.py` search scoring, chunking logic
- **LLM Integration**: `services/llm.py` model configuration and response formatting
- **Message Handling**: `handlers/message.py` filtering, context construction, response processing

## Reference Documentation

- **`ROADMAP.md`**: Planned features and improvements (hot reload, slash commands, reranking)
- **`knowledge/references/FORMAT_GUIDE.md`**: Definitive formatting rules for knowledge files
- **`commands/add_frontmatter.py`**: Script to add YAML metadata to markdown files
- **`commands/update_vectors_with_metadata.py`**: Update vector store with new metadata