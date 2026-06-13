from __future__ import annotations

import ipaddress
import re
from dataclasses import dataclass
from typing import Any, Protocol
from urllib.parse import urlparse

import httpx
from core.config import (
    SEARCH_BASE_URL,
    SEARCH_BLOCK_PRIVATE_IPS,
    SEARCH_PROVIDER,
    SEARCH_SAFE_DOMAINS,
    SEARCH_TIMEOUT_SECONDS,
)

_WHITESPACE_RE = re.compile(r"\s+")
_MAX_SNIPPET_LENGTH = 320


class SearchError(RuntimeError):
    pass


@dataclass(slots=True)
class SearchResult:
    title: str
    url: str
    snippet: str
    source: str
    published_at: str | None
    score: float | None


@dataclass(slots=True)
class SearchBundle:
    query: str
    results: list[SearchResult]
    provider: str
    used_fallback_query: bool


class SearchProvider(Protocol):
    async def search(self, query: str, limit: int) -> SearchBundle: ...


def _normalize_text(text: str, *, max_length: int | None = None) -> str:
    normalized = _WHITESPACE_RE.sub(" ", text).strip()
    if max_length is None or len(normalized) <= max_length:
        return normalized
    return f"{normalized[: max_length - 3].rstrip()}..."


def _matches_allowed_domain(hostname: str, safe_domains: list[str]) -> bool:
    if not safe_domains:
        return True

    host = hostname.lower().rstrip(".")
    for domain in safe_domains:
        candidate = domain.lower().strip().rstrip(".")
        if host == candidate or host.endswith(f".{candidate}"):
            return True
    return False


def _is_private_host(hostname: str) -> bool:
    host = hostname.lower().rstrip(".")
    if host in {"localhost", "localhost.localdomain"}:
        return True

    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return False

    return (
        ip.is_private
        or ip.is_loopback
        or ip.is_link_local
        or ip.is_reserved
        or ip.is_multicast
        or ip.is_unspecified
    )


def _extract_source(url: str) -> str:
    hostname = urlparse(url).hostname or ""
    return hostname.lower().rstrip(".")


class SearxNGSearchProvider:
    def __init__(
        self,
        *,
        base_url: str,
        timeout_seconds: float,
        safe_domains: list[str] | None = None,
        block_private_ips: bool = True,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.safe_domains = safe_domains or []
        self.block_private_ips = block_private_ips

    async def search(self, query: str, limit: int) -> SearchBundle:
        params = {
            "q": query,
            "format": "json",
            "language": "en",
        }

        try:
            async with httpx.AsyncClient(timeout=self.timeout_seconds) as client:
                response = await client.get(f"{self.base_url}/search", params=params)
                response.raise_for_status()
                payload = response.json()
        except httpx.TimeoutException as exc:
            raise SearchError(f"SearxNG request timed out after {self.timeout_seconds}s") from exc
        except httpx.HTTPError as exc:
            raise SearchError(f"SearxNG request failed: {exc}") from exc
        except ValueError as exc:
            raise SearchError("SearxNG returned invalid JSON") from exc

        return SearchBundle(
            query=query,
            results=self._parse_results(payload, limit=limit),
            provider="searxng",
            used_fallback_query=False,
        )

    def _parse_results(self, payload: dict[str, Any], *, limit: int) -> list[SearchResult]:
        raw_results = payload.get("results")
        if not isinstance(raw_results, list):
            raise SearchError("SearxNG payload missing results list")

        parsed: list[SearchResult] = []
        for item in raw_results:
            if not isinstance(item, dict):
                continue

            title = _normalize_text(str(item.get("title", "")))
            url = str(item.get("url", "")).strip()
            if not title or not url:
                continue

            source = _extract_source(url)
            if not source:
                continue
            if self.block_private_ips and _is_private_host(source):
                continue
            if not _matches_allowed_domain(source, self.safe_domains):
                continue

            snippet = _normalize_text(
                str(item.get("content") or item.get("snippet") or ""),
                max_length=_MAX_SNIPPET_LENGTH,
            )
            published_at = _normalize_text(str(item.get("publishedDate") or ""), max_length=64) or None

            score_value = item.get("score")
            score: float | None = None
            if isinstance(score_value, int | float):
                score = float(score_value)

            parsed.append(
                SearchResult(
                    title=title,
                    url=url,
                    snippet=snippet,
                    source=source,
                    published_at=published_at,
                    score=score,
                )
            )
            if len(parsed) >= limit:
                break

        return parsed


def build_search_provider() -> SearchProvider:
    if SEARCH_PROVIDER == "searxng":
        return SearxNGSearchProvider(
            base_url=SEARCH_BASE_URL,
            timeout_seconds=SEARCH_TIMEOUT_SECONDS,
            safe_domains=SEARCH_SAFE_DOMAINS,
            block_private_ips=SEARCH_BLOCK_PRIVATE_IPS,
        )
    raise SearchError(f"Unsupported search provider: {SEARCH_PROVIDER}")
