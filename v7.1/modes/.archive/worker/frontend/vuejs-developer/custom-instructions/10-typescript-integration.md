# Vue.js: TypeScript Integration

Using TypeScript effectively within Vue 3 components, particularly with `<script setup>`.

## Core Concept: Type Safety in Components

Vue 3 offers excellent first-class TypeScript support, especially when using Single-File Components (SFCs) with the `<script setup>` syntax. This enables static typing for props, emits, reactive state, computed properties, template refs, and more, enhancing code reliability and developer experience.

**Key Benefits:**

*   **Stronger Component Contracts:** Clearly define expected types for props and emitted event payloads.
*   **Improved Refactoring:** Types make renaming variables, restructuring code, and updating component APIs safer.
*   **Enhanced Autocompletion & Intellisense:** IDEs provide more accurate suggestions and type checking based on defined types.
*   **Early Error Detection:** Catch type mismatches and potential runtime errors during development/compilation.
*   **Better Maintainability:** Explicit types make code easier to understand and maintain over time.

## Using TypeScript with `<script setup>`

1.  **Enable TS:** Add `lang="ts"` to the `<script setup>` tag. Ensure your project is configured for TypeScript (usually handled by `create-vue` or Vue CLI presets).
2.  **Type Definitions:** Use TypeScript interfaces, types, enums, etc., to define the shapes of your data.
3.  **Compiler Macros:** Utilize Vue's TypeScript-aware compiler macros (`defineProps`, `defineEmits`, `defineModel`).

```vue
<script setup lang="ts">
// Import types and functions
import { ref, computed, reactive, onMounted, type Ref } from 'vue';
// Import custom types if defined elsewhere
// import type { User, Status } from '@/types';

// --- Define Custom Types (or import) ---
interface User {
  id: number;
  name: string;
  email?: string; // Optional property
}
type Status = 'pending' | 'active' | 'inactive'; // Literal union type

// --- Props ---
// Use defineProps with a generic type argument for full type safety
interface Props {
  message: string;
  user: User | null; // Union type
  tags?: string[]; // Optional array prop
  status: Status;
}
// Use withDefaults for default values (factory functions for objects/arrays)
const props = withDefaults(defineProps<Props>(), {
  user: null,
  tags: () => ['default'],
  // 'message' and 'status' are required, no default needed
});

// --- Emits ---
// Use defineEmits with a generic type argument and call signatures
const emit = defineEmits<{
  (e: 'updateStatus', newStatus: Status, timestamp: number): void; // Event with multiple typed payloads
  (e: 'userLogout', userId: number): void;
}>();

// --- Reactive State ---
// Type inference often works well for simple cases
const count = ref(0); // Inferred as Ref<number>

// Explicit typing using generics when needed
const items = ref<string[]>([]);
const currentUser = ref<User | null>(props.user); // Initialize with prop value
const settings = reactive<{ theme: string; fontSize: number }>({
  theme: 'light',
  fontSize: 14,
});

// --- Computed ---
// Return type is usually inferred, but can be explicit
const welcomeMessage = computed<string>(() => {
  return `Welcome, ${currentUser.value?.name ?? 'Guest'}! (${props.message})`;
});
const isActive = computed<boolean>(() => props.status === 'active');

// --- Functions ---
// Type function parameters and return values
function changeStatus(newStatus: Status): void {
  if (newStatus !== props.status) {
    emit('updateStatus', newStatus, Date.now());
  }
}

function logout(): void {
  if (currentUser.value) {
    emit('userLogout', currentUser.value.id);
    currentUser.value = null; // Update local state
  }
}

// Type DOM event handlers
function handleInput(event: Event): void {
  // Type assertion needed to access specific input properties
  const target = event.target as HTMLInputElement;
  console.log('Input value:', target.value);
}

// --- Template Refs ---
// Type the ref with the specific HTML element type (or component type)
// Initialize with null as the element doesn't exist before mount
const mainContainerRef = ref<HTMLDivElement | null>(null);
const customInputRef = ref<InstanceType<typeof CustomInputComponent> | null>(null); // For component refs

onMounted(() => {
  // Access element/component via .value (might be null)
  mainContainerRef.value?.focus(); // Example: Focus the div (if focusable)
  // customInputRef.value?.someMethodOnComponent(); // Call method on child component instance
});

// --- Importing Components ---
// Ensure imported components also have proper type definitions for props/emits
// import CustomInputComponent from './CustomInputComponent.vue';

</script>

<template>
  <div ref="mainContainerRef" tabindex="-1"> <!-- tabindex needed to make div focusable -->
    <p>{{ welcomeMessage }}</p>
    <p>Status: {{ props.status }} (Active: {{ isActive }})</p>
    <ul>
      <li v-for="tag in props.tags" :key="tag">{{ tag }}</li>
    </ul>

    <button @click="changeStatus('active')" :disabled="props.status === 'active'">Activate</button>
    <button @click="changeStatus('inactive')" :disabled="props.status === 'inactive'">Deactivate</button>
    <button v-if="currentUser" @click="logout">Logout {{ currentUser.name }}</button>

    <input type="text" @input="handleInput" placeholder="Type something...">

    <!-- Example using component ref -->
    <!-- <CustomInputComponent ref="customInputRef" /> -->
  </div>
</template>
```

**Key TypeScript Integration Points:**

*   **`lang="ts"`:** Essential on `<script setup>`.
*   **`defineProps<Type>()`:** Use generic for type-safe props. Use `withDefaults` for defaults.
*   **`defineEmits<{...}>()`:** Use generic with call signatures for type-safe emits.
*   **`defineModel<Type>()`:** Use generic for type-safe `v-model`.
*   **`ref<Type>()` / `reactive<Type>()`:** Explicit types for reactive state if inference isn't sufficient.
*   **`computed<Type>()`:** Explicit return type for computed properties if needed.
*   **Function Signatures:** Type function parameters and return values.
*   **Event Handlers:** Type the `event` parameter (e.g., `Event`, `MouseEvent`, `KeyboardEvent`). Use type assertions (`as HTMLInputElement`) to access specific event target properties.
*   **Template Refs:** Type the `ref` with the element/component type (e.g., `Ref<HTMLInputElement | null>`, `Ref<InstanceType<typeof MyComponent> | null>`). Remember the initial `null` value.

Using TypeScript with `<script setup>` provides a robust and efficient way to build type-safe Vue applications, significantly improving code quality and developer productivity.