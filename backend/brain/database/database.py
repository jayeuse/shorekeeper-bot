from pathlib import Path

from sqlmodel import create_engine


def memory_database_url(db_path: str) -> str:
    if db_path.startswith(("postgresql://", "postgres://", "sqlite:///")):
        return db_path
    absolute = Path(db_path).resolve()
    absolute.parent.mkdir(parents=True, exist_ok=True)
    return f"sqlite:///{absolute}"


def create_memory_engine(db_path: str):
    return create_engine(memory_database_url(db_path), echo=False)
