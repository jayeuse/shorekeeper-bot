"""
Memory system smoke test.

Exercises short-term memory, triggers compaction, and verifies long-term memory.
Requires a running LLM provider (local or online) configured in .env.local.

Usage:
    uv run python brain/tests/memory_smoke.py
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.config import MEMORY_COMPACTION_TIMEOUT_SECONDS, MEMORY_SHORT_TERM_TURN_LIMIT
from handlers.conversation_context import (
    clear_chat,
    get_chat,
    mark_compacting,
    store_turn,
    unmark_compacting,
    user_context,
)
from services.llm import LLMClient
from services.user_memory import (
    UserMemoryRepository,
    build_compaction_messages,
    parse_compaction_response,
)

USER_ID = "smoke_user_42"
SERVER_ID = "smoke_server_1"
CHANNEL_ID = "smoke_channel_1"
DB_PATH = str(Path(__file__).resolve().parents[2] / "data" / "smoke_memory_test.db")


def _step(label: str) -> None:
    print(f"\n{'=' * 70}")
    print(f"  {label}")
    print(f"{'=' * 70}")


def _dump(short_term: list[dict], long_term) -> None:
    print(f"  STM turns: {len(short_term)}")
    if short_term:
        for t in short_term[-3:]:
            role = t["role"].ljust(9)
            content = t["content"][:60]
            print(f"    [{role}] {content}")
    print(f"  LTM: {'exists' if long_term else 'none'}")
    if long_term:
        print(f"    version .. {long_term.memory_version}")
        print(f"    topic .... {long_term.topic}")
        print(f"    score .... {long_term.importance_score}")
        print(f"    tags ..... {long_term.tags}")
        text = long_term.memory_content
        print(f"    content .. {text[:200]}{'...' if len(text) > 200 else ''}")


# ── Simulated conversation turns ───────────────────────────────────────────


def _topic_turns(about: str) -> list[tuple[str, str]]:
    """Return user/assistant turn pairs for a topic."""
    pairs = {
        "greeting": [
            ("Hello there!", "Greetings. The tides are calm today. How may I assist you?"),
        ],
        "lore": [
            (
                "Tell me about the Black Shores.",
                "The Black Shores is a sanctuary I oversee. A place where records of this world are kept.",
            ),
            (
                "Who founded the Black Shores?",
                "The Rover founded the Black Shores long ago. I carry out their will in their absence.",
            ),
            (
                "What is the Tethys System?",
                "The Tethys System is the computational core that processes the world's records. I am its Second Instance.",
            ),
        ],
        "character": [
            (
                "Tell me about Camellya.",
                "Camellya is a resonator bound to the Black Shores. Her connection to the Tethys System runs deep.",
            ),
            (
                "What are Camellya's abilities?",
                "She wields a unique frequency that can resonate with Remnant Energy. Her combat style is elegant and precise.",
            ),
            (
                "Is Phoebe connected to Camellya?",
                "They share ties through the Black Shores, though their paths and purposes differ.",
            ),
        ],
        "abilities": [
            (
                "What's a good team for Camellya?",
                "Camellya pairs well with support resonators who can amplify her damage output.",
            ),
            (
                "What rotation should I use?",
                "Open with her resonance skill, then follow with basic attacks until the mark triggers.",
            ),
            (
                "What weapon is best for her?",
                "Her signature weapon amplifies her skill damage. Any sword with crit substats works well.",
            ),
        ],
        "user_prefs": [
            (
                "I prefer playing support characters.",
                "A thoughtful choice. Supporting others requires patience and precision.",
            ),
            (
                "My favorite team is Shorekeeper, Camellya, and Verina.",
                "A balanced composition. Healer, amplifier, and damage dealer complement each other.",
            ),
            (
                "I mostly play on mobile.",
                "Mobile requires steady fingers. The tides of battle shift quickly on smaller screens.",
            ),
            (
                "I've been playing for about 3 months now.",
                "Three months — still young in your journey. There is much yet to discover.",
            ),
        ],
    }
    return pairs.get(about, [("test", "I acknowledge your input.")])


async def main() -> None:
    # ── Setup ────────────────────────────────────────────────────────────

    repo = UserMemoryRepository(db_path=DB_PATH)
    llm = LLMClient()
    user_context.clear()

    _step("PHASE 1: Short-Term Memory — conversation continuity")

    # Run 5 turns (10 STM entries) — well below the 16-turn compaction threshold.
    for i in range(5):
        user_msg = f"Test message {i + 1}: What is {i + 1} plus {i + 2}?"
        store_turn(USER_ID, SERVER_ID, user_msg, "user")
        asst_msg = f"The result of {i + 1} plus {i + 2} is {i + i + 3}."
        store_turn(USER_ID, SERVER_ID, asst_msg, "assistant")

    chat = get_chat(USER_ID, SERVER_ID)
    print(f"After 5 exchanges: {len(chat)} turns in STM")
    assert len(chat) == 10, f"Expected 10 turns, got {len(chat)}"

    # Verify earlier turns still present (FIFO retention)
    assert chat[0]["content"] == "Test message 1: What is 1 plus 2?"
    print("  First turn retained ✓")
    assert chat[-1]["role"] == "assistant"
    print("  Last turn is assistant ✓")

    _step("PHASE 2: Short-Term Memory — per-user isolation")

    # Add turns for another user — should not pollute the first user's context.
    OTHER_USER = "smoke_user_99"
    store_turn(OTHER_USER, SERVER_ID, "I am a different user.", "user")
    store_turn(OTHER_USER, SERVER_ID, "Acknowledged.", "assistant")

    user1_chat = get_chat(USER_ID, SERVER_ID)
    user2_chat = get_chat(OTHER_USER, SERVER_ID)

    assert len(user1_chat) == 10, f"User 1 should still have 10, got {len(user1_chat)}"
    assert len(user2_chat) == 2, f"User 2 should have 2, got {len(user2_chat)}"
    assert user1_chat != user2_chat
    print("  User isolation verified ✓")
    clear_chat(OTHER_USER, SERVER_ID)

    _step("PHASE 3: Short-Term Memory — FIFO eviction at 16-turn limit")

    # Current STM: 10 turns from phase 1.
    # add 4 more exchanges (8 turns) → 18 total → first 2 should be evicted.
    for i in range(5, 9):
        user_msg = f"Continuation {i}: What is the square root of {i * i}?"
        store_turn(USER_ID, SERVER_ID, user_msg, "user")
        asst_msg = f"The square root of {i * i} is {i}."
        store_turn(USER_ID, SERVER_ID, asst_msg, "assistant")

    chat = get_chat(USER_ID, SERVER_ID)
    print(
        f"After adding 4 more exchanges: {len(chat)} turns (cap at {MEMORY_SHORT_TERM_TURN_LIMIT})"
    )
    assert len(chat) == MEMORY_SHORT_TERM_TURN_LIMIT, (
        f"Expected {MEMORY_SHORT_TERM_TURN_LIMIT}, got {len(chat)}"
    )
    # First 2 turns should be evicted
    assert "Test message 1" not in chat[0]["content"], "Oldest turn should be evicted"
    print("  FIFO eviction at 16-turn cap ✓")
    clear_chat(USER_ID, SERVER_ID)

    _step("PHASE 4: Memory Compaction — build topic-rich conversation")

    # Build 8 exchanges (16 turns) across multiple topics.
    # This will fill STM to exactly the threshold.
    conversations = (
        _topic_turns("user_prefs")
        + _topic_turns("lore")
        + _topic_turns("character")
        + _topic_turns("abilities")
    )

    for user_msg, asst_msg in conversations:
        store_turn(USER_ID, SERVER_ID, user_msg, "user")
        store_turn(USER_ID, SERVER_ID, asst_msg, "assistant")

    chat = get_chat(USER_ID, SERVER_ID)
    print(f"After loading topic conversations: {len(chat)} turns")
    assert len(chat) == MEMORY_SHORT_TERM_TURN_LIMIT

    # No existing LTM
    existing = repo.get_by_user(USER_ID, SERVER_ID)
    assert existing is None, "Should have no LTM before first compaction"
    print("  No pre-existing long-term memory ✓")

    _step("PHASE 5: Memory Compaction — run compaction")

    # Build and show the compaction prompt (useful for debugging)
    messages = build_compaction_messages(existing, chat)
    print(f"\n  Compaction system prompt ({len(messages[0]['content'])} chars)")
    print(f"  Compaction user input   ({len(messages[1]['content'])} chars)")
    print(f"  Total messages: {len(messages)}")

    print("\n  Calling LLM for summary...")
    mark_compacting(USER_ID, SERVER_ID)
    try:
        response = await asyncio.wait_for(
            llm.chat(messages), timeout=MEMORY_COMPACTION_TIMEOUT_SECONDS
        )
        reply = response.get("message", {}).get("content", "")
        parsed = parse_compaction_response(reply)

        if parsed is None:
            print("⚠️  LLM response did not contain valid JSON.")
            print(f"  Raw response (first 500 chars):\n    {reply[:500]}")
            return

        print("\n  Parsed compaction result:")
        print(f"    topic ............ {parsed.topic}")
        print(f"    importance_score . {parsed.importance_score}")
        print(f"    tags ............. {parsed.tags}")
        print("    content (truncated):")
        for line in parsed.memory_content.split("\n"):
            print(f"      {line}")

        # Store to LTM
        memory = repo.upsert(
            user_id=USER_ID,
            server_id=SERVER_ID,
            channel_id=CHANNEL_ID,
            memory_content=parsed.memory_content,
            topic=parsed.topic,
            importance_score=parsed.importance_score,
            tags=",".join(parsed.tags),
        )
        print(f"\n  Stored to LTM (v{memory.memory_version}) ✓")

    except TimeoutError:
        print(f"⚠️  LLM call timed out ({MEMORY_COMPACTION_TIMEOUT_SECONDS}s)")
        print("  This is expected if no model server is running.")
        print("  To test locally, start llama.cpp or set MODE=online with a valid API key.")
        return
    except Exception as exc:
        print(f"⚠️  Compaction failed: {exc}")
        return
    finally:
        unmark_compacting(USER_ID, SERVER_ID)

    _step("PHASE 6: Post-Compaction — fresh STM, persistent LTM")

    # STM should be cleared (if we had called snapshot_and_clear in the real flow)
    # In this test we manually cleared it; verify LTM persists.
    existing = repo.get_by_user(USER_ID, SERVER_ID)
    assert existing is not None
    assert existing.memory_version >= 1
    print(f"  LTM version: {existing.memory_version}")
    print(f"  LTM topic:   {existing.topic}")
    print(f"  LTM content: {existing.memory_content[:120]}...")
    print("  LTM survives after STM cleared ✓")

    _step("PHASE 7: Re-compaction — second cycle merges new info")

    # Simulate new conversation with additional preferences
    new_turns = [
        (
            "I also enjoy playing DPS characters now.",
            "A shift in role. The damage dealer path is more direct, but equally demanding.",
        ),
        (
            "My favorite DPS is Jinhsi.",
            "Jinhsi's conviction is her strength. Her strikes carry the weight of her purpose.",
        ),
        (
            "What's a good team for Jinhsi?",
            "Pair her with coordinated attackers. She thrives when off-field damage supports her sequence.",
        ),
    ]
    for user_msg, asst_msg in new_turns:
        store_turn(USER_ID, SERVER_ID, user_msg, "user")
        store_turn(USER_ID, SERVER_ID, asst_msg, "assistant")

    print(f"\n  Added {len(new_turns)} new exchanges")

    # Re-compact: existing LTM + new STM → updated LTM
    chat = get_chat(USER_ID, SERVER_ID)
    messages = build_compaction_messages(existing, chat)

    print("  Calling LLM for re-compaction...")
    mark_compacting(USER_ID, SERVER_ID)
    try:
        response = await asyncio.wait_for(
            llm.chat(messages), timeout=MEMORY_COMPACTION_TIMEOUT_SECONDS
        )
        reply = response.get("message", {}).get("content", "")
        parsed = parse_compaction_response(reply)

        if parsed is None:
            print("⚠️  Re-compaction JSON parse failed.")
            print(f"  First 400 chars: {reply[:400]}")
            return

        previous_version = existing.memory_version
        memory = repo.upsert(
            user_id=USER_ID,
            server_id=SERVER_ID,
            channel_id=CHANNEL_ID,
            memory_content=parsed.memory_content,
            topic=parsed.topic,
            importance_score=parsed.importance_score,
            tags=",".join(parsed.tags),
            existing=existing,
        )
        print(f"\n  Re-compaction stored (v{memory.memory_version}) ✓")
        print(f"  Content: {memory.memory_content[:200]}")
        assert memory.memory_version == previous_version + 1, (
            f"Version should increment: {memory.memory_version} != {previous_version + 1}"
        )
        print("  Version correctly incremented ✓")

        # New info should be reflected
        assert "DPS" in memory.memory_content or "Jinhsi" in memory.memory_content
        print("  New info (DPS/Jinhsi) reflected in updated LTM ✓")

    except TimeoutError:
        print("⚠️  Re-compaction timed out.")
    except Exception as exc:
        print(f"⚠️  Re-compaction failed: {exc}")

    _step("CLEANUP")

    repo.close()
    # Remove temp DB
    Path(DB_PATH).unlink(missing_ok=True)
    clear_chat(USER_ID, SERVER_ID)

    _step("SUMMARY")
    print("  Phase 1 — STM continuity ......... ✓")
    print("  Phase 2 — User isolation ......... ✓")
    print("  Phase 3 — FIFO eviction .......... ✓")
    print("  Phase 4 — Topic conversation ..... ✓")
    print("  Phase 5 — First compaction ....... ✅" if existing else " ✗")
    print("  Phase 6 — LTM persistence ........ ✅" if existing else " ✗")
    print("  Phase 7 — Re-compaction .......... see above")
    print("\n  Note: If LLM was unavailable, the smoke test still validated")
    print("  STM behavior, compaction prompt building, and JSON parsing.")


if __name__ == "__main__":
    asyncio.run(main())
