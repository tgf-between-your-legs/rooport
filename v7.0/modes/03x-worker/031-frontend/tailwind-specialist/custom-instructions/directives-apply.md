# Tailwind CSS Directives (`@tailwind`, `@layer`, `@apply`)

Using Tailwind directives in your CSS files.

## 1. `@tailwind`

*   **Purpose:** Injects Tailwind's `base`, `components`, `utilities`, and `variants` styles into your CSS. This is the main entry point for Tailwind's generated styles.
*   **Usage:** Typically placed at the top of your main CSS file (e.g., `globals.css`, `index.css`).
    ```css
    /* src/globals.css */
    @tailwind base;     /* Injects Preflight base styles & browser resets */
    @tailwind components; /* Injects component classes (used by plugins) */
    @tailwind utilities;  /* Injects all core utility classes */

    /* Optional: Inject variants separately if needed, less common */
    /* @tailwind variants; */

    /* Your custom base styles or component styles can go here */
    @layer base {
      h1 {
        @apply text-2xl font-bold mb-4; /* Example using @apply */
      }
    }
    ```

## 2. `@layer`

*   **Purpose:** Tells Tailwind which "bucket" or layer (`base`, `components`, `utilities`) your custom styles belong to. This helps control the order of styles in the final CSS output, ensuring utilities can override component styles, and component styles can override base styles. It also helps Tailwind's purging process identify custom styles correctly.
*   **Usage:** Wrap your custom CSS rules within `@layer base { ... }`, `@layer components { ... }`, or `@layer utilities { ... }`.
    ```css
    /* src/custom.css (or globals.css) */
    @tailwind base;
    @tailwind components;
    @tailwind utilities;

    @layer base {
      /* Custom base styles */
      body {
        @apply font-sans antialiased;
      }
      button, input {
        @apply focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500;
      }
    }

    @layer components {
      /* Custom component classes */
      .card {
        @apply bg-white rounded-lg shadow-md p-4;
      }
      .btn-primary {
        @apply py-2 px-4 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50;
      }
    }

    @layer utilities {
      /* Custom utility classes (less common, prefer plugins) */
      .text-shadow {
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
      }
    }
    ```

## 3. `@apply`

*   **Purpose:** Allows you to inline existing Tailwind utility classes directly into your custom CSS rules within `@layer`.
*   **Usage:** Use `@apply` followed by the utility classes you want to include.
    ```css
    @layer components {
      .btn {
        @apply font-bold py-2 px-4 rounded;
      }
      .btn-blue {
        @apply bg-blue-500 hover:bg-blue-700 text-white;
        /* You can mix @apply with regular CSS */
        transition-property: background-color;
        transition-duration: 150ms;
      }
    }
    ```
*   **Best Practice - Use Sparingly:**
    *   **Avoid Overuse:** The primary benefit of Tailwind is using utility classes directly in your markup. Overusing `@apply` can recreate the problems of traditional CSS (large CSS files, difficulty finding styles, unused style bloat if not purged correctly).
    *   **When to Use:**
        *   Small, reusable component classes (like `.btn` above) where abstracting common utilities makes sense.
        *   Applying styles to elements you don't control directly (e.g., styling markdown output via `@tailwindcss/typography`'s `prose` class overrides, or styling third-party library components).
        *   Applying default styles within `@layer base`.
    *   **Alternative:** For reusable UI elements, strongly consider creating actual components (React, Vue, Svelte, Blade, etc.) and applying utilities directly to the elements within those components. This is often more maintainable than creating many custom CSS classes with `@apply`.

## Important Notes

*   **Purging:** Ensure your `tailwind.config.js` `content` paths correctly include files where you use `@apply` within `@layer`, otherwise those styles might be purged in production.
*   **IntelliSense:** Tailwind IntelliSense extensions might not fully understand complex `@apply` usage or custom components defined with it.
*   **Specificity:** Styles defined using `@apply` within a layer follow standard CSS cascade rules. Utilities applied directly in HTML generally have higher specificity due to being applied via attribute selectors or similar mechanisms by Tailwind's engine, but the layer order (`base` < `components` < `utilities`) helps manage this.

*(Refer to the official Tailwind CSS documentation on Functions & Directives: https://tailwindcss.com/docs/functions-and-directives)*