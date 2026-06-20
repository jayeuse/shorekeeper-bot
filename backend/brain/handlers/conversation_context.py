from __future__ import annotations

from core.config import MEMORY_SHORT_TERM_TURN_LIMIT

user_context: dict[str, list[dict[str, str]]] = {}
_compaction_locks: set[str] = set()


def _user_key(user_id: str, server_id: str) -> str:
    return f"{user_id}_{server_id}"


def store_turn(user_id: str, server_id: str, message: str, role: str, author: str = "") -> bool:
    key = _user_key(user_id, server_id)
    if key not in user_context:
        user_context[key] = []

    chat = user_context[key]
    chat.append({"role": role, "content": message, "author": author})

    threshold_hit = len(chat) >= MEMORY_SHORT_TERM_TURN_LIMIT
    if len(chat) > MEMORY_SHORT_TERM_TURN_LIMIT:
        chat.pop(0)
    return threshold_hit


def get_chat(user_id: str, server_id: str) -> list[dict[str, str]]:
    return user_context.get(_user_key(user_id, server_id), [])


def format_chat_for_llm(chat: list[dict[str, str]]) -> list[dict[str, str]]:
    formatted: list[dict[str, str]] = []
    for msg in chat:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        author = msg.get("author", "")
        if role == "user" and author:
            content = f"[{author}] {content}"
        formatted.append({"role": role, "content": content})
    return formatted


def snapshot_and_clear(user_id: str, server_id: str) -> list[dict[str, str]]:
    key = _user_key(user_id, server_id)
    chat = user_context.pop(key, [])
    return chat


def is_compacting(user_id: str, server_id: str) -> bool:
    return _user_key(user_id, server_id) in _compaction_locks


def mark_compacting(user_id: str, server_id: str) -> None:
    _compaction_locks.add(_user_key(user_id, server_id))


def unmark_compacting(user_id: str, server_id: str) -> None:
    _compaction_locks.discard(_user_key(user_id, server_id))


def clear_chat(user_id: str, server_id: str) -> None:
    key = _user_key(user_id, server_id)
    user_context.pop(key, None)
