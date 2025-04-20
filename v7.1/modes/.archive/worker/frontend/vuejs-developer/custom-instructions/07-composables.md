# Vue.js: Composables

Extracting and reusing stateful logic across components using Composition API functions.

## Core Concept: Reusable Stateful Logic

Composables are functions that leverage Vue's Composition API (`ref`, `computed`, `watch`, lifecycle hooks, etc.) to encapsulate and manage stateful logic. They provide a clean, flexible, and highly reusable way to share functionality between components, representing the primary logic reuse pattern in Composition API (superior to mixins).

**Key Characteristics:**

*   **Just Functions:** Composables are regular JavaScript/TypeScript functions. Conventionally, their names start with `use` (e.g., `useMouse`, `useFetch`, `useCounter`).
*   **Use Composition API:** They internally use `ref`, `reactive`, `computed`, `watch`, `onMounted`, etc., to manage state and lifecycle.
*   **Return Reactive State:** They typically return an object containing reactive state (`ref`s or `reactive` objects) and functions that components can use. Exposing state via `readonly()` is often a good practice if the composable manages its own state updates internally.
*   **Called in `setup()` Context:** Composables **must** be called directly within a component's `<script setup>` or `setup()` function (or another composable called within `setup`). This ensures they are bound to the correct component instance context, allowing lifecycle hooks and `provide`/`inject` to work correctly. Each component calling a composable gets its own instance of the composable's state (unless the composable implements a shared state pattern intentionally).

## Creating a Composable

1.  **Define a Function:** Create a `.js` or `.ts` file (e.g., `src/composables/useFeatureName.ts`). Export a function named starting with `use`.
2.  **Use Composition API:** Inside the function, use `ref`, `reactive`, `computed`, `watch`, lifecycle hooks as needed.
3.  **Return Values:** Return an object containing the reactive state and methods you want to expose to the component.

```typescript
// src/composables/useEventListener.ts
import { onMounted, onUnmounted, isRef, unref, watch, Ref } from 'vue';

// Type definition for the target element (can be Ref, Element, or Window/Document)
type Target = Ref<EventTarget | null | undefined> | EventTarget | null | undefined;

export function useEventListener(
  target: Target,
  event: string,
  handler: (event: Event) => void
) {
  // If the target is a ref, watch it for changes.
  if (isRef(target)) {
    watch(target, (value, oldValue) => {
      oldValue?.removeEventListener(event, handler);
      value?.addEventListener(event, handler);
    });
  } else {
    // Otherwise, add the listener directly on mount.
    onMounted(() => {
      unref(target)?.addEventListener(event, handler);
    });
  }

  // Clean up the listener on unmount.
  onUnmounted(() => {
    unref(target)?.removeEventListener(event, handler);
  });
}

// src/composables/useMousePosition.ts
import { ref } from 'vue';
import { useEventListener } from './useEventListener'; // Import another composable

export function useMousePosition() {
  const x = ref(0);
  const y = ref(0);

  useEventListener(window, 'mousemove', (event) => {
    // Type assertion needed as 'mousemove' event is a MouseEvent
    const mouseEvent = event as MouseEvent;
    x.value = mouseEvent.pageX;
    y.value = mouseEvent.pageY;
  });

  // Expose the reactive coordinates
  return { x, y };
}
```

## Using a Composable in a Component

1.  **Import:** Import the composable function in your component's `<script setup>`.
2.  **Call:** Call the composable function (passing any required arguments) to get the returned reactive state and methods.
3.  **Use:** Use the returned values directly in your component's template and logic.

```vue
<script setup lang="ts">
import { useMousePosition } from '@/composables/useMousePosition'; // Import the composable
import { useCounter } from '@/composables/useCounter'; // Import another example

// Call the composable to get its returned state and methods
const { x, y } = useMousePosition();

// Can use multiple composables or instances
const { count, doubleCount, increment } = useCounter(10);
</script>

<template>
  <div>
    <h2>Mouse Position Composable</h2>
    <p>Mouse X: {{ x }}</p>
    <p>Mouse Y: {{ y }}</p>

    <h2>Counter Composable</h2>
    <p>Count: {{ count }}</p>
    <p>Double Count: {{ doubleCount }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>
```

## VueUse Library

*   **Website:** https://vueuse.org/
*   A vital collection of pre-built, high-quality, and tree-shakable composables for common tasks.
*   **Always check VueUse first** before writing your own composable for common patterns (e.g., event listeners, fetch, local storage, timers, state synchronization, element visibility, etc.).
*   Example:
    ```typescript
    import { useLocalStorage, useDebouncedRef } from '@vueuse/core';

    // Reactive ref synced with localStorage
    const storedName = useLocalStorage('my-app-user-name', 'Guest');

    // Ref that debounces updates
    const debouncedInput = useDebouncedRef('', 500); // 500ms debounce delay
    ```

Composables are the primary mechanism for logic reuse and organization in Vue 3's Composition API. They allow you to create clean, maintainable, testable, and type-safe stateful logic that can be easily shared across components. Leverage the extensive VueUse library whenever possible.