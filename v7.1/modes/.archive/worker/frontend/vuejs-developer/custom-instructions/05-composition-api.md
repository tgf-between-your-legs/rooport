# Vue.js: Composition API

Using the Composition API (`<script setup>`, `ref`, `reactive`, `computed`, `watch`, lifecycle hooks) for building Vue 3 components. This is the **recommended approach** for new Vue 3 development.

## Core Concept: Logic Organization & Reusability

The Composition API provides a flexible way to organize component logic by logical concern rather than by option type (as in the Options API). This improves readability and maintainability, especially in complex components, and facilitates logic reuse through composables.

**Key Features:**

*   **`<script setup>`:** Recommended syntactic sugar for using Composition API within Single-File Components (SFCs). Code inside runs directly in the component's `setup()` context. Variables, imports, and functions declared are automatically exposed to the template. Use `lang="ts"` for TypeScript integration.
*   **Reactivity APIs:**
    *   `ref()`: Creates a reactive reference object, typically for primitive values (string, number, boolean) or single object references. Access/modify the underlying value using `.value`.
    *   `reactive()`: Creates a reactive proxy for objects (deep reactivity). Access/modify properties directly. Be mindful of reactivity loss when destructuring (use `toRefs` or `toRef` if needed). Generally prefer `ref` for most state unless dealing with complex, deeply nested objects where direct mutation is desired.
    *   `computed()`: Creates a computed property (a cached, reactive ref) whose value is derived from other reactive sources. Re-evaluates only when dependencies change.
    *   `watch()`: Runs a callback function whenever specified reactive sources change. Allows fine-grained control over dependencies, timing (`flush: 'post'`), and deep watching (`deep: true`).
    *   `watchEffect()`: Runs a callback function immediately and re-runs it whenever any of its reactive dependencies change. Tracks dependencies automatically. Useful for simple side effects tied to reactive state.
*   **Lifecycle Hooks:** Importable functions prefixed with `on` (e.g., `onMounted`, `onUpdated`, `onUnmounted`, `onBeforeMount`, etc.) that register callbacks for component lifecycle events. Call these directly within `<script setup>`.
*   **Dependency Injection:** `provide()` and `inject()` allow passing data down the component tree without prop drilling.

## Implementation (`<script setup lang="ts">`)

```vue
<script setup lang="ts">
// Import necessary functions from 'vue'
import { ref, reactive, computed, watch, watchEffect, onMounted, onUnmounted, toRefs } from 'vue';
// Import composables (example)
// import { useMouse } from '@/composables/useMouse';

// --- Props & Emits (See 03-components-sfcs.md) ---
interface Props { initialCount?: number; message?: string; }
const props = withDefaults(defineProps<Props>(), { initialCount: 0, message: 'Default' });
const emit = defineEmits<{ (e: 'update', value: number): void; }>();

// --- Reactive State ---
// Prefer ref for primitives and simple objects/arrays
const count = ref<number>(props.initialCount);
const user = ref<{ name: string; age: number } | null>(null);
const items = ref<string[]>(['item1']);

// Use reactive for complex, nested objects where direct mutation is convenient
const settings = reactive({ theme: 'dark', notifications: { enabled: true, sound: 'default' } });

// --- Composables ---
// Example: Using a custom composable
// const { x, y } = useMouse();

// --- Computed Properties ---
const doubleCount = computed<number>(() => count.value * 2);
const userName = computed<string>(() => user.value?.name ?? 'Guest');
// Computed based on reactive object
const notificationSound = computed(() => settings.notifications.sound);

// --- Methods ---
// Functions declared are automatically available in the template
function increment(): void {
  count.value++;
  emit('update', count.value); // Emit event
}

function loadUser(): void {
  // Simulate loading user data
  user.value = { name: 'Alice', age: 30 };
}

function toggleTheme(): void {
  settings.theme = settings.theme === 'dark' ? 'light' : 'dark'; // Mutate reactive object
}

// --- Watchers ---
// Watch a specific ref
watch(count, (newVal, oldVal) => {
  console.log(`Count changed from ${oldVal} to ${newVal}`);
});

// Watch a getter function for more complex sources
watch(() => props.message, (newMessage) => {
  console.log(`Message prop changed: ${newMessage}`);
});

// Watch reactive object property
watch(() => settings.theme, (newTheme) => {
    console.log(`Theme changed to ${newTheme}`);
});

// WatchEffect runs immediately and tracks dependencies
watchEffect(() => {
  // This runs initially and whenever count.value changes
  console.log(`watchEffect: Current count is: ${count.value}`);
  // Avoid side effects that modify the dependencies being watched within the same tick
});

// --- Lifecycle Hooks ---
onMounted(() => {
  console.log('Component mounted!');
  loadUser(); // Example: Fetch data on mount
  // Perform setup, add non-Vue event listeners
});

onUnmounted(() => {
  console.log('Component unmounting!');
  // Clean up timers, non-Vue event listeners, etc.
});

// --- Template Refs (See 10-typescript-integration.md) ---
const myElementRef = ref<HTMLDivElement | null>(null);

</script>

<template>
  <div>
    <h2>{{ message }}</h2>
    <p>Count: {{ count }}</p>
    <p>Double Count: {{ doubleCount }}</p>
    <p>User: {{ userName }}</p>
    <p>Theme: {{ settings.theme }}</p>
    <!-- <p>Mouse Position: {{ x }}, {{ y }}</p> -->

    <button @click="increment">Increment</button>
    <button @click="toggleTheme">Toggle Theme</button>

    <div ref="myElementRef">I am an element</div>
  </div>
</template>

<style scoped>
/* Component-specific styles */
button { margin: 5px; }
</style>
```

The Composition API with `<script setup>` offers a more organized, type-safe, and scalable way to handle component logic in Vue 3, especially for larger components or when reusing logic via composables. Prefer `ref` for most reactive state unless `reactive` offers clear benefits for nested object manipulation.