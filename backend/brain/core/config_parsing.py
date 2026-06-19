from collections.abc import Mapping
from typing import Any


def require_env(env: Mapping[str, str], name: str) -> str:
    value = env.get(name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    text = value.strip()
    if not text:
        raise RuntimeError(f"Environment variable must not be empty: {name}")
    return text


def require_bool_env(env: Mapping[str, str], name: str) -> bool:
    value = env.get(name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    lowered = value.strip().lower()
    if lowered in {"1", "true", "yes", "on"}:
        return True
    if lowered in {"0", "false", "no", "off"}:
        return False
    raise RuntimeError(f"Environment variable must be a boolean: {name}")


def coerce_str(value: Any, default: str) -> str:
    if value is None:
        return default
    text = str(value).strip()
    return text or default


def coerce_int(value: Any, default: int) -> int:
    if value is None:
        return default
    return int(value)


def coerce_float(value: Any, default: float) -> float:
    if value is None:
        return default
    return float(value)


def coerce_bool(value: Any, default: bool) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def coerce_str_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    raise RuntimeError(f"Expected a list-compatible value, got: {type(value).__name__}")


def coerce_mapping(value: Any, default: dict[str, Any] | None = None) -> dict[str, Any]:
    if value is None:
        return default or {}
    if isinstance(value, Mapping):
        return dict(value)
    raise RuntimeError(f"Expected a mapping value, got: {type(value).__name__}")


def require_nested(mapping: Mapping[str, Any], *keys: str) -> Any:
    current: Any = mapping
    traversed: list[str] = []
    for key in keys:
        traversed.append(key)
        if not isinstance(current, Mapping) or key not in current:
            joined = ".".join(traversed)
            raise RuntimeError(f"Missing required config key: {joined}")
        current = current[key]
    return current
