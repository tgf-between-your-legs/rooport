## Vue.js (Version Unknown) - Condensed Context Index

### Overall Purpose
Vue.js is a progressive JavaScript framework for building user interfaces. It focuses on declarative rendering and component composition, offering flexibility through its Options API and Composition API for managing state and logic.

### Core Concepts & Capabilities
*   **Component System:** Build UIs with reusable Single-File Components (SFCs - `.vue` files). Define components using either the **Options API** (`data`, `methods`, `computed`, lifecycle hooks like `mounted`) or the **Composition API** (`setup()` function or `<script setup>`, `ref`, `reactive`, `computed`, lifecycle hooks like `onMounted`).
*   **Reactivity:** Automatically track dependencies and update the DOM when state changes. Key APIs include `ref()` for primitive values (access with `.value`) and `reactive()` for objects.
*   **Template Syntax:** HTML-based syntax with directives for binding data and behavior. Includes text interpolation (`{{ msg }}`), attribute binding (`v-bind:` or `:`), event handling (`v-on:` or `@`), conditional rendering (`v-if`, `v-else`), list rendering (`v-for`), and two-way binding (`v-model`).
*   **Props & Events:** Pass data down from parent to child via `props` (declared with `defineProps` or `props` option). Communicate from child to parent using custom `events` (`$emit` or `defineEmits`).
*   **Slots:** Allow parent components to inject content into child component layouts using `<slot>` outlets (default and named slots with `#name` syntax).
*   **Composables:** Extract and reuse stateful logic across components using Composition API functions (e.g., `useMouse()`).
*   **Application Setup:** Initialize apps with `createApp()`, mount to DOM with `.mount()`. Configure global aspects like error handling (`app.config.errorHandler`). Use `create-vue` for project scaffolding.
*   **TypeScript Support:** Integrates well with TypeScript using `defineComponent` (Options API) or `<script setup lang="ts">` (Composition API) for type safety.

### Key APIs / Components / Configuration / Patterns
*   `createApp(rootComponent, rootProps?)`: Creates a Vue application instance.
*   `app.mount(selector)`: Mounts the application instance to a DOM element.
*   `ref(value)`: Creates a reactive reference object (for primitives). Access/modify via `.value`.
*   `reactive(object)`: Returns a reactive proxy of an object (deep reactivity).
*   `computed(getter)` / `computed({ get, set })`: Creates a cached reactive reference based on other reactive sources. Can be read-only or writable.
*   `watch(source, callback, options?)`: Runs a callback when reactive dependencies change.
*   `defineProps([...])` / `defineProps({...})`: Declares component props within `<script setup>`. Supports array or object syntax with validation.
*   `defineEmits([...])`: Declares events a component can emit within `<script setup>`.
*   `defineModel()`: (Vue 3.4+) Macro for simplified `v-model` implementation on components.
*   `v-model`: Directive for two-way data binding on form inputs (`<input>`, `<select>`, `<textarea>`) and components.
*   `v-bind:attribute` / `:attribute`: Binds an attribute or prop dynamically to an expression.
*   `v-on:event` / `@event`: Attaches an event listener to an element. Supports modifiers (`.prevent`, `.stop`).
*   `v-if` / `v-else-if` / `v-else`: Directives for conditional rendering.
*   `v-for="(item, index) in items"`: Directive for rendering lists from arrays or objects. Requires `:key` binding for performance.
*   `<script setup>`: Compile-time syntactic sugar for using Composition API inside SFCs. Simplifies component definition.
*   **Options API:** Component definition structure using options like `data()`, `methods: {}`, `computed: {}`, `mounted()`, `props: {}`, etc.
*   `<slot>` / `<slot name="name">`: Outlet for content provided by the parent component. Use `<template #name>` to target named slots.
*   `defineComponent({...})`: Helper function for defining components with TypeScript (primarily for Options API type inference).
*   `app.config.errorHandler`: Configuration option to set a global handler for uncaught errors from components.
*   `create-vue` (via `npm create vue@latest`, etc.): Official scaffolding tool for creating new Vue projects.

### Common Patterns & Best Practices / Pitfalls
*   **Component Naming:** Use multi-word names (PascalCase in script, PascalCase or kebab-case in template) to avoid conflicts with HTML elements (e.g., `<TodoItem>`, `<todo-item>`).
*   **Props Stability:** Avoid passing frequently changing primitive props; compute derived data in the parent if possible to optimize child updates.
*   **Reactivity:** Use `ref` for primitives/single values, `reactive` for objects. Remember `.value` for `ref`.
*   **API Choice:** `<script setup>` with Composition API is the recommended modern approach for new projects. Options API remains fully supported.
*   **Composables:** Encapsulate and reuse stateful logic (e.g., fetching data, tracking browser APIs) using composable functions.
*   **Props Validation:** Define explicit types, `required` status, `default` values, and custom `validator` functions for props to improve component robustness.
*   **Keys in `v-for`:** Always provide a unique `:key` when using `v-for` for efficient list updates.

---
This index summarizes the core concepts, APIs, and patterns for Vue.js based on the provided snippets (Source: project_journal/context/source_docs/vuejs-developer-llms-context-20250406.md). Consult the full official Vue.js documentation for exhaustive details.