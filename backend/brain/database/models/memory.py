from __future__ import annotations

from datetime import UTC, datetime
from typing import ClassVar

from sqlalchemy import Index
from sqlmodel import Field, SQLModel


class MemoryPair(SQLModel, table=True):
    __tablename__: ClassVar[str] = "memory_pairs"
    __table_args__: ClassVar[tuple[Index, ...]] = (
        Index("idx_memory_server_time", "server_id", "created_at"),
        Index("idx_memory_channel_time", "channel_id", "created_at"),
        Index("idx_memory_user_time", "user_id", "created_at"),
        Index("idx_memory_topics", "topics"),
    )

    id: int | None = Field(default=None, primary_key=True)
    server_id: str = Field(index=True)
    channel_id: str = Field(index=True)
    user_id: str = Field(index=True)
    user_message: str
    assistant_message: str
    topics: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC), index=True)
