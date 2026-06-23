# Local SearXNG

This directory contains the repo-managed local SearXNG runtime used by Shorekeeper's live search grounding.

## Start

```bash
cp infra/searxng/.env.example infra/searxng/.env
docker compose -f infra/searxng/docker-compose.yml up -d
```

Or start it together with both local llama.cpp servers from the repo root:

```bash
./scripts/start.sh
```

## Stop

```bash
docker compose -f infra/searxng/docker-compose.yml down
```

## Verify

```bash
docker compose -f infra/searxng/docker-compose.yml ps
curl "http://127.0.0.1:8083/search?q=latest%20Wuthering%20Waves%20update&format=json"

cd backend
uv run python brain/commands/verify_search.py
```

Shorekeeper search is considered ready only when `verify_search.py` succeeds against `SEARCH_BASE_URL`.
