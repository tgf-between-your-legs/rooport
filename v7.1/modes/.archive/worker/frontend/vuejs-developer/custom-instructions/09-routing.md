# Vue.js: Routing with Vue Router

Implementing client-side navigation in Single-Page Applications (SPAs) using Vue Router (v4 for Vue 3).

## Core Concept: Client-Side Navigation

Vue Router is the official routing library for Vue.js. It enables navigation between different "pages" or views within your SPA without requiring a full page reload, by mapping URL paths to specific Vue components.

**Key Features:**

*   **Route Mapping:** Define routes linking URL paths (e.g., `/`, `/users`, `/user/:id`) to components.
*   **Router Instance:** A central `router` instance manages routing state and configuration. Created using `createRouter`.
*   **History Modes:**
    *   `createWebHistory()`: Uses HTML5 History API (clean URLs like `/users`). Requires server configuration to handle direct page loads. **Preferred mode.**
    *   `createWebHashHistory()`: Uses URL hash (`#`) for routing (e.g., `/#/users`). Works without server config but URLs are less clean.
*   **`<router-view>`:** Component acting as a placeholder where the matched route component is rendered. Can be nested for nested routes.
*   **`<router-link>`:** Component for declarative navigation. Renders an `<a>` tag with correct `href` and handles navigation. Use the `to` prop (path string or route object).
*   **Programmatic Navigation:** Use `router.push()`, `router.replace()`, `router.go()` methods (accessed via `useRouter()` hook) for imperative navigation in `<script setup>`.
*   **Dynamic Routes & Params:** Define routes with parameters (e.g., `/user/:id`). Access params via `useRoute().params` or as props if `props: true` is set in the route definition.
*   **Nested Routes:** Define `children` arrays in route definitions for nested layouts and views.
*   **Navigation Guards:** Functions that intercept navigation transitions (globally, per-route, or in-component). Used for authentication checks, data fetching, logging, etc.
    *   Global: `router.beforeEach()`, `router.beforeResolve()`, `router.afterEach()`.
    *   Per-Route: `beforeEnter` in the route definition.
    *   In-Component: `onBeforeRouteUpdate()`, `onBeforeRouteLeave()`.
*   **Lazy Loading Routes:** Use dynamic imports (`() => import('@/views/AboutView.vue')`) for route components to split code and load views on demand.

## Implementation Steps

1.  **Install:** `npm install vue-router@4`

2.  **Define Routes & Create Router:**
    ```typescript
    // src/router/index.ts
    import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
    import HomeView from '@/views/HomeView.vue'; // Eager load home

    // Lazy load other views
    const AboutView = () => import('@/views/AboutView.vue');
    const UserProfile = () => import('@/views/UserProfile.vue');
    const UserSettings = () => import('@/views/UserSettings.vue'); // For nested route
    const NotFound = () => import('@/views/NotFound.vue');

    const routes: Array<RouteRecordRaw> = [
      {
        path: '/',
        name: 'Home',
        component: HomeView,
        meta: { requiresAuth: false }, // Example meta field
      },
      {
        path: '/about',
        name: 'About',
        component: AboutView,
        meta: { requiresAuth: false },
      },
      {
        path: '/user/:id', // Dynamic segment ':id'
        name: 'User',
        component: UserProfile,
        props: true, // Pass route.params as props ({ id: '...' })
        meta: { requiresAuth: true },
        // Example nested route
        children: [
          {
            // UserSettings will be rendered inside UserProfile's <router-view>
            // when /user/:id/settings is matched
            path: 'settings',
            name: 'UserSettings',
            component: UserSettings,
            meta: { requiresAuth: true },
          },
        ],
        // Per-route guard
        // beforeEnter: (to, from) => {
        //   // Check something before entering this route or its children
        //   return true; // Allow
        // },
      },
      // Catch-all 404 route (must be last)
      {
        path: '/:pathMatch(.*)*', // Matches everything not matched above
        name: 'NotFound',
        component: NotFound,
      },
    ];

    const router = createRouter({
      history: createWebHistory(import.meta.env.BASE_URL), // HTML5 history mode
      routes,
      scrollBehavior(to, from, savedPosition) {
        // Control scroll position on navigation
        if (savedPosition) {
          return savedPosition;
        } else {
          return { top: 0, behavior: 'smooth' };
        }
      },
    });

    // --- Example Global Navigation Guard ---
    router.beforeEach((to, from, next) => {
      const isAuthenticated = /* check auth status, e.g., from Pinia store */;
      const requiresAuth = to.matched.some(record => record.meta.requiresAuth);

      if (requiresAuth && !isAuthenticated) {
        // Redirect to login page, saving the intended destination
        next({ name: 'Login', query: { redirect: to.fullPath } });
      } else {
        next(); // Proceed with navigation
      }
    });

    export default router;
    ```

3.  **Install Router Plugin:**
    ```typescript
    // src/main.ts
    import { createApp } from 'vue';
    import router from './router'; // Import the configured router
    import App from './App.vue';

    const app = createApp(App);
    app.use(router); // Install router
    app.mount('#app');
    ```

4.  **Use `<router-view>` & `<router-link>`:**
    ```vue
    <!-- src/App.vue (Main Layout) -->
    <template>
      <nav>
        <router-link to="/">Home</router-link> |
        <router-link :to="{ name: 'About' }">About</router-link> |
        <router-link :to="{ name: 'User', params: { id: '123' } }">User 123</router-link>
      </nav>
      <main>
        <!-- Top-level route components render here -->
        <router-view v-slot="{ Component, route }">
          <!-- Optional: Add transitions -->
          <transition :name="route.meta.transition || 'fade'" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </main>
    </template>
    <style>
    .fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
    .fade-enter-from, .fade-leave-to { opacity: 0; }
    /* Active link styling */
    .router-link-active { font-weight: bold; }
    .router-link-exact-active { text-decoration: underline; }
    </style>
    ```
    ```vue
    <!-- src/views/UserProfile.vue (Example Parent Route Component) -->
    <template>
      <div>
        <h1>User Profile: {{ id }}</h1>
        <nav>
          <!-- Link to nested route -->
          <router-link :to="{ name: 'UserSettings', params: { id: id } }">Settings</router-link>
        </nav>
        <!-- Nested route components render here -->
        <router-view />
      </div>
    </template>
    <script setup lang="ts">
    defineProps<{ id: string }>(); // Receiving param via props: true
    </script>
    ```

5.  **Access Route Info & Navigate Programmatically (`<script setup>`):**
    ```typescript
    import { useRoute, useRouter, onBeforeRouteUpdate, onBeforeRouteLeave } from 'vue-router';
    import { computed } from 'vue';

    const route = useRoute(); // Access current route info (params, query, path, meta)
    const router = useRouter(); // Access router instance (push, replace, go)

    // Access param (if not using props: true)
    const userId = computed(() => route.params.id as string);
    // Access query param
    const searchQuery = computed(() => route.query.q as string | undefined);

    function goToUser(userId: string) {
      router.push({ name: 'User', params: { id: userId } });
    }

    function goBack() {
      router.go(-1); // Go back one step in history
    }

    // In-component guards
    onBeforeRouteUpdate((to, from) => {
      // Fired when route changes but component is reused (e.g., /user/1 -> /user/2)
      console.log(`Updating route from user ${from.params.id} to ${to.params.id}`);
      // Fetch data for to.params.id
    });

    onBeforeRouteLeave((to, from) => {
      // Fired when navigating away from this component's route
      // const answer = window.confirm('Leave without saving?');
      // if (!answer) return false; // Cancel navigation
    });
    ```

Vue Router provides a robust solution for SPA navigation. Key aspects include defining routes, using `<router-link>` and `<router-view>`, accessing route information with `useRoute()`, navigating programmatically with `useRouter()`, and controlling transitions with navigation guards. Remember to configure your server for `createWebHistory` mode.