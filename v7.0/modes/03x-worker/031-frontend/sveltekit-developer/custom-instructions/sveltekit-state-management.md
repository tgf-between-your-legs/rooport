# SvelteKit: State Management (Stores & Context)

Managing and sharing state within SvelteKit applications.

## Core Concept: Svelte's Reactivity + Stores/Context

Svelte's built-in reactivity system handles local component state efficiently. For sharing state *between* components, SvelteKit leverages Svelte's core state management features: Stores and the Context API.

**1. Svelte Stores (`svelte/store`):**

*   **Purpose:** The primary way to manage shared state that needs to be accessed by multiple, unrelated components. Stores hold a value and notify subscribers when that value changes.
*   **Types:**
    *   `writable(initialValue)`: A store whose value can be updated from anywhere using its `set` or `update` methods.
    *   `readable(initialValue, start?)`: A store whose value cannot be set directly from outside. Its value is typically derived or set within its `start` function (e.g., setting up timers or external subscriptions).
    *   `derived(store | [stores], callback)`: A store whose value is derived from one or more other stores. The `callback` function re-runs whenever the source store(s) change.
*   **Subscription:** Components subscribe to stores using the `$` prefix auto-subscription syntax (`$myStore`) within the component's `<script>` or template. This automatically handles subscribing on mount and unsubscribing on unmount. Alternatively, use the `store.subscribe(callback)` method manually (requires manual unsubscription).
*   **Location:** Store definitions are typically placed in `.js` or `.ts` files within the `src/lib` directory (e.g., `src/lib/stores/userStore.ts`).

**2. Context API (`svelte`):**

*   **Purpose:** Passing data down the component tree without prop drilling, similar to React Context. Useful for making data available to a specific subtree of components.
*   **Not Reactive:** Unlike stores, Svelte's Context API is **not** inherently reactive. If the value provided to context changes, consuming components will *not* automatically update unless the value itself is a reactive store.
*   **API:**
    *   `setContext(key, value)`: Called in a parent component's `<script>` to associate a `value` with a `key` (can be any object, often a string or symbol).
    *   `getContext(key)`: Called in a descendant component's `<script>` to retrieve the `value` associated with the `key` by the nearest ancestor that called `setContext`.
*   **Use Case:** Often used to provide stores or other non-reactive values (like API clients) to a specific part of the component tree.

## Implementation

**1. Svelte Stores Example:**

```typescript
// src/lib/stores/counterStore.ts
import { writable, derived } from 'svelte/store';

// Writable store for the count
export const count = writable(0);

// Writable store for the step
export const step = writable(1);

// Derived store for doubled count
export const doubled = derived(count, ($count) => $count * 2);

// Custom store with methods (alternative pattern)
function createComplexCounter() {
	const { subscribe, set, update } = writable({ value: 0, lastAction: '' });

	return {
		subscribe,
		increment: (amount: number) => update(s => ({ value: s.value + amount, lastAction: 'increment' })),
		decrement: (amount: number) => update(s => ({ value: s.value - amount, lastAction: 'decrement' })),
		reset: () => set({ value: 0, lastAction: 'reset' })
	};
}
export const complexCounter = createComplexCounter();

```

```svelte
<!-- src/routes/my-counter/+page.svelte -->
<script lang="ts">
  // Import stores
  import { count, step, doubled, complexCounter } from '$lib/stores/counterStore';

  // Auto-subscribe using $ prefix
  // $: currentCount = $count; // Optional: assign to local variable if needed

  function increment() {
    count.update(n => n + $step); // Update using current step value
  }

  function decrement() {
    count.update(n => n - $step);
  }

  function reset() {
    count.set(0);
    step.set(1);
  }

  function handleComplexIncrement() {
    complexCounter.increment(5);
  }
</script>

<h2>Simple Counter</h2>
<p>Count: {$count}</p>
<p>Doubled: {$doubled}</p>
<label> Step: <input type="number" bind:value={$step} /> </label>
<button on:click={increment}>Increment by {$step}</button>
<button on:click={decrement}>Decrement by {$step}</button>
<button on:click={reset}>Reset</button>

<hr />

<h2>Complex Counter</h2>
<p>Value: {$complexCounter.value}</p>
<p>Last Action: {$complexCounter.lastAction}</p>
<button on:click={handleComplexIncrement}>Increment by 5</button>
<button on:click={() => complexCounter.reset()}>Reset Complex</button>

```

**2. Context API Example (Providing a Store):**

```typescript
// src/routes/settings/+layout.svelte (Parent providing context)
<script lang="ts">
  import { setContext } from 'svelte';
  import { writable } from 'svelte/store';

  // Create a store specific to this layout and its children
  const settingsStore = writable({ theme: 'light', fontSize: 16 });

  // Provide the store via context
  setContext('settings', settingsStore);
</script>

<div class="settings-layout">
  <h1>Settings Layout</h1>
  <slot />
</div>
```

```svelte
<!-- src/routes/settings/appearance/+page.svelte (Child consuming context) -->
<script lang="ts">
  import { getContext } from 'svelte';
  import type { Writable } from 'svelte/store';

  interface Settings { theme: string; fontSize: number; }

  // Get the store from context
  const settings = getContext<Writable<Settings>>('settings');

  function toggleTheme() {
    settings.update(s => ({ ...s, theme: s.theme === 'light' ? 'dark' : 'light' }));
  }
</script>

<h2>Appearance Settings</h2>
<p>Current Theme (from context store): {$settings.theme}</p>
<button on:click={toggleTheme}>Toggle Theme</button>
```

## Choosing Between Stores and Context

*   Use **Stores** for state that needs to be shared across different, potentially unrelated parts of your application. They are reactive and the standard Svelte way for shared state.
*   Use **Context API** primarily to pass stores or non-reactive values down a specific component subtree, avoiding prop drilling without making the state globally accessible via module imports.

SvelteKit leverages Svelte's built-in stores and context API for flexible state management, from local component state to globally shared application state.

*(Refer to the official Svelte documentation on Stores and Context API.)*