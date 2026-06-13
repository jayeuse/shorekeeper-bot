from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services.memory import MemoryService


def _build_service(tmp_path: Path) -> MemoryService:
    return MemoryService(db_path=str(tmp_path / "memory_test.db"), recency_half_life_days=30.0)


def test_extract_topics_detects_expected_labels(tmp_path: Path) -> None:
    service = _build_service(tmp_path)

    topics = service.extract_topics("Tell me Camellya lore and skill rotation details")

    assert "character" in topics
    assert "lore" in topics
    assert "abilities" in topics


def test_retrieve_relevant_prefers_user_scope(tmp_path: Path) -> None:
    service = _build_service(tmp_path)

    # Same server, same channel, same user -> user scope.
    service.store_exchange(
        server_id="s1",
        channel_id="c1",
        user_id="u1",
        user_message="Who is Sister Isabella?",
        assistant_message="She cared for Phoebe in Ragunna.",
    )

    # Same server and channel, different user -> channel scope.
    service.store_exchange(
        server_id="s1",
        channel_id="c1",
        user_id="u2",
        user_message="Tell me about Sister Isabella",
        assistant_message="She appears in Phoebe's story.",
    )

    # Same server, different channel and user -> server scope.
    service.store_exchange(
        server_id="s1",
        channel_id="c2",
        user_id="u3",
        user_message="Sister Isabella records",
        assistant_message="Older records mention her and Phoebe.",
    )

    results = service.retrieve_relevant(
        query="Who is Sister Isabella?",
        server_id="s1",
        channel_id="c1",
        user_id="u1",
        limit=3,
        relevance_threshold=0.1,
        candidate_pool=60,
    )

    assert len(results) == 3
    assert results[0].scope == "user"
    assert {record.scope for record in results} == {"user", "channel", "server"}


def test_retrieve_relevant_with_metrics_respects_threshold(tmp_path: Path) -> None:
    service = _build_service(tmp_path)
    service.store_exchange(
        server_id="s1",
        channel_id="c1",
        user_id="u1",
        user_message="hello there",
        assistant_message="Hello. The tides are calm.",
    )

    results, scanned_count = service.retrieve_relevant_with_metrics(
        query="Tell me Camellya ability rotation details",
        server_id="s1",
        channel_id="c1",
        user_id="u1",
        limit=3,
        relevance_threshold=0.85,
        candidate_pool=30,
    )

    assert scanned_count >= 1
    assert results == []
