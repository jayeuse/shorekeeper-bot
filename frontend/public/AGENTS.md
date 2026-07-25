# Public Asset Guidelines

- Files here are served unchanged from the site root; reference them with absolute paths such as `/icons.svg`.
- Use stable lowercase filenames and avoid secrets, source maps, or machine-specific files.
- Prefer `src/assets/` when an asset should be fingerprinted or transformed by Vite.
- Optimize assets and verify cache-sensitive replacements in the production build.
