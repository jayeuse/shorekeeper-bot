"""create user_memories table

Revision ID: 20260620_0001
Revises: 20260619_0001
Create Date: 2026-06-20 00:00:00
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "20260620_0001"
down_revision: str | None = "20260619_0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "user_memories",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("server_id", sa.String(), nullable=False),
        sa.Column("channel_id", sa.String(), nullable=False),
        sa.Column("memory_content", sa.Text(), nullable=False),
        sa.Column("topic", sa.String(), nullable=False),
        sa.Column("importance_score", sa.Float(), nullable=False),
        sa.Column("memory_version", sa.Integer(), nullable=False),
        sa.Column("tags", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index("idx_user_memory_user", "user_memories", ["user_id"], unique=False)
    op.create_index("idx_user_memory_server", "user_memories", ["server_id"], unique=False)


def downgrade() -> None:
    op.drop_index("idx_user_memory_user", table_name="user_memories")
    op.drop_index("idx_user_memory_server", table_name="user_memories")
    op.drop_table("user_memories")
