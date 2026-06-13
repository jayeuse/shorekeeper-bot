"""server baseline

Revision ID: 20260405_0001_server
Revises:
Create Date: 2026-04-05 00:00:00
"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "20260405_0001_server"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
