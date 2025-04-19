# SvelteKit Error Handling

Handling expected and unexpected errors in SvelteKit applications.

## Core Concepts

SvelteKit provides multiple mechanisms for handling errors gracefully, both on the server and the client:

*   **Expected Errors (e.g., Not Found):** Use the `error` helper function from `@sveltejs/kit` within `load` functions or `actions` to trigger a specific HTTP status code and error message. These are caught by the nearest `+error.svelte` boundary.
*   **Unexpected Errors (e.g., Runtime Bugs):** Uncaught errors during rendering or in `load`/`actions` are caught by the nearest `+error.svelte` boundary. Server-side unexpected errors can also be intercepted by the `handleError` hook.
*   **Validation Errors (Forms):** Use the `fail()` helper function from `@sveltejs/kit` within `actions` to return validation errors (and optionally form data) back to the page component without triggering an error boundary.

## 1. `error()` Helper

*   **Purpose:** To generate an expected error response with a specific HTTP status code and message, typically used within `load` or `action` functions. This immediately stops execution and renders the appropriate `+error.svelte` page.
*   **Usage:** Import from `@sveltejs/kit`. Call `throw error(status, message | { message: string })`.
    ```typescript
    // src/routes/items/[id]/+page.server.ts
    import { error } from '@sveltejs/kit';
    import type { PageServerLoad } from './$types';

    export const load: PageServerLoad = async ({ params }) => {
      // const item = await db.getItem(params.id);
      const item = params.id === 'valid' ? { id: params.id, name: 'Valid Item' } : null; // Placeholder

      if (!item) {
        // Throw a 404 error - caught by +error.svelte
        throw error(404, { message: `Item with ID ${params.id} not found` });
      }

      return { item };
    };
    ```

## 2. `+error.svelte` Component

*   **Purpose:** A special Svelte component that renders when an error (either thrown via `error()` or an unexpected runtime error) occurs during loading or rendering for routes within its directory scope.
*   **File Naming:** Create `+error.svelte` within `src/routes` or any subdirectory. The nearest boundary catches the error.
*   **Accessing Error:** Use the `$page` store (from `$app/stores`) to access error details: `$page.status` and `$page.error.message`.
    ```svelte
    <!-- src/routes/+error.svelte (Root error boundary) -->
    <script lang="ts">
      import { page } from '$app/stores';
    </script>

    <h1>{$page.status}</h1>
    <p>{$page.error?.message ?? 'An unknown error occurred.'}</p>

    {#if $page.status === 404}
      <p>Sorry, we couldn't find that page.</p>
    {:else if $page.status >= 500}
      <p>Sorry, something went wrong on our end. Please try again later.</p>
    {/if}

    <a href="/">Go Home</a>
    ```

## 3. `fail()` Helper (Form Actions)

*   **Purpose:** To return data (typically validation errors and submitted form values) back to the page component from an `action` function **without** triggering an error boundary. Indicates a failed *action*, not a critical application error.
*   **Usage:** Import from `@sveltejs/kit`. Call `return fail(status, data?)`. `status` is usually 400 (Bad Request) or 422 (Unprocessable Entity). `data` is an optional object containing error messages and form values.
*   **Accessing Data:** The returned data is available in the `form` prop within the corresponding `+page.svelte`.
    ```typescript
    // src/routes/contact/+page.server.ts
    import { fail } from '@sveltejs/kit';
    import type { Actions } from './$types';

    export const actions: Actions = {
      default: async ({ request }) => {
        const formData = await request.formData();
        const email = formData.get('email') as string;
        const message = formData.get('message') as string;

        const errors: Record<string, string> = {};
        if (!email || !email.includes('@')) {
          errors.email = 'A valid email is required';
        }
        if (!message) {
          errors.message = 'Message cannot be empty';
        }

        // If errors exist, return them using fail()
        if (Object.keys(errors).length > 0) {
          return fail(400, { errors, email, message }); // Return errors and original values
        }

        // TODO: Process valid data (e.g., send email)
        console.log('Processing contact form:', { email, message });

        return { success: true }; // Indicate success
      }
    };
    ```
    ```svelte
    <!-- src/routes/contact/+page.svelte -->
    <script lang="ts">
      import type { ActionData } from './$types';
      export let form: ActionData; // Receives data from fail() or successful action return
    </script>

    <form method="POST" use:enhance> {/* use:enhance is optional but recommended */}
      <label>
        Email:
        <input type="email" name="email" value={form?.email ?? ''} />
        {#if form?.errors?.email}<p style="color: red;">{form.errors.email}</p>{/if}
      </label>
      <label>
        Message:
        <textarea name="message">{form?.message ?? ''}</textarea>
        {#if form?.errors?.message}<p style="color: red;">{form.errors.message}</p>{/if}
      </label>
      <button type="submit">Send</button>
      {#if form?.success}<p style="color: green;">Message sent successfully!</p>{/if}
    </form>
    ```

## 4. `handleError` Server Hook

*   **Purpose:** A server-only hook (`src/hooks.server.js` or `.ts`) that acts as a global, last-resort error handler for **unexpected** errors occurring on the server during rendering or `load`/`action` execution. It runs *after* the `+error.svelte` boundary has rendered.
*   **Usage:** Export an async function `handleError({ error, event })`. Use it primarily for logging/reporting unexpected errors. The return value shapes the error object passed to `$page.error`.
    ```typescript
    // src/hooks.server.ts
    import type { HandleServerError } from '@sveltejs/kit';

    export const handleError: HandleServerError = async ({ error, event }) => {
      // Log the error to your monitoring service
      console.error('Unexpected server error:', error, 'Event:', event);
      // reportErrorToService(error, event);

      // Optionally customize the error object passed to +error.svelte
      return {
        message: 'An unexpected error occurred on the server.',
        // You can add more context here if needed, but avoid leaking sensitive info
        errorId: generateErrorId(), // Example
      };
    };
    ```

*(Refer to the official SvelteKit Error Handling documentation: https://kit.svelte.dev/docs/errors)*