# Tailwind CSS: Responsive Design

Applying styles conditionally at different screen sizes using Tailwind's breakpoint prefixes.

## Core Concept: Mobile-First Responsive Utilities

Tailwind uses a **mobile-first** breakpoint system. Utility classes without a breakpoint prefix (like `p-4`, `text-center`) apply to all screen sizes, while prefixed utilities (like `md:p-8`, `lg:text-left`) apply only at that specific breakpoint *and above*.

**Default Breakpoints (Configurable in `tailwind.config.js`):**

*   `sm`: 640px
*   `md`: 768px
*   `lg`: 1024px
*   `xl`: 1280px
*   `2xl`: 1536px

**Syntax:** `{breakpoint}:{utility}` (e.g., `md:text-lg`)

## Applying Responsive Prefixes

Prefix any standard Tailwind utility class with a breakpoint name followed by a colon (`:`) to make it apply only at that screen size and larger.

```html
<!-- Example: Responsive Card Layout -->
<div class="p-4 bg-white rounded shadow"> <!-- Base styles (mobile) -->
  <!-- Mobile: Stacked layout -->
  <img class="w-full h-48 object-cover mb-4 md:hidden" src="/path/to/image.jpg" alt="Feature image"> <!-- Image only on mobile -->

  <!-- Tablet and up: Flex layout -->
  <div class="md:flex md:items-start md:space-x-4">
    <img class="hidden md:block md:w-32 md:h-32 md:rounded object-cover" src="/path/to/image.jpg" alt="Feature image"> <!-- Image only on tablet+ -->
    <div>
      <!-- Text size changes at 'lg' breakpoint -->
      <h2 class="text-lg font-bold mb-1 lg:text-xl">Responsive Title</h2>
      <!-- Text alignment changes at 'md' breakpoint -->
      <p class="text-gray-600 text-sm text-center md:text-left lg:text-base">
        This description is centered on mobile but left-aligned on medium screens and larger. The text size also increases on large screens.
      </p>
      <!-- Button hidden on mobile, shown on tablet+ -->
      <button class="hidden md:inline-block mt-4 bg-blue-500 hover:bg-blue-700 text-white py-1 px-3 rounded text-sm">
        Learn More
      </button>
    </div>
  </div>
   <!-- Button shown only on mobile -->
  <button class="block w-full mt-4 md:hidden bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded">
    Learn More (Mobile)
  </button>
</div>

<!-- Example: Responsive Grid -->
<!-- Mobile: 1 column, Tablet: 2 columns, Desktop: 4 columns -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 p-4">
  <div class="bg-gray-200 p-4 rounded">Item 1</div>
  <div class="bg-gray-200 p-4 rounded">Item 2</div>
  <div class="bg-gray-200 p-4 rounded">Item 3</div>
  <div class="bg-gray-200 p-4 rounded">Item 4</div>
</div>
```

## Combining Prefixes

You can combine responsive prefixes with state variants (like `hover:`, `focus:`, `dark:`). The state variant comes *before* the responsive prefix.

*   `hover:text-blue-500`: Apply blue text on hover (all screen sizes).
*   `md:hover:text-red-500`: Apply red text on hover, but *only* on medium screens and larger.
*   `dark:md:bg-gray-800`: Apply dark background on medium screens and larger, *only* when dark mode is active.

```html
<button class="bg-blue-500 text-white p-2 rounded
               hover:bg-blue-700
               md:bg-green-500 md:hover:bg-green-700
               dark:bg-indigo-600 dark:hover:bg-indigo-800
               dark:md:bg-purple-600 dark:md:hover:bg-purple-800">
  Responsive & State Button
</button>
```

## Customizing Breakpoints

You can customize, add, or remove breakpoints in your `tailwind.config.js` file under the `theme.screens` or `theme.extend.screens` key.

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    extend: {
      screens: {
        '3xl': '1920px', // Add a larger breakpoint
      },
    },
  },
  plugins: [],
}
```

Tailwind's mobile-first responsive prefixes provide a powerful and intuitive way to build UIs that adapt seamlessly to different screen sizes. Apply base styles first, then layer on overrides for larger screens using the `sm:`, `md:`, `lg:`, etc., prefixes.

*(Refer to the official Tailwind CSS documentation on Responsive Design.)*