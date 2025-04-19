# 2. Theming (CSS Variables & Dark Mode)

Customizing the appearance and implementing dark mode for Shadcn UI components using CSS variables.

## Core Concept: CSS Variables

Shadcn UI's theming is primarily built upon **CSS Variables** defined in your global CSS file (e.g., `globals.css`). These variables control colors (background, foreground, primary, secondary, destructive, accent, etc.), border radius, and potentially other aspects.

*   **Initialization:** The `npx shadcn-ui@latest init` command sets up these variables based on your chosen base color and style.
*   **Tailwind Integration:** Tailwind utility classes (like `bg-background`, `text-primary`, `border`) are often configured in `tailwind.config.js` to use these CSS variables.
*   **Customization:** You can customize the theme by:
    *   Modifying the HSL values or hex codes of the CSS variables directly in `globals.css`.
    *   Adding new CSS variables for more granular control.
    *   Overriding variables for specific components or sections using inline styles or CSS selectors.

## Example `globals.css` (Simplified)

```css
/* Your global styles - e.g., app/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    /* Light Mode Variables (Example - values depend on init choices) */
    --background: 0 0% 100%; /* hsl(0, 0%, 100%) */
    --foreground: 222.2 84% 4.9%;

    --card: 0 0% 100%;
    --card-foreground: 222.2 84% 4.9%;

    --popover: 0 0% 100%;
    --popover-foreground: 222.2 84% 4.9%;

    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;

    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;

    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;

    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;

    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;

    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 222.2 84% 4.9%; /* Focus ring */

    --radius: 0.5rem; /* Border radius */
  }

  .dark {
    /* Dark Mode Variable Overrides */
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;

    --card: 222.2 84% 4.9%;
    --card-foreground: 210 40% 98%;

    --popover: 222.2 84% 4.9%;
    --popover-foreground: 210 40% 98%;

    --primary: 210 40% 98%;
    --primary-foreground: 222.2 47.4% 11.2%;

    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;

    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;

    --accent: 217.2 32.6% 17.5%;
    --accent-foreground: 210 40% 98%;

    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;

    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 212.7 26.8% 83.9%;
  }
}

@layer base {
  * {
    @apply border-border; /* Apply border color variable globally */
  }
  body {
    @apply bg-background text-foreground; /* Apply background/text color variables */
    /* Font smoothing */
  }
}
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

## Implementing Dark Mode

Shadcn UI recommends using the `next-themes` library for easy theme switching (light/dark/system).

**1. Install `next-themes`:**

```bash
npm install next-themes
# or
yarn add next-themes
```

**2. Create Theme Provider:**

Create a provider component that wraps `next-themes`'s `ThemeProvider`.

```typescript
// components/theme-provider.tsx
"use client"; // Theme provider needs client context

import * as React from "react";
import { ThemeProvider as NextThemesProvider } from "next-themes";
import type { ThemeProviderProps } from "next-themes/dist/types";

export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>;
}
```

**3. Wrap Root Layout:**

Apply the `ThemeProvider` in your root layout (`app/layout.tsx` in Next.js). Add `suppressHydrationWarning` to `<html>` to avoid warnings related to theme switching.

```typescript
// app/layout.tsx
import { ThemeProvider } from "@/components/theme-provider"; // Adjust import path

export default function RootLayout({ children }) {
  return (
    <html lang="en" suppressHydrationWarning> {/* Add suppressHydrationWarning */}
      <body>
        <ThemeProvider
          attribute="class" // Apply theme via class ('dark') on <html>
          defaultTheme="system" // Default to system preference
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

**4. Create Mode Toggle Component (Optional):**

Create a component to allow users to switch themes. (See `shadcn-common-components.md` or official docs for an example using `DropdownMenu`).

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

By defining light/dark mode variables in `globals.css` and using a theme provider like `next-themes`, you can easily implement theme switching for Shadcn UI components. Customization primarily involves adjusting these CSS variables and using Tailwind utilities.