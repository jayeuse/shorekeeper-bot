import asyncio
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from handlers import message as message_module


def _analysis(
    *,
    rag_query: str,
    reason: str = "test-analysis",
    query_type: str = "general",
) -> message_module.AnalysisDecision:
    return message_module.AnalysisDecision(
        rag_query=rag_query,
        reason=reason,
        query_type=query_type,
        raw_payload={"source": "test"},
    )


async def _build_route_with_analysis(
    monkeypatch: pytest.MonkeyPatch,
    prompt: str,
    decision: message_module.AnalysisDecision,
    chat_history: list[dict] | None = None,
) -> message_module.RoutePlan:
    async def _fake_analysis(
        user_content: str, chat_history: list[dict], *, user_context_str: str = ""
    ) -> message_module.AnalysisDecision:
        assert user_content == prompt
        return decision

    monkeypatch.setattr(message_module, "_run_analysis_pass", _fake_analysis)
    return await message_module._build_route_plan(prompt, chat_history or [])


@pytest.mark.parametrize(
    ("prompt", "analysis_query_type", "expected_plan"),
    [
        ("whats the date today?", "datetime", ("datetime", "datetime")),
        ("what time is it right now?", "datetime", ("datetime", "datetime")),
        ("what was the first question i asked?", "memory", ("memory", "memory")),
        ("do you remember what i told you earlier?", "memory", ("memory", "memory")),
        ("how are you today?", "casual", ("general", "casual")),
        ("good morning", "casual", ("general", "casual")),
        ("what factions are in your records?", "meta", ("general", "meta")),
    ],
)
def test_prompt_matrix_analysis_routes(
    monkeypatch: pytest.MonkeyPatch,
    prompt: str,
    analysis_query_type: str,
    expected_plan: tuple[str, str],
) -> None:
    decision = _analysis(
        rag_query=prompt,
        query_type=analysis_query_type,
    )

    async def _fake_analysis(
        user_content: str, chat_history: list[dict], *, user_context_str: str = ""
    ) -> message_module.AnalysisDecision:
        assert user_content == prompt
        return decision

    monkeypatch.setattr(message_module, "_run_analysis_pass", _fake_analysis)
    plan = asyncio.run(message_module._build_route_plan(prompt, []))

    assert plan.path == expected_plan[0]
    assert plan.deterministic_gate == expected_plan[1]


@pytest.mark.parametrize(
    ("prompt", "decision", "expected_path", "expected_type", "expected_domain", "expected_entity"),
    [
        (
            "tell me about black shores",
            _analysis(rag_query="tell me about black shores"),
            "rag",
            "background_fact",
            "general",
            "",
        ),
        (
            "who is shorekeeper?",
            _analysis(rag_query="who is Shorekeeper"),
            "rag",
            "background_fact",
            "general",
            "Shorekeeper",
        ),
    ],
)
def test_prompt_matrix_analysis_route_plan(
    monkeypatch: pytest.MonkeyPatch,
    prompt: str,
    decision: message_module.AnalysisDecision,
    expected_path: str,
    expected_type: str,
    expected_domain: str,
    expected_entity: str,
) -> None:
    plan = asyncio.run(_build_route_with_analysis(monkeypatch, prompt, decision))

    assert plan.path == expected_path
    assert plan.analysis_used is True
    assert plan.query_text == decision.rag_query
    assert plan.question_type_hint == expected_type
    assert plan.subject_domain == expected_domain
    assert plan.target_entity == expected_entity


def test_analysis_fallback_resolves_elliptical_followup() -> None:
    decision = message_module._analysis_fallback(
        "what about there?",
        ["tell me about black shores"],
    )

    assert decision.rag_query == "what about there tell me about black shores"


def test_validate_analysis_decision_rejects_empty_rag_query() -> None:
    decision = message_module._validate_analysis_decision(
        {
            "rag_query": "   ",
            "reason": "invalid",
        }
    )

    assert decision is None
