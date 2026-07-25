# API Schema Guidelines

- Use Pydantic schemas for external request and response contracts.
- Separate create, update, read, and internal representations when their fields differ.
- Reject unexpected or invalid input deliberately and document optional/default behavior.
- Never expose secrets or internal-only persistence fields in response schemas.

