import asyncio
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from handlers import message as message_module


def _analysis(
    *,
    time_sensitive: bool,
    search_query: str = "",
    rag_query: str = "",
    can_answer_from_general_knowledge: bool = False,
    general_knowledge_confidence: float = 0.0,
    reason: str = "test-analysis",
) -> message_module.AnalysisDecision:
    return message_module.AnalysisDecision(
        time_sensitive=time_sensitive,
        search_query=search_query,
        rag_query=rag_query,
        can_answer_from_general_knowledge=can_answer_from_general_knowledge,
        general_knowledge_confidence=general_knowledge_confidence,
        reason=reason,
        raw_payload={"source": "test"},
    )


async def _build_route_with_analysis(
    monkeypatch: pytest.MonkeyPatch,
    prompt: str,
    decision: message_module.AnalysisDecision,
    chat_history: list[dict] | None = None,
) -> message_module.RoutePlan:
    async def _fake_analysis(user_content: str, history: list[dict]) -> message_module.AnalysisDecision:
        assert user_content == prompt
        return decision

    monkeypatch.setattr(message_module, "_run_analysis_pass", _fake_analysis)
    monkeypatch.setattr(message_module, "SEARCH_TRIGGER_MODE", "hybrid")
    return await message_module._build_route_plan(prompt, chat_history or [])


@pytest.mark.parametrize(
    ("prompt", "expected_path", "expected_gate"),
    [
        ("whats the date today?", "datetime", "datetime"),
        ("what time is it right now?", "datetime", "datetime"),
        ("what day is it today?", "datetime", "datetime"),
        ("whats the date and time now?", "datetime", "datetime"),
        ("search: latest nvidia stock price", "search", "explicit_search"),
        ("search: current weather in tokyo", "search", "explicit_search"),
        ("search: now", "general", "explicit_search_short"),
        ("what was the first question i asked?", "memory", "memory"),
        ("do you remember what i told you earlier?", "memory", "memory"),
        ("what did i tell you previously?", "memory", "memory"),
        ("how are you today?", "general", "casual"),
        ("good morning", "general", "casual"),
        ("tell me about yourself", "general", "casual"),
        ("what factions are in your records?", "general", "meta"),
        ("what topics do you have?", "general", "meta"),
    ],
)
def test_prompt_matrix_deterministic_routes(prompt: str, expected_path: str, expected_gate: str) -> None:
    plan = message_module._build_deterministic_route_plan(prompt)

    assert plan is not None
    assert plan.path == expected_path
    assert plan.deterministic_gate == expected_gate


@pytest.mark.parametrize(
    ("prompt", "decision", "expected_query", "expected_fact", "expected_type", "expected_domain", "expected_entity"),
    [
        (
            "whats the current nvidia stock price?",
            _analysis(time_sensitive=True, search_query="NVIDIA current stock price"),
            "NVIDIA current stock price",
            "price per share",
            "current_metric",
            "finance",
            "NVIDIA",
        ),
        (
            "whats bitcoin trading at right now?",
            _analysis(time_sensitive=True, search_query="Bitcoin current price"),
            "Bitcoin current price",
            "",
            "background_fact",
            "general",
            "",
        ),
        pytest.param(
            "what is the latest ios version?",
            _analysis(time_sensitive=True, search_query="latest iOS version"),
            "latest iOS version",
            "latest version",
            "latest_release",
            "general",
            "",
            marks=pytest.mark.xfail(
                reason="requested_fact inference only recognizes phrases like 'latest version', not 'latest X version'"
            ),
        ),
        pytest.param(
            "what is the latest python version?",
            _analysis(time_sensitive=True, search_query="latest Python version"),
            "latest Python version",
            "latest version",
            "latest_release",
            "general",
            "",
            marks=pytest.mark.xfail(
                reason="requested_fact inference only recognizes phrases like 'latest version', not 'latest X version'"
            ),
        ),
        (
            "whats the latest version of wuthering waves?",
            _analysis(time_sensitive=True, search_query="latest version of Wuthering Waves"),
            "latest version of Wuthering Waves",
            "latest version",
            "latest_release",
            "game",
            "Wuthering Waves",
        ),
        (
            "who are the current banners in genshin impact?",
            _analysis(time_sensitive=True, search_query="Genshin Impact current character banners"),
            "Genshin Impact current character banners",
            "current banners",
            "current_availability",
            "game",
            "Genshin Impact",
        ),
        (
            "what are todays top headlines?",
            _analysis(time_sensitive=True, search_query="today top headlines"),
            "today top headlines",
            "",
            "background_fact",
            "general",
            "",
        ),
        (
            "what is the weather in manila today?",
            _analysis(time_sensitive=True, search_query="weather in Manila today"),
            "weather in Manila today",
            "",
            "background_fact",
            "general",
            "",
        ),
        pytest.param(
            "what is the latest minecraft version and when did it release?",
            _analysis(time_sensitive=True, search_query="latest Minecraft version release date"),
            "latest Minecraft version release date",
            "latest version",
            "latest_release",
            "general",
            "",
            marks=pytest.mark.xfail(
                reason="requested_fact inference misses 'latest <entity> version' query shapes"
            ),
        ),
        (
            "what is the current inflation rate in the us?",
            _analysis(time_sensitive=True, search_query="current US inflation rate"),
            "current US inflation rate",
            "",
            "background_fact",
            "general",
            "",
        ),
    ],
)
def test_prompt_matrix_time_sensitive_route_plan(
    monkeypatch: pytest.MonkeyPatch,
    prompt: str,
    decision: message_module.AnalysisDecision,
    expected_query: str,
    expected_fact: str,
    expected_type: str,
    expected_domain: str,
    expected_entity: str,
) -> None:
    plan = asyncio.run(_build_route_with_analysis(monkeypatch, prompt, decision))

    assert plan.path == "general"
    assert plan.analysis_used is True
    assert plan.query_text == (decision.rag_query or prompt)
    assert plan.requested_fact == expected_fact
    assert plan.question_type_hint == expected_type
    assert plan.subject_domain == expected_domain
    assert plan.target_entity == expected_entity
    assert plan.search_plans is not None
    assert plan.search_plans[0].query == expected_query
    assert plan.search_plans[0].freshness_required is True


@pytest.mark.parametrize(
    ("prompt", "decision", "expected_path", "expected_type", "expected_domain"),
    [
        (
            "tell me about black shores",
            _analysis(time_sensitive=False, rag_query="tell me about black shores"),
            "rag",
            "background_fact",
            "general",
        ),
        (
            "who is shorekeeper?",
            _analysis(time_sensitive=False, rag_query="who is Shorekeeper"),
            "rag",
            "background_fact",
            "general",
        ),
        (
            "what do you know about rinascita?",
            _analysis(time_sensitive=False, rag_query="what do you know about Rinascita"),
            "rag",
            "background_fact",
            "general",
        ),
        pytest.param(
            "what does transmission mean?",
            _analysis(
                time_sensitive=False,
                rag_query="what does transmission mean",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.9,
            ),
            "general",
            "definition",
            "language",
            marks=pytest.mark.xfail(
                reason="subject domain inference only recognizes explicit 'meaning'/'definition' wording"
            ),
        ),
        pytest.param(
            "define entropy",
            _analysis(
                time_sensitive=False,
                rag_query="define entropy",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.9,
            ),
            "general",
            "definition",
            "language",
            marks=pytest.mark.xfail(
                reason="definition inference does not recognize bare 'define <term>' prompts"
            ),
        ),
        (
            "what is photosynthesis?",
            _analysis(
                time_sensitive=False,
                rag_query="what is photosynthesis",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.85,
            ),
            "rag",
            "background_fact",
            "general",
        ),
        (
            "what is your name?",
            _analysis(
                time_sensitive=False,
                rag_query="what is your name",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.95,
            ),
            "general",
            "identity",
            "identity",
        ),
        (
            "who wrote 1984?",
            _analysis(
                time_sensitive=False,
                rag_query="who wrote 1984",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.9,
            ),
            "rag",
            "background_fact",
            "general",
        ),
        (
            "what is a database index?",
            _analysis(
                time_sensitive=False,
                rag_query="what is a database index",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.9,
            ),
            "rag",
            "background_fact",
            "general",
        ),
        (
            "difference between a compiler and an interpreter",
            _analysis(
                time_sensitive=False,
                rag_query="difference between a compiler and an interpreter",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.9,
            ),
            "rag",
            "background_fact",
            "general",
        ),
    ],
)
def test_prompt_matrix_non_time_sensitive_route_plan(
    monkeypatch: pytest.MonkeyPatch,
    prompt: str,
    decision: message_module.AnalysisDecision,
    expected_path: str,
    expected_type: str,
    expected_domain: str,
) -> None:
    plan = asyncio.run(_build_route_with_analysis(monkeypatch, prompt, decision))

    assert plan.path == expected_path
    assert plan.analysis_used is True
    assert plan.question_type_hint == expected_type
    assert plan.subject_domain == expected_domain


@pytest.mark.parametrize(
    ("chat_history", "expected_recent"),
    [
        (
            [
                {"role": "user", "content": "whats the latest version of minecraft?"},
                {"role": "assistant", "content": "stub"},
                {"role": "user", "content": "what about fortnite?"},
            ],
            ["what about fortnite?", "whats the latest version of minecraft?"],
        ),
        (
            [
                {"role": "user", "content": "<@999> whats the current nvidia stock price?"},
                {"role": "assistant", "content": "stub"},
                {"role": "user", "content": "<@999> what about tesla?"},
            ],
            ["what about tesla?", "whats the current nvidia stock price?"],
        ),
        (
            [
                {"role": "user", "content": "whats the date today?"},
                {"role": "assistant", "content": "stub"},
                {"role": "user", "content": "what is photosynthesis?"},
            ],
            ["what is photosynthesis?"],
        ),
    ],
)
def test_prompt_matrix_recent_user_turn_extraction(chat_history: list[dict], expected_recent: list[str]) -> None:
    recent = message_module._extract_recent_user_queries(chat_history, limit=3)

    assert recent == expected_recent


@pytest.mark.parametrize(
    ("prompt", "recent_user_queries", "expected_time_sensitive", "expected_search_query"),
    [
        pytest.param(
            "what about fortnite?",
            ["whats the latest version of minecraft?"],
            False,
            "what about fortnite",
            marks=pytest.mark.xfail(
                reason="fallback reconstruction always appends the latest user turn for elliptical follow-ups"
            ),
        ),
        (
            "what about the price there?",
            ["whats the current nvidia stock price?"],
            True,
            "what about the price there whats the current nvidia stock price",
        ),
        (
            "and in japan?",
            ["what is the weather in tokyo today?"],
            False,
            "and in japan what is the weather in tokyo today",
        ),
        (
            "what about the latest one?",
            ["what is the latest ios version?"],
            True,
            "what about the latest one what is the latest ios version",
        ),
    ],
)
def test_prompt_matrix_analysis_fallback_followup_reconstruction(
    prompt: str,
    recent_user_queries: list[str],
    expected_time_sensitive: bool,
    expected_search_query: str,
) -> None:
    decision = message_module._analysis_fallback(prompt, recent_user_queries)

    assert decision.time_sensitive is expected_time_sensitive
    assert decision.search_query == expected_search_query
