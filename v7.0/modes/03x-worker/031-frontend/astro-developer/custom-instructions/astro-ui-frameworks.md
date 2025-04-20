# Astro: Integrating UI Frameworks (React, Vue, Svelte, etc.)

Using components from other UI frameworks within Astro islands.

## Core Concept: Framework Integrations

Astro allows you to use components written in popular UI frameworks like React, Preact, Vue, Svelte, SolidJS, Lit, and more, right alongside your `.astro` components. This is a key part of the **Islands Architecture**.

*   **Zero JS by Default:** Framework components are server-rendered to HTML by default, just like `.astro` components. No client-side framework JavaScript is loaded initially.
*   **Selective Hydration:** To make a framework component interactive in the browser, you **must** add a `client:*` directive to it in your `.astro` template. This tells Astro to load the component's framework runtime and hydrate the component according to the directive's strategy (`load`, `idle`, `visible`, etc.).
*   **Multiple Frameworks:** You can mix components from different frameworks on the same page. Astro isolates framework runtimes so they don't interfere.

## Setup

1.  **Install Integration:** Use the `astro add` command to install and configure the integration for the framework(s) you want to use.
    ```bash
    # Example for React
    npx astro add react

    # Example for Vue
    npx astro add vue

    # Example for Svelte
    npx astro add svelte
    ```
    This command typically installs necessary dependencies (like `@astrojs/react`, `react`, `react-dom`) and updates your `astro.config.mjs` file to include the integration.
2.  **Configure `tsconfig.json` (If using TypeScript):** Ensure your `tsconfig.json` is set up correctly for JSX support if using React/Preact (Astro usually handles this during `astro add`).

## Using Framework Components

1.  **Create Component:** Write your component using the framework's standard syntax (e.g., `.jsx`/`.tsx` for React, `.vue` for Vue, `.svelte` for Svelte) within your `src/components/` directory (or elsewhere in `src/`).
2.  **Import Component:** Import the framework component into your `.astro` file's script fence.
3.  **Use in Template:** Use the imported component like an HTML tag in the Astro template.
4.  **Pass Props:** Pass props as attributes. Remember props must be **serializable** (convertible to JSON) if the component is hydrated on the client (`client:*` directive used). Functions and complex class instances cannot be passed directly to client-hydrated islands.
5.  **Add `client:*` Directive (for Interactivity):** If the component needs to be interactive in the browser, add the appropriate `client:*` directive (`client:load`, `client:idle`, `client:visible`, etc.). **Without a `client:*` directive, the component remains static HTML.**

```astro
---
// src/pages/frameworks.astro
import BaseLayout from '../layouts/BaseLayout.astro';

// Import framework components
import ReactCounter from '../components/ReactCounter.jsx';
import VueToggle from '../components/VueToggle.vue';
import SvelteTimer from '../components/SvelteTimer.svelte';

const initialReactCount = 5;
const messageForVue = "Toggle Me (Vue)";
---
<BaseLayout pageTitle="Framework Components">
  <h1>Using UI Frameworks in Astro</h1>

  {/* --- React Component --- */}
  <h2>React Counter</h2>
  {/* This island hydrates as soon as the main thread is free */}
  <ReactCounter initialCount={initialReactCount} client:idle />

  <hr />

  {/* --- Vue Component --- */}
  <h2>Vue Toggle</h2>
  {/* This island hydrates only when it becomes visible */}
  <VueToggle client:visible message={messageForVue} />

  <hr />

  {/* --- Svelte Component --- */}
  <h2>Svelte Timer</h2>
  {/* This island hydrates immediately on page load */}
  <SvelteTimer client:load />

</BaseLayout>
```

```jsx
// src/components/ReactCounter.jsx
import React, { useState } from 'react';

function ReactCounter({ initialCount = 0 }) {
  const [count, setCount] = useState(initialCount);

  return (
    <div>
      <p>Count (React): {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
export default ReactCounter;
```

```vue
<!-- src/components/VueToggle.vue -->
<template>
  <div>
    <button @click="toggle">{{ message }}</button>
    <p v-if="isOn">Status (Vue): ON</p>
    <p v-else>Status (Vue): OFF</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  message: String
});

const isOn = ref(false);
const toggle = () => {
  isOn.value = !isOn.value;
};
</script>
```

```svelte
<!-- src/components/SvelteTimer.svelte -->
<script>
  import { onMount, onDestroy } from 'svelte';

  export let intervalMs = 1000; // Prop
  let seconds = 0;
  let intervalId;

  onMount(() => {
    console.log('Svelte Timer Mounted');
    intervalId = setInterval(() => {
      seconds += 1;
    }, intervalMs);
  });

  onDestroy(() => {
    console.log('Svelte Timer Destroyed');
    clearInterval(intervalId);
  });
</script>

<p>Seconds Elapsed (Svelte): {seconds}</p>
```

Astro's framework integrations and island architecture allow you to leverage existing component libraries or build interactive UIs with your preferred framework while maintaining excellent performance by default.

*(Refer to the official Astro UI Frameworks documentation.)*