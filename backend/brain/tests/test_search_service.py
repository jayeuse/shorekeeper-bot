import asyncio
import sys
from pathlib import Path

import httpx
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services import search as search_module
from services.search import SearchError, SearxNGSearchProvider


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
                "title": "  Latest   Shorekeeper   Update ",
                "url": "https://www.example.com/news/shorekeeper",
                "content": " ".join(["tidal"] * 100),
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
            {
                "title": "Other domain",
                "url": "https://news.invalid/story",
                "content": "ignored",
            },
        ]
    }

    results = provider._parse_results(payload, limit=5)

    assert len(results) == 1
    assert results[0].title == "Latest Shorekeeper Update"
    assert results[0].source == "www.example.com"
    assert results[0].published_at == "2026-06-13"
    assert results[0].score == 1.5
    assert results[0].snippet.endswith("...")
    assert len(results[0].snippet) <= 320


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
        asyncio.run(provider.search("latest shorekeeper update", limit=3))


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
        asyncio.run(provider.search("latest shorekeeper update", limit=3))
