# Utility Guidelines

- Keep utilities small, dependency-light, and reusable across runtime layers.
- Do not hide domain orchestration or provider behavior in generic helpers.
- Logging must include useful timing and failure context while redacting tokens and sensitive payloads.
- Add tests when a helper performs parsing, transformation, or non-trivial branching.

