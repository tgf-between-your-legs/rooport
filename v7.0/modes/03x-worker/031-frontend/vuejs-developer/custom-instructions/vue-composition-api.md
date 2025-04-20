# Vue.js: Composition API

Using the Composition API (`<script setup>`, `ref`, `reactive`, `computed`, `watch`, lifecycle hooks) for building Vue 3 components.

## Core Concept: Logic Organization & Reusability

The Composition API provides an alternative, more flexible way to organize component logic compared to the Options API. It allows grouping code by logical concern rather than by option type, making it easier to manage complex components and extract reusable logic (composables).

**Key Features:**

*   **`<script setup>`:** Recommended syntactic sugar for using Composition API within Single-File Components (SFCs). Code inside runs directly in the component's `setup()` context. Variables and functions declared are automatically exposed to the template.
*   **Reactivity APIs:**
    *   `ref()`: Creates a reactive reference for primitive values (string, number, boolean) or single object references. Access/modify the value using `.value`.
    *   `reactive()`: Creates a reactive proxy for objects (deep reactivity). Access/modify properties directly. Be mindful of reactivity loss when destructuring (use `toRefs`).
    *   `computed()`: Creates a computed property (a ref) whose value is derived from other reactive sources and cached.
    *   `watch()`: Runs a callback function whenever specified reactive sources change. Allows fine-grained control over dependencies and timing.
    *   `watchEffect()`: Runs a callback function immediately and re-runs it whenever any of its reactive dependencies change. Tracks dependencies automatically.
*   **Lifecycle Hooks:** Importable functions prefixed with `on` (e.g., `onMounted`, `onUpdated`, `onUnmounted`) that register callbacks for component lifecycle events.
*   **Composables:** Regular functions that encapsulate and reuse stateful logic using Composition API functions (`ref`, `computed`, `watch`, etc.).

## Implementation (`<script setup>`)

```vue
<script setup lang="ts">
// Import necessary functions from 'vue'
import { ref, reactive, computed, watch, onMounted, onUnmounted } from 'vue';
// Import composables (example)
// import { useMouse } from '@/composables/useMouse';

// --- Props & Emits ---
// Define props using defineProps macro
interface Props {
  initialCount?: number;
  message?: string;
}
const props = withDefaults(defineProps<Props>(), {
  initialCount: 0,
  message: 'Default Message'
});

// Define emits using defineEmits macro
const emit = defineEmits<{
  (e: 'update', value: number): void;
  (e: 'reset'): void;
}>();

// --- Reactive State ---
// Reactive primitive using ref()
const count = ref<number>(props.initialCount);

// Reactive object using reactive()
const state = reactive({
  user: { name: 'Alice', age: 30 },
  isAdmin: false,
});

// --- Composables ---
// Example: Using a custom composable
// const { x, y } = useMouse();

// --- Computed Properties ---
const doubleCount = computed<number>(() => count.value * 2);
const userInfo = computed<string>(() => `${state.user.name} (${state.user.age})`);

// --- Methods ---
// Functions declared are automatically available in the template
function increment(): void {
  count.value++;
  emit('update', count.value); // Emit event
}

function resetCounter(): void {
  count.value = props.initialCount;
  emit('reset');
}

function updateUserAge(newAge: number): void {
  state.user.age = newAge; // Mutate reactive object directly
}

// --- Watchers ---
// Watch a specific ref or reactive source
watch(count, (newVal, oldVal) => {
  console.log(`Count changed from ${oldVal} to ${newVal}`);
});

// Watch multiple sources
// watch([count, () => state.user.age], ([newCount, newAge], [oldCount, oldAge]) => {
//   console.log(`Count or age changed`);
// });

// WatchEffect runs immediately and tracks dependencies
// watchEffect(() => {
//   console.log(`Current count is: ${count.value}`);
// });

// --- Lifecycle Hooks ---
onMounted(() => {
  console.log('Component mounted!');
  // Perform setup, fetch data, add event listeners
});

onUnmounted(() => {
  console.log('Component unmounting!');
  // Clean up timers, event listeners, etc.
});

// Other hooks: onUpdated, onBeforeMount, onBeforeUpdate, onBeforeUnmount, etc.

</script>

<template>
  <div>
    <h2>{{ message }}</h2>
    <p>Count: {{ count }}</p>
    <p>Double Count: {{ doubleCount }}</p>
    <p>User: {{ userInfo }}</p>
    <!-- <p>Mouse Position: {{ x }}, {{ y }}</p> -->

    <button @click="increment">Increment</button>
    <button @click="resetCounter">Reset</button>
    <button @click="updateUserAge(state.user.age + 1)">Increase Age</button>
  </div>
</template>

<style scoped>
/* Component-specific styles */
button {
  margin: 5px;
}
</style>
```

The Composition API with `<script setup>` offers a more organized and scalable way to handle component logic in Vue 3, especially for larger components or when reusing logic via composables.

*(Refer to the official Vue.js documentation on Composition API and `<script setup>`.)*