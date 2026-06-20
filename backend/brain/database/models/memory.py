from __future__ import annotations

from datetime import UTC, datetime
from typing import ClassVar

from sqlalchemy import Index
from sqlmodel import Field, SQLModel, Text


class UserMemory(SQLModel, table=True):
    __tablename__: ClassVar[str] = "user_memories"
    __table_args__: ClassVar[tuple[Index, ...]] = (
        Index("idx_user_memory_user", "user_id"),
        Index("idx_user_memory_server", "server_id"),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    server_id: str = Field(index=True)
    channel_id: str
    memory_content: str = Field(sa_type=Text)
    topic: str = Field(default="general")
    importance_score: float = Field(default=0.5)
    memory_version: int = Field(default=1)
    tags: str = Field(default="")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
