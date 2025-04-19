# 9. Customization & Updates

Modifying Shadcn UI components and handling updates.

## Core Concept: You Own the Code

Unlike traditional component libraries installed as dependencies in `node_modules`, Shadcn UI uses a CLI (`npx shadcn-ui@latest add [component]`) to copy the source code of the requested component directly into your project (typically under `components/ui/`).

**Implications:**

*   **Direct Customization:** You have full control to modify the component's structure (JSX), styling (Tailwind classes), and even logic directly within its file.
*   **No Version Locking:** You are not locked into a specific version of the Shadcn UI "library" because the code is part of your codebase.
*   **Update Responsibility:** You are responsible for updating components if Shadcn UI releases improvements or bug fixes. Updates are **not** automatic via `npm install` or `yarn upgrade`.

## Customizing Components

1.  **Locate the Component File:** Find the component's source file (e.g., `components/ui/button.tsx`).
2.  **Modify JSX:** Change the underlying HTML structure if needed (e.g., wrap an element, add attributes). Be mindful of accessibility implications and Radix UI primitive requirements.
3.  **Modify Styling (Tailwind):**
    *   Add, remove, or change Tailwind utility classes directly in the `className` attributes within the JSX.
    *   Adjust default styles defined using `cva` (Class Variance Authority) if the component uses it for variants.
    *   Use the `cn()` utility function (from `lib/utils`) to correctly merge default classes with any `className` prop passed to the component.
4.  **Modify Logic (If Necessary):** Change component behavior or internal state management (use standard React practices).

**Example: Adding a Loading State to Button**

```diff
--- a/src/components/ui/button.tsx
+++ b/src/components/ui/button.tsx
@@ -1,5 +1,6 @@
 import * as React from "react"
 import { Slot } from "@radix-ui/react-slot"
+import { Loader2 } from "lucide-react" // Example icon
 import { cva, type VariantProps } from "class-variance-authority"

 import { cn } from "@/lib/utils"
@@ -29,6 +30,7 @@
   className?: string
   variant?: VariantProps<typeof buttonVariants>["variant"]
   size?: VariantProps<typeof buttonVariants>["size"]
+  isLoading?: boolean // Add new prop for loading state
   asChild?: boolean
 }

@@ -36,12 +38,15 @@
   ({ className, variant, size, isLoading, asChild = false, ...props }, ref) => {
     const Comp = asChild ? Slot : "button"
     return (
+      // Add relative positioning for potential spinner overlay
       <Comp
-        className={cn(buttonVariants({ variant, size, className }))}
+        className={cn(buttonVariants({ variant, size, className }), "relative")}
         ref={ref}
+        disabled={isLoading || props.disabled} // Disable if loading
         {...props}
-      />
+      >
+        {/* Add loading spinner */}
+        {isLoading && <Loader2 className="absolute h-4 w-4 animate-spin" />}
+        {/* Make children invisible when loading */}
+        <span className={cn(isLoading && "invisible")}>{props.children}</span>
+      </Comp>
     )
   }
 )
 Button.displayName = "Button"

 export { Button, buttonVariants }

```

## Handling Updates

When Shadcn UI updates its components (e.g., bug fixes, new features, style changes), these updates are **not** automatically applied to your project.

**Update Strategies:**

1.  **Manual Diffing (Recommended for Customizations):**
    *   Check the Shadcn UI changelog or component documentation for updates.
    *   View the changes made to the component's source code in the official Shadcn UI repository or documentation examples.
    *   Manually apply the relevant changes to *your* version of the component file (`components/ui/*.tsx`), carefully merging them with your existing customizations. This preserves your modifications. Use diff tools if necessary.
2.  **Re-running the CLI `add` Command (Overwrites Customizations):**
    *   Run `npx shadcn-ui@latest add [component] --overwrite`.
    *   This will **overwrite** your existing component file (`components/ui/[component].tsx`) with the latest version from Shadcn UI.
    *   **Warning:** This will **discard any customizations** you have made to that specific file. Only use this if you haven't customized the component or are willing to re-apply your customizations manually afterward. Back up your customized file before overwriting.
3.  **Selective Updates:** You only need to update components if you need the specific fixes or features included in the update. You can update components individually as needed.

Because you own the component code, you have full control over customization but also the responsibility for managing updates by comparing and merging changes or carefully overwriting and reapplying modifications.

*(Refer to the official Shadcn UI documentation on Updates and Customization.)*