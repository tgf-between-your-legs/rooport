# SvelteKit: Advanced Routing Features

Exploring optional parameters, rest parameters, and route guards in SvelteKit routing.

## 1. Optional Parameters (`[[param]]`)

*   **Purpose:** Define route segments that are optional. The route matches whether the segment is present or not.
*   **Syntax:** Wrap the parameter name in double square brackets in the folder or file name.
*   **Example:** `src/routes/users/[[id]]/+page.svelte`
    *   Matches `/users` (`params.id` will be `undefined`).
    *   Matches `/users/123` (`params.id` will be `"123"`).
*   **Use Case:** Useful for pages that can optionally display details for a specific item, like a user profile page that also serves as a general user listing or settings page when no ID is provided.

```typescript
// src/routes/users/[[id]]/+page.server.ts
import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';
// import { getUserList, getUserById } from '$lib/server/db';

export const load: PageServerLoad = async ({ params }) => {
  if (params.id) {
    // If ID is present, load specific user
    // const user = await getUserById(params.id);
    const user = { id: params.id, name: `User ${params.id}` }; // Placeholder
    if (!user) {
      error(404, 'User not found');
    }
    return { user }; // Return single user object
  } else {
    // If ID is not present, load list of users
    // const users = await getUserList();
    const users = [{ id: '1', name: 'Alice' }, { id: '2', name: 'Bob' }]; // Placeholder
    return { users }; // Return users array
  }
};
```

```svelte
<!-- src/routes/users/[[id]]/+page.svelte -->
<script lang="ts">
  import type { PageData } from './$types';
  export let data: PageData;

  // data will contain either { user: ... } or { users: [...] }
  $: user = data.user;
  $: users = data.users;
</script>

{#if user}
  <h1>User Profile: {user.name}</h1>
  <!-- Display user details -->
{:else if users}
  <h1>User List</h1>
  <ul>
    {#each users as u}
      <li><a href="/users/{u.id}">{u.name}</a></li>
    {/each}
  </ul>
{:else}
  <p>Loading...</p> <!-- Or handle error state -->
{/if}
```

## 2. Rest Parameters (`[...param]`)

*   **Purpose:** Match *one or more* path segments at a specific point in the route.
*   **Syntax:** Use square brackets with three dots `[...]` around the parameter name. Must be at the *end* of a route path within a directory, or as a filename itself.
*   **Example:** `src/routes/files/[...path]/+page.svelte`
    *   Matches `/files/a` (`params.path` is `"a"`).
    *   Matches `/files/a/b/c` (`params.path` is `"a/b/c"`).
    *   Does **not** match `/files`.
*   **Use Case:** Catching arbitrary file paths, documentation pages with nested sections.

```typescript
// src/routes/docs/[...slug]/+page.server.ts
import type { PageServerLoad } from './$types';
import { error } from '@sveltejs/kit';
// import { getDocContent } from '$lib/server/docs';

export const load: PageServerLoad = async ({ params }) => {
  const slug = params.slug; // e.g., "getting-started/installation"
  console.log(`Loading doc for: ${slug}`);
  // const content = await getDocContent(slug);
  const content = `Content for ${slug}`; // Placeholder

  if (!content) {
    error(404, 'Document not found');
  }
  return { slug, content };
};
```

## 3. Route Guards (Protection)

SvelteKit doesn't have built-in middleware specifically for route guarding like some frameworks, but you can implement guards using:

*   **Server `load` Functions:** Check authentication or permissions within a `+layout.server.js` or `+page.server.js`. If checks fail, use `redirect()` or `error()`. This is the most common and recommended approach.

    ```typescript
    // src/routes/admin/+layout.server.ts (Protect all routes under /admin)
    import type { LayoutServerLoad } from './$types';
    import { redirect } from '@sveltejs/kit';
    // import { requireAdminUser } from '$lib/server/auth';

    export const load: LayoutServerLoad = async ({ locals }) => {
      // if (!locals.user?.isAdmin) {
      if (!locals.user) { // Simplified check using locals from hooks.server.js
        console.log('Admin access denied, redirecting to login.');
        redirect(303, '/login?redirectTo=/admin');
      }
      console.log('Admin access granted.');
      // No need to return anything specific if just guarding
      return {};
    };
    ```

*   **`handle` Hook (`src/hooks.server.js`):** Perform checks within the global `handle` hook based on `event.url.pathname`. Can redirect or modify `event.locals` for use in loaders. Suitable for global rules or setting up user context. (See `sveltekit-hooks.md`).

Choose the appropriate routing feature based on whether segments are optional, need to capture multiple parts, or require server-side protection before loading or rendering.

*(Refer to the official SvelteKit documentation on Advanced Routing.)*