# SvelteKit Dev: State Management

SvelteKit leverages Svelte's core state management features: Stores and the Context API.

## 1. Svelte Stores (`svelte/store`)

*   **Purpose:** The primary way to manage shared, reactive state accessible by multiple, unrelated components. Stores notify subscribers when their value changes.
*   **Location:** Define stores in `.js` or `.ts` files, typically within `src/lib/stores/`.
*   **Types:**
    *   `writable(initialValue)`: Value can be updated via `set(value)` or `update(callback)`.
    *   `readable(initialValue, start?)`: Value set internally, often via the `start` function (e.g., timers, external subscriptions). Cannot be set directly from outside.
    *   `derived(store | [stores], callback)`: Value derived reactively from other stores. `callback` re-runs when source stores change.
*   **Subscription:**
    *   **Auto-subscription (`$` prefix):** Use `$myStore` in component `<script>` or template. Handles subscribe/unsubscribe automatically.
    *   **Manual:** Use `store.subscribe(callback)` method (requires manual unsubscription, usually in `onDestroy`).
*   **SvelteKit Stores (`$app/stores`):** SvelteKit provides built-in readable stores:
    *   `page`: Contains page data (`url`, `params`, `route`, `status`, `error`, `data`, `form`).
    *   `navigating`: Contains navigation target info (`from`, `to`) during client-side navigation, or `null`.
    *   `updated`: A readable store whose value is `true` if the app has been updated since the user loaded the page (useful for service workers).

```typescript
// src/lib/stores/userStore.ts
import { writable, derived } from 'svelte/store';
import { page } from '$app/stores'; // Example using built-in store

export interface User { id: string; name: string; email?: string; }

// Writable store for the current user
export const currentUser = writable<User | null>(null);

// Derived store for user's initials
export const userInitials = derived(currentUser, ($user) => {
  return $user ? $user.name.split(' ').map(n => n[0]).join('') : '?';
});

// Derived store combining page data and user state
export const pageTitle = derived(
  [page, currentUser],
  ([$page, $user]) => {
    if ($page.data?.title) return $page.data.title;
    if ($user) return `Dashboard for ${$user.name}`;
    return 'SvelteKit App';
  }
);
```

## 2. Context API (`svelte`)

*   **Purpose:** Pass data down the component tree without prop drilling. Useful for making data available to a specific subtree.
*   **Not Reactive:** Context itself is **not** reactive. If the provided value changes, consuming components **do not** automatically update unless the value itself is a reactive store.
*   **API:**
    *   `setContext(key, value)`: Called in a parent component to associate a `value` with a `key`.
    *   `getContext(key)`: Called in a descendant component to retrieve the `value` associated with the `key`.
*   **Use Case:** Often used to provide stores, API clients, or other non-reactive configuration to a specific part of the component tree.

```svelte
<!-- src/routes/settings/+layout.svelte (Parent providing context) -->
<script lang="ts">
  import { setContext } from 'svelte';
  import { writable } from 'svelte/store';
  import type { Writable } from 'svelte/store';

  interface Settings { theme: string; }
  const settingsStore = writable<Settings>({ theme: 'light' });

  // Provide the *store* via context
  setContext('settings-store', settingsStore);

  // Provide a non-reactive value
  setContext('api-client', { call: async (endpoint: string) => { /*...*/ } });
</script>

<slot />
```

```svelte
<!-- src/routes/settings/appearance/+page.svelte (Child consuming context) -->
<script lang="ts">
  import { getContext } from 'svelte';
  import type { Writable } from 'svelte/store';

  interface Settings { theme: string; }
  interface ApiClient { call: (endpoint: string) => Promise<any>; }

  // Get the store from context
  const settings = getContext<Writable<Settings>>('settings-store');
  // Get the non-reactive value
  const apiClient = getContext<ApiClient>('api-client');

  function toggleTheme() {
    settings.update(s => ({ ...s, theme: s.theme === 'light' ? 'dark' : 'light' }));
  }
</script>

<p>Theme (from context store): {$settings.theme}</p>
<button on:click={toggleTheme}>Toggle Theme</button>
```

## 3. Choosing Between Stores and Context

*   Use **Stores** for reactive state shared across different parts of the application. This is the standard Svelte approach.
*   Use **Context API** primarily to pass stores or non-reactive values down a specific component subtree, avoiding prop drilling without making the state globally accessible via module imports.