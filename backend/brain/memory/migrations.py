from pathlib import Path

from alembic import command
from alembic.config import Config

from memory.database import memory_database_url


def upgrade_memory_database(db_path: str) -> None:
    backend_root = Path(__file__).resolve().parents[2]
    ini_path = backend_root / "alembic-memory.ini"

    config = Config(str(ini_path))
    config.set_main_option("script_location", str(backend_root / "alembic" / "memory"))
    config.set_main_option("sqlalchemy.url", memory_database_url(db_path))
    command.upgrade(config, "head")
