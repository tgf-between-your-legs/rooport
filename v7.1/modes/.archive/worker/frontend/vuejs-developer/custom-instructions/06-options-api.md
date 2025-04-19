# Vue.js: Options API (Legacy / Reference)

Understanding the Options API for structuring Vue components, primarily for **Vue 2** or **legacy Vue 3** codebases. **Composition API with `<script setup>` is preferred for new Vue 3 development.**

## Core Concept: Organizing by Option Type

The Options API is the traditional way of defining Vue components (dominant in Vue 2). Logic is organized into different properties (options) within the component definition object, such as `data`, `methods`, `computed`, `watch`, and lifecycle hooks.

**Key Features:**

*   **`data()` function:** Must return an object containing the component's reactive state properties.
*   **`methods` object:** Contains functions that can be called from the template or other methods (bound to the component instance `this`).
*   **`computed` object:** Contains functions that act as reactive getters. Their results are cached based on their reactive dependencies. Accessed via `this`.
*   **`watch` object:** Contains functions that run whenever a specific reactive property (usually in `data` or `props`) changes.
*   **Lifecycle Hooks:** Specific option properties (e.g., `mounted`, `created`, `updated`, `beforeDestroy`/`unmounted`) that contain functions executed at specific points in the component's lifecycle. Accessed via `this`.
*   **`props` object/array:** Defines the properties the component accepts from its parent.
*   **`emits` array/object:** Declares the events the component can emit.
*   **`this` Context:** Inside `methods`, `computed`, `watch`, and lifecycle hooks, `this` refers to the component instance, allowing access to `data`, `props`, methods, etc. Arrow functions should generally be avoided for top-level methods/computed/watchers as they don't bind `this` correctly.

## Implementation Example (Vue 3 Options API with TypeScript)

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
// Use defineComponent for better TypeScript inference with Options API
import { defineComponent, PropType } from 'vue';

export default defineComponent({
  name: 'CounterComponentOptions', // Component name

  // --- Props ---
  props: {
    initialCount: {
      type: Number,
      default: 0,
    },
    message: {
      type: String as PropType<string>, // Use PropType for complex types
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
      // Type inference for data properties can be less robust than with <script setup>
      // Consider defining an interface for the data return type for complex state
    };
  },

  // --- Computed Properties ---
  computed: {
    doubleCount(): number { // Explicit return type recommended
      return this.count * 2; // Access data via 'this'
    },
  },

  // --- Methods ---
  methods: {
    increment(): void { // Type parameters and return type
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
    // Watch data property 'count'
    count(newVal: number, oldVal: number): void {
      console.log(`Options API: Count changed from ${oldVal} to ${newVal}`);
    },
    // Watch prop 'initialCount'
    initialCount(newVal: number): void {
       console.log(`Options API: initialCount prop changed to ${newVal}`);
       // Optionally react to prop changes, e.g., reset internal state
       // this.count = newVal;
    }
  },

  // --- Lifecycle Hooks ---
  beforeCreate() {
    // 'this' data/computed/methods not available yet
  },
  created() {
    // 'this' is available, data is reactive, but DOM not mounted
  },
  mounted() {
    console.log('Options API: mounted');
    // Component is in the DOM, access via this.$el
  },
  unmounted() { // (beforeDestroy in Vue 2)
    console.log('Options API: unmounted');
    // Cleanup timers, event listeners etc.
  },
  // Other hooks: beforeMount, beforeUpdate, updated, beforeUnmount, errorCaptured, etc.
});
</script>

<style scoped>
/* Component-specific styles */
button { margin: 5px; }
</style>
```

**Comparison with Composition API:**

*   **Pros:** Can feel more structured initially for simple components due to predefined sections. Familiar to Vue 2 developers.
*   **Cons:** Logic related to a single feature can be scattered across `data`, `methods`, `computed`, `watch`, and lifecycle hooks, making complex components harder to understand and maintain. Logic reuse is less straightforward (mixins have drawbacks compared to composables). `this` context can sometimes be confusing. TypeScript integration is less ergonomic and type inference less powerful than with `<script setup>`.

While the Composition API with `<script setup>` is recommended for new Vue 3 projects, understanding the Options API is crucial for working with existing Vue 2/3 codebases or when migrating. Use `defineComponent` to improve TypeScript support when using the Options API.