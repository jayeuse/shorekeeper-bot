import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from core.config_files import find_project_root, load_yaml_mapping, resolve_project_path
from core.config_parsing import (
    coerce_bool,
    coerce_float,
    coerce_int,
    coerce_mapping,
    coerce_str,
    coerce_str_list,
    require_bool_env,
    require_env,
    require_nested,
)
from dotenv import load_dotenv


def load_runtime_environment(project_root: Path | None = None) -> Path:
    active_project_root = project_root or find_project_root(Path(__file__))
    load_dotenv(str(active_project_root / ".env.local"), override=True)
    return active_project_root


def _build_launcher_settings(
    runtime_config: Mapping[str, Any],
    *,
    local_base_url: str,
    local_model: str,
    embed_base_url: str,
    embed_model: str,
    local_context_window: int,
) -> dict[str, Any]:
    chat_flash_attn = coerce_bool(
        require_nested(runtime_config, "llama", "launcher", "chat", "flash_attn"),
        False,
    )
    chat_jinja = coerce_bool(
        require_nested(runtime_config, "llama", "launcher", "chat", "jinja"),
        False,
    )
    chat_no_mmap = coerce_bool(
        require_nested(runtime_config, "llama", "launcher", "chat", "no_mmap"),
        False,
    )
    embed_no_mmap = coerce_bool(
        require_nested(runtime_config, "llama", "launcher", "embed", "no_mmap"),
        False,
    )
    llama_metrics = coerce_bool(
        require_nested(runtime_config, "llama", "launcher", "metrics"),
        False,
    )

    return {
        "LLAMA_BIN_DIR": coerce_str(
            require_nested(runtime_config, "llama", "launcher", "llama_bin_dir"),
            "",
        ),
        "LOCAL_BASE_URL": local_base_url,
        "LOCAL_MODEL": local_model,
        "CHAT_MODEL_PATH": coerce_str(
            require_nested(runtime_config, "llama", "launcher", "chat_model_path"),
            "",
        ),
        "EMBED_BASE_URL": embed_base_url,
        "EMBED_MODEL": embed_model,
        "EMBED_MODEL_PATH": coerce_str(
            require_nested(runtime_config, "llama", "launcher", "embed_model_path"),
            "",
        ),
        "GPU_LAYERS": coerce_int(
            require_nested(runtime_config, "llama", "launcher", "gpu_layers"),
            0,
        ),
        "THREADS": coerce_int(
            require_nested(runtime_config, "llama", "launcher", "threads"),
            0,
        ),
        "LOCAL_CONTEXT_WINDOW": local_context_window,
        "CHAT_PARALLEL": coerce_int(
            require_nested(runtime_config, "llama", "launcher", "chat_parallel"),
            0,
        ),
        "CHAT_TEMPERATURE": coerce_float(
            require_nested(runtime_config, "llama", "launcher", "chat", "temperature"),
            0.0,
        ),
        "CHAT_TOP_P": coerce_float(
            require_nested(runtime_config, "llama", "launcher", "chat", "top_p"),
            0.0,
        ),
        "CHAT_TOP_K": coerce_int(
            require_nested(runtime_config, "llama", "launcher", "chat", "top_k"),
            0,
        ),
        "CHAT_REPEAT_PENALTY": coerce_float(
            require_nested(runtime_config, "llama", "launcher", "chat", "repeat_penalty"),
            0.0,
        ),
        "CHAT_FLASH_ATTN": "on" if chat_flash_attn else "off",
        "CHAT_CACHE_TYPE_K": coerce_str(
            require_nested(runtime_config, "llama", "launcher", "chat", "cache_type_k"),
            "",
        ),
        "CHAT_CACHE_TYPE_V": coerce_str(
            require_nested(runtime_config, "llama", "launcher", "chat", "cache_type_v"),
            "",
        ),
        "CHAT_JINJA": "--jinja" if chat_jinja else "",
        "CHAT_NO_MMAP": "--no-mmap" if chat_no_mmap else "",
        "EMBED_POOLING": coerce_str(
            require_nested(runtime_config, "llama", "launcher", "embed", "pooling"),
            "",
        ),
        "EMBED_NO_MMAP": "--no-mmap" if embed_no_mmap else "",
        "LLAMA_METRICS": "--metrics" if llama_metrics else "",
    }


def build_runtime_values(
    env: Mapping[str, str] | None = None, project_root: Path | None = None
) -> dict[str, Any]:
    active_env = dict(os.environ if env is None else env)
    active_project_root = project_root or find_project_root(Path(__file__))

    search_config_path = resolve_project_path(active_project_root, "config/search.config.yml")
    runtime_config_path = resolve_project_path(active_project_root, "config/runtime.config.yml")
    search_config = load_yaml_mapping(Path(search_config_path))
    runtime_config = load_yaml_mapping(Path(runtime_config_path))

    local_base_url = coerce_str(
        require_nested(runtime_config, "llama", "local", "base_url"),
        "",
    )
    embed_base_url = coerce_str(
        require_nested(runtime_config, "llama", "embed", "base_url"),
        "",
    )
    local_model = coerce_str(
        require_nested(runtime_config, "llama", "local", "model"),
        "",
    )
    embed_model = coerce_str(
        require_nested(runtime_config, "llama", "embed", "model"),
        "",
    )

    llm_provider = coerce_str(
        require_nested(runtime_config, "providers", "llm_provider"), ""
    ).lower()
    embedding_provider = coerce_str(
        require_nested(runtime_config, "providers", "embedding_provider"),
        "",
    ).lower()
    online_model = coerce_str(
        require_nested(runtime_config, "providers", "online_model"),
        "",
    )
    online_base_url = coerce_str(active_env.get("ONLINE_BASE_URL"), "") or coerce_str(
        require_nested(runtime_config, "providers", "online_base_url"),
        "",
    )

    mode = coerce_str(active_env.get("MODE"), "local").lower()
    if mode not in {"online", "local"}:
        raise RuntimeError(f"MODE must be 'online' or 'local', got: {mode}")

    online_llm_api_key = active_env.get("ONLINE_LLM_API_KEY")
    online_llm_model = (
        active_env.get("ONLINE_LLM_MODEL") or active_env.get("ONLINE_LLM_NAME") or online_model
    )
    online_embedder_model = (
        active_env.get("ONLINE_EMBEDDER_MODEL")
        or active_env.get("ONLINE_EMBEDDER_NAME")
        or embed_model
    )

    if mode == "online":
        llm_provider = "openai"
        embedding_provider = "openai"
        online_model = online_llm_model

    search_provider = coerce_str(require_nested(search_config, "provider"), "").strip().lower()
    search_base_url = coerce_str(require_nested(search_config, "base_url"), "").strip()
    search_topic_domain_overrides = coerce_mapping(
        require_nested(search_config, "topic_domain_overrides")
    )
    search_extraction = coerce_mapping(search_config.get("extraction"), {})

    database_url = active_env.get("DATABASE_URL") or active_env.get(
        "SUPABASE_DIRECT_CONNECTION_STRING"
    )
    if mode == "online" and not database_url:
        raise RuntimeError("DATABASE_URL is required when MODE=online")

    local_context_window = coerce_int(
        require_nested(runtime_config, "llama", "local", "context_window"),
        0,
    )

    values: dict[str, Any] = {
        "PROJECT_ROOT": active_project_root,
        "DISCORD_TOKEN": require_env(active_env, "DISCORD_TOKEN"),
        "MODE": mode,
        "ONLINE_BASE_URL": online_base_url,
        "ONLINE_LLM_API_KEY": online_llm_api_key,
        "ONLINE_LLM_MODEL": online_llm_model,
        "ONLINE_EMBEDDER_MODEL": online_embedder_model,
        "LOCAL_API_KEY": require_env(active_env, "LOCAL_API_KEY"),
        "LOCAL_BASE_URL": local_base_url,
        "EMBED_BASE_URL": embed_base_url,
        "EMBED_API_KEY": require_env(active_env, "EMBED_API_KEY"),
        "LLM_PROVIDER": llm_provider,
        "EMBEDDING_PROVIDER": embedding_provider,
        "ONLINE_MODEL": online_model,
        "LOCAL_MODEL": local_model,
        "EMBED_MODEL": embed_model,
        "DATABASE_URL": database_url,
        "LOCAL_CONTEXT_WINDOW": local_context_window,
        "LOCAL_KV_CACHE_KEEP": coerce_int(
            require_nested(runtime_config, "llama", "local", "kv_cache_keep"),
            0,
        ),
        "MEMORY_ENABLED": require_bool_env(active_env, "MEMORY_ENABLED"),
        "MEMORY_RECALL_LIMIT": coerce_int(
            require_nested(runtime_config, "memory", "recall_limit"), 0
        ),
        "MEMORY_RELEVANCE_THRESHOLD": coerce_float(
            require_nested(runtime_config, "memory", "relevance_threshold"),
            0.0,
        ),
        "MEMORY_CANDIDATE_POOL": coerce_int(
            require_nested(runtime_config, "memory", "candidate_pool"),
            0,
        ),
        "MEMORY_RECENCY_HALFLIFE_DAYS": coerce_float(
            require_nested(runtime_config, "memory", "recency_halflife_days"),
            0.0,
        ),
        "SEARCH_ENABLED": require_bool_env(active_env, "SEARCH_ENABLED"),
        "SEARCH_PROVIDER": search_provider,
        "SEARCH_BASE_URL": search_base_url,
        "SEARCH_TIMEOUT_SECONDS": coerce_float(
            require_nested(search_config, "timeout_seconds"),
            0.0,
        ),
        "SEARCH_MAX_RESULTS": coerce_int(require_nested(search_config, "max_results"), 0),
        "SEARCH_MIN_QUERY_LENGTH": coerce_int(
            require_nested(search_config, "min_query_length"),
            0,
        ),
        "SEARCH_SAFE_DOMAINS": coerce_str_list(require_nested(search_config, "safe_domains")),
        "SEARCH_BLOCK_PRIVATE_IPS": coerce_bool(
            require_nested(search_config, "block_private_ips"),
            False,
        ),
        "SEARCH_EXTRACTION_ENABLED": coerce_bool(
            search_extraction.get("enabled"),
            True,
        ),
        "SEARCH_EXTRACTION_MAX_RESULTS": coerce_int(
            search_extraction.get("max_results"),
            3,
        ),
        "SEARCH_EXTRACTION_TIMEOUT_SECONDS": coerce_float(
            search_extraction.get("timeout_seconds"),
            4.0,
        ),
        "SEARCH_EXTRACTION_MAX_CONCURRENCY": coerce_int(
            search_extraction.get("max_concurrency"),
            2,
        ),
        "SEARCH_EXTRACTION_MAX_RESPONSE_BYTES": coerce_int(
            search_extraction.get("max_response_bytes"),
            1_048_576,
        ),
        "SEARCH_EXTRACTION_MAX_CHARS_PER_RESULT": coerce_int(
            search_extraction.get("max_extracted_chars_per_result"),
            2000,
        ),
        "SEARCH_EXTRACTION_MAX_TOTAL_CHARS": coerce_int(
            search_extraction.get("max_total_extracted_chars"),
            6000,
        ),
        "SEARCH_EXTRACTION_ALLOW_REDIRECTS": coerce_bool(
            search_extraction.get("allow_redirects"),
            True,
        ),
        "SEARCH_EXTRACTION_MAX_REDIRECTS": coerce_int(
            search_extraction.get("max_redirects"),
            2,
        ),
        "SEARCH_EXTRACTION_USER_AGENT": coerce_str(
            search_extraction.get("user_agent"),
            "ShorekeeperBot/0.1",
        ),
        "SEARCH_TRUSTED_DOMAINS_OFFICIAL": coerce_str_list(
            require_nested(search_config, "trusted_domains", "official")
        ),
        "SEARCH_TRUSTED_DOMAINS_REFERENCE": coerce_str_list(
            require_nested(search_config, "trusted_domains", "reference")
        ),
        "SEARCH_TRUSTED_DOMAINS_NEWS": coerce_str_list(
            require_nested(search_config, "trusted_domains", "news")
        ),
        "SEARCH_DEMOTED_DOMAINS": coerce_str_list(require_nested(search_config, "demoted_domains")),
        "SEARCH_TOPIC_DOMAIN_OVERRIDES": search_topic_domain_overrides,
        "ANALYSIS_ENABLED": coerce_bool(
            require_nested(runtime_config, "analysis", "enabled"),
            False,
        ),
        "ANALYSIS_TIMEOUT_SECONDS": coerce_float(
            require_nested(runtime_config, "analysis", "timeout_seconds"),
            0.0,
        ),
        "RAG_ANSWER_SCORE_THRESHOLD": coerce_float(
            require_nested(runtime_config, "analysis", "rag_answer_score_threshold"),
            0.0,
        ),
        "GENERAL_KNOWLEDGE_CONFIDENCE_THRESHOLD": coerce_float(
            require_nested(runtime_config, "analysis", "general_knowledge_confidence_threshold"),
            0.0,
        ),
        "ROUTER_HISTORY_TURNS": coerce_int(
            require_nested(runtime_config, "router", "history_turns"),
            0,
        ),
        "ROUTER_MAX_QUERY_CHARS": coerce_int(
            require_nested(runtime_config, "router", "max_query_chars"),
            0,
        ),
    }

    values["LLAMA_LAUNCHER_SETTINGS"] = _build_launcher_settings(
        runtime_config,
        local_base_url=local_base_url,
        local_model=local_model,
        embed_base_url=embed_base_url,
        embed_model=embed_model,
        local_context_window=local_context_window,
    )

    memory_default_db_path = str(active_project_root / "database" / "memory" / "memory.db")
    if mode == "online":
        values["MEMORY_DB_PATH"] = database_url
    else:
        values["MEMORY_DB_PATH"] = active_env.get("MEMORY_DB_PATH", memory_default_db_path)
    values["DATA_DIR"] = active_project_root / "backend" / "brain" / "data"
    values["VECTORS_PATH"] = values["DATA_DIR"] / "vectors.json"
    values["EMBEDDINGS_PATH"] = values["DATA_DIR"] / "embeddings.npz"
    values["KNOWLEDGE_PATH"] = active_project_root / "backend" / "brain" / "knowledge"
    values["MODEL"] = online_model if llm_provider in {"openai", "server"} else local_model

    return values
