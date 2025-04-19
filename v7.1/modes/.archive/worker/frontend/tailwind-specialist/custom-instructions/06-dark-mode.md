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
/** @type {import('tailwindcss').Config} */
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
<!-- Or more commonly: -->
<!-- <html class="dark"> ... </html> -->
```

**3. Toggle the `dark` Class:**

You need JavaScript to add or remove the `dark` class from the `<html>` or `<body>` element based on user preference or system settings.

*   **Manual Toggle:** Add an event listener to a button that toggles the class and potentially saves the preference in `localStorage`.
*   **Using `next-themes` (Recommended for React/Next.js):** This library handles system preference detection, `localStorage` persistence, and applying the class automatically.

**Example Manual Toggle (Simplified):**

```javascript
// Simple dark mode toggle logic - place in <head> or early script
const toggleBtn = document.getElementById('dark-mode-toggle'); // Assuming you have a button with this ID
const htmlEl = document.documentElement; // Target <html> element

// Function to apply theme based on preference
function applyTheme(theme) {
  if (theme === 'dark') {
    htmlEl.classList.add('dark');
  } else {
    htmlEl.classList.remove('dark');
  }
}

// Check localStorage and system preference on load
const savedTheme = localStorage.theme;
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
  applyTheme('dark');
} else {
  applyTheme('light'); // Default to light
}

// Add event listener for the toggle button (if it exists)
if (toggleBtn) {
  toggleBtn.addEventListener('click', () => {
    const isDark = htmlEl.classList.contains('dark');
    const newTheme = isDark ? 'light' : 'dark';
    applyTheme(newTheme);
    localStorage.theme = newTheme; // Save preference
  });
}
```

**Using CSS Variables:**

If using CSS variables for theming (common with libraries like Shadcn UI), define the dark mode variable values within a `.dark { ... }` block in your global CSS. Tailwind's `dark:` variant works seamlessly with this.

```css
/* globals.css */
:root {
  --background: 0 0% 100%; /* Light background */
  --foreground: 222.2 84% 4.9%; /* Light text */
  /* ... other light theme variables ... */
}

.dark {
  --background: 222.2 84% 4.9%; /* Dark background */
  --foreground: 210 40% 98%; /* Dark text */
  /* ... other dark theme variables ... */
}

body {
  background-color: hsl(var(--background));
  color: hsl(var(--foreground));
}
```

The `dark:` variant, combined with the `class` strategy and a mechanism to toggle the `dark` class, provides a flexible and robust way to implement dark mode in Tailwind CSS projects.

*(Refer to the official Tailwind CSS documentation on Dark Mode.)*