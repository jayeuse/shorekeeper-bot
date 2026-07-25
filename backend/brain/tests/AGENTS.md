# Test Guidelines

- Prefer pytest tests named `test_*.py`; retain script-style regressions only where model-backed inspection is intentional.
- Make unit tests deterministic with stubs, monkeypatching, and temporary paths. Do not require network access for unit coverage.
- Add a regression test for every bug fix and cover both success and failure paths.
- Run the unit gate from `backend/` with `uv run pytest`; target a test path while iterating without weakening the committed coverage threshold.
- Name model-backed/manual validations `*_smoke.py` so pytest does not collect them. Document required chat or embedding servers in the module docstring.
- Maintain at least the coverage threshold configured in `backend/pyproject.toml`; raise it as coverage improves.
