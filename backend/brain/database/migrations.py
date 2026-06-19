from pathlib import Path

from alembic.config import Config
from database.database import memory_database_url

from alembic import command


def upgrade_memory_database(db_path: str) -> None:
    backend_root = Path(__file__).resolve().parents[2]
    ini_path = backend_root / "alembic.ini"

    config = Config(str(ini_path))
    config.set_main_option("script_location", str(backend_root / "alembic"))
    url = db_path if db_path.startswith("postgresql://") else memory_database_url(db_path)
    config.set_main_option("sqlalchemy.url", url)
    command.upgrade(config, "head")
