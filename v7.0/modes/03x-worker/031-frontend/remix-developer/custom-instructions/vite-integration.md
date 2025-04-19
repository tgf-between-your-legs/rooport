# Remix + Vite Integration

Notes on using Vite as the build tool and development server for Remix applications.

## Core Concept

Starting with Remix v2, Vite became the default build tool for new projects, replacing the previous Remix compiler. Vite offers significantly faster development server startup and Hot Module Replacement (HMR).

## Setup

*   **New Projects:** Running `npx create-remix@latest` typically sets up a Vite-based project by default.
*   **Existing Projects:** Follow the official Remix migration guide to switch from the classic compiler to Vite. This usually involves:
    *   Installing Vite and the `@remix-run/dev` and `@remix-run/react` packages (if not already latest).
    *   Installing the Remix Vite plugin: `npm install @remix-run/dev --save-dev` (or yarn/pnpm).
    *   Creating/updating `vite.config.ts` (or `.js`).
    *   Updating `package.json` scripts (`dev`, `build`, `start`).
    *   Adjusting server entry point (`server.js` or `server.ts`).
    *   Potentially updating `remix.config.js` (though many options move to `vite.config.ts`).

## `vite.config.ts`

The main configuration happens here.

```typescript
import { vitePlugin as remix } from "@remix-run/dev";
import { installGlobals } from "@remix-run/node"; // Or your adapter
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";

installGlobals(); // Polyfills Web APIs for Node environment

export default defineConfig({
  plugins: [
    remix({
      // appDirectory: "app", // Default
      // routes(defineRoutes) { // Optional: Define routes programmatically
      //   return defineRoutes((route) => {
      //     route("/", "routes/home.tsx", { index: true });
      //   });
      // },
      // future: { // Enable future flags
      //   v3_fetcherPersist: true,
      //   v3_relativeSplatPath: true,
      //   v3_throwAbortReason: true,
      // },
    }),
    tsconfigPaths(), // Allows using paths defined in tsconfig.json (e.g., "~/")
  ],
  // Optional: Server configuration (port, etc.)
  // server: {
  //   port: 3000,
  // },
  // Optional: SSR specific options
  // ssr: {
  //   noExternal: [/^@acme\/.*/], // Example: Force bundling specific deps
  // }
});
```

*   **`@remix-run/dev`:** Provides the `remix()` Vite plugin.
*   **`installGlobals()`:** Polyfills necessary Web APIs (like `fetch`, `Request`, `Response`) when running in a Node.js environment. Import from your chosen adapter (`@remix-run/node`, `@remix-run/cloudflare`, etc.).
*   **`tsconfigPaths()`:** Useful plugin for resolving path aliases defined in `tsconfig.json`.
*   **Plugin Options:** The `remix()` plugin accepts options, including enabling `future` flags for upcoming Remix features.

## Development (`npm run dev`)

*   Starts the Vite development server.
*   Provides fast HMR for CSS, components, and sometimes even loaders/actions (depending on the change).
*   Server-side code (`loader`/`action`) changes often trigger a server restart, but it's usually very fast with Vite.

## Build (`npm run build`)

*   Vite performs two builds:
    1.  **Client Build:** Creates optimized bundles for the browser.
    2.  **Server Build:** Creates bundles for the server environment (Node.js, Cloudflare Workers, etc.).
*   Output is typically placed in `build/client` and `build/server`.

## Server Entry (`server.js` or `server.ts`)

*   When using Vite, the custom Remix server entry point becomes more important, especially for production builds or custom server logic.
*   It needs to handle serving static assets from the client build and rendering the application using the server build.
*   The exact implementation depends heavily on the chosen adapter (Node, Vercel, Cloudflare, etc.). Consult the Remix documentation for adapter-specific server setup with Vite.

**Example (Node Adapter - Simplified):**
```typescript
import path from "node:path";
import express from "express";
import { createRequestHandler } from "@remix-run/express"; // Adapter specific
import { installGlobals } from "@remix-run/node";

installGlobals();

const viteDevServer =
  process.env.NODE_ENV === "production"
    ? undefined
    : await import("vite").then((vite) =>
        vite.createServer({
          server: { middlewareMode: true },
        })
      );

const app = express();

// Handle asset requests in development
if (viteDevServer) {
  app.use(viteDevServer.middlewares);
} else {
  // Serve static assets in production
  app.use(
    "/assets",
    express.static(path.join(__dirname, "../build/client/assets"), { immutable: true, maxAge: "1y" })
  );
  app.use(express.static(path.join(__dirname, "../build/client"), { maxAge: "1h" }));
}

// Remix request handler
app.all(
  "*",
  createRequestHandler({
    // The server build path may differ depending on project setup
    build: viteDevServer
      ? () => viteDevServer.ssrLoadModule("virtual:remix/server-build")
      : // Adjust path as needed for production build
        await import("../build/server/index.js"),
  })
);


const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Express server listening on port ${port}`));

```

## Key Differences from Classic Compiler

*   **Build Speed:** Vite is significantly faster for development builds and HMR.
*   **Configuration:** Configuration moves primarily to `vite.config.ts`. `remix.config.js` is less used or simplified.
*   **Server Entry:** More explicit server setup might be required depending on the adapter.
*   **HMR:** Generally more reliable and faster HMR.

*(Refer to the official Remix Vite documentation: https://remix.run/docs/en/main/future/vite)*