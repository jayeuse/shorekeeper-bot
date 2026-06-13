from pathlib import Path

from alembic.config import Config

from alembic import command
from server.core.config import SERVER_DATABASE_URL


def upgrade_server_database(database_url: str | None = None) -> None:
    backend_root = Path(__file__).resolve().parents[2]
    ini_path = backend_root / "alembic-server.ini"

    config = Config(str(ini_path))
    config.set_main_option("script_location", str(backend_root / "alembic" / "server"))
    config.set_main_option("sqlalchemy.url", database_url or SERVER_DATABASE_URL)
    command.upgrade(config, "head")
