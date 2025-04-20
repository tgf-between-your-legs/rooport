# Shadcn UI: Theming (CSS Variables & Dark Mode)

Customizing the appearance and implementing dark mode for Shadcn UI components.

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

Create a component to allow users to switch themes.

```typescript
// components/mode-toggle.tsx
"use client";

import * as React from "react";
import { Moon, Sun } from "lucide-react"; // Example icons
import { useTheme } from "next-themes";

import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"; // Shadcn Dropdown

export function ModeToggle() {
  const { setTheme } = useTheme();

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="icon">
          <Sun className="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
          <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
          <span className="sr-only">Toggle theme</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        <DropdownMenuItem onClick={() => setTheme("light")}>Light</DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme("dark")}>Dark</DropdownMenuItem>
        <DropdownMenuItem onClick={() => setTheme("system")}>System</DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
```

By defining light/dark mode variables in `globals.css` and using a theme provider like `next-themes`, you can easily implement theme switching for Shadcn UI components. Customization primarily involves adjusting these CSS variables and using Tailwind utilities.

*(Refer to the official Shadcn UI documentation on Theming and Dark Mode.)*