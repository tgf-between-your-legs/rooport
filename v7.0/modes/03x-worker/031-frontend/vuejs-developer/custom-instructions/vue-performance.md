# Vue.js: Performance Optimization

Techniques for improving the runtime and rendering performance of Vue applications.

## Core Concept: Efficient Rendering & Updates

Vue's reactivity system is generally efficient, but performance bottlenecks can arise in complex applications. Optimization focuses on minimizing unnecessary work during rendering, updates, and component initialization.

**Key Areas:**

*   **Re-renders:** Components re-render when their reactive dependencies change. Minimizing the scope and frequency of re-renders is crucial.
*   **Computed Properties:** Expensive computations should be cached using `computed`.
*   **Watchers:** Overuse or inefficient watchers can impact performance.
*   **Large Lists:** Rendering very long lists can block the main thread.
*   **Component Initialization:** Complex logic in `setup()` or lifecycle hooks can delay rendering.
*   **Bundle Size:** Large JavaScript bundles increase load times (handled primarily by build tool optimization - see `vite-performance.md`).

## Common Optimization Techniques

1.  **Minimize Reactivity Scope:**
    *   Use `shallowRef()` and `shallowReactive()` when deep reactivity isn't needed for large objects or arrays. This prevents Vue from traversing the entire structure on changes.
    *   Use `readonly()` to prevent accidental mutations of objects that shouldn't change, which can sometimes help Vue optimize updates.

2.  **Optimize `v-for`:**
    *   **Always use `:key`:** Provide a unique and stable key for each item to help Vue efficiently track, reuse, and reorder elements. Avoid using `index` as a key if the list order can change or items can be inserted/deleted.
    *   **Virtual Scrolling:** For very long lists (hundreds/thousands of items), use virtual scrolling libraries (e.g., `vue-virtual-scroller`, `vue-virtual-scroll-grid`) to render only the visible items in the viewport.
    *   **Avoid Complex Expressions in Template:** Keep expressions within `v-for` loops simple. Move complex calculations to `computed` properties or methods.

3.  **Conditional Rendering (`v-if` vs. `v-show`):**
    *   **`v-if`:** "Real" conditional rendering. Elements are destroyed and recreated when the condition changes. Higher toggle cost, lower initial render cost if condition is initially false. Use when the condition doesn't change often.
    *   **`v-show`:** Toggles the element's CSS `display` property. Element is always rendered, just hidden/shown. Lower toggle cost, higher initial render cost. Use for elements that need to be toggled frequently.

4.  **Efficient Computed Properties:**
    *   Leverage caching: Computed properties only re-evaluate when their reactive dependencies change. Use them for expensive calculations based on reactive state.
    *   Avoid side effects within computed getters.

5.  **Optimize Watchers (`watch`, `watchEffect`):**
    *   **Specificity:** Use `watch` to track specific data sources rather than `watchEffect` if you don't need immediate execution or automatic dependency tracking, as `watch` is lazier.
    *   **Debounce/Throttle:** For watchers triggered by frequent updates (like user input), debounce or throttle the handler function to limit how often it runs. (Use libraries like Lodash's `debounce` or VueUse's `watchDebounced`).
    *   **Cleanup:** Clean up side effects (e.g., timers, event listeners) created within `watchEffect` by returning a cleanup function. `watch` can be stopped using the returned handler function.
    *   **`deep: false`:** If watching reactive objects, consider `deep: false` (default) if you only care about identity changes, not nested property changes.

6.  **Lazy Loading Components:**
    *   Use dynamic imports (`const Comp = () => import('./MyComponent.vue')`) for components that are not needed immediately (e.g., components associated with specific routes, modals shown on demand). This leverages build tool code splitting.

7.  **Keep Components Small & Focused:** Break down large components into smaller, more manageable ones. This can improve reusability and potentially limit the scope of re-renders.

8.  **Use `v-once`:** For parts of the template that render once and never need to update, use the `v-once` directive to skip future updates for that element and its children.

9.  **Functional Components (Less Common in Vue 3):** In Vue 2, functional components offered performance benefits as they were stateless. In Vue 3, the performance difference is negligible, and `<script setup>` provides better organization.

10. **Server-Side Rendering (SSR):** Improves perceived initial load time by sending rendered HTML from the server (see `vue-ssr-basics.md`).

## Profiling

*   **Vue Devtools:** Use the "Performance" tab to record and analyze component render times, event handling, and state updates. Identify components that re-render frequently or take a long time to render.
*   **Browser DevTools (Performance Tab):** Profile JavaScript execution time to find bottlenecks in component logic, watchers, or expensive computations.

Focus on optimizing component re-renders, efficiently handling large lists, and using computed properties effectively. Profile your application using Vue Devtools to identify specific bottlenecks before applying optimizations.

*(Refer to the official Vue.js documentation on Performance.)*