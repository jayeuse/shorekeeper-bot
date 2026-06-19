# Local PostgreSQL

A local PostgreSQL instance for Shorekeeper Bot — usable in local mode as an alternative to SQLite or Supabase.

## Prerequisites

Add these to the repo root `.env.local`:

```ini
POSTGRES_DB=shorekeeper
POSTGRES_USER=shorekeeper
POSTGRES_PASSWORD=shorekeeper_dev
```

## Start

```bash
docker compose -f infra/postgres/docker-compose.yml up -d
```

## Stop

```bash
docker compose -f infra/postgres/docker-compose.yml down
```

## Wipe data

```bash
docker compose -f infra/postgres/docker-compose.yml down -v
```

## Use with the bot

Set these in `.env.local`:

```ini
MODE=local
DATABASE_URL=postgresql://shorekeeper:shorekeeper_dev@127.0.0.1:5432/shorekeeper
```

## Adminer

Adminer runs on `http://127.0.0.1:8080`. Log in with server: `db` and the credentials from `.env.local`.
