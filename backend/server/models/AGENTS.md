# API Model Guidelines

- Define persistence models and relationships here; keep request/response contracts in `schemas/`.
- Use explicit types, constraints, indexes, nullable behavior, and stable table names.
- Pair schema changes with the server Alembic migration tree.
- Avoid embedding request handling or business workflows in model classes.

