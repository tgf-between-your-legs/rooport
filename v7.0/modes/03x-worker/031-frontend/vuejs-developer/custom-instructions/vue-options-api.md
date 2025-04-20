# Vue.js: Options API

Understanding the Options API for structuring Vue components (primarily for Vue 2 or legacy Vue 3 codebases).

## Core Concept: Organizing by Option Type

The Options API is the traditional way of defining Vue components (dominant in Vue 2). Logic is organized into different properties (options) within the component definition object, such as `data`, `methods`, `computed`, `watch`, and lifecycle hooks.

**Key Features:**

*   **`data()` function:** Must return an object containing the component's reactive state properties.
*   **`methods` object:** Contains functions that can be called from the template or other methods (bound to the component instance `this`).
*   **`computed` object:** Contains functions that act as reactive getters. Their results are cached based on their reactive dependencies.
*   **`watch` object:** Contains functions that run whenever a specific reactive property (usually in `data` or `props`) changes.
*   **Lifecycle Hooks:** Specific option properties (e.g., `mounted`, `created`, `updated`, `beforeDestroy`/`unmounted`) that contain functions executed at specific points in the component's lifecycle.
*   **`this` Context:** Inside `methods`, `computed`, `watch`, and lifecycle hooks, `this` refers to the component instance, allowing access to `data`, `props`, and other options.

## Implementation Example (Vue 3 Options API)

```vue
<template>
  <div>
    <h2>{{ message }}</h2>
    <p>Count: {{ count }}</p>
    <p>Double Count: {{ doubleCount }}</p>
    <button @click="increment">Increment</button>
    <button @click="resetCounter">Reset</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';

export default defineComponent({
  name: 'CounterComponent', // Component name

  // --- Props ---
  props: {
    initialCount: {
      type: Number,
      default: 0,
    },
    message: {
      type: String as PropType<string>, // Use PropType for complex types with TS
      default: 'Default Message',
    },
  },

  // --- Emits ---
  emits: ['update', 'reset'], // Declare emitted events

  // --- Data ---
  // Must be a function returning the initial state object
  data() {
    return {
      count: this.initialCount, // Access props via 'this'
    };
  },

  // --- Computed Properties ---
  computed: {
    doubleCount(): number {
      return this.count * 2; // Access data via 'this'
    },
  },

  // --- Methods ---
  methods: {
    increment(): void {
      this.count++;
      this.$emit('update', this.count); // Emit event using this.$emit
    },
    resetCounter(): void {
      this.count = this.initialCount;
      this.$emit('reset');
    },
  },

  // --- Watchers ---
  watch: {
    count(newVal: number, oldVal: number): void {
      console.log(`Options API: Count changed from ${oldVal} to ${newVal}`);
    },
    // Watch props (less common, often better to use computed or react in methods)
    // initialCount(newVal: number): void {
    //   this.count = newVal; // Reset count if initialCount prop changes
    // }
  },

  // --- Lifecycle Hooks ---
  beforeCreate() {
    console.log('Options API: beforeCreate');
    // 'this' data/computed/methods not available yet
  },
  created() {
    console.log('Options API: created');
    // 'this' is available
  },
  mounted() {
    console.log('Options API: mounted');
    // Component is in the DOM
  },
  unmounted() { // (beforeDestroy in Vue 2)
    console.log('Options API: unmounted');
    // Cleanup
  },
  // Other hooks: beforeMount, beforeUpdate, updated, beforeUnmount, errorCaptured, etc.
});
</script>

<style scoped>
/* Component-specific styles */
button {
  margin: 5px;
}
</style>
```

**Comparison with Composition API:**

*   **Pros:** Can feel more structured initially for simple components due to predefined sections. Familiar to Vue 2 developers.
*   **Cons:** Logic related to a single feature can be scattered across `data`, `methods`, `computed`, `watch`, and lifecycle hooks, making complex components harder to understand and maintain. Logic reuse is less straightforward (mixins have drawbacks compared to composables). `this` context can sometimes be confusing (especially with arrow functions inside methods). TypeScript integration is slightly less ergonomic than with `<script setup>`.

While the Composition API with `<script setup>` is recommended for new Vue 3 projects, understanding the Options API is crucial for working with existing Vue 2/3 codebases or when migrating.

*(Refer to the official Vue.js documentation on Options API.)*