# Shadcn UI: Form Integration (React Hook Form & Zod)

Building accessible and validated forms using Shadcn UI components, React Hook Form, and Zod.

## Core Concept: Combining Libraries

Shadcn UI provides styled form components (`Form`, `FormField`, `FormItem`, `FormLabel`, `FormControl`, `FormDescription`, `FormMessage`) that are designed to integrate seamlessly with `react-hook-form` for state management and `zod` for schema validation.

**Libraries:**

*   **Shadcn UI:** Provides the styled UI components (`Input`, `Checkbox`, `Select`, etc.) and form layout components.
*   **React Hook Form (`react-hook-form`):** Manages form state (values, errors, touched fields, submission status) efficiently with minimal re-renders. Uses uncontrolled inputs by default.
*   **Zod (`zod`):** A TypeScript-first schema declaration and validation library. Define your form's expected data shape and validation rules.

## Setup

1.  **Install Dependencies:**
    ```bash
    npm install react-hook-form zod @hookform/resolvers
    # or
    yarn add react-hook-form zod @hookform/resolvers
    ```
2.  **Add Shadcn Form Components:**
    ```bash
    npx shadcn-ui@latest add form label input button toast # Add others as needed (select, checkbox, etc.)
    ```

## Implementation Steps

**1. Define Zod Schema:**

Create a schema defining the form fields and their validation rules.

```typescript
// src/lib/validators/profileSchema.ts (Example)
import { z } from "zod";

export const profileFormSchema = z.object({
  username: z.string().min(2, {
    message: "Username must be at least 2 characters.",
  }).max(30, {
    message: "Username must not exceed 30 characters.",
  }),
  email: z.string().email({ message: "Invalid email address." }),
  bio: z.string().max(160).optional(),
  newsletter: z.boolean().default(false).optional(),
});

export type ProfileFormValues = z.infer<typeof profileFormSchema>;
```

**2. Create the Form Component:**

*   Import necessary components from Shadcn UI (`Form`, `FormField`, etc.), `react-hook-form` (`useForm`), `zodResolver` from `@hookform/resolvers/zod`, and your Zod schema.
*   Use the `useForm` hook, providing the Zod schema to `resolver` for validation.
*   Wrap your form elements in the Shadcn `<Form {...form}>` component.
*   Use the Shadcn `<FormField>` component for each input field. It connects `react-hook-form`'s state to the individual input components.
    *   `control`: Pass `form.control` from `useForm`.
    *   `name`: The name of the field (must match schema).
    *   `render={({ field }) => (...) }`: A render prop function receiving the `field` object (`onChange`, `onBlur`, `value`, `ref`, `name`). Spread `...field` onto your Shadcn input component (`Input`, `Checkbox`, etc.).
*   Use `FormItem`, `FormLabel`, `FormControl`, `FormDescription`, `FormMessage` for structure and displaying labels/errors. `FormMessage` automatically displays validation errors from `react-hook-form`.

```typescript
// src/components/ProfileForm.tsx
"use client"; // Forms require client-side interactivity

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import * as z from "zod";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Checkbox } from "@/components/ui/checkbox";
import { Textarea } from "@/components/ui/textarea"; // Assuming Textarea component added
import { toast } from "@/components/ui/use-toast"; // Assuming Toast component added

// Import schema defined earlier
import { profileFormSchema, type ProfileFormValues } from "@/lib/validators/profileSchema";

export function ProfileForm() {
  // 1. Define form with useForm and Zod resolver
  const form = useForm<ProfileFormValues>({
    resolver: zodResolver(profileFormSchema),
    defaultValues: { // Set default values matching schema
      username: "",
      email: "",
      bio: "",
      newsletter: false,
    },
  });

  // 2. Define submit handler
  function onSubmit(values: ProfileFormValues) {
    // Do something with the validated form values.
    console.log(values);
    toast({ // Example using Shadcn Toast
      title: "Profile Submitted:",
      description: <pre className="mt-2 w-[340px] rounded-md bg-slate-950 p-4"><code className="text-white">{JSON.stringify(values, null, 2)}</code></pre>,
    });
  }

  return (
    // 3. Build form structure with Shadcn components
    <Form {...form}> {/* Spread form methods */}
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => ( // Render prop provides field state/handlers
            <FormItem>
              <FormLabel>Username</FormLabel>
              <FormControl>
                <Input placeholder="Your username" {...field} /> {/* Spread field props */}
              </FormControl>
              <FormDescription>This is your public display name.</FormDescription>
              <FormMessage /> {/* Displays validation errors for this field */}
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input type="email" placeholder="your@email.com" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
         <FormField
          control={form.control}
          name="bio"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Bio</FormLabel>
              <FormControl>
                <Textarea placeholder="Tell us about yourself" {...field} />
              </FormControl>
              <FormDescription>Max 160 characters.</FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
         <FormField
          control={form.control}
          name="newsletter"
          render={({ field }) => (
            <FormItem className="flex flex-row items-start space-x-3 space-y-0 rounded-md border p-4">
              <FormControl>
                 {/* Note: Checkbox uses checked/onCheckedChange */}
                <Checkbox
                  checked={field.value}
                  onCheckedChange={field.onChange}
                  // disabled={...}
                  // aria-invalid={...}
                />
              </FormControl>
              <div className="space-y-1 leading-none">
                <FormLabel>Subscribe to newsletter</FormLabel>
                <FormDescription>Receive updates via email.</FormDescription>
              </div>
               <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit" disabled={form.formState.isSubmitting}>
          {form.formState.isSubmitting ? "Saving..." : "Save Profile"}
        </Button>
      </form>
    </Form>
  );
}
```

This combination provides a robust way to build accessible, styled forms with powerful validation and state management in React applications using Shadcn UI.

*(Refer to Shadcn UI Form docs, React Hook Form docs, and Zod docs.)*