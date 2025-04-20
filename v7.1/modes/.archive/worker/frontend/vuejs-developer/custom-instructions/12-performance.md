# Vue.js: Performance Optimization

Techniques for improving the runtime rendering performance and responsiveness of Vue applications. (Bundle size optimization is primarily handled by the build tool, e.g., Vite).

## Core Concept: Efficient Rendering & Updates

Vue's reactivity system is generally efficient, but performance bottlenecks can arise, especially in complex applications. Optimization focuses on minimizing unnecessary work during component rendering, updates, and initialization.

**Key Areas for Runtime Performance:**

*   **Component Re-renders:** Minimize the scope and frequency of component updates triggered by reactive changes.
*   **Computed Properties:** Cache expensive calculations derived from reactive state.
*   **Watchers:** Avoid overuse or inefficient watchers that trigger complex logic frequently.
*   **Large Lists:** Efficiently render and update long lists of data.
*   **Component Initialization:** Optimize logic within `setup()` or lifecycle hooks that might delay initial rendering.

## Common Optimization Techniques

1.  **Minimize Reactivity Scope:**
    *   Use `shallowRef()` and `shallowReactive()` for large objects or arrays where deep reactivity (tracking changes within nested properties) is not required. This reduces Vue's overhead in tracking changes.
    *   Use `readonly()` when passing reactive objects/arrays to child components or composables that should not modify them, potentially allowing Vue further optimization.

2.  **Optimize `v-for` List Rendering:**
    *   **Mandatory `:key`:** Always provide a unique and stable `:key` attribute for each item in a `v-for` loop. This allows Vue to efficiently track, reuse, and reorder elements instead of recreating them. **Do not use `index` as a key** if the list order can change or items can be inserted/deleted, as this leads to incorrect updates and performance issues. Use a unique ID from the data item itself.
    *   **Virtual Scrolling:** For very long lists (hundreds/thousands of items), implement virtual scrolling using libraries like `vue-virtual-scroller` or `@tanstack/vue-virtual`. This renders only the items currently visible in the viewport, drastically improving performance.
    *   **Keep Loop Body Simple:** Avoid complex expressions or heavy component rendering directly inside `v-for`. Move calculations to `computed` properties or methods outside the loop if possible.

3.  **Conditional Rendering (`v-if` vs. `v-show`):**
    *   **`v-if`:** "True" conditional rendering. Elements and components within `v-if` are destroyed and recreated when the condition changes. Higher toggle cost, but lower initial render cost if the condition is initially false. Use when the condition changes infrequently or when the conditional block is heavy.
    *   **`v-show`:** Toggles the element's CSS `display: none;` property. The element is always rendered in the DOM. Lower toggle cost, but higher initial render cost. Use for elements that need to be toggled frequently (e.g., based on user interaction).

4.  **Efficient Computed Properties:**
    *   Leverage caching: Computed properties only re-evaluate when their reactive dependencies change. Use them for any calculation derived from reactive state, especially if it's computationally intensive.
    *   Avoid side effects within computed getters.

5.  **Optimize Watchers (`watch`, `watchEffect`):**
    *   **Specificity:** Prefer `watch` over `watchEffect` when you need to track specific data sources, control the timing (`flush: 'post'`), or access old/new values. `watchEffect` is simpler for direct side effects based on automatically tracked dependencies.
    *   **Debounce/Throttle:** For watchers triggered by frequent updates (e.g., user input, window resize), debounce or throttle the handler function using utilities like `watchDebounced` or `watchThrottled` from VueUse, or Lodash's `debounce`/`throttle`. This limits how often the expensive handler logic runs.
    *   **Cleanup:** Clean up side effects (e.g., timers, manual event listeners) created within `watchEffect` by returning a cleanup function from the effect callback. `watch` can be stopped explicitly by calling the function it returns.
    *   **`deep: false`:** When watching reactive objects/arrays, use `deep: false` (default) if you only care about the reference changing, not nested property mutations. Use `deep: true` cautiously as it can be expensive.

6.  **Lazy Loading Components & Routes:**
    *   Use dynamic imports (`const Comp = () => import('./MyComponent.vue')`) for components that are not needed on the initial page load (e.g., modals, components in inactive tabs, components below the fold).
    *   Lazy load route components in Vue Router (see `09-routing.md`). This leverages build tool code splitting, reducing the initial bundle size.

7.  **Keep Components Small & Focused:** Decompose large, complex components into smaller, more manageable ones. This improves reusability, testability, and can limit the scope of unnecessary re-renders.

8.  **Use `v-once`:** For parts of the template that contain static content derived from initial state and never need to update, use the `v-once` directive. Vue will skip future updates for that element and all its children.

9.  **Functional Components (Rare in Vue 3):** While functional components offered performance benefits in Vue 2 due to being stateless, the difference is negligible in Vue 3 with Composition API. Prefer standard components with `<script setup>`.

10. **Server-Side Rendering (SSR) / Static Site Generation (SSG):** Can improve perceived initial load performance (Time-to-Content) by sending rendered HTML from the server or pre-rendering at build time (see `14-ssr-basics.md`). Often managed by frameworks like Nuxt.js.

## Profiling Performance

*   **Vue Devtools:** Use the "Performance" tab (or "Timeline" tab with "Component Renders" enabled) to record and analyze component render times, update frequency, and event handling. Identify components that render too often or take too long.
*   **Browser DevTools (Performance Tab):** Profile JavaScript execution time using the browser's built-in profiler to find bottlenecks in component logic, watchers, or expensive computations within your code.

**General Approach:** Profile first to identify actual bottlenecks. Focus on optimizing component re-renders, efficiently handling large lists, and leveraging computed properties. Apply optimizations strategically based on profiling data.