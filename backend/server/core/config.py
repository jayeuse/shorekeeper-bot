from pathlib import Path

from dotenv import load_dotenv

_PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Load environment for MODE toggle and database URL
load_dotenv(str(_PROJECT_ROOT / ".env.local"), override=True)

import os  # noqa: E402

_MODE = os.environ.get("MODE", "local").strip().lower()

if _MODE == "online":
    _DATABASE_URL = os.environ.get("DATABASE_URL") or os.environ.get(
        "SUPABASE_DIRECT_CONNECTION_STRING"
    )
    if not _DATABASE_URL:
        raise RuntimeError("DATABASE_URL is required when MODE=online")
    SERVER_DB_PATH = _DATABASE_URL
    SERVER_DATABASE_URL = _DATABASE_URL
else:
    _SERVER_DB_PATH_DEFAULT = str(_PROJECT_ROOT / "database" / "server" / "server.db")
    SERVER_DB_PATH = _SERVER_DB_PATH_DEFAULT
    SERVER_DATABASE_URL = f"sqlite:///{Path(SERVER_DB_PATH).resolve()}"
