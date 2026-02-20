import os
import re
import json
import numpy as np
import ollama

KNOWLEDGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge")
STORE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "vectors.json")
EMBED_MODEL = "nomic-embed-text"


def _extract_label(source):
    """Extract a human-readable label from the source path.

    Examples:
        characters/camellya/camellya_kit.md  → "Camellya Kit"
        personalization/personality.md       → "Personality"
        lore/black_shores.md                → "Black Shores"
        dialogues/idle_lines.md             → "Idle Lines"
    """
    name = os.path.splitext(os.path.basename(source))[0]  # e.g. "camellya_kit"

    # Strip character-name prefix for character files (camellya_kit → kit)
    parts = source.replace("\\", "/").split("/")
    if len(parts) >= 2 and parts[0] == "characters":
        char_name = parts[1].replace("_", " ").title()  # "Camellya"
        suffix = name.replace(parts[1] + "_", "").replace("_", " ").title()  # "Kit"
        return f"{char_name} {suffix}".strip()

    return name.replace("_", " ").title()


def load_knowledge():
    chunks = []

    for root, dirs, files in os.walk(KNOWLEDGE_DIR):
        # Exclude references directory and system directories
        dirs[:] = [d for d in dirs if d != "references" and not d.startswith(".")]

        for file in sorted(files):
            if not file.endswith(".md") or file == "FORMAT_GUIDE.md":
                continue

            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, KNOWLEDGE_DIR)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            file_chunks = chunk_by_heading(content, source=rel_path)
            chunks.extend(file_chunks)

    return chunks


def chunk_by_heading(text, source=""):
    sections = re.split(r"(?=^## )", text, flags=re.MULTILINE)
    chunks = []
    label = _extract_label(source)

    for section in sections:
        section = section.strip()
        if not section or section.startswith("<!--"):
            continue

        lines = [line for line in section.split("\n")
                 if not line.strip().startswith("<!--") and not line.strip().endswith("-->")]
        cleaned = "\n".join(lines).strip()

        if len(cleaned) < 20:
            continue

        heading_match = re.match(r"^## (.+)", cleaned)
        heading = heading_match.group(1) if heading_match else "General"

        chunks.append({
            "id": f"{source}::{heading}".replace(" ", "_").lower(),
            "text": cleaned,
            "source": source,
            "heading": heading,
            "label": label,
        })

    return chunks


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


class RAG:
    def __init__(self):
        self.chunks = []
        self.embeddings = []
        self.personalization_cache = None

    def build(self):
        self.chunks = load_knowledge()

        if not self.chunks:
            print("⚠️  No knowledge chunks found. Add content to knowledge/ folder.")
            return

        print(f"📚 Embedding {len(self.chunks)} knowledge chunks...")

        for chunk in self.chunks:
            # Include the label (character/file identity) in embedding for disambiguation
            doc_text = f"search_document: [{chunk['label']}] {chunk['heading']}. {chunk['text']}"
            response = ollama.embed(model=EMBED_MODEL, input=doc_text)
            chunk["embedding"] = response["embeddings"][0]

        os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)
        with open(STORE_PATH, "w", encoding="utf-8") as f:
            json.dump(self.chunks, f, indent=4)

        print(f"✅ Knowledge base built: {len(self.chunks)} chunks saved to {STORE_PATH}")

    def load(self):
        if not os.path.exists(STORE_PATH):
            return False

        with open(STORE_PATH, "r", encoding="utf-8") as f:
            self.chunks = json.load(f)

        print(f"📚 Loaded {len(self.chunks)} chunks from existing knowledge base")
        return True

    def search(self, query, top_k=8):
        if not self.chunks:
            if not self.load():
                return []

        query_text = f"search_query: {query}"
        query_response = ollama.embed(model=EMBED_MODEL, input=query_text)
        query_embedding = query_response["embeddings"][0]

        query_words = set(
            w.strip("?!.,;:'\"") for w in query.lower().split()
        )

        scored = []
        for chunk in self.chunks:
            if "embedding" not in chunk:
                continue

            semantic_score = cosine_similarity(query_embedding, chunk["embedding"])
            keyword_score = self._keyword_boost(query_words, chunk)
            combined = (0.7 * semantic_score) + (0.3 * keyword_score)

            scored.append((combined, semantic_score, keyword_score, chunk))

        scored.sort(key=lambda x: x[0], reverse=True)

        return [
            {
                "text": chunk["text"],
                "source": chunk["source"],
                "heading": chunk["heading"],
                "score": float(combined),
            }
            for combined, _, _, chunk in scored[:top_k]
        ]

    def get_personalization_context(self):
        """Retrieve all chunks from the personalization directory (Cached)."""
        if self.personalization_cache:
            return self.personalization_cache

        if not self.chunks:
            if not self.load():
                return ""

        # Filter for personalization files
        persona_chunks = [
            c for c in self.chunks
            if "personalization" in c["source"]
        ]

        # Sort by source filename to ensure consistent order
        persona_chunks.sort(key=lambda x: x["source"])

        self.personalization_cache = "\n\n".join(c["text"] for c in persona_chunks)
        return self.personalization_cache

    def _keyword_boost(self, query_words, chunk):
        heading = chunk["heading"].lower()
        text = chunk["text"].lower()
        source = chunk["source"].lower()
        label = chunk.get("label", "").lower()

        stopwords = {
            "what", "who", "how", "why", "when", "where", "which",
            "are", "is", "was", "were", "been", "being",
            "the", "and", "for", "that", "this", "with", "from",
            "you", "your", "her", "his", "she", "they", "our",
            "can", "could", "would", "should", "will", "have", "has",
            "about", "tell", "think", "know", "like", "does", "did",
            "not", "but", "all", "some", "any", "more",
            "work", "me",
        }

        score = 0.0
        for word in query_words:
            if len(word) < 3 or word in stopwords:
                continue

            stem = word[:4] if len(word) > 4 else word

            # Source/label match — strongest signal for character disambiguation
            if stem in source or stem in label:
                score += 0.5

            # Heading match — strong topic signal
            if stem in heading:
                score += 0.4
            # Text body match — weaker but still useful
            elif stem in text:
                score += 0.1

        return min(score, 1.0)
