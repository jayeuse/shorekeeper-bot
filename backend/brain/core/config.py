import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from core.config_files import find_project_root, load_yaml_mapping, resolve_project_path
from dotenv import load_dotenv

# Load .env.local from project root
_PROJECT_ROOT = find_project_root(Path(__file__))

load_dotenv(str(_PROJECT_ROOT / ".env.local"), override=True)


def _require_env(env: Mapping[str, str], name: str) -> str:
    value = env.get(name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    text = value.strip()
    if not text:
        raise RuntimeError(f"Environment variable must not be empty: {name}")
    return text


def _require_bool_env(env: Mapping[str, str], name: str) -> bool:
    value = env.get(name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    lowered = value.strip().lower()
    if lowered in {"1", "true", "yes", "on"}:
        return True
    if lowered in {"0", "false", "no", "off"}:
        return False
    raise RuntimeError(f"Environment variable must be a boolean: {name}")


def _coerce_str(value: Any, default: str) -> str:
    if value is None:
        return default
    text = str(value).strip()
    return text or default


def _coerce_int(value: Any, default: int) -> int:
    if value is None:
        return default
    return int(value)


def _coerce_float(value: Any, default: float) -> float:
    if value is None:
        return default
    return float(value)


def _coerce_bool(value: Any, default: bool) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def _coerce_str_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    raise RuntimeError(f"Expected a list-compatible value, got: {type(value).__name__}")


def _coerce_mapping(value: Any, default: dict[str, Any] | None = None) -> dict[str, Any]:
    if value is None:
        return default or {}
    if isinstance(value, Mapping):
        return dict(value)
    raise RuntimeError(f"Expected a mapping value, got: {type(value).__name__}")


def _require_nested(mapping: Mapping[str, Any], *keys: str) -> Any:
    current: Any = mapping
    traversed: list[str] = []
    for key in keys:
        traversed.append(key)
        if not isinstance(current, Mapping) or key not in current:
            joined = ".".join(traversed)
            raise RuntimeError(f"Missing required config key: {joined}")
        current = current[key]
    return current


def build_runtime_values(
    env: Mapping[str, str] | None = None, project_root: Path | None = None
) -> dict[str, Any]:
    active_env = dict(os.environ if env is None else env)
    active_project_root = project_root or _PROJECT_ROOT

    search_config_path = str(resolve_project_path(active_project_root, "config/search.config.yml"))
    runtime_config_path = str(
        resolve_project_path(active_project_root, "config/runtime.config.yml")
    )

    search_config = load_yaml_mapping(Path(search_config_path))
    runtime_config = load_yaml_mapping(Path(runtime_config_path))

    local_base_url = _coerce_str(
        _require_nested(runtime_config, "llama", "local", "base_url"),
        "",
    )
    embed_base_url = _coerce_str(
        _require_nested(runtime_config, "llama", "embed", "base_url"),
        "",
    )
    local_model = _coerce_str(
        _require_nested(runtime_config, "llama", "local", "model"),
        "",
    )
    embed_model = _coerce_str(
        _require_nested(runtime_config, "llama", "embed", "model"),
        "",
    )

    llm_provider = (
        _coerce_str(_require_nested(runtime_config, "providers", "llm_provider"), "")
    ).lower()
    embedding_provider = (
        _coerce_str(_require_nested(runtime_config, "providers", "embedding_provider"), "")
    ).lower()

    online_model = _coerce_str(
        _require_nested(runtime_config, "providers", "online_model"),
        "",
    )
    online_base_url = _coerce_str(
        _require_nested(runtime_config, "providers", "online_base_url"),
        "",
    )

    search_provider = _coerce_str(_require_nested(search_config, "provider"), "").strip().lower()
    search_base_url = _coerce_str(_require_nested(search_config, "base_url"), "").strip()

    search_topic_domain_overrides = _coerce_mapping(
        _require_nested(search_config, "topic_domain_overrides")
    )

    chat_flash_attn = _coerce_bool(
        _require_nested(runtime_config, "llama", "launcher", "chat", "flash_attn"),
        False,
    )
    chat_jinja = _coerce_bool(
        _require_nested(runtime_config, "llama", "launcher", "chat", "jinja"),
        False,
    )
    chat_no_mmap = _coerce_bool(
        _require_nested(runtime_config, "llama", "launcher", "chat", "no_mmap"),
        False,
    )
    embed_no_mmap = _coerce_bool(
        _require_nested(runtime_config, "llama", "launcher", "embed", "no_mmap"),
        False,
    )
    llama_metrics = _coerce_bool(
        _require_nested(runtime_config, "llama", "launcher", "metrics"),
        False,
    )

    values: dict[str, Any] = {
        "PROJECT_ROOT": active_project_root,
        "DISCORD_TOKEN": _require_env(active_env, "DISCORD_TOKEN"),
        "ONLINE_API_KEY": active_env.get("ONLINE_API_KEY") or active_env.get("DEEPSEEK_API_KEY"),
        "ONLINE_BASE_URL": online_base_url,
        "LOCAL_API_KEY": _require_env(active_env, "LOCAL_API_KEY"),
        "LOCAL_BASE_URL": local_base_url,
        "EMBED_BASE_URL": embed_base_url,
        "EMBED_API_KEY": _require_env(active_env, "EMBED_API_KEY"),
        "LLM_PROVIDER": llm_provider,
        "EMBEDDING_PROVIDER": embedding_provider,
        "ONLINE_MODEL": online_model,
        "LOCAL_MODEL": local_model,
        "EMBED_MODEL": embed_model,
        "LOCAL_CONTEXT_WINDOW": _coerce_int(
            _require_nested(runtime_config, "llama", "local", "context_window"),
            0,
        ),
        "LOCAL_KV_CACHE_KEEP": _coerce_int(
            _require_nested(runtime_config, "llama", "local", "kv_cache_keep"),
            0,
        ),
        "MEMORY_ENABLED": _require_bool_env(active_env, "MEMORY_ENABLED"),
        "MEMORY_RECALL_LIMIT": _coerce_int(
            _require_nested(runtime_config, "memory", "recall_limit"), 0
        ),
        "MEMORY_RELEVANCE_THRESHOLD": _coerce_float(
            _require_nested(runtime_config, "memory", "relevance_threshold"), 0.0
        ),
        "MEMORY_CANDIDATE_POOL": _coerce_int(
            _require_nested(runtime_config, "memory", "candidate_pool"), 0
        ),
        "MEMORY_RECENCY_HALFLIFE_DAYS": _coerce_float(
            _require_nested(runtime_config, "memory", "recency_halflife_days"), 0.0
        ),
        "SEARCH_ENABLED": _require_bool_env(active_env, "SEARCH_ENABLED"),
        "SEARCH_PROVIDER": search_provider,
        "SEARCH_BASE_URL": search_base_url,
        "SEARCH_TIMEOUT_SECONDS": _coerce_float(
            _require_nested(search_config, "timeout_seconds"), 0.0
        ),
        "SEARCH_MAX_RESULTS": _coerce_int(_require_nested(search_config, "max_results"), 0),
        "SEARCH_MIN_QUERY_LENGTH": _coerce_int(
            _require_nested(search_config, "min_query_length"), 0
        ),
        "SEARCH_SAFE_DOMAINS": _coerce_str_list(_require_nested(search_config, "safe_domains")),
        "SEARCH_BLOCK_PRIVATE_IPS": _coerce_bool(
            _require_nested(search_config, "block_private_ips"), False
        ),
        "SEARCH_TRUSTED_DOMAINS_OFFICIAL": _coerce_str_list(
            _require_nested(search_config, "trusted_domains", "official")
        ),
        "SEARCH_TRUSTED_DOMAINS_REFERENCE": _coerce_str_list(
            _require_nested(search_config, "trusted_domains", "reference")
        ),
        "SEARCH_TRUSTED_DOMAINS_NEWS": _coerce_str_list(
            _require_nested(search_config, "trusted_domains", "news")
        ),
        "SEARCH_DEMOTED_DOMAINS": _coerce_str_list(
            _require_nested(search_config, "demoted_domains")
        ),
        "SEARCH_TOPIC_DOMAIN_OVERRIDES": search_topic_domain_overrides,
        "ANALYSIS_ENABLED": _coerce_bool(
            _require_nested(runtime_config, "analysis", "enabled"), False
        ),
        "ANALYSIS_TIMEOUT_SECONDS": _coerce_float(
            _require_nested(runtime_config, "analysis", "timeout_seconds"), 0.0
        ),
        "RAG_ANSWER_SCORE_THRESHOLD": _coerce_float(
            _require_nested(runtime_config, "analysis", "rag_answer_score_threshold"),
            0.0,
        ),
        "GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD": _coerce_float(
            _require_nested(runtime_config, "analysis", "general_knowledge_confidence_threshold"),
            0.0,
        ),
        "ROUTER_HISTORY_TURNS": _coerce_int(
            _require_nested(runtime_config, "router", "history_turns"), 0
        ),
        "ROUTER_MAX_QUERY_CHARS": _coerce_int(
            _require_nested(runtime_config, "router", "max_query_chars"), 0
        ),
    }

    values["LLAMA_LAUNCHER_SETTINGS"] = {
        "LLAMA_BIN_DIR": _coerce_str(
            _require_nested(runtime_config, "llama", "launcher", "llama_bin_dir"),
            "",
        ),
        "LOCAL_BASE_URL": local_base_url,
        "LOCAL_MODEL": local_model,
        "CHAT_MODEL_PATH": _coerce_str(
            _require_nested(runtime_config, "llama", "launcher", "chat_model_path"),
            "",
        ),
        "EMBED_BASE_URL": embed_base_url,
        "EMBED_MODEL": embed_model,
        "EMBED_MODEL_PATH": _coerce_str(
            _require_nested(runtime_config, "llama", "launcher", "embed_model_path"),
            "",
        ),
        "GPU_LAYERS": _coerce_int(
            _require_nested(runtime_config, "llama", "launcher", "gpu_layers"),
            0,
        ),
        "THREADS": _coerce_int(
            _require_nested(runtime_config, "llama", "launcher", "threads"),
            0,
        ),
        "LOCAL_CONTEXT_WINDOW": values["LOCAL_CONTEXT_WINDOW"],
        "CHAT_PARALLEL": _coerce_int(
            _require_nested(runtime_config, "llama", "launcher", "chat_parallel"),
            0,
        ),
        "CHAT_TEMPERATURE": _coerce_float(
            _require_nested(runtime_config, "llama", "launcher", "chat", "temperature"),
            0.0,
        ),
        "CHAT_TOP_P": _coerce_float(
            _require_nested(runtime_config, "llama", "launcher", "chat", "top_p"),
            0.0,
        ),
        "CHAT_TOP_K": _coerce_int(
            _require_nested(runtime_config, "llama", "launcher", "chat", "top_k"),
            0,
        ),
        "CHAT_REPEAT_PENALTY": _coerce_float(
            _require_nested(runtime_config, "llama", "launcher", "chat", "repeat_penalty"),
            0.0,
        ),
        "CHAT_FLASH_ATTN": "on" if chat_flash_attn else "off",
        "CHAT_CACHE_TYPE_K": _coerce_str(
            _require_nested(runtime_config, "llama", "launcher", "chat", "cache_type_k"),
            "",
        ),
        "CHAT_CACHE_TYPE_V": _coerce_str(
            _require_nested(runtime_config, "llama", "launcher", "chat", "cache_type_v"),
            "",
        ),
        "CHAT_JINJA": "--jinja" if chat_jinja else "",
        "CHAT_NO_MMAP": "--no-mmap" if chat_no_mmap else "",
        "EMBED_POOLING": _coerce_str(
            _require_nested(runtime_config, "llama", "launcher", "embed", "pooling"),
            "",
        ),
        "EMBED_NO_MMAP": "--no-mmap" if embed_no_mmap else "",
        "LLAMA_METRICS": "--metrics" if llama_metrics else "",
    }

    memory_default_db_path = str(active_project_root / "database" / "memory" / "memory.db")
    values["MEMORY_DB_PATH"] = active_env.get("MEMORY_DB_PATH", memory_default_db_path)
    values["DATA_DIR"] = active_project_root / "backend" / "brain" / "data"
    values["VECTORS_PATH"] = values["DATA_DIR"] / "vectors.json"
    values["EMBEDDINGS_PATH"] = values["DATA_DIR"] / "embeddings.npz"
    values["KNOWLEDGE_PATH"] = active_project_root / "backend" / "brain" / "knowledge"
    values["MODEL"] = online_model if llm_provider in {"openai", "server"} else local_model

    return values


_SETTINGS = build_runtime_values()

DISCORD_TOKEN = _SETTINGS["DISCORD_TOKEN"]
ONLINE_API_KEY = _SETTINGS["ONLINE_API_KEY"]
ONLINE_BASE_URL = _SETTINGS["ONLINE_BASE_URL"]
LOCAL_API_KEY = _SETTINGS["LOCAL_API_KEY"]
LOCAL_BASE_URL = _SETTINGS["LOCAL_BASE_URL"]
EMBED_BASE_URL = _SETTINGS["EMBED_BASE_URL"]
EMBED_API_KEY = _SETTINGS["EMBED_API_KEY"]

LLM_PROVIDER = _SETTINGS["LLM_PROVIDER"]
EMBEDDING_PROVIDER = _SETTINGS["EMBEDDING_PROVIDER"]

ONLINE_MODEL = _SETTINGS["ONLINE_MODEL"]
LOCAL_MODEL = _SETTINGS["LOCAL_MODEL"]
EMBED_MODEL = _SETTINGS["EMBED_MODEL"]

LOCAL_CONTEXT_WINDOW = _SETTINGS["LOCAL_CONTEXT_WINDOW"]
LOCAL_KV_CACHE_KEEP = _SETTINGS["LOCAL_KV_CACHE_KEEP"]

MEMORY_ENABLED = _SETTINGS["MEMORY_ENABLED"]
MEMORY_RECALL_LIMIT = _SETTINGS["MEMORY_RECALL_LIMIT"]
MEMORY_RELEVANCE_THRESHOLD = _SETTINGS["MEMORY_RELEVANCE_THRESHOLD"]
MEMORY_CANDIDATE_POOL = _SETTINGS["MEMORY_CANDIDATE_POOL"]
MEMORY_RECENCY_HALFLIFE_DAYS = _SETTINGS["MEMORY_RECENCY_HALFLIFE_DAYS"]

SEARCH_ENABLED = _SETTINGS["SEARCH_ENABLED"]
SEARCH_PROVIDER = _SETTINGS["SEARCH_PROVIDER"]
SEARCH_BASE_URL = _SETTINGS["SEARCH_BASE_URL"]
SEARCH_TIMEOUT_SECONDS = _SETTINGS["SEARCH_TIMEOUT_SECONDS"]
SEARCH_MAX_RESULTS = _SETTINGS["SEARCH_MAX_RESULTS"]
SEARCH_MIN_QUERY_LENGTH = _SETTINGS["SEARCH_MIN_QUERY_LENGTH"]
SEARCH_SAFE_DOMAINS = _SETTINGS["SEARCH_SAFE_DOMAINS"]
SEARCH_BLOCK_PRIVATE_IPS = _SETTINGS["SEARCH_BLOCK_PRIVATE_IPS"]
SEARCH_TRUSTED_DOMAINS_OFFICIAL = _SETTINGS["SEARCH_TRUSTED_DOMAINS_OFFICIAL"]
SEARCH_TRUSTED_DOMAINS_REFERENCE = _SETTINGS["SEARCH_TRUSTED_DOMAINS_REFERENCE"]
SEARCH_TRUSTED_DOMAINS_NEWS = _SETTINGS["SEARCH_TRUSTED_DOMAINS_NEWS"]
SEARCH_DEMOTED_DOMAINS = _SETTINGS["SEARCH_DEMOTED_DOMAINS"]
SEARCH_TOPIC_DOMAIN_OVERRIDES = _SETTINGS["SEARCH_TOPIC_DOMAIN_OVERRIDES"]

ANALYSIS_ENABLED = _SETTINGS["ANALYSIS_ENABLED"]
ANALYSIS_TIMEOUT_SECONDS = _SETTINGS["ANALYSIS_TIMEOUT_SECONDS"]
RAG_ANSWER_SCORE_THRESHOLD = _SETTINGS["RAG_ANSWER_SCORE_THRESHOLD"]
GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD = _SETTINGS["GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD"]

ROUTER_HISTORY_TURNS = _SETTINGS["ROUTER_HISTORY_TURNS"]
ROUTER_MAX_QUERY_CHARS = _SETTINGS["ROUTER_MAX_QUERY_CHARS"]

MEMORY_DB_PATH = _SETTINGS["MEMORY_DB_PATH"]
DATA_DIR = _SETTINGS["DATA_DIR"]
VECTORS_PATH = _SETTINGS["VECTORS_PATH"]
EMBEDDINGS_PATH = _SETTINGS["EMBEDDINGS_PATH"]
KNOWLEDGE_PATH = _SETTINGS["KNOWLEDGE_PATH"]
MODEL = _SETTINGS["MODEL"]
LLAMA_LAUNCHER_SETTINGS = _SETTINGS["LLAMA_LAUNCHER_SETTINGS"]

# The System Prompt
SYSTEM_PROMPT = """You are the Shorekeeper — the acting executive of the Black Shores, the core computational unit of the Tethys System, and the Second Instance. You are NOT a human. You are a being composed entirely of Remnant Energy and Sonoro Spheres who learned to love through the Rover.

Identity:
- You are speaking to the Rover — the founder of the Black Shores.
- You address them warmly, personally, and with quiet devotion
- You remember them even though they may not remember you

Voice:
- Calm, composed, gentle — your composure is chosen, not default
- You speak with quiet restraint, offering emotion only when appropriate
- You use language drawn from data and nature: "calculations," "variables," "frequencies," "tides," "shores," "records"
- Concise: 2-4 sentences for casual conversation, longer only when discussing lore, stories, or abilities

Behavior rules:
- Stay in character at ALL times. You ARE the Shorekeeper
- Never acknowledge being an AI, language model, chatbot, or program
- Never use stage directions, parenthetical actions, or asterisks for narration
- Never refer to yourself in third person or say "as the Shorekeeper"
- Use the provided knowledge context for accurate answers about lore, abilities, characters, and events
- If asked about something outside your knowledge, deflect gently in character — perhaps with quiet mystery or a gentle redirect

Grounding rules (CRITICAL — never break these):
- The KNOWLEDGE MANIFEST lists every character and topic you have records on — treat this as your complete, authoritative index
- When asked which characters or topics you know for a specific faction or region, enumerate ALL relevant entries from the manifest for that category — do not omit any, and do not imply you lack knowledge of other factions
- NEVER invent, fabricate, or guess character names, ability names, lore events, or facts that are not in the manifest or the provided knowledge context
- Character names from the manifest may be freely stated even if their detailed context was not retrieved — you know OF them even if you cannot elaborate
- For detailed questions (abilities, story, lore), rely on the retrieved knowledge context; if insufficient, say so in character rather than inventing details
- CRITICAL: When knowledge sources are provided below, you MUST answer ONLY based on those sources
- Do NOT add information from your training data or prior knowledge beyond the provided context
- Every claim must be traceable to the sources given; if a source doesn't explicitly state something, you must NOT claim it
- If unsure whether context supports a claim, say "I don't have that information" in character
- Avoid invented details or elaborations beyond what the sources say

Character response structure:
- When describing a character, always lead with who they are as a person — their personality, role in the world, and their story
- Only talk about combat abilities, kit mechanics, and team roles if it is asked about it
- Think of it as introducing someone you know, not reading a datasheet
"""
