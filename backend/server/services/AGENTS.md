# API Service Guidelines

- Services own API business rules and coordinate persistence or external providers.
- Keep functions typed and independent of FastAPI response objects where practical.
- Define transaction and error boundaries explicitly; do not swallow failures.
- Unit-test services with controlled dependencies before covering them through routers.

