# Scripts Guide

## Scope
This guide applies to `scripts/`.

## Purpose
`scripts/` owns repo-level operational helpers that are run directly from a shell.

## Current Files
- `start.sh` starts the local PostgreSQL and SearXNG Docker Compose stacks plus the configured llama.cpp chat and embedding `llama-server` processes from root `.env.local`, then shuts everything down together.

## Belongs Here
- Cross-subsystem startup helpers.
- Local operational checks that are not Python package modules or npm scripts.
- Thin wrappers around repo-owned configuration.

## Does Not Belong Here
- Bot maintenance commands; put those under `backend/brain/commands/`.
- FastAPI application code; put that under `backend/server/`.
- Frontend build, test, or formatting tasks; keep those as npm scripts in `frontend/package.json`.
- Machine-specific paths, tokens, or one-off personal shell snippets.

## Rules
- Use Bash explicitly with `#!/usr/bin/env bash` and `set -euo pipefail` where compatible.
- Resolve the repository root from the script location; do not assume the caller's working directory.
- Validate required executables, files, and environment variables before starting long-running processes.
- Quote variable expansions and preserve exit codes.
- Clean up child processes with traps when scripts launch background work.
- Do not print secrets or embed machine-specific paths when `.env.local` can supply them.
- Keep user-facing output stable enough for humans to diagnose failures.

## Interfaces
- Inputs come from repo files, command arguments, and root `.env.local`.
- `start.sh` resolves model paths, aliases, ports, and llama.cpp tuning from the tracked grouped YAML config files under `config/`.
- Values with spaces in `.env.local` must be quoted because the script sources the file with Bash.
- Keep `.env.example`, `README.md`, and `backend/brain/core/config.py` aligned when launcher environment keys change.

## Validation
After changing shell syntax, run from the repo root:

- `bash -n scripts/start.sh`

After changing `.env.local` parsing or launcher-required variables, also validate with a local `.env.local` present.

After changing the llama.cpp command shape, run the script only when the configured model files and `llama-server` binary are available.

## Known Failure Modes
- Symptom: the launcher exits immediately with a missing variable message.
  Cause: `.env.local` is missing a required runtime key.
  Fix: add the key to `.env.local` and keep `.env.example` updated if the key is required.

- Symptom: sourcing `.env.local` fails around a value containing commas or spaces.
  Cause: the value is not valid Bash assignment syntax.
  Fix: quote values that contain spaces, especially config-file paths or any future free-text values.

- Symptom: the script starts one server but leaves another process running after failure.
  Cause: child process cleanup was changed or a trap no longer preserves the exit path.
  Fix: restore cleanup traps and verify both PIDs are stopped on exit.
