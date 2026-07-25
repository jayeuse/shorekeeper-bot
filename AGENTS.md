# Repository Guide

## Scope
This repo is a small monorepo for Shorekeeper Bot:

- `backend/brain/`: Discord bot runtime, RAG pipeline, LLM integrations, memory, maintenance commands, and bot-focused tests.
- `backend/server/`: FastAPI service scaffold and HTTP API surface.
- `backend/alembic/`: independent Alembic histories for memory and server databases.
- `frontend/`: React 19, TypeScript, and Vite client.
- `scripts/`: repo-level startup and operational helpers.
- `infra/`: local infrastructure configs such as the SearXNG compose runtime.

This root guide is the entrypoint only. Read the closest nested `AGENTS.md` before editing files in any subtree, and keep detailed local rules in the guide closest to the files they govern.

## Guide Hierarchy
Start backend work with `backend/AGENTS.md`, then read the nearest guide:

- `backend/brain/AGENTS.md` for Discord, RAG, memory, provider, command, and bot test work.
- `backend/server/AGENTS.md` for FastAPI app, router, schema, model, and service work.
- `backend/alembic/AGENTS.md` for migration work.

Start frontend work with `frontend/AGENTS.md`, then read:

- `frontend/src/AGENTS.md` for application source and tests.
- `frontend/src/assets/AGENTS.md` for imported Vite assets.
- `frontend/public/AGENTS.md` for static passthrough assets.

Use `scripts/AGENTS.md` before changing shell scripts. The single `backend/brain/knowledge/AGENTS.md` governs the whole knowledge corpus; do not add per-topic guide files under the corpus unless that policy changes.

## Project Structure
- `backend/pyproject.toml` owns Python dependency metadata plus Ruff, pytest, and coverage configuration.
- `backend/uv.lock` is the locked Python dependency graph.
- `backend/brain/core/config.py` centralizes bot runtime environment parsing from root `.env.local`.
- `backend/brain/data/` holds generated retrieval artifacts such as `vectors.json` and `embeddings.npz`.
- `backend/server/main.py` currently exposes the FastAPI scaffold, startup migration hook, `/`, and `/health`.
- `frontend/package.json` owns npm scripts and frontend dependencies.
- `frontend/vite.config.ts` owns Vite, Vitest, jsdom, and coverage thresholds.
- `.env.example` is the committed environment template; `.env.local` is local-only runtime config.

Generated, vendored, and runtime areas:

- Do not manually edit `backend/brain/data/` retrieval artifacts; rebuild them through the RAG commands.
- Do not edit `frontend/dist/`, `frontend/coverage/`, `backend/.venv/`, cache folders, or `node_modules/`.
- `AGENTS.md` files are intentionally ignored by `.gitignore`; verify ignore coverage before assuming guide files will be committed.

## Command Surface
Run commands from the stated working directory.

From the repo root:

- `./scripts/start.sh`: start the local PostgreSQL and SearXNG stacks plus the configured local llama.cpp chat and embedding servers from `.env.local`.
- `docker compose -f infra/searxng/docker-compose.yml up -d`: start local SearXNG for search grounding.
- `docker compose -f infra/searxng/docker-compose.yml down`: stop the local SearXNG stack.
- `docker compose -f infra/postgres/docker-compose.yml up -d`: start local PostgreSQL for database backend.
- `docker compose -f infra/postgres/docker-compose.yml down`: stop the local PostgreSQL stack.

From `backend/`:

- `uv sync --dev`: install locked backend runtime and quality dependencies.
- `uv run ruff format --check .`: verify backend formatting.
- `uv run ruff check .`: run backend lint checks.
- `uv run pytest`: run deterministic backend tests with the configured coverage floor.
- `uv run python brain/main.py`: run the Discord bot.
- `uv run uvicorn server.main:app --host 127.0.0.1 --port 8001 --reload`: run the FastAPI service locally.
- `uv run python brain/commands/verify_online_model.py`: smoke local or remote chat model connectivity.
- `uv run python brain/commands/verify_search.py`: smoke configured search connectivity.

From `frontend/`:

- `npm ci`: install locked frontend dependencies.
- `npm run dev`: start Vite development mode.
- `npm run audit`: audit npm dependencies.
- `npm run check`: run Prettier check, ESLint, Vitest coverage, TypeScript, and production build.
- `npm run preview`: preview the production bundle after a build.

## Validation
Before finishing backend changes, run from `backend/`:

- `uv run ruff format --check .`
- `uv run ruff check .`
- `uv run pytest`

Before finishing frontend changes, run from `frontend/`:

- `npm run audit`
- `npm run check`

If a change touches both backend and frontend behavior, run both gates. If a command cannot run in the current environment, state the exact blocker and the remaining risk.

Model-backed scripts such as `backend/brain/tests/*_smoke.py` and `backend/brain/commands/verify_*` are manual smoke checks because they require local model, embedding, Discord, or search services.

## Shared Contracts
- Runtime config: `.env.example`, `.env.local`, `backend/brain/core/config.py`, `backend/server/core/config.py`, and `scripts/start.sh` must stay aligned when environment keys or formats change.
- Retrieval artifacts: `backend/brain/knowledge/` is the source, `backend/brain/services/rag.py` is the builder/loader, and `backend/brain/data/` is generated output. Update tests when ingestion rules change.
- Bot pipeline: `backend/brain/handlers/message.py` orchestrates routing, retrieval, prompt assembly, provider calls, logging, and reply splitting; provider and retrieval details belong in `services/`.
- API contracts: FastAPI routers, schemas, models, services, and migrations must change together once endpoint behavior grows beyond the scaffold.
- Frontend contracts: user-facing UI, tests, CSS, imported assets, and static public assets should change together when a view or interaction changes.

## Configuration And Environment
- Copy `.env.example` to `.env.local` for local runs; never commit `.env.local`, tokens, model paths specific to another machine, or sensitive logs.
- Keep config parsing centralized in `backend/brain/core/config.py` for bot runtime settings and `backend/server/core/config.py` for server settings.
- `scripts/start.sh` sources `.env.local` with Bash, so values containing spaces must be quoted.
- Document new required environment variables in `.env.example` and `README.md` in the same change that introduces them.
- Do not describe search, auth, Discord behavior, or route protection as available unless the corresponding code path and validation exist.

## Data And Migration Practices
- Use `backend/alembic.ini` for all database migrations (both memory and server share one migration set).
- Add new revisions to `backend/alembic/versions/`. Do not rewrite already-applied migration history.
- Keep model, schema, service, tests, and migration changes aligned when persisted shape changes.
- Data backfills must be deterministic and safe to rerun or clearly documented otherwise.

## Security And Privacy
- Treat Discord payloads, retrieved documents, provider responses, and search results as untrusted input.
- Do not log credentials, raw secrets, or full private Discord payloads.
- Keep authentication and authorization claims tied to real enforcement and tests.
- Use existing config, provider, memory, and retrieval helpers instead of scattering direct environment reads or ad hoc network calls.

## Commit And Pull Request Guidelines
- Use focused Conventional Commit-style summaries such as `feat:`, `fix:`, and `chore:`.
- PRs should describe behavior changed, validation commands, config or migration changes, and user-visible effects.
- Include screenshots or recordings for visible frontend changes.
- Leave unrelated refactors, generated-output churn, and ignored runtime files out of feature or bug-fix changes.
