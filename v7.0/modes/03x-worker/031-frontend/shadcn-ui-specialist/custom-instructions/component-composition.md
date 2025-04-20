# Shadcn UI: Component Composition

Building UIs by composing Shadcn UI components.

## Core Concept

Shadcn UI is **not** a traditional component library package you install. Instead, you use its CLI to copy the source code for individual, unstyled components (built using Radix UI primitives and styled with Tailwind CSS) directly into your project (typically under `components/ui/`).

You then import these components from your local project structure and compose them together just like regular React components. Customization happens by directly editing the copied component code or by applying Tailwind utility classes when using the component.

## Example: Building a Card with Button

1.  **Add Components via CLI:**
    ```bash
    npx shadcn-ui@latest add card button
    ```
    This copies `card.tsx` and `button.tsx` (and any dependencies) into your `components/ui/` directory.

2.  **Import and Compose:** Import the components from your local `components/ui` path and use them in your React component.
    ```tsx
    // src/components/MyFeatureCard.tsx
    import React from 'react';
    import { Button } from "@/components/ui/button"; // Adjust import path based on your setup
    import {
      Card,
      CardContent,
      CardDescription,
      CardFooter,
      CardHeader,
      CardTitle,
    } from "@/components/ui/card";
    import { BellRing, Check } from "lucide-react"; // Example icon library

    export function MyFeatureCard() {
      return (
        <Card className="w-[380px]"> {/* Use Tailwind classes for layout */}
          <CardHeader>
            <CardTitle>Feature Title</CardTitle>
            <CardDescription>Brief description of the feature.</CardDescription>
          </CardHeader>
          <CardContent className="grid gap-4">
            {/* Add specific content */}
            <div className="flex items-center space-x-4 rounded-md border p-4">
              <BellRing />
              <div className="flex-1 space-y-1">
                <p className="text-sm font-medium leading-none">
                  Push Notifications
                </p>
                <p className="text-sm text-muted-foreground">
                  Send notifications to device.
                </p>
              </div>
            </div>
            {/* ... other content ... */}
          </CardContent>
          <CardFooter>
            <Button className="w-full"> {/* Use Tailwind classes for styling */}
              <Check className="mr-2 h-4 w-4" /> Mark as Read
            </Button>
          </CardFooter>
        </Card>
      );
    }
    ```

## Key Principles

*   **Import Locally:** Always import Shadcn components from your project's `components/ui` directory (or wherever the CLI placed them), not directly from `@radix-ui` or a non-existent `@shadcn/ui` package.
*   **Composition:** Build complex UI elements by nesting and combining different Shadcn components (`Card` containing `Button`, `Input` inside `Form`, etc.).
*   **Styling via Tailwind:** Apply layout, spacing, colors, and other styles primarily using Tailwind utility classes directly on the components in your JSX.
*   **Direct Customization:** If a component's structure or base style needs significant changes, directly edit the corresponding file in `components/ui/`. Remember that re-running `npx shadcn-ui@latest add [component]` might overwrite your changes unless you use the diffing option or manage changes carefully.
*   **Leverage Variants:** Components often come with pre-defined variants (e.g., `<Button variant="destructive">`). Use these where appropriate. You can also add custom variants by modifying the component's source code (often using `cva` - Class Variance Authority).

*(Refer to the official Shadcn UI documentation for examples of specific components: https://ui.shadcn.com/docs/components)*