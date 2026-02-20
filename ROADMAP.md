# Shorekeeper Bot Roadmap

## 🌟 Current Features

### Core Logic
- **Custom RAG System**: A lightweight, dependency-free implementation using JSON and NumPy.
- **Smart Chunking**: Splits markdown files by `##` headers to keep context intact.
- **Hybrid Search**: Combines semantic similarity (via `nomic-embed-text`) with keyword boosting for better accuracy.
- **Persistent Storage**: Saves embeddings to `data/vectors.json` to avoid rebuilding every run.
- **Local Inference**: Fully local using Ollama for both embedding and chat generation.

### Discord Integration
- **Character Persona**: strictly enforced via system prompt and `core/config.py` to roleplay as Shorekeeper.
- **Smart Reply**: Automatically splits long messages exceeding Discord's character limit.
- **Context Awareness**: Maintains a sliding window of the last 16 messages per channel for conversation continuity.
- **Typing Indicators**: Displays "Shorekeeper is typing..." while generating responses.

---

## 🚀 Planned Improvements

### Phase 1: Knowledge Management (Priority: High)
- [ ] **Hot Reload Command**: Add a command (e.g., `!reload`) to rebuild the knowledge base without restarting the bot.
- [ ] **Source Attribution**: Modify responses to cite which knowledge chunk (source file/heading) was used.
- [ ] **Knowledge Validation**: A script to check for malformed markdown or missing headers in `knowledge/`.

### Phase 2: Bot Capabilities (Priority: Medium)
- [ ] **Slash Commands**: Migrate from `on_message` to Discord's Slash Commands (`/ask`, `/help`, `/reload`) for better UX.
- [ ] **Status Rotation**: Change the bot's status periodically (e.g., "Calculating probabilities...", "Watching the Black Shores").
- [ ] **Long-Term Memory**: Implement a summary-based memory for users who talk to the bot frequently.

### Phase 3: RAG Enhancements (Priority: Medium)
- [ ] **Reranking**: Add a reranking step (using a cross-encoder) to strictly filter irrelevant chunks before sending to the LLM.
- [ ] **Meta-Data Filtering**: Allow searching only specific categories (e.g., `category:lore` or `category:mechanics`).

### Phase 4: DevOps / Quality of Life (Priority: Low)
- [ ] **Docker Support**: Create a `Dockerfile` and `compose.yaml` for easy deployment.
- [ ] **Configurable Model**: Allow changing the model via environment variables or commands.
