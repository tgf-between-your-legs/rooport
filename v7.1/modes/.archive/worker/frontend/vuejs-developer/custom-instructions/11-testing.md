# Vue.js: Testing Components & Logic

Strategies and tools for testing Vue applications, focusing on unit and component tests.

## Core Concept: Verifying Correctness & Preventing Regressions

Testing ensures Vue components and logic behave as expected, catches regressions during development, and enables confident refactoring.

**Levels of Testing:**

*   **Unit Testing:** Testing individual, isolated functions (especially composables, utility functions) without rendering components. Focuses on pure logic.
*   **Component Testing:** Testing individual Vue components in isolation. Involves mounting the component, simulating interactions (props changes, user input, clicks), and asserting its output (rendered DOM, emitted events, internal state). This is the most common type of testing for Vue components.
*   **End-to-End (E2E) Testing:** Testing complete user flows through the entire application running in a browser (handled by `e2e-tester` mode).

**Common Tools for Vue 3 + Vite:**

*   **Test Runner:** **Vitest** (https://vitest.dev/) - Fast, Vite-native test runner with Jest-compatible API. Recommended for Vite projects.
*   **Component Mounting:** **Vue Test Utils** (VTU) (https://test-utils.vuejs.org/) - The official library for mounting Vue components in tests. Provides utilities to interact with and assert on component instances and rendered output. Use the version compatible with your Vue version (v2 for Vue 3).
*   **DOM Querying/Interaction:**
    *   VTU's built-in finders (`wrapper.find()`, `wrapper.findAll()`).
    *   **Testing Library (`@testing-library/vue`)** (https://testing-library.com/docs/vue-testing-library/intro) - Encourages testing components the way users interact with them (querying by accessible roles, text, labels). Often used alongside VTU.
*   **Assertion Library:** Vitest includes **Chai** and Jest's `expect` compatible assertions built-in.

## Unit Testing (Composables with Vitest)

Test pure logic in isolation.

```typescript
// src/composables/useCounter.spec.ts
import { describe, it, expect, beforeEach } from 'vitest';
import { useCounter } from './useCounter'; // Assuming useCounter composable exists
import { ref } from 'vue'; // Needed if composable uses Vue reactivity internally

// Composables often need to run within a simulated component context
// if they use lifecycle hooks or provide/inject.
// For simple composables like useCounter, direct calls might work.

describe('useCounter', () => {
  let counter;

  // Optional: Setup before each test
  beforeEach(() => {
    // Create a fresh instance for each test
    counter = useCounter(5); // Example initial value
  });

  it('initializes count correctly', () => {
    expect(counter.count.value).toBe(5);
  });

  it('increments the count', () => {
    counter.increment();
    expect(counter.count.value).toBe(6);
  });

  it('decrements the count', () => {
    counter.decrement();
    expect(counter.count.value).toBe(4);
  });

  it('calculates doubleCount', () => {
    expect(counter.doubleCount.value).toBe(10);
    counter.increment();
    expect(counter.doubleCount.value).toBe(12);
  });
});
```

## Component Testing (with Vitest & VTU)

Mount components, interact, and assert output/behavior.

```typescript
// src/components/MyButton.spec.ts
import { describe, it, expect } from 'vitest';
import { mount } from '@vue/test-utils'; // Import mount from VTU
import MyButton from './MyButton.vue'; // The component to test

describe('MyButton.vue', () => {
  it('renders slot content', () => {
    const wrapper = mount(MyButton, {
      slots: {
        default: 'Click Me', // Provide slot content
      },
    });
    // Assert text content
    expect(wrapper.text()).toContain('Click Me');
    // Assert rendered HTML structure (use sparingly)
    // expect(wrapper.html()).toContain('<button>Click Me</button>');
  });

  it('applies disabled attribute based on prop', async () => {
    const wrapper = mount(MyButton, {
      props: {
        disabled: true,
      },
    });
    // Find the button element and check its disabled property
    expect(wrapper.find('button').element.disabled).toBe(true);

    // Test reactivity: Update props and assert change
    await wrapper.setProps({ disabled: false });
    expect(wrapper.find('button').element.disabled).toBe(false);
  });

  it('emits "submit" event with payload on click', async () => {
    const wrapper = mount(MyButton);
    const button = wrapper.find('button'); // Find the button element

    // Simulate a click event on the button
    await button.trigger('click');

    // Assert that the 'submit' event was emitted
    expect(wrapper.emitted()).toHaveProperty('submit');

    // Assert the payload of the first emitted 'submit' event
    // emitted() returns an array of arrays, where each inner array contains the arguments for one emission
    expect(wrapper.emitted('submit')?.[0]).toEqual(['payload-data']); // Assuming 'payload-data' is the expected payload
  });

  it('does not emit "submit" event when disabled', async () => {
    const wrapper = mount(MyButton, {
      props: { disabled: true },
    });
    await wrapper.find('button').trigger('click');
    // Assert that the 'submit' event was NOT emitted
    expect(wrapper.emitted('submit')).toBeUndefined();
  });

  // Example using Testing Library (if installed and preferred)
  // import { render, screen, fireEvent } from '@testing-library/vue';
  // it('renders slot content (Testing Library)', () => {
  //   render(MyButton, { slots: { default: 'Click Me TL' } });
  //   expect(screen.getByRole('button', { name: /Click Me TL/i })).toBeInTheDocument();
  // });
  // it('emits submit on click (Testing Library)', async () => {
  //   const { emitted } = render(MyButton);
  //   await fireEvent.click(screen.getByRole('button'));
  //   expect(emitted()).toHaveProperty('submit');
  //   expect(emitted().submit[0]).toEqual(['payload-data']);
  // });
});
```

**Key Testing Practices:**

*   **Arrange, Act, Assert:** Structure tests clearly.
*   **Test Behavior, Not Implementation:** Focus on what the component does from a user's perspective (renders correct output, emits events on interaction) rather than internal implementation details. Testing Library encourages this.
*   **Isolation:** Test components individually. Mock dependencies (stores, router, child components, composables) where necessary using Vitest's mocking features (`vi.mock`) or VTU's `global.plugins`, `global.stubs`.
*   **Coverage:** Aim for reasonable test coverage, focusing on critical paths and logic. Use Vitest's coverage reporting (`vitest run --coverage`).
*   **Readability:** Write clear and descriptive test names (`it(...)`).

Testing is essential for robust Vue applications. Use Vitest for running tests and Vue Test Utils (optionally with Testing Library) for mounting and interacting with components. Test props, events, slots, and user interactions.