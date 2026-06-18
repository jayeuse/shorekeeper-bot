from __future__ import annotations

import ipaddress
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any, Protocol
from urllib.parse import urlparse

import httpx
from core.config import (
    SEARCH_BASE_URL,
    SEARCH_BLOCK_PRIVATE_IPS,
    SEARCH_DEMOTED_DOMAINS,
    SEARCH_PROVIDER,
    SEARCH_SAFE_DOMAINS,
    SEARCH_TIMEOUT_SECONDS,
    SEARCH_TOPIC_DOMAIN_OVERRIDES,
    SEARCH_TRUSTED_DOMAINS_NEWS,
    SEARCH_TRUSTED_DOMAINS_OFFICIAL,
    SEARCH_TRUSTED_DOMAINS_REFERENCE,
)

_WHITESPACE_RE = re.compile(r"\s+")
_MAX_SNIPPET_LENGTH = 320
_COMMUNITY_HOST_HINTS = (
    "fandom.com",
    "wiki.gg",
    "game8.co",
    "gamewith.net",
    "dotgg.gg",
    "reddit.com",
)
_MIRROR_HOST_HINTS = (
    "uptodown.com",
    "apkpure.com",
    "qoo-app.com",
    "softonic.com",
    "filehippo.com",
)
_DEMOTED_HOST_HINTS = (
    "youtube.com",
    "youtu.be",
    "tiktok.com",
    "instagram.com",
    "facebook.com",
    "x.com",
    "twitter.com",
    "play.google.com",
    "apps.apple.com",
)
_ARTICLE_FARM_HOST_HINTS = (
    "ldshop.gg",
    "driffle.com",
    "gamsgo.com",
    "lootbar.com",
)
_PREVIEW_HINTS = (
    "scheduled for release",
    "preview",
    "livestream",
    "coming soon",
    "upcoming",
    "pre-register",
    "preorder",
)
_STOPWORD_TOKENS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "that",
    "this",
    "your",
    "into",
    "version",
    "current",
    "latest",
    "banners",
    "banner",
    "price",
    "share",
    "update",
    "event",
    "patch",
    "guide",
    "history",
    "next",
    "past",
}


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
    source_class: str = "fallback"
    rank_score: float = 0.0
    rank_reason: str = ""
    entity_match_score: float = 0.0
    fact_match_score: float = 0.0
    specificity_score: float = 0.0
    evidence_quality: str = "low"
    supports_exact_answer: bool = False
    surface_class: str = "generic"
    freshness_bucket: str = "undated"
    stale_penalty_applied: bool = False
    preview_penalty_applied: bool = False
    agreement_participant: bool = False


@dataclass(slots=True)
class SearchBundle:
    query: str
    results: list[SearchResult]
    provider: str
    used_fallback_query: bool
    label: str = ""
    confidence_summary: str = "low"
    exact_claim_allowed: bool = False
    evidence_summary: str = ""
    agreement_status: str = "unknown"
    trusted_result_count: int = 0
    fallback_result_count: int = 0
    exact_claim_reason: str = ""
    response_mode: str = "uncertain"


def _slugify_tokens(text: str) -> list[str]:
    return [token for token in re.findall(r"[a-z0-9]+", text.lower()) if len(token) > 2]


def _meaningful_tokens(text: str) -> set[str]:
    return {token for token in _slugify_tokens(text) if token not in _STOPWORD_TOKENS}


class SearchProvider(Protocol):
    async def search(
        self,
        query: str,
        limit: int,
        *,
        topic: str = "",
        target_entity: str = "",
        requested_fact: str = "",
        question_type: str = "",
        freshness_required: bool = False,
        label: str = "",
    ) -> SearchBundle: ...


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


def _matches_domain_list(hostname: str, domains: list[str]) -> bool:
    if not domains:
        return False
    return _matches_allowed_domain(hostname, domains)


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


def _parse_published_at(value: str | None) -> datetime | None:
    if not value:
        return None
    text = value.strip()
    if not text:
        return None
    candidates = [text]
    if text.endswith("Z"):
        candidates.append(text[:-1] + "+00:00")
    if "T" in text:
        candidates.append(text.split("T", 1)[0])
    for candidate in candidates:
        try:
            parsed = datetime.fromisoformat(candidate)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=UTC)
            return parsed.astimezone(UTC)
        except ValueError:
            continue
    return None


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

    async def search(
        self,
        query: str,
        limit: int,
        *,
        topic: str = "",
        target_entity: str = "",
        requested_fact: str = "",
        question_type: str = "",
        freshness_required: bool = False,
        label: str = "",
    ) -> SearchBundle:
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

        results = self._parse_results(
            payload,
            limit=limit,
            topic=topic,
            target_entity=target_entity,
            requested_fact=requested_fact,
            question_type=question_type,
            freshness_required=freshness_required,
        )
        (
            confidence_summary,
            exact_claim_allowed,
            evidence_summary,
            agreement_status,
            trusted_result_count,
            fallback_result_count,
            exact_claim_reason,
            response_mode,
        ) = self._summarize_bundle_confidence(
            results,
            question_type=question_type,
            freshness_required=freshness_required,
        )

        return SearchBundle(
            query=query,
            results=results,
            provider="searxng",
            used_fallback_query=False,
            label=label,
            confidence_summary=confidence_summary,
            exact_claim_allowed=exact_claim_allowed,
            evidence_summary=evidence_summary,
            agreement_status=agreement_status,
            trusted_result_count=trusted_result_count,
            fallback_result_count=fallback_result_count,
            exact_claim_reason=exact_claim_reason,
            response_mode=response_mode,
        )

    def _classify_source(self, source: str, *, topic: str) -> tuple[str, float, str]:
        topic_config = (
            SEARCH_TOPIC_DOMAIN_OVERRIDES.get(topic.lower(), {})
            if isinstance(SEARCH_TOPIC_DOMAIN_OVERRIDES, dict)
            else {}
        )
        preferred = topic_config.get("preferred", []) if isinstance(topic_config, dict) else []
        blocked = topic_config.get("blocked", []) if isinstance(topic_config, dict) else []

        if _matches_domain_list(source, blocked):
            return ("blocked", -10.0, "topic-blocked")
        if _matches_domain_list(source, preferred):
            return ("topic_preferred", 5.0, "topic-preferred")
        if _matches_domain_list(source, SEARCH_TRUSTED_DOMAINS_OFFICIAL):
            return ("official", 4.0, "official")
        if _matches_domain_list(source, SEARCH_TRUSTED_DOMAINS_REFERENCE):
            return ("reference", 3.0, "reference")
        if _matches_domain_list(source, SEARCH_TRUSTED_DOMAINS_NEWS):
            return ("news", 2.0, "news")
        if _matches_domain_list(source, list(_MIRROR_HOST_HINTS)):
            return ("mirror", -1.5, "mirror-heuristic")
        if _matches_domain_list(source, SEARCH_DEMOTED_DOMAINS):
            return ("demoted", -2.0, "demoted-domain")
        if _matches_domain_list(source, list(_DEMOTED_HOST_HINTS)):
            return ("demoted", -2.0, "demoted-heuristic")
        if _matches_domain_list(source, list(_ARTICLE_FARM_HOST_HINTS)):
            return ("fallback", -0.75, "article-farm-heuristic")
        if _matches_domain_list(source, list(_COMMUNITY_HOST_HINTS)):
            return ("community", -0.5, "community-heuristic")
        return ("fallback", 0.0, "fallback")

    def _classify_surface(self, *, source: str, url: str, title: str, snippet: str) -> str:
        title_lower = title.lower()
        snippet_lower = snippet.lower()
        combined = f"{title_lower} {snippet_lower}"
        path = urlparse(url).path.lower()
        if source.endswith(("fandom.com", "wiki.gg", "wikipedia.org")):
            return "wiki_page"
        if source.endswith(("store.steampowered.com", "play.google.com", "apps.apple.com")):
            return "store_page"
        if source.endswith(_MIRROR_HOST_HINTS) or "apk" in title_lower or "download" in combined:
            return "download_page"
        if "patch notes" in combined or "version preview" in combined:
            return "patch_notes"
        if "news" in path or "notice" in path or "announcement" in combined:
            return "news_post"
        if any(term in combined for term in ("guide", "schedule", "history", "build", "tier list")):
            return "guide"
        if _matches_domain_list(source, list(_ARTICLE_FARM_HOST_HINTS)):
            return "article_farm"
        if (
            path.strip("/") in {"", "main", "en/main", "main/news"}
            or len([part for part in path.split("/") if part]) <= 1
        ):
            return "index_page"
        return "generic"

    def _freshness_bucket(self, published_dt: datetime | None) -> str:
        if published_dt is None:
            return "undated"
        age_days = (datetime.now(UTC) - published_dt).days
        if age_days <= 14:
            return "recent"
        if age_days <= 90:
            return "aging"
        return "stale"

    def _score_result(
        self,
        *,
        title: str,
        snippet: str,
        source: str,
        url: str,
        published_at: str | None,
        topic: str,
        target_entity: str,
        requested_fact: str,
        question_type: str,
        freshness_required: bool,
        provider_score: float | None,
    ) -> tuple[str, float, str, float, float, float, str, bool, str, str, bool, bool]:
        source_class, base_score, reason = self._classify_source(source, topic=topic)
        score = base_score
        combined = f"{title} {snippet}".lower()
        surface_class = self._classify_surface(source=source, url=url, title=title, snippet=snippet)
        if topic and topic.lower() in combined:
            score += 1.0
        entity_match_score = self._token_match_score(target_entity, combined)
        fact_match_score = self._token_match_score(requested_fact, combined)
        specificity_score = self._specificity_score(url, title, snippet)
        score += entity_match_score * 3.0
        score += fact_match_score * 2.5
        score += specificity_score * 1.5
        published_dt = _parse_published_at(published_at)
        freshness_bucket = self._freshness_bucket(published_dt)
        stale_penalty_applied = False
        preview_penalty_applied = False
        if published_at:
            score += 0.5
            if freshness_required:
                score += 0.5
        if freshness_required and published_dt is not None:
            age_days = (datetime.now(UTC) - published_dt).days
            if age_days > 180:
                score -= 2.5
                stale_penalty_applied = True
            elif age_days > 90:
                score -= 1.5
                stale_penalty_applied = True
            elif age_days > 30:
                score -= 0.5
                stale_penalty_applied = True
            elif age_days >= 0:
                score += 0.6
        if freshness_required and any(hint in combined for hint in _PREVIEW_HINTS):
            score -= 2.0
            preview_penalty_applied = True
        if surface_class in {"download_page", "store_page"}:
            score -= 1.25
        elif surface_class == "article_farm":
            score -= 1.0
        elif surface_class == "guide":
            score -= 0.6 if freshness_required else 0.1
        elif surface_class == "index_page":
            score -= 0.75 if freshness_required else 0.0
        elif surface_class in {"patch_notes", "news_post"} and source_class in {
            "official",
            "news",
            "reference",
            "topic_preferred",
        }:
            score += 1.0
        if provider_score is not None:
            score += min(provider_score, 3.0) * 0.1
        evidence_score = (
            entity_match_score * 0.45 + fact_match_score * 0.35 + specificity_score * 0.20
        )
        evidence_quality = (
            "high" if evidence_score >= 0.75 else "medium" if evidence_score >= 0.45 else "low"
        )
        supports_exact_answer = (
            evidence_quality == "high"
            and entity_match_score >= 0.7
            and fact_match_score >= 0.55
            and specificity_score >= 0.4
            and source_class in {"official", "reference", "news", "topic_preferred"}
            and surface_class
            not in {"download_page", "store_page", "guide", "article_farm", "index_page"}
            and freshness_bucket in {"recent", "aging"}
            and not any(hint in combined for hint in _PREVIEW_HINTS)
        )
        penalties: list[str] = []
        if stale_penalty_applied:
            penalties.append("stale_penalty")
        if preview_penalty_applied:
            penalties.append("preview_penalty")
        if source_class == "mirror":
            penalties.append("mirror_penalty")
        if surface_class == "article_farm":
            penalties.append("article_farm_penalty")
        penalty_text = f"; penalties={','.join(penalties)}" if penalties else ""
        rank_reason = (
            f"{reason}; entity={entity_match_score:.2f}; fact={fact_match_score:.2f}; specificity={specificity_score:.2f}; "
            f"type={question_type or 'generic'}; surface={surface_class}; freshness={freshness_bucket}{penalty_text}"
        )
        return (
            source_class,
            score,
            rank_reason,
            entity_match_score,
            fact_match_score,
            specificity_score,
            evidence_quality,
            supports_exact_answer,
            surface_class,
            freshness_bucket,
            stale_penalty_applied,
            preview_penalty_applied,
        )

    def _parse_results(
        self,
        payload: dict[str, Any],
        *,
        limit: int,
        topic: str = "",
        target_entity: str = "",
        requested_fact: str = "",
        question_type: str = "",
        freshness_required: bool = False,
    ) -> list[SearchResult]:
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
            published_at = (
                _normalize_text(str(item.get("publishedDate") or ""), max_length=64) or None
            )

            score_value = item.get("score")
            score: float | None = None
            if isinstance(score_value, int | float):
                score = float(score_value)

            (
                source_class,
                rank_score,
                rank_reason,
                entity_match_score,
                fact_match_score,
                specificity_score,
                evidence_quality,
                supports_exact_answer,
                surface_class,
                freshness_bucket,
                stale_penalty_applied,
                preview_penalty_applied,
            ) = self._score_result(
                title=title,
                snippet=snippet,
                source=source,
                url=url,
                published_at=published_at,
                topic=topic,
                target_entity=target_entity,
                requested_fact=requested_fact,
                question_type=question_type,
                freshness_required=freshness_required,
                provider_score=score,
            )
            if source_class == "blocked":
                continue

            parsed.append(
                SearchResult(
                    title=title,
                    url=url,
                    snippet=snippet,
                    source=source,
                    published_at=published_at,
                    score=score,
                    source_class=source_class,
                    rank_score=rank_score,
                    rank_reason=rank_reason,
                    entity_match_score=entity_match_score,
                    fact_match_score=fact_match_score,
                    specificity_score=specificity_score,
                    evidence_quality=evidence_quality,
                    supports_exact_answer=supports_exact_answer,
                    surface_class=surface_class,
                    freshness_bucket=freshness_bucket,
                    stale_penalty_applied=stale_penalty_applied,
                    preview_penalty_applied=preview_penalty_applied,
                )
            )
        parsed.sort(key=lambda result: result.rank_score, reverse=True)
        return self._filter_ranked_results(
            parsed,
            limit=limit,
            freshness_required=freshness_required,
            requested_fact=requested_fact,
        )

    def _filter_ranked_results(
        self,
        results: list[SearchResult],
        *,
        limit: int,
        freshness_required: bool,
        requested_fact: str,
    ) -> list[SearchResult]:
        if not results:
            return []

        if freshness_required or requested_fact:
            trusted = [
                result
                for result in results
                if result.source_class in {"official", "reference", "news", "topic_preferred"}
            ]
            if trusted:
                preserved = trusted[:limit]
                if len(preserved) < limit:
                    preserved.extend(
                        result
                        for result in results
                        if (
                            result.source_class == "fallback"
                            and result.surface_class
                            not in {"download_page", "store_page", "article_farm"}
                            and result not in preserved
                        )
                    )
                return preserved[:limit]

        non_demoted = [
            result for result in results if result.source_class not in {"demoted", "mirror"}
        ]
        return (non_demoted or results)[:limit]

    def _token_match_score(self, phrase: str, combined_text: str) -> float:
        tokens = [
            token for token in _WHITESPACE_RE.sub(" ", phrase.lower()).split() if len(token) > 2
        ]
        if not tokens:
            return 0.0
        matches = sum(1 for token in tokens if token in combined_text)
        return matches / len(tokens)

    def _specificity_score(self, url: str, title: str, snippet: str) -> float:
        parsed = urlparse(url)
        path = parsed.path.strip("/")
        generic_titles = {"google finance", "yahoo finance", "cnbc", "msn money", "stock market"}
        title_lower = title.lower()
        snippet_lower = snippet.lower()
        score = 0.0
        if path and len(path.split("/")) >= 2:
            score += 0.5
        if path and path not in {"", "finance", "news"}:
            score += 0.25
        if title_lower not in generic_titles:
            score += 0.15
        if len(snippet_lower) > 80:
            score += 0.10
        return min(score, 1.0)

    def _extract_claim_signature(self, result: SearchResult, *, question_type: str) -> str:
        combined = f"{result.title} {result.snippet}"
        if question_type == "latest_release":
            match = re.search(r"\b(?:version|v)\s*(\d+(?:\.\d+)+)\b", combined, re.IGNORECASE)
            if match:
                return f"version:{match.group(1)}"
        if question_type == "current_metric":
            match = re.search(r"\b(\d+(?:\.\d+)?)\b", combined)
            if match:
                return f"metric:{match.group(1)}"
        tokens = sorted(_meaningful_tokens(combined))
        return "tokens:" + ",".join(tokens[:8])

    def _agreement_status(
        self,
        results: list[SearchResult],
        *,
        question_type: str,
        freshness_required: bool,
    ) -> tuple[str, set[int], str]:
        trusted_candidates = [
            (index, result)
            for index, result in enumerate(results[:5])
            if result.source_class in {"official", "reference", "news", "topic_preferred"}
            and result.evidence_quality in {"high", "medium"}
            and result.freshness_bucket
            in {"recent", "aging", "undated" if not freshness_required else "recent"}
        ]
        if len(trusted_candidates) < 2:
            return ("insufficient_trusted", set(), "fewer than two trusted results")

        signatures: dict[str, list[int]] = {}
        for index, result in trusted_candidates:
            signature = self._extract_claim_signature(result, question_type=question_type)
            signatures.setdefault(signature, []).append(index)

        best_signature, best_indexes = max(signatures.items(), key=lambda item: len(item[1]))
        if len(best_indexes) >= 2:
            return ("agree", set(best_indexes), f"trusted agreement on {best_signature}")
        return ("disagree", set(), "trusted results disagree")

    def _summarize_bundle_confidence(
        self,
        results: list[SearchResult],
        *,
        question_type: str,
        freshness_required: bool,
    ) -> tuple[str, bool, str, str, int, int, str, str]:
        if not results:
            return ("low", False, "No usable evidence", "none", 0, 0, "no results", "uncertain")
        trusted_result_count = sum(
            1
            for result in results
            if result.source_class in {"official", "reference", "news", "topic_preferred"}
        )
        fallback_result_count = sum(1 for result in results if result.source_class == "fallback")
        agreement_status, participant_indexes, agreement_reason = self._agreement_status(
            results,
            question_type=question_type,
            freshness_required=freshness_required,
        )
        for index, result in enumerate(results):
            result.agreement_participant = index in participant_indexes
        top = results[0]
        exact_claim_allowed = (
            top.supports_exact_answer and trusted_result_count >= 2 and agreement_status == "agree"
        )
        if exact_claim_allowed:
            return (
                "high",
                True,
                "Trusted corroborated evidence supports an exact current answer",
                agreement_status,
                trusted_result_count,
                fallback_result_count,
                agreement_reason,
                "exact",
            )
        if agreement_status == "disagree":
            return (
                "low",
                False,
                "Current reports are mixed across trusted sources",
                agreement_status,
                trusted_result_count,
                fallback_result_count,
                agreement_reason,
                "summary",
            )
        if trusted_result_count >= 1 and any(
            result.evidence_quality in {"high", "medium"} for result in results[:3]
        ):
            return (
                "medium",
                False,
                "Trusted evidence is relevant but not corroborated enough for exact claims",
                agreement_status,
                trusted_result_count,
                fallback_result_count,
                agreement_reason,
                "summary",
            )
        if any(result.evidence_quality == "medium" for result in results[:3]):
            return (
                "low",
                False,
                "Only fallback or weak evidence is available",
                agreement_status,
                trusted_result_count,
                fallback_result_count,
                agreement_reason,
                "uncertain",
            )
        return (
            "low",
            False,
            "Evidence is generic or weak",
            agreement_status,
            trusted_result_count,
            fallback_result_count,
            agreement_reason,
            "uncertain",
        )


def build_search_provider() -> SearchProvider:
    if SEARCH_PROVIDER == "searxng":
        return SearxNGSearchProvider(
            base_url=SEARCH_BASE_URL,
            timeout_seconds=SEARCH_TIMEOUT_SECONDS,
            safe_domains=SEARCH_SAFE_DOMAINS,
            block_private_ips=SEARCH_BLOCK_PRIVATE_IPS,
        )
    raise SearchError(f"Unsupported search provider: {SEARCH_PROVIDER}")
