# Vue.js: State Management with Vuex (Legacy)

Understanding Vuex for state management, primarily for Vue 2 or existing Vue 3 projects using it.

## Core Concept: Centralized State Pattern (Flux-inspired)

Vuex was the official state management library for Vue 2 and is still usable in Vue 3, although **Pinia is now the recommended choice for new Vue 3 projects**. Vuex implements the Flux architecture pattern, providing a centralized store for application state with rules ensuring state changes predictably.

**Key Concepts:**

*   **Store:** A single container holding the entire application state.
*   **State:** The raw data object (similar to `data` in a component). Should be the single source of truth.
*   **Getters:** Computed properties for the store. Used to derive state based on store state (e.g., filtered lists). Results are cached. Accessed via `store.getters`.
*   **Mutations:** The **only** way to actually change state in the store. Must be **synchronous** functions. Receive `state` as the first argument. Committed using `store.commit('mutationName', payload)`.
*   **Actions:** Similar to methods. Can contain arbitrary **asynchronous** operations (like API calls). Actions **commit mutations** to change state; they don't modify state directly. Receive `context` object (with `commit`, `state`, `getters`, `dispatch`) as the first argument. Dispatched using `store.dispatch('actionName', payload)`.
*   **Modules:** Allow splitting a large store into smaller, self-contained modules, each with its own state, getters, mutations, and actions (can be namespaced).

## Implementation Example (Vue 3 with Vuex 4)

1.  **Install Vuex:**
    ```bash
    npm install vuex@next --save # Vuex 4 for Vue 3
    # or
    yarn add vuex@next
    ```

2.  **Create Store:** Define the store structure (state, getters, mutations, actions).

    ```typescript
    // src/store/index.ts
    import { createStore, createLogger } from 'vuex';

    // Define state type (optional but recommended with TS)
    export interface RootState {
      count: number;
      user: { name: string } | null;
    }

    export default createStore<RootState>({
      // --- State ---
      state: {
        count: 0,
        user: null,
      },

      // --- Getters ---
      getters: {
        doubleCount(state): number {
          return state.count * 2;
        },
        userName(state): string {
          return state.user?.name ?? 'Guest';
        },
      },

      // --- Mutations --- (Must be synchronous)
      mutations: {
        SET_COUNT(state, newCount: number) {
          state.count = newCount;
        },
        INCREMENT(state, amount: number = 1) {
          state.count += amount;
        },
        SET_USER(state, user: { name: string } | null) {
          state.user = user;
        },
      },

      // --- Actions --- (Can be asynchronous)
      actions: {
        incrementAsync({ commit }, payload: { amount: number; delay: number }) {
          setTimeout(() => {
            commit('INCREMENT', payload.amount); // Commit mutation after delay
          }, payload.delay);
        },
        resetCounter({ commit }) {
          commit('SET_COUNT', 0);
        },
        async loginUser({ commit }, userName: string) {
          // Simulate API call
          // const user = await api.login(userName);
          const user = { name: userName }; // Dummy user
          commit('SET_USER', user); // Commit mutation with fetched data
        },
        logoutUser({ commit }) {
          commit('SET_USER', null);
        },
      },

      // --- Modules --- (Optional)
      // modules: {
      //   cart: cartModule,
      //   products: productsModule,
      // },

      // --- Plugins --- (Optional, e.g., for logging in dev)
      plugins: process.env.NODE_ENV !== 'production' ? [createLogger()] : [],

      // --- Strict Mode --- (Optional, ensures state isn't mutated outside mutations - dev only)
      strict: process.env.NODE_ENV !== 'production',
    });

    ```

3.  **Install Store in App:**

    ```typescript
    // src/main.ts
    import { createApp } from 'vue';
    import store from './store'; // Import the store
    import App from './App.vue';

    const app = createApp(App);
    app.use(store); // Install store
    app.mount('#app');
    ```

4.  **Access Store in Components:**
    *   **Composition API:** Use `useStore()` hook.
    *   **Options API:** Use `this.$store`. Helper functions `mapState`, `mapGetters`, `mapMutations`, `mapActions` can simplify access.

    ```vue
    <!-- MyComponent.vue (Composition API) -->
    <script setup lang="ts">
    import { computed } from 'vue';
    import { useStore } from 'vuex';
    import { type RootState } from '@/store'; // Import state type

    const store = useStore<RootState>();

    // Access state (wrap in computed for reactivity)
    const count = computed(() => store.state.count);
    const user = computed(() => store.state.user);

    // Access getters (wrap in computed)
    const doubleCount = computed(() => store.getters.doubleCount);
    const userName = computed(() => store.getters.userName);

    function increment() {
      // Dispatch action
      store.dispatch('incrementAsync', { amount: 1, delay: 500 });
    }

    function login() {
        // Commit mutation directly (less common for complex logic)
        // store.commit('SET_USER', { name: 'Alice' });
        // Dispatch action
        store.dispatch('loginUser', 'Alice');
    }
    </script>

    <template>
      <div>
        <p>Count: {{ count }}</p>
        <p>Double: {{ doubleCount }}</p>
        <p>User: {{ userName }}</p>
        <button @click="increment">Increment Async</button>
        <button v-if="!user" @click="login">Login</button>
        <button v-else @click="store.dispatch('logoutUser')">Logout</button>
      </div>
    </template>
    ```

**Vuex vs. Pinia:**

*   **Mutations:** Vuex requires mutations for all state changes; Pinia allows direct state mutation within actions (or components, though actions are preferred).
*   **Modularity:** Pinia enforces modularity (each `defineStore` is a module); Vuex modules are optional.
*   **TypeScript:** Pinia has superior TypeScript inference and requires less boilerplate for type safety.
*   **API:** Pinia's API aligns more closely with Vue 3's Composition API (`ref`, `computed` in setup stores).

While Vuex is powerful, Pinia is generally simpler and more type-safe for new Vue 3 projects. Understanding Vuex remains important for maintaining existing applications.

*(Refer to the official Vuex 4 documentation.)*