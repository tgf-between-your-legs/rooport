# Shadcn UI: Styling & Customization

Applying styles and customizing the appearance of Shadcn UI components using Tailwind CSS and direct code modification.

## Core Styling Approach

Shadcn UI components are styled primarily using **Tailwind CSS utility classes**. Because you add the component source code directly to your project, you have full control over these classes.

## 1. Using Tailwind Utilities

*   **Directly on Components:** Apply Tailwind classes directly via the `className` prop when using the components.
    ```tsx
    import { Button } from "@/components/ui/button";
    import { Card } from "@/components/ui/card";

    <Card className="mt-4 p-6 border-blue-500 shadow-lg">
      <p className="text-lg font-semibold mb-2">Card Title</p>
      <Button variant="outline" className="text-red-600 border-red-600 hover:bg-red-50">
        Destructive Action
      </Button>
    </Card>
    ```
*   **Inside Component Source:** Modify the component's source file (e.g., `components/ui/button.tsx`) to change the default utility classes applied. This affects all instances of that component.
    ```tsx
    // Example modification inside components/ui/button.tsx
    // (Using `cva` for variants)
    const buttonVariants = cva(
      "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
      {
        variants: {
          variant: {
            default: "bg-primary text-primary-foreground hover:bg-primary/90",
            destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
            outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
            secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
            ghost: "hover:bg-accent hover:text-accent-foreground",
            link: "text-primary underline-offset-4 hover:underline",
            // Add a custom variant
            premium: "bg-gradient-to-r from-yellow-400 via-gold-500 to-yellow-600 text-white border-none shadow-md"
          },
          size: {
            default: "h-10 px-4 py-2",
            sm: "h-9 rounded-md px-3",
            lg: "h-11 rounded-md px-8 text-lg", // Make lg bigger
            icon: "h-10 w-10",
          },
        },
        defaultVariants: {
          variant: "default",
          size: "default",
        },
      }
    )
    // ... rest of button component ...
    ```

## 2. Using CSS Variables (Theming)

*   **Initialization:** During `npx shadcn-ui@latest init`, Shadcn UI sets up CSS variables in your global CSS file (e.g., `globals.css` or `index.css`) for colors, border radius, etc., based on your selections.
*   **Tailwind Configuration:** Your `tailwind.config.js` is configured to use these CSS variables.
    ```js
    // tailwind.config.js (example snippet)
    theme: {
      container: { center: true, padding: "2rem", screens: { "2xl": "1400px" } },
      extend: {
        colors: {
          border: "hsl(var(--border))",
          input: "hsl(var(--input))",
          // ... other color variables ...
          primary: {
            DEFAULT: "hsl(var(--primary))",
            foreground: "hsl(var(--primary-foreground))",
          },
          // ... secondary, destructive, etc.
        },
        borderRadius: {
          lg: "var(--radius)",
          md: "calc(var(--radius) - 2px)",
          sm: "calc(var(--radius) - 4px)",
        },
        // ... other theme extensions ...
      },
    },
    ```
*   **Customization:**
    *   **Modify `globals.css`:** Change the HSL values for the CSS variables (e.g., `--primary`, `--radius`) in `globals.css` to globally alter the theme. Make sure to update both the light (`:root`) and dark (`.dark`) theme variables if supporting dark mode.
    *   **Use Variables in Tailwind:** Tailwind utilities like `bg-primary`, `text-destructive-foreground`, `rounded-lg` automatically use these CSS variables because of the `tailwind.config.js` setup.

## 3. Combining Approaches

*   Use CSS variables in `globals.css` for the overall theme (colors, radius).
*   Use Tailwind utilities in your JSX for layout, spacing, and one-off style adjustments.
*   Modify the component source code (`components/ui/*.tsx`) if you need to change the fundamental structure or add/modify default variants using `cva`.

## Key Considerations

*   **Component Ownership:** You own the component code copied into `components/ui/`. Feel free to modify it, but be aware that updates via the CLI might overwrite changes. Consider version control and careful merging.
*   **`cn` Utility:** Shadcn components use a utility function (often named `cn`, imported from `lib/utils`) which merges Tailwind classes, typically using `clsx` and `tailwind-merge`. This handles conditional classes and prevents conflicting Tailwind utilities.
*   **Radix UI:** Underlying accessibility and behavior often come from Radix UI primitives. Styling these primitives directly might sometimes be necessary for deep customization, but usually styling the composed Shadcn component is sufficient.

*(Refer to the official Shadcn UI documentation on Theming and Customization: https://ui.shadcn.com/docs/theming)*