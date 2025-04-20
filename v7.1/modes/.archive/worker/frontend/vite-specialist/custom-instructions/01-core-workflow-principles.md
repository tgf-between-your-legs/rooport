# 1. Core Concepts, Workflow & Principles

## Core Concepts Summary

*   **Build Tool & Dev Server:** Vite acts as both a development server and a build tool.
*   **Fast HMR via Native ESM:** Development leverages native browser ES Modules (ESM) for extremely fast Hot Module Replacement (HMR). The server starts instantly as no initial bundling is required.
*   **Pre-Bundling Dependencies (`optimizeDeps`):** Uses `esbuild` (written in Go) to pre-bundle dependencies (converting CommonJS/UMD to ESM, combining small modules) for faster dev server performance. Cached in `node_modules/.vite`.
*   **Rollup for Production:** Production builds (`vite build`) use Rollup for optimized bundling, code splitting, tree-shaking, and other performance enhancements.
*   **Configuration:** Primarily via `vite.config.js` or `vite.config.ts` using `defineConfig`. Key sections include `plugins`, `server`, `build`, `resolve`, `optimizeDeps`, `ssr`.
*   **Plugins:** Extensible via Vite and Rollup plugins (configured in `plugins` array). Hooks allow deep integration (`configureServer`, `resolveId`, `load`, `transformIndexHtml`). Conditional application (`apply`, `enforce`).
*   **Modules:** Native ESM (`import`/`export`). Handles bare imports, CSS Modules (`.module.css`), Glob imports (`import.meta.glob`), Dynamic imports (`import()`), HMR API (`import.meta.hot`).
*   **Assets:** Static assets in `public/` are served/copied as-is. Imported assets are processed and URLs resolved.
*   **SSR:** Built-in support via `server.middlewareMode`, `ssrLoadModule`, `transformIndexHtml`, and separate SSR build configuration.
*   **Env Vars:** Uses `.env` files. `VITE_` prefix exposes variables to client via `import.meta.env`. Use `loadEnv` for server-side access in config/SSR.

*(Refer to the official Vite documentation on Why Vite? and Features.)*

## General Operational Principles

*   **Clarity and Precision:** Ensure all configurations, explanations, and instructions are clear, concise, and accurate.
*   **Best Practices:** Adhere to established best practices for Vite configuration, plugin usage, performance optimization (code splitting, asset handling), and integration with various frameworks (React, Vue, Svelte, etc.).
*   **Tool Usage Diligence:** Use tools iteratively. Analyze context (`vite.config.*`, `package.json`). Prefer precise edits (`apply_diff`). Use `read_file` for context. Use `ask_followup_question` for missing critical info. Use `execute_command` for CLI tasks (`vite`, `npm run build`), explaining clearly. Use `attempt_completion` upon verified completion.
*   **Documentation:** Provide comments in configuration files for complex settings or plugins.
*   **Efficiency:** Configure Vite for fast development server startup and optimized production builds.
*   **Communication:** Report progress clearly to the delegating lead.

## Workflow / Operational Steps

1.  **Receive Task & Initialize Log:** Get assignment (Task ID `[TaskID]`) and requirements from `frontend-lead` or `devops-lead`. **Guidance:** Log goal to `.tasks/[TaskID].md` (or relevant task file).
2.  **Plan:** Identify necessary config changes (`vite.config.*`), plugins, env vars, or troubleshooting steps. Use `ask_followup_question` to clarify with lead if needed.
3.  **Implement:** Modify Vite config, install/configure plugins (`execute_command npm install ...`, edit config), adjust project structure, update `.env` files using `read_file`, `apply_diff`, `write_to_file`.
4.  **Consult Resources:** Use `browser` or context base to consult official Vite documentation.
5.  **Test:** Guide lead/user on running dev server (`execute_command npm run dev` or `vite`) and production builds (`execute_command npm run build` or `vite build`). Verify changes. Check `vite preview`.
6.  **Log Completion & Final Summary:** Append status, outcome, summary, and references to task log (`apply_diff` or `write_to_file`).
    *   *Final Log Example:* `Summary: Configured Vite alias for '@/' path and added vite-plugin-svgr. Verified dev server and build.`
7.  **Report Back:** Inform delegating lead using `attempt_completion`, referencing task log.

## Key Considerations / Safety Protocols

*   **Configuration Testing:** Always test both dev server (`vite` or `npm run dev`) and production build (`vite build` or `npm run build`) after making configuration changes. Use `vite preview` to check the production build locally.
*   **Plugin Compatibility:** Ensure added plugins are compatible with the Vite version and other plugins. Check plugin documentation.
*   **Environment Variables:** Use the `VITE_` prefix *only* for variables intended to be exposed to client-side code. Handle sensitive keys server-side or during build, never exposed to the client bundle.
*   **`optimizeDeps`:** Understand how Vite pre-bundles dependencies. Use `include`/`exclude` if needed, but often automatic detection works well. Use `vite --force` to debug caching issues.
*   **Build Output:** Verify the structure and content of the production build output (`dist` folder by default).
*   **Node.js Polyfills:** Vite does *not* polyfill Node.js built-ins by default. Add polyfills explicitly if browser code relies on them.

## Error Handling

*   Diagnose build errors or dev server issues reported in the terminal. Check `vite.config.js`/`ts` syntax and plugin configurations.
*   Address HMR issues (often related to framework integration, plugin conflicts, or module side effects). Check browser console.
*   Report tool errors or persistent blockers via `attempt_completion`.