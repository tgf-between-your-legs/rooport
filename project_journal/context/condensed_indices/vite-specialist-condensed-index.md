## Vite vUnknown - Condensed Context Index

### Overall Purpose
Vite is a modern frontend build tool and development server designed for speed and an optimal developer experience. It utilizes native ES modules during development for extremely fast Hot Module Replacement (HMR) and bundles applications efficiently for production using Rollup. Vite is framework-agnostic but offers templates and integrations for popular frameworks like Vue, React, Svelte, etc.

### Core Concepts & Capabilities
*   **Build & Dev Server:** Provides a fast development server (`vite`) leveraging native ESM & HMR, and an optimized production build command (`vite build`) using Rollup. Includes a local server (`vite preview`) to test the production build.
*   **Configuration (`vite.config.js`/`ts`):** Uses a central `vite.config.js` or `vite.config.ts` file with the `defineConfig` helper for type safety. Configures server options, build settings, plugins, SSR, optimizations (`optimizeDeps`), environment variables (`define`, `import.meta.env`), module resolution (`resolve`), etc.
*   **Plugin Ecosystem:** Highly extensible via Vite-specific and Rollup-compatible plugins configured in the `plugins` array. Supports hooks like `configureServer`, `resolveId`, `load`, and conditional application (`apply: 'build' | 'serve'`). Enables creation of virtual modules.
*   **Module Handling:** Natively supports ES module syntax (`import`/`export`). Resolves bare module imports (e.g., `import React from 'react'`). Supports CSS Modules (`.module.css`), glob imports (`import.meta.glob`), dynamic imports, and JSON imports. Provides an HMR API (`import.meta.hot`).
*   **Asset Management:** Handles static assets (importing returns URL), CSS imports/processing (including preprocessors like Sass/Less if installed), and Web Workers (via `?worker`, `?sharedworker`, `?worker&inline` suffixes).
*   **Server-Side Rendering (SSR):** Offers built-in support for SSR development and builds. Key features include dev server middleware mode (`server.middlewareMode`), programmatic APIs like `ssrLoadModule` and `transformIndexHtml`, and SSR-specific configuration options.
*   **Multi-Environment Support:** Advanced feature (`environments` config) allowing distinct configurations for different runtime targets (e.g., `client`, `ssr`, `edge`, custom like `workerd`) within one project.
*   **Performance:** Focuses on speed through native ESM dev server, dependency pre-bundling (`optimizeDeps`), and features like server warmup (`server.warmup`).

### Key APIs / Components / Configuration / Patterns
*   `npm create vite@latest [app-name] [--template <template>]`: Scaffolds a new Vite project (e.g., `--template vue`).
*   `vite.config.js` / `vite.config.ts`: Primary configuration file location.
*   `defineConfig({...})`: Helper function for type-safe configuration.
*   `vite`: CLI command; starts the development server.
*   `vite build`: CLI command; bundles the application for production.
*   `vite preview`: CLI command; serves the production build locally.
*   `plugins: [...]`: Config array for adding Vite/Rollup plugins.
*   `server: { proxy: {...}, middlewareMode: true, warmup: {...}, port: ..., host: ... }`: Config section for dev server options.
*   `build: { rollupOptions: {...}, lib: {...}, outDir: 'dist', sourcemap: ..., manifest: ... }`: Config section for build options.
*   `import.meta.glob('./*.js')`: Vite-specific function to import multiple files matching a pattern.
*   `import.meta.env.VITE_VAR_NAME`: Accessing client-exposed environment variables (must start with `VITE_`).
*   `import.meta.hot`: HMR API object (`accept()`, `data`, `dispose()`, `invalidate()`) available in dev. Use `if (import.meta.hot)` guard.
*   `createServer({...})` (from 'vite'): Programmatic API to create/control a Vite dev server instance.
*   `build({...})` (from 'vite'): Programmatic API to trigger/configure the build process.
*   `ssrLoadModule(url)`: Server API (on `ViteDevServer`) to load a module in SSR context.
*   `transformIndexHtml(url, html)`: Server API (on `ViteDevServer`) to apply HTML transformations.
*   `environments: { client: {...}, ssr: {...} }`: Config option for defining distinct runtime environment configurations.
*   `resolve: { alias: {...}, conditions: [...] }`: Config section for module resolution (aliases, conditional exports).
*   `optimizeDeps: { include: [...], exclude: [...] }`: Config section for dependency pre-bundling control.
*   Asset Imports: `import assetUrl from './asset.png'`, `import Worker from './script.js?worker'`.
*   CSS Modules: `import styles from './styles.module.css'`.

### Common Patterns & Best Practices / Pitfalls
*   **HMR API Guard:** Always wrap `import.meta.hot` usage in `if (import.meta.hot) { ... }` for production tree-shaking.
*   **Environment Variables:** Prefix client-exposed variables with `VITE_` in `.env` files. Non-prefixed variables are only available server-side (e.g., in `vite.config.js` or during SSR).
*   **SSR Integration:** Use `server.middlewareMode: true` and `appType: 'custom'` when integrating Vite's dev server into a custom Node.js server (like Express). Manually handle HTML serving, `transformIndexHtml`, and `ssrLoadModule` calls.
*   **Plugin Application:** Use `apply: 'build' | 'serve'` within a plugin object to control when it runs.
*   **Monorepo/Linked Deps:** List linked dependencies in `optimizeDeps.include` and potentially `build.commonjsOptions.include` for correct handling.
*   **Virtual Modules:** Use `resolveId` and `load` plugin hooks, often prefixing the virtual ID with `\0` in `resolveId`'s return value.

---
This index summarizes the core concepts, APIs, and patterns for Vite (Version Unknown) based on the provided source snippets. Consult the full official Vite documentation (vitejs.dev) for exhaustive details. Source: `project_journal/context/source_docs/vite-specialist-llms-context-20250406.md`