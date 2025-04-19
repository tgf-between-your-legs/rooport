# 4. Styling & Customization

Applying styles and customizing the appearance of Shadcn UI components using Tailwind CSS and direct code modification.

## Core Styling Approach

Shadcn UI components are styled primarily using **Tailwind CSS utility classes**. Because you add the component source code directly to your project, you have full control over these classes.

## 1. Using Tailwind Utilities

*   **Directly on Components:** Apply Tailwind classes directly via the `className` prop when using the components. Use the `cn()` utility (from `lib/utils`) to merge classes safely.
    ```tsx
    import { Button } from "@/components/ui/button";
    import { Card } from "@/components/ui/card";
    import { cn } from "@/lib/utils";

    <Card className={cn("mt-4 p-6 border-blue-500 shadow-lg", props.className)}>
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
    // ... rest of button component using cn(buttonVariants({ variant, size, className })) ...
    ```

## 2. Using CSS Variables (Theming)

*   **Initialization:** During `npx shadcn-ui@latest init`, Shadcn UI sets up CSS variables in your global CSS file (e.g., `globals.css`) for colors, border radius, etc.
*   **Tailwind Configuration:** Your `tailwind.config.js` is configured to use these CSS variables (e.g., `hsl(var(--primary))`).
*   **Customization:**
    *   **Modify `globals.css`:** Change the HSL values for the CSS variables (e.g., `--primary`, `--radius`) in `globals.css` to globally alter the theme. Update both `:root` (light) and `.dark` variables.
    *   **Use Variables in Tailwind:** Tailwind utilities like `bg-primary`, `text-destructive-foreground`, `rounded-lg` automatically use these CSS variables.

## 3. `cn()` Utility

*   Shadcn UI includes a utility function (often in `lib/utils.ts`) based on `clsx` and `tailwind-merge`.
*   **Purpose:** Safely merge default component classes (including variants) with classes passed via the `className` prop, handling Tailwind class conflicts intelligently.
*   **Usage:** Wrap class strings and variant objects in `cn()` within the component's implementation.
    ```typescript
    // Example inside components/ui/button.tsx
    import { cn } from "@/lib/utils"; // Adjust import path
    // ... (buttonVariants definition) ...

    const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
      ({ className, variant, size, asChild = false, ...props }, ref) => {
        const Comp = asChild ? Slot : "button";
        return (
          <Comp
            // Use cn() to merge default variant styles with passed className
            className={cn(buttonVariants({ variant, size, className }))}
            ref={ref}
            {...props}
          />
        );
      }
    );
    ```

## 4. Direct Component Code Customization

*   Since you own the code in `components/ui/`, you can directly modify the JSX structure, add/remove elements, or change internal logic.
*   Be mindful of the underlying Radix UI primitives and accessibility implications.
*   Remember that CLI updates (`add --overwrite`) will discard these changes. (See `08-customization-updates.md`).

## Combining Approaches

*   Use CSS variables in `globals.css` for the overall theme (colors, radius).
*   Use Tailwind utilities in your JSX (`className` prop with `cn()`) for layout, spacing, and instance-specific style adjustments.
*   Modify the component source code (`components/ui/*.tsx`) for structural changes or adding/modifying default variants.

Styling in Shadcn UI primarily involves using Tailwind utility classes directly on the component code (copied into your project) or via the `className` prop, leveraging the underlying CSS variables for theming.