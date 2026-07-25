# Frontend Guide

## Scope

This guide applies to `frontend/`.

Read this file first for frontend work, then read the closest local guide:

- `src/AGENTS.md` for application source, CSS, tests, and setup files.
- `src/assets/AGENTS.md` for assets imported and fingerprinted by Vite.
- `public/AGENTS.md` for files served unchanged from the site root.

## Stack And Runtime

- Framework/runtime: React 19 with TypeScript, Vite, and TailwindCSS v4.
- Package manager: npm with `package-lock.json`; install with `npm ci`.
- Routing/server-state dependencies: TanStack Router and React Query are available; prefer them over ad hoc routing or fetch-state machinery when that behavior is needed.
- Test stack: Vitest, jsdom, Testing Library, `@testing-library/user-event`, and `@testing-library/jest-dom`.
- Quality tools: Prettier, ESLint flat config, TypeScript build, Vitest coverage, and Vite production build.

## Current Structure

- `src/main.tsx` owns React startup and root mounting.
- `src/App.tsx` and `src/App.css` own the current app shell.
- `src/index.css` owns global styles.
- `src/setupTests.ts` owns Testing Library setup.
- `src/**/*.test.tsx` and `src/**/*.test.ts` own frontend tests.
- `src/assets/` contains assets imported by application code.
- `public/` contains static passthrough assets referenced by absolute paths.
- `dist/` and `coverage/` are generated outputs; do not edit them manually.

## Command Surface

Run these from `frontend/`:

- `npm ci`: install locked dependencies.
- `pre-commit install --config .pre-commit-config.yaml --hook-type pre-commit`:
  install the local frontend hook set.
- `pre-commit run --config .pre-commit-config.yaml --all-files`: run the full frontend
  hook set manually.
- `npm run dev`: start Vite development mode.
- `npm run format:check`: verify Prettier formatting.
- `npm run lint`: run ESLint with `--max-warnings=0`.
- `npm run test`: run Vitest once.
- `npm run test:coverage`: run Vitest coverage with configured thresholds.
- `npm run build`: run TypeScript project build and Vite production build.
- `npm run audit`: audit dependencies.
- `npm run check`: run format, lint, coverage, and production build.
- `npm run preview`: preview the production build.

## Validation

Before finishing frontend changes, run:

- `npm run audit`
- `npm run check`

The committed frontend pre-commit config runs Prettier, ESLint, Vitest coverage, and
the production build on `pre-commit` so commits exercise the same durable validation
gate expected before finishing work.

For visible UI changes, also inspect the affected route or component in a browser and check loading, error, keyboard, focus, and responsive states where relevant.

If a command cannot run because dependencies are missing or network access is blocked, state the exact blocker and remaining risk.

## Architecture

- Keep route-level composition and app wiring in focused components; move repeated UI into reusable components when duplication appears.
- Keep server state in React Query when remote data is introduced; keep local presentation state in React hooks.
- Keep reusable hooks named `use*`, with one responsibility and symmetrical effect setup/cleanup.
- Keep shared utilities deterministic and side-effect light.
- Keep static files in `public/` only when Vite should not transform them; otherwise import assets from `src/assets/`.

## TypeScript And Linting

- TypeScript is strict; avoid `any`, unused declarations, and unchecked side-effect imports.
- Use `PascalCase` component names and files for components, and camelCase hooks and helpers.
- Follow `eslint.config.js`; it combines recommended JS, TypeScript, React Hooks, and React Refresh rules.
- Avoid unrelated formatting churn. Use `npm run format` only when intentional.

## Testing Standards

- Prefer user-visible Testing Library assertions over implementation details.
- Use `userEvent` for interactions.
- Mock network boundaries and timers when needed so tests stay deterministic.
- Keep coverage thresholds in `vite.config.ts` passing for branches, functions, lines, and statements.
- Add or update tests when behavior, accessibility, routing, data loading, or error handling changes.

## Accessibility And UI

- Use semantic HTML, accessible names, useful alt text, and visible focus states.
- Preserve keyboard behavior for interactive controls.
- Utilize TailwindCSS utility classes exclusively for all UI additions, modifications, and layout adjustments. Avoid writing custom CSS in component style sheets or `App.css` unless extending Tailwind's base/theme classes in `index.css`.
- Keep text responsive and prevent button, card, and layout overflow at small and wide viewports.
- Include screenshots or a short visual note in PRs for user-visible changes.
