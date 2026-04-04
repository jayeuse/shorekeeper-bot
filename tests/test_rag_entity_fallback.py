import numpy as np
from typing import Any, cast
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services.rag import RAG


class _StubEmbedder:
    def embed_query(self, text: str) -> list[float]:
        # Keep query embedding deterministic for unit tests.
        return [1.0, 0.0]


def _make_chunk(
    *,
    text: str,
    source: str,
    heading: str,
    label: str,
    embedding: list[float],
    metadata: dict | None = None,
) -> dict:
    return {
        "id": f"{source}::{heading}".lower(),
        "text": text,
        "source": source,
        "heading": heading,
        "label": label,
        "metadata": metadata or {},
        "embedding": np.array(embedding, dtype=np.float32),
    }


def test_entity_rescue_prioritizes_text_mentions() -> None:
    rag = RAG()
    rag.embedder = cast(Any, _StubEmbedder())
    rag.chunks = [
        _make_chunk(
            text="Iuno is a lunar DPS with two state rotations.",
            source="characters/rinascita/iuno/iuno_kit.md",
            heading="Iuno: Key Resources",
            label="Iuno Kit",
            embedding=[0.75, 0.6614],
            metadata={"character": "Iuno", "tags": ["rinascita"]},
        ),
        _make_chunk(
            text=(
                "Sister Isabella took Phoebe around Ragunna after her parents died "
                "and later brought her back to the orphanage."
            ),
            source="characters/rinascita/phoebe/phoebe_story.md",
            heading='Phoebe Character Story II: "Home"',
            label="Phoebe Story",
            embedding=[0.20, 0.9798],
            metadata={"character": "Phoebe", "tags": ["rinascita", "order_of_the_deep"]},
        ),
    ]

    results = rag.search("Who is Sister Isabella?", top_k=1)

    assert len(results) == 1
    assert "phoebe" in results[0]["source"]
    assert "sister isabella" in results[0]["text"].lower()


def test_entity_rescue_does_not_override_grounded_top_hit() -> None:
    rag = RAG()
    rag.embedder = cast(Any, _StubEmbedder())
    rag.chunks = [
        _make_chunk(
            text="Camellya is a Black Shores Resonator with a dual-state combat style.",
            source="characters/black_shores/camellya/camellya_character.md",
            heading="Camellya Profile",
            label="Camellya Character",
            embedding=[0.95, 0.3122],
            metadata={"character": "Camellya", "tags": ["black_shores"]},
        ),
        _make_chunk(
            text="Iuno controls moonlight through Lunar Cycle.",
            source="characters/rinascita/iuno/iuno_kit.md",
            heading="Iuno: Key Resources",
            label="Iuno Kit",
            embedding=[0.70, 0.7141],
            metadata={"character": "Iuno", "tags": ["rinascita"]},
        ),
    ]

    results = rag.search("Who is Camellya?", top_k=1)

    assert len(results) == 1
    assert "camellya" in results[0]["source"]


def test_extract_entity_candidates_handles_lowercase_identity_query() -> None:
    rag = RAG()

    candidates = rag._extract_entity_candidates("who is sister isabella?")

    assert "sister isabella" in candidates
