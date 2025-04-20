# 6. Using and Configuring Plugins

Extending Vite's functionality with the plugin ecosystem.

## Core Concept: Extending Vite with Plugins

Vite has a powerful plugin API based on Rollup's plugin interface, allowing developers to customize Vite's behavior during development and build time. Plugins can:

*   Add support for custom file types (e.g., `.vue`, `.svelte`).
*   Transform code (e.g., Babel, SWC).
*   Inject scripts or modify HTML (`transformIndexHtml`).
*   Configure the dev server (`configureServer`).
*   Add custom Rollup options for the build.
*   Implement framework-specific features (like HMR for React Fast Refresh).

**Plugin Types:**

*   **Vite Plugins:** Designed specifically for Vite, leveraging Vite-specific hooks (`configureServer`, `transformIndexHtml`, `handleHotUpdate`).
*   **Rollup Plugins:** Many existing Rollup plugins are compatible with Vite's build process (as Vite uses Rollup for builds). Some may need adjustments or a Vite-specific wrapper plugin to work correctly with the dev server.

## Using Plugins

1.  **Install Plugin:** Add the plugin package as a dev dependency.
    ```bash
    npm install -D @vitejs/plugin-react vite-plugin-svgr
    # or
    yarn add -D @vitejs/plugin-react vite-plugin-svgr
    ```
2.  **Import and Add to Config:** Import the plugin factory function in `vite.config.js`/`ts` and add it to the `plugins` array. Pass any necessary options to the factory function.

    ```typescript
    // vite.config.ts
    import { defineConfig } from 'vite';
    import react from '@vitejs/plugin-react'; // Official React plugin
    import svgr from 'vite-plugin-svgr'; // Example: Load SVGs as React components

    export default defineConfig({
      plugins: [
        // Basic React support (Fast Refresh, JSX)
        react(),

        // Configure SVGR plugin
        svgr({
          // svgr options:
          svgo: true, // Enable SVGO optimization
          svgoConfig: {
            plugins: ['preset-default', 'removeDimensions'],
          },
          // esbuild options:
          esbuildOptions: {
            // ...
          },
          // include: "**/*.svg?react", // Default: only process SVGs imported with ?react
          // exclude: "",
        }),

        // Add other plugins...
      ],
      // ... other Vite config
    });
    ```

## Common Plugin Categories & Examples

*   **Framework Integration:**
    *   `@vitejs/plugin-react`: Adds React Fast Refresh (HMR) and automatic JSX runtime.
    *   `@vitejs/plugin-vue`: Adds Vue SFC support.
    *   `@vitejs/plugin-vue-jsx`: Adds Vue JSX support.
    *   `@sveltejs/vite-plugin-svelte`: Adds Svelte support (used by SvelteKit).
*   **Asset Handling:**
    *   `vite-plugin-svgr`: Load SVG files as React components.
    *   `vite-imagetools`: Transform and optimize images during build.
*   **Code Transformation:**
    *   `@vitejs/plugin-legacy`: Generate legacy chunks and polyfills for older browser support.
    *   Plugins for Babel or SWC (though Vite uses esbuild by default for TS/JSX).
*   **Linting/Formatting:**
    *   `vite-plugin-eslint`: Integrate ESLint into the dev server/build.
*   **Backend Integration:**
    *   Plugins for specific backend frameworks (Laravel, Ruby on Rails) to integrate Vite's manifest and asset handling.
*   **Other Utilities:**
    *   `vite-tsconfig-paths`: Resolve path aliases defined in `tsconfig.json`.
    *   `vite-plugin-mkcert`: Automatically generate trusted HTTPS certificates for local development.

## Plugin Order (`enforce`)

Sometimes, the order in which plugins are applied matters. You can influence this using the `enforce` property on a plugin object:

*   `enforce: 'pre'`: Apply this plugin *before* core Vite plugins.
*   (No enforce): Apply after core Vite plugins (default).
*   `enforce: 'post'`: Apply *after* build plugins.

```typescript
// vite.config.ts
import myPrePlugin from 'my-pre-plugin';
import myPostPlugin from 'my-post-plugin';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [
    { ...myPrePlugin(), enforce: 'pre' }, // Runs first
    react(), // Runs after pre, before post
    { ...myPostPlugin(), enforce: 'post' }, // Runs last
  ],
});
```

## Conditional Application (`apply`)

You can specify whether a plugin should run only during development (`'serve'`) or only during build (`'build'`).

```typescript
// vite.config.ts
import eslint from 'vite-plugin-eslint';

export default defineConfig({
  plugins: [
    // Only run ESLint during development server
    { ...eslint(), apply: 'serve' },
  ],
});
```

Vite's plugin system, built on Rollup's foundation, provides extensive extensibility. Use official framework plugins for core support and explore the ecosystem for asset handling, code transformation, and other development/build needs. Pay attention to plugin configuration options and potential ordering issues using `enforce`.

*(Refer to the official Vite documentation on Plugins and explore awesome-vite.com for community plugins.)*