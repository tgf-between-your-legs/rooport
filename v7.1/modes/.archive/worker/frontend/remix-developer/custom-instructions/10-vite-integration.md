# Vite Integration

## Core Concept: Remix + Vite

Starting with Remix v2, Vite became the default build tool, offering faster development server startup and Hot Module Replacement (HMR).

**Key Aspects:**

*   **Fast Development:** Near-instant HMR and fast cold starts.
*   **Optimized Production Builds:** Uses Rollup for optimized bundles.
*   **Plugin Ecosystem:** Access to Vite's plugin ecosystem.
*   **Configuration:** Managed via `vite.config.ts`.

## Setup

*   New Remix projects (`npx create-remix@latest`) typically use Vite by default.
*   Migration involves installing Vite, `@remix-run/dev`, creating `vite.config.ts`, and updating `package.json` scripts and server entry.

**Key Files:**

*   **`vite.config.ts`:** Main Vite configuration, includes Remix Vite plugin.
*   **`remix.config.js` (Optional):** For some Remix-specific configs (e.g., `future` flags).
*   **`tsconfig.json`:** TypeScript config, often includes path aliases (`~/`).
*   **`package.json`:** Scripts (`dev`, `build`, `start`).

## `vite.config.ts` Example

```typescript
// vite.config.ts
import { vitePlugin as remix } from "@remix-run/dev";
import { installGlobals } from "@remix-run/node"; // Or your adapter
import { defineConfig } from "vite";
import tsconfigPaths from "vite-tsconfig-paths";

installGlobals(); // Polyfills Web APIs for Node

export default defineConfig({
  plugins: [
    remix({
      // future: { /* ... future flags ... */ },
    }),
    tsconfigPaths(), // Handles tsconfig path aliases like '~/'
  ],
  // server: { port: 3000 }, // Optional server config
});
```

*   **`@remix-run/dev`:** Provides the `remix()` Vite plugin.
*   **`installGlobals()`:** Polyfills necessary Web APIs for the server environment.
*   **`tsconfigPaths()`:** Useful for resolving path aliases.

## Development & Build

*   **Development:** `npm run dev` starts the Vite dev server (fast HMR).
*   **Build:** `npm run build` runs `vite build` (client) and `vite build --ssr` (server). Output typically in `build/client` and `build/server`.
*   **Run Production:** `npm run start` runs the production server (e.g., Node adapter) serving built assets.

## Server Entry (`server.js` or `server.ts`)

*   Handles serving static assets and rendering the app using the server build.
*   Implementation depends heavily on the chosen adapter (Node, Vercel, Cloudflare, etc.). Consult Remix docs for adapter-specific setup with Vite.

## Key Differences from Classic Compiler

*   **Build Tool:** Vite + Rollup vs. esbuild.
*   **Dev Server:** Vite dev server vs. Remix App Server.
*   **HMR:** Generally faster/more reliable.
*   **Configuration:** Primarily `vite.config.ts`.
*   **Environment Variables:** Uses Vite's `import.meta.env` (`VITE_` prefix for client exposure).

*(Combined from `remix-vite-integration.md` and `vite-integration.md`)*