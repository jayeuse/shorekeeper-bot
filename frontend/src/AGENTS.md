# Frontend Source Guidelines

- Keep components focused, accessible, and typed; extract hooks or modules when state or effects become reusable.
- Use semantic HTML, keyboard-accessible controls, useful alt text, and visible focus states.
- Utilize TailwindCSS utility classes exclusively for all UI and component styling. Avoid adding new CSS files or custom style declarations in `App.css` or component stylesheets.
- Keep server state in React Query and local presentation state in React hooks.
- Co-locate component styling using Tailwind utility classes, preserving global design tokens or base extensions in `index.css`.
- Co-locate tests as `*.test.ts` or `*.test.tsx`. Use Testing Library and `userEvent` to exercise accessible behavior.
- Keep tests deterministic and mock network boundaries. Maintain the coverage thresholds in `vite.config.ts`.
