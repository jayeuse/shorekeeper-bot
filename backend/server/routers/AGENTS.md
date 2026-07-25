# API Router Guidelines

- Routers translate HTTP requests into typed service calls; keep them thin.
- Declare response models, status codes, dependencies, and expected errors explicitly.
- Validate path and query inputs and never return raw exceptions or persistence objects accidentally.
- Add endpoint tests for authorization, validation, success, and failure paths.

