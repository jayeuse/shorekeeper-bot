from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[3]
_SERVER_DB_PATH_DEFAULT = str(_PROJECT_ROOT / "database" / "server" / "server.db")


SERVER_DB_PATH = _SERVER_DB_PATH_DEFAULT
SERVER_DATABASE_URL = f"sqlite:///{Path(SERVER_DB_PATH).resolve()}"
