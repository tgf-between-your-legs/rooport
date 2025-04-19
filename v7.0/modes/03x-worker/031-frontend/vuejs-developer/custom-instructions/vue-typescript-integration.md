# Vue.js: TypeScript Integration

Using TypeScript effectively within Vue 3 components, particularly with `<script setup>`.

## Core Concept: Type Safety in Components

Vue 3 has excellent built-in TypeScript support, especially when using Single-File Components (SFCs) with the `<script setup>` syntax. This allows you to add static types to your props, emits, reactive state, computed properties, and more, catching errors at compile time.

**Key Benefits:**

*   **Stronger Prop/Emit Contracts:** Clearly define the expected types for data passed between components.
*   **Improved Refactoring:** Types make it safer to rename variables or restructure code.
*   **Better Autocompletion:** IDEs provide more accurate suggestions based on types.
*   **Early Error Detection:** Catch type mismatches before running the code.

## Using TypeScript with `<script setup>`

Add `lang="ts"` to the `<script setup>` tag.

```vue
<script setup lang="ts">
// Import types and functions
import { ref, computed, PropType, defineProps, defineEmits } from 'vue';

// --- Props ---
// Use defineProps with a generic type argument
interface User {
  id: number;
  name: string;
}
interface Props {
  message?: string;
  user: User | null;
  tags: string[];
  status: 'pending' | 'active' | 'inactive'; // Literal union type
}
const props = withDefaults(defineProps<Props>(), {
  message: 'Default',
  user: null,
  tags: () => [], // Use factory function for object/array defaults
});

// --- Emits ---
// Use defineEmits with a generic type argument for typed payloads
const emit = defineEmits<{
  (e: 'userUpdate', payload: { id: number; name: string }): void;
  (e: 'statusChange', newStatus: Props['status']): void; // Reference prop type
}>();

// --- Reactive State ---
// Type inference often works well
const count = ref(0); // Inferred as Ref<number>
const isAdmin = ref(false); // Inferred as Ref<boolean>

// Explicit typing if needed
const items = ref<string[]>([]);
const complexData = reactive<{ value: number | null; label?: string }>({ value: null });

// --- Computed ---
// Return type is usually inferred, but can be explicit
const formattedMessage = computed<string>(() => `Msg: ${props.message}`);
const canActivate = computed<boolean>(() => props.status === 'pending' && !!props.user);

// --- Functions ---
// Parameter and return types
function activateUser(): void {
  if (props.user) {
    emit('statusChange', 'active');
    emit('userUpdate', { id: props.user.id, name: props.user.name.toUpperCase() });
  }
}

// Type DOM event handlers
function handleClick(event: MouseEvent): void {
  console.log('Clicked!', event.clientX);
}

// --- Template Refs ---
// Type the ref with the element type (or component type)
const inputRef = ref<HTMLInputElement | null>(null);
onMounted(() => {
  inputRef.value?.focus(); // Access element via .value (might be null initially)
});

</script>

<template>
  <div>
    <p>{{ formattedMessage }}</p>
    <p v-if="props.user">User: {{ props.user.name }}</p>
    <p>Status: {{ props.status }}</p>
    <button @click="activateUser" :disabled="!canActivate">Activate</button>
    <input type="text" ref="inputRef" @click="handleClick">
  </div>
</template>
```

## Key TypeScript Integration Points

*   **`lang="ts"`:** Essential on the `<script setup>` tag.
*   **`defineProps<Type>()`:** Use generic argument for type-safe props definition. Use `withDefaults` for default values.
*   **`defineEmits<{ (e: 'event', payload: Type): void }>()`:** Use generic argument with call signatures for type-safe emits.
*   **`ref<Type>()` / `reactive<Type>()`:** Use generic arguments for explicit typing of reactive state if inference isn't sufficient.
*   **`computed<Type>()`:** Explicit return type for computed properties if needed.
*   **Function Signatures:** Type function parameters and return values.
*   **Event Handlers:** Type the `event` parameter (e.g., `MouseEvent`, `KeyboardEvent`).
*   **Template Refs:** Type the `ref` with the expected element type (e.g., `Ref<HTMLInputElement | null>`). Remember it might be `null` before mounting.
*   **`PropType<T>`:** Import from `vue` for complex prop types (like functions or generics) when using the `props` option (less common with `<script setup>`).

Using TypeScript with `<script setup>` provides a seamless and powerful way to build type-safe Vue components, catching errors early and improving the overall development experience.

*(Refer to the official Vue.js documentation on Using Vue with TypeScript and `<script setup>`.)*