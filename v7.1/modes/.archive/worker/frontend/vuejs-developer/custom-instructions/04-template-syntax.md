# Vue.js: Template Syntax

Understanding Vue's HTML-based template syntax for declarative rendering and data binding.

## Core Concept: Declarative Binding

Vue uses an HTML-based template syntax that allows you to declaratively bind the rendered DOM to the underlying component instance's data (from `<script setup>` or `data()`). Vue compiles templates into highly optimized JavaScript render functions.

**Key Features:**

*   **Text Interpolation:** Use double curly braces `{{ }}` (mustaches) for embedding JavaScript expressions (usually simple variable access or basic operations) directly into the text content.
*   **Directives:** Special attributes prefixed with `v-` that apply reactive side effects to the DOM when the expression's value changes.
*   **Attribute Binding:** Use `v-bind:` or its shorthand `:` to bind HTML attributes dynamically to component data.
*   **Event Handling:** Use `v-on:` or its shorthand `@` to listen to DOM events and run component methods or JavaScript expressions. Supports event modifiers (`.prevent`, `.stop`, `.once`, etc.) and key modifiers (`.enter`, `.tab`, etc.).
*   **Conditional Rendering:** Use `v-if`, `v-else-if`, `v-else` to conditionally render elements or template blocks. Elements are added/removed from the DOM.
*   **Conditional Display:** Use `v-show` to conditionally display elements by toggling the CSS `display` property. Elements are always rendered.
*   **List Rendering:** Use `v-for` to render a list of items based on an array or object. Requires a unique `:key`.
*   **Two-Way Binding:** Use `v-model` on form inputs (`<input>`, `<select>`, `<textarea>`) and custom components to create two-way data bindings.
*   **Slots:** Use `<slot>` elements as content distribution outlets in component templates (default, named, scoped).
*   **Raw HTML:** Use `v-html` to output raw HTML (use with extreme caution due to XSS risks).
*   **One-time Binding:** Use `v-once` to render an element and its children once, skipping future updates.

## Common Directives and Syntax

```vue
<template>
  <div :id="dynamicId" :class="[dynamicClass, { active: isActive }]">
    <!-- 1. Text Interpolation -->
    <h1>{{ pageTitle }}</h1>
    <p>Message: {{ message.toUpperCase() }}</p>
    <!-- Use v-html ONLY with trusted content or after sanitization -->
    <!-- <p>Raw HTML: <span v-html="sanitizedHtmlContent"></span></p> -->

    <!-- 2. Attribute Binding (v-bind or :) -->
    <img :src="imageUrl" :alt="imageAltText">
    <button :disabled="isButtonDisabled">Submit</button>

    <!-- Binding multiple attributes -->
    <div v-bind="divAttributesObject"></div>

    <!-- 3. Event Handling (v-on or @) -->
    <button @click="incrementCounter">Increment</button>
    <form @submit.prevent="handleSubmit"> <!-- .prevent modifier -->
      <input @keyup.enter="submitOnEnter"> <!-- .enter key modifier -->
      <button type="submit">Save</button>
    </form>

    <!-- 4. Conditional Rendering (v-if, v-else-if, v-else) -->
    <p v-if="status === 'loading'">Loading...</p>
    <p v-else-if="status === 'error'" class="error">An error occurred.</p>
    <div v-else>
      Data loaded: {{ data }}
    </div>
    <!-- Use v-show for frequent toggling -->
    <p v-show="isVisible">Toggled with v-show.</p>

    <!-- Conditional groups with <template> -->
    <template v-if="userLoggedIn">
      <p>Welcome, {{ userName }}!</p>
      <button @click="logout">Logout</button>
    </template>
    <template v-else>
      <button @click="login">Login</button>
    </template>

    <!-- 5. List Rendering (v-for) -->
    <ul>
      <!-- Always use :key with v-for for performance and state management -->
      <li v-for="item in items" :key="item.id">
        {{ item.name }}
      </li>
    </ul>
    <ul>
      <li v-for="(value, key, index) in myObject" :key="key">
        {{ index }}. {{ key }}: {{ value }}
      </li>
    </ul>
    <!-- v-for with a range -->
    <span v-for="n in 5" :key="n">{{ n }} </span>

    <!-- v-for with v-if (v-for has higher priority) -->
    <!-- Better to filter data source first if possible -->
    <ul>
      <template v-for="item in items" :key="item.id">
        <li v-if="!item.isHidden">
          {{ item.name }}
        </li>
      </template>
    </ul>
    <!-- Alternative: Computed property for filtered list -->
    <!-- <ul>
      <li v-for="item in visibleItems" :key="item.id">{{ item.name }}</li>
    </ul> -->

    <!-- 6. Two-Way Binding (v-model) -->
    <input type="text" v-model="inputText" placeholder="Type here">
    <p>Input: {{ inputText }}</p>

    <input type="checkbox" v-model="isChecked" id="checkbox">
    <label for="checkbox">{{ isChecked }}</label>

    <select v-model="selectedOption">
      <option disabled value="">Please select one</option>
      <option value="A">Option A</option>
      <option value="B">Option B</option>
    </select>

    <!-- v-model modifiers (.lazy, .number, .trim) -->
    <input type="text" v-model.lazy="lazyInputText" placeholder="Updates on change">
    <input type="text" v-model.number="numericInput" placeholder="Type number">
    <input type="text" v-model.trim="trimmedInput" placeholder="Trims whitespace">

    <!-- v-model on custom component (see 03-components-sfcs.md) -->
    <!-- <CustomInput v-model="customValue" /> -->
    <!-- <CustomInput v-model:title="customTitle" /> -->

    <!-- 7. Slots (see 03-components-sfcs.md) -->
    <!-- <MyLayout>
      <template #header><h1>Header Content</h1></template>
      <p>Default slot content</p>
      <template #footer="{ year }"><p>Footer Content {{ year }}</p></template>
    </MyLayout> -->

    <!-- 8. v-once -->
    <p v-once>This content will never change: {{ initialMessage }}</p>

  </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed } from 'vue';
// Dummy data for examples
const pageTitle = ref('Vue Template Syntax');
const message = ref('hello vue');
const dynamicId = ref('main-content');
const dynamicClass = ref('container');
const isActive = ref(true);
const imageUrl = ref('/path/to/image.jpg');
const imageAltText = ref('Descriptive text');
const isButtonDisabled = ref(false);
const divAttributesObject = reactive({ 'data-test': 'attrs', class: 'bg-blue' });
const status = ref('loaded'); // 'loading', 'error', 'loaded'
const data = ref({ info: 'Some data' });
const isVisible = ref(true);
const userLoggedIn = ref(false);
const userName = ref('User');
const items = ref([{ id: 1, name: 'Item 1', isHidden: false }, { id: 2, name: 'Item 2', isHidden: true }]);
const myObject = reactive({ title: 'Book', author: 'Author Name' });
const inputText = ref('');
const isChecked = ref(false);
const selectedOption = ref('');
const lazyInputText = ref('');
const numericInput = ref<number | null>(null);
const trimmedInput = ref('');
const initialMessage = ref('Loaded!');

// Computed property for filtered list example
// const visibleItems = computed(() => items.value.filter(item => !item.isHidden));

function incrementCounter() { console.log('increment'); }
function handleSubmit() { console.log('submit'); }
function submitOnEnter() { console.log('submit on enter'); }
function login() { userLoggedIn.value = true; }
function logout() { userLoggedIn.value = false; }
</script>

<style scoped>
.active { border: 1px solid green; }
.error { color: red; }
button { margin: 5px; }
.container { padding: 10px; }
.bg-blue { background-color: lightblue; }
</style>
```

Vue's template syntax provides a declarative and efficient way to map component state to the DOM. Understanding directives like `v-bind`, `v-on`, `v-if`, `v-for`, and `v-model` is fundamental to building Vue applications. Keep expressions within templates simple; move complex logic to computed properties or methods in `<script setup>`.