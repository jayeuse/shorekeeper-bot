import asyncio
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from handlers import conversation_context
from handlers import message as message_module
from services.search import SearchBundle, SearchError, SearchResult


class _StubRag:
    def __init__(self) -> None:
        self.calls: list[tuple[str, int]] = []

    def search(self, query: str, top_k: int = 0) -> list[dict]:
        self.calls.append((query, top_k))
        return []

    def get_personalization_context(self) -> str:
        return "Calm and observant."

    def get_manifest(self) -> str:
        return "Known records manifest."


class _StubLLM:
    def __init__(self) -> None:
        self.model = "stub-model"
        self.last_messages: list[dict] | None = None

    async def chat(self, messages: list[dict]) -> dict:
        self.last_messages = messages
        return {
            "model": self.model,
            "message": {"content": "The tides remain steady."},
            "prompt_eval_count": 1,
            "eval_count": 1,
            "prompt_eval_duration": 1,
            "eval_duration": 1,
        }


class _TypingContext:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb) -> bool:
        return False


class _Channel:
    def __init__(self) -> None:
        self.id = 456
        self.sent: list[str] = []

    def typing(self) -> _TypingContext:
        return _TypingContext()

    async def send(self, content: str) -> None:
        self.sent.append(content)

    def __str__(self) -> str:
        return "general"


class _Message:
    def __init__(self, *, content: str, bot_user) -> None:
        self.content = content
        self.author = SimpleNamespace(id=123, __str__=lambda self: "Rover")
        self.guild = SimpleNamespace(id=789)
        self.channel = _Channel()
        self.mentions = [bot_user]
        self.reference = None
        self.replies: list[str] = []

    async def reply(self, content: str) -> None:
        self.replies.append(content)


class _SuccessSearchProvider:
    def __init__(self) -> None:
        self.calls: list[tuple[str, int]] = []

    async def search(self, query: str, limit: int) -> SearchBundle:
        self.calls.append((query, limit))
        return SearchBundle(
            query=query,
            provider="searxng",
            used_fallback_query=False,
            results=[
                SearchResult(
                    title="Latest Patch Notes",
                    url="https://example.com/patch",
                    snippet="Version 2.4 patch notes and live changes.",
                    source="example.com",
                    published_at="2026-06-13",
                    score=1.0,
                )
            ],
        )


class _EmptySearchProvider:
    async def search(self, query: str, limit: int) -> SearchBundle:
        return SearchBundle(
            query=query,
            provider="searxng",
            used_fallback_query=False,
            results=[],
        )


class _FailingSearchProvider:
    async def search(self, query: str, limit: int) -> SearchBundle:
        raise SearchError("backend unavailable")


def _configure_runtime(monkeypatch, *, search_provider):
    conversation_context.conversation_context.clear()
    stub_rag = _StubRag()
    stub_llm = _StubLLM()
    log_calls: list[dict] = []

    def _fake_log_response(*args, **kwargs) -> None:
        log_calls.append(kwargs)

    monkeypatch.setattr(message_module, "rag", stub_rag)
    monkeypatch.setattr(message_module, "llm_client", stub_llm)
    monkeypatch.setattr(message_module, "memory_service", None)
    monkeypatch.setattr(message_module, "search_provider", search_provider)
    monkeypatch.setattr(message_module, "SEARCH_ENABLED", True)
    monkeypatch.setattr(message_module, "SEARCH_TRIGGER_MODE", "hybrid")
    monkeypatch.setattr(message_module, "SEARCH_EXPLICIT_PREFIX", "search:")
    monkeypatch.setattr(message_module, "SEARCH_MIN_QUERY_LENGTH", 5)
    monkeypatch.setattr(message_module, "SEARCH_MAX_RESULTS", 5)
    monkeypatch.setattr(message_module, "log_response", _fake_log_response)

    return stub_rag, stub_llm, log_calls


def test_decide_search_explicit_prefix(monkeypatch) -> None:
    monkeypatch.setattr(message_module, "SEARCH_ENABLED", True)
    monkeypatch.setattr(message_module, "search_provider", object())
    monkeypatch.setattr(message_module, "SEARCH_EXPLICIT_PREFIX", "search:")
    monkeypatch.setattr(message_module, "SEARCH_MIN_QUERY_LENGTH", 5)

    decision = message_module._decide_search("search: latest shorekeeper update")

    assert decision.reason == "search_explicit"
    assert decision.query == "latest shorekeeper update"
    assert decision.should_search is True


def test_decide_search_freshness_trigger(monkeypatch) -> None:
    monkeypatch.setattr(message_module, "SEARCH_ENABLED", True)
    monkeypatch.setattr(message_module, "search_provider", object())
    monkeypatch.setattr(message_module, "SEARCH_TRIGGER_MODE", "hybrid")

    decision = message_module._decide_search("latest market news for Wuthering Waves")

    assert decision.reason == "search_freshness"
    assert decision.should_search is True


def test_decide_search_skips_lore_queries(monkeypatch) -> None:
    monkeypatch.setattr(message_module, "SEARCH_ENABLED", True)
    monkeypatch.setattr(message_module, "search_provider", object())

    decision = message_module._decide_search("Tell me Camellya lore and abilities.")

    assert decision.reason == "search_not_needed"
    assert decision.should_search is False


def test_decide_search_skips_short_explicit_query(monkeypatch) -> None:
    monkeypatch.setattr(message_module, "SEARCH_ENABLED", True)
    monkeypatch.setattr(message_module, "search_provider", object())
    monkeypatch.setattr(message_module, "SEARCH_EXPLICIT_PREFIX", "search:")
    monkeypatch.setattr(message_module, "SEARCH_MIN_QUERY_LENGTH", 5)

    decision = message_module._decide_search("search: hi")

    assert decision.reason == "search_not_needed"
    assert decision.should_search is False


def test_decide_search_disabled_bypasses(monkeypatch) -> None:
    monkeypatch.setattr(message_module, "SEARCH_ENABLED", False)
    monkeypatch.setattr(message_module, "search_provider", object())

    decision = message_module._decide_search("latest shorekeeper update")

    assert decision.reason == "search_disabled"
    assert decision.should_search is False


def test_build_system_prompt_appends_search_context() -> None:
    execution = message_module.SearchExecution(
        used=True,
        reason="search_freshness",
        query="latest shorekeeper update",
        provider="searxng",
        result_count=1,
        duration=0.1,
        error=None,
        bundle=SearchBundle(
            query="latest shorekeeper update",
            provider="searxng",
            used_fallback_query=False,
            results=[
                SearchResult(
                    title="Latest Patch Notes",
                    url="https://example.com/patch",
                    snippet="Version 2.4 patch notes and live changes.",
                    source="example.com",
                    published_at="2026-06-13",
                    score=1.0,
                )
            ],
        ),
    )

    prompt = message_module._build_system_prompt(
        personalization="Calm and observant.",
        manifest="Known records manifest.",
        context_text="Grounded lore section.",
        relevant_memories=[],
        search_execution=execution,
    )

    assert "Grounded lore section." in prompt
    assert "=== LIVE SEARCH RESULTS ===" in prompt
    assert "Latest Patch Notes" in prompt


def test_build_system_prompt_skips_search_context_without_results() -> None:
    execution = message_module.SearchExecution(
        used=False,
        reason="search_not_needed",
        query="",
        provider="searxng",
        result_count=0,
        duration=0.0,
        error=None,
    )

    prompt = message_module._build_system_prompt(
        personalization="Calm and observant.",
        manifest="Known records manifest.",
        context_text="Grounded lore section.",
        relevant_memories=[],
        search_execution=execution,
    )

    assert "Grounded lore section." in prompt
    assert "=== LIVE SEARCH RESULTS ===" not in prompt


def test_on_message_uses_explicit_search_results(monkeypatch) -> None:
    search = _SuccessSearchProvider()
    _, stub_llm, log_calls = _configure_runtime(monkeypatch, search_provider=search)
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> search: latest shorekeeper update", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert search.calls == [("latest shorekeeper update", 5)]
    assert msg.replies == ["The tides remain steady."]
    assert "=== LIVE SEARCH RESULTS ===" in stub_llm.last_messages[0]["content"]
    assert log_calls[0]["search_used"] is True


def test_on_message_falls_back_when_search_fails(monkeypatch) -> None:
    _, stub_llm, log_calls = _configure_runtime(
        monkeypatch,
        search_provider=_FailingSearchProvider(),
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> search: latest shorekeeper update", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert "=== LIVE SEARCH RESULTS ===" not in stub_llm.last_messages[0]["content"]
    assert "Live search was unavailable for this response." in stub_llm.last_messages[0]["content"]
    assert log_calls[0]["search_reason"] == "search_failed_continue_without_results"
    assert log_calls[0]["search_error"] == "backend unavailable"


def test_on_message_handles_explicit_search_with_no_results(monkeypatch) -> None:
    _, stub_llm, log_calls = _configure_runtime(
        monkeypatch,
        search_provider=_EmptySearchProvider(),
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> search: latest shorekeeper update", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert "=== LIVE SEARCH RESULTS ===" not in stub_llm.last_messages[0]["content"]
    assert "Live search was unavailable for this response." in stub_llm.last_messages[0]["content"]
    assert log_calls[0]["search_error"] == "Search returned no results"


def test_on_message_uses_freshness_query_search(monkeypatch) -> None:
    search = _SuccessSearchProvider()
    _, stub_llm, _ = _configure_runtime(monkeypatch, search_provider=search)
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> latest Wuthering Waves update news", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert search.calls == [("latest Wuthering Waves update news", 5)]
    assert "=== LIVE SEARCH RESULTS ===" in stub_llm.last_messages[0]["content"]


def test_on_message_keeps_lore_queries_rag_only(monkeypatch) -> None:
    search = _SuccessSearchProvider()
    _, stub_llm, log_calls = _configure_runtime(monkeypatch, search_provider=search)
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> Tell me Camellya lore.", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert search.calls == []
    assert "=== LIVE SEARCH RESULTS ===" not in stub_llm.last_messages[0]["content"]
    assert log_calls[0]["search_reason"] == "search_not_needed"
