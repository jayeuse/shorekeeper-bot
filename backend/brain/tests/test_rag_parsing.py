import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services import rag as rag_module
from services.rag import RAG, chunk_by_heading, cosine_similarity, parse_frontmatter


def test_parse_frontmatter_returns_metadata_and_body() -> None:
    metadata, body = parse_frontmatter(
        "---\ncharacter: Shorekeeper\ntags:\n  - black_shores\n---\n# Record"
    )

    assert metadata == {"character": "Shorekeeper", "tags": ["black_shores"]}
    assert body == "# Record"


@pytest.mark.parametrize(
    "content",
    ["# No frontmatter", "---\ninvalid: [\n---\n# Body", "---\nmissing delimiter"],
)
def test_parse_frontmatter_falls_back_safely(content: str) -> None:
    metadata, body = parse_frontmatter(content)

    assert metadata == {}
    assert body in {content, "# Body"}


def test_chunk_by_heading_removes_comments_and_keeps_metadata() -> None:
    chunks = chunk_by_heading(
        "# Character Record\n\n## Overview\n<!-- hidden -->\nVisible grounded details.",
        source="characters/shorekeeper/shorekeeper_character.md",
        metadata={"importance": "high"},
    )

    assert [chunk["heading"] for chunk in chunks] == ["Overview"]
    assert "hidden" not in chunks[0]["text"]
    assert chunks[0]["metadata"] == {"importance": "high"}
    assert chunks[0]["label"] == "Shorekeeper Character"


def test_cosine_similarity_handles_matches_and_empty_vectors() -> None:
    assert cosine_similarity([1.0, 0.0], [1.0, 0.0]) == pytest.approx(1.0)
    assert cosine_similarity([0.0, 0.0], [1.0, 0.0]) == 0.0
    assert cosine_similarity([], [1.0]) == 0.0


def test_rag_load_reads_metadata_and_binary_embeddings(tmp_path, monkeypatch) -> None:
    store_path = tmp_path / "vectors.json"
    embeddings_path = tmp_path / "embeddings"
    store_path.write_text(
        '[{"text":"Known detail","source":"lore.md","heading":"Overview"}]',
        encoding="utf-8",
    )
    np.savez_compressed(embeddings_path, embeddings=np.array([[0.5, 0.25]], dtype=np.float16))
    monkeypatch.setattr(rag_module, "STORE_PATH", str(store_path))
    monkeypatch.setattr(rag_module, "EMBEDDINGS_PATH", str(embeddings_path))

    rag = RAG()

    assert rag.load() is True
    assert rag.chunks[0]["embedding"].dtype == np.float32
    assert rag.chunks[0]["embedding"].tolist() == [0.5, 0.25]


def test_personalization_and_manifest_are_cached() -> None:
    rag = RAG()
    rag.chunks = [
        {
            "source": "personalization/personality.md",
            "text": "Calm and concise.",
            "metadata": {},
            "label": "Personality",
        },
        {
            "source": "characters/black_shores/shorekeeper/shorekeeper_character.md",
            "text": "Character details.",
            "metadata": {"character": "Shorekeeper"},
            "label": "Shorekeeper Character",
        },
        {
            "source": "lore/regions/black_shores/black_shores_story.md",
            "text": "Region details.",
            "metadata": {"region": "Black Shores"},
            "label": "Black Shores Story",
        },
    ]

    assert rag.get_personalization_context() == "Calm and concise."
    manifest = rag.get_manifest()
    assert "Black Shores: Shorekeeper" in manifest
    assert "Lore topics:\n  Black Shores" in manifest
    assert rag.get_manifest() is manifest
