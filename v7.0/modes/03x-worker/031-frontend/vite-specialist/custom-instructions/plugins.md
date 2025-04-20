# Vite: Plugins

Extending Vite's functionality using its plugin system (which is based on Rollup's plugin interface).

## Core Concept

Vite's plugin system allows developers to customize the build process and development server behavior. Plugins can transform code, handle specific file types, modify resolved module IDs, inject code, manage assets, and much more. Vite plugins are largely compatible with Rollup plugins (especially those following the unified hooks standard), but Vite also provides some specific hooks.

## Using Plugins

1.  **Install:** Install the plugin package (e.g., `npm install -D @vitejs/plugin-react`).
2.  **Configure:** Import the plugin factory function and add it to the `plugins` array in `vite.config.js` or `vite.config.ts`.

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react'; // Official React plugin
import svgr from 'vite-plugin-svgr'; // Example community plugin

export default defineConfig({
  plugins: [
    // Official React plugin with options
    react({
      // Options like Babel configuration can go here
    }),
    // Community plugin to handle SVGs as React components
    svgr({
      // svgr options
      svgrOptions: {
        // ...
      },
    }),
    // Add other Vite or compatible Rollup plugins
  ],
  // ... other Vite config
});
```

## Common Official Plugins (`@vitejs/`)

*   **`@vitejs/plugin-react`:** Provides React Fast Refresh (HMR) and automatic JSX runtime.
*   **`@vitejs/plugin-vue`:** Provides Vue 3 SFC support and HMR.
*   **`@vitejs/plugin-vue-jsx`:** Provides Vue 3 JSX support.
*   **`@vitejs/plugin-legacy`:** Generates legacy chunks for older browsers that don't support native ESM (often uses Babel and SystemJS).

## Finding Plugins

*   **Awesome Vite:** A curated list of Vite resources, including many plugins: [https://github.com/vitejs/awesome-vite#plugins](https://github.com/vitejs/awesome-vite#plugins)
*   **NPM Search:** Search for packages tagged with `vite-plugin` or `rollup-plugin`.

## Plugin Hooks (Simplified Overview)

Plugins work by implementing specific "hooks" that Vite calls at different stages of the build or dev server lifecycle.

*   **Server Hooks (Vite Specific):**
    *   `configureServer`: Modify the dev server instance (e.g., add middleware).
    *   `transformIndexHtml`: Modify the main `index.html` file.
    *   `handleHotUpdate`: Custom HMR handling.
*   **Build Hooks (Mostly Rollup Compatible):**
    *   `resolveId`: Customize how module import specifiers are resolved to file paths.
    *   `load`: Load the content of a module given its ID.
    *   `transform`: Transform the code of a module (e.g., Babel, TypeScript compilation).
    *   `buildStart` / `buildEnd`: Run logic at the start/end of the build.
    *   `generateBundle` / `writeBundle`: Modify the output bundle before/after writing to disk.
*   **Universal Hooks:**
    *   `config`: Modify the Vite configuration before it's resolved.
    *   `configResolved`: Access the resolved Vite configuration.

## Key Considerations

*   **Compatibility:** While many Rollup plugins work, Vite-specific hooks (`configureServer`, etc.) are only available in Vite plugins. Check plugin documentation for compatibility.
*   **Order:** The order of plugins in the `plugins` array matters. Plugins are generally applied sequentially. Some plugins have an `enforce` property (`'pre'` or `'post'`) to control their execution order relative to others.
*   **Configuration:** Plugins often accept options. Refer to the specific plugin's documentation for available settings.
*   **Performance:** Too many complex plugins can slow down the build process or dev server.

*(Refer to the official Vite Plugin API documentation: https://vitejs.dev/guide/api-plugin.html)*