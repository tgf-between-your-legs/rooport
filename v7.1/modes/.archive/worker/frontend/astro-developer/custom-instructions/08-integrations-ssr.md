# Astro: Integrations, SSR & Middleware

## 1. Integrations

Add features and framework support using Astro Integrations.

**Adding Integrations:**

*   Use `npx astro add [integration-name]` (e.g., `react`, `tailwind`, `node`, `vercel`).
*   This installs dependencies and updates `astro.config.mjs`.

**Configuration (`astro.config.mjs`):**

```javascript
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';
import node from '@astrojs/node'; // Example SSR adapter

export default defineConfig({
  integrations: [
    react(),
    tailwind(),
  ],
  // SSR config below (if needed)
});
```

**Common Types:**
*   **UI Frameworks:** `@astrojs/react`, `@astrojs/vue`, `@astrojs/svelte`, etc.
*   **CSS/Styling:** `@astrojs/tailwind`, `@astrojs/partytown`.
*   **SSR Adapters:** `@astrojs/node`, `@astrojs/vercel`, `@astrojs/netlify`, `@astrojs/cloudflare`.
*   **Site Features:** `@astrojs/sitemap`, `@astrojs/mdx`, `@astrojs/rss`.

## 2. Server-Side Rendering (SSR)

Render pages on the server at request time for dynamic content.

**Enabling SSR:**

1.  **Set `output`:** In `astro.config.mjs`, set `output: 'server'` or `output: 'hybrid'`.
2.  **Add Adapter:** Install and configure an adapter for your deployment platform using `npx astro add [adapter-name]`.

```javascript
// astro.config.mjs (Example with Vercel adapter)
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  output: 'server', // or 'hybrid'
  adapter: vercel(),
  // ... integrations
});
```

**SSR Features:**

*   **Request-Time Rendering:** Pages in `src/pages/` are rendered per request.
*   **`Astro` Global:** Access request-specific info:
    *   `Astro.request`: Standard Request object.
    *   `Astro.params`: Dynamic route parameters.
    *   `Astro.cookies`: Get/set cookies.
    *   `Astro.redirect()`: Server-side redirects.
    *   `Astro.clientAddress`: Request IP.
    *   `Astro.locals`: Data shared from middleware.
*   **API Routes:** `.js`/`.ts` files in `src/pages/` become API endpoints.
*   **Middleware:** Code run before/after rendering.

## 3. API Routes (`src/pages/**/*.js|.ts`)

Create server endpoints.

*   **Implementation:** Export async functions named after HTTP methods (`GET`, `POST`, `PUT`, `DELETE`, `ALL`).
*   **Context:** Function receives `{ request, cookies, params, locals, ... }`.
*   **Response:** Return a standard `Response` object.

```typescript
// src/pages/api/items.ts
import type { APIRoute } from 'astro';

export const GET: APIRoute = async ({ request }) => {
  // Fetch items...
  const items = [{ id: 1, name: 'Item 1' }];
  return new Response(JSON.stringify(items), { status: 200 });
}

export const POST: APIRoute = async ({ request }) => {
  const data = await request.json();
  // Create item...
  return new Response(JSON.stringify({ message: 'Item created' }), { status: 201 });
}
```

## 4. Middleware (`src/middleware.js|.ts`)

Intercept requests to perform actions like auth, logging, or modifying responses.

*   **Implementation:** Export an `onRequest` async function (or use `sequence` for multiple). Receives `context` and `next`.
*   **`context.locals`:** Share data with pages/endpoints (e.g., `context.locals.user = ...`). Must be typed in `src/env.d.ts`.
*   **Control Flow:** Call `await next()` to proceed, or return a `Response` directly to intercept (e.g., redirect).

```typescript
// src/middleware.ts
import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware(async (context, next) => {
  // Example: Attach user data to locals
  // const user = await getUserFromSession(context.cookies.get('session'));
  // context.locals.user = user;

  // Example: Redirect unauthenticated users
  // if (!context.locals.user && context.url.pathname.startsWith('/admin')) {
  //   return context.redirect('/login');
  // }

  const response = await next(); // Call next middleware or page

  // Example: Add custom header
  response.headers.set('X-Handled-By', 'Middleware');
  return response;
});
```

*(Refer to the official Astro Integrations, SSR, API Routes, and Middleware documentation.)*