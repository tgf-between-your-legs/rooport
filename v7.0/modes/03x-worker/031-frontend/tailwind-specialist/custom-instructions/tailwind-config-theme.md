# Tailwind CSS: Customizing the Theme (`tailwind.config.js`)

Modifying and extending Tailwind's default design system via `tailwind.config.js`.

## Core Concept: `tailwind.config.js`

This file is the heart of your Tailwind CSS customization. It allows you to define your project's specific design tokens (colors, spacing, fonts, breakpoints, etc.), overriding or extending Tailwind's defaults.

**Key Sections:**

*   **`content`:** (Required) Specifies the files Tailwind should scan to find utility classes being used. Crucial for production purging. (See `tailwind-config-content-purging.md`).
*   **`theme`:** The main section for defining your design system.
    *   **`theme.screens`:** Define responsive breakpoints.
    *   **`theme.colors`:** Define your color palette.
    *   **`theme.spacing`:** Define spacing units (for padding, margin, width, height).
    *   **`theme.fontFamily`:** Define font families.
    *   **`theme.fontSize`:** Define font sizes.
    *   **`theme.fontWeight`:** Define font weights.
    *   ...and many other keys corresponding to CSS properties (borderRadius, boxShadow, etc.).
*   **`theme.extend`:** Use this section to **add** new values or **extend** existing Tailwind defaults without completely overwriting them. This is generally the preferred way to customize.
*   **`plugins`:** Add official or third-party plugins. (See `tailwind-config-plugins.md`).
*   **`presets`:** Inherit configurations from base presets (less common for typical customization).
*   **`darkMode`:** Configure dark mode strategy (`'class'` or `'media'`). (See `tailwind-dark-mode.md`).

## Customizing the Theme

**1. Overriding Default Theme Values:**

Placing keys directly under `theme` **replaces** Tailwind's default values for that key entirely.

```javascript
// tailwind.config.js
module.exports = {
  content: ["./src/**/*.{html,js,jsx,ts,tsx}"],
  theme: {
    // This COMPLETELY REPLACES Tailwind's default screens
    screens: {
      tablet: '768px',
      desktop: '1280px',
    },
    // This COMPLETELY REPLACES Tailwind's default colors
    colors: {
      'blue': '#1fb6ff',
      'purple': '#7e5bef',
      'white': '#ffffff',
      // No default gray, red, etc. will be available unless redefined here
    },
    // ... other full overrides
  },
  plugins: [],
}
```
*Use full overrides with caution, as you lose all the default Tailwind values for that key.*

**2. Extending the Default Theme (Recommended):**

Placing keys under `theme.extend` **adds** your values to the defaults or **overrides specific default values** while keeping the rest.

```javascript
// tailwind.config.js
const colors = require('tailwindcss/colors') // Optional: Import default colors for reference

module.exports = {
  content: ["./src/**/*.{html,js,jsx,ts,tsx}"],
  theme: {
    extend: {
      // Add custom values or override specific defaults
      colors: {
        'brand-primary': '#FF6347', // Add a custom brand color
        'brand-secondary': '#4682B4',
        gray: colors.neutral, // Example: Use 'neutral' palette as 'gray'
        blue: { // Override specific shades of blue
          '500': '#3B82F6', // Keep default blue-500
          '700': '#1D4ED8', // Override default blue-700
        }
      },
      spacing: {
        '128': '32rem', // Add a large spacing unit
        '14': '3.5rem', // Add an intermediate spacing unit
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'], // Change default sans-serif font
        serif: ['Merriweather', 'serif'], // Add a serif font family
      },
      fontSize: {
        'tiny': '.625rem', // Add a custom font size
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
    // screens: { ... } // This would still replace default screens
  },
  plugins: [],
}
```

**Accessing Theme Values:**

*   **In Utilities:** Use the defined keys in your utility classes (e.g., `bg-brand-primary`, `text-gray-600`, `p-14`, `font-serif`, `rounded-4xl`, `3xl:p-10`).
*   **In CSS (`theme()`):** Use the `theme()` function in your CSS files (if using `@apply` or custom CSS) to access theme values.
    ```css
    .custom-button {
      background-color: theme('colors.brand-primary');
      padding: theme('spacing.3') theme('spacing.6');
      font-family: theme('fontFamily.sans');
    }
    ```

Customizing `tailwind.config.js` allows you to tailor Tailwind's design system to your project's specific needs. Prefer using `theme.extend` to add or modify specific values while retaining the comprehensive defaults provided by Tailwind.

*(Refer to the official Tailwind CSS documentation on Theme Configuration.)*