# Vite: Configuration File (`vite.config.js`/`ts`)

Understanding and using the main configuration file for Vite projects.

## Core Concept: Central Configuration

Vite is configured using a `vite.config.js` or `vite.config.ts` file located in the project root. This file exports a configuration object that tells Vite how to behave for both the development server and the production build.

**Key Features:**

*   **ESM Syntax:** The config file uses native Node.js ES module syntax (`import`/`export`).
*   **`defineConfig` Helper:** While optional, it's recommended to wrap your config object in the `defineConfig` helper (imported from `vite`) to get TypeScript IntelliSense and type checking for the configuration options.
*   **Conditional Config:** You can export an async function that returns the config object, allowing you to conditionally set options based on the `command` (`'serve'` or `'build'`) and `mode` (e.g., `'development'`, `'production'`, or custom modes set via `--mode`).
*   **Environment Variables:** Vite automatically loads `.env` files. The config file itself runs in Node.js and has access to `process.env`, but client-side code uses `import.meta.env`.

## Basic Structure

```typescript
// vite.config.ts
import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react'; // Example plugin for React
import path from 'path'; // Node.js path module

// https://vitejs.dev/config/
export default defineConfig(({ command, mode }) => {
  // Load env file based on `mode` in the current working directory.
  // Set the third parameter to '' to load all env regardless of the `VITE_` prefix.
  const env = loadEnv(mode, process.cwd(), '');

  console.log(`Vite command: ${command}, mode: ${mode}`);
  // console.log('Loaded Env:', env); // Be careful logging sensitive vars

  // Conditional config based on command
  const isBuild = command === 'build';

  return {
    // --- Shared Options ---
    plugins: [
      react(), // Example: Add React plugin
      // other plugins...
    ],
    resolve: {
      alias: {
        // Example: Set up '@' alias to src directory
        '@': path.resolve(__dirname, './src'),
      },
      // extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json'] // Default extensions
    },
    // Define global constants (use with caution, prefer env variables)
    // define: {
    //   __APP_VERSION__: JSON.stringify(process.env.npm_package_version),
    // },
    base: env.VITE_BASE_URL || '/', // Base public path (e.g., '/my-app/')

    // --- Server Options (Dev Server) ---
    server: {
      port: 3000, // Dev server port
      // open: true, // Automatically open browser
      // proxy: { // Setup proxy for API requests
      //   '/api': {
      //     target: 'http://localhost:8080',
      //     changeOrigin: true,
      //     rewrite: (path) => path.replace(/^\/api/, ''),
      //   },
      // },
      // host: true, // Expose on network
    },

    // --- Build Options (Production Build) ---
    build: {
      outDir: 'dist', // Output directory
      sourcemap: !isBuild ? 'inline' : false, // Enable source maps only for dev builds
      // Target browser compatibility
      // target: 'modules', // Default: browsers supporting native ESM
      // target: ['es2020', 'edge88', 'firefox78', 'chrome87', 'safari14'],
      minify: isBuild ? 'terser' : false, // Minify only for production builds ('esbuild' is faster but less optimized)
      // terserOptions: { ... }, // Options for Terser minifier
      // rollupOptions: { // Advanced customization via Rollup options
      //   output: {
      //     manualChunks(id) {
      //       if (id.includes('node_modules')) {
      //         return 'vendor'; // Example: Create a vendor chunk
      //       }
      //     }
      //   }
      // },
      // lib: { // Library mode configuration (see vite-library-mode.md)
      //   entry: path.resolve(__dirname, 'src/main.ts'),
      //   name: 'MyLib',
      //   fileName: (format) => `my-lib.${format}.js`
      // },
    },

    // --- Preview Options (vite preview command) ---
    preview: {
      port: 4173, // Port for previewing the production build
      // open: true,
    },

    // --- Dependency Optimization Options ---
    // optimizeDeps: {
    //   include: ['lodash-es'], // Force pre-bundling
    //   exclude: ['my-local-linked-package'], // Exclude from pre-bundling
    // },

    // --- SSR Options ---
    // ssr: { ... }, // See vite-ssr.md

    // --- Worker Options ---
    // worker: { ... },
  };
});
```

## Key Configuration Areas

*   **`plugins`:** Add framework support (React, Vue, Svelte) and other build features.
*   **`resolve.alias`:** Define path aliases for cleaner imports.
*   **`server`:** Configure the development server (port, proxy, HTTPS).
*   **`build`:** Configure the production build (output directory, minification, code splitting via `rollupOptions`, library mode).
*   **`optimizeDeps`:** Fine-tune dependency pre-bundling if needed.
*   **`define`:** Inject global constants (use sparingly).
*   **`base`:** Set the base public path for deployment.

The `vite.config.js`/`ts` file provides extensive options for tailoring Vite to your project's specific needs, from development server behavior to highly optimized production builds. Use `defineConfig` for type safety and leverage conditional configuration based on `command` and `mode`.

*(Refer to the official Vite documentation on Configuring Vite.)*