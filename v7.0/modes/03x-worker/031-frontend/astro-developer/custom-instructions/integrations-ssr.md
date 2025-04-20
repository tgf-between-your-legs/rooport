# Astro Integrations & SSR

Guide to adding integrations and configuring Server-Side Rendering (SSR) in Astro.

## Integrations (`astro add`)

*   **Concept:** Astro's official way to add framework integrations (React, Vue, Svelte, Solid, Lit), utility integrations (Tailwind, Partytown), or adapters (Node, Vercel, Netlify).
*   **Command:** Use the Astro CLI: `npx astro add [integration-name]`
    *   *Examples:*
        *   `npx astro add react`
        *   `npx astro add tailwind`
        *   `npx astro add node` (for SSR)
        *   `npx astro add vercel` (for Vercel deployment)
*   **Process:** The command typically handles:
    *   Installing necessary dependencies (`npm`/`yarn`/`pnpm`).
    *   Updating `astro.config.mjs` with the integration import and configuration.
    *   Sometimes adding necessary configuration files (e.g., `tailwind.config.cjs`).
*   **Configuration (`astro.config.mjs`):** Integrations are added to the `integrations` array in the config file.
    ```js
    import { defineConfig } from 'astro/config';
    import react from '@astrojs/react';
    import tailwind from '@astrojs/tailwind';
    import node from '@astrojs/node'; // Example SSR adapter

    // https://astro.build/config
    export default defineConfig({
      integrations: [
        react(),
        tailwind(),
      ],
      // Add output and adapter for SSR
      output: 'server', // or 'hybrid'
      adapter: node({
        mode: 'standalone' // or 'middleware'
      }),
    });
    ```

## Server-Side Rendering (SSR) & Adapters

*   **Default:** Astro builds static HTML (`output: 'static'`).
*   **SSR:** To enable server-side rendering on demand for dynamic routes or personalized content:
    1.  **Set `output`:** Change `output: 'server'` or `output: 'hybrid'` in `astro.config.mjs`.
        *   `'server'`: All pages are server-rendered by default.
        *   `'hybrid'`: Pages are static by default, but individual pages can opt-in to SSR using `export const prerender = false;`.
    2.  **Add an Adapter:** Use `npx astro add [adapter-name]` to add the adapter matching your deployment target (e.g., `node`, `vercel`, `netlify`, `cloudflare`). This configures the `adapter` option in `astro.config.mjs`.
*   **Adapters:** Bridge the gap between Astro and your deployment environment's server runtime. They handle request/response logic. Common adapters:
    *   `@astrojs/node`: For Node.js environments (standalone server or middleware).
    *   `@astrojs/vercel`: For deploying to Vercel (Serverless or Edge functions).
    *   `@astrojs/netlify`: For deploying to Netlify (Edge or Serverless functions).
    *   `@astrojs/cloudflare`: For deploying to Cloudflare Pages/Workers.
*   **SSR Considerations:**
    *   **API Routes:** Create server endpoints by adding files to `src/pages/api/`.
    *   **Dynamic Routes:** Use `[param]` or `[...rest]` syntax in filenames within `src/pages/` for dynamic routing. Access params via `Astro.params`.
    *   **Request Object:** Access request details (headers, method, URL) via the global `Astro` object (`Astro.request`).
    *   **Response Object:** Customize responses (status codes, headers) using `Astro.response` or returning a `Response` object from API routes or pages.

## Middleware (`src/middleware.js` or `.ts`)

*   **Concept:** Functions that run before rendering each page or API route in SSR/hybrid mode. Useful for authentication, redirects, modifying response headers, or injecting data into `Astro.locals`.
*   **Implementation:** Create `src/middleware.js` (or `.ts`) and export an `onRequest` function (or a sequence of functions).
    ```javascript
    // src/middleware.js
    import { defineMiddleware, sequence } from 'astro:middleware';

    const auth = defineMiddleware(async (context, next) => {
      // Example: Check for auth cookie
      const session = context.cookies.get('session')?.value;
      if (!session && !context.url.pathname.startsWith('/login')) {
        return context.redirect('/login'); // Redirect if not logged in
      }
      context.locals.user = session ? { id: '123' } : null; // Pass data to components
      return next(); // Continue to next middleware or page
    });

    const logger = defineMiddleware(async (context, next) => {
      const response = await next();
      console.log(`${context.request.method} ${context.url.pathname} -> ${response.status}`);
      return response;
    });

    export const onRequest = sequence(auth, logger);
    ```
*   **`context` Object:** Provides access to `request`, `cookies`, `url`, `locals`, `redirect`, etc.
*   **`context.locals`:** An object to pass data from middleware to `.astro` components (`Astro.locals`). Must be typed in `src/env.d.ts`.

*(Refer to official Astro docs for Integrations, SSR, Adapters, and Middleware.)*