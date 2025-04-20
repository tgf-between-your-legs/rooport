# Usage Examples for 🧩 Shadcn UI Specialist

This directory contains example prompts and expected interactions for the `shadcn-ui-specialist` mode. These examples illustrate how to request tasks and the kind of responses or actions the mode should take.

*(Examples should be added here based on common use cases)*

**Example 1: Adding and using a Button**

*   **Prompt:** "Add the Shadcn Button component and create a simple React component that displays a primary button with the text 'Submit'."
*   **Expected Actions:**
    *   Use `execute_command` to run `npx shadcn-ui@latest add button`.
    *   Use `write_to_file` or `apply_diff` to create/modify a `.tsx` file containing:
        ```tsx
        import { Button } from "@/components/ui/button";

        export function SubmitButton() {
          return <Button>Submit</Button>;
        }
        ```

**Example 2: Creating a Form Field**

*   **Prompt:** "Create a form field using Shadcn Form components for a 'username' input, integrated with react-hook-form. Assume the form instance is available as `form`."
*   **Expected Actions:**
    *   Use `apply_diff` or `write_to_file` to add the following structure within an existing `<Form {...form}>` context:
        ```tsx
        import { FormField, FormItem, FormLabel, FormControl, FormDescription, FormMessage } from "@/components/ui/form";
        import { Input } from "@/components/ui/input";

        // ... inside the form component ...
        <FormField
          control={form.control}
          name="username"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Username</FormLabel>
              <FormControl>
                <Input placeholder="shadcn" {...field} />
              </FormControl>
              <FormDescription>
                This is your public display name.
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />