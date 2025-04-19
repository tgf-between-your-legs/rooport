# Vue.js: State Management with Pinia

Using Pinia, the official state management library for Vue 3, for centralized and type-safe state.

## Core Concept: Centralized State Store

Pinia provides a store for managing state that needs to be shared across multiple components or maintained throughout the application lifecycle. It's designed to be simple, type-safe (with excellent TypeScript support), modular, and integrates well with Vue Devtools.

**Key Features:**

*   **Stores:** State is organized into modular stores. Each store holds related state, actions, and getters.
*   **`defineStore()`:** Function used to create a new store definition. Requires a unique ID and an options object (or setup function).
*   **State:** Defined using a `state` function (similar to `data` in Options API) or directly using `ref`/`reactive` in a setup function store.
*   **Getters:** Defined in the `getters` object. Equivalent to computed properties for the store. They receive `state` as the first argument.
*   **Actions:** Defined in the `actions` object. Equivalent to methods. Can be asynchronous (`async`/`await`). Can access state and other getters/actions via `this`.
*   **Usage in Components:** Import the store definition function, call it within `<script setup>` (or `setup()`) to get the store instance, and access state/getters/actions directly.
*   **TypeScript Support:** Excellent type inference and safety, especially when defining stores with TypeScript.

## Implementation Steps

1.  **Install Pinia:**
    ```bash
    npm install pinia
    # or
    yarn add pinia
    ```

2.  **Create Pinia Instance & Install Plugin:** In your main application entry point (e.g., `main.ts`), create a Pinia instance and install it as a Vue plugin.

    ```typescript
    // src/main.ts
    import { createApp } from 'vue';
    import { createPinia } from 'pinia'; // Import
    import App from './App.vue';

    const app = createApp(App);

    const pinia = createPinia(); // Create instance
    app.use(pinia); // Install plugin

    app.mount('#app');
    ```

3.  **Define a Store:** Create a new file (e.g., `src/stores/counter.ts`) and use `defineStore`.

    ```typescript
    // src/stores/counter.ts
    import { defineStore } from 'pinia';
    import { ref, computed } from 'vue'; // Can use Composition API inside setup stores

    // Option 1: Options Store (similar to Options API)
    export const useCounterStore = defineStore('counter', {
      // State: Must be a function returning the initial state
      state: () => ({
        count: 0,
        name: 'My Counter',
      }),
      // Getters: Like computed properties for the store
      getters: {
        doubleCount(state): number {
          return state.count * 2;
        },
        // Access other getters via 'this' (need explicit return type)
        doubleCountPlusOne(): number {
          return this.doubleCount + 1;
        },
      },
      // Actions: Like methods for the store
      actions: {
        increment(amount: number = 1) {
          this.count += amount; // Mutate state directly via 'this'
        },
        reset() {
          this.count = 0;
        },
        async fetchAndUpdate() {
          // Example async action
          // const data = await fetch(...);
          // this.count = data.initialCount;
        },
      },
    });

    // Option 2: Setup Store (using Composition API) - Recommended for TS
    // export const useCounterStoreSetup = defineStore('counterSetup', () => {
    //   const count = ref(0);
    //   const name = ref('My Setup Counter');
    //
    //   const doubleCount = computed(() => count.value * 2);
    //
    //   function increment(amount: number = 1) {
    //     count.value += amount;
    //   }
    //   function reset() {
    //     count.value = 0;
    //   }
    //
    //   // Return state, getters, and actions
    //   return { count, name, doubleCount, increment, reset };
    // });

    ```

4.  **Use Store in Component:** Import the store hook and call it within `<script setup>`.

    ```vue
    // src/components/CounterDisplay.vue
    <script setup lang="ts">
    import { useCounterStore } from '@/stores/counter'; // Import the store hook

    // Call the hook to get the store instance
    const counterStore = useCounterStore();

    // Access state and getters directly (they are reactive refs/computed refs)
    // No need for .value for state properties in the template
    // No need for mapState/mapGetters

    function handleIncrement() {
      // Call actions directly on the store instance
      counterStore.increment(5);
    }
    </script>

    <template>
      <div>
        <h2>{{ counterStore.name }}</h2>
        <p>Count: {{ counterStore.count }}</p>
        <p>Double Count: {{ counterStore.doubleCount }}</p>
        <p>Double + 1: {{ counterStore.doubleCountPlusOne }}</p>
        <button @click="handleIncrement">Add 5</button>
        <button @click="counterStore.reset">Reset</button>
        <!-- Directly modify state (possible but actions are preferred for complex logic) -->
        <!-- <button @click="counterStore.count++">Direct Increment</button> -->
        <!-- Patch state -->
        <!-- <button @click="counterStore.$patch({ count: counterStore.count + 10 })">Patch +10</button> -->
      </div>
    </template>
    ```

Pinia offers a simple, modular, and type-safe approach to state management in Vue 3. Define stores using `defineStore`, access them in components by calling the exported hook, and interact with state, getters, and actions directly on the store instance. Setup stores provide better TypeScript inference and align closely with the Composition API style.

*(Refer to the official Pinia documentation.)*