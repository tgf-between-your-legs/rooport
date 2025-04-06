TITLE: Optimizing Props Stability in Vue.js Components
DESCRIPTION: Illustrates how to improve update performance by computing derived data in the parent component instead of passing frequently changing props to child components.

LANGUAGE: vue
CODE:
<ListItem
  v-for="item in list"
  :id="item.id"
  :active="item.id === activeId" />

----------------------------------------

TITLE: Basic v-model Usage with Text Input in Vue
DESCRIPTION: Demonstrates the basic usage of v-model directive with a text input, showing two-way data binding between the input value and a reactive variable.

LANGUAGE: vue
CODE:
<p>Message is: {{ message }}</p>
<input v-model="message" placeholder="edit me" />

----------------------------------------

TITLE: Using Refs in Vue.js Single-File Components with <script setup>
DESCRIPTION: Demonstrates the simplified usage of refs in Single-File Components using <script setup>. The ref and related functions are automatically exposed to the template without needing an explicit return statement.

LANGUAGE: vue
CODE:
<script setup>
import { ref } from 'vue'

const count = ref(0)

function increment() {
  count.value++
}
</script>

<template>
  <button @click="increment">
    {{ count }}
  </button>
</template>

----------------------------------------

TITLE: Defining Basic Vue Component (Options API)
DESCRIPTION: Example of defining a basic Vue component using Options API with a data property and click counter functionality.

LANGUAGE: vue
CODE:
<script>
export default {
  data() {
    return {
      count: 0
    }
  }
}
</script>

<template>
  <button @click="count++">You clicked me {{ count }} times.</button>
</template>

----------------------------------------

TITLE: Basic Vue.js Application Setup - Options API
DESCRIPTION: Demonstrates creating a basic Vue application using Options API with a counter component. Shows how to create the app instance and handle state using the data option.

LANGUAGE: javascript
CODE:
import { createApp } from 'vue'

createApp({
  data() {
    return {
      count: 0
    }
  }
}).mount('#app')

----------------------------------------

TITLE: Creating Value Watchers with watch()
DESCRIPTION: Watches reactive data sources and calls a callback when sources change. Supports watching multiple sources, deep watching, and effect cleanup.

LANGUAGE: typescript
CODE:
function watch<T>(
  source: WatchSource<T>,
  callback: WatchCallback<T>,
  options?: WatchOptions
): WatchHandle

LANGUAGE: javascript
CODE:
const state = reactive({ count: 0 })
watch(
  () => state.count,
  (count, prevCount) => {
    /* ... */
  }
)

----------------------------------------

TITLE: Attribute Binding with v-bind
DESCRIPTION: Demonstrates how to bind HTML attributes using v-bind directive and its shorthand syntax.

LANGUAGE: vue-html
CODE:
<div v-bind:id="dynamicId"></div>

----------------------------------------

TITLE: Creating Reactive References with ref()
DESCRIPTION: Creates a reactive and mutable reference object with a .value property containing the inner value. The ref object tracks reads/writes and triggers reactive updates.

LANGUAGE: typescript
CODE:
function ref<T>(value: T): Ref<UnwrapRef<T>>

interface Ref<T> {
  value: T
}

LANGUAGE: javascript
CODE:
const count = ref(0)
console.log(count.value) // 0

count.value = 1
console.log(count.value) // 1

----------------------------------------

TITLE: Installing Vue Project with Package Managers
DESCRIPTION: Commands to create a new Vue project using different package managers (npm, pnpm, yarn, bun) via create-vue scaffolding tool

LANGUAGE: sh
CODE:
$ npm create vue@latest

LANGUAGE: sh
CODE:
$ pnpm create vue@latest

LANGUAGE: sh
CODE:
# For Yarn (v1+)
$ yarn create vue

# For Yarn Modern (v2+)
$ yarn create vue@latest

# For Yarn ^v4.11
$ yarn dlx create-vue@latest

LANGUAGE: sh
CODE:
$ bun create vue@latest

----------------------------------------

TITLE: Vue Single-File Component - Complete Example
DESCRIPTION: Comprehensive example of a Vue Single-File Component showing script, template, and style sections working together.

LANGUAGE: vue
CODE:
<script setup>
import { ref } from 'vue'
const count = ref(0)
</script>

<template>
  <button @click="count++">Count is: {{ count }}</button>
</template>

<style scoped>
button {
  font-weight: bold;
}
</style>

----------------------------------------

TITLE: Creating Vue Application Instance
DESCRIPTION: Demonstrates how to create a Vue application instance using createApp() method with both inline and imported root components.

LANGUAGE: typescript
CODE:
function createApp(rootComponent: Component, rootProps?: object): App

LANGUAGE: javascript
CODE:
import { createApp } from 'vue'

const app = createApp({
  /* root component options */
})

LANGUAGE: javascript
CODE:
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

----------------------------------------

TITLE: Basic v-for Usage with Array in Vue.js
DESCRIPTION: Demonstrates how to use v-for directive to render a list of items from an array. Shows examples for both Composition API and Options API.

LANGUAGE: javascript
CODE:
const items = ref([{ message: 'Foo' }, { message: 'Bar' }])

LANGUAGE: javascript
CODE:
data() {
  return {
    items: [{ message: 'Foo' }, { message: 'Bar' }]
  }
}

LANGUAGE: vue-html
CODE:
<li v-for="item in items">
  {{ item.message }}
</li>

----------------------------------------

TITLE: Creating Reactive Objects with reactive()
DESCRIPTION: Creates a reactive proxy of an object with deep reactivity. Automatically unwraps refs while maintaining reactivity. The proxy is not equal to the original object.

LANGUAGE: typescript
CODE:
function reactive<T extends object>(target: T): UnwrapNestedRefs<T>

LANGUAGE: javascript
CODE:
const obj = reactive({ count: 0 })
obj.count++

----------------------------------------

TITLE: Two-way Binding with v-model Directive in Vue
DESCRIPTION: The v-model directive creates two-way data bindings on form inputs and components. It automatically picks the correct way to update the element based on the input type.

LANGUAGE: vue
CODE:
<input v-model="message">
<textarea v-model="message"></textarea>
<select v-model="selected">
  <option>A</option>
  <option>B</option>
  <option>C</option>
</select>

----------------------------------------

TITLE: Creating Vue Application Instance in JavaScript
DESCRIPTION: This snippet demonstrates how to create a new Vue application instance using the createApp function. It's the starting point for any Vue application.

LANGUAGE: javascript
CODE:
import { createApp } from 'vue'

const app = createApp({
  /* root component options */
})

----------------------------------------

TITLE: Emitting Events in Vue Template
DESCRIPTION: Demonstrates how to emit a custom event directly in a Vue template using the $emit method.

LANGUAGE: vue-html
CODE:
<button @click="$emit('someEvent')">Click Me</button>

----------------------------------------

TITLE: Vue Options API Component Example
DESCRIPTION: Demonstrates a complete component using Options API with lifecycle hooks, methods, and state management.

LANGUAGE: vue
CODE:
<script>
export default {
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      this.count++
    }
  },
  mounted() {
    console.log(`The initial count is ${this.count}.`)
  }
}
</script>

<template>
  <button @click="increment">Count is: {{ count }}</button>
</template>

----------------------------------------

TITLE: Basic Text Interpolation in Vue
DESCRIPTION: Demonstrates basic text interpolation using Vue's mustache syntax (double curly braces) to display dynamic content.

LANGUAGE: vue-html
CODE:
<span>Message: {{ msg }}</span>

----------------------------------------

TITLE: Dynamic Select Options with v-for and v-model in Vue
DESCRIPTION: Shows how to dynamically render select options using v-for and bind them with v-model.

LANGUAGE: javascript
CODE:
const selected = ref('A')

const options = ref([
  { text: 'One', value: 'A' },
  { text: 'Two', value: 'B' },
  { text: 'Three', value: 'C' }
])

LANGUAGE: vue
CODE:
<select v-model="selected">
  <option v-for="option in options" :value="option.value">
    {{ option.text }}
  </option>
</select>

<div>Selected: {{ selected }}</div>

----------------------------------------

TITLE: Props Validation Configuration
DESCRIPTION: Comprehensive example of prop validation including type checks, required props, defaults, and custom validators

LANGUAGE: js
CODE:
defineProps({
  propA: Number,
  propB: [String, Number],
  propC: {
    type: String,
    required: true
  },
  propD: {
    type: [String, null],
    required: true
  },
  propE: {
    type: Number,
    default: 100
  },
  propF: {
    type: Object,
    default(rawProps) {
      return { message: 'hello' }
    }
  },
  propG: {
    validator(value, props) {
      return ['success', 'warning', 'danger'].includes(value)
    }
  }
})

----------------------------------------

TITLE: Defining a Vue Single-File Component with Composition API
DESCRIPTION: This snippet shows the structure of a Vue Single-File Component using the Composition API with <script setup>. It demonstrates reactive data management, template rendering, and component-scoped styling.

LANGUAGE: vue
CODE:
<script setup>
import { ref } from 'vue'
const greeting = ref('Hello World!')
</script>

<template>
  <p class="greeting">{{ greeting }}</p>
</template>

<style>
.greeting {
  color: red;
  font-weight: bold;
}
</style>

----------------------------------------

TITLE: Creating Global and Local State with Composition API
DESCRIPTION: This snippet demonstrates how to create and share both global and local state using Vue's Composition API. It uses ref to create reactive state and exports a composable function.

LANGUAGE: javascript
CODE:
import { ref } from 'vue'

// global state, created in module scope
const globalCount = ref(1)

export function useCount() {
  // local state, created per-component
  const localCount = ref(1)

  return {
    globalCount,
    localCount
  }
}

----------------------------------------

TITLE: Basic Script Setup Usage in Vue
DESCRIPTION: Basic example of using <script setup> syntax in Vue SFC to declare and expose variables to the template.

LANGUAGE: vue
CODE:
<script setup>
console.log('hello script setup')
</script>

----------------------------------------

TITLE: Basic Vue Component with setup() Hook
DESCRIPTION: Demonstrates basic usage of setup() hook with ref for reactive state management and template integration. Shows how to expose reactive state to both template and other Options API hooks.

LANGUAGE: vue
CODE:
<script>
import { ref } from 'vue'

export default {
  setup() {
    const count = ref(0)

    // expose to template and other options API hooks
    return {
      count
    }
  },

  mounted() {
    console.log(this.count) // 0
  }
}
</script>

<template>
  <button @click="count++">{{ count }}</button>
</template>

----------------------------------------

TITLE: Defining Vue Component with TypeScript using defineComponent
DESCRIPTION: Example showing how to define a Vue component using TypeScript with defineComponent() to enable proper type inference for component options including props, data, and lifecycle methods.

LANGUAGE: typescript
CODE:
import { defineComponent } from 'vue'

export default defineComponent({
  // type inference enabled
  props: {
    name: String,
    msg: { type: String, required: true }
  },
  data() {
    return {
      count: 1
    }
  },
  mounted() {
    this.name // type: string | undefined
    this.msg // type: string
    this.count // type: number
  }
})

----------------------------------------

TITLE: Defining a Vue Single-File Component with Options API
DESCRIPTION: This snippet demonstrates the structure of a Vue Single-File Component using the Options API. It includes a script section for component logic, a template for the view, and a style section for CSS.

LANGUAGE: vue
CODE:
<script>
export default {
  data() {
    return {
      greeting: 'Hello World!'
    }
  }
}
</script>

<template>
  <p class="greeting">{{ greeting }}</p>
</template>

<style>
.greeting {
  color: red;
  font-weight: bold;
}
</style>

----------------------------------------

TITLE: Component Naming Examples in Vue
DESCRIPTION: Demonstrates the correct multi-word naming convention for Vue components to prevent conflicts with HTML elements.

LANGUAGE: vue-html
CODE:
<!-- Bad Examples -->
<Item />
<item></item>

<!-- Good Examples -->
<TodoItem />
<todo-item></todo-item>

----------------------------------------

TITLE: Writable Computed Property Example
DESCRIPTION: Example of implementing a writable computed property with both getter and setter functions.

LANGUAGE: javascript
CODE:
export default {
  data() {
    return {
      firstName: 'John',
      lastName: 'Doe'
    }
  },
  computed: {
    fullName: {
      get() {
        return this.firstName + ' ' + this.lastName
      },
      set(newValue) {
        [this.firstName, this.lastName] = newValue.split(' ')
      }
    }
  }
}

----------------------------------------

TITLE: Attribute Binding with v-bind Directive in Vue
DESCRIPTION: The v-bind directive dynamically binds attributes or component props to expressions. It supports various value types and has shorthand syntax using ':'.

LANGUAGE: vue
CODE:
<!-- bind an attribute -->
<img v-bind:src="imageSrc" />

<!-- shorthand -->
<img :src="imageSrc" />

<!-- class binding -->
<div :class="{ red: isRed }"></div>

<!-- style binding -->
<div :style="{ fontSize: size + 'px' }"></div>

<!-- binding an object of attributes -->
<div v-bind="{ id: someProp, 'other-attr': otherProp }"></div>

----------------------------------------

TITLE: Computed Property Implementation (Composition API)
DESCRIPTION: Implementation of a computed property using Composition API with computed ref to determine published books status.

LANGUAGE: vue
CODE:
<script setup>
import { reactive, computed } from 'vue'

const author = reactive({
  name: 'John Doe',
  books: [
    'Vue 2 - Advanced Guide',
    'Vue 3 - Basic Guide',
    'Vue 4 - The Mystery'
  ]
})

const publishedBooksMessage = computed(() => {
  return author.books.length > 0 ? 'Yes' : 'No'
})
</script>

<template>
  <p>Has published books:</p>
  <span>{{ publishedBooksMessage }}</span>
</template>

----------------------------------------

TITLE: Basic Vue SFC Structure Example
DESCRIPTION: Demonstrates the fundamental structure of a Vue Single-File Component with template, script, style, and custom blocks.

LANGUAGE: vue
CODE:
<template>
  <div class="example">{{ msg }}</div>
</template>

<script>
export default {
  data() {
    return {
      msg: 'Hello world!'
    }
  }
}
</script>

<style>
.example {
  color: red;
}
</style>

<custom1>
  This could be e.g. documentation for the component.
</custom1>

----------------------------------------

TITLE: Configuring Vue Application Error Handler in JavaScript
DESCRIPTION: This snippet shows how to configure an app-level error handler for a Vue application. This handler will capture errors from all descendant components.

LANGUAGE: javascript
CODE:
app.config.errorHandler = (err) => {
  /* handle error */
}

----------------------------------------

TITLE: Event Handling with v-on Directive in Vue
DESCRIPTION: The v-on directive attaches event listeners to elements. It supports method handlers, inline statements, and modifiers for common operations like event propagation control.

LANGUAGE: vue
CODE:
<!-- method handler -->
<button v-on:click="doThis"></button>

<!-- inline statement -->
<button v-on:click="doThat('hello', $event)"></button>

<!-- shorthand -->
<button @click="doThis"></button>

<!-- stop propagation -->
<button @click.stop="doThis"></button>

<!-- prevent default -->
<button @click.prevent="doThis"></button>

----------------------------------------

TITLE: Configuring Error Handling for Production in Vue
DESCRIPTION: This snippet demonstrates how to set up an app-level error handler in Vue to report errors to tracking services. It shows the creation of a Vue app instance and configuration of the errorHandler property.

LANGUAGE: javascript
CODE:
import { createApp } from 'vue'

const app = createApp(...)

app.config.errorHandler = (err, instance, info) => {
  // report error to tracking services
}

----------------------------------------

TITLE: Basic Props Declaration in Vue 3 Composition API
DESCRIPTION: Shows how to declare props using defineProps macro in a Single File Component with <script setup>

LANGUAGE: vue
CODE:
<script setup>
const props = defineProps(['foo'])

console.log(props.foo)
</script>

----------------------------------------

TITLE: Registering Lifecycle Hook with Options API in Vue
DESCRIPTION: Example of registering a mounted lifecycle hook using Vue's Options API. The hook logs a message when the component is mounted to the DOM.

LANGUAGE: javascript
CODE:
export default {
  mounted() {
    console.log(`the component is now mounted.`)
  }
}

----------------------------------------

TITLE: Creating Multiple Vue Application Instances in JavaScript
DESCRIPTION: This snippet shows how to create and mount multiple Vue application instances on the same page, each with its own configuration and global assets.

LANGUAGE: javascript
CODE:
const app1 = createApp({
  /* ... */
})
app1.mount('#container-1')

const app2 = createApp({
  /* ... */
})
app2.mount('#container-2')

----------------------------------------

TITLE: Emitting Events with Arguments
DESCRIPTION: Shows how to emit an event with additional arguments to pass data to the parent component.

LANGUAGE: vue-html
CODE:
<button @click="$emit('increaseBy', 1)">
  Increase by 1
</button>

----------------------------------------

TITLE: Method Handler with Event Object in Vue.js
DESCRIPTION: Shows how to handle events using component methods, demonstrating access to the native DOM event object and component instance.

LANGUAGE: javascript
CODE:
const name = ref('Vue.js')\n\nfunction greet(event) {\n  alert(`Hello ${name.value}!`)\n  // `event` is the native DOM event\n  if (event) {\n    alert(event.target.tagName)\n  }\n}

LANGUAGE: vue-html
CODE:
<!-- `greet` is the name of the method defined above -->\n<button @click="greet">Greet</button>

----------------------------------------

TITLE: Basic v-model Implementation with Composition API
DESCRIPTION: Shows how to implement v-model on a component using the defineModel macro in Vue 3.4+.

LANGUAGE: vue
CODE:
<script setup>
const model = defineModel()

function update() {
  model.value++
}
</script>

<template>
  <div>Parent bound v-model is: {{ model }}</div>
  <button @click="update">Increment</button>
</template>

----------------------------------------

TITLE: Defining Component Data in Vue
DESCRIPTION: Demonstrates how to define the initial reactive state for a Vue component using the data option. The function returns a plain JavaScript object that becomes reactive.

LANGUAGE: javascript
CODE:
export default {
  data() {
    return { a: 1 }
  },
  created() {
    console.log(this.a) // 1
    console.log(this.$data) // { a: 1 }
  }
}

----------------------------------------

TITLE: Binding Styles to Arrays in Vue
DESCRIPTION: Shows how to bind multiple style objects to an element using an array.

LANGUAGE: vue-html
CODE:
<div :style="[baseStyles, overridingStyles]"></div>

----------------------------------------

TITLE: Binding HTML Classes to Objects in Vue Template
DESCRIPTION: Demonstrates using v-bind to dynamically toggle classes based on data properties. The presence of the 'active' class is determined by the truthiness of isActive.

LANGUAGE: vue-html
CODE:
<div :class="{ active: isActive }"></div>

----------------------------------------

TITLE: Mouse Position Tracking Composable in Vue
DESCRIPTION: A reusable composable function that encapsulates mouse tracking logic using Vue's Composition API.

LANGUAGE: javascript
CODE:
// mouse.js
import { ref, onMounted, onUnmounted } from 'vue'

export function useMouse() {
  const x = ref(0)
  const y = ref(0)

  function update(event) {
    x.value = event.pageX
    y.value = event.pageY
  }

  onMounted(() => window.addEventListener('mousemove', update))
  onUnmounted(() => window.removeEventListener('mousemove', update))

  return { x, y }
}

----------------------------------------

TITLE: Basic Data Structure with Composition API
DESCRIPTION: Example showing how to define reactive data structure in Vue using Composition API with reactive author object.

LANGUAGE: javascript
CODE:
const author = reactive({
  name: 'John Doe',
  books: [
    'Vue 2 - Advanced Guide',
    'Vue 3 - Basic Guide',
    'Vue 4 - The Mystery'
  ]
})

----------------------------------------

TITLE: Implementing Basic Client-Side Routing in Vue (Composition API)
DESCRIPTION: A simple client-side router implementation using Vue's Composition API. Uses hash-based routing with dynamic components to handle route changes and component rendering based on URL paths.

LANGUAGE: vue
CODE:
<script setup>
import { ref, computed } from 'vue'
import Home from './Home.vue'
import About from './About.vue'
import NotFound from './NotFound.vue'

const routes = {
  '/': Home,
  '/about': About
}

const currentPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  currentPath.value = window.location.hash
})

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || '/'] || NotFound
})
</script>

<template>
  <a href="#/">Home</a> |
  <a href="#/about">About</a> |
  <a href="#/non-existent-path">Broken Link</a>
  <component :is="currentView" />
</template>

----------------------------------------

TITLE: Select Binding with v-model in Vue
DESCRIPTION: Demonstrates v-model usage with select elements, including single and multiple selections.

LANGUAGE: vue
CODE:
<select v-model="selected">
  <option disabled value="">Please select one</option>
  <option>A</option>
  <option>B</option>
  <option>C</option>
</select>

LANGUAGE: vue
CODE:
<select v-model="selected" multiple>
  <option>A</option>
  <option>B</option>
  <option>C</option>
</select>

----------------------------------------

TITLE: JavaScript Expressions in Vue Templates
DESCRIPTION: Examples of using JavaScript expressions within Vue template bindings for dynamic content.

LANGUAGE: vue-html
CODE:
{{ number + 1 }}

{{ ok ? 'YES' : 'NO' }}

{{ message.split('').reverse().join('') }}

<div :id="`list-${id}`"></div>

----------------------------------------

TITLE: Using a Vue.js Component with Class Attribute
DESCRIPTION: Shows how to use a custom Vue.js component with a class attribute, demonstrating attribute inheritance.

LANGUAGE: vue-html
CODE:
<MyButton class="large" />

----------------------------------------

TITLE: Registering Lifecycle Hook with Composition API in Vue
DESCRIPTION: Example of registering an onMounted lifecycle hook using Vue's Composition API within a script setup block. The hook logs a message when the component is mounted to the DOM.

LANGUAGE: vue
CODE:
<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  console.log(`the component is now mounted.`)
})
</script>

----------------------------------------

TITLE: Named Slots in Vue.js
DESCRIPTION: Shows how to use named slots to define multiple slot outlets in a single component.

LANGUAGE: vue-html
CODE:
<div class="container">
  <header>
    <slot name="header"></slot>
  </header>
  <main>
    <slot></slot>
  </main>
  <footer>
    <slot name="footer"></slot>
  </footer>
</div>

LANGUAGE: vue-html
CODE:
<BaseLayout>
  <template #header>
    <h1>Here might be a page title</h1>
  </template>

  <template #default>
    <p>A paragraph for the main content.</p>
    <p>And another one.</p>
  </template>

  <template #footer>
    <p>Here's some contact info</p>
  </template>
</BaseLayout>

----------------------------------------

TITLE: Typing reactive() in Vue 3 with TypeScript
DESCRIPTION: Demonstrates how to type reactive() objects in Vue 3 using TypeScript, including type inference and explicit interface typing.

LANGUAGE: typescript
CODE:
import { reactive } from 'vue'

// inferred type: { title: string }
const book = reactive({ title: 'Vue 3 Guide' })

interface Book {
  title: string
  year?: number
}

const book: Book = reactive({ title: 'Vue 3 Guide' })

----------------------------------------

TITLE: Reactivity with Script Setup
DESCRIPTION: Shows how to create reactive state using ref and access it in the template with automatic unwrapping.

LANGUAGE: vue
CODE:
<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <button @click="count++">{{ count }}</button>
</template>

----------------------------------------

TITLE: v-for with Index in Vue.js
DESCRIPTION: Shows how to use v-for with an additional index parameter. Includes access to parent scope properties.

LANGUAGE: javascript
CODE:
const parentMessage = ref('Parent')
const items = ref([{ message: 'Foo' }, { message: 'Bar' }])

LANGUAGE: javascript
CODE:
data() {
  return {
    parentMessage: 'Parent',
    items: [{ message: 'Foo' }, { message: 'Bar' }]
  }
}

LANGUAGE: vue-html
CODE:
<li v-for="(item, index) in items">
  {{ parentMessage }} - {{ index }} - {{ item.message }}
</li>

----------------------------------------

TITLE: Using v-if Directive in Vue.js
DESCRIPTION: Demonstrates the usage of v-if directive for conditional rendering in Vue.js. The element will only be rendered if the condition is truthy.

LANGUAGE: vue-html
CODE:
<h1 v-if="awesome">Vue is awesome!</h1>

----------------------------------------

TITLE: Vue Render Function with Stable Fragment
DESCRIPTION: Demonstrates a compiled Vue render function for a template with multiple root nodes, using a stable fragment for optimized rendering.

LANGUAGE: javascript
CODE:
export function render() {
  return (_openBlock(), _createElementBlock(_Fragment, null, [
    /* children */
  ], 64 /* STABLE_FRAGMENT */))
}

----------------------------------------

TITLE: Rendering Slot Content in Vue.js Child Component
DESCRIPTION: This snippet demonstrates how to render slot content passed from a parent component in a child component using the <slot> element as an outlet.

LANGUAGE: vue-html
CODE:
<!-- in child template -->
<slot/>

LANGUAGE: vue-html
CODE:
<!-- in child template -->
<slot></slot>

----------------------------------------

TITLE: Event Listener Inheritance in Vue.js Components
DESCRIPTION: Demonstrates how event listeners are inherited by child components in Vue.js.

LANGUAGE: vue-html
CODE:
<MyButton @click="onClick" />

----------------------------------------

TITLE: Vue Component with Composition API and TypeScript
DESCRIPTION: Demonstrates using TypeScript with Vue's Composition API, showing type inference for props in the setup function.

LANGUAGE: typescript
CODE:
import { defineComponent } from 'vue'

export default defineComponent({
  // type inference enabled
  props: {
    message: String
  },
  setup(props) {
    props.message // type: string | undefined
  }
})

----------------------------------------

TITLE: Implementing v-else with v-if in Vue.js
DESCRIPTION: Shows how to use v-else directive in conjunction with v-if for conditional rendering. It includes a toggle button to switch between two states.

LANGUAGE: vue-html
CODE:
<button @click="awesome = !awesome">Toggle</button>

<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>

----------------------------------------

TITLE: v-for with an Object in Vue.js
DESCRIPTION: Demonstrates how to use v-for to iterate through object properties. Shows examples with value, key, and index.

LANGUAGE: javascript
CODE:
const myObject = reactive({
  title: 'How to do lists in Vue',
  author: 'Jane Doe',
  publishedAt: '2016-04-10'
})

LANGUAGE: javascript
CODE:
data() {
  return {
    myObject: {
      title: 'How to do lists in Vue',
      author: 'Jane Doe',
      publishedAt: '2016-04-10'
    }
  }
}

LANGUAGE: vue-html
CODE:
<li v-for="(value, key, index) in myObject">
  {{ index }}. {{ key }}: {{ value }}
</li>