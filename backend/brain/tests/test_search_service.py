import asyncio
import sys
from pathlib import Path

import httpx
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services import search as search_module
from services.search import SearchError, SearchResult, SearxNGSearchProvider


def test_parse_results_normalizes_trims_and_filters() -> None:
    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
        safe_domains=["example.com"],
        block_private_ips=True,
    )
    payload = {
        "results": [
            {
                "title": "  Specific   Subject   Update ",
                "url": "https://www.example.com/news/subject/update",
                "content": " ".join(["detailed"] * 40),
                "publishedDate": " 2026-06-13 ",
                "score": 1.5,
            },
            {
                "title": "",
                "url": "https://www.example.com/ignored",
                "content": "ignored",
            },
            {
                "title": "Local result",
                "url": "http://127.0.0.1/internal",
                "content": "ignored",
            },
        ]
    }

    results = provider._parse_results(
        payload,
        limit=5,
        target_entity="Specific Subject",
        requested_fact="update",
        question_type="latest_release",
        freshness_required=True,
    )

    assert len(results) == 1
    assert results[0].title == "Specific Subject Update"
    assert results[0].published_at == "2026-06-13"
    assert results[0].evidence_quality in {"medium", "high"}


def test_parse_results_requires_results_list() -> None:
    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )

    with pytest.raises(SearchError, match="missing results list"):
        provider._parse_results({"unexpected": []}, limit=3)


def test_search_timeout_raises_controlled_error(monkeypatch) -> None:
    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )

    class _TimeoutClient:
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False

        async def get(self, *args, **kwargs):
            raise httpx.TimeoutException("timed out")

    monkeypatch.setattr(search_module.httpx, "AsyncClient", _TimeoutClient)

    with pytest.raises(SearchError, match="timed out"):
        asyncio.run(provider.search("subject fact", limit=3))


def test_search_invalid_payload_raises_controlled_error(monkeypatch) -> None:
    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )

    class _Response:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict:
            return {"unexpected": []}

    class _Client:
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False

        async def get(self, *args, **kwargs) -> _Response:
            return _Response()

    monkeypatch.setattr(search_module.httpx, "AsyncClient", _Client)

    with pytest.raises(SearchError, match="missing results list"):
        asyncio.run(provider.search("subject fact", limit=3))


def test_parse_results_prefers_specific_entity_fact_match_over_generic_portal(monkeypatch) -> None:
    monkeypatch.setattr(search_module, "SEARCH_TOPIC_DOMAIN_OVERRIDES", {})
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_OFFICIAL", ["finance.yahoo.com"])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_REFERENCE", ["example.com"])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_NEWS", ["reuters.com"])
    monkeypatch.setattr(search_module, "SEARCH_DEMOTED_DOMAINS", ["youtube.com"])

    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )
    payload = {
        "results": [
            {
                "title": "Yahoo Finance",
                "url": "https://finance.yahoo.com/",
                "content": "Stock quotes and financial news.",
                "publishedDate": "2026-06-14",
            },
            {
                "title": "NVIDIA stock price today",
                "url": "https://www.example.com/stocks/nvda-price",
                "content": "NVIDIA price per share today and related market data.",
                "publishedDate": "2026-06-14",
            },
        ]
    }

    results = provider._parse_results(
        payload,
        limit=5,
        topic="finance",
        target_entity="NVIDIA",
        requested_fact="price per share",
        question_type="current_metric",
        freshness_required=True,
    )

    assert results[0].title == "NVIDIA stock price today"
    assert results[0].entity_match_score >= results[1].entity_match_score
    assert results[0].specificity_score >= results[1].specificity_score


def test_parse_results_demotes_social_results_for_factual_queries(monkeypatch) -> None:
    monkeypatch.setattr(search_module, "SEARCH_TOPIC_DOMAIN_OVERRIDES", {})
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_OFFICIAL", [])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_REFERENCE", ["example.com"])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_NEWS", [])
    monkeypatch.setattr(search_module, "SEARCH_DEMOTED_DOMAINS", ["youtube.com"])

    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )
    payload = {
        "results": [
            {
                "title": "Specific report",
                "url": "https://example.com/report",
                "content": "Subject status update with precise details.",
                "publishedDate": "2026-06-14",
            },
            {
                "title": "Video clip",
                "url": "https://www.youtube.com/watch?v=123",
                "content": "Subject status update with precise details.",
                "publishedDate": "2026-06-14",
            },
        ]
    }

    results = provider._parse_results(
        payload,
        limit=5,
        target_entity="Subject",
        requested_fact="status update",
        question_type="event_status",
        freshness_required=True,
    )

    assert len(results) == 1
    assert results[0].source == "example.com"


def test_parse_results_classifies_fandom_as_community_and_filters_when_trusted_exists(
    monkeypatch,
) -> None:
    monkeypatch.setattr(search_module, "SEARCH_TOPIC_DOMAIN_OVERRIDES", {})
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_OFFICIAL", [])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_REFERENCE", ["wikipedia.org"])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_NEWS", [])
    monkeypatch.setattr(search_module, "SEARCH_DEMOTED_DOMAINS", [])

    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )
    payload = {
        "results": [
            {
                "title": "Subject Wiki | Fandom",
                "url": "https://subject.fandom.com/wiki/Subject",
                "content": "Community-maintained game wiki entry for Subject.",
                "publishedDate": "2026-06-14",
            },
            {
                "title": "Subject - Wikipedia",
                "url": "https://en.wikipedia.org/wiki/Subject",
                "content": "Reference article describing Subject.",
                "publishedDate": "2026-06-14",
            },
        ]
    }

    results = provider._parse_results(
        payload,
        limit=5,
        target_entity="Subject",
        requested_fact="latest version",
        question_type="latest_release",
        freshness_required=True,
    )

    assert len(results) == 1
    assert results[0].source == "en.wikipedia.org"
    assert results[0].source_class == "reference"


def test_parse_results_promotes_official_heuristic_domain(monkeypatch) -> None:
    monkeypatch.setattr(search_module, "SEARCH_TOPIC_DOMAIN_OVERRIDES", {})
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_OFFICIAL", ["investor.nvidia.com"])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_REFERENCE", [])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_NEWS", [])
    monkeypatch.setattr(search_module, "SEARCH_DEMOTED_DOMAINS", [])

    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )
    payload = {
        "results": [
            {
                "title": "NVIDIA Investor Relations",
                "url": "https://investor.nvidia.com/stock-info/default.aspx",
                "content": "Official stock information and filings.",
                "publishedDate": "2026-06-14",
            }
        ]
    }

    results = provider._parse_results(
        payload,
        limit=5,
        target_entity="NVIDIA",
        requested_fact="price per share",
        question_type="current_metric",
        freshness_required=True,
    )

    assert results[0].source_class == "official"
    assert "official" in results[0].rank_reason


def test_search_bundle_marks_exact_claims_only_for_strong_specific_results(monkeypatch) -> None:
    monkeypatch.setattr(search_module, "SEARCH_TOPIC_DOMAIN_OVERRIDES", {})
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_OFFICIAL", ["example.com"])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_REFERENCE", [])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_NEWS", [])
    monkeypatch.setattr(search_module, "SEARCH_DEMOTED_DOMAINS", [])

    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )

    class _Response:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict:
            return {
                "results": [
                    {
                        "title": "NVIDIA price per share today",
                        "url": "https://example.com/finance/nvda/price",
                        "content": "NVIDIA price per share today is 205.19 with specific market details.",
                        "publishedDate": "2026-06-14",
                    },
                    {
                        "title": "NVIDIA stock quote today",
                        "url": "https://example.com/finance/nvda/quote",
                        "content": "NVIDIA price per share today is 205.19 with specific market details.",
                        "publishedDate": "2026-06-14",
                    },
                ]
            }

    class _Client:
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False

        async def get(self, *args, **kwargs) -> _Response:
            return _Response()

    monkeypatch.setattr(search_module.httpx, "AsyncClient", _Client)

    bundle = asyncio.run(
        provider.search(
            "NVIDIA price per share today",
            limit=3,
            target_entity="NVIDIA",
            requested_fact="price per share",
            question_type="current_metric",
            freshness_required=True,
        )
    )

    assert bundle.confidence_summary == "high"
    assert bundle.exact_claim_allowed is True


def test_search_bundle_allows_close_current_metric_values(monkeypatch) -> None:
    monkeypatch.setattr(search_module, "SEARCH_TOPIC_DOMAIN_OVERRIDES", {})
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_OFFICIAL", [])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_REFERENCE", ["example.com"])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_NEWS", ["reuters.com"])
    monkeypatch.setattr(search_module, "SEARCH_DEMOTED_DOMAINS", [])

    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )

    class _Response:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict:
            return {
                "results": [
                    {
                        "title": "NVIDIA stock price today",
                        "url": "https://example.com/stocks/nvda-price",
                        "content": "NVIDIA price per share today is 205.19 with live market details.",
                        "publishedDate": "2026-06-14",
                    },
                    {
                        "title": "Reuters market quote for NVIDIA",
                        "url": "https://reuters.com/markets/us/nvda",
                        "content": "NVIDIA shares trade at 205.27 in current market coverage.",
                        "publishedDate": "2026-06-14",
                    },
                ]
            }

    class _Client:
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False

        async def get(self, *args, **kwargs) -> _Response:
            return _Response()

    monkeypatch.setattr(search_module.httpx, "AsyncClient", _Client)

    bundle = asyncio.run(
        provider.search(
            "NVIDIA price per share today",
            limit=3,
            target_entity="NVIDIA",
            requested_fact="price per share",
            question_type="current_metric",
            freshness_required=True,
        )
    )

    assert bundle.agreement_status == "agree"
    assert bundle.exact_claim_allowed is True


def test_current_metric_recent_trusted_result_returns_summary_mode() -> None:
    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )

    result = SearchResult(
        title="NVIDIA quote page",
        url="https://finance.yahoo.com/quote/NVDA",
        snippet="Live market page for NVIDIA stock.",
        source="finance.yahoo.com",
        published_at="2026-06-14",
        score=None,
        source_class="reference",
        rank_score=5.0,
        rank_reason="reference",
        entity_match_score=0.3,
        fact_match_score=0.2,
        specificity_score=0.3,
        evidence_quality="low",
        supports_exact_answer=False,
        surface_class="generic",
        freshness_bucket="recent",
    )

    summary = provider._summarize_bundle_confidence(
        [result],
        question_type="current_metric",
        freshness_required=True,
    )

    assert summary[0] == "low"
    assert summary[1] is False
    assert summary[7] == "summary"


def test_parse_results_classifies_download_portal_as_mirror_not_official(monkeypatch) -> None:
    monkeypatch.setattr(search_module, "SEARCH_TOPIC_DOMAIN_OVERRIDES", {})
    monkeypatch.setattr(
        search_module, "SEARCH_TRUSTED_DOMAINS_OFFICIAL", ["wutheringwaves.kurogames.com"]
    )
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_REFERENCE", [])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_NEWS", [])
    monkeypatch.setattr(search_module, "SEARCH_DEMOTED_DOMAINS", [])

    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )
    payload = {
        "results": [
            {
                "title": "Wuthering Waves for Android - Download the APK from Uptodown",
                "url": "https://wuthering-waves.en.uptodown.com/android",
                "content": "Get the latest version 3.4.1 Jun 13, 2026.",
                "publishedDate": "2026-06-13",
            }
        ]
    }

    results = provider._parse_results(
        payload,
        limit=5,
        target_entity="Wuthering Waves",
        requested_fact="latest version",
        question_type="latest_release",
        freshness_required=True,
    )

    assert results[0].source_class == "mirror"
    assert results[0].surface_class == "download_page"
    assert results[0].supports_exact_answer is False


def test_parse_results_penalizes_stale_freshness_results(monkeypatch) -> None:
    monkeypatch.setattr(search_module, "SEARCH_TOPIC_DOMAIN_OVERRIDES", {})
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_OFFICIAL", [])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_REFERENCE", ["example.com"])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_NEWS", [])
    monkeypatch.setattr(search_module, "SEARCH_DEMOTED_DOMAINS", [])

    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )
    payload = {
        "results": [
            {
                "title": "Current NVIDIA stock price",
                "url": "https://example.com/stocks/nvda-price-2025",
                "content": "NVIDIA price per share today and related market data.",
                "publishedDate": "2025-01-10",
            },
            {
                "title": "Current NVIDIA stock price",
                "url": "https://example.com/stocks/nvda-price-2026",
                "content": "NVIDIA price per share today and related market data.",
                "publishedDate": "2026-06-13",
            },
        ]
    }

    results = provider._parse_results(
        payload,
        limit=5,
        target_entity="NVIDIA",
        requested_fact="price per share",
        question_type="current_metric",
        freshness_required=True,
    )

    assert results[0].published_at == "2026-06-13"


def test_parse_results_penalizes_preview_style_results_for_current_fact(monkeypatch) -> None:
    monkeypatch.setattr(search_module, "SEARCH_TOPIC_DOMAIN_OVERRIDES", {})
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_OFFICIAL", [])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_REFERENCE", ["example.com"])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_NEWS", [])
    monkeypatch.setattr(search_module, "SEARCH_DEMOTED_DOMAINS", [])

    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )
    payload = {
        "results": [
            {
                "title": "Wuthering Waves Version Preview",
                "url": "https://example.com/wuwa/preview",
                "content": "Version Preview scheduled for release on November 20.",
                "publishedDate": "2026-06-13",
            },
            {
                "title": "Wuthering Waves current update summary",
                "url": "https://example.com/wuwa/current-update",
                "content": "Current version summary and update details.",
                "publishedDate": "2026-06-13",
            },
        ]
    }

    results = provider._parse_results(
        payload,
        limit=5,
        target_entity="Wuthering Waves",
        requested_fact="latest version",
        question_type="latest_release",
        freshness_required=True,
    )

    assert results[0].url.endswith("/current-update")


def test_search_bundle_requires_trusted_agreement_for_exact_claims(monkeypatch) -> None:
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_OFFICIAL", ["example.com"])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_REFERENCE", [])
    monkeypatch.setattr(search_module, "SEARCH_TRUSTED_DOMAINS_NEWS", [])
    monkeypatch.setattr(search_module, "SEARCH_TOPIC_DOMAIN_OVERRIDES", {})
    monkeypatch.setattr(search_module, "SEARCH_DEMOTED_DOMAINS", [])

    provider = SearxNGSearchProvider(
        base_url="http://127.0.0.1:8083",
        timeout_seconds=8,
    )

    class _Response:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict:
            return {
                "results": [
                    {
                        "title": "Wuthering Waves Version 3.4",
                        "url": "https://example.com/news/patch-3-4",
                        "content": "Version 3.4 patch notes and release details.",
                        "publishedDate": "2026-06-13",
                    },
                    {
                        "title": "Wuthering Waves Version 3.3",
                        "url": "https://example.com/news/patch-3-3",
                        "content": "Version 3.3 patch notes and release details.",
                        "publishedDate": "2026-06-13",
                    },
                ]
            }

    class _Client:
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False

        async def get(self, *args, **kwargs) -> _Response:
            return _Response()

    monkeypatch.setattr(search_module.httpx, "AsyncClient", _Client)

    bundle = asyncio.run(
        provider.search(
            "latest version of Wuthering Waves",
            limit=5,
            target_entity="Wuthering Waves",
            requested_fact="latest version",
            question_type="latest_release",
            freshness_required=True,
        )
    )

    assert bundle.exact_claim_allowed is False
    assert bundle.agreement_status == "disagree"
    assert bundle.response_mode == "summary"
