# Vite: Production Builds (`vite build`)

Understanding how Vite builds your application for production using Rollup.

## Core Concept

While Vite uses a native ESM dev server for speed, production builds require optimization for browser compatibility and performance. Vite uses **Rollup** under the hood for its production build process.

## Build Process (`vite build` or `npm run build`)

Running the build command triggers several optimizations:

1.  **Bundling:** Code is bundled into fewer JavaScript chunks using Rollup, reducing the number of HTTP requests needed in production.
2.  **Code Splitting:** Vite automatically splits code based on dynamic imports (`import()`). It also attempts to split vendor code (from `node_modules`) into a separate chunk (`build.rollupOptions.output.manualChunks`).
3.  **Tree Shaking:** Unused code (dead code elimination) is removed from the bundles by Rollup.
4.  **Minification:** JavaScript and CSS code is minified (using Terser for JS and CSSNano for CSS by default) to reduce file size.
5.  **Asset Handling:**
    *   Imported assets (images, fonts) smaller than `build.assetsInlineLimit` are inlined as base64 data URIs.
    *   Larger assets are copied to the output directory (`dist/assets` by default) with hashed filenames for cache busting.
    *   CSS assets are processed, potentially pre-processed (Sass, Less), PostCSS plugins applied, and bundled.
6.  **Preload Directives:** Vite automatically injects `<link rel="modulepreload">` directives into the generated `index.html` for entry chunks and their direct imports, optimizing loading performance.
7.  **Legacy Browser Support (Optional):** If using `@vitejs/plugin-legacy`, separate legacy chunks are generated with necessary polyfills and syntax transformations (via Babel).

## Output Directory (`dist`)

By default, the production build output is placed in the `dist` directory at the project root.

*   **`dist/index.html`:** The main entry point for your application, with script/style tags pointing to the generated bundles.
*   **`dist/assets/`:** Contains JavaScript chunks, CSS files, images, fonts, and other static assets, typically with hashed filenames.

## Configuration (`vite.config.js`/`ts`)

*   **`build` Options:** Control the production build process.
    *   `outDir`: Specify the output directory (default: `dist`).
    *   `assetsDir`: Directory under `outDir` for assets (default: `assets`).
    *   `sourcemap`: Generate source maps for debugging production issues (boolean or `'inline'` or `'hidden'`).
    *   `minify`: Enable/disable minification or specify the minifier (`'terser'` or `'esbuild'`). Default is `'esbuild'` which is faster but Terser can sometimes produce smaller bundles.
    *   `target`: Target browser compatibility (e.g., `'modules'` for native ESM support, or specific ES versions like `'es2015'`). Affects syntax transformations.
    *   `cssCodeSplit`: Enable/disable CSS code splitting (default: `true`).
    *   `rollupOptions`: Directly pass options to the underlying Rollup build process (e.g., for `output.manualChunks`, custom plugins).
    *   `lib`: Configure library mode builds (see `library-mode.md`).
    ```typescript
    // vite.config.ts
    import { defineConfig } from 'vite';

    export default defineConfig({
      build: {
        outDir: 'build', // Change output directory
        sourcemap: true, // Generate source maps
        minify: 'terser', // Use Terser for potentially smaller bundles
        rollupOptions: {
          output: {
            // Example: Create a separate chunk for a large vendor library
            manualChunks: {
              'lodash-es': ['lodash-es'],
            },
          },
        },
      },
      // ... other config
    });
    ```

## Previewing the Build (`vite preview`)

*   After running `vite build`, you can use the `vite preview` command to start a local static web server that serves the files from your `dist` (or configured `build.outDir`) directory.
*   This helps verify that the production build works correctly before deploying.

*(Refer to the official Vite Build documentation: https://vitejs.dev/guide/build.html and Build Options: https://vitejs.dev/config/build-options.html)*