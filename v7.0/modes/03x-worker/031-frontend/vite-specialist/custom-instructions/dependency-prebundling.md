# Vite: Dependency Pre-Bundling (`optimizeDeps`)

Understanding how and why Vite pre-bundles dependencies using esbuild.

## Core Concept

Vite's dev server serves source code over native ESM. However, dependencies from `node_modules` present two challenges:

1.  **Compatibility:** Many dependencies are published as CommonJS (CJS) modules, which the browser doesn't understand natively.
2.  **Performance:** Large dependencies with many internal modules (e.g., `lodash-es`) can lead to a cascade of hundreds of HTTP requests when loaded via native ESM, slowing down page load significantly during development.

Vite addresses this with **dependency pre-bundling**. Before starting the dev server, Vite scans your source code, discovers imported dependencies, and uses **esbuild** to:

*   Convert CommonJS dependencies to ESM.
*   Bundle dependencies with many internal modules into single (or fewer) ESM modules.

This results in faster page loads and improved compatibility during development.

## How it Works

1.  **Discovery:** Vite crawls your source code (`src/**/*.js`, `src/**/*.ts`, etc., plus HTML entry points) to find bare module imports (e.g., `import React from 'react'`).
2.  **Pre-Bundling with esbuild:** Vite uses the extremely fast `esbuild` bundler to process the discovered dependencies.
3.  **Caching:** The pre-bundled dependencies are cached in `node_modules/.vite/deps`. Vite checks if dependencies or configuration have changed and only re-bundles if necessary, making subsequent server starts very fast.
4.  **Serving:** When the browser requests a dependency (e.g., `/node_modules/.vite/deps/react.js`), Vite serves the pre-bundled ESM version from the cache.

## Configuration (`vite.config.js`/`ts`)

*   **`optimizeDeps` Options:** Fine-tune the pre-bundling process.
    *   `include`: (string[]) Force pre-bundling for specific dependencies that might not be automatically discovered (e.g., dynamically imported libraries, linked monorepo packages). Also useful if a dependency uses non-standard entry points.
    *   `exclude`: (string[]) Prevent specific dependencies from being pre-bundled. Useful if Vite's automatic bundling causes issues or if you want to debug the original dependency code.
    *   `esbuildOptions`: Pass custom options directly to esbuild during pre-bundling.
    *   `force`: (boolean) Force dependency re-bundling, ignoring the cache (useful for debugging or after clearing `node_modules/.vite`). Can also be triggered via `vite --force` or `vite dev --force`.

```typescript
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  optimizeDeps: {
    include: [
      // Force pre-bundling for a dependency that might be missed
      'some-optional-dependency > nested-dependency',
      // Force pre-bundling for linked monorepo packages
      '@my-workspace/shared-ui',
    ],
    exclude: [
      // Exclude a dependency if pre-bundling causes issues
      'problematic-dependency',
    ],
    // esbuildOptions: {
    //   // Example: Target a specific JS version for bundled deps
    //   target: 'es2020',
    // }
  },
  // ... other config
});
```

## When to Configure `optimizeDeps`

You usually **don't need** to configure `optimizeDeps` extensively, as Vite's automatic discovery works well most of the time. Common scenarios where manual configuration might be needed:

*   **Monorepos:** Linked packages (`npm link`, `yarn link`, pnpm workspaces) might need to be explicitly included in `optimizeDeps.include`.
*   **Dynamic Imports:** If dependencies are only imported via dynamic `import()` and not discoverable via static analysis, they might need to be included.
*   **Plugin Dependencies:** Dependencies used only within Vite plugins might need to be included.
*   **Bundling Issues:** If a dependency doesn't work correctly after pre-bundling, try adding it to `optimizeDeps.exclude`.
*   **Debugging:** Use `vite --force` or `optimizeDeps.force: true` to force re-bundling if you suspect caching issues.

*(Refer to the official Vite Dependency Pre-Bundling documentation: https://vitejs.dev/guide/dep-pre-bundling.html and `optimizeDeps` options: https://vitejs.dev/config/dep-optimization-options.html)*