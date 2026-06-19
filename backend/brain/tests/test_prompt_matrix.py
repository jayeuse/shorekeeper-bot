import asyncio
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from handlers import message as message_module


def _analysis(
    *,
    rag_query: str,
    can_answer_from_general_knowledge: bool = False,
    general_knowledge_confidence: float = 0.0,
    reason: str = "test-analysis",
) -> message_module.AnalysisDecision:
    return message_module.AnalysisDecision(
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
    async def _fake_analysis(
        user_content: str, history: list[dict]
    ) -> message_module.AnalysisDecision:
        assert user_content == prompt
        return decision

    monkeypatch.setattr(message_module, "_run_analysis_pass", _fake_analysis)
    return await message_module._build_route_plan(prompt, chat_history or [])


@pytest.mark.parametrize(
    ("prompt", "expected_plan"),
    [
        ("whats the date today?", ("datetime", "datetime")),
        ("what time is it right now?", ("datetime", "datetime")),
        ("what was the first question i asked?", ("memory", "memory")),
        ("do you remember what i told you earlier?", ("memory", "memory")),
        ("how are you today?", ("general", "casual")),
        ("good morning", ("general", "casual")),
        ("what factions are in your records?", ("general", "meta")),
        ("search: latest nvidia stock price", None),
    ],
)
def test_prompt_matrix_deterministic_routes(
    prompt: str, expected_plan: tuple[str, str] | None
) -> None:
    plan = message_module._build_deterministic_route_plan(prompt)

    if expected_plan is None:
        assert plan is None
        return

    assert plan is not None
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
        (
            "what does transmission mean?",
            _analysis(
                rag_query="what does transmission mean",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.9,
            ),
            "general",
            "definition",
            "general",
            "",
        ),
        (
            "whats your name?",
            _analysis(
                rag_query="what is your name",
                can_answer_from_general_knowledge=True,
                general_knowledge_confidence=0.95,
            ),
            "general",
            "identity",
            "identity",
            "",
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
    assert decision.can_answer_from_general_knowledge is False


def test_validate_analysis_decision_rejects_empty_rag_query() -> None:
    decision = message_module._validate_analysis_decision(
        {
            "rag_query": "   ",
            "can_answer_from_general_knowledge": True,
            "general_knowledge_confidence": 0.8,
            "reason": "invalid",
        }
    )

    assert decision is None
