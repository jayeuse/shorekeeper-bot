import math
import re
from dataclasses import dataclass
from datetime import datetime, timezone

from memory.models import MemoryPair
from memory.repository import MemoryRepository


_WORD_RE = re.compile(r"[a-zA-Z0-9_]+")


@dataclass(frozen=True)
class MemoryRecord:
    id: int
    server_id: str
    channel_id: str
    user_id: str
    user_message: str
    assistant_message: str
    topics: tuple[str, ...]
    created_at: str
    score: float
    scope: str


class MemoryService:
    """Persistent conversational memory for user, channel, and server scopes."""

    TOPIC_KEYWORDS: dict[str, tuple[str, ...]] = {
        "lore": (
            "lore",
            "story",
            "history",
            "region",
            "faction",
            "event",
            "timeline",
            "legend",
        ),
        "character": (
            "character",
            "resonator",
            "shorekeeper",
            "jinhsi",
            "camellya",
            "phoebe",
            "iuno",
            "phrolova",
        ),
        "abilities": (
            "kit",
            "ability",
            "skill",
            "echo",
            "ultimate",
            "rotation",
            "build",
            "weapon",
            "damage",
        ),
        "meta": (
            "what do you know",
            "how many",
            "list",
            "which",
            "manifest",
            "stored",
        ),
        "casual": (
            "hello",
            "hey",
            "hi",
            "good morning",
            "good night",
            "how are you",
            "thank",
        ),
    }

    SCOPE_WEIGHTS: dict[str, float] = {
        "user": 1.0,
        "channel": 0.78,
        "server": 0.62,
    }

    def __init__(self, db_path: str, recency_half_life_days: float = 30.0) -> None:
        self.repository = MemoryRepository(db_path=db_path)
        self.recency_half_life_days = recency_half_life_days

    def store_exchange(
        self,
        server_id: str,
        channel_id: str,
        user_id: str,
        user_message: str,
        assistant_message: str,
    ) -> int:
        created_at = datetime.now(timezone.utc)
        topics = self.extract_topics(f"{user_message}\n{assistant_message}")
        topics_str = ",".join(topics)
        return self.repository.store_exchange(
            server_id=server_id,
            channel_id=channel_id,
            user_id=user_id,
            user_message=user_message,
            assistant_message=assistant_message,
            topics=topics_str,
            created_at=created_at,
        )

    def retrieve_relevant(
        self,
        query: str,
        server_id: str,
        channel_id: str,
        user_id: str,
        limit: int,
        relevance_threshold: float,
        candidate_pool: int,
    ) -> list[MemoryRecord]:
        records, _ = self.retrieve_relevant_with_metrics(
            query=query,
            server_id=server_id,
            channel_id=channel_id,
            user_id=user_id,
            limit=limit,
            relevance_threshold=relevance_threshold,
            candidate_pool=candidate_pool,
        )
        return records

    def retrieve_relevant_with_metrics(
        self,
        query: str,
        server_id: str,
        channel_id: str,
        user_id: str,
        limit: int,
        relevance_threshold: float,
        candidate_pool: int,
    ) -> tuple[list[MemoryRecord], int]:
        if limit <= 0:
            return [], 0

        candidates = self._load_candidates(
            server_id=server_id,
            channel_id=channel_id,
            user_id=user_id,
            candidate_pool=candidate_pool,
        )
        scanned_count = len(candidates)
        if scanned_count == 0:
            return [], 0

        query_tokens = self._tokenize(query)
        query_topics = self.extract_topics(query)
        scored: list[MemoryRecord] = []

        for row in candidates:
            scope = self._resolve_scope(row, server_id, channel_id, user_id)
            scope_weight = self.SCOPE_WEIGHTS.get(scope, 0.5)
            topic_score = self._topic_overlap(query_topics, row.topics)
            lexical_score = self._lexical_similarity(
                query_tokens,
                f"{row.user_message}\n{row.assistant_message}",
            )
            recency_score = self._recency_score(row.created_at)
            final_score = (
                (0.52 * lexical_score)
                + (0.18 * topic_score)
                + (0.14 * recency_score)
                + (0.16 * scope_weight)
            )

            if final_score < relevance_threshold:
                continue

            scored.append(
                MemoryRecord(
                    id=int(row.id or 0),
                    server_id=row.server_id,
                    channel_id=row.channel_id,
                    user_id=row.user_id,
                    user_message=row.user_message,
                    assistant_message=row.assistant_message,
                    topics=self._split_topics(row.topics),
                    created_at=row.created_at.isoformat(),
                    score=final_score,
                    scope=scope,
                )
            )

        scored.sort(key=lambda item: item.score, reverse=True)
        return scored[:limit], scanned_count

    def extract_topics(self, text: str) -> tuple[str, ...]:
        normalized = text.lower()
        found: list[str] = []
        for topic, keywords in self.TOPIC_KEYWORDS.items():
            if any(keyword in normalized for keyword in keywords):
                found.append(topic)

        if not found:
            return ("general",)

        # Preserve deterministic order while removing duplicates.
        unique = tuple(dict.fromkeys(found))
        return unique

    def _load_candidates(
        self,
        server_id: str,
        channel_id: str,
        user_id: str,
        candidate_pool: int,
    ) -> list[MemoryPair]:
        return self.repository.load_candidates(
            server_id=server_id,
            channel_id=channel_id,
            user_id=user_id,
            candidate_pool=candidate_pool,
        )

    def _resolve_scope(
        self,
        row: MemoryPair,
        server_id: str,
        channel_id: str,
        user_id: str,
    ) -> str:
        if row.server_id == server_id and row.channel_id == channel_id and row.user_id == user_id:
            return "user"
        if row.server_id == server_id and row.channel_id == channel_id:
            return "channel"
        return "server"

    def _lexical_similarity(self, query_tokens: set[str], candidate_text: str) -> float:
        if not query_tokens:
            return 0.0
        candidate_tokens = self._tokenize(candidate_text)
        if not candidate_tokens:
            return 0.0
        overlap = len(query_tokens.intersection(candidate_tokens))
        return overlap / len(query_tokens)

    def _topic_overlap(self, query_topics: tuple[str, ...], row_topics: str | None) -> float:
        if not query_topics:
            return 0.0
        row_topic_set = set(self._split_topics(row_topics))
        if not row_topic_set:
            return 0.0
        overlap = len(set(query_topics).intersection(row_topic_set))
        return overlap / len(query_topics)

    def _recency_score(self, created_at: datetime) -> float:
        created = created_at
        if created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)

        delta = datetime.now(timezone.utc) - created
        age_days = max(0.0, delta.total_seconds() / 86400.0)
        if self.recency_half_life_days <= 0:
            return 1.0

        decay = age_days / self.recency_half_life_days
        return math.exp(-math.log(2) * decay)

    def _tokenize(self, text: str) -> set[str]:
        return {token.lower() for token in _WORD_RE.findall(text) if len(token) > 1}

    def _split_topics(self, topics: str | None) -> tuple[str, ...]:
        if not topics:
            return ("general",)
        values = [part.strip() for part in topics.split(",") if part.strip()]
        if not values:
            return ("general",)
        return tuple(values)

    def get_stats(self, server_id: str) -> dict[str, int]:
        return self.repository.get_stats(server_id=server_id)