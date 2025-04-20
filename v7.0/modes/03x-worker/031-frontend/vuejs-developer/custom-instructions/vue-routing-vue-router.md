# Vue.js: Routing with Vue Router

Implementing client-side navigation in Single-Page Applications (SPAs) using Vue Router.

## Core Concept: Client-Side Navigation

Vue Router is the official routing library for Vue.js. It allows you to map different URL paths to specific Vue components, enabling navigation within your SPA without requiring a full page reload from the server.

**Key Features:**

*   **Route Mapping:** Define routes that link URL paths (like `/users` or `/user/:id`) to components.
*   **Router Instance:** A central router instance manages the application's routing state.
*   **`<router-view>`:** A component provided by Vue Router that acts as a placeholder where the matched route component will be rendered.
*   **`<router-link>`:** A component for declarative navigation. Renders an `<a>` tag with the correct `href` and handles click events to trigger navigation without a page reload.
*   **Programmatic Navigation:** Use `router.push()`, `router.replace()`, `router.go()` methods for navigating imperatively within your component logic.
*   **Dynamic Route Matching:** Define routes with parameters (e.g., `/user/:id`) to match dynamic segments in the URL. Access parameters via `$route.params` (Options API) or `useRoute().params` (Composition API).
*   **Nested Routes:** Create nested UI layouts by defining child routes and using nested `<router-view>` components.
*   **Navigation Guards:** Hooks (like `beforeEach`, `beforeResolve`, `afterEach`, and per-route guards) that allow you to intercept navigation, perform checks (like authentication), redirect, or modify the navigation process.
*   **History Modes:** Supports different history modes (`createWebHistory` for HTML5 History API - clean URLs, requires server config; `createWebHashHistory` for hash mode - uses `#`, works without server config).

## Implementation Steps

1.  **Install Vue Router:**
    ```bash
    npm install vue-router@4 # Vue Router 4 for Vue 3
    # or
    yarn add vue-router@4
    ```

2.  **Define Routes:** Create a file (e.g., `src/router/index.ts`) to define your route mappings.

    ```typescript
    // src/router/index.ts
    import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
    import HomeView from '@/views/HomeView.vue'; // Example view component
    // Lazy load components for better code splitting
    const AboutView = () => import('@/views/AboutView.vue');
    const UserProfile = () => import('@/views/UserProfile.vue');
    const NotFound = () => import('@/views/NotFound.vue');

    const routes: Array<RouteRecordRaw> = [
      {
        path: '/',
        name: 'Home', // Optional name for programmatic navigation
        component: HomeView,
      },
      {
        path: '/about',
        name: 'About',
        component: AboutView,
      },
      {
        path: '/user/:id', // Dynamic segment ':id'
        name: 'UserProfile',
        component: UserProfile,
        props: true, // Pass route params as props to the component
      },
      // Example Nested Routes
      // {
      //   path: '/settings',
      //   component: SettingsLayout,
      //   children: [
      //     { path: 'profile', component: SettingsProfile },
      //     { path: 'account', component: SettingsAccount },
      //   ]
      // },
      // Catch-all 404 route (must be last)
      {
        path: '/:pathMatch(.*)*', // Matches everything else
        name: 'NotFound',
        component: NotFound,
      },
    ];

    const router = createRouter({
      history: createWebHistory(import.meta.env.BASE_URL), // Use HTML5 history mode
      // history: createWebHashHistory(import.meta.env.BASE_URL), // Use hash mode
      routes, // Short for `routes: routes`
      // Optional: Scroll behavior
      // scrollBehavior(to, from, savedPosition) {
      //   if (savedPosition) {
      //     return savedPosition;
      //   } else {
      //     return { top: 0 };
      //   }
      // },
    });

    // --- Optional: Navigation Guards ---
    // router.beforeEach((to, from, next) => {
    //   console.log(`Navigating from ${from.fullPath} to ${to.fullPath}`);
    //   // Example: Check authentication
    //   // const isAuthenticated = checkAuth();
    //   // if (to.meta.requiresAuth && !isAuthenticated) {
    //   //   next({ name: 'Login' }); // Redirect to login
    //   // } else {
    //   //   next(); // Proceed with navigation
    //   // }
    //   next();
    // });

    export default router;
    ```

3.  **Install Router in App:**

    ```typescript
    // src/main.ts
    import { createApp } from 'vue';
    import router from './router'; // Import the router instance
    import App from './App.vue';

    const app = createApp(App);
    app.use(router); // Install router plugin
    app.mount('#app');
    ```

4.  **Use `<router-view>` and `<router-link>`:** In your main `App.vue` or layout components, use `<router-view>` to display the matched route component. Use `<router-link>` for navigation links.

    ```vue
    <!-- src/App.vue -->
    <template>
      <header>
        <nav>
          <router-link to="/">Home</router-link> |
          <router-link :to="{ name: 'About' }">About</router-link> | <!-- Navigation by name -->
          <router-link to="/user/123">User 123</router-link>
        </nav>
      </header>

      <main>
        <!-- Component matched by the route will render here -->
        <router-view />
      </main>
    </template>

    <script setup lang="ts">
    // No script needed for basic router-view/link usage
    </script>
    ```

5.  **Access Route Info & Navigate Programmatically:**

    ```vue
    <!-- src/views/UserProfile.vue -->
    <script setup lang="ts">
    import { useRoute, useRouter, onBeforeRouteUpdate, onBeforeRouteLeave } from 'vue-router';
    import { computed, watch } from 'vue';

    // Option 1: Access params via props (if props: true in route definition)
    const props = defineProps<{ id: string }>();
    const userIdFromProp = computed(() => props.id);

    // Option 2: Access route object directly
    const route = useRoute(); // Provides access to $route object (params, query, path, etc.)
    const router = useRouter(); // Provides access to router instance (push, replace, go)

    const userIdFromRoute = computed(() => route.params.id as string);

    console.log('User ID (prop):', userIdFromProp.value);
    console.log('User ID (route):', userIdFromRoute.value);
    console.log('Query params:', route.query);

    function goToAbout() {
      router.push({ name: 'About' }); // Programmatic navigation by name
      // router.push('/about'); // By path
      // router.replace('/about'); // Like push, but doesn't add to history stack
    }

    // Watch for route param changes within the same component instance
    watch(() => route.params.id, (newId) => {
        console.log('Route param id changed within component:', newId);
        // Fetch new user data based on newId
    });

    // --- In-component Navigation Guards ---
    onBeforeRouteUpdate((to, from) => {
      // Fired when the route changes but this component is reused
      console.log(`Route update from ${String(from.params.id)} to ${String(to.params.id)}`);
      // Fetch data for the new user ID (to.params.id)
      // return true; // Allow navigation
      // return false; // Block navigation
      // return { name: 'OtherRoute' }; // Redirect
    });

    onBeforeRouteLeave((to, from) => {
      // Fired when navigating away from the route that renders this component
      // const answer = window.confirm('Do you really want to leave? You have unsaved changes!');
      // if (!answer) return false; // Block navigation
    });

    </script>

    <template>
      <div>
        <h1>User Profile</h1>
        <p>Displaying profile for User ID: {{ userIdFromProp }} (or {{ userIdFromRoute }})</p>
        <button @click="goToAbout">Go to About</button>
      </div>
    </template>
    ```

Vue Router provides a comprehensive solution for managing client-side navigation in Vue SPAs, supporting basic linking, dynamic routes, nested views, and advanced navigation control with guards.

*(Refer to the official Vue Router 4 documentation.)*