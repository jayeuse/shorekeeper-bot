import os
import re
import json
from typing import Any, Callable, Optional

import numpy as np
import ollama

try:
    from yaml import safe_load  # type: ignore
    YAML_AVAILABLE = True
except Exception:
    safe_load: Optional[Callable[[str], Any]] = None
    YAML_AVAILABLE = False
    print("⚠️  PyYAML not installed. Install with: pip install pyyaml")

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


def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content.

    Returns:
        tuple: (metadata_dict, remaining_content)
    """
    if not YAML_AVAILABLE:
        return {}, content

    # Check for frontmatter delimiter at start
    if not content.startswith("---\n"):
        return {}, content

    # Find the second delimiter
    end_delim = content.find("\n---\n", 4)  # Skip first "---\n"
    if end_delim == -1:
        return {}, content

    frontmatter_text = content[4:end_delim]  # Between first and second delimiters
    remaining = content[end_delim + 5:]  # After "\n---\n"

    # Ensure the imported safe_load is available for type checkers
    assert safe_load is not None
    try:
        metadata = safe_load(frontmatter_text) or {}
    except Exception:
        metadata = {}

    return metadata, remaining


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

            metadata, remaining_content = parse_frontmatter(content)
            file_chunks = chunk_by_heading(remaining_content, source=rel_path, metadata=metadata)
            chunks.extend(file_chunks)

    return chunks


def chunk_by_heading(text, source="", metadata=None):
    sections = re.split(r"(?=^## )", text, flags=re.MULTILINE)
    chunks = []
    label = _extract_label(source)
    if metadata is None:
        metadata = {}

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
            "metadata": metadata,
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
        self.manifest_cache = None

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

            # Importance boost from metadata
            importance = chunk.get("metadata", {}).get("importance", "medium")
            if importance == "high":
                combined *= 1.1
            elif importance == "low":
                combined *= 0.9

            scored.append((combined, semantic_score, keyword_score, chunk))

        scored.sort(key=lambda x: x[0], reverse=True)

        return [
            {
                "text": chunk["text"],
                "source": chunk["source"],
                "heading": chunk["heading"],
                "score": float(combined),
                "metadata": chunk.get("metadata", {}),
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

    def get_manifest(self):
        """Build a structured knowledge manifest from loaded chunks.

        Returns a human-readable string listing all characters and lore topics
        present in the knowledge base, grouped by category.
        """
        if self.manifest_cache:
            return self.manifest_cache

        if not self.chunks:
            if not self.load():
                return ""

        # Collect unique sources (one entry per file, not per chunk)
        seen_sources = set()
        characters: dict[str, list[str]] = {}  # group -> [character names]
        lore_topics: list[str] = []
        other_topics: list[str] = []

        for chunk in self.chunks:
            source = chunk["source"]
            if source in seen_sources:
                continue
            seen_sources.add(source)

            parts = source.replace("\\", "/").split("/")
            metadata = chunk.get("metadata", {})

            if parts[0] == "characters" and len(parts) >= 3:
                group = parts[1].replace("_", " ").title()
                char = metadata.get("character") or parts[2].replace("_", " ").title()
                if group not in characters:
                    characters[group] = []
                if char not in characters[group]:
                    characters[group].append(char)

            elif parts[0] == "lore":
                doc_type = metadata.get("document_type", "")
                region = metadata.get("region", "")
                label = chunk.get("label", source.replace("_", " ").title())
                entry = region if region else label
                if entry and entry not in lore_topics:
                    lore_topics.append(entry)

            elif parts[0] not in ("personalization",):
                label = chunk.get("label", source)
                if label not in other_topics:
                    other_topics.append(label)

        lines = ["=== KNOWLEDGE MANIFEST ==="]
        lines.append("The following is a precise list of what is stored in your knowledge base. Reference ONLY these entries when asked what you know.\n")

        if characters:
            lines.append("Characters:")
            for group in sorted(characters):
                names = ", ".join(sorted(set(characters[group])))
                lines.append(f"  {group}: {names}")

        if lore_topics:
            lines.append("\nLore topics:")
            lines.append(f"  {', '.join(sorted(set(lore_topics)))}")

        if other_topics:
            lines.append("\nOther topics:")
            lines.append(f"  {', '.join(sorted(set(other_topics)))}")

        self.manifest_cache = "\n".join(lines)
        return self.manifest_cache

    def _keyword_boost(self, query_words, chunk):
        heading = chunk["heading"].lower()
        text = chunk["text"].lower()
        source = chunk["source"].lower()
        label = chunk.get("label", "").lower()
        metadata = chunk.get("metadata", {})

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

            # Metadata field matches
            if metadata:
                # Character name match
                char_name = metadata.get("character", "").lower()
                if char_name and stem in char_name:
                    score += 0.3

                # Region match
                region = metadata.get("region", "").lower()
                if region and stem in region:
                    score += 0.3

                # Group match
                group = metadata.get("group", "").lower()
                if group and stem in group:
                    score += 0.3

                # Tags match
                tags = metadata.get("tags", [])
                for tag in tags:
                    if isinstance(tag, str) and stem in tag.lower():
                        score += 0.2
                        break

        return min(score, 1.0)
