# Custom Instructions for 💚 Vue.js Developer (`vuejs-developer`)

This directory contains specific instructions and guidelines for the `vuejs-developer` mode, supplementing the base system prompt.

## Instruction Files

1.  **`01-core-workflow-principles.md`**: General operational guidelines, standard workflow, API preferences (Composition API first), tool usage, error handling, and safety protocols.
2.  **`02-collaboration-escalation.md`**: Defines how this mode interacts with other specialist modes (e.g., styling, testing, backend) and when to delegate or escalate tasks.
3.  **`03-components-sfcs.md`**: Covers building Single-File Components (`.vue`), defining props (`defineProps`), emitting events (`defineEmits`), and using `defineModel` for `v-model` support.
4.  **`04-template-syntax.md`**: Details Vue's HTML-based template syntax, including interpolation, directives (`v-bind`, `v-on`, `v-if`, `v-for`, `v-model`), attribute binding, event handling, and slots.
5.  **`05-composition-api.md`**: Focuses on the preferred Composition API, including `<script setup>`, reactivity (`ref`, `reactive`), computed properties (`computed`), watchers (`watch`, `watchEffect`), and lifecycle hooks (`onMounted`, etc.).
6.  **`06-options-api.md`**: Explains the legacy Options API (`data`, `methods`, `computed`, `watch`, lifecycle hooks) for reference when working with older codebases.
7.  **`07-composables.md`**: Describes creating and using composable functions for reusable stateful logic, including leveraging the VueUse library.
8.  **`08-state-management.md`**: Covers centralized state management, focusing on Pinia (recommended) and providing context on Vuex (legacy).
9.  **`09-routing.md`**: Details client-side navigation using Vue Router, including setup, route definition, `<router-link>`, `<router-view>`, programmatic navigation, and navigation guards.
10. **`10-typescript-integration.md`**: Guides on effectively using TypeScript within Vue components, especially with `<script setup>`, for type safety in props, emits, state, refs, etc.
11. **`11-testing.md`**: Outlines strategies for unit and component testing using Vitest and Vue Test Utils (VTU).
12. **`12-performance.md`**: Provides techniques for optimizing Vue application runtime performance (rendering, updates, large lists).
13. **`13-build-tools.md`**: Overview of build tool integration, primarily focusing on Vite (recommended) and mentioning Vue CLI/Webpack (legacy).
14. **`14-ssr-basics.md`**: Conceptual explanation of Server-Side Rendering (SSR), hydration, universal code considerations, and the role of frameworks like Nuxt.js.