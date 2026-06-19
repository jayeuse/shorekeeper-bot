from pathlib import Path
from typing import Any

import yaml


def find_project_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__)).resolve()
    for candidate in [current.parent, *current.parents]:
        if (candidate / ".env.example").exists():
            return candidate
    raise RuntimeError("Could not locate project root")


def resolve_project_path(project_root: Path, raw_path: str) -> Path:
    candidate = Path(raw_path).expanduser()
    if candidate.is_absolute():
        return candidate
    return project_root / candidate


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise RuntimeError(f"Missing config file: {path}")

    with path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle) or {}

    if not isinstance(loaded, dict):
        raise RuntimeError(f"Config file must contain a YAML mapping: {path}")

    return loaded
