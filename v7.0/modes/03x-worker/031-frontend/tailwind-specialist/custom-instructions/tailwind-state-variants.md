# Tailwind CSS: State Variants (Hover, Focus, Dark Mode, etc.)

Applying styles conditionally based on element states or other conditions using Tailwind's variant prefixes.

## Core Concept: Conditional Styling with Variants

Tailwind provides **variant prefixes** that allow you to apply utility classes conditionally based on the element's state, parent state, media queries, or other conditions.

**Syntax:** `{variant}:{utility}` (e.g., `hover:bg-blue-700`, `focus:ring-2`, `dark:text-white`)

**Key Points:**

*   **Prefixing:** Variants are always added *before* the utility class they modify.
*   **Chaining:** Variants can be chained together, typically with state variants coming first, then responsive variants (e.g., `dark:hover:bg-gray-700`, `md:focus:ring-offset-4`).
*   **Configuration:** Available variants can be configured in `tailwind.config.js` under the `variants` key (though defaults cover most common cases).

## Common State Variants

These variants apply styles based on user interaction or element state:

*   **`hover:`:** Applies when the user hovers over the element with a mouse pointer.
    ```html
    <button class="bg-blue-500 hover:bg-blue-700 text-white p-2">Hover Me</button>
    ```
*   **`focus:`:** Applies when the element receives focus (e.g., via keyboard navigation or clicking on an input). Crucial for accessibility.
    ```html
    <input type="text" class="border border-gray-300 rounded p-2 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 focus:outline-none">
    ```
*   **`active:`:** Applies when the element is being actively pressed (e.g., mouse button held down on a button).
    ```html
    <button class="bg-green-500 active:bg-green-800 text-white p-2">Press Me</button>
    ```
*   **`disabled:`:** Applies when the element has the `disabled` attribute. Useful for styling disabled form elements or buttons.
    ```html
    <button class="bg-gray-400 text-gray-700 p-2 cursor-not-allowed" disabled>Disabled</button>
    <button class="bg-blue-500 text-white p-2 disabled:bg-gray-400 disabled:cursor-not-allowed">Maybe Disabled</button>
    ```
*   **`focus-within:`:** Applies when the element *or any of its descendants* has focus. Useful for highlighting form groups.
    ```html
    <div class="border p-4 focus-within:border-blue-500 focus-within:shadow-md">
      <label>Name:</label>
      <input type="text" class="border ml-2 focus:outline-none">
    </div>
    ```
*   **`focus-visible:`:** Applies only when the element receives focus via keyboard navigation (not mouse click). Helps create less intrusive focus styles for mouse users while maintaining keyboard accessibility.
    ```html
    <button class="p-2 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-400">Focus Visible</button>
    ```
*   **`visited:`:** Applies to visited `<a>` links.

## Dark Mode (`dark:`)

*   Applies styles only when dark mode is active.
*   Requires `darkMode: 'class'` (recommended) or `darkMode: 'media'` to be set in `tailwind.config.js`.
*   If using `'class'`, you need to toggle a `dark` class on a parent element (usually `<html>` or `<body>`), often managed by a library like `next-themes`. (See `tailwind-dark-mode.md`).

```html
<div class="bg-white dark:bg-gray-900 text-black dark:text-white p-4">
  This element changes background and text color in dark mode.
</div>
```

## Responsive + State Variants

Combine responsive prefixes and state variants. State variants generally come first.

```html
<a href="#" class="text-blue-600 hover:text-blue-800 md:text-lg md:hover:underline dark:text-blue-400 dark:hover:text-blue-300">
  Responsive & State Link
</a>
```
*   Base: Blue 600
*   Hover (all sizes): Blue 800
*   Medium screens and up (`md:`): Text size large (`text-lg`)
*   Medium screens and up + Hover (`md:hover:`): Underlined (`underline`)
*   Dark mode (`dark:`): Blue 400
*   Dark mode + Hover (`dark:hover:`): Blue 300

## Other Variants (Examples)

*   **Group States (`group-hover:`, `group-focus:`):** Style an element based on the state of a parent element marked with the `group` class.
    ```html
    <a href="#" class="group block border p-4 hover:bg-gray-100">
      <h3 class="font-bold group-hover:text-blue-600">Title</h3>
      <p class="text-sm text-gray-500 group-hover:text-gray-700">Description</p>
    </a>
    ```
*   **Peer States (`peer-focus:`, `peer-checked:`):** Style an element based on the state of a *sibling* element marked with the `peer` class. Useful for custom form controls.
    ```html
    <label class="flex items-center space-x-2">
      <input type="checkbox" class="peer sr-only"> <!-- Hidden checkbox is the peer -->
      <span class="w-4 h-4 border rounded peer-checked:bg-blue-500"></span> <!-- Custom box styled by peer state -->
      <span>Check me</span>
    </label>
    ```
*   **Positional (`first:`, `last:`, `odd:`, `even:`):** Style elements based on their position within a list or group.
    ```html
    <ul>
      <li class="p-2 border-b first:border-t odd:bg-gray-50">Item 1</li>
      <li class="p-2 border-b odd:bg-gray-50">Item 2</li>
      <li class="p-2 border-b odd:bg-gray-50">Item 3</li>
    </ul>
    ```
*   **Form States (`required:`, `invalid:`, `valid:`, `placeholder-shown:`):** Style form elements based on their validation or placeholder state.

Variants are essential for creating dynamic and interactive interfaces with Tailwind, allowing styles to change based on user interaction, screen size, and other conditions.

*(Refer to the official Tailwind CSS documentation on Hover, Focus, & Other States.)*