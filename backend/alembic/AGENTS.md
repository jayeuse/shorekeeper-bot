# Alembic Guide

## Scope
This guide applies to `backend/alembic/`.

Read this file before editing the migration environment or revision files.

## Purpose
`backend/alembic/` owns the unified schema migration history for all backend databases (memory and server). Both databases share one set of migration scripts; each tracks its own applied revision state via its own `alembic_version` table.

## Current Structure
- `env.py` imports all model sets (`database.models`, `server.models`) into a single SQLModel metadata.
- `versions/` contains all revision scripts.
- `../alembic.ini` is the single Alembic configuration file.

## Command Surface
Run these from `backend/`:

- `uv run alembic -c alembic.ini upgrade head`: apply all pending migrations to the configured database.
- `uv run alembic -c alembic.ini revision --autogenerate -m "<message>"`: generate a new migration from model changes.

## Rules
- Add new revision files under `versions/`; never rewrite an applied revision.
- Keep migrations deterministic, reviewable, and compatible with both SQLite and PostgreSQL.
- Use explicit index and constraint names so upgrades and downgrades remain predictable.
- Do not import application runtime code in revision files.

## Validation
After migration changes, run the matching upgrade command from `backend/`.

For model-backed changes, also run:

- `uv run ruff format --check .`
- `uv run ruff check .`
- `uv run pytest`

When practical, test both a clean upgrade to `head` and an upgrade from the previous revision.
