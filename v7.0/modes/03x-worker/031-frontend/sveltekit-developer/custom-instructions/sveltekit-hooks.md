# SvelteKit: Hooks (`hooks.server.js`, `hooks.client.js`)

Intercepting requests and responses globally using SvelteKit hooks.

## Core Concept: Intercepting Requests & Responses

SvelteKit hooks allow you to run code in response to events happening within the framework, primarily during the request-response lifecycle. They are defined in specific files in the `src` directory.

**Key Hook Files:**

1.  **`src/hooks.server.js` (or `.ts`):**
    *   **Runs ONLY on the server.**
    *   Used to intercept **all requests** handled by the SvelteKit server (page requests, form actions, server endpoint requests).
    *   **Exports:**
        *   `handle({ event, resolve })`: The main hook. Runs for every request. You can modify the `event` object (e.g., `event.locals`) or the `Response` returned by `resolve`. **Must call and return `resolve(event)`** to continue processing the request, or return your own `Response` to short-circuit.
        *   `handleError({ error, event })`: Runs when an *unexpected* error occurs during request handling (errors thrown from `load`/`action` are typically handled by `+error.svelte`). Use for logging errors to external services.
        *   `handleFetch({ request, event, fetch })`: Intercepts `fetch` calls made *within* `load` or `action` functions on the server. Useful for modifying requests (e.g., adding auth headers) before they go out. **Must call and return `fetch(request)`**.
2.  **`src/hooks.client.js` (or `.ts`):**
    *   **Runs ONLY on the client (browser).**
    *   **Exports:**
        *   `handleError({ error, event, status, message })`: Runs when an *unexpected* error occurs during client-side loading or rendering. Use for client-side error logging. Returns error details to be shown (can customize).
        *   `reroute({ url })`: Advanced hook to change routing logic on the client. Less common.

## Server Hooks (`src/hooks.server.js`)

**1. `handle` Hook:**

*   **Purpose:** Authentication checks, setting request context (`event.locals`), modifying response headers.
*   **`event.locals`:** An object where you can store data specific to the current request (e.g., user session data) that can then be accessed in `load`, `action`, and `+server.js` functions.

```typescript
// src/hooks.server.ts
import type { Handle, HandleFetch, HandleServerError } from '@sveltejs/kit';
import { redirect } from '@sveltejs/kit';
// import { getSessionFromCookie } from '$lib/server/auth'; // Example auth helper

// --- handle ---
// Runs for every request to the server.
export const handle: Handle = async ({ event, resolve }) => {
  console.log(`Server Hook (handle): Processing ${event.request.method} ${event.url.pathname}`);

  // 1. Get user session from cookie (example)
  // event.locals.user = await getSessionFromCookie(event.request.headers.get('cookie'));
  event.locals.user = event.cookies.get('session_id') ? { id: 'user123', name: 'Alice' } : null; // Placeholder

  // 2. Authorization check (example)
  if (event.url.pathname.startsWith('/admin') && !event.locals.user) {
    // Redirect to login if trying to access /admin without session
    return redirect(303, '/login'); // Use 303 for POST redirects after login
  }

  // 3. Call resolve() to continue processing the request
  // This runs load functions, actions, renders the page, etc.
  const response = await resolve(event);

  // 4. Modify the response (optional)
  // response.headers.set('X-Custom-Header', 'Processed by handle hook');

  // 5. Return the response
  return response;
};

// --- handleFetch ---
// Intercepts fetch calls made *on the server* (in load/action)
export const handleFetch: HandleFetch = async ({ request, event, fetch }) => {
  console.log(`Server Hook (handleFetch): Intercepting fetch to ${request.url}`);

  // Example: Add an Authorization header to requests to internal API
  if (request.url.startsWith('http://internal-api/')) {
    const token = event.locals.apiToken; // Assuming token is set in handle
    if (token) {
      request.headers.set('Authorization', `Bearer ${token}`);
    }
  }

  // Must call and return the original fetch or a modified one
  return fetch(request);
};


// --- handleError ---
// Handles *unexpected* errors on the server
export const handleError: HandleServerError = ({ error, event }) => {
  // Log the error to an external service
  console.error('Server Hook (handleError): Unexpected error:', error, 'Event:', event);
  // logErrorToService(error, { url: event.url.toString(), user: event.locals.user });

  // Return value is used for the error page ($page.error)
  // Keep sensitive details out of the returned object
  return {
    message: 'Whoops! An unexpected error occurred.',
    // You can add a unique error ID for support correlation
    errorId: crypto.randomUUID(),
  };
};
```

## Client Hooks (`src/hooks.client.js`)

```typescript
// src/hooks.client.ts
import type { HandleClientError } from '@sveltejs/kit';

// --- handleError ---
// Handles *unexpected* errors on the client
export const handleError: HandleClientError = ({ error, event, status, message }) => {
  // Log the error to an external service
  console.error('Client Hook (handleError): Unexpected error:', error, 'Event:', event);
  // logErrorToService(error, { url: event.url.toString(), status, message });

  // Return value is shown to the user (via $page.error in +error.svelte)
  // Avoid returning sensitive details from the original error
  return {
    message: `An error occurred on the client: ${message}`,
    // errorId: crypto.randomUUID(), // Can add correlation ID
  };
};
```

Hooks provide powerful interception points in the SvelteKit request lifecycle. Use `hooks.server.js` for server-side logic like authentication, context setting, and error logging. Use `hooks.client.js` primarily for client-side error logging.

*(Refer to the official SvelteKit documentation on Hooks.)*