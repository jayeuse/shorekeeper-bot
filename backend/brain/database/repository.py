from datetime import UTC, datetime

from database.database import create_memory_engine
from database.migrations import upgrade_memory_database
from database.models import MemoryPair
from sqlalchemy import func
from sqlmodel import Session, col, select


class MemoryRepository:
    def __init__(self, db_path: str) -> None:
        upgrade_memory_database(db_path)
        self.engine = create_memory_engine(db_path)

    def close(self) -> None:
        self.engine.dispose()

    def store_exchange(
        self,
        server_id: str,
        channel_id: str,
        user_id: str,
        user_message: str,
        assistant_message: str,
        topics: str,
        created_at: datetime | None = None,
    ) -> int:
        timestamp = created_at or datetime.now(UTC)
        with Session(self.engine) as session:
            pair = MemoryPair(
                server_id=server_id,
                channel_id=channel_id,
                user_id=user_id,
                user_message=user_message,
                assistant_message=assistant_message,
                topics=topics,
                created_at=timestamp,
            )
            session.add(pair)
            session.commit()
            session.refresh(pair)

        if pair.id is None:
            raise RuntimeError("Failed to store memory exchange: missing row id")

        return int(pair.id)

    def load_candidates(
        self,
        server_id: str,
        channel_id: str,
        user_id: str,
        candidate_pool: int,
    ) -> list[MemoryPair]:
        scoped_limit = max(8, candidate_pool // 3)
        seen: set[int] = set()
        rows: list[MemoryPair] = []

        with Session(self.engine) as session:
            scopes = (
                (
                    select(MemoryPair)
                    .where(MemoryPair.server_id == server_id)
                    .where(MemoryPair.channel_id == channel_id)
                    .where(MemoryPair.user_id == user_id)
                    .order_by(col(MemoryPair.created_at).desc())
                    .limit(scoped_limit)
                ),
                (
                    select(MemoryPair)
                    .where(MemoryPair.server_id == server_id)
                    .where(MemoryPair.channel_id == channel_id)
                    .order_by(col(MemoryPair.created_at).desc())
                    .limit(scoped_limit)
                ),
                (
                    select(MemoryPair)
                    .where(MemoryPair.server_id == server_id)
                    .order_by(col(MemoryPair.created_at).desc())
                    .limit(scoped_limit)
                ),
            )

            for statement in scopes:
                result = session.exec(statement).all()
                for row in result:
                    if row.id is None:
                        continue
                    row_id = int(row.id)
                    if row_id in seen:
                        continue
                    seen.add(row_id)
                    rows.append(row)

        return rows

    def get_stats(self, server_id: str) -> dict[str, int]:
        with Session(self.engine) as session:
            total = session.exec(
                select(func.count())
                .select_from(MemoryPair)
                .where(MemoryPair.server_id == server_id)
            ).one()
            users = session.exec(
                select(func.count(func.distinct(MemoryPair.user_id))).where(
                    MemoryPair.server_id == server_id
                )
            ).one()
            channels = session.exec(
                select(func.count(func.distinct(MemoryPair.channel_id))).where(
                    MemoryPair.server_id == server_id
                )
            ).one()

        return {
            "total_pairs": int(total),
            "unique_users": int(users),
            "unique_channels": int(channels),
        }
