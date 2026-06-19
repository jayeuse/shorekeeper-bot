"""create memory pairs table

Revision ID: 20260405_0001
Revises:
Create Date: 2026-04-05 00:00:00
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "20260405_0001"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "memory_pairs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("server_id", sa.String(), nullable=False),
        sa.Column("channel_id", sa.String(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("user_message", sa.Text(), nullable=False),
        sa.Column("assistant_message", sa.Text(), nullable=False),
        sa.Column("topics", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "idx_memory_server_time",
        "memory_pairs",
        ["server_id", "created_at"],
        unique=False,
    )
    op.create_index(
        "idx_memory_channel_time",
        "memory_pairs",
        ["channel_id", "created_at"],
        unique=False,
    )
    op.create_index("idx_memory_user_time", "memory_pairs", ["user_id", "created_at"], unique=False)
    op.create_index("idx_memory_topics", "memory_pairs", ["topics"], unique=False)


def downgrade() -> None:
    op.drop_index("idx_memory_topics", table_name="memory_pairs")
    op.drop_index("idx_memory_user_time", table_name="memory_pairs")
    op.drop_index("idx_memory_channel_time", table_name="memory_pairs")
    op.drop_index("idx_memory_server_time", table_name="memory_pairs")
    op.drop_table("memory_pairs")
