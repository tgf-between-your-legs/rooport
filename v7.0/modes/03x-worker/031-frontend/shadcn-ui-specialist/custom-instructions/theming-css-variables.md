# Shadcn UI: Theming with CSS Variables

Customizing the look and feel of Shadcn UI components using CSS variables and supporting light/dark modes.

## Core Concept

Shadcn UI theming relies heavily on **CSS variables** defined in your global CSS file (e.g., `globals.css` or `index.css`). These variables control colors (background, foreground, primary, secondary, destructive, etc.), border radius, and potentially other aspects. Tailwind CSS is configured in `tailwind.config.js` to use these variables.

## Initialization (`npx shadcn-ui@latest init`)

During initialization, the CLI asks for your preferred base color (e.g., Slate, Gray, Zinc, Neutral, Stone) and primary color. It then populates your global CSS file with HSL-based color variables for both light (`:root`) and dark (`.dark`) themes.

**Example `globals.css` (Snippet):**
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%; /* White */
    --foreground: 222.2 84% 4.9%; /* Dark Gray/Black */

    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;

    /* ... other base colors ... */

    --primary: 222.2 47.4% 11.2%; /* Example: Blue */
    --primary-foreground: 210 40% 98%; /* Light text for primary */

    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;

    /* ... destructive, accent, etc. ... */

    --radius: 0.5rem; /* Border radius variable */
  }

  .dark {
    --background: 222.2 84% 4.9%; /* Dark Gray/Black */
    --foreground: 210 40% 98%; /* Light Gray/White */

    --card: 222.2 84% 4.9%;
    --card-foreground: 210 40% 98%;

    /* ... other dark base colors ... */

    --primary: 210 40% 98%; /* Example: Light Blue */
    --primary-foreground: 222.2 47.4% 11.2%; /* Dark text for primary */

    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;

    /* ... dark destructive, accent, etc. ... */

    /* Radius usually stays the same */
  }
}

/* ... other base styles ... */
```

## Customizing the Theme

1.  **Modify CSS Variables:** The primary way to theme is by changing the HSL values in `:root` (light mode) and `.dark` (dark mode) within your `globals.css`.
    *   Find HSL values using color pickers or online tools.
    *   Adjust `--primary`, `--secondary`, `--accent`, `--destructive`, `--background`, `--foreground`, `--radius`, etc., to match your desired design.
2.  **Tailwind Configuration:** Ensure your `tailwind.config.js` correctly references these CSS variables using the `hsl(var(--variable-name))` syntax. The `init` command usually sets this up correctly.
    ```js
    // tailwind.config.js (snippet)
    extend: {
      colors: {
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        // ... other colors referencing CSS vars ...
      },
      borderRadius: {
        lg: "var(--radius)",
        // ...
      },
    }
    ```
3.  **Use Tailwind Utilities:** Apply theme colors and radius using Tailwind classes like `bg-primary`, `text-secondary-foreground`, `border-destructive`, `rounded-lg`. These utilities automatically pick up the values from your CSS variables via the Tailwind config.

## Dark Mode

*   **Setup:** Shadcn UI setup often includes `next-themes` or a similar library. Ensure you have a theme provider component that manages adding/removing the `.dark` class to the `<html>` element.
    ```tsx
    // Example using next-themes
    // app/providers.tsx (or similar)
    "use client";
    import { ThemeProvider as NextThemesProvider } from "next-themes";
    import { type ThemeProviderProps } from "next-themes/dist/types";

    export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
      return <NextThemesProvider {...props}>{children}</NextThemesProvider>;
    }

    // app/layout.tsx
    import { ThemeProvider } from "@/app/providers"; // Adjust path

    export default function RootLayout({ children }) {
      return (
        <html lang="en" suppressHydrationWarning> {/* suppressHydrationWarning often needed */}
          <body>
            <ThemeProvider
              attribute="class"
              defaultTheme="system"
              enableSystem
              disableTransitionOnChange
            >
              {children}
            </ThemeProvider>
          </body>
        </html>
      );
    }
    ```
*   **Toggling:** Create a `ModeToggle` component (often provided as an example in Shadcn docs) that uses the `useTheme` hook from `next-themes` to switch between 'light', 'dark', and 'system' modes.
*   **CSS Variables:** Define corresponding color variables within the `.dark { ... }` block in `globals.css`.

## Adding Custom Colors/Variables

1.  Define new CSS variables in `:root` and `.dark` in `globals.css`.
    ```css
    :root {
      --brand-purple: 259 94% 51%;
    }
    .dark {
      --brand-purple: 259 94% 65%;
    }
    ```
2.  Add the new color to your `tailwind.config.js`.
    ```js
    // tailwind.config.js
    extend: {
      colors: {
        brand: { // Define a new color name
          DEFAULT: "hsl(var(--brand-purple))",
          // Optionally define foreground if needed
          // foreground: "hsl(var(--brand-purple-foreground))",
        },
        // ... other colors
      },
    }
    ```
3.  Use the new color with Tailwind utilities: `bg-brand`, `text-brand`.

*(Refer to the official Shadcn UI Theming documentation: https://ui.shadcn.com/docs/theming)*