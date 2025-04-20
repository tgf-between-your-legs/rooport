# 3. Dev Server & HMR (Hot Module Replacement)

Understanding Vite's fast development server and its Hot Module Replacement capabilities.

## Core Concept: Native ESM Dev Server

Unlike traditional bundlers (like Webpack in development), Vite leverages native ES modules (ESM) in the browser during development.

*   **No Bundling Needed (Initially):** When you request a module (e.g., your `main.ts`), Vite serves it directly after transforming it (e.g., TS to JS). The browser then requests imported modules via native `import` statements. Vite intercepts these requests and serves the transformed code for each module on demand.
*   **Fast Startup:** This avoids bundling the entire application upfront, leading to significantly faster cold server starts.
*   **On-Demand Compilation:** Modules are compiled only when requested by the browser.

## Hot Module Replacement (HMR)

*   **Concept:** When you edit a file during development, Vite can update the running application *without* requiring a full page reload. It intelligently replaces only the modules that have changed.
*   **Mechanism:**
    1.  Vite maintains a WebSocket connection between the server and the client.
    2.  When a file is edited, Vite precisely identifies which modules are affected by the change.
    3.  It sends update messages to the client via the WebSocket.
    4.  The client-side HMR runtime receives the updated module code and replaces the old module in memory.
    5.  Framework integrations (like `@vitejs/plugin-react` with Fast Refresh or `@vitejs/plugin-vue`) handle updating the UI components or application state accordingly.
*   **Speed:** Because it only updates the changed modules (and potentially their direct importers), HMR is extremely fast, regardless of application size.
*   **State Preservation:** Framework-specific HMR often preserves component state during updates, improving the development experience.
*   **CSS HMR:** CSS changes are injected via `<style>` tags without page reloads and without losing application state.

## Configuration (`vite.config.js`/`ts`)

*   **`server` Options:** Configure the dev server behavior.
    *   `port`: Specify the server port (default: 5173).
    *   `host`: Set to `true` to expose the server on your network IP address.
    *   `open`: Automatically open the app in the browser on server start.
    *   `proxy`: Configure proxies for API requests to avoid CORS issues during development (e.g., proxy `/api` requests to `http://localhost:3000`).
    *   `https`: Configure HTTPS for the dev server.
    *   `hmr`: Advanced HMR options (port, overlay, etc.).
    *   `warmup`: Pre-transform frequently used files on startup. (See `12-performance.md`)
    ```typescript
    // vite.config.ts
    import { defineConfig } from 'vite';

    export default defineConfig({
      server: {
        port: 3000,
        open: true, // Open browser on start
        proxy: {
          // Proxy /api requests to backend server
          '/api': {
            target: 'http://localhost:8000', // Your backend URL
            changeOrigin: true,
            // rewrite: (path) => path.replace(/^\/api/, '') // Optional: remove /api prefix
          }
        }
      },
      // ... other config
    });
    ```

## Troubleshooting HMR

*   **Full Reloads:** If HMR consistently causes full page reloads, check:
    *   **Framework Plugin:** Ensure the correct framework plugin (`@vitejs/plugin-react`, `@vitejs/plugin-vue`, etc.) is installed and configured.
    *   **Root Component Exports:** Ensure components intended for HMR are exported correctly (often default exports, depending on the framework).
    *   **Side Effects:** Code with significant side effects at the module level might break HMR state preservation.
    *   **Console Errors:** Check the browser console for HMR-related errors.
*   **CSS Not Updating:** Ensure CSS files are being imported correctly into your JavaScript/TypeScript modules or included via `<link>` in `index.html`. Check `vite.config.js` for any CSS-related plugin configurations.

Vite's native ESM dev server and fine-grained HMR provide a significantly faster and smoother development experience compared to traditional bundler-based approaches.

*(Refer to the official Vite Dev Server documentation: https://vitejs.dev/config/server-options.html and HMR API: https://vitejs.dev/guide/api-hmr.html)*