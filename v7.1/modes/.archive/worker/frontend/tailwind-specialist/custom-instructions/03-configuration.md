# Tailwind CSS: Configuration (`tailwind.config.js`)

Customizing Tailwind's theme, content scanning, and plugins via `tailwind.config.js`.

## 1. Core Concept: `tailwind.config.js`

This file is the central hub for customizing your Tailwind CSS setup. It allows you to define your project's design system (theme), control which files are scanned for classes (content), and extend functionality with plugins.

**Key Sections:**

*   **`content`:** (Required) Specifies the files Tailwind should scan to find utility classes being used. Crucial for production purging.
*   **`theme`:** The main section for defining your design system (colors, spacing, fonts, breakpoints, etc.).
*   **`theme.extend`:** Use this section to **add** new values or **extend** existing Tailwind defaults without completely overwriting them (Recommended).
*   **`plugins`:** Add official or third-party plugins.
*   **`darkMode`:** Configure dark mode strategy (`'class'` or `'media'`).
*   **`presets`:** Inherit configurations from base presets.

## 2. Customizing the Theme (`theme` and `theme.extend`)

Tailor Tailwind's default design tokens to match your project's requirements.

**Extending the Theme (Recommended):**

Place keys under `theme.extend` to **add** your values to the defaults or **override specific default values** while keeping the rest.

```javascript
// tailwind.config.js
const colors = require('tailwindcss/colors') // Optional: Import default colors

module.exports = {
  content: ["./src/**/*.{html,js,jsx,ts,tsx}"],
  theme: {
    extend: {
      // Add custom values or override specific defaults
      colors: {
        'brand-primary': '#FF6347', // Add a custom brand color
        'brand-secondary': '#4682B4',
        gray: colors.neutral, // Example: Use 'neutral' palette as 'gray'
      },
      spacing: {
        '128': '32rem', // Add a large spacing unit
        '14': '3.5rem', // Add an intermediate spacing unit
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'], // Change default sans-serif font
      },
      borderRadius: {
        '4xl': '2rem', // Add a larger border radius
      },
      screens: {
        '3xl': '1920px', // Add a larger breakpoint
      }
      // ... extend other theme properties
    },
    // You can still have keys directly under theme if you WANT to fully replace
    // screens: { tablet: '768px', desktop: '1280px' } // This would replace ALL default screens
  },
  plugins: [],
}
```

**Accessing Theme Values in CSS:**

Use the `theme()` function in your CSS files (within `@layer` or `@apply`) to access theme values.

```css
.custom-button {
  background-color: theme('colors.brand-primary');
  padding: theme('spacing.3') theme('spacing.6');
  font-family: theme('fontFamily.sans');
}
```

## 3. Configuring Content Scanning (`content`)

The `content` array tells Tailwind where to look for class names to ensure unused styles are removed (purged) in production builds.

**Key Considerations:**

*   **Be Specific:** Include glob patterns for **all** file types where you use Tailwind classes (HTML, JS, JSX, TSX, Svelte, Vue, PHP, Blade, etc.).
*   **Include Full Class Names:** Tailwind scans for *complete, unbroken* class names. Avoid constructing class names dynamically using string concatenation in ways Tailwind cannot detect statically.
    *   **Bad:** `text-{{ color }}-500`
    *   **Good:** `{{ error ? 'text-red-500' : 'text-green-500' }}`
    *   **Good (Mapping):** Use objects to map conditions to full class names.
*   **Framework Presets:** Frameworks might configure basic paths, but explicitly defining them is safer.

**Example `content` Array:**

```javascript
// tailwind.config.js
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/**/*.html",
    "./src/**/*.svelte",
    // Add paths for any other relevant file types
  ],
  // ... theme, plugins
}
```

**Verifying Purging:**

*   Run your production build (`npm run build`).
*   Inspect the generated CSS file size; it should be significantly smaller.
*   Test your application to ensure no necessary styles were accidentally removed. If styles are missing, check your `content` paths and ensure you're not using undetectable dynamic class names.

## 4. Using Plugins (`plugins`)

Extend Tailwind's capabilities with official or custom JavaScript plugins.

**Official Plugins (Examples):**

*   `@tailwindcss/typography`: Adds `prose` class for styling long-form content.
*   `@tailwindcss/forms`: Provides resets and base styles for form elements.
*   `@tailwindcss/aspect-ratio`: Adds aspect ratio utilities.
*   `@tailwindcss/container-queries`: Adds container query utilities.

**Implementation:**

1.  **Install:** `npm install -D @tailwindcss/forms @tailwindcss/typography`
2.  **Add to `tailwind.config.js`:**
    ```javascript
    // tailwind.config.js
    module.exports = {
      // ... content, theme
      plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        // Add other plugins here
      ],
    }
    ```
3.  **Use Plugin Features:** Refer to the plugin's documentation for usage (e.g., `<article class="prose">`, styling `<input>`, `<textarea>`).

**Custom Plugins:**

You can write your own plugins using helper functions like `addUtilities`, `addComponents`, `addVariant`.

```javascript
// tailwind.config.js
const plugin = require('tailwindcss/plugin')

module.exports = {
  // ... content, theme
  plugins: [
    plugin(function({ addUtilities, addVariant }) {
      addUtilities({
        '.text-shadow': { textShadow: '1px 1px 2px rgba(0,0,0,0.5)' },
      })
      addVariant('hocus', ['&:hover', '&:focus']) // Adds hocus: variant
    })
  ],
}
```

Proper configuration of `theme`, `content`, and `plugins` in `tailwind.config.js` is essential for creating a consistent design system, optimizing performance, and extending Tailwind's functionality.