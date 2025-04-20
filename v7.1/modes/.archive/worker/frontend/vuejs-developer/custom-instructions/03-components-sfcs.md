# Vue.js: Single-File Components (SFCs) & Props/Events

Building reusable UI elements using Vue's `.vue` file format and defining component communication.

## Core Concept: Encapsulated Components

Vue's Single-File Components (SFCs) provide a way to encapsulate the template, logic, and styles of a component within a single `.vue` file. This promotes modularity, reusability, and better organization.

**Structure of a `.vue` file:**

1.  **`<template>`:** Contains the HTML-based template syntax for the component's structure and layout. There should be exactly one top-level `<template>` block.
2.  **`<script setup lang="ts">` (Recommended):** Contains the component's TypeScript logic using the Composition API. Code runs directly in the `setup` context. Variables, imports, and functions declared are automatically exposed to the template.
3.  **`<script>` (Options API / Non-setup):** Contains the component's JavaScript/TypeScript logic, typically exporting a default object for Options API or containing the `setup()` function if not using `<script setup>`. Less common for new Vue 3 development.
4.  **`<style>`:** Contains CSS rules for the component.
    *   **`scoped` attribute (`<style scoped>`):** Limits CSS rules to apply only to elements within the current component, preventing global style conflicts. Achieved via data attributes added during compilation. This is the **recommended** approach for component styles.
    *   **CSS Modules (`<style module>`):** Allows creating locally scoped CSS class names accessible via the `$style` object in the template or script.
    *   Can use preprocessors like SCSS or Less by adding the `lang` attribute (e.g., `<style lang="scss" scoped>`).

## Defining Props (`defineProps`)

Props allow parent components to pass data down to child components. In `<script setup>`, use the `defineProps` macro with TypeScript generics for type safety.

```typescript
// ChildComponent.vue
<script setup lang="ts">
import { computed } from 'vue';

// --- Define Props ---
// Type-based declaration (recommended with TypeScript)
interface Props {
  title: string;
  likes?: number; // Optional prop
  isActive: boolean;
  tags: string[];
  // Example complex prop type
  // onUpdate?: (payload: { id: number }) => void;
}

// withDefaults provides default values for optional props
// Use factory functions for object/array defaults to avoid sharing refs
const props = withDefaults(defineProps<Props>(), {
  likes: 0, // Default value for 'likes'
  tags: () => ['default-tag'],
  // isActive doesn't need a default if required or handled otherwise
});

// Access props directly in <script setup> and template
const formattedTitle = computed(() => `Item: ${props.title}`);

// Props are readonly within the child component.
// Do NOT attempt to mutate props directly (e.g., props.likes++).
// If a change is needed based on child interaction, emit an event.
</script>

<template>
  <div>
    <h3>{{ formattedTitle }} (Active: {{ isActive }})</h3>
    <p>Likes: {{ props.likes }}</p>
    <ul>
      <li v-for="tag in props.tags" :key="tag">{{ tag }}</li>
    </ul>
    <!-- Example using complex prop -->
    <!-- <button @click="props.onUpdate?.({ id: 1 })">Call Update Prop</button> -->
  </div>
</template>
```

```vue
<!-- ParentComponent.vue -->
<template>
  <ChildComponent
    title="My Item"
    :is-active="true"
    :tags="['tag1', 'tag2']"
    :likes="15"
    <!-- :onUpdate="handleChildUpdate" -->
  />
  <ChildComponent
    title="Another Item"
    :is-active="false"
    :tags="['tag3']"
    <!-- likes prop uses default value (0) -->
  />
</template>

<script setup lang="ts">
import ChildComponent from './ChildComponent.vue';

// function handleChildUpdate(payload: { id: number }) {
//   console.log('Update received from child:', payload);
// }
</script>
```

## Defining Emits (`defineEmits`)

Events allow child components to communicate back up to parent components, typically in response to user interactions. In `<script setup>`, use the `defineEmits` macro with TypeScript generics for type safety.

```typescript
// ChildComponent.vue (continued from above)
<script setup lang="ts">
// ... imports and defineProps ...

// --- Define Emits ---
// Type-based declaration (recommended with TypeScript)
const emit = defineEmits<{
  (e: 'updateLikes', newLikes: number): void; // Event with payload type
  (e: 'deleteItem', id: string): void;
  (e: 'simpleEvent'): void; // Event without payload
}>();

function handleLikeClick() {
  const newLikes = (props.likes ?? 0) + 1;
  emit('updateLikes', newLikes); // Emit event with payload
}

function handleDelete() {
    // Assuming component has an id prop or similar
    // emit('deleteItem', props.id);
    emit('deleteItem', 'item-id-placeholder');
}
</script>

<template>
  <div>
    <!-- ... other template content ... -->
    <button @click="handleLikeClick">Like</button>
    <button @click="handleDelete">Delete</button>
  </div>
</template>
```

```vue
<!-- ParentComponent.vue (continued) -->
<template>
  <ChildComponent
    title="My Item"
    :is-active="true"
    :tags="['tag1', 'tag2']"
    :likes="currentLikes"
    @update-likes="handleLikesUpdate" <!-- Listen for event using @event-name -->
    @delete-item="handleDeleteRequest"
  />
  <!-- ... -->
</template>

<script setup lang="ts">
import ChildComponent from './ChildComponent.vue';
import { ref } from 'vue';

const currentLikes = ref(15);

function handleLikesUpdate(newLikes: number) {
  console.log('Likes updated in parent:', newLikes);
  currentLikes.value = newLikes;
}

function handleDeleteRequest(id: string) {
    console.log('Delete requested for item:', id);
    // ... perform delete logic ...
}
</script>
```

## `defineModel` (Vue 3.3+)

Simplifies creating components that support `v-model` for two-way binding by implicitly defining a `modelValue` prop and an `update:modelValue` emit.

```typescript
// CustomInput.vue
<script setup lang="ts">
// Defines 'modelValue' prop and 'update:modelValue' emit implicitly
// Type argument defines the type of the model value
const model = defineModel<string>();
// Or with options: const model = defineModel<string>({ required: true });

// For named v-model (e.g., v-model:title="bookTitle")
// const title = defineModel<string>('title');
</script>

<template>
  <input
    type="text"
    :value="model"
    @input="model = ($event.target as HTMLInputElement).value"
    placeholder="Enter text..."
  />
  <!-- Example using named model -->
  <!-- <input type="text" v-model="title" placeholder="Enter title..."> -->
</template>
```

```vue
<!-- ParentComponent.vue -->
<script setup lang="ts">
import CustomInput from './CustomInput.vue';
import { ref } from 'vue';
const message = ref('Hello');
// const bookTitle = ref('Default Title');
</script>
<template>
  <CustomInput v-model="message" />
  <p>Message: {{ message }}</p>

  <!-- Example using named model -->
  <!-- <CustomInput v-model:title="bookTitle" /> -->
  <!-- <p>Book Title: {{ bookTitle }}</p> -->
</template>
```

SFCs are the standard way to build Vue applications, providing excellent organization. Use `defineProps` to receive data from parents and `defineEmits` (or `defineModel`) to communicate changes or actions back up. Always use TypeScript with `<script setup>` for robust component definitions.