# API Base Guidelines

- Place shared API abstractions here only when multiple features genuinely need them.
- Keep base classes and protocols small, typed, and independent of concrete feature modules.
- Prefer composition over deep inheritance and avoid catch-all utility modules.
- Add tests for shared behavior because changes here have broad impact.

