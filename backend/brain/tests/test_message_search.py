import asyncio
import json
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from handlers import conversation_context
from handlers import message as message_module
from handlers import search_command as search_command_module
from services.search import SearchBundle, SearchResult


class _StubRag:
    def __init__(self, results=None) -> None:
        self.calls: list[tuple[str, int]] = []
        self.results = results or []

    def search(self, query: str, top_k: int = 0) -> list[dict]:
        self.calls.append((query, top_k))
        return list(self.results)

    def get_personalization_context(self) -> str:
        return "Calm and observant."

    def get_manifest(self) -> str:
        return "Known records manifest."


class _StubLLM:
    def __init__(self) -> None:
        self.model = "stub-model"
        self.calls: list[list[dict]] = []
        self.responses: list[dict] = []

    async def chat(self, messages: list[dict]) -> dict:
        self.calls.append(messages)
        if self.responses:
            response = self.responses.pop(0)
            if isinstance(response, Exception):
                raise response
            return response
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


class _Author:
    def __init__(self, user_id: int) -> None:
        self.id = user_id

    def __str__(self) -> str:
        return "Rover"


class _Message:
    def __init__(self, *, content: str, bot_user) -> None:
        self.content = content
        self.author = _Author(123)
        self.guild = SimpleNamespace(id=789)
        self.channel = _Channel()
        self.mentions = [bot_user]
        self.reference = None
        self.replies: list[str] = []

    async def reply(self, content: str) -> None:
        self.replies.append(content)


class _SuccessSearchProvider:
    def __init__(self, *, exact_claim_allowed=False, confidence_summary="medium") -> None:
        self.calls: list[tuple[str, int, str, str, bool]] = []
        self.exact_claim_allowed = exact_claim_allowed
        self.confidence_summary = confidence_summary

    async def search(self, query: str, limit: int, **kwargs) -> SearchBundle:
        self.calls.append(
            (
                query,
                limit,
                kwargs.get("label", ""),
                kwargs.get("question_type", ""),
                kwargs.get("freshness_required", False),
            )
        )
        return SearchBundle(
            query=query,
            provider="searxng",
            used_fallback_query=False,
            label=kwargs.get("label", ""),
            confidence_summary=self.confidence_summary,
            exact_claim_allowed=self.exact_claim_allowed,
            evidence_summary="Evidence is somewhat relevant but not exact.",
            agreement_status="agree" if self.exact_claim_allowed else "insufficient_trusted",
            trusted_result_count=2 if self.exact_claim_allowed else 1,
            fallback_result_count=0,
            exact_claim_reason="trusted agreement"
            if self.exact_claim_allowed
            else "not corroborated",
            response_mode="exact" if self.exact_claim_allowed else "summary",
            results=[
                SearchResult(
                    title="Specific factual result",
                    url="https://example.com/fact",
                    snippet="Specific evidence for the requested fact.",
                    source="example.com",
                    published_at="2026-06-13",
                    score=1.0,
                    source_class="reference",
                    rank_score=5.0,
                    rank_reason="reference; entity=1.00; fact=0.80; specificity=0.75",
                    entity_match_score=1.0,
                    fact_match_score=0.8,
                    specificity_score=0.75,
                    evidence_quality="medium",
                    supports_exact_answer=self.exact_claim_allowed,
                    surface_class="news_post",
                    freshness_bucket="recent",
                )
            ],
        )


class _CustomSearchProvider:
    def __init__(self, bundle: SearchBundle) -> None:
        self.bundle = bundle
        self.calls: list[str] = []

    async def search(self, query: str, limit: int, **kwargs) -> SearchBundle:
        self.calls.append(query)
        return self.bundle


class _InteractionResponse:
    def __init__(self) -> None:
        self.sent: list[str] = []
        self.deferred = False

    async def send_message(self, content: str) -> None:
        self.sent.append(content)

    async def defer(self, *, thinking: bool = False) -> None:
        self.deferred = thinking


class _InteractionFollowup:
    def __init__(self) -> None:
        self.sent: list[str] = []

    async def send(self, content: str) -> None:
        self.sent.append(content)


class _Interaction:
    def __init__(self) -> None:
        self.response = _InteractionResponse()
        self.followup = _InteractionFollowup()
        self.user = SimpleNamespace(id=123, __str__=lambda: "Rover")
        self.channel = SimpleNamespace(__str__=lambda: "bot")


def _analysis_response(
    *,
    rag_query: str,
    can_answer_from_general_knowledge: bool,
    general_knowledge_confidence: float,
    reason: str,
) -> dict:
    payload = {
        "rag_query": rag_query,
        "can_answer_from_general_knowledge": can_answer_from_general_knowledge,
        "general_knowledge_confidence": general_knowledge_confidence,
        "reason": reason,
    }
    return {
        "model": "stub-model",
        "message": {"content": json.dumps(payload)},
        "prompt_eval_count": 1,
        "eval_count": 1,
        "prompt_eval_duration": 1,
        "eval_duration": 1,
    }


def _final_response(text: str) -> dict:
    return {
        "model": "stub-model",
        "message": {"content": text},
        "prompt_eval_count": 1,
        "eval_count": 1,
        "prompt_eval_duration": 1,
        "eval_duration": 1,
    }


def _configure_message_runtime(
    monkeypatch,
    *,
    rag_results=None,
    llm_responses=None,
):
    conversation_context.conversation_context.clear()
    stub_rag = _StubRag(results=rag_results)
    stub_llm = _StubLLM()
    stub_llm.responses = list(llm_responses or [])
    log_calls: list[dict] = []

    def _fake_log_response(*args, **kwargs) -> None:
        log_calls.append(kwargs)

    monkeypatch.setattr(message_module, "rag", stub_rag)
    monkeypatch.setattr(message_module, "llm_client", stub_llm)
    monkeypatch.setattr(message_module, "memory_service", None)
    monkeypatch.setattr(message_module, "ANALYSIS_ENABLED", True)
    monkeypatch.setattr(message_module, "ANALYSIS_TIMEOUT_SECONDS", 6.0)
    monkeypatch.setattr(message_module, "RAG_ANSWER_SCORE_THRESHOLD", 0.62)
    monkeypatch.setattr(message_module, "GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD", 0.70)
    monkeypatch.setattr(message_module, "ROUTER_HISTORY_TURNS", 3)
    monkeypatch.setattr(message_module, "log_response", _fake_log_response)

    return stub_rag, stub_llm, log_calls


def _configure_slash_runtime(monkeypatch, *, search_provider, llm_responses=None):
    stub_rag = _StubRag()
    stub_llm = _StubLLM()
    stub_llm.responses = list(llm_responses or [])
    log_calls: list[dict] = []

    def _fake_log_response(*args, **kwargs) -> None:
        log_calls.append(kwargs)

    monkeypatch.setattr(search_command_module, "rag", stub_rag)
    monkeypatch.setattr(search_command_module, "llm_client", stub_llm)
    monkeypatch.setattr(search_command_module, "search_provider", search_provider)
    monkeypatch.setattr(search_command_module, "log_response", _fake_log_response)
    return stub_rag, stub_llm, log_calls


def test_build_system_prompt_warns_when_exact_claims_not_allowed() -> None:
    execution = message_module.SearchExecution(
        used=True,
        reason="slash_search",
        query="query",
        provider="searxng",
        result_count=1,
        duration=0.1,
        error=None,
        bundles=[
            SearchBundle(
                query="query",
                provider="searxng",
                used_fallback_query=False,
                label="general",
                confidence_summary="low",
                exact_claim_allowed=False,
                evidence_summary="Evidence is generic or weak.",
                results=[
                    SearchResult(
                        title="Portal page",
                        url="https://example.com/",
                        snippet="Generic homepage",
                        source="example.com",
                        published_at=None,
                        score=1.0,
                    )
                ],
            )
        ],
    )

    prompt = message_module._build_system_prompt(
        source_path="search",
        personalization="Calm and observant.",
        manifest="Known records manifest.",
        resolved_query="query",
        relevant_memories=[],
        rag_decision=None,
        search_execution=execution,
    )

    assert "do not state exact prices" in prompt.lower()
    assert "Exact claims allowed: False" in prompt


def test_analysis_fallback_builds_safe_default() -> None:
    decision = message_module._analysis_fallback("whats the latest nvidia price?", [])

    assert decision.rag_query == "whats the latest nvidia price"
    assert decision.can_answer_from_general_knowledge is False


def test_on_message_uses_local_datetime_without_llm(monkeypatch) -> None:
    stub_rag, stub_llm, log_calls = _configure_message_runtime(monkeypatch)
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> whats the date today?", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert stub_rag.calls == []
    assert stub_llm.calls == []
    assert log_calls[0]["final_path"] == "local-datetime"
    assert log_calls[0]["deterministic_gate"] == "datetime"


def test_message_search_prefix_no_longer_triggers_live_search(monkeypatch) -> None:
    _, stub_llm, log_calls = _configure_message_runtime(
        monkeypatch,
        llm_responses=[
            _analysis_response(
                rag_query="search latest nvidia share price",
                can_answer_from_general_knowledge=False,
                general_knowledge_confidence=0.1,
                reason="current fact requires slash search",
            )
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> search: latest nvidia share price", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert len(stub_llm.calls) == 1
    assert "do not know that accurately" in msg.replies[0].lower()
    assert log_calls[0]["final_path"] == "uncertain"


def test_non_time_sensitive_prompt_uses_rag_when_strong(monkeypatch) -> None:
    rag_results = [
        {
            "score": 0.83,
            "source": "lore/black_shores.md",
            "heading": "Black Shores",
            "text": "The Black Shores are a sanctuary.",
        }
    ]
    stub_rag, stub_llm, log_calls = _configure_message_runtime(
        monkeypatch,
        rag_results=rag_results,
        llm_responses=[
            _analysis_response(
                rag_query="tell me about black shores",
                can_answer_from_general_knowledge=False,
                general_knowledge_confidence=0.0,
                reason="stable local knowledge",
            ),
            _final_response("The Black Shores are a sanctuary."),
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)

    asyncio.run(
        message_module.on_message(
            bot, _Message(content="<@999> tell me about black shores", bot_user=bot_user)
        )
    )

    assert stub_rag.calls == [("tell me about black shores", 5)]
    assert len(stub_llm.calls) == 2
    assert log_calls[0]["rag_accepted"] is True
    assert log_calls[0]["final_path"] == "rag-grounded"


def test_weak_rag_falls_back_to_general_when_analysis_confident(monkeypatch) -> None:
    rag_results = [{"score": 0.22, "source": "lore.md", "heading": "Lore", "text": "Weak match."}]
    _, stub_llm, log_calls = _configure_message_runtime(
        monkeypatch,
        rag_results=rag_results,
        llm_responses=[
            _analysis_response(
                rag_query="what does transmission mean",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.91,
                reason="stable definition",
            ),
            _final_response("Transmission means sending something from one place to another."),
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)

    asyncio.run(
        message_module.on_message(
            bot, _Message(content="<@999> what does transmission mean?", bot_user=bot_user)
        )
    )

    assert len(stub_llm.calls) == 2
    assert log_calls[0]["rag_accepted"] is False
    assert log_calls[0]["final_path"] == "general-knowledge"


def test_weak_rag_low_general_confidence_returns_uncertain(monkeypatch) -> None:
    rag_results = [{"score": 0.15, "source": "lore.md", "heading": "Lore", "text": "Weak match."}]
    _, stub_llm, log_calls = _configure_message_runtime(
        monkeypatch,
        rag_results=rag_results,
        llm_responses=[
            _analysis_response(
                rag_query="what is ligma exactly",
                can_answer_from_general_knowledge=False,
                general_knowledge_confidence=0.2,
                reason="unsafe to answer",
            ),
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> what is ligma exactly?", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert len(stub_llm.calls) == 1
    assert "do not know that accurately" in msg.replies[0].lower()
    assert log_calls[0]["final_path"] == "uncertain"


def test_definition_prompt_bypasses_rag_and_uses_general_knowledge(monkeypatch) -> None:
    stub_rag, _, log_calls = _configure_message_runtime(
        monkeypatch,
        rag_results=[
            {"score": 0.99, "source": "lore.md", "heading": "Lore", "text": "Irrelevant lore"}
        ],
        llm_responses=[
            _analysis_response(
                rag_query='what does the word "approximately" mean',
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.9,
                reason="dictionary definition",
            ),
            _final_response("Approximately means nearly, but not exactly."),
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)

    asyncio.run(
        message_module.on_message(
            bot,
            _Message(content='<@999> what does the word "approximately" mean?', bot_user=bot_user),
        )
    )

    assert stub_rag.calls == []
    assert log_calls[0]["final_path"] == "general-knowledge"


def test_identity_prompt_bypasses_rag_when_not_lore(monkeypatch) -> None:
    stub_rag, _, log_calls = _configure_message_runtime(
        monkeypatch,
        rag_results=[
            {"score": 0.99, "source": "identity.md", "heading": "Identity", "text": "Shorekeeper"}
        ],
        llm_responses=[
            _analysis_response(
                rag_query="what is your name",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.95,
                reason="identity question",
            ),
            _final_response("I am Shorekeeper."),
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)

    asyncio.run(
        message_module.on_message(
            bot, _Message(content="<@999> whats your name?", bot_user=bot_user)
        )
    )

    assert stub_rag.calls == []
    assert log_calls[0]["final_path"] == "general-knowledge"


def test_slash_search_returns_disabled_when_search_off(monkeypatch) -> None:
    monkeypatch.setattr(search_command_module, "SEARCH_ENABLED", False)
    _, _, log_calls = _configure_slash_runtime(monkeypatch, search_provider=None)
    interaction = _Interaction()

    asyncio.run(
        search_command_module.handle_search_interaction(
            cast(Any, interaction),
            query="latest nvidia price",
        )
    )

    assert interaction.response.sent == [
        "Live search is currently disabled in my records, so I cannot look that up for you right now."
    ]
    assert interaction.followup.sent == []
    assert log_calls[0]["final_path"] == "search-disabled"
    assert log_calls[0]["query_type"] == "slash-search"
    assert log_calls[0]["search_used"] is False


def test_slash_search_returns_successful_search_reply(monkeypatch) -> None:
    monkeypatch.setattr(search_command_module, "SEARCH_ENABLED", True)
    search = _SuccessSearchProvider(exact_claim_allowed=True, confidence_summary="high")
    _, stub_llm, log_calls = _configure_slash_runtime(
        monkeypatch,
        search_provider=search,
        llm_responses=[_final_response("The latest reports place it at a steady value.")],
    )
    interaction = _Interaction()

    asyncio.run(
        search_command_module.handle_search_interaction(
            cast(Any, interaction),
            query="latest nvidia stock price",
        )
    )

    assert interaction.response.deferred is True
    assert interaction.followup.sent == ["The latest reports place it at a steady value."]
    assert search.calls == [("latest nvidia stock price", 5, "slash", "current_metric", True)]
    assert len(stub_llm.calls) == 1
    system_prompt = stub_llm.calls[0][0]["content"]
    assert "consulted the outside world for reliable signals" in system_prompt
    assert "Do NOT say the information is outside your records" in system_prompt
    assert log_calls[0]["final_path"] == "search-grounded"
    assert log_calls[0]["search_used"] is True
    assert log_calls[0]["search_query"] == "latest nvidia stock price"


def test_slash_search_returns_uncertain_on_weak_evidence(monkeypatch) -> None:
    monkeypatch.setattr(search_command_module, "SEARCH_ENABLED", True)
    bundle = SearchBundle(
        query="latest version of Wuthering Waves",
        provider="searxng",
        used_fallback_query=False,
        label="slash",
        confidence_summary="low",
        exact_claim_allowed=False,
        evidence_summary="Current reports are mixed across trusted sources",
        agreement_status="disagree",
        trusted_result_count=2,
        fallback_result_count=0,
        exact_claim_reason="trusted results disagree",
        response_mode="uncertain",
        results=[
            SearchResult(
                title="Wuthering Waves Version 3.4",
                url="https://example.com/news/3-4",
                snippet="Version 3.4 patch notes.",
                source="example.com",
                published_at="2026-06-13",
                score=1.0,
                source_class="official",
                surface_class="patch_notes",
                freshness_bucket="recent",
                evidence_quality="high",
                supports_exact_answer=False,
            )
        ],
    )
    _, stub_llm, log_calls = _configure_slash_runtime(
        monkeypatch,
        search_provider=_CustomSearchProvider(bundle),
    )
    interaction = _Interaction()

    asyncio.run(
        search_command_module.handle_search_interaction(
            cast(Any, interaction),
            query="latest version of Wuthering Waves",
        )
    )

    assert stub_llm.calls == []
    assert interaction.followup.sent == [
        "Current reports are too mixed or weak for me to state that confidently. I would rather leave it uncertain than offer you a false exact answer."
    ]
    assert log_calls[0]["final_path"] == "uncertain"
    assert log_calls[0]["search_used"] is True


def test_slash_search_returns_runtime_error_when_llm_fails(monkeypatch) -> None:
    monkeypatch.setattr(search_command_module, "SEARCH_ENABLED", True)
    search = _SuccessSearchProvider(exact_claim_allowed=False, confidence_summary="medium")
    _, stub_llm, log_calls = _configure_slash_runtime(
        monkeypatch,
        search_provider=search,
        llm_responses=[RuntimeError("upstream provider disconnected")],
    )
    interaction = _Interaction()

    asyncio.run(
        search_command_module.handle_search_interaction(
            cast(Any, interaction),
            query="latest version of wuthering waves",
        )
    )

    assert len(stub_llm.calls) == 1
    assert interaction.followup.sent == [
        "The signals beyond these shores have grown turbulent for a moment. I could not finish assembling a reliable answer just now."
    ]
    assert log_calls[0]["final_path"] == "search-runtime-error"


def test_slash_search_returns_rate_limited_message_when_llm_is_throttled(monkeypatch) -> None:
    monkeypatch.setattr(search_command_module, "SEARCH_ENABLED", True)
    bundle = SearchBundle(
        query="nvidia stock prices today",
        provider="searxng",
        used_fallback_query=False,
        label="slash",
        confidence_summary="medium",
        exact_claim_allowed=False,
        evidence_summary="Trusted evidence is relevant but not corroborated enough for exact claims",
        agreement_status="insufficient_trusted",
        trusted_result_count=3,
        fallback_result_count=0,
        exact_claim_reason="fewer than two trusted results",
        response_mode="summary",
        results=[
            SearchResult(
                title="(NVDA.O) | Stock Price & Latest News | Reuters",
                url="https://www.reuters.com/markets/companies/NVDA.O/",
                snippet="Company Information NVIDIA Corporation is an artificial intelligence (AI) infrastructure company.",
                source="www.reuters.com",
                extracted_text="NVIDIA stock reporting remains active across market desks, though the exact intraday figure shifts too quickly for a stable quoted value here.",
                published_at=None,
                score=1.0,
                source_class="reference",
                evidence_quality="high",
                supports_exact_answer=False,
            ),
            SearchResult(
                title="NVDA Stock Price | MarketWatch",
                url="https://www.marketwatch.com/investing/stock/nvda",
                snippet="View real-time stock prices and stock quotes for a full financial overview.",
                source="www.reuters.com",
                published_at=None,
                score=1.0,
                source_class="reference",
                evidence_quality="high",
                supports_exact_answer=False,
            ),
            SearchResult(
                title="NVIDIA Corporation (NVDA) Stock Price | Yahoo Finance",
                url="https://finance.yahoo.com/quote/NVDA/",
                snippet="Find the latest NVIDIA Corporation stock quote, history, news and other vital information.",
                source="finance.yahoo.com",
                published_at=None,
                score=1.0,
                source_class="reference",
                evidence_quality="high",
                supports_exact_answer=False,
            ),
        ],
    )
    _, stub_llm, log_calls = _configure_slash_runtime(
        monkeypatch,
        search_provider=_CustomSearchProvider(bundle),
        llm_responses=[
            RuntimeError("OpenAI-compatible model call failed (HTTP 429): rate limit exceeded")
        ],
    )
    interaction = _Interaction()

    asyncio.run(
        search_command_module.handle_search_interaction(
            cast(Any, interaction),
            query="latest version of wuthering waves",
        )
    )

    assert len(stub_llm.calls) == 1
    assert len(interaction.followup.sent) == 1
    assert "The archive holds little on this matter" in interaction.followup.sent[0]
    assert "www.reuters.com, finance.yahoo.com" in interaction.followup.sent[0]
    assert "not aligned enough for a precise live claim" in interaction.followup.sent[0]
    assert "exact intraday figure shifts too quickly" in interaction.followup.sent[0]
    assert log_calls[0]["final_path"] == "search-rate-limited"


def test_register_search_command_registers_once() -> None:
    class _FakeTree:
        def __init__(self) -> None:
            self.commands: dict[str, SimpleNamespace] = {}

        def get_command(self, name: str):
            return self.commands.get(name)

        def command(self, *, name: str, description: str):
            def _decorator(func):
                self.commands[name] = SimpleNamespace(
                    name=name,
                    description=description,
                    callback=func,
                )
                return func

            return _decorator

    tree = _FakeTree()

    search_command_module.register_search_command(cast(Any, tree))
    search_command_module.register_search_command(cast(Any, tree))

    assert list(tree.commands) == ["search"]
    assert tree.commands["search"].description == "Search the live web for current information"
