# Database Persistence Guidelines

- This package owns SQLModel entities, database connections, migrations, and repository operations for conversation memory.
- `models/` holds per-domain model modules (e.g. `models/memory.py` for conversation memory).
- Keep database access behind repository methods; services should not embed SQL or session lifecycle details.
- Store timestamps in UTC and preserve server, channel, and user scope semantics.
- Add indexes for demonstrated query patterns and pair schema changes with Alembic revisions.
- Tests must use temporary databases and cover ranking, scoping, and failure behavior.
