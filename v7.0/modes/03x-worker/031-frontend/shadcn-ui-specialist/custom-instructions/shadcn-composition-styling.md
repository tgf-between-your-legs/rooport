# Shadcn UI: Composition & Styling

Building UIs by composing Shadcn components and styling with Tailwind CSS.

## Core Concept: Composition over Configuration

Shadcn UI emphasizes **composition**. Instead of providing monolithic components with dozens of props for every variation, it gives you building blocks that you combine and style to create the UI you need.

*   **Component Code Ownership:** When you use `npx shadcn-ui@latest add [component]`, the component's source code (React + Tailwind) is copied directly into your project (typically `components/ui/`). You own this code.
*   **Direct Customization:** You modify the component's structure (JSX) and appearance (Tailwind classes) directly in these copied files.
*   **Building Blocks:** Components are often built using Radix UI primitives (for accessibility and core logic) and styled with Tailwind CSS.

## Styling Methods

1.  **Tailwind CSS Utility Classes:**
    *   The primary method for styling Shadcn UI components.
    *   Apply Tailwind classes directly within the JSX of the component files (`components/ui/*.tsx`).
    *   Use standard Tailwind utilities (`bg-primary`, `text-destructive-foreground`, `p-4`, `rounded-md`, `hover:bg-accent`, `dark:text-white`, etc.).
    *   Leverage your project's `tailwind.config.js` for customizations.

2.  **CSS Variables (for Theming):**
    *   Shadcn UI uses CSS variables defined in your global CSS file (`globals.css` or similar) for theming (colors, border radius).
    *   These variables are typically configured during `npx shadcn-ui@latest init`.
    *   Tailwind classes like `bg-primary`, `text-foreground`, `border`, `ring-offset-background` often map to these CSS variables.
    *   You can override these variables globally or locally (using inline styles) for theme adjustments. (See `shadcn-theming.md`).

    ```css
    /* Example from globals.css */
    :root {
      --background: 0 0% 100%;
      --foreground: 222.2 84% 4.9%;
      /* ... other light theme variables ... */
      --radius: 0.5rem;
    }

    .dark {
      --background: 222.2 84% 4.9%;
      --foreground: 210 40% 98%;
      /* ... other dark theme variables ... */
    }
    ```

3.  **`className` Prop:**
    *   Pass additional Tailwind classes via the `className` prop when using a Shadcn component to apply instance-specific overrides or additions. Use `cn()` utility for merging classes.

4.  **`cn()` Utility:**
    *   Shadcn UI includes a utility function (often in `lib/utils.ts`) based on `clsx` and `tailwind-merge`.
    *   **Purpose:** Safely merge default component classes with classes passed via the `className` prop, handling Tailwind class conflicts intelligently.
    *   **Usage:** Wrap class strings in `cn()` within the component's implementation.

    ```typescript
    // Example inside components/ui/button.tsx
    import { cn } from "@/lib/utils"; // Adjust import path
    import { Slot } from "@radix-ui/react-slot";
    import * as React from "react";

    // ... (variant definitions, etc.)

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
    Button.displayName = "Button";

    export { Button, buttonVariants };
    ```

## Composition Example

Building a custom card using Shadcn components:

```jsx
// src/components/MyCustomCard.tsx
import React from 'react';
import { Button } from "@/components/ui/button"; // Shadcn Button
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"; // Shadcn Card components
import { Badge } from "@/components/ui/badge"; // Shadcn Badge
import { cn } from "@/lib/utils"; // Class merging utility

interface MyCustomCardProps {
  title: string;
  description?: string;
  imageUrl?: string;
  tags?: string[];
  className?: string; // Allow passing extra classes
}

export function MyCustomCard({
  title,
  description,
  imageUrl,
  tags,
  className,
}: MyCustomCardProps) {
  return (
    // Use cn() to merge default card styles with custom classes
    <Card className={cn("w-[350px]", className)}> {/* Default width + custom class */}
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        {description && <CardDescription>{description}</CardDescription>}
      </CardHeader>
      <CardContent>
        {imageUrl && (
          <img src={imageUrl} alt={title} className="mb-4 rounded-md" /> // Standard img tag
        )}
        {tags && tags.length > 0 && (
          <div className="flex flex-wrap gap-2">
            {tags.map((tag) => (
              <Badge key={tag} variant="secondary">{tag}</Badge>
            ))}
          </div>
        )}
      </CardContent>
      <CardFooter className="flex justify-end"> {/* Tailwind flex utilities */}
        <Button variant="outline">Cancel</Button>
        <Button className="ml-2">Deploy</Button> {/* Tailwind margin utility */}
      </CardFooter>
    </Card>
  );
}
```

Styling in Shadcn UI primarily involves using Tailwind utility classes directly on the component code (copied into your project) or via the `className` prop, leveraging the underlying CSS variables for theming. Composition is key to building complex UIs from the provided primitives.

*(Refer to Shadcn UI, Tailwind CSS, and Radix UI documentation.)*