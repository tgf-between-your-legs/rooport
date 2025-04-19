# SvelteKit Dev: Form Actions

SvelteKit Actions provide a robust, built-in mechanism for handling form submissions securely on the server, integrating seamlessly with HTML forms and progressive enhancement.

## 1. Core Concept

*   **Server-Side Execution:** Action code runs **only on the server** (`+page.server.js`), allowing secure data mutations (DB access, calling private APIs).
*   **File Convention:** Actions are exported as an `actions` object from `+page.server.js`.
*   **Request Handling:** Actions automatically handle `POST` requests from corresponding `<form>` elements on the page.
*   **Progressive Enhancement:** Works with standard HTML form submissions (full page reload) and enhanced client-side submissions (`use:enhance`) without code duplication.

## 2. Implementation

**a) Define Actions (`+page.server.js`)**

*   Export an `actions` object of type `Actions` (from `./$types`).
*   Each property is an `async` function representing an action.
*   **Default Action:** A function named `default` handles submissions from forms without a specific `action` attribute (`<form method="POST">`).
*   **Named Actions:** Functions with other names (e.g., `update`, `delete`) handle submissions from forms targeting that action (`<form method="POST" action="?/delete">`).
*   **Arguments:** Action functions receive `{ request, cookies, locals, params, fetch, url }`.
*   **Processing:** Use `await request.formData()` to get form data. Perform validation and data mutation logic.

```typescript
// src/routes/settings/+page.server.ts
import type { Actions } from './$types';
import { fail, redirect } from '@sveltejs/kit';
// import { updateUserProfile } from '$lib/server/db';

export const actions: Actions = {
  // Default action (e.g., update primary settings)
  default: async ({ request, locals }) => {
    const formData = await request.formData();
    const email = formData.get('email') as string;

    if (!email || !email.includes('@')) {
      // Use fail() for validation errors
      return fail(400, { email, error: 'Invalid email address' });
    }

    try {
      // await updateUserProfile(locals.userId, { email });
      return { success: true, message: 'Settings updated!' }; // Return success data
    } catch (err) {
      console.error(err);
      return fail(500, { email, error: 'Server error updating settings.' });
    }
  },

  // Named action (e.g., update password)
  updatePassword: async ({ request, locals }) => {
    const formData = await request.formData();
    const password = formData.get('password') as string;

    if (!password || password.length < 8) {
      return fail(400, { error: 'Password must be at least 8 characters' }); // No need to return password
    }

    try {
      // await updateUserPassword(locals.userId, password);
      // Redirect on success (Post/Redirect/Get pattern)
      redirect(303, '/settings?passwordUpdated=true');
    } catch (err) {
      console.error(err);
      return fail(500, { error: 'Server error updating password.' });
    }
  }
};
```

**b) Use Forms (`+page.svelte`)**

*   Use standard HTML `<form method="POST">`.
*   Target named actions using `action="?/actionName"` (e.g., `action="?/updatePassword"`).
*   **Progressive Enhancement:** Add `use:enhance` (from `$app/forms`) to the `<form>` tag. This intercepts the submission, uses `fetch` client-side, and updates page state without a full reload, falling back gracefully if JS is disabled.
*   **Accessing Results:**
    *   Import `export let form: ActionData` (from `./$types`) in the component's script.
    *   `form` will contain the data returned by the most recent action (`fail()` or successful return object). Access validation errors (`form?.error`), submitted values (`form?.email`), or success flags (`form?.success`).
    *   The `$page.form` store also holds this data.
*   **Loading States:** `use:enhance` provides parameters like `submitting` to show loading indicators.

```svelte
<!-- src/routes/settings/+page.svelte -->
<script lang="ts">
  import type { ActionData } from './$types';
  import { enhance } from '$app/forms';
  import { page } from '$app/stores'; // Can also use $page.form

  export let form: ActionData; // Data from last action

  // Reactive access to form data/errors
  $: defaultErrors = form?.action === 'default' ? form : undefined;
  $: passwordErrors = form?.action === '?/updatePassword' ? form : undefined;

</script>

<h2>Update Email (Default Action)</h2>
<form method="POST" use:enhance={( { formElement, data, action, cancel, submitter } ) => {
    // Optional: Callback for enhance
    console.log('Submitting default action...');
    return async ({ result, update }) => {
      // Optional: Run after submission completes
      console.log('Default action result:', result);
      await update(); // Update page data ($page.form, invalidate load functions)
    };
}}>
  <label> Email: <input type="email" name="email" value={defaultErrors?.email ?? $page.data.userEmail ?? ''} /> </label>
  {#if defaultErrors?.error}<p style="color: red;">{defaultErrors.error}</p>{/if}
  {#if defaultErrors?.success}<p style="color: green;">{defaultErrors.message}</p>{/if}
  <button type="submit">Update Email</button>
</form>

<h2>Update Password (Named Action)</h2>
<form method="POST" action="?/updatePassword" use:enhance>
  <label> New Password: <input type="password" name="password" /> </label>
  {#if passwordErrors?.error}<p style="color: red;">{passwordErrors.error}</p>{/if}
  {#if $page.url.searchParams.has('passwordUpdated')}<p style="color: green;">Password updated successfully!</p>{/if}
  <button type="submit">Update Password</button>
</form>
```

## 3. Handling Results

*   **`fail(status, data?)`:** Return validation errors or other non-critical failures. `status` is typically 400 or 422. `data` is an optional object available in `form`/`$page.form`. **Does not trigger `+error.svelte`**.
*   **`redirect(status, location)`:** Redirect the user after a successful action (Post/Redirect/Get pattern). `status` is typically 303.
*   **Return Object:** Return a plain object on success. This data is available in `form`/`$page.form`.
*   **Invalidation:** After a successful action using `use:enhance`, SvelteKit automatically invalidates the page's `load` function data and re-runs it, ensuring the UI reflects the changes. Use `invalidateAll()` from `$app/navigation` for broader invalidation if needed.

## 4. Security

*   **ALWAYS validate data server-side** within the action function, even if client-side validation exists.
*   Perform authorization checks within actions (using `locals` from hooks) to ensure the user is allowed to perform the mutation.