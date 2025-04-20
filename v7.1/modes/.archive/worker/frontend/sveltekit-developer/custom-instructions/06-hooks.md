# SvelteKit Dev: Hooks

Hooks allow you to intercept and modify SvelteKit's core behavior, primarily during the request/response cycle.

## 1. Core Concept

*   Hooks run code in response to framework events.
*   Defined in specific files in `src/`: `hooks.server.js` (or `.ts`) and `hooks.client.js` (or `.ts`).

## 2. Server Hooks (`src/hooks.server.js`)

*   **Runs ONLY on the server.** Intercepts all requests handled by the SvelteKit server.

**a) `handle({ event, resolve })`**

*   **Purpose:** The main server hook. Runs for every request *before* `load` functions or endpoint handlers.
*   **Use Cases:**
    *   Authentication/Authorization: Check cookies/headers, load user sessions.
    *   Setting Request Context: Add data to `event.locals` (e.g., `event.locals.user = await getUser(...)`) to make it available in `load`, `actions`, and `+server.js`.
    *   Modifying Response Headers: Add/change headers on the final `Response`.
    *   Conditional Redirects: Redirect users based on auth status or other conditions.
*   **Execution:**
    1.  Perform setup logic (e.g., load user).
    2.  **Crucially, call and `await resolve(event)`** to continue processing the request (runs `load`, renders page, etc.).
    3.  Optionally modify the `response` returned by `resolve`.
    4.  Return the final `response`.
    *   Alternatively, return your own `Response` directly to bypass `resolve` (e.g., for redirects).

```typescript
// src/hooks.server.ts
import type { Handle } from '@sveltejs/kit';
import { redirect } from '@sveltejs/kit';
// import { getUserFromSession } from '$lib/server/auth';

export const handle: Handle = async ({ event, resolve }) => {
  // 1. Populate event.locals (e.g., user session)
  const sessionId = event.cookies.get('session_id');
  // event.locals.user = await getUserFromSession(sessionId);
  event.locals.user = sessionId ? { id: 'user123', name: 'Alice', isAdmin: false } : null; // Placeholder

  // 2. Authorization / Redirects
  if (event.url.pathname.startsWith('/admin') && !event.locals.user?.isAdmin) {
    console.log('Admin access denied, redirecting...');
    return redirect(303, '/login'); // Return Response directly
  }

  // 3. Process the request (runs load, actions, render)
  const response = await resolve(event);

  // 4. Modify response (optional)
  // response.headers.set('X-Powered-By', 'Roo Commander');

  // 5. Return final response
  return response;
};
```

**b) `handleFetch({ request, event, fetch })`**

*   **Purpose:** Intercepts `fetch` calls made *within server-side* `load` or `action` functions.
*   **Use Cases:** Modifying outgoing requests (e.g., adding auth tokens to internal API calls), logging outgoing fetches.
*   **Execution:** Must call and return `fetch(request)` (potentially modified).

```typescript
// src/hooks.server.ts (continued)
import type { HandleFetch } from '@sveltejs/kit';

export const handleFetch: HandleFetch = async ({ request, event, fetch }) => {
  console.log(`Server Fetch Hook: Intercepting ${request.method} ${request.url}`);
  if (request.url.startsWith('https://api.internal.service/')) {
    // Add auth token if user is logged in
    if (event.locals.user?.apiToken) {
      request.headers.set('Authorization', `Bearer ${event.locals.user.apiToken}`);
    }
  }
  // Forward the request
  return fetch(request);
};
```

**c) `handleError({ error, event })`**

*   **Purpose:** Global handler for **unexpected** errors occurring on the server during request processing (rendering, `load`, `action`, `handle`). Does *not* catch errors thrown via the `error()` helper.
*   **Use Cases:** Logging unexpected errors to external monitoring services (Sentry, DataDog, etc.).
*   **Execution:** Runs *after* the error occurs. The return value shapes the object passed to `+error.svelte` via `$page.error`. **Avoid returning sensitive details.**

```typescript
// src/hooks.server.ts (continued)
import type { HandleServerError } from '@sveltejs/kit';

export const handleError: HandleServerError = ({ error, event }) => {
  const errorId = crypto.randomUUID();
  console.error('Server Error Hook:', error, `ID: ${errorId}`, 'Event:', event);
  // logToMonitoringService(error, { event, errorId, user: event.locals.user });

  // Return value populates $page.error in +error.svelte
  return {
    message: 'An unexpected error occurred on the server.',
    errorId: errorId // For user reference
  };
};
```

## 3. Client Hooks (`src/hooks.client.js`)

*   **Runs ONLY in the browser.**

**a) `handleError({ error, event, status, message })`**

*   **Purpose:** Global handler for **unexpected** errors during client-side loading or rendering.
*   **Use Cases:** Logging client-side errors to external services.
*   **Execution:** Runs when an unhandled error occurs on the client. The return value shapes `$page.error`.

```typescript
// src/hooks.client.ts
import type { HandleClientError } from '@sveltejs/kit';

export const handleError: HandleClientError = ({ error, event, status, message }) => {
  const errorId = crypto.randomUUID();
  console.error('Client Error Hook:', error, `ID: ${errorId}`, 'Event:', event, 'Status:', status, 'Message:', message);
  // logToMonitoringService(error, { event, status, message, errorId });

  // Return value populates $page.error in +error.svelte
  return {
    message: 'An unexpected error occurred in your browser.',
    errorId: errorId
  };
};
```

**b) `reroute({ url })`**

*   Advanced hook to dynamically change routing logic on the client before navigation occurs. Less common.