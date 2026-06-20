#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
ENV_FILE="${PROJECT_ROOT}/.env.local"
SEARXNG_COMPOSE_FILE="${PROJECT_ROOT}/infra/searxng/docker-compose.yml"
POSTGRES_COMPOSE_FILE="${PROJECT_ROOT}/infra/postgres/docker-compose.yml"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "Missing env file: $ENV_FILE" >&2
  exit 1
fi

if [[ ! -f "$SEARXNG_COMPOSE_FILE" ]]; then
  echo "Missing SearXNG compose file: $SEARXNG_COMPOSE_FILE" >&2
  exit 1
fi

if [[ ! -f "$POSTGRES_COMPOSE_FILE" ]]; then
  echo "Missing Postgres compose file: $POSTGRES_COMPOSE_FILE" >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

CHAT_PID=""
EMBED_PID=""

require_env() {
  local name="$1"
  local value="${!name:-}"
  if [[ -z "$value" ]]; then
    echo "Missing required env var in .env.local: $name" >&2
    exit 1
  fi
}

require_file() {
  local path="$1"
  local label="$2"
  if [[ ! -f "$path" ]]; then
    echo "Missing ${label}: $path" >&2
    exit 1
  fi
}

require_command() {
  local name="$1"
  if ! command -v "$name" >/dev/null 2>&1; then
    echo "Missing required executable: $name" >&2
    exit 1
  fi
}

cleanup() {
  local exit_code=$?
  trap - EXIT INT TERM

  if [[ -n "$CHAT_PID" ]] && kill -0 "$CHAT_PID" 2>/dev/null; then
    kill "$CHAT_PID" 2>/dev/null || true
  fi
  if [[ -n "$EMBED_PID" ]] && kill -0 "$EMBED_PID" 2>/dev/null; then
    kill "$EMBED_PID" 2>/dev/null || true
  fi

  if command -v docker >/dev/null 2>&1; then
    docker compose -f "$SEARXNG_COMPOSE_FILE" down >/dev/null 2>&1 || true
    docker compose -f "$POSTGRES_COMPOSE_FILE" down >/dev/null 2>&1 || true
  fi

  wait 2>/dev/null || true
  exit "$exit_code"
}

trap cleanup EXIT INT TERM

require_command "docker"
require_command "uv"

# Load launcher values from the grouped YAML config selected by .env.local.
# shellcheck disable=SC1091
source <(
  uv run --project "$PROJECT_ROOT/backend" python \
    "$PROJECT_ROOT/scripts/print-llama-launcher-env.py"
)

require_env "LLAMA_BIN_DIR"
require_env "LOCAL_BASE_URL"
require_env "LOCAL_MODEL"
require_env "CHAT_MODEL_PATH"
require_env "EMBED_BASE_URL"
require_env "EMBED_MODEL"
require_env "EMBED_MODEL_PATH"
require_env "EMBED_UBATCH_SIZE"
require_env "GPU_LAYERS"
require_env "THREADS"
require_env "LOCAL_CONTEXT_WINDOW"
require_env "CHAT_PARALLEL"
require_env "CHAT_TEMPERATURE"
require_env "CHAT_TOP_P"
require_env "CHAT_TOP_K"
require_env "CHAT_REPEAT_PENALTY"
require_env "CHAT_FLASH_ATTN"
require_env "CHAT_CACHE_TYPE_K"
require_env "CHAT_CACHE_TYPE_V"
require_env "EMBED_POOLING"

LLAMA_SERVER_BIN="${LLAMA_BIN_DIR}/llama-server"
CHAT_ALIAS="${LOCAL_MODEL}"
EMBED_ALIAS="${EMBED_MODEL}"
CHAT_HOST="$(printf '%s' "$LOCAL_BASE_URL" | sed -E 's#https?://([^/:]+).*#\1#')"
CHAT_PORT="$(printf '%s' "$LOCAL_BASE_URL" | sed -E 's#https?://[^/:]+:([0-9]+).*#\1#')"
EMBED_HOST="$(printf '%s' "$EMBED_BASE_URL" | sed -E 's#https?://([^/:]+).*#\1#')"
EMBED_PORT="$(printf '%s' "$EMBED_BASE_URL" | sed -E 's#https?://[^/:]+:([0-9]+).*#\1#')"

require_file "$LLAMA_SERVER_BIN" "llama-server binary"
require_file "$CHAT_MODEL_PATH" "chat model"
require_file "$EMBED_MODEL_PATH" "embedding model"

echo "Starting Postgres compose stack from ${POSTGRES_COMPOSE_FILE}"
docker compose -f "$POSTGRES_COMPOSE_FILE" up -d

echo "Starting SearXNG compose stack from ${SEARXNG_COMPOSE_FILE}"
docker compose -f "$SEARXNG_COMPOSE_FILE" up -d

chat_args=(
  -m "$CHAT_MODEL_PATH"
  --alias "$CHAT_ALIAS"
  --host "$CHAT_HOST"
  --port "$CHAT_PORT"
  -ngl "$GPU_LAYERS"
  -c "$LOCAL_CONTEXT_WINDOW"
  --parallel "$CHAT_PARALLEL"
  -t "$THREADS"
  -fa "$CHAT_FLASH_ATTN"
  --cache-type-k "$CHAT_CACHE_TYPE_K"
  --cache-type-v "$CHAT_CACHE_TYPE_V"
  --temp "$CHAT_TEMPERATURE"
  --top-p "$CHAT_TOP_P"
  --top-k "$CHAT_TOP_K"
  --repeat-penalty "$CHAT_REPEAT_PENALTY"
)

if [[ -n "${CHAT_NO_MMAP:-}" ]]; then
  chat_args+=("$CHAT_NO_MMAP")
fi
if [[ -n "${CHAT_JINJA:-}" ]]; then
  chat_args+=("$CHAT_JINJA")
fi
if [[ -n "${LLAMA_METRICS:-}" ]]; then
  chat_args+=("$LLAMA_METRICS")
fi

embed_args=(
  -m "$EMBED_MODEL_PATH"
  --alias "$EMBED_ALIAS"
  --host "$EMBED_HOST"
  --port "$EMBED_PORT"
  --embeddings
  --pooling "$EMBED_POOLING"
  --ubatch-size "$EMBED_UBATCH_SIZE"
  -ngl "$GPU_LAYERS"
  -t "$THREADS"
)

if [[ -n "${EMBED_NO_MMAP:-}" ]]; then
  embed_args+=("$EMBED_NO_MMAP")
fi
if [[ -n "${LLAMA_METRICS:-}" ]]; then
  embed_args+=("$LLAMA_METRICS")
fi

echo "Starting llama.cpp chat server on ${CHAT_HOST}:${CHAT_PORT} with alias ${CHAT_ALIAS}"
"$LLAMA_SERVER_BIN" "${chat_args[@]}" &
CHAT_PID=$!

echo "Starting llama.cpp embedding server on ${EMBED_HOST}:${EMBED_PORT} with alias ${EMBED_ALIAS}"
LLAMA_ARG_UBATCH="$EMBED_UBATCH_SIZE" "$LLAMA_SERVER_BIN" "${embed_args[@]}" &
EMBED_PID=$!

echo "Chat PID: $CHAT_PID"
echo "Embed PID: $EMBED_PID"
echo "Press Ctrl-C to stop the database, SearXNG, and llama.cpp servers."

wait -n "$CHAT_PID" "$EMBED_PID"
