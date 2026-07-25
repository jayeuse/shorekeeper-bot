# Application Module Guidelines

- Use this directory for cohesive FastAPI feature packages when a feature spans routers, schemas, services, and models.
- Keep feature boundaries explicit and avoid circular imports between apps.
- Expose only deliberate package APIs from `__init__.py`.
- Do not move shared infrastructure here; it belongs in `core/` or `base/`.

