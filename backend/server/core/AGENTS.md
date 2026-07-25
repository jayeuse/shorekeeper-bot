# API Core Guidelines

- This directory owns server configuration, startup infrastructure, and migration wiring.
- Resolve repository paths with `pathlib.Path` and load deployable values from environment-backed configuration.
- Startup work must be idempotent, observable, and safe under reload.
- Keep routes and feature business logic out of core infrastructure.

