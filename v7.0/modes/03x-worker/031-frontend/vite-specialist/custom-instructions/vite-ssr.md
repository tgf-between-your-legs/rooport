# Vite: Server-Side Rendering (SSR)

Configuring and understanding Vite's built-in support for Server-Side Rendering.

## Core Concept: Rendering on the Server

SSR involves rendering your application's components (React, Vue, Svelte, etc.) into an HTML string on the server for the initial request. This HTML is sent to the browser, providing faster perceived load times and better SEO compared to client-side only rendering (CSR) where the browser receives minimal HTML and builds the page using JavaScript.

Vite provides built-in APIs and conventions to support SSR, handling module loading and transformations on the server during development and providing tools for production builds.

**Key Aspects:**

*   **Development:** Vite's dev server can be used as middleware in a Node.js server (like Express, Koa). Vite handles HMR for SSR updates and transforms modules on demand using native ESM.
*   **Production Build:** `vite build` generates two bundles:
    *   **Client Build:** The standard browser bundle (similar to a CSR build).
    *   **SSR Build:** A bundle designed to run in Node.js, exporting a function (e.g., `render`) that takes a URL and returns the rendered HTML string.
*   **Server Entry Point:** You need a server entry file (e.g., `server.js`) that imports the SSR build's `render` function and uses it within a server framework (Express, etc.) to handle incoming requests.
*   **Client Hydration:** After the server-rendered HTML is sent, the client-side JavaScript bundle takes over ("hydrates") the static HTML, making it interactive.

## Configuration (`vite.config.js`/`ts`)

*   **`server.middlewareMode`:** Set to `true` when using Vite's dev server as middleware in a custom Node.js server. This disables Vite's own HTML serving logic.
*   **`ssr` Options:**
    *   `ssr.entry`: Specifies the entry point for the SSR build (e.g., `src/entry-server.jsx`).
    *   `ssr.noExternal`: List dependencies that should *not* be externalized in the SSR build (force them to be bundled). Useful for CSS or components that need processing by Vite/Rollup plugins. By default, most `node_modules` are externalized for faster builds.
    *   `ssr.external`: Explicitly list dependencies to externalize.
    *   `ssr.target`: Target environment for the SSR build (`'node'` or `'webworker'`).
*   **`build.ssr`:** Can be set to `true` or the path to the SSR entry point to trigger an SSR build alongside the client build when running `vite build`.

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: { '@': path.resolve(__dirname, './src') },
  },
  // server: {
  //   // Use if running Vite dev server as middleware
  //   middlewareMode: true,
  // },
  build: {
    // Trigger SSR build alongside client build
    ssr: 'src/entry-server.tsx', // Path to your SSR entry point
    // Other build options...
    outDir: 'dist', // Client build goes here
    // SSR build output is controlled by rollupOptions
    rollupOptions: {
        // Ensure shared dependencies are handled correctly
        // output: {
        //     // ... potentially configure chunks ...
        // }
    }
  },
  ssr: {
    // Dependencies to include in the SSR bundle (not externalized)
    // Example: Component libraries with CSS that needs processing
    noExternal: ['@mui/material', /@react-aria\/.*/],
    // Example: Explicitly externalize a dependency
    // external: ['some-node-native-module'],
    // target: 'node' // Default
  }
});
```

## SSR Entry Point (`src/entry-server.tsx` Example)

This file typically exports a `render` function that takes the request URL and returns the rendered HTML. Framework-specific adapters often provide helpers for this.

```typescript
// src/entry-server.tsx (Example for React with React Router)
import React from 'react';
import ReactDOMServer from 'react-dom/server';
import { StaticRouter } from 'react-router-dom/server';
import App from './App';

export function render(url: string, context: any) { // Context might be passed for data fetching
  const html = ReactDOMServer.renderToString(
    <React.StrictMode>
      <StaticRouter location={url}>
        <App />
      </StaticRouter>
    </React.StrictMode>
  );
  return { html }; // Return HTML and potentially preloaded state
}
```

## Production Server (`server.js` Example)

This Node.js server imports the SSR build and uses it to handle requests.

```javascript
// server.js (Example using Express)
import fs from 'fs';
import path from 'path';
import express from 'express';
import { fileURLToPath } from 'url';
import { createServer as createViteServer } from 'vite';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const isProd = process.env.NODE_ENV === 'production';

async function createServer() {
  const app = express();
  let vite;

  if (!isProd) {
    // Create Vite server in middleware mode (dev)
    vite = await createViteServer({
      server: { middlewareMode: true },
      appType: 'custom' // Don't include Vite's default HTML handling
    });
    // Use vite's connect instance as middleware
    app.use(vite.middlewares);
  } else {
    // Serve static assets from dist/client (prod)
    app.use(express.static(path.resolve(__dirname, 'dist/client'), { index: false }));
  }

  app.use('*', async (req, res, next) => {
    const url = req.originalUrl;

    try {
      let template, render;

      if (!isProd) {
        // 1. Read index.html (dev)
        template = fs.readFileSync(path.resolve(__dirname, 'index.html'), 'utf-8');
        // 2. Apply Vite HTML transforms (injects HMR client, etc.) (dev)
        template = await vite.transformIndexHtml(url, template);
        // 3. Load server entry using Vite's SSR loader (dev)
        render = (await vite.ssrLoadModule('/src/entry-server.tsx')).render;
      } else {
        // 1. Read index.html from dist (prod)
        template = fs.readFileSync(path.resolve(__dirname, 'dist/client/index.html'), 'utf-8');
        // 2. Load server entry from dist/server (prod)
        // Adjust path based on your build output
        render = (await import('./dist/server/entry-server.js')).render;
      }

      // 4. Render the app HTML using the entry's render function
      const context = {}; // Optional context for data fetching
      const { html: appHtml } = await render(url, context); // Pass URL and context

      // 5. Inject the app-rendered HTML into the template
      const html = template.replace(`<!--ssr-outlet-->`, appHtml);

      // 6. Send the rendered HTML back.
      res.status(200).set({ 'Content-Type': 'text/html' }).end(html);
    } catch (e) {
      // If an error is caught, let Vite fix the stack trace so it maps back
      // to your actual source code.
      if (vite) vite.ssrFixStacktrace(e);
      next(e);
    }
  });

  app.listen(5173, () => {
    console.log('Server listening on http://localhost:5173');
  });
}

createServer();
```

Vite provides the core infrastructure for SSR, but implementation details often depend on the specific framework (React, Vue, Svelte) and routing library being used. Framework-specific Vite plugins often simplify SSR setup significantly.

*(Refer to the official Vite documentation on Server-Side Rendering (SSR).)*