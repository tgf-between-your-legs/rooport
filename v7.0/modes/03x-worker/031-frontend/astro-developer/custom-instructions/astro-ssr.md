# Astro: Server-Side Rendering (SSR) & Middleware

Enabling and using server-side rendering, API routes, and middleware in Astro.

## Core Concept: SSR vs. SSG

*   **Static Site Generation (SSG - Default):** Astro pre-renders your entire site to static HTML, CSS, and minimal JavaScript during the build process. This is great for performance and SEO for content-heavy sites.
*   **Server-Side Rendering (SSR):** Astro renders pages on the server *at request time*. This allows for dynamic content based on user sessions, database queries, API calls, or request parameters without needing client-side JavaScript for the initial render.
*   **Hybrid Rendering:** Astro also supports `output: 'hybrid'`, where most routes are pre-rendered (SSG), but specific routes can opt-in to server-rendering on demand.

## Enabling SSR

1.  **Set `output` Mode:** In `astro.config.mjs`, change the `output` option from `'static'` (default) to `'server'` or `'hybrid'`.
    ```javascript
    // astro.config.mjs
    import { defineConfig } from 'astro/config';

    export default defineConfig({
      output: 'server', // or 'hybrid'
      // ... other config
    });
    ```
2.  **Add an Adapter:** SSR requires a **runtime adapter** specific to your deployment platform (Node.js standalone, Vercel, Netlify, Cloudflare, etc.). Use `npx astro add <adapter-name>` to install and configure it.
    ```bash
    # Example for standalone Node.js server
    npx astro add node

    # Example for Vercel serverless functions
    npx astro add vercel
    ```
    This updates `astro.config.mjs` with the chosen adapter.
    ```javascript
    // astro.config.mjs (after adding node adapter)
    import { defineConfig } from 'astro/config';
    import node from '@astrojs/node'; // Import adapter

    export default defineConfig({
      output: 'server',
      adapter: node({ // Add adapter configuration
        mode: 'standalone' // or 'middleware'
      }),
      // ...
    });
    ```

## Server-Side Rendering Features

With `output: 'server'` or `'hybrid'`, the following become available:

*   **Request-Time Rendering:** Pages in `src/pages/` are rendered on the server for each incoming request.
*   **`Astro` Global:** Provides request-specific information:
    *   `Astro.request`: Standard Request object (URL, headers, method, body).
    *   `Astro.params`: Dynamic route parameters (e.g., from `[id].astro`).
    *   `Astro.props`: Props passed from `getStaticPaths` (only relevant in `hybrid` mode for pre-rendered dynamic routes).
    *   `Astro.cookies`: Get/set cookies (`Astro.cookies.get('session')`, `Astro.cookies.set('theme', 'dark', { path: '/' })`).
    *   `Astro.redirect()`: Perform server-side redirects.
    *   `Astro.clientAddress`: IP address of the request.
    *   `Astro.locals`: An object to share data between middleware and pages/endpoints (see Middleware).
*   **API Routes:** Files inside `src/pages/api/` (or any `.js`/`.ts` file in `src/pages/`) become serverless function-like API endpoints. They export functions corresponding to HTTP methods (`GET`, `POST`, `PUT`, `DELETE`, etc.).
*   **Middleware:** Code that runs before or after page/endpoint rendering for every request.

## API Routes (`src/pages/**/*.js|.ts`)

*   **Purpose:** Create server endpoints for tasks like handling form submissions, interacting with databases, or providing data to client-side JavaScript.
*   **Implementation:** Export async functions named after HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `ALL`).
*   **Context:** The function receives an object containing `request`, `cookies`, `params`, `locals`, etc.
*   **Response:** Return a standard Response object.

```typescript
// src/pages/api/users/[id].ts
import type { APIRoute } from 'astro';
import { db, User } from 'astro:db'; // Example using Astro DB

// GET /api/users/:id
export const GET: APIRoute = async ({ params, request }) => {
  const id = params.id;
  if (!id) {
    return new Response('User ID required', { status: 400 });
  }
  try {
    const user = await db.select().from(User).where({ id: parseInt(id) }).first();
    if (!user) {
      return new Response('User not found', { status: 404 });
    }
    return new Response(JSON.stringify(user), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error) {
    console.error(error);
    return new Response('Internal Server Error', { status: 500 });
  }
}

// POST /api/users (Example - assumes different file: src/pages/api/users.ts)
export const POST: APIRoute = async ({ request, locals }) => {
    // Check authentication if using middleware (example)
    // if (!locals.user) {
    //   return new Response('Unauthorized', { status: 401 });
    // }
    try {
        const data = await request.formData(); // Or request.json()
        const name = data.get('name');
        const email = data.get('email');
        // Add validation here...
        // const newUser = await db.insert(User).values({ name, email }).returning().first();
        return new Response(JSON.stringify({ message: 'User created' /*, user: newUser */ }), { status: 201 });
    } catch (error) {
        return new Response('Error creating user', { status: 400 });
    }
}
```

## Middleware (`src/middleware.js|.ts`)

*   **Purpose:** Intercept requests to perform actions like authentication checks, logging, modifying response headers, or passing data to pages/endpoints.
*   **Implementation:** Export an `onRequest` async function. It receives `context` (containing `locals`, `request`, `cookies`, `url`, etc.) and `next` (a function to call the next middleware or the page/endpoint).
*   **`context.locals`:** An object unique to each request, used to share data between middleware and the final route handler. You can attach properties to it (e.g., `context.locals.user = await getUserFromSession(...)`).
*   **Modifying Responses:** You can return a `Response` directly from middleware to override the default behavior (e.g., for redirects or authentication failures). You can also modify the response returned by `await next()` before returning it.

```typescript
// src/middleware.ts
import { defineMiddleware } from 'astro:middleware';
// Assume some auth functions exist
// import { verifyAuth } from './lib/auth';

export const onRequest = defineMiddleware(async (context, next) => {
  console.log(`Middleware processing: ${context.request.method} ${context.url.pathname}`);

  // Example: Authentication check
  // const sessionCookie = context.cookies.get('session')?.value;
  // const user = await verifyAuth(sessionCookie);
  // context.locals.user = user; // Pass user info to page/endpoint

  // Example: Redirect based on path or auth
  // if (context.url.pathname === '/admin' && !context.locals.user?.isAdmin) {
  //   return context.redirect('/login'); // Return Response directly
  // }

  // Call the next middleware or route handler
  const response = await next();

  // Example: Modify response headers
  response.headers.set('X-Custom-Header', 'Processed by middleware');

  return response;
});
```

SSR, API Routes, and Middleware unlock dynamic capabilities in Astro, allowing you to build full-stack applications while still benefiting from Astro's performance focus.

*(Refer to the official Astro SSR, API Routes, and Middleware documentation.)*