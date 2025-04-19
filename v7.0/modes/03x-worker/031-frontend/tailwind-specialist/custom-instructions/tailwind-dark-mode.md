# Tailwind CSS: Dark Mode

Implementing dark mode support using Tailwind's `dark:` variant.

## Core Concept: Conditional Dark Styles

Tailwind provides a `dark:` variant that allows you to apply utility classes conditionally when dark mode is active. This makes it easy to adapt your design for users who prefer a dark color scheme.

**Two Strategies:**

1.  **`class` Strategy (Recommended):**
    *   **How it works:** You manually toggle a `dark` class on a parent element (usually `<html>` or `<body>`). Tailwind utilities prefixed with `dark:` (e.g., `dark:bg-gray-900`) will only apply when this `dark` class is present.
    *   **Setup:** Set `darkMode: 'class'` in `tailwind.config.js`.
    *   **Control:** Gives you full control over when dark mode is enabled (e.g., via user toggle, system preference detection). Often used with libraries like `next-themes`.
2.  **`media` Strategy:**
    *   **How it works:** Uses the CSS `prefers-color-scheme: dark` media query. Utilities prefixed with `dark:` automatically apply if the user's operating system is set to dark mode.
    *   **Setup:** Set `darkMode: 'media'` in `tailwind.config.js`.
    *   **Control:** Simpler setup, but relies entirely on the user's OS setting; you cannot provide a manual toggle easily.

## Implementation (`class` Strategy - Recommended)

**1. Configure `tailwind.config.js`:**

Set the `darkMode` option to `'class'`.

```javascript
// tailwind.config.js
module.exports = {
  darkMode: 'class', // Enable the class strategy
  content: [
    // ... your content paths
  ],
  theme: {
    extend: {
      // ... your theme extensions
    },
  },
  plugins: [],
}
```

**2. Apply Dark Mode Utilities:**

Prefix utilities with `dark:` to specify the styles that should apply when the `dark` class is active on a parent element.

```html
<body class=""> <!-- Light mode by default -->
  <div class="p-4 bg-white text-gray-900 dark:bg-gray-800 dark:text-gray-100">
    <h1 class="text-xl font-bold text-blue-600 dark:text-blue-400">Dark Mode Example</h1>
    <p class="mt-2">This text and background will change in dark mode.</p>
    <button class="mt-4 px-4 py-2 bg-gray-200 text-black rounded hover:bg-gray-300 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600">
      Toggle Dark Mode
    </button>
  </div>
</body>

<!-- Later, if dark mode is enabled via JS: -->
<!-- <body class="dark"> ... </body> -->
```

**3. Toggle the `dark` Class:**

You need JavaScript to add or remove the `dark` class from the `<html>` or `<body>` element based on user preference or system settings.

*   **Manual Toggle:** Add an event listener to a button that toggles the class and potentially saves the preference in `localStorage`.
*   **Using `next-themes` (Recommended for React/Next.js):** This library handles system preference detection, `localStorage` persistence, and applying the class automatically. (See `shadcn-theming.md` for an example setup with `next-themes`).

**Example Manual Toggle (Simplified):**

```javascript
// Simple dark mode toggle logic
const toggleBtn = document.getElementById('dark-mode-toggle');
const htmlEl = document.documentElement; // Target <html> element

// Check localStorage on load
if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  htmlEl.classList.add('dark');
} else {
  htmlEl.classList.remove('dark');
}

toggleBtn.addEventListener('click', () => {
  if (htmlEl.classList.contains('dark')) {
    htmlEl.classList.remove('dark');
    localStorage.theme = 'light';
  } else {
    htmlEl.classList.add('dark');
    localStorage.theme = 'dark';
  }
});
```

The `dark:` variant, combined with the `class` strategy and a mechanism to toggle the `dark` class, provides a flexible and robust way to implement dark mode in Tailwind CSS projects.

*(Refer to the official Tailwind CSS documentation on Dark Mode.)*