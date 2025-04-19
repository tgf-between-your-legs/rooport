# Vue.js: Testing Components & Logic

Strategies and tools for testing Vue applications, including unit and component tests.

## Core Concept: Verifying Correctness

Testing is crucial for ensuring Vue applications behave as expected, catching regressions, and enabling confident refactoring. Vue testing typically involves:

*   **Unit Testing:** Testing individual functions (especially composables or utility functions) in isolation, without rendering components. Focuses on pure logic.
*   **Component Testing:** Testing individual Vue components in isolation. Involves mounting the component, interacting with it (simulating user input, clicks), and asserting its output (rendered DOM, emitted events, state changes).
*   **End-to-End (E2E) Testing:** Testing the entire application flow by interacting with it through a browser (covered by `e2e-tester` mode).

**Common Tools:**

*   **Test Runner:** Executes tests and reports results (e.g., **Vitest**, Jest). Vitest is often preferred in Vite-based Vue projects for its speed and compatibility.
*   **Component Mounting Library:** Provides utilities to mount Vue components in a test environment (e.g., **Vue Test Utils**).
*   **DOM Testing Library:** Utilities for querying and interacting with the rendered DOM within tests (e.g., **Testing Library** - `@testing-library/vue`).
*   **Assertion Library:** Provides functions for making assertions about expected outcomes (e.g., Vitest's built-in `expect`, Chai).

## Unit Testing (with Vitest)

Focus on testing pure JavaScript/TypeScript logic, especially composables.

```typescript
// src/composables/useCounter.ts (Example from vue-composables.md)
import { ref, computed, readonly } from 'vue';
export function useCounter(initialValue: number = 0) {
  const count = ref(initialValue);
  const doubleCount = computed(() => count.value * 2);
  function increment() { count.value++; }
  function decrement() { count.value--; }
  return { count: readonly(count), doubleCount, increment, decrement };
}

// src/composables/useCounter.spec.ts (Test file)
import { describe, it, expect } from 'vitest'; // Import from Vitest
import { useCounter } from './useCounter';

describe('useCounter', () => {
  it('initializes with default value 0', () => {
    const { count } = useCounter();
    expect(count.value).toBe(0);
  });

  it('initializes with provided value', () => {
    const { count } = useCounter(10);
    expect(count.value).toBe(10);
  });

  it('increments the count', () => {
    const { count, increment } = useCounter();
    increment();
    expect(count.value).toBe(1);
    increment();
    expect(count.value).toBe(2);
  });

  it('decrements the count', () => {
    const { count, decrement } = useCounter(5);
    decrement();
    expect(count.value).toBe(4);
  });

  it('calculates doubleCount correctly', () => {
    const { count, doubleCount, increment } = useCounter(3);
    expect(doubleCount.value).toBe(6);
    increment();
    expect(doubleCount.value).toBe(8); // Computed value updates reactively
  });
});
```

## Component Testing (with Vitest & Vue Test Utils)

Mount components, interact, and assert output.

```typescript
// src/components/MyButton.vue
<script setup lang="ts">
const emit = defineEmits<{ (e: 'submit', payload: string): void }>();
const props = defineProps<{ disabled?: boolean }>();

function handleClick() {
  emit('submit', 'payload-data');
}
</script>
<template>
  <button :disabled="props.disabled" @click="handleClick">
    <slot>Default Text</slot>
  </button>
</template>

// src/components/MyButton.spec.ts
import { describe, it, expect } from 'vitest';
import { mount } from '@vue/test-utils'; // Import mount from VTU
import MyButton from './MyButton.vue';

describe('MyButton.vue', () => {
  it('renders default slot content', () => {
    const wrapper = mount(MyButton);
    expect(wrapper.text()).toContain('Default Text');
  });

  it('renders provided slot content', () => {
    const wrapper = mount(MyButton, {
      slots: {
        default: 'Click Me!',
      },
    });
    expect(wrapper.text()).toContain('Click Me!');
  });

  it('is enabled by default', () => {
    const wrapper = mount(MyButton);
    expect((wrapper.element as HTMLButtonElement).disabled).toBe(false);
  });

  it('disables button when disabled prop is true', async () => {
    const wrapper = mount(MyButton, {
      props: {
        disabled: true,
      },
    });
    expect((wrapper.element as HTMLButtonElement).disabled).toBe(true);

    // Test reactivity (optional)
    // await wrapper.setProps({ disabled: false });
    // expect((wrapper.element as HTMLButtonElement).disabled).toBe(false);
  });

  it('emits "submit" event with payload on click', async () => {
    const wrapper = mount(MyButton);

    // Trigger a click event
    await wrapper.trigger('click');

    // Assert that the event was emitted
    expect(wrapper.emitted()).toHaveProperty('submit');

    // Assert payload of the first emitted 'submit' event
    expect(wrapper.emitted('submit')?.[0]).toEqual(['payload-data']);
  });

   it('does not emit "submit" event when disabled', async () => {
    const wrapper = mount(MyButton, {
        props: { disabled: true }
    });
    await wrapper.trigger('click');
    expect(wrapper.emitted('submit')).toBeUndefined();
  });
});
```

**Key Vue Test Utils Functions:**

*   `mount()`: Creates a wrapper around a mounted component.
*   `shallowMount()`: Mounts a component without rendering its child components (stubs them). Faster, good for isolated unit tests.
*   `wrapper.find()`: Finds a DOM element or child component using CSS selectors or component references.
*   `wrapper.text()`: Gets the text content of the component/element.
*   `wrapper.html()`: Gets the rendered HTML.
*   `wrapper.trigger()`: Simulates DOM events (e.g., 'click', 'input').
*   `wrapper.emitted()`: Returns an object containing emitted events and their payloads.
*   `wrapper.setProps()`: Updates component props reactively.
*   `wrapper.vm`: Accesses the component instance (useful for checking data, computed properties in Options API).

Testing is essential for robust Vue applications. Use Vitest for running tests and Vue Test Utils (often with Testing Library) for mounting and interacting with components. Test component props, events, slots, and internal logic.

*(Refer to the official Vue Test Utils documentation and Vitest documentation.)*