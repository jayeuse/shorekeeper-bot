import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services import rag as rag_module


def test_load_knowledge_excludes_agent_guides(tmp_path, monkeypatch) -> None:
    (tmp_path / "AGENTS.md").write_text(
        "# Repository Guidelines\n\n## Rules\nDo not retrieve this content.",
        encoding="utf-8",
    )
    (tmp_path / "lore.md").write_text(
        "# Lore\n\n## Known Record\nThis is valid retrieval content.",
        encoding="utf-8",
    )
    monkeypatch.setattr(rag_module, "KNOWLEDGE_DIR", str(tmp_path))

    chunks = rag_module.load_knowledge()

    assert [chunk["source"] for chunk in chunks] == ["lore.md"]
