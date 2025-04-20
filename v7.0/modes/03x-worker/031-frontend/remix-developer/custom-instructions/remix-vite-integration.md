# Remix: Vite Integration

Using Vite as the build tool and development server for Remix applications.

## Core Concept: Remix + Vite

Starting with Remix v2, Vite became the default build tool and development server, replacing the previous Remix compiler and server. This integration leverages Vite's speed and ecosystem while retaining Remix's core features.

**Key Aspects:**

*   **Fast Development:** Vite provides near-instant Hot Module Replacement (HMR) and fast cold starts using native ES modules during development.
*   **Optimized Production Builds:** Vite uses Rollup under the hood for highly optimized production bundles (code splitting, tree shaking, etc.).
*   **Plugin Ecosystem:** Access to Vite's rich plugin ecosystem for various integrations and transformations.
*   **Configuration:** Managed primarily through `vite.config.ts` (or `.js`).

## Setup

*   New Remix projects created with `npx create-remix@latest` typically use Vite by default.
*   For existing projects, follow the official Remix migration guide.

**Key Files:**

*   **`vite.config.ts`:** The main configuration file for Vite. Includes the Remix Vite plugin.
*   **`remix.config.js` (Optional):** Still used for some Remix-specific configurations not handled by the Vite plugin (e.g., `future` flags, server build path, ignored route files).
*   **`tsconfig.json`:** TypeScript configuration, often includes paths for aliases (`~/`).
*   **`package.json`:** Contains scripts like `dev`, `build`, `start`.

## `vite.config.ts` Example

```typescript
// vite.config.ts
import { vitePlugin as remix } from "@remix-run/dev";
import { installGlobals } from "@remix-run/node";
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths"; // Plugin for handling tsconfig paths like '~/'

// Install Node.js globals for compatibility (needed for some Remix features/packages)
installGlobals();

export default defineConfig({
  plugins: [
    remix({
      // appDirectory: "app", // Default
      // routes(defineRoutes) { // Optional: Define routes programmatically
      //   return defineRoutes((route) => {
      //     route("/", "routes/_index.tsx", { index: true });
      //   });
      // },
      // future: { // Enable future flags from remix.config.js
      //   v3_fetcherPersist: true,
      //   v3_relativeSplatPath: true,
      //   v3_throwAbortReason: true,
      // },
    }),
    tsconfigPaths(), // Add this plugin
  ],
  // Optional: Server configuration (port, etc.)
  // server: {
  //   port: 3000,
  // },
  // Optional: Build configuration
  // build: {
  //   // ...
  // }
});
```

## Development Workflow

*   **Start Dev Server:** `npm run dev` (or `yarn dev`, `pnpm dev`).
*   Vite starts the server, typically on `http://localhost:5173` (or configured port).
*   Benefit from fast HMR for CSS, components, and even loader/action changes in many cases.

## Production Build & Run

1.  **Build:** `npm run build` (or `yarn build`, `pnpm build`).
    *   Runs `vite build` (client bundle) and `vite build --ssr` (server bundle).
    *   Outputs optimized assets to `build/client` and `build/server`.
2.  **Run:** `npm run start` (or `yarn start`, `pnpm start`).
    *   Starts the production Remix server (e.g., using the Node adapter) serving the built assets.

## Key Differences from Classic Remix Compiler

*   **Build Tool:** Vite + Rollup instead of esbuild.
*   **Dev Server:** Vite's dev server instead of Remix App Server.
*   **HMR:** Generally faster and more reliable HMR via Vite.
*   **Configuration:** Primarily `vite.config.ts` instead of just `remix.config.js`.
*   **Environment Variables:** Uses Vite's `import.meta.env` system (variables prefixed with `VITE_` are exposed client-side, others server-only). Remix adapters might provide ways to access server-only variables in loaders/actions via `context`. Check adapter documentation.

Using Vite brings significant development experience improvements to Remix while maintaining its core server-centric architecture and features. Configuration shifts primarily to `vite.config.ts`, leveraging Vite's ecosystem.

*(Refer to the official Remix documentation on Vite.)*