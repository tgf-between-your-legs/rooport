# Tailwind CSS: Dark Mode

Implementing dark mode support using Tailwind's `dark:` variant.

## Core Concept

Tailwind provides a `dark:` variant that allows you to apply different utility classes when dark mode is active. You can control how dark mode is detected (based on OS preference or a manually toggled class).

## Configuration (`tailwind.config.js`)

*   **`darkMode` Option:** Controls the dark mode strategy.
    *   **`'media'` (Default):** Uses the `prefers-color-scheme: dark` CSS media query. Dark mode is enabled based on the user's operating system setting. No manual toggle is possible with this strategy alone.
    *   **`'class'`:** Enables dark mode whenever a `dark` class is present on an ancestor element (usually `<html>` or `<body>`). This allows you to manually toggle dark mode using JavaScript.
    *   **`'selector'`:** Enables dark mode whenever a specific selector (e.g., `[data-theme="dark"]`) is present on an ancestor element. Similar to `'class'` but uses a data attribute.

    ```javascript
    // tailwind.config.js
    module.exports = {
      // Use 'class' strategy for manual toggling
      darkMode: 'class',
      content: [
        // ... your content paths ...
      ],
      theme: {
        extend: {},
      },
      plugins: [],
    }
    ```

## Applying Dark Mode Styles

*   Prefix utility classes with `dark:` to apply them only when dark mode is active.
    ```html
    <div class="bg-white dark:bg-gray-900">
      <h1 class="text-gray-900 dark:text-white">Light/Dark Title</h1>
      <p class="text-gray-600 dark:text-gray-300">
        This text changes color in dark mode.
      </p>
      <button class="bg-blue-500 hover:bg-blue-600 dark:bg-blue-700 dark:hover:bg-blue-800 text-white font-bold py-2 px-4 rounded">
        Button
      </button>
    </div>
    ```

## Toggling Dark Mode (`'class'` Strategy)

If using `darkMode: 'class'`, you need JavaScript to add or remove the `dark` class from the `<html>` element.

**Example using `localStorage` and simple JS:**

```html
<!-- Add this script preferably in the <head> to avoid FOUC -->
<script>
  // On page load or when changing themes, best to add inline in `head` to avoid FOUC
  if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }

  // Optional: Function to toggle theme
  function toggleTheme() {
    const isDark = document.documentElement.classList.toggle('dark');
    localStorage.theme = isDark ? 'dark' : 'light';
  }
</script>

<!-- Example Toggle Button -->
<button onclick="toggleTheme()">Toggle Theme</button>
```

**Example using `next-themes` (Recommended for React/Next.js):**

1.  **Install:** `npm install next-themes`
2.  **Create Theme Provider:**
    ```jsx
    // app/providers.tsx (or similar)
    "use client";
    import { ThemeProvider as NextThemesProvider } from "next-themes";
    import { type ThemeProviderProps } from "next-themes/dist/types";

    export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
      return <NextThemesProvider {...props}>{children}</NextThemesProvider>;
    }
    ```
3.  **Wrap Root Layout:**
    ```jsx
    // app/layout.tsx
    import { ThemeProvider } from "@/app/providers"; // Adjust path

    export default function RootLayout({ children }) {
      return (
        <html lang="en" suppressHydrationWarning> {/* suppressHydrationWarning needed */}
          <body>
            <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
              {children}
            </ThemeProvider>
          </body>
        </html>
      );
    }
    ```
4.  **Create Toggle Component:**
    ```jsx
    // components/ModeToggle.tsx
    "use client";
    import { useTheme } from "next-themes";
    import { Button } from "@/components/ui/button"; // Assuming Shadcn UI Button

    export function ModeToggle() {
      const { theme, setTheme } = useTheme();

      return (
        <Button
          variant="outline"
          size="icon"
          onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
        >
          {/* Add Sun/Moon Icons here */}
          <span className="sr-only">Toggle theme</span>
        </Button>
      );
    }
    ```

## CSS Variables & Dark Mode

*   If using CSS variables for theming (like with Shadcn UI), define the dark mode values within a `.dark { ... }` block in your global CSS file. Tailwind's `dark:` variant will work correctly with these variables.

```css
/* globals.css */
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  /* ... other light theme variables ... */
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  /* ... other dark theme variables ... */
}
```

*(Refer to the official Tailwind CSS Dark Mode documentation: https://tailwindcss.com/docs/dark-mode)*