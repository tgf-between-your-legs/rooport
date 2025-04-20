# Vue.js: State Management (Pinia & Vuex)

Managing shared state across components using centralized stores.

## Core Concept: Centralized State

When multiple components need to access or modify the same piece of data, or when you need to maintain state across different views/routes, a centralized state management solution is necessary. It provides a single source of truth and predictable ways to update the state.

*   **Pinia:** The **official and recommended** state management library for Vue 3. Simple, type-safe, modular, and integrates well with Composition API and DevTools.
*   **Vuex:** The previous official library, common in Vue 2 and older Vue 3 projects. More boilerplate and less type-safe compared to Pinia.

**Choose Pinia for new Vue 3 projects.** Understand Vuex for maintaining legacy projects.

## 1. Pinia (Recommended for Vue 3)

*   **Website:** https://pinia.vuejs.org/
*   **Key Idea:** Organize state into modular "stores". Each store manages a specific domain of state (e.g., user authentication, shopping cart, UI settings).

**Setup:**

1.  Install: `npm install pinia`
2.  Register Plugin:
    ```typescript
    // src/main.ts
    import { createApp } from 'vue';
    import { createPinia } from 'pinia';
    import App from './App.vue';

    const app = createApp(App);
    app.use(createPinia()); // Use the pinia instance
    app.mount('#app');
    ```

**Defining a Store (`defineStore`):**

*   Use a unique ID (string) for the store.
*   Define using either an **Options Object** (similar to Options API) or a **Setup Function** (similar to `<script setup>`, recommended for TS).

```typescript
// src/stores/counter.ts
import { defineStore } from 'pinia';
import { ref, computed } from 'vue'; // For Setup Store

// --- Option 1: Options Store ---
export const useCounterStoreOptions = defineStore('counterOptions', {
  state: () => ({ // State must be a function
    count: 0,
    name: 'My Counter',
  }),
  getters: { // Like computed properties
    doubleCount(state): number {
      return state.count * 2;
    },
    // Access other getters via 'this' (needs explicit return type)
    doublePlusOne(): number {
      return this.doubleCount + 1;
    },
  },
  actions: { // Like methods, can be async
    increment(amount: number = 1) {
      this.count += amount; // Mutate state via 'this'
    },
    async resetAsync() {
      // await someAsyncTask();
      this.count = 0;
    },
  },
});

// --- Option 2: Setup Store (Recommended for TS) ---
export const useCounterStoreSetup = defineStore('counterSetup', () => {
  // State (reactive refs)
  const count = ref(0);
  const name = ref('My Setup Counter');

  // Getters (computed refs)
  const doubleCount = computed(() => count.value * 2);

  // Actions (functions)
  function increment(amount: number = 1) {
    count.value += amount;
  }
  async function resetAsync() {
    // await someAsyncTask();
    count.value = 0;
  }

  // Return exposed state, getters, actions
  return { count, name, doubleCount, increment, resetAsync };
});
```

**Using a Store in Components (`<script setup>`):**

```vue
<script setup lang="ts">
import { useCounterStoreSetup } from '@/stores/counter'; // Import store hook

const counterStore = useCounterStoreSetup(); // Call hook to get instance

// Access state/getters directly (they are reactive)
// No mapState/mapGetters needed
</script>

<template>
  <div>
    <h2>{{ counterStore.name }}</h2>
    <p>Count: {{ counterStore.count }}</p>
    <p>Double: {{ counterStore.doubleCount }}</p>
    <button @click="counterStore.increment(1)">Increment</button>
    <button @click="counterStore.resetAsync">Reset Async</button>
    <!-- Can also destructure (use storeToRefs for state/getters to keep reactivity) -->
    <!-- import { storeToRefs } from 'pinia'; -->
    <!-- const { count, name, doubleCount } = storeToRefs(counterStore); -->
    <!-- const { increment, resetAsync } = counterStore; -->
  </div>
</template>
```

## 2. Vuex (Legacy / Vue 2)

*   **Website:** https://vuex.vuejs.org/ (Vuex 4 for Vue 3)
*   **Key Idea:** Single global store, Flux-inspired pattern (State -> View -> Actions -> Mutations -> State).

**Core Concepts:**

*   **State:** Single state tree object.
*   **Getters:** Computed properties for the store (`store.getters.someGetter`).
*   **Mutations:** **Synchronous** functions to change state (`store.commit('MUTATION_NAME', payload)`). **Only way to modify state.**
*   **Actions:** Can be **asynchronous**. Commit mutations (`context.commit`). Dispatched via `store.dispatch('actionName', payload)`.
*   **Modules:** Split store into namespaced modules.

**Setup (Vuex 4 for Vue 3):**

1.  Install: `npm install vuex@next --save`
2.  Create & Register Store:
    ```typescript
    // src/store/index.ts (Vuex example)
    import { createStore } from 'vuex';
    export default createStore({ /* state, getters, mutations, actions */ });

    // src/main.ts
    import store from './store';
    app.use(store);
    ```

**Using Vuex in Components (`<script setup>`):**

```typescript
import { computed } from 'vue';
import { useStore } from 'vuex'; // Import useStore hook

const store = useStore(); // Get store instance

// Access state (wrap in computed for reactivity)
const count = computed(() => store.state.count);
// Access getters (wrap in computed)
const doubleCount = computed(() => store.getters.doubleCount);

function increment() {
  // Dispatch action
  store.dispatch('incrementAsync', { amount: 1, delay: 100 });
}
function reset() {
  // Commit mutation (less common for complex logic)
  // store.commit('SET_COUNT', 0);
  // Dispatch action
  store.dispatch('resetCounter');
}
```

**Summary:** Use **Pinia** for new Vue 3 projects due to its simplicity, type safety, and better Composition API integration. Use Vuex primarily for maintaining older projects.