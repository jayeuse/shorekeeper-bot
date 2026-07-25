# Core Runtime Guidelines

- `config.py` owns environment parsing, paths, provider selection, and the system prompt; `bot.py` owns Discord client wiring.
- Validate required configuration early and provide safe defaults only for non-secret local settings.
- Keep constants in `UPPER_SNAKE_CASE` and helper functions private unless they form a deliberate API.
- Do not move message handling, retrieval logic, or provider calls into this layer.

