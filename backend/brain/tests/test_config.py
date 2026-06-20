import sys
from pathlib import Path
from textwrap import dedent

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.config import SYSTEM_PROMPT, build_runtime_values


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).strip() + "\n", encoding="utf-8")


def test_build_runtime_values_reads_grouped_yaml_configs(tmp_path: Path) -> None:
    _write(
        tmp_path / "config" / "search.config.yml",
        """
        provider: searxng
        base_url: http://127.0.0.1:9999
        timeout_seconds: 3.5
        max_results: 8
        min_query_length: 9
        safe_domains:
          - allowed.example
        block_private_ips: false
        extraction:
          enabled: true
          max_results: 2
          timeout_seconds: 1.5
          max_concurrency: 1
          max_response_bytes: 2048
          max_extracted_chars_per_result: 256
          max_total_extracted_chars: 1024
          allow_redirects: false
          max_redirects: 1
          user_agent: TestAgent/1.0
        trusted_domains:
          official:
            - official.example
          reference:
            - reference.example
          news:
            - news.example
        demoted_domains:
          - demoted.example
        topic_domain_overrides:
          finance:
            preferred:
              - finance.example
        """,
    )
    _write(
        tmp_path / "config" / "runtime.config.yml",
        """
        providers:
          llm_provider: openai
          embedding_provider: llamacpp
          online_base_url: https://api.example.com
          online_model: remote-model
        llama:
          local:
            base_url: http://127.0.0.1:9001/v1
            model: custom-chat
            context_window: 32768
            kv_cache_keep: 9
          embed:
            base_url: http://127.0.0.1:9002/v1
            model: custom-embed
          launcher:
            llama_bin_dir: ~/custom-llama/bin
            chat_model_path: /models/chat.gguf
            embed_model_path: /models/embed.gguf
            gpu_layers: 42
            threads: 7
            chat_parallel: 3
            chat:
              temperature: 0.6
              top_p: 0.8
              top_k: 12
              repeat_penalty: 1.15
              flash_attn: false
              cache_type_k: q8_0
              cache_type_v: q6_0
              jinja: false
              no_mmap: false
            embed:
              pooling: mean
              ubatch_size: 2048
              no_mmap: false
            metrics: false
        memory:
          recall_limit: 5
          relevance_threshold: 0.44
          candidate_pool: 70
          recency_halflife_days: 12
        analysis:
          enabled: false
          timeout_seconds: 2.5
          rag_answer_score_threshold: 0.91
          general_knowledge_confidence_threshold: 0.88
        router:
          history_turns: 6
          max_query_chars: 320
        """,
    )

    values = build_runtime_values(
        env={
            "DISCORD_TOKEN": "token",
            "MEMORY_ENABLED": "false",
            "SEARCH_ENABLED": "true",
            "LOCAL_API_KEY": "no-key",
            "EMBED_API_KEY": "embed-key",
            "DATABASE_URL": "postgresql://shorekeeper:shorekeeper_dev@localhost:5432/shorekeeper",
        },
        project_root=tmp_path,
    )

    assert values["LOCAL_BASE_URL"] == "http://127.0.0.1:9001/v1"
    assert values["LOCAL_MODEL"] == "custom-chat"
    assert values["EMBED_BASE_URL"] == "http://127.0.0.1:9002/v1"
    assert values["EMBED_MODEL"] == "custom-embed"
    assert values["LOCAL_CONTEXT_WINDOW"] == 32768
    assert values["LOCAL_KV_CACHE_KEEP"] == 9
    assert values["ONLINE_BASE_URL"] == "https://api.example.com"
    assert values["ONLINE_MODEL"] == "remote-model"
    assert values["LLM_PROVIDER"] == "openai"
    assert values["MEMORY_ENABLED"] is False
    assert values["SEARCH_ENABLED"] is True
    assert values["SEARCH_BASE_URL"] == "http://127.0.0.1:9999"
    assert values["SEARCH_TIMEOUT_SECONDS"] == 3.5
    assert values["SEARCH_EXTRACTION_ENABLED"] is True
    assert values["SEARCH_EXTRACTION_MAX_RESULTS"] == 2
    assert values["SEARCH_EXTRACTION_TIMEOUT_SECONDS"] == 1.5
    assert values["SEARCH_EXTRACTION_MAX_CONCURRENCY"] == 1
    assert values["SEARCH_EXTRACTION_MAX_RESPONSE_BYTES"] == 2048
    assert values["SEARCH_EXTRACTION_MAX_CHARS_PER_RESULT"] == 256
    assert values["SEARCH_EXTRACTION_MAX_TOTAL_CHARS"] == 1024
    assert values["SEARCH_EXTRACTION_ALLOW_REDIRECTS"] is False
    assert values["SEARCH_EXTRACTION_MAX_REDIRECTS"] == 1
    assert values["SEARCH_EXTRACTION_USER_AGENT"] == "TestAgent/1.0"
    assert values["SEARCH_TRUSTED_DOMAINS_OFFICIAL"] == ["official.example"]
    assert values["SEARCH_TOPIC_DOMAIN_OVERRIDES"] == {
        "finance": {"preferred": ["finance.example"]}
    }
    assert values["ANALYSIS_ENABLED"] is False
    assert values["ROUTER_HISTORY_TURNS"] == 6
    assert values["KNOWLEDGE_DB_PATH"] == values["DATABASE_URL"]
    assert values["VECTORS_PATH"] == tmp_path / "backend" / "brain" / "data" / "local_vectors.json"
    assert values["EMBEDDINGS_PATH"] == (
        tmp_path / "backend" / "brain" / "data" / "local_embeddings.npz"
    )
    assert values["LLAMA_LAUNCHER_SETTINGS"] == {
        "LLAMA_BIN_DIR": "~/custom-llama/bin",
        "LOCAL_BASE_URL": "http://127.0.0.1:9001/v1",
        "LOCAL_MODEL": "custom-chat",
        "CHAT_MODEL_PATH": "/models/chat.gguf",
        "EMBED_BASE_URL": "http://127.0.0.1:9002/v1",
        "EMBED_MODEL": "custom-embed",
        "EMBED_MODEL_PATH": "/models/embed.gguf",
        "EMBED_UBATCH_SIZE": 2048,
        "GPU_LAYERS": 42,
        "THREADS": 7,
        "LOCAL_CONTEXT_WINDOW": 32768,
        "CHAT_PARALLEL": 3,
        "CHAT_TEMPERATURE": 0.6,
        "CHAT_TOP_P": 0.8,
        "CHAT_TOP_K": 12,
        "CHAT_REPEAT_PENALTY": 1.15,
        "CHAT_FLASH_ATTN": "off",
        "CHAT_CACHE_TYPE_K": "q8_0",
        "CHAT_CACHE_TYPE_V": "q6_0",
        "CHAT_JINJA": "",
        "CHAT_NO_MMAP": "",
        "EMBED_POOLING": "mean",
        "EMBED_NO_MMAP": "",
        "LLAMA_METRICS": "",
    }


def test_build_runtime_values_uses_online_artifact_paths_and_db_target(tmp_path: Path) -> None:
    _write(
        tmp_path / "config" / "search.config.yml",
        """
        provider: searxng
        base_url: http://127.0.0.1:8083
        timeout_seconds: 8
        max_results: 5
        min_query_length: 5
        safe_domains: []
        block_private_ips: true
        trusted_domains:
          official: []
          reference: []
          news: []
        demoted_domains: []
        topic_domain_overrides: {}
        """,
    )
    _write(
        tmp_path / "config" / "runtime.config.yml",
        """
        providers:
          llm_provider: llamacpp
          embedding_provider: llamacpp
          online_base_url: https://api.example.com
          online_model: yaml-remote
        llama:
          local:
            base_url: http://127.0.0.1:8081/v1
            model: yaml-chat
            context_window: 16384
            kv_cache_keep: 4
          embed:
            base_url: http://127.0.0.1:8082/v1
            model: yaml-embed
          launcher:
            llama_bin_dir: ~/llama/bin
            chat_model_path: /models/chat.gguf
            embed_model_path: /models/embed.gguf
            gpu_layers: 20
            threads: 8
            chat_parallel: 1
            chat:
              temperature: 0.3
              top_p: 0.9
              top_k: 40
              repeat_penalty: 1.05
              flash_attn: true
              cache_type_k: q4_0
              cache_type_v: q4_0
              jinja: true
              no_mmap: true
            embed:
              pooling: cls
              ubatch_size: 2048
              no_mmap: true
            metrics: true
        memory:
          recall_limit: 3
          relevance_threshold: 0.22
          candidate_pool: 60
          recency_halflife_days: 30
        analysis:
          enabled: true
          timeout_seconds: 6
          rag_answer_score_threshold: 0.62
          general_knowledge_confidence_threshold: 0.7
        router:
          history_turns: 4
          max_query_chars: 240
        """,
    )

    values = build_runtime_values(
        env={
            "DISCORD_TOKEN": "token",
            "MEMORY_ENABLED": "true",
            "SEARCH_ENABLED": "false",
            "LOCAL_API_KEY": "no-key",
            "EMBED_API_KEY": "embed-key",
            "MODE": "online",
            "DATABASE_URL": "postgresql://postgres:postgres@localhost:5432/shorekeeper",
            "ONLINE_LLM_API_KEY": "remote-key",
        },
        project_root=tmp_path,
    )

    assert values["KNOWLEDGE_DB_PATH"] == values["DATABASE_URL"]
    assert values["VECTORS_PATH"] == tmp_path / "backend" / "brain" / "data" / "vectors.json"
    assert values["EMBEDDINGS_PATH"] == tmp_path / "backend" / "brain" / "data" / "embeddings.npz"


def test_build_runtime_values_local_mode_uses_database_url_when_set(tmp_path: Path) -> None:
    _write(
        tmp_path / "config" / "search.config.yml",
        """
        provider: searxng
        base_url: http://127.0.0.1:8083
        timeout_seconds: 8
        max_results: 5
        min_query_length: 5
        safe_domains: []
        block_private_ips: true
        trusted_domains:
          official: []
          reference: []
          news: []
        demoted_domains: []
        topic_domain_overrides: {}
        """,
    )
    _write(
        tmp_path / "config" / "runtime.config.yml",
        """
        providers:
          llm_provider: llamacpp
          embedding_provider: llamacpp
          online_base_url: https://api.example.com
          online_model: yaml-remote
        llama:
          local:
            base_url: http://127.0.0.1:8081/v1
            model: yaml-chat
            context_window: 16384
            kv_cache_keep: 4
          embed:
            base_url: http://127.0.0.1:8082/v1
            model: yaml-embed
          launcher:
            llama_bin_dir: ~/llama/bin
            chat_model_path: /models/chat.gguf
            embed_model_path: /models/embed.gguf
            gpu_layers: 20
            threads: 8
            chat_parallel: 1
            chat:
              temperature: 0.3
              top_p: 0.9
              top_k: 40
              repeat_penalty: 1.05
              flash_attn: true
              cache_type_k: q4_0
              cache_type_v: q4_0
              jinja: true
              no_mmap: true
            embed:
              pooling: cls
              no_mmap: true
            metrics: true
        memory:
          recall_limit: 3
          relevance_threshold: 0.22
          candidate_pool: 60
          recency_halflife_days: 30
        analysis:
          enabled: true
          timeout_seconds: 6
          rag_answer_score_threshold: 0.62
          general_knowledge_confidence_threshold: 0.7
        router:
          history_turns: 4
          max_query_chars: 240
        """,
    )

    values = build_runtime_values(
        env={
            "DISCORD_TOKEN": "token",
            "MEMORY_ENABLED": "true",
            "SEARCH_ENABLED": "false",
            "LOCAL_API_KEY": "no-key",
            "EMBED_API_KEY": "embed-key",
            "MODE": "local",
            "DATABASE_URL": "postgresql://shorekeeper:shorekeeper_dev@localhost:5432/shorekeeper",
        },
        project_root=tmp_path,
    )

    assert values["KNOWLEDGE_DB_PATH"] == values["DATABASE_URL"]
    assert values["MEMORY_DB_PATH"] == values["DATABASE_URL"]


def test_build_runtime_values_requires_expected_config_keys(tmp_path: Path) -> None:
    _write(
        tmp_path / "config" / "search.config.yml",
        """
        provider: searxng
        base_url: http://127.0.0.1:8083
        timeout_seconds: 8
        max_results: 5
        min_query_length: 5
        safe_domains: []
        block_private_ips: true
        trusted_domains:
          official: []
          reference: []
          news: []
        demoted_domains: []
        topic_domain_overrides: {}
        """,
    )
    _write(
        tmp_path / "config" / "runtime.config.yml",
        """
        providers:
          llm_provider: llamacpp
          embedding_provider: llamacpp
          online_base_url: https://api.example.com
          online_model: yaml-remote
        llama:
          local:
            base_url: http://127.0.0.1:8081/v1
            model: yaml-chat
          embed:
            base_url: http://127.0.0.1:8082/v1
            model: yaml-embed
          launcher:
            llama_bin_dir: ~/llama/bin
            chat_model_path: /models/chat.gguf
            gpu_layers: 999
            threads: 12
            chat_parallel: 1
            chat:
              temperature: 0.3
              top_p: 0.9
              top_k: 40
              repeat_penalty: 1.05
              flash_attn: true
              cache_type_k: q4_0
              cache_type_v: q4_0
              jinja: true
              no_mmap: true
            embed:
              pooling: cls
              no_mmap: true
            metrics: true
        memory:
          recall_limit: 3
          relevance_threshold: 0.22
          candidate_pool: 60
          recency_halflife_days: 30
        analysis:
          enabled: true
          timeout_seconds: 6
          rag_answer_score_threshold: 0.62
          general_knowledge_confidence_threshold: 0.7
        router:
          history_turns: 4
          max_query_chars: 240
        """,
    )

    with pytest.raises(RuntimeError, match="DATABASE_URL is required"):
        build_runtime_values(
            env={
                "DISCORD_TOKEN": "token",
                "MEMORY_ENABLED": "true",
                "SEARCH_ENABLED": "false",
                "LOCAL_API_KEY": "no-key",
                "EMBED_API_KEY": "embed-key",
            },
            project_root=tmp_path,
        )


def test_system_prompt_allows_grounded_live_search_answers() -> None:
    assert "If grounded live-search evidence is provided" in SYSTEM_PROMPT
    assert "When live-search sources are provided below" in SYSTEM_PROMPT
