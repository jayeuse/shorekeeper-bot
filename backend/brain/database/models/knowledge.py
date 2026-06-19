from __future__ import annotations

from datetime import UTC, datetime
from typing import ClassVar

from sqlalchemy import Index, LargeBinary
from sqlmodel import Field, SQLModel


class KnowledgeVector(SQLModel, table=True):
    __tablename__: ClassVar[str] = "knowledge_vectors"
    __table_args__: ClassVar[tuple[Index, ...]] = (
        Index("idx_kv_source", "source"),
        Index("idx_kv_heading", "heading"),
    )

    id: int | None = Field(default=None, primary_key=True)
    chunk_id: str = Field(index=True, unique=True)
    source: str
    heading: str
    label: str
    text: str
    metadata_json: str = Field(default="{}")
    embedding_blob: bytes = Field(sa_type=LargeBinary)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
