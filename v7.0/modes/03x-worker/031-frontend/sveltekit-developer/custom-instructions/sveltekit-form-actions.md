# SvelteKit: Form Actions & Progressive Enhancement

Handling form submissions and data mutations server-side using SvelteKit Actions.

## Core Concept: Server Actions & Progressive Enhancement

SvelteKit provides a built-in mechanism for handling form submissions securely on the server using **Actions**. Actions are defined within `+page.server.js` and automatically handle POST requests from HTML `<form>` elements, working seamlessly with or without client-side JavaScript (Progressive Enhancement).

**Key Features:**

*   **Server-Side Execution:** Action code runs **only on the server**, allowing secure access to databases, APIs, and environment variables for data mutations.
*   **File Convention:** Actions are defined as named exports within an `actions` object in `+page.server.js`.
*   **Default Action:** If no specific action name is provided by the form, the `default` action within the `actions` object is executed.
*   **Named Actions:** Forms can target specific named actions using a query parameter in the `action` attribute (e.g., `<form action="?/updateName" method="POST">`).
*   **Progressive Enhancement (`use:enhance`):** SvelteKit provides the `enhance` action (imported from `$app/forms`) which can be applied to a `<form>` element (`<form method="POST" use:enhance>`). This intercepts the form submission on the client-side, performs it using `fetch`, and updates the page state without a full page reload, while still falling back to standard form submission if JavaScript is disabled.
*   **Data & Error Handling:**
    *   Actions can return data (using `json()` from `@sveltejs/kit`) which becomes available in the component via the `$page.form` store after submission.
    *   Use the `fail(status, data)` helper (from `@sveltejs/kit`) to return validation errors or other failure states without throwing an error. This data is also available in `$page.form`.
    *   Use `redirect()` (from `@sveltejs/kit`) to navigate the user after a successful action.
*   **Pending States:** The `$page.form` store and the `submitting` property provided by `use:enhance` can be used to show loading indicators or disable forms during submission.

## Implementation

**1. Define Actions (`+page.server.js`):**

```typescript
// src/routes/todos/+page.server.ts
import type { Actions, PageServerLoad } from './$types';
import { fail, redirect } from '@sveltejs/kit';
// import { db } from '$lib/server/db'; // Example DB client

// Example Load function to get initial data
export const load: PageServerLoad = async ({ locals }) => {
  // const todos = await db.getTodos(locals.userId);
  const todos = [{ id: 1, text: 'Learn SvelteKit', done: false }]; // Placeholder
  return { todos };
};

// Define actions object
export const actions: Actions = {
  // Default action (handles POST requests to /todos without ?/actionName)
  default: async ({ request, locals }) => {
    const formData = await request.formData();
    const text = formData.get('text') as string;

    // Basic validation
    if (!text || text.trim().length < 3) {
      // Return validation error using fail()
      // This data goes into $page.form
      return fail(400, { text, error: 'Todo must be at least 3 characters long.' });
    }

    try {
      console.log('Default Action: Creating todo', text);
      // await db.createTodo({ userId: locals.userId, text });
      // No explicit return needed on success if no data needs to go back
      // Remix automatically invalidates the loader data for the page
    } catch (err) {
      console.error(err);
      return fail(500, { text, error: 'Failed to create todo.' });
    }
  },

  // Named action (handles POST requests to /todos?/delete)
  delete: async ({ request, locals }) => {
    const formData = await request.formData();
    const id = formData.get('id') as string;

    try {
      console.log('Delete Action: Deleting todo', id);
      // await db.deleteTodo({ userId: locals.userId, id });
      return { success: true }; // Optional success data for $page.form
    } catch (err) {
      console.error(err);
      return fail(500, { error: 'Failed to delete todo.' });
    }
  },

  // Named action for toggling status
  toggle: async ({ request, locals }) => {
    const formData = await request.formData();
    const id = formData.get('id') as string;
    const done = !!formData.get('done'); // Convert to boolean

     try {
      console.log(`Toggle Action: Setting todo ${id} to ${done}`);
      // await db.updateTodoStatus({ userId: locals.userId, id, done });
      // No return needed, loader will re-run
    } catch (err) {
      console.error(err);
      return fail(500, { error: 'Failed to update todo status.' });
    }
  }
};
```

**2. Use Forms in Component (`+page.svelte`):**

```svelte
<!-- src/routes/todos/+page.svelte -->
<script lang="ts">
  import type { PageData, ActionData } from './$types';
  import { enhance } from '$app/forms'; // Import enhance action
  import { page } from '$app/stores'; // Import page store for form data

  export let data: PageData; // Data from load()
  export let form: ActionData; // Data from the most recent action (fail() or json())

  // Reactive variables for convenience
  $: ({ todos } = data);
  $: errors = form?.errors; // Access errors returned by fail()
  $: successMessage = form?.successMessage; // Access success data returned by json()

  // Reset form error when input changes (optional UX improvement)
  $: if (form?.text) errors = undefined;

</script>

<h1>Todos</h1>

<!-- Form for default action (Add Todo) -->
<form method="POST" use:enhance> {/* use:enhance enables progressive enhancement */}
  <label>
    New Todo:
    <input
      type="text"
      name="text"
      aria-invalid={!!errors?.text}
      bind:value={form?.text ?? ''} {/* Pre-fill on error */}
    />
  </label>
  <button type="submit">Add</button>
  {#if errors?.text}
    <em style="color: red;">{errors.text}</em>
  {/if}
  {#if errors?.form}
    <p style="color: red;">{errors.form}</p>
  {/if}
</form>

<!-- List of Todos -->
<ul>
  {#each todos as todo (todo.id)}
    <li>
      <form method="POST" action="?/toggle" use:enhance style="display: inline;">
        <input type="hidden" name="id" value={todo.id} />
        <input type="hidden" name="done" value={!todo.done} />
        <input type="checkbox" checked={todo.done} on:change={(e) => e.currentTarget.form?.requestSubmit()} />
      </form>

      <span style:text-decoration={todo.done ? 'line-through' : 'none'}>
        {todo.text}
      </span>

      <!-- Form for named action (Delete Todo) -->
      <form method="POST" action="?/delete" use:enhance style="display: inline;">
        <input type="hidden" name="id" value={todo.id} />
        <button type="submit" aria-label="Delete todo">❌</button>
      </form>
    </li>
  {/each}
</ul>

{#if successMessage}
  <p style="color: green;">{successMessage}</p>
{/if}

<style>
  li { margin-bottom: 0.5em; }
  input[type="checkbox"] { margin-right: 0.5em; }
  button[aria-label="Delete todo"] { margin-left: 0.5em; border: none; background: none; cursor: pointer; }
</style>
```

SvelteKit Actions provide a powerful, progressively enhanced way to handle data mutations directly within your route modules, keeping server logic secure and simplifying data flow between client and server. Use `fail()` for validation errors and leverage `use:enhance` and `$page.form` for a smooth client-side experience.

*(Refer to the official SvelteKit documentation on Form Actions.)*