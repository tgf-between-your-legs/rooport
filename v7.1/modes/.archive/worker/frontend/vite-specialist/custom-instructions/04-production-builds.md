# 4. Production Build Options (`build.*`)

Configuring the production build process (`vite build`) in `vite.config.js`/`ts`.

## Core Concept: Optimizing for Production

While Vite focuses on speed during development, the production build (`vite build`) prioritizes generating optimized, static assets suitable for deployment. Vite uses Rollup under the hood for this process, and the `build` section in the config file allows you to control various aspects of the output.

## Key `build` Options

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  build: {
    // --- Output ---
    outDir: 'dist', // Directory relative to project root for build output. Default: 'dist'
    assetsDir: 'assets', // Directory under outDir for generated assets (JS, CSS, images). Default: 'assets'
    // assetsInlineLimit: 4096, // (bytes) Assets smaller than this are inlined as base64 URIs. Default: 4096 (4 KB)
    emptyOutDir: true, // Clean outDir before building. Default: true (unless outDir is project root or outside root)

    // --- Code Generation & Optimization ---
    target: 'modules', // Browser compatibility target. Default: 'modules' (browsers supporting native ESM). Can be an ES version ('es2020') or array of browser targets.
    minify: 'terser', // Minifier to use. 'terser' (default for prod) or 'esbuild' (faster, less optimized) or false.
    terserOptions: { // Options passed to Terser if minify: 'terser'
      compress: {
        // drop_console: true, // Example: Remove console logs in production
        // keep_fnames: /AbortSignal/, // Example: Preserve specific function names
      },
      // format: {
      //   comments: false, // Remove comments
      // },
    },
    cssCodeSplit: true, // Enable/disable CSS code splitting. Default: true
    // cssMinify: 'lightningcss', // Minifier for CSS. Default: 'lightningcss' if installed, otherwise 'esbuild'. Set to false to disable.
    sourcemap: false, // Generate production source maps? 'inline', 'hidden', or boolean. Default: false
    // manifest: false, // Generate manifest.json for server integration. Default: false (set to true or a filename string)
    // ssrManifest: false, // Generate SSR manifest for server integration. Default: false (set to true or a filename string)

    // --- Advanced (Rollup) ---
    rollupOptions: {
      // Directly configure Rollup options (https://rollupjs.org/configuration-options/)
      input: { // Define multiple entry points for MPA (Multi-Page App)
        main: path.resolve(__dirname, 'index.html'),
        // nested: path.resolve(__dirname, 'nested/index.html'),
      },
      output: {
        // Control output chunk generation
        manualChunks(id) {
          // Example: Create a vendor chunk for node_modules
          if (id.includes('node_modules')) {
            // Group specific large libraries into their own chunks
            // if (id.includes('lodash')) return 'lodash';
            // if (id.includes('react')) return 'react';
            return 'vendor';
          }
        },
        // Customize output filenames
        // entryFileNames: `assets/[name].[hash].js`,
        // chunkFileNames: `assets/[name].[hash].js`,
        // assetFileNames: `assets/[name].[hash].[ext]`,
      },
      // Add Rollup plugins (use Vite plugins where possible)
      // plugins: [ myRollupPlugin() ],
    },

    // --- Library Mode ---
    // lib: { // Configure build as a library (see 11-library-mode.md)
    //   entry: path.resolve(__dirname, 'src/main.ts'),
    //   name: 'MyLib',
    //   formats: ['es', 'umd'], // Output formats
    //   fileName: (format) => `my-lib.${format}.js`,
    // },

    // --- Other ---
    // chunkSizeWarningLimit: 500, // (kB) Limit for chunk size warnings. Default: 500
    // reportCompressedSize: true, // Report compressed size of chunks. Default: true (can slow down large builds)
    // watch: null, // Enable Rollup watcher for rebuilds during build (e.g., for library development). Default: null
  },
  // ... other config
});
```

## Common Use Cases

*   **Changing Output Directory:** Use `build.outDir`.
*   **Configuring Minification:** Use `build.minify` and `build.terserOptions`. Set `minify: false` to disable.
*   **Generating Source Maps:** Set `build.sourcemap: true`.
*   **Code Splitting / Chunking:** Customize `build.rollupOptions.output.manualChunks` for fine-grained control over vendor or feature chunks. Use dynamic `import()` in your code. (See `12-performance.md`)
*   **Multi-Page Applications (MPA):** Define multiple HTML entry points in `build.rollupOptions.input`.
*   **Library Authoring:** Use `build.lib` to build distributable libraries in various formats. (See `11-library-mode.md`)
*   **Browser Compatibility:** Adjust `build.target` for older browser support (may require additional polyfills or the `@vitejs/plugin-legacy`).
*   **Server Integration:** Generate `manifest.json` or `ssrManifest.json` using `build.manifest` or `build.ssrManifest` for frameworks that need to map entry points to generated assets. (See `10-ssr.md`)

The `build` options provide extensive control over the production output, leveraging Rollup's capabilities for optimization, code splitting, and format generation.

*(Refer to the official Vite documentation on Build Options.)*