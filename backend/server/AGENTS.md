# API Server Guide

## Scope
This guide applies to `backend/server/`.

Read this file first for FastAPI work, then read the closest local guide:

- `routers/AGENTS.md` for HTTP route handlers.
- `schemas/AGENTS.md` for request and response contracts.
- `models/AGENTS.md` for persisted data shape.
- `services/AGENTS.md` for API business logic.
- `core/AGENTS.md` for config and migration helpers.
- `apps/AGENTS.md` and `base/AGENTS.md` for local package scaffolding.

## Stack And Runtime
- Framework: FastAPI.
- Entrypoint: `server.main:app`.
- Local command from `backend/`: `uv run uvicorn server.main:app --host 127.0.0.1 --port 8001 --reload`.
- Startup currently runs the server Alembic upgrade hook before serving routes.
- Current exposed routes are `/` and `/health`.

## Current Structure
- `main.py` owns app creation, startup hook, and current scaffold routes.
- `core/config.py` owns server database configuration.
- `core/migrations.py` owns programmatic server Alembic upgrades.
- `routers/` owns transport-level request handling as endpoints are added.
- `schemas/` owns request and response contracts.
- `models/` owns SQLModel persistence models.
- `services/` owns business rules and persistence coordination.

## Command Surface
Run these from `backend/`:

- `uv run uvicorn server.main:app --host 127.0.0.1 --port 8001 --reload`: run the API locally.
- `uv run pytest`: run backend tests.
- `uv run alembic -c alembic.ini upgrade head`: apply all pending migrations to the configured database.
- `uv run alembic -c alembic.ini revision --autogenerate -m "<message>"`: generate a new migration from model changes.

## Validation
Before finishing API changes, run:

- `uv run ruff format --check .`
- `uv run ruff check .`
- `uv run pytest`

For route changes, add endpoint tests for status codes, response shape, validation errors, and expected domain failures.

For model changes, generate and review a server Alembic migration, then run the server upgrade path.

## Architecture
- Keep routers thin: parse input, call typed services, return explicit response models.
- Keep business rules, persistence coordination, and external calls in services.
- Keep persistence shape in models and public contracts in schemas.
- Keep config and startup migration wiring in `core/`.
- Do not import Discord objects or bot handler state into the API server.

## Error Handling And Security
- Map expected domain failures to stable HTTP errors.
- Do not return raw exceptions, stack traces, or persistence objects accidentally.
- Keep authentication and authorization dependencies explicit on protected routes once protection exists.
- Do not describe a route as protected until enforcement and tests exist.

## Data And Migrations
- Server and memory schema history share `backend/alembic.ini` and `backend/alembic/`.
- Keep model, schema, service, router, test, and migration changes aligned.
- Do not rewrite shared or already-applied migration history.
- Keep startup migration behavior deterministic and narrow.
