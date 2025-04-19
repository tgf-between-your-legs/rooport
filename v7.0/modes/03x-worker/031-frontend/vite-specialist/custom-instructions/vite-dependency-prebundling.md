# Vite: Dependency Pre-Bundling (`optimizeDeps`)

Understanding how and why Vite pre-bundles dependencies using esbuild.

## Core Concept: Optimizing for Native ESM Dev Server

Vite's dev server uses native browser ES Modules (ESM). However, dependencies in `node_modules` often present two challenges for this approach:

1.  **Format Compatibility:** Many older packages are published only in CommonJS (CJS) or UMD formats, which browsers don't understand natively.
2.  **Request Waterfall:** Modern packages written in ESM might consist of many small internal modules. Importing such a package could lead to a cascade of hundreds of HTTP requests as the browser discovers nested imports, significantly slowing down page load during development.

**Vite's Solution: Pre-Bundling with esbuild**

Before starting the dev server, Vite scans your source code, discovers bare module imports (like `import React from 'react'`), and uses **esbuild** to pre-bundle these dependencies.

**Benefits:**

*   **CJS/UMD to ESM Conversion:** esbuild converts CommonJS and UMD dependencies into native ESM, making them usable by Vite's dev server.
*   **Performance:** esbuild bundles dependencies with many internal modules into fewer, larger ESM chunks. This drastically reduces the number of browser requests needed, preventing the network waterfall issue and improving dev server load times.
*   **Speed:** esbuild is written in Go and performs bundling much faster (10-100x) than JavaScript-based bundlers like Webpack or Rollup.

## How it Works

1.  **Discovery:** Vite crawls your source code (`.html`, `.js`, `.ts`, `.jsx`, `.tsx`, `.vue`, `.svelte`, etc.) to find bare module imports.
2.  **Analysis:** It analyzes the dependencies to determine which need pre-bundling (CommonJS/UMD format or many internal modules).
3.  **Pre-Bundling:** esbuild bundles the identified dependencies into ESM chunks.
4.  **Caching:** The results are cached in `node_modules/.vite`. On subsequent server starts, Vite checks if dependencies or relevant config have changed. If not, it reuses the cached bundles, making startup almost instantaneous.
5.  **Rewriting Imports:** During development, Vite intercepts browser requests for bare module imports and rewrites them to point to the appropriate pre-bundled chunk in the `.vite` cache (e.g., `/node_modules/.vite/deps/react.js?v=xxxx`).

## Configuration (`optimizeDeps` in `vite.config.js`)

While Vite's automatic dependency scanning usually works well, you can fine-tune the behavior using the `optimizeDeps` option:

```typescript
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  optimizeDeps: {
    // --- include ---
    // Force pre-bundling for specific packages that might not be automatically detected
    // (e.g., if imported dynamically or via non-standard means).
    // Also useful for packages with optional peer dependencies that Vite might exclude.
    include: [
      'lodash-es',
      'my-ui-library/dist/components', // Example: Include specific sub-path
      '@headlessui/react > react', // Example: Include nested dependency
    ],

    // --- exclude ---
    // Prevent specific dependencies from being pre-bundled.
    // Useful if Vite's automatic bundling causes issues with a particular library,
    // or if a dependency is intended to be loaded differently (e.g., via CDN).
    exclude: [
      'my-local-linked-package', // Often exclude linked local packages during development
      'firebase/app', // Example: If using Firebase via CDN script
    ],

    // --- esbuildOptions ---
    // Pass custom options directly to esbuild during pre-bundling.
    // esbuildOptions: {
    //   plugins: [
    //     // Add esbuild plugins if needed (rare)
    //   ],
    //   // target: 'es2020', // Override esbuild target
    // },

    // --- force ---
    // Set to true to force dependency pre-bundling, ignoring the cache.
    // Useful for debugging cache issues. Run `vite --force` or `vite dev --force`.
    // force: false, // Default
  },
  // ... other config
});
```

**When to Use `include`:**

*   The dependency is not automatically discovered (e.g., dynamic `import()` not statically analyzable).
*   A package uses non-standard entry points or conditional exports that confuse Vite.
*   To ensure consistent versions of peer dependencies are bundled.

**When to Use `exclude`:**

*   The dependency causes errors during esbuild pre-bundling.
*   You are linking a local package (`npm link` or yarn/pnpm workspaces) and want to use its source code directly with HMR during development (excluding it prevents pre-bundling).
*   The dependency is loaded externally (e.g., via a `<script>` tag).

Dependency pre-bundling is a key reason for Vite's fast development server performance. While largely automatic, the `optimizeDeps` options provide control for edge cases and troubleshooting.

*(Refer to the official Vite documentation on Dependency Pre-Bundling.)*