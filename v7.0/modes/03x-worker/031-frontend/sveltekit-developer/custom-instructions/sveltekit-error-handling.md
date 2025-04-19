# SvelteKit: Error Handling

Handling expected and unexpected errors in SvelteKit applications.

## Core Concept: Layered Error Handling

SvelteKit provides multiple mechanisms for handling errors gracefully, distinguishing between expected errors (like "Not Found") and unexpected runtime errors.

**Key Mechanisms:**

1.  **`error()` Helper (from `@sveltejs/kit`):**
    *   **Purpose:** Used within `load` functions or `actions` to trigger an **expected error** condition (e.g., 404 Not Found, 401 Unauthorized, 403 Forbidden).
    *   **How it works:** Stops execution of the `load`/`action` and looks for the nearest `+error.svelte` boundary up the route hierarchy to render.
    *   **Signature:** `error(status: number, body?: App.Error | string)`
        *   `status`: The HTTP status code (e.g., 404).
        *   `body` (Optional): Data passed to the `+error.svelte` component via `$page.error`. Can be a simple string or an object conforming to the `App.Error` interface (defined in `app.d.ts`). **Avoid putting sensitive details here.**
2.  **`+error.svelte` Component:**
    *   **Purpose:** Renders the UI for **expected errors** triggered by the `error()` helper or for **unexpected errors** caught by SvelteKit's server/client error handling if no server/client `handleError` hook overrides it.
    *   **Location:** Place in `src/routes` for a global error page, or within specific route directories for more granular error UIs. The nearest boundary matching the URL path is used.
    *   **Data Access:** Receives error information via the `$page` store: `import { page } from '$app/stores'; $page.status`, `$page.error`. The `$page.error` object contains the `message` (from `error(status, message)` or default status text) and any additional properties passed in the body object.
3.  **`handleError` Hook (`hooks.server.js` / `hooks.client.js`):**
    *   **Purpose:** Catches **unexpected errors** (JavaScript errors during rendering, unhandled exceptions in `load`/`action`/`handle`). Primarily used for **logging** errors to external services.
    *   **Server (`src/hooks.server.js`):** `export async function handleError({ error, event }) { ... }`. Runs only on the server. The return value populates `$page.error` (if not overridden by `+error.svelte`).
    *   **Client (`src/hooks.client.js`):** `export function handleError({ error, event, status, message }) { ... }`. Runs only in the browser. The return value populates `$page.error`.
    *   **Note:** These hooks do *not* catch errors thrown using the `error()` helper or `Response` objects thrown from `load`/`action` – those are handled directly by `+error.svelte`.

## Implementation Examples

**1. Using `error()` Helper in `load`:**

```typescript
// src/routes/products/[id]/+page.server.ts
import type { PageServerLoad } from './$types';
import { error, json } from '@sveltejs/kit';
// import { getProductById } from '$lib/server/db';

export const load: PageServerLoad = async ({ params }) => {
  // const product = await getProductById(params.id);
  const product = params.id === 'exists' ? { id: params.id, name: `Product ${params.id}` } : null; // Placeholder

  if (!product) {
    // Trigger a 404 error - caught by nearest +error.svelte
    error(404, {
        message: `Product not found: ID ${params.id}`,
        // You can add non-sensitive context if needed
        // context: 'Product detail page load'
    });
  }

  return json({ product });
};
```

**2. Creating `+error.svelte`:**

```svelte
<!-- src/routes/+error.svelte (Global Error Page) -->
<script lang="ts">
	import { page } from '$app/stores';
</script>

<h1>{$page.status}: {$page.error?.message ?? 'Unknown Error'}</h1>

{#if $page.error?.context}
  <p>Context: {$page.error.context}</p>
{/if}

{#if $page.status === 404}
  <p>Sorry, the page you're looking for doesn't exist.</p>
  <a href="/">Go Home</a>
{:else if $page.status >= 500}
   <p>Something went wrong on our end. Please try again later.</p>
   {#if $page.error?.errorId}
     <p>Error ID: {$page.error.errorId}</p> {/* Display ID from handleError */}
   {/if}
{:else}
   <p>An unexpected error occurred.</p>
{/if}

{#if process.env.NODE_ENV === 'development' && $page.error?.stack}
	<pre>{$page.error.stack}</pre>
{/if}
```

**3. Using `handleError` Hook for Logging:**

```typescript
// src/hooks.server.ts
import type { HandleServerError } from '@sveltejs/kit';
// import * as Sentry from '@sentry/node'; // Example error logging service

// Initialize Sentry or other service...

export const handleError: HandleServerError = ({ error, event }) => {
  const errorId = crypto.randomUUID();
  // Log to external service
  console.error('Server Hook (handleError):', error, 'Event:', event);
  // Sentry.captureException(error, { extra: { event, errorId } });

  // Return data for the +error.svelte page ($page.error)
  // Avoid returning the raw error object here for security
  return {
    message: 'An unexpected server error occurred.',
    errorId, // For user reference
  };
};

// src/hooks.client.ts
import type { HandleClientError } from '@sveltejs/kit';

export const handleError: HandleClientError = ({ error, event, status, message }) => {
    const errorId = crypto.randomUUID();
    console.error('Client Hook (handleError):', error, 'Event:', event);
    // logErrorToService({ error, event, status, message, errorId });

    return {
        message: `A client-side error occurred: ${message}`,
        errorId,
    };
};
```

Use the `error()` helper for expected error conditions within `load`/`action`. Implement `+error.svelte` pages for user-facing error UI. Use `handleError` hooks primarily for logging unexpected errors to monitoring services.

*(Refer to the official SvelteKit documentation on Error Handling.)*