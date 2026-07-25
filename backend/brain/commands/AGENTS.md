# Maintenance Command Guidelines

- Commands are operator-facing scripts for knowledge validation, index rebuilding, metadata updates, and provider checks.
- Keep scripts idempotent where practical, fail with actionable errors, and print concise progress summaries.
- Resolve paths from the repository structure rather than the caller's current directory.
- Reuse runtime services instead of duplicating retrieval or provider logic.
- Never print secrets or silently overwrite source knowledge.

