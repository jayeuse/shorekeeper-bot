import asyncio
import json
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from handlers import conversation_context
from handlers import message as message_module
from services.search import SearchBundle, SearchError, SearchResult


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
            return self.responses.pop(0)
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


class _EmptySearchProvider:
    async def search(self, query: str, limit: int, **kwargs) -> SearchBundle:
        return SearchBundle(
            query=query,
            provider="searxng",
            used_fallback_query=False,
            label=kwargs.get("label", ""),
            confidence_summary="low",
            exact_claim_allowed=False,
            evidence_summary="No usable evidence.",
            agreement_status="none",
            trusted_result_count=0,
            fallback_result_count=0,
            exact_claim_reason="no results",
            response_mode="uncertain",
            results=[],
        )


class _FailingSearchProvider:
    async def search(self, query: str, limit: int, **kwargs) -> SearchBundle:
        raise SearchError("backend unavailable")


class _CustomSearchProvider:
    def __init__(self, bundle: SearchBundle) -> None:
        self.bundle = bundle
        self.calls: list[str] = []

    async def search(self, query: str, limit: int, **kwargs) -> SearchBundle:
        self.calls.append(query)
        return self.bundle


def _analysis_response(
    *,
    time_sensitive: bool,
    search_query: str,
    rag_query: str,
    can_answer_from_general_knowledge: bool,
    general_knowledge_confidence: float,
    reason: str,
) -> dict:
    payload = {
        "time_sensitive": time_sensitive,
        "search_query": search_query,
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


def _configure_runtime(
    monkeypatch,
    *,
    rag_results=None,
    search_provider=None,
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
    monkeypatch.setattr(message_module, "search_provider", search_provider)
    monkeypatch.setattr(message_module, "SEARCH_ENABLED", True)
    monkeypatch.setattr(message_module, "SEARCH_EXPLICIT_PREFIX", "search:")
    monkeypatch.setattr(message_module, "SEARCH_MIN_QUERY_LENGTH", 5)
    monkeypatch.setattr(message_module, "SEARCH_MAX_RESULTS", 5)
    monkeypatch.setattr(message_module, "SEARCH_TRIGGER_MODE", "hybrid")
    monkeypatch.setattr(message_module, "ANALYSIS_ENABLED", True)
    monkeypatch.setattr(message_module, "ANALYSIS_TIMEOUT_SECONDS", 6.0)
    monkeypatch.setattr(message_module, "RAG_ANSWER_SCORE_THRESHOLD", 0.62)
    monkeypatch.setattr(message_module, "GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD", 0.70)
    monkeypatch.setattr(message_module, "ROUTER_HISTORY_TURNS", 3)
    monkeypatch.setattr(message_module, "log_response", _fake_log_response)

    return stub_rag, stub_llm, log_calls


def test_build_system_prompt_warns_when_exact_claims_not_allowed() -> None:
    execution = message_module.SearchExecution(
        used=True,
        reason="analysis_time_sensitive",
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

    assert decision.time_sensitive is True
    assert "nvidia" in decision.search_query
    assert decision.rag_query == "whats the latest nvidia price"


def test_on_message_uses_local_datetime_without_llm(monkeypatch) -> None:
    stub_rag, stub_llm, log_calls = _configure_runtime(
        monkeypatch,
        search_provider=_SuccessSearchProvider(),
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> whats the date today?", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert stub_rag.calls == []
    assert stub_llm.calls == []
    assert log_calls[0]["final_path"] == "local-datetime"
    assert log_calls[0]["deterministic_gate"] == "datetime"


def test_on_message_explicit_search_bypasses_analysis(monkeypatch) -> None:
    search = _SuccessSearchProvider()
    _, stub_llm, log_calls = _configure_runtime(monkeypatch, search_provider=search)
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> search: latest nvidia share price", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert search.calls == [("latest nvidia share price", 5, "explicit", "current_metric", True)]
    assert len(stub_llm.calls) == 1
    assert log_calls[0]["analysis_used"] is False
    assert log_calls[0]["final_path"] == "explicit-search"


def test_on_message_explicit_search_returns_disabled_when_search_off(monkeypatch) -> None:
    search = _SuccessSearchProvider()
    _, stub_llm, log_calls = _configure_runtime(monkeypatch, search_provider=search)
    monkeypatch.setattr(message_module, "SEARCH_ENABLED", False)
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> search: latest nvidia share price", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert search.calls == []
    assert stub_llm.calls == []
    assert "search is currently disabled" in msg.replies[0].lower()
    assert log_calls[0]["final_path"] == "search-disabled"


def test_time_sensitive_prompt_forces_search(monkeypatch) -> None:
    search = _SuccessSearchProvider()
    _, stub_llm, log_calls = _configure_runtime(
        monkeypatch,
        search_provider=search,
        llm_responses=[
            _analysis_response(
                time_sensitive=True,
                search_query="current nvidia stock price",
                rag_query="current nvidia stock price",
                can_answer_from_general_knowledge=False,
                general_knowledge_confidence=0.1,
                reason="current external fact",
            ),
            _final_response("I checked the latest market data."),
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> whats the current nvidia stock pricing?", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert search.calls == [("current nvidia stock price", 5, "primary", "current_metric", True)]
    assert len(stub_llm.calls) == 2
    assert log_calls[0]["analysis_time_sensitive"] is True
    assert log_calls[0]["final_path"] == "search-grounded"


def test_explicit_search_mode_disables_automatic_search(monkeypatch) -> None:
    search = _SuccessSearchProvider()
    stub_rag, _, log_calls = _configure_runtime(
        monkeypatch,
        rag_results=[
            {"score": 0.10, "source": "lore.md", "heading": "Lore", "text": "Weak match."}
        ],
        search_provider=search,
        llm_responses=[
            _analysis_response(
                time_sensitive=True,
                search_query="current nvidia stock price",
                rag_query="current nvidia stock price",
                can_answer_from_general_knowledge=False,
                general_knowledge_confidence=0.1,
                reason="current external fact",
            ),
        ],
    )
    monkeypatch.setattr(message_module, "SEARCH_TRIGGER_MODE", "explicit")
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> whats the current nvidia stock price?", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert search.calls == []
    assert stub_rag.calls == []
    assert "do not know that accurately" in msg.replies[0].lower()
    assert log_calls[0]["final_path"] == "uncertain"


def test_current_domain_specific_fact_still_forces_search_not_rag(monkeypatch) -> None:
    search = _SuccessSearchProvider()
    stub_rag, _, log_calls = _configure_runtime(
        monkeypatch,
        rag_results=[{"score": 0.99, "source": "lore.md", "heading": "Lore", "text": "Old lore"}],
        search_provider=search,
        llm_responses=[
            _analysis_response(
                time_sensitive=True,
                search_query="latest version of wuthering waves",
                rag_query="latest version of wuthering waves",
                can_answer_from_general_knowledge=False,
                general_knowledge_confidence=0.1,
                reason="latest external fact",
            ),
            _final_response("I checked the latest release reports."),
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)

    asyncio.run(
        message_module.on_message(
            bot,
            _Message(
                content="<@999> whats the latest version of wuthering waves?", bot_user=bot_user
            ),
        )
    )

    assert stub_rag.calls == []
    assert search.calls == [
        ("latest version of wuthering waves", 5, "primary", "latest_release", True)
    ]
    assert log_calls[0]["final_path"] == "search-grounded"


def test_non_time_sensitive_prompt_uses_rag_when_strong(monkeypatch) -> None:
    rag_results = [
        {
            "score": 0.83,
            "source": "lore/black_shores.md",
            "heading": "Black Shores",
            "text": "The Black Shores are a sanctuary.",
        }
    ]
    stub_rag, stub_llm, log_calls = _configure_runtime(
        monkeypatch,
        rag_results=rag_results,
        search_provider=_SuccessSearchProvider(),
        llm_responses=[
            _analysis_response(
                time_sensitive=False,
                search_query="",
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
    _, stub_llm, log_calls = _configure_runtime(
        monkeypatch,
        rag_results=rag_results,
        search_provider=_SuccessSearchProvider(),
        llm_responses=[
            _analysis_response(
                time_sensitive=False,
                search_query="",
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
    _, stub_llm, log_calls = _configure_runtime(
        monkeypatch,
        rag_results=rag_results,
        search_provider=_SuccessSearchProvider(),
        llm_responses=[
            _analysis_response(
                time_sensitive=False,
                search_query="",
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


def test_search_with_weak_exact_claims_produces_search_grounded_path(monkeypatch) -> None:
    search = _SuccessSearchProvider(exact_claim_allowed=False, confidence_summary="medium")
    _, _, log_calls = _configure_runtime(
        monkeypatch,
        search_provider=search,
        llm_responses=[
            _analysis_response(
                time_sensitive=True,
                search_query="current tesla stock price",
                rag_query="current tesla stock price",
                can_answer_from_general_knowledge=False,
                general_knowledge_confidence=0.1,
                reason="current external fact",
            ),
            _final_response("I checked the latest market reports and can only answer cautiously."),
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)

    asyncio.run(
        message_module.on_message(
            bot, _Message(content="<@999> whats tesla stock price today?", bot_user=bot_user)
        )
    )

    assert log_calls[0]["exact_claims_allowed"] is False
    assert log_calls[0]["search_evidence_summary"][0]["confidence_summary"] == "medium"
    assert log_calls[0]["final_path"] == "search-grounded"


def test_definition_prompt_bypasses_rag_and_uses_general_knowledge(monkeypatch) -> None:
    stub_rag, stub_llm, log_calls = _configure_runtime(
        monkeypatch,
        rag_results=[
            {"score": 0.99, "source": "lore.md", "heading": "Lore", "text": "Irrelevant lore"}
        ],
        search_provider=_SuccessSearchProvider(),
        llm_responses=[
            _analysis_response(
                time_sensitive=False,
                search_query="",
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
    assert (
        log_calls[0]["rag_rejection_reason"] in {"", "-"} or log_calls[0]["rag_accepted"] is False
    )


def test_identity_prompt_bypasses_rag_when_not_lore(monkeypatch) -> None:
    stub_rag, _, log_calls = _configure_runtime(
        monkeypatch,
        rag_results=[
            {"score": 0.99, "source": "identity.md", "heading": "Identity", "text": "Shorekeeper"}
        ],
        search_provider=_SuccessSearchProvider(),
        llm_responses=[
            _analysis_response(
                time_sensitive=False,
                search_query="",
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


def test_mixed_version_results_return_uncertain_not_exact(monkeypatch) -> None:
    bundle = SearchBundle(
        query="latest version of Wuthering Waves",
        provider="searxng",
        used_fallback_query=False,
        label="primary",
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
            ),
            SearchResult(
                title="Wuthering Waves Version 3.3",
                url="https://example.com/news/3-3",
                snippet="Version 3.3 patch notes.",
                source="example.com",
                published_at="2026-06-13",
                score=1.0,
                source_class="official",
                surface_class="patch_notes",
                freshness_bucket="recent",
                evidence_quality="high",
                supports_exact_answer=False,
            ),
        ],
    )
    _, stub_llm, log_calls = _configure_runtime(
        monkeypatch,
        search_provider=_CustomSearchProvider(bundle),
        llm_responses=[
            _analysis_response(
                time_sensitive=True,
                search_query="latest version of Wuthering Waves",
                rag_query="latest version of Wuthering Waves",
                can_answer_from_general_knowledge=False,
                general_knowledge_confidence=0.1,
                reason="latest external fact",
            ),
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)
    msg = _Message(content="<@999> whats the latest version of wuthering waves?", bot_user=bot_user)

    asyncio.run(message_module.on_message(bot, msg))

    assert len(stub_llm.calls) == 1
    assert "mixed or weak" in msg.replies[0].lower()
    assert log_calls[0]["final_path"] == "uncertain"
    assert log_calls[0]["search_evidence_summary"][0]["agreement_status"] == "disagree"


def test_logger_metadata_includes_surface_freshness_and_agreement(monkeypatch) -> None:
    search = _SuccessSearchProvider(exact_claim_allowed=False, confidence_summary="medium")
    _, _, log_calls = _configure_runtime(
        monkeypatch,
        search_provider=search,
        llm_responses=[
            _analysis_response(
                time_sensitive=True,
                search_query="current tesla stock price",
                rag_query="current tesla stock price",
                can_answer_from_general_knowledge=False,
                general_knowledge_confidence=0.1,
                reason="current external fact",
            ),
            _final_response("I checked the latest market reports and can only answer cautiously."),
        ],
    )
    bot_user = SimpleNamespace(id=999)
    bot = SimpleNamespace(user=bot_user)

    asyncio.run(
        message_module.on_message(
            bot, _Message(content="<@999> whats tesla stock price today?", bot_user=bot_user)
        )
    )

    first_result = log_calls[0]["search_results"][0]
    summary = log_calls[0]["search_evidence_summary"][0]
    assert "surface_class" in first_result
    assert "freshness_bucket" in first_result
    assert "agreement_status" in summary
    assert "response_mode" in summary
