"""create knowledge vectors table

Revision ID: 20260619_0001
Revises: 20260405_0001
Create Date: 2026-06-19 00:00:00
"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "20260619_0001"
down_revision: str | None = "20260405_0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "knowledge_vectors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("chunk_id", sa.String(), nullable=False),
        sa.Column("source", sa.String(), nullable=False),
        sa.Column("heading", sa.String(), nullable=False),
        sa.Column("label", sa.String(), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("metadata_json", sa.Text(), nullable=False, server_default="{}"),
        sa.Column("embedding_blob", sa.LargeBinary(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index("idx_kv_chunk_id", "knowledge_vectors", ["chunk_id"], unique=True)
    op.create_index("idx_kv_source", "knowledge_vectors", ["source"], unique=False)
    op.create_index("idx_kv_heading", "knowledge_vectors", ["heading"], unique=False)


def downgrade() -> None:
    op.drop_index("idx_kv_heading", table_name="knowledge_vectors")
    op.drop_index("idx_kv_source", table_name="knowledge_vectors")
    op.drop_index("idx_kv_chunk_id", table_name="knowledge_vectors")
    op.drop_table("knowledge_vectors")
