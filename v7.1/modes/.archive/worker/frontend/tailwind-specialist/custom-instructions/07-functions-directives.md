# Tailwind CSS: Functions & Directives (`@tailwind`, `@layer`, `@apply`, `theme()`)

Using Tailwind's directives and functions in your CSS for advanced customization and organization.

## Core Concept: Integrating with CSS

While Tailwind promotes a utility-first approach, it provides directives and functions to use within your regular CSS files (`.css`, `.scss`, `.less`, etc.) for specific scenarios like setting up base styles, organizing custom styles, or accessing theme values.

**Key Directives & Functions:**

*   **`@tailwind base;`**
    *   Injects Tailwind's base styles (like Preflight, a reset based on modern-normalize) and any base styles registered by plugins.
    *   **Placement:** Typically placed at the top of your main CSS file.
*   **`@tailwind components;`**
    *   Injects Tailwind's component classes (pre-defined utility combinations, mostly used by plugins like forms/typography) and any component classes registered by plugins.
*   **`@tailwind utilities;`**
    *   Injects all of Tailwind's core utility classes. Variants (like `hover:`, `md:`) are automatically generated based on your configuration.
*   **`@layer base | components | utilities { ... }`:**
    *   Allows you to register your own custom styles within one of Tailwind's "layers".
    *   **Purpose:** Controls the order in which styles appear in the final CSS output, ensuring utilities override base styles, and custom component styles can be overridden by utilities if needed. Helps manage CSS specificity and ensures custom styles are correctly processed by Tailwind (e.g., for purging).
    *   Use `@layer base` for element selectors (like `h1`, `body`), `@layer components` for custom component classes (like `.btn`), and `@layer utilities` for new utility-like classes.
*   **`@apply utility1 utility2 ...;`:**
    *   **Purpose:** Apply the styles of existing Tailwind utility classes within your custom CSS rules (inside an `@layer` directive).
    *   **Use Case:** Primarily used for extracting *highly repeated* utility patterns into reusable CSS classes (component abstraction) or styling elements you don't directly control (e.g., third-party library components, markdown output).
    *   **Caution:** Overuse of `@apply` can negate the benefits of utility-first (reintroduces naming, harder to see styles in markup, potential for specificity issues). **Use sparingly.** Prefer abstracting components in your template language (React, Vue, Svelte components) over creating many custom CSS classes with `@apply`.
*   **`theme('key', 'defaultValue?')`:**
    *   **Purpose:** Access values from your `tailwind.config.js` theme directly within your CSS.
    *   **Syntax:** `theme('section.key.subkey')`, e.g., `theme('colors.blue.500')`, `theme('spacing.4')`, `theme('screens.lg')`.
    *   **Use Case:** Applying theme values in custom CSS properties, `calc()` functions, or within `@apply` directives where a dynamic theme value is needed.

## Implementation Examples

**1. Basic CSS Setup:**

```css
/* src/styles/globals.css */

/* Inject Tailwind's base, components, and utilities layers */
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Optional: Add custom base styles using @layer */
@layer base {
  h1 {
    @apply text-2xl font-bold mb-4; /* Example using @apply for base heading style */
    color: theme('colors.brand-primary', #FF6347); /* Example using theme() with fallback */
  }
  body {
    font-family: theme('fontFamily.sans'); /* Apply default sans font from config */
    @apply antialiased; /* Apply utility via @apply */
  }
  button, input {
    @apply focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500; /* Consistent focus */
  }
}

/* Optional: Add custom component styles using @layer */
@layer components {
  .btn-custom {
    @apply py-2 px-4 bg-brand-primary text-white rounded hover:opacity-90 focus:ring-2;
    /* Mix utilities with custom CSS if needed */
    transition: background-color 0.15s ease-in-out;
  }
  .card {
    @apply bg-white rounded-lg shadow-md p-4;
  }
}

/* Optional: Add custom utility styles using @layer */
@layer utilities {
  .text-shadow {
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
  }
  .content-auto {
    content-visibility: auto;
  }
}
```

**2. Using `@apply` (Sparingly):**

```css
/* Example: Extracting button styles */
@layer components {
  .button-base { /* Define base button styles */
    @apply inline-block font-medium text-center px-4 py-2 rounded border focus:outline-none focus:ring-2 focus:ring-offset-2 transition-colors duration-150;
  }
  .button-primary {
    @apply button-base bg-blue-600 text-white border-transparent hover:bg-blue-700 focus:ring-blue-500;
  }
  .button-secondary {
     @apply button-base bg-white text-gray-700 border-gray-300 hover:bg-gray-50 focus:ring-indigo-500;
  }
}
```
*Instead of the above, often it's better to create a `<Button variant="primary">` component in your framework.*

**3. Using `theme()`:**

```css
.custom-gradient {
  background-image: linear-gradient(to right, theme('colors.purple.500'), theme('colors.pink.500'));
}

.element-with-dynamic-padding {
  padding: calc(theme('spacing.4') + 1px);
}
```

## Important Notes

*   **Purging:** Ensure your `tailwind.config.js` `content` paths correctly include CSS/SCSS files where you use `@apply` within `@layer`, otherwise those styles might be purged in production.
*   **IntelliSense:** Tailwind IntelliSense extensions might not fully understand complex `@apply` usage or custom components defined with it.
*   **Specificity:** Styles defined using `@apply` within a layer follow standard CSS cascade rules. The layer order (`base` < `components` < `utilities`) helps manage this.

Use `@tailwind` directives to include Tailwind's core styles. Use `@layer` to organize custom CSS and manage specificity relative to Tailwind's layers. Use `theme()` to access your design tokens within CSS. Use `@apply` cautiously, preferring component abstraction in your templates when possible.

*(Refer to the official Tailwind CSS documentation on Functions & Directives.)*