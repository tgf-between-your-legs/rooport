# SvelteKit Dev: Error Handling

SvelteKit provides a layered approach to handling errors gracefully.

## 1. Expected Errors (`error()` Helper)

*   **Purpose:** To intentionally trigger an error condition with a specific HTTP status code, typically within `load` functions or `actions`. Used for predictable errors like "Not Found" (404), "Forbidden" (403), etc.
*   **Usage:** Import `error` from `@sveltejs/kit`. Call `throw error(status, message | { message: string, ... })`.
    *   `status`: HTTP status code (e.g., 404).
    *   `body` (Optional): String or object passed to `+error.svelte` via `$page.error`. Avoid sensitive details.
*   **Effect:** Stops execution of the current function (`load`/`action`) and renders the nearest `+error.svelte` boundary.

```typescript
// src/routes/items/[id]/+page.server.ts
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
  // const item = await db.getItem(params.id);
  const item = params.id === 'valid' ? { id: params.id } : null; // Placeholder

  if (!item) {
    // Throw a 404 error
    throw error(404, { message: `Item ${params.id} not found` });
  }
  return { item };
};
```

## 2. Validation Errors (`fail()` Helper)

*   **Purpose:** To return validation errors (and optionally submitted form data) back to the page from an `action` function **without** triggering an error page. Indicates a failed *action*, not a critical application error.
*   **Usage:** Import `fail` from `@sveltejs/kit`. Call `return fail(status, data?)`.
    *   `status`: Usually 400 (Bad Request) or 422 (Unprocessable Entity).
    *   `data` (Optional): Object containing error messages and original form values, accessible in the page component via the `form` prop (or `$page.form`).
*   **Effect:** Returns data to the page component; does **not** render `+error.svelte`.

```typescript
// src/routes/contact/+page.server.ts
import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';

export const actions: Actions = {
  default: async ({ request }) => {
    const formData = await request.formData();
    const email = formData.get('email') as string;
    if (!email || !email.includes('@')) {
      // Return validation error using fail()
      return fail(400, { email, error: 'Invalid email address' });
    }
    // ... process valid data ...
    return { success: true };
  }
};
```

## 3. Error UI (`+error.svelte`)

*   **Purpose:** A Svelte component that renders the UI for:
    *   Expected errors thrown via the `error()` helper.
    *   Unexpected runtime errors caught by SvelteKit (if not handled differently by `handleError`).
*   **Location:** Place in `src/routes` for a global fallback, or within specific route directories for more granular error pages. The nearest boundary up the route hierarchy catches the error.
*   **Data Access:** Use the `$page` store (from `$app/stores`) to access error details:
    *   `$page.status`: The HTTP status code.
    *   `$page.error`: The error object (containing `message` and any other properties passed via `error()` or returned by `handleError`).

```svelte
<!-- src/routes/+error.svelte -->
<script lang="ts">
  import { page } from '$app/stores';
</script>

<h1>{$page.status}</h1>
<p>{$page.error?.message ?? 'An unknown error occurred.'}</p>

{#if $page.error?.errorId}
  <p>Error ID: {$page.error.errorId}</p> <!-- From handleError -->
{/if}

{#if $page.status === 404}
  <p>Sorry, we couldn't find that page.</p>
{:else if $page.status >= 500}
  <p>Sorry, something went wrong on our end.</p>
{/if}
<a href="/">Go Home</a>
```

## 4. Unexpected Errors (`handleError` Hook)

*   **Purpose:** Catches **unexpected** runtime errors (JavaScript errors during rendering, unhandled exceptions in `load`/`action`/`handle`). Primarily used for **logging/reporting** errors.
*   **Location:**
    *   `src/hooks.server.js`: `export async function handleError({ error, event }) { ... }` (Server-only).
    *   `src/hooks.client.js`: `export function handleError({ error, event, status, message }) { ... }` (Client-only).
*   **Execution:** Runs *after* an unexpected error occurs. Does *not* catch errors thrown via `error()` or `fail()`.
*   **Return Value:** Shapes the `$page.error` object passed to `+error.svelte`. **Crucially, avoid returning sensitive details from the original `error` object.** Log the full error internally but return only safe information (like a generic message and an error ID).

```typescript
// src/hooks.server.ts
import type { HandleServerError } from '@sveltejs/kit';

export const handleError: HandleServerError = ({ error, event }) => {
  const errorId = crypto.randomUUID();
  console.error('Unexpected Server Error:', error, `ID: ${errorId}`);
  // logToMonitoringService(error, { event, errorId });

  return {
    message: 'An unexpected error occurred.',
    errorId: errorId, // For user reference
  };
};
```

## Summary

*   Use `error()` for expected conditions (404, 403 etc.) -> renders `+error.svelte`.
*   Use `fail()` for form validation errors -> returns data to the page component (`form` prop).
*   Implement `+error.svelte` for user-facing error UI.
*   Use `handleError` hooks (server/client) for logging unexpected runtime errors.