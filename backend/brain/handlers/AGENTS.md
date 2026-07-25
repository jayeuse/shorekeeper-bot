# Handler Guidelines

- Handlers orchestrate Discord interactions; they must not implement retrieval scoring, persistence queries, or provider-specific protocols.
- Preserve the bot-self check and mention/reply trigger gate before expensive work.
- Keep query classification and context assembly deterministic and testable.
- Sanitize user-facing failures, avoid internal stack traces, and keep replies within Discord limits.
- Add regression tests for routing, classification, context history, and response splitting changes.

