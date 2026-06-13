import json
import os
import re
from collections.abc import Callable
from typing import Any

import numpy as np

try:
    from yaml import safe_load  # type: ignore

    YAML_AVAILABLE = True
except Exception:
    safe_load: Callable[[str], Any] | None = None
    YAML_AVAILABLE = False
    print("⚠️  PyYAML not installed. Install with: pip install pyyaml")

from services.embedder import EmbedderClient

KNOWLEDGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge")
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
STORE_PATH = os.path.join(DATA_DIR, "vectors.json")
EMBEDDINGS_PATH = os.path.join(DATA_DIR, "embeddings")  # np.savez_compressed appends .npz

# Trigger entity rescue when top semantic+keyword score is weak, or when top chunks
# do not mention the named entity requested by the user.
ENTITY_RESCUE_SCORE_THRESHOLD = 0.62
ENTITY_RESCUE_BOOST_WEIGHT = 0.45
ENTITY_RESCUE_TOP_SCAN = 3
NON_KNOWLEDGE_MARKDOWN = {"AGENTS.md", "FORMAT_GUIDE.md"}


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
    remaining = content[end_delim + 5 :]  # After "\n---\n"

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
            if not file.endswith(".md") or file in NON_KNOWLEDGE_MARKDOWN:
                continue

            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, KNOWLEDGE_DIR)

            with open(filepath, encoding="utf-8") as f:
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

        lines = [
            line
            for line in section.split("\n")
            if not line.strip().startswith("<!--") and not line.strip().endswith("-->")
        ]
        cleaned = "\n".join(lines).strip()

        if len(cleaned) < 20:
            continue

        heading_match = re.match(r"^## (.+)", cleaned)
        heading = heading_match.group(1) if heading_match else "General"

        chunks.append(
            {
                "id": f"{source}::{heading}".replace(" ", "_").lower(),
                "text": cleaned,
                "source": source,
                "heading": heading,
                "label": label,
                "metadata": metadata,
            }
        )

    return chunks


def cosine_similarity(a, b):
    if a is None or b is None or len(a) == 0 or len(b) == 0:
        return 0.0
    a = np.array(a)
    b = np.array(b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return np.dot(a, b) / (norm_a * norm_b)


class RAG:
    def __init__(self) -> None:
        self.chunks = []
        self.embeddings = []
        self.personalization_cache = None
        self.manifest_cache = None
        self.embedder = EmbedderClient()

    def build(self):
        self.chunks = load_knowledge()

        if not self.chunks:
            print("⚠️  No knowledge chunks found. Add content to knowledge/ folder.")
            return

        print(f"📚 Embedding {len(self.chunks)} knowledge chunks...")

        embeddings = []
        failed_count = 0
        for i, chunk in enumerate(self.chunks):
            if i % 100 == 0:
                print(f"   Progress: {i}/{len(self.chunks)}...")

            doc_text = f"[{chunk['label']}] {chunk['heading']}. {chunk['text']}"
            vector = self.embedder.embed_document(doc_text)

            if not vector:
                failed_count += 1
                # If it's a massive failure, stop early
                if failed_count > 50:
                    raise Exception(
                        "Too many embedding failures. Check your server connection/batch size."
                    )
                # Use a zero vector as fallback (will have 0 similarity)
                vector = [0.0] * 768  # Default size for nomic-embed-text

            embeddings.append(vector)

        if failed_count > 0:
            print(
                f"⚠️  Warning: {failed_count} chunks failed to embed. They will be ignored in semantic search."
            )

        # Store embeddings as float16 binary (major size reduction)
        embedding_matrix = np.array(embeddings, dtype=np.float16)

        os.makedirs(DATA_DIR, exist_ok=True)
        np.savez_compressed(EMBEDDINGS_PATH, embeddings=embedding_matrix)

        # Store metadata-only chunks as minified JSON (no embeddings)
        chunks_for_storage = [
            {k: v for k, v in chunk.items() if k != "embedding"} for chunk in self.chunks
        ]
        with open(STORE_PATH, "w", encoding="utf-8") as f:
            json.dump(chunks_for_storage, f)

        # Keep embeddings in memory as float32 for accuracy
        self.embeddings = embedding_matrix.astype(np.float32)
        for i, chunk in enumerate(self.chunks):
            chunk["embedding"] = self.embeddings[i]

        print(f"✅ Knowledge base built: {len(self.chunks)} chunks saved")
        print(f"   Metadata: {STORE_PATH}")
        print(f"   Embeddings: {EMBEDDINGS_PATH}.npz (float16, compressed)")

    def load(self):
        if not os.path.exists(STORE_PATH):
            return False

        with open(STORE_PATH, encoding="utf-8") as f:
            self.chunks = json.load(f)

        # Load binary embeddings if present, fall back gracefully
        embeddings_file = EMBEDDINGS_PATH + ".npz"
        if os.path.exists(embeddings_file):
            data = np.load(embeddings_file)
            # Upcast to float32 for computation accuracy
            embedding_matrix = data["embeddings"].astype(np.float32)
            for i, chunk in enumerate(self.chunks):
                if i < len(embedding_matrix):
                    chunk["embedding"] = embedding_matrix[i]
        elif os.path.exists(EMBEDDINGS_PATH):
            # Legacy: .npz without extension appended by np.savez_compressed
            data = np.load(EMBEDDINGS_PATH)
            embedding_matrix = data["embeddings"].astype(np.float32)
            for i, chunk in enumerate(self.chunks):
                if i < len(embedding_matrix):
                    chunk["embedding"] = embedding_matrix[i]

        print(f"📚 Loaded {len(self.chunks)} chunks from existing knowledge base")
        return True

    def search(self, query: str, top_k: int = 8) -> list[dict[str, Any]]:
        if not self.chunks:
            if not self.load():
                return []

        query_embedding = self.embedder.embed_query(query)
        # We continue even if query_embedding is empty by using keyword-only search

        query_words = set(w.strip("?!.,;:'\"") for w in query.lower().split())

        scored: list[tuple[float, float, float, dict[str, Any]]] = []
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

        entity_candidates = self._extract_entity_candidates(query)
        if self._should_run_entity_rescue(scored, entity_candidates, top_k):
            scored = self._apply_entity_rescue(scored, entity_candidates)
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

    def _should_run_entity_rescue(
        self,
        scored: list[tuple[float, float, float, dict[str, Any]]],
        entity_candidates: list[str],
        top_k: int,
    ) -> bool:
        if not scored or not entity_candidates:
            return False

        top_score = scored[0][0]
        if top_score < ENTITY_RESCUE_SCORE_THRESHOLD:
            return True

        scan_limit = max(1, min(top_k, ENTITY_RESCUE_TOP_SCAN, len(scored)))
        top_chunks = [chunk for _, _, _, chunk in scored[:scan_limit]]
        return not any(
            self._chunk_mentions_entity(chunk, entity_candidates) for chunk in top_chunks
        )

    def _apply_entity_rescue(
        self,
        scored: list[tuple[float, float, float, dict[str, Any]]],
        entity_candidates: list[str],
    ) -> list[tuple[float, float, float, dict[str, Any]]]:
        rescued: list[tuple[float, float, float, dict[str, Any]]] = []
        for combined, semantic_score, keyword_score, chunk in scored:
            entity_score = self._entity_match_score(chunk, entity_candidates)
            boosted = combined + (entity_score * ENTITY_RESCUE_BOOST_WEIGHT)
            rescued.append((boosted, semantic_score, keyword_score, chunk))
        return rescued

    def _extract_entity_candidates(self, query: str) -> list[str]:
        candidates: set[str] = set()
        raw_query = query.strip()
        lower_query = raw_query.lower()

        identity_prefixes = (
            "who is ",
            "what is ",
            "who was ",
            "what was ",
            "tell me about ",
            "describe ",
        )
        for prefix in identity_prefixes:
            if lower_query.startswith(prefix):
                tail = raw_query[len(prefix) :].strip(" ?!.,:;\"'")
                if tail:
                    candidates.add(tail)

        quoted_patterns = re.findall(r'"([^"]+)"|\'([^\']+)\'', raw_query)
        for double_quote, single_quote in quoted_patterns:
            value = (double_quote or single_quote).strip()
            if value:
                candidates.add(value)

        phrase_matches = re.findall(r"\b[A-Z][A-Za-z'-]*(?:\s+[A-Z][A-Za-z'-]*)*", raw_query)
        capitalized_stopwords = {
            "Who",
            "What",
            "When",
            "Where",
            "Why",
            "How",
            "Tell",
            "Describe",
            "Explain",
            "The",
            "A",
            "An",
            "Is",
            "Are",
            "Was",
            "Were",
        }
        for phrase in phrase_matches:
            words = [w for w in phrase.split() if w]
            if not words:
                continue
            if all(word in capitalized_stopwords for word in words):
                continue
            if len(" ".join(words)) >= 3:
                candidates.add(" ".join(words))

        normalized = {
            self._normalize_for_match(candidate) for candidate in candidates if candidate.strip()
        }
        return [candidate for candidate in normalized if candidate]

    def _chunk_mentions_entity(self, chunk: dict[str, Any], entity_candidates: list[str]) -> bool:
        heading = self._normalize_for_match(chunk.get("heading", ""))
        source = self._normalize_for_match(chunk.get("source", ""))
        label = self._normalize_for_match(chunk.get("label", ""))

        metadata = chunk.get("metadata", {})
        metadata_values = [
            metadata.get("character", ""),
            metadata.get("group", ""),
            metadata.get("region", ""),
        ]
        tags = metadata.get("tags", [])
        if isinstance(tags, list):
            metadata_values.extend(tag for tag in tags if isinstance(tag, str))
        metadata_blob = self._normalize_for_match(" ".join(str(v) for v in metadata_values if v))

        for candidate in entity_candidates:
            if (
                candidate in heading
                or candidate in source
                or candidate in label
                or candidate in metadata_blob
            ):
                return True
        return False

    def _entity_match_score(self, chunk: dict[str, Any], entity_candidates: list[str]) -> float:
        heading = self._normalize_for_match(chunk.get("heading", ""))
        text = self._normalize_for_match(chunk.get("text", ""))
        source = self._normalize_for_match(chunk.get("source", ""))
        label = self._normalize_for_match(chunk.get("label", ""))

        metadata = chunk.get("metadata", {})
        metadata_values = [
            metadata.get("character", ""),
            metadata.get("group", ""),
            metadata.get("region", ""),
        ]
        tags = metadata.get("tags", [])
        if isinstance(tags, list):
            metadata_values.extend(tag for tag in tags if isinstance(tag, str))
        metadata_blob = self._normalize_for_match(" ".join(str(v) for v in metadata_values if v))

        score = 0.0
        for candidate in entity_candidates:
            if candidate in heading:
                score += 1.2
                continue
            if candidate in text:
                score += 1.0
                continue
            if candidate in source or candidate in label:
                score += 0.9
                continue
            if candidate in metadata_blob:
                score += 0.8
                continue

            tokens = [t for t in candidate.split() if len(t) >= 3]
            token_hits = 0
            for token in tokens:
                if (
                    token in heading
                    or token in text
                    or token in source
                    or token in label
                    or token in metadata_blob
                ):
                    token_hits += 1

            if token_hits >= 2:
                score += 0.6 + (0.1 * min(token_hits - 2, 2))
            elif token_hits == 1:
                score += 0.2

        return min(score, 1.8)

    def _normalize_for_match(self, value: str) -> str:
        normalized = re.sub(r"[^a-z0-9]+", " ", value.lower())
        return re.sub(r"\s+", " ", normalized).strip()

    def get_personalization_context(self):
        """Retrieve all chunks from the personalization directory (Cached)."""
        if self.personalization_cache:
            return self.personalization_cache

        if not self.chunks:
            if not self.load():
                return ""

        # Filter for personalization files
        persona_chunks = [c for c in self.chunks if "personalization" in c["source"]]

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
        lines.append(
            "The following is a precise list of what is stored in your knowledge base. Reference ONLY these entries when asked what you know.\n"
        )

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

    def _keyword_boost(self, query_words: set[str], chunk: dict[str, Any]) -> float:
        heading = chunk["heading"].lower()
        text = chunk["text"].lower()
        source = chunk["source"].lower()
        label = chunk.get("label", "").lower()
        metadata = chunk.get("metadata", {})

        stopwords = {
            "what",
            "who",
            "how",
            "why",
            "when",
            "where",
            "which",
            "are",
            "is",
            "was",
            "were",
            "been",
            "being",
            "the",
            "and",
            "for",
            "that",
            "this",
            "with",
            "from",
            "you",
            "your",
            "her",
            "his",
            "she",
            "they",
            "our",
            "can",
            "could",
            "would",
            "should",
            "will",
            "have",
            "has",
            "about",
            "tell",
            "think",
            "know",
            "like",
            "does",
            "did",
            "not",
            "but",
            "all",
            "some",
            "any",
            "more",
            "work",
            "me",
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
