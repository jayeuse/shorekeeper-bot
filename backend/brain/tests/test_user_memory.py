import json
import sys
from collections.abc import Iterator
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from handlers.conversation_context import (
    clear_chat,
    get_chat,
    is_compacting,
    mark_compacting,
    snapshot_and_clear,
    store_turn,
    unmark_compacting,
    user_context,
)
from services.user_memory import (
    UserMemoryRepository,
    build_compaction_messages,
    parse_compaction_response,
)

# ─── Repository Tests ────────────────────────────────────────────────────────


@pytest.fixture
def user_memory_repo(tmp_path: Path) -> Iterator[UserMemoryRepository]:
    repo = UserMemoryRepository(db_path=str(tmp_path / "user_memory_test.db"))
    yield repo
    repo.close()


def test_repo_get_by_user_returns_none_when_empty(user_memory_repo: UserMemoryRepository) -> None:
    result = user_memory_repo.get_by_user(user_id="u1", server_id="s1")
    assert result is None


def test_repo_upsert_creates_new_memory(user_memory_repo: UserMemoryRepository) -> None:
    result = user_memory_repo.upsert(
        user_id="u1",
        server_id="s1",
        channel_id="c1",
        memory_content="User likes Wuthering Waves lore.",
        topic="lore",
        importance_score=0.8,
        tags="gaming,lore",
    )

    assert result.id is not None
    assert result.user_id == "u1"
    assert result.server_id == "s1"
    assert result.channel_id == "c1"
    assert result.memory_content == "User likes Wuthering Waves lore."
    assert result.topic == "lore"
    assert result.importance_score == 0.8
    assert result.tags == "gaming,lore"
    assert result.memory_version == 1


def test_repo_upsert_updates_existing_memory(user_memory_repo: UserMemoryRepository) -> None:
    first = user_memory_repo.upsert(
        user_id="u1",
        server_id="s1",
        channel_id="c1",
        memory_content="Original summary.",
        topic="general",
        importance_score=0.5,
        tags="",
    )

    second = user_memory_repo.upsert(
        user_id="u1",
        server_id="s1",
        channel_id="c2",
        memory_content="Updated summary with more detail.",
        topic="character",
        importance_score=0.9,
        tags="shorekeeper",
        existing=first,
    )

    assert second.id == first.id
    assert second.memory_content == "Updated summary with more detail."
    assert second.topic == "character"
    assert second.importance_score == 0.9
    assert second.tags == "shorekeeper"
    assert second.channel_id == "c2"
    assert second.memory_version == 2


def test_repo_get_by_user_returns_after_upsert(user_memory_repo: UserMemoryRepository) -> None:
    user_memory_repo.upsert(
        user_id="u1",
        server_id="s1",
        channel_id="c1",
        memory_content="Some memory.",
        topic="general",
        importance_score=0.5,
        tags="",
    )

    result = user_memory_repo.get_by_user(user_id="u1", server_id="s1")
    assert result is not None
    assert result.memory_content == "Some memory."


def test_repo_user_isolation(user_memory_repo: UserMemoryRepository) -> None:
    user_memory_repo.upsert(
        user_id="u1",
        server_id="s1",
        channel_id="c1",
        memory_content="User 1 memory",
        topic="general",
        importance_score=0.5,
        tags="",
    )
    user_memory_repo.upsert(
        user_id="u2",
        server_id="s1",
        channel_id="c1",
        memory_content="User 2 memory",
        topic="general",
        importance_score=0.5,
        tags="",
    )

    result_u1 = user_memory_repo.get_by_user(user_id="u1", server_id="s1")
    result_u2 = user_memory_repo.get_by_user(user_id="u2", server_id="s1")
    assert result_u1 is not None and result_u1.memory_content == "User 1 memory"
    assert result_u2 is not None and result_u2.memory_content == "User 2 memory"

    # Different server
    result_u1_other = user_memory_repo.get_by_user(user_id="u1", server_id="s2")
    assert result_u1_other is None


def test_repo_search_by_content(user_memory_repo: UserMemoryRepository) -> None:
    user_memory_repo.upsert(
        user_id="u1",
        server_id="s1",
        channel_id="c1",
        memory_content="Identifier: etacidnys\nInterests:\n\tSubject: Wuthering Waves lore\n\tReason: Enjoys worldbuilding\nFacts: loves Wuthering Waves",
        topic="lore",
        importance_score=0.8,
        tags="",
    )
    user_memory_repo.upsert(
        user_id="u2",
        server_id="s1",
        channel_id="c1",
        memory_content="Identifier: unfairuelo\nFacts: prefers citrus fruits",
        topic="preferences",
        importance_score=0.5,
        tags="",
    )

    matches = user_memory_repo.search_by_content("etacidnys", server_id="s1")
    assert len(matches) == 1
    assert matches[0].user_id == "u1"

    # Different server should return nothing
    matches_other = user_memory_repo.search_by_content("etacidnys", server_id="s2")
    assert len(matches_other) == 0


def test_repo_get_stats(user_memory_repo: UserMemoryRepository) -> None:
    stats = user_memory_repo.get_stats(server_id="s1")
    assert stats == {"total_memories": 0, "unique_topics": 0}

    user_memory_repo.upsert(
        user_id="u1",
        server_id="s1",
        channel_id="c1",
        memory_content="A",
        topic="lore",
        importance_score=0.5,
        tags="",
    )
    user_memory_repo.upsert(
        user_id="u2",
        server_id="s1",
        channel_id="c1",
        memory_content="B",
        topic="general",
        importance_score=0.5,
        tags="",
    )

    stats = user_memory_repo.get_stats(server_id="s1")
    assert stats["total_memories"] == 2
    assert stats["unique_topics"] == 2


# ─── Compaction Prompt Tests ──────────────────────────────────────────────────


def test_build_compaction_messages_no_existing_memory() -> None:
    messages = build_compaction_messages(
        existing_memory=None,
        turns=[
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there"},
        ],
    )

    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert "memory consolidation" in messages[0]["content"].lower()
    assert messages[1]["role"] == "user"
    assert "No existing memory" in messages[1]["content"]
    assert "User: Hello" in messages[1]["content"]
    assert "Assistant: Hi there" in messages[1]["content"]


def test_build_compaction_messages_with_existing_memory() -> None:
    existing = type("FakeMemory", (), {"memory_content": "User loves lore."})()

    messages = build_compaction_messages(
        existing_memory=existing,
        turns=[
            {"role": "user", "content": "Tell me more lore"},
        ],
    )

    assert len(messages) == 2
    assert "EXISTING USER MEMORY" in messages[1]["content"]
    assert "User loves lore." in messages[1]["content"]
    assert "User: Tell me more lore" in messages[1]["content"]


# ─── Parse Response Tests ────────────────────────────────────────────────────


def test_parse_valid_compaction_response() -> None:
    text = json.dumps(
        {
            "memory_content": (
                "Identifier: etacidnys\n"
                "Interests:\n"
                "\tSubject: Rinascita history\n"
                "\tReason: Fascinated by the lore\n"
                "Personality: thoughtful, curious, analytical\n"
                "Facts: Has a feline companion named Morgan"
            ),
            "topic": "lore",
            "importance_score": 0.75,
            "tags": ["wuthering_waves", "lore"],
        }
    )

    result = parse_compaction_response(text)
    assert result is not None
    assert "Identifier: etacidnys" in result.memory_content
    assert "Subject: Rinascita history" in result.memory_content
    assert "Facts: Has a feline companion named Morgan" in result.memory_content
    assert result.topic == "lore"
    assert result.importance_score == 0.75
    assert result.tags == ["wuthering_waves", "lore"]


def test_parse_compaction_response_invalid_json() -> None:
    result = parse_compaction_response("This is not JSON")
    assert result is None


def test_parse_compaction_response_missing_content() -> None:
    text = json.dumps({"topic": "lore", "importance_score": 0.5, "tags": []})
    result = parse_compaction_response(text)
    assert result is None


def test_parse_compaction_response_empty_content() -> None:
    text = json.dumps(
        {
            "memory_content": "",
            "topic": "lore",
            "importance_score": 0.5,
            "tags": [],
        }
    )
    result = parse_compaction_response(text)
    assert result is None


def test_parse_compaction_response_with_extra_text() -> None:
    text = f"Here is the memory:\n{json.dumps({'memory_content': 'Identifier: someone\\nFacts: likes cats', 'topic': 'casual', 'importance_score': 0.3, 'tags': ['pets']})}\n---END"
    result = parse_compaction_response(text)
    assert result is not None
    assert "Identifier: someone" in result.memory_content
    assert "Facts: likes cats" in result.memory_content
    assert result.tags == ["pets"]


def test_parse_compaction_response_importance_clamped() -> None:
    text = json.dumps(
        {
            "memory_content": "Test.",
            "topic": "general",
            "importance_score": 5.0,
            "tags": [],
        }
    )
    result = parse_compaction_response(text)
    assert result is not None
    assert result.importance_score == 1.0


def test_parse_compaction_response_non_list_tags() -> None:
    text = json.dumps(
        {
            "memory_content": "Test.",
            "topic": "general",
            "importance_score": 0.5,
            "tags": "not a list",
        }
    )
    result = parse_compaction_response(text)
    assert result is not None
    assert result.tags == []


# ─── Conversation Context Tests ──────────────────────────────────────────────


@pytest.fixture(autouse=True)
def clear_user_context():
    user_context.clear()
    yield


def test_store_turn_creates_context() -> None:
    store_turn("u1", "s1", "Hello", "user")
    chat = get_chat("u1", "s1")
    assert len(chat) == 1
    assert chat[0]["role"] == "user"
    assert chat[0]["content"] == "Hello"


def test_store_turn_multiple_roles() -> None:
    store_turn("u1", "s1", "Hello", "user")
    store_turn("u1", "s1", "Hi there", "assistant")
    chat = get_chat("u1", "s1")
    assert len(chat) == 2
    assert chat[0]["role"] == "user"
    assert chat[1]["role"] == "assistant"


def test_get_chat_returns_empty_for_unknown_user() -> None:
    assert get_chat("unknown", "s1") == []


def test_user_isolation() -> None:
    store_turn("u1", "s1", "Message from u1", "user")
    store_turn("u2", "s1", "Message from u2", "user")
    assert len(get_chat("u1", "s1")) == 1
    assert len(get_chat("u2", "s1")) == 1


def test_server_isolation() -> None:
    store_turn("u1", "s1", "In server s1", "user")
    store_turn("u1", "s2", "In server s2", "user")
    assert len(get_chat("u1", "s1")) == 1
    assert get_chat("u1", "s1")[0]["content"] == "In server s1"
    assert get_chat("u1", "s2")[0]["content"] == "In server s2"


def test_snapshot_and_clears() -> None:
    store_turn("u1", "s1", "Turn 1", "user")
    store_turn("u1", "s1", "Turn 2", "assistant")

    snapshot = snapshot_and_clear("u1", "s1")
    assert len(snapshot) == 2
    assert get_chat("u1", "s1") == []


def test_snapshot_unknown_user() -> None:
    snapshot = snapshot_and_clear("unknown", "s1")
    assert snapshot == []


def test_clear_chat() -> None:
    store_turn("u1", "s1", "Something", "user")
    clear_chat("u1", "s1")
    assert get_chat("u1", "s1") == []


def test_is_compacting_default_false() -> None:
    assert is_compacting("u1", "s1") is False


def test_mark_and_unmark_compacting() -> None:
    mark_compacting("u1", "s1")
    assert is_compacting("u1", "s1") is True
    unmark_compacting("u1", "s1")
    assert is_compacting("u1", "s1") is False


def test_compacting_lock_key_isolation() -> None:
    mark_compacting("u1", "s1")
    assert is_compacting("u2", "s1") is False
    assert is_compacting("u1", "s2") is False
    unmark_compacting("u1", "s1")
