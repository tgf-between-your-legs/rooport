# Vue.js: Single-File Components (SFCs) & Props/Events

Building reusable UI elements using Vue's `.vue` file format and defining component communication.

## Core Concept: Encapsulated Components

Vue's Single-File Components (SFCs) provide a way to encapsulate the template, logic, and styles of a component within a single `.vue` file. This promotes modularity, reusability, and better organization.

**Structure of a `.vue` file:**

1.  **`<template>`:** Contains the HTML-based template syntax for the component's structure and layout. There should be exactly one top-level `<template>` block.
2.  **`<script>`:** Contains the component's JavaScript/TypeScript logic.
    *   **Options API:** Exports a default object with options like `data`, `methods`, `computed`, etc.
    *   **Composition API (`<script setup>`):** Recommended for Vue 3. Code runs directly in the `setup` context. Variables, imports, and functions declared are automatically exposed to the template. Use `<script setup lang="ts">` for TypeScript.
3.  **`<style>`:** Contains CSS rules for the component.
    *   **`scoped` attribute (`<style scoped>`):** Limits CSS rules to apply only to elements within the current component, preventing global style conflicts. Achieved via data attributes added during compilation.
    *   **CSS Modules (`<style module>`):** Allows creating locally scoped CSS class names accessible via the `$style` object in the template or script.
    *   Can use preprocessors like SCSS or Less by adding the `lang` attribute (e.g., `<style lang="scss" scoped>`).

## Defining Props (`defineProps`)

Props allow parent components to pass data down to child components. In `<script setup>`, use the `defineProps` macro.

```typescript
// ChildComponent.vue
<script setup lang="ts">
import { computed } from 'vue';

// --- Define Props ---
// Runtime declaration (less type safe)
// const props = defineProps(['title', 'likes']);

// Type-based declaration (recommended with TypeScript)
interface Props {
  title: string;
  likes?: number; // Optional prop
  isActive: boolean;
  tags: string[];
}
// withDefaults provides default values for optional props
const props = withDefaults(defineProps<Props>(), {
  likes: 0, // Default value for 'likes'
  // isActive doesn't need a default if required or handled otherwise
});

// Access props directly in <script setup> and template
const formattedTitle = computed(() => `Item: ${props.title}`);
</script>

<template>
  <div>
    <h3>{{ formattedTitle }} (Active: {{ isActive }})</h3>
    <p>Likes: {{ props.likes }}</p>
    <ul>
      <li v-for="tag in props.tags" :key="tag">{{ tag }}</li>
    </ul>
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
</script>
```

## Defining Emits (`defineEmits`)

Events allow child components to communicate back up to parent components, typically in response to user interactions. In `<script setup>`, use the `defineEmits` macro.

```typescript
// ChildComponent.vue (continued from above)
<script setup lang="ts">
// ... imports and defineProps ...

// --- Define Emits ---
// Runtime declaration
// const emit = defineEmits(['updateLikes', 'deleteItem']);

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

Simplifies creating components that support `v-model` for two-way binding.

```typescript
// CustomInput.vue
<script setup lang="ts">
// Defines 'modelValue' prop and 'update:modelValue' emit implicitly
const model = defineModel<string>();
// Or with options: const model = defineModel<string>({ required: true });

// For named v-model (e.g., v-model:title)
// const title = defineModel<string>('title');
</script>

<template>
  <input
    type="text"
    :value="model"
    @input="model = ($event.target as HTMLInputElement).value"
  />
</template>
```

```vue
<!-- ParentComponent.vue -->
<script setup lang="ts">
import CustomInput from './CustomInput.vue';
import { ref } from 'vue';
const message = ref('Hello');
</script>
<template>
  <CustomInput v-model="message" />
  <p>Message: {{ message }}</p>
</template>
```

SFCs are the standard way to build Vue applications, providing excellent organization. Use `defineProps` to receive data from parents and `defineEmits` (or `defineModel`) to communicate changes or actions back up.

*(Refer to the official Vue.js documentation on Single-File Components, Props, Events, and `v-model` on Components.)*