# Vue.js: Composables

Extracting and reusing stateful logic across components using Composition API functions.

## Core Concept: Reusable Stateful Logic

Composables are functions that leverage Vue's Composition API (`ref`, `computed`, `watch`, lifecycle hooks, etc.) to encapsulate and manage stateful logic. They provide a clean and highly reusable way to share functionality between components without the drawbacks of older patterns like mixins.

**Key Characteristics:**

*   **Just Functions:** Composables are regular JavaScript/TypeScript functions. Conventionally, their names start with `use` (e.g., `useMouse`, `useFetch`).
*   **Use Composition API:** They internally use `ref`, `reactive`, `computed`, `watch`, `onMounted`, etc., to manage state and lifecycle.
*   **Return Reactive State:** They typically return an object containing reactive state (`ref`s or `reactive` objects) and functions that components can use.
*   **Called in `setup()`:** Composables are designed to be called directly within a component's `<script setup>` or `setup()` function to ensure they are bound to the correct component instance context (especially for lifecycle hooks).

## Creating a Composable

1.  **Define a Function:** Create a `.js` or `.ts` file (e.g., `src/composables/useCounter.ts`). Export a function named starting with `use`.
2.  **Use Composition API:** Inside the function, use `ref`, `reactive`, `computed`, `watch`, lifecycle hooks as needed.
3.  **Return Values:** Return an object containing the reactive state and methods you want to expose to the component.

```typescript
// src/composables/useCounter.ts
import { ref, computed, readonly, onMounted } from 'vue';

// The composable function
export function useCounter(initialValue: number = 0) {
  // --- State ---
  // Internal reactive state
  const count = ref(initialValue);

  // --- Getters (Computed) ---
  // Computed property derived from state
  const doubleCount = computed(() => count.value * 2);

  // --- Actions (Methods) ---
  // Function to modify the state
  function increment() {
    count.value++;
  }

  function decrement() {
    count.value--;
  }

  // --- Lifecycle ---
  onMounted(() => {
    console.log(`Counter initialized with ${count.value}`);
  });

  // --- Return Exposed Values ---
  // Expose state (often readonly if direct mutation isn't intended from component)
  // Expose methods to interact with the state
  return {
    count: readonly(count), // Expose count as readonly ref
    // count, // Or expose the mutable ref directly
    doubleCount, // Expose computed property
    increment,   // Expose method
    decrement,
  };
}
```

## Using a Composable in a Component

1.  **Import:** Import the composable function in your component's `<script setup>`.
2.  **Call:** Call the composable function to get the returned reactive state and methods.
3.  **Use:** Use the returned values directly in your component's template and logic.

```vue
<script setup lang="ts">
import { useCounter } from '@/composables/useCounter'; // Import the composable

// Call the composable to get its returned state and methods
const { count, doubleCount, increment, decrement } = useCounter(10); // Start with initial value 10

// Can use multiple instances if needed
// const { count: count2, increment: increment2 } = useCounter(100);
</script>

<template>
  <div>
    <h2>Counter Composable</h2>
    <p>Count: {{ count }}</p>
    <p>Double Count: {{ doubleCount }}</p>
    <button @click="increment">Increment</button>
    <button @click="decrement">Decrement</button>

    <!-- Example using a second instance -->
    <!-- <p>Count 2: {{ count2 }}</p> -->
    <!-- <button @click="increment2">Increment 2</button> -->
  </div>
</template>
```

## VueUse Library

*   **Website:** https://vueuse.org/
*   A popular and comprehensive collection of pre-built, high-quality composables for common tasks like:
    *   Tracking mouse position (`useMouse`)
    *   Detecting element visibility (`useIntersectionObserver`)
    *   Fetching data (`useFetch`)
    *   Managing browser storage (`useLocalStorage`, `useSessionStorage`)
    *   Handling timers (`useIntervalFn`)
    *   And many, many more.
*   Highly recommended to check VueUse before writing your own composable for common patterns.

```typescript
// Example using VueUse
import { useLocalStorage } from '@vueuse/core';

const storedName = useLocalStorage('my-app-user-name', 'Guest'); // Key, default value

// storedName.value is reactive and persists in localStorage
```

Composables are the primary mechanism for logic reuse and organization in Vue 3's Composition API. They allow you to create clean, maintainable, and testable stateful logic that can be easily shared across components.

*(Refer to the official Vue.js documentation on Composables.)*