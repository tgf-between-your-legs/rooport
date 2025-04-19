# Next.js Server Actions

Using Server Actions for handling form submissions and server mutations in Next.js App Router.

## Core Concept

Server Actions are functions marked with the `'use server'` directive that run **only on the server**. They can be called directly from Client Components (e.g., in form submissions or event handlers) or Server Components. They simplify handling mutations and server-side logic without manually creating API Route Handlers for every action.

## Enabling Server Actions

Server Actions are enabled by default in recent Next.js versions. If using an older version, you might need to enable the experimental flag in `next.config.js`:

```js
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    serverActions: true,
  },
};
module.exports = nextConfig;
```

## Defining Server Actions

1.  **Inline (in Server Components):** Define an async function directly within a Server Component and add `'use server';` at the *top* of the function body.
    ```tsx
    // app/page.tsx (Server Component)
    import { revalidatePath } from 'next/cache';

    export default function Page() {
      async function createItem(formData: FormData) {
        'use server'; // Directive inside the function

        const rawData = {
          name: formData.get('itemName') as string,
        };
        // TODO: Validate rawData
        // TODO: Save data to database
        console.log('Creating item:', rawData);
        revalidatePath('/'); // Revalidate the current page
      }

      return (
        <form action={createItem}> {/* Pass the action directly */}
          <input type="text" name="itemName" required />
          <button type="submit">Add Item</button>
        </form>
      );
    }
    ```
2.  **Separate File (Recommended for Reusability):** Create a separate file (e.g., `app/actions.ts`) and add `'use server';` at the **very top** of the file. Export your action functions.
    ```typescript
    // app/actions.ts
    'use server'; // Directive at the top of the file

    import { revalidatePath } from 'next/cache';
    import { z } from 'zod'; // Example using Zod for validation

    const itemSchema = z.object({
      name: z.string().min(3, "Name must be at least 3 characters"),
    });

    export async function createItemAction(prevState: any, formData: FormData) {
      const validatedFields = itemSchema.safeParse({
        name: formData.get('itemName'),
      });

      // Return early if validation fails
      if (!validatedFields.success) {
        return {
          errors: validatedFields.error.flatten().fieldErrors,
          message: 'Validation failed.',
        };
      }

      // TODO: Save validatedFields.data to database
      console.log('Creating item:', validatedFields.data);

      revalidatePath('/'); // Revalidate relevant path(s)
      return { message: `Item "${validatedFields.data.name}" created.` };
    }

    export async function deleteItemAction(itemId: string) {
       // TODO: Delete item from database using itemId
       console.log('Deleting item:', itemId);
       revalidatePath('/');
       // Can return data or status
    }
    ```

## Calling Server Actions

*   **From Forms:** Pass the action function directly to the `<form action={...}>` prop. Next.js handles progressive enhancement.
*   **From Client Components (Event Handlers):** Import the action and call it directly within an event handler (e.g., `onClick`). Use `startTransition` from React to manage pending states.
    ```tsx
    // app/components/ItemCard.tsx
    'use client';
    import { useTransition } from 'react';
    import { deleteItemAction } from '../actions'; // Import the action

    export function ItemCard({ item }: { item: { id: string; name: string } }) {
      let [isPending, startTransition] = useTransition();

      return (
        <div>
          <span>{item.name}</span>
          <button
            onClick={() => {
              startTransition(async () => {
                // Call the server action
                await deleteItemAction(item.id);
                // Optionally show feedback after completion
              });
            }}
            disabled={isPending}
          >
            {isPending ? 'Deleting...' : 'Delete'}
          </button>
        </div>
      );
    }
    ```

## Handling Return Values & State

*   **Forms (`useFormState` - React Hook):** Use the `useFormState` hook (from `react-dom`) to handle form state (pending status, validation errors, success messages) returned by Server Actions. The action needs to accept `prevState` as its first argument.
    ```tsx
    // app/components/AddItemForm.tsx
    'use client';
    import { useFormState, useFormStatus } from 'react-dom';
    import { createItemAction } from '../actions';

    const initialState = { message: null, errors: {} };

    function SubmitButton() {
      const { pending } = useFormStatus(); // Hook to get form pending state
      return <button type="submit" disabled={pending}>{pending ? 'Adding...' : 'Add Item'}</button>;
    }

    export function AddItemForm() {
      const [state, formAction] = useFormState(createItemAction, initialState);

      return (
        <form action={formAction}>
          <label htmlFor="itemName">Item Name:</label>
          <input id="itemName" type="text" name="itemName" required />
          {state?.errors?.name && <p style={{ color: 'red' }}>{state.errors.name[0]}</p>}

          <SubmitButton />
          {state?.message && !state.errors && <p style={{ color: 'green' }}>{state.message}</p>}
          {state?.message && state.errors && <p style={{ color: 'red' }}>{state.message}</p>}
        </form>
      );
    }
    ```
*   **Event Handlers:** Use `useTransition` to manage pending states. The return value of the action is available in the `await` call.

## Security

*   Server Actions execute on the server, protecting sensitive logic.
*   **Always validate data** passed to Server Actions (using libraries like Zod is recommended).
*   **Always perform authorization checks** within Server Actions to ensure the user has permission to perform the action (e.g., check `auth().userId` or roles).

*(Refer to the official Next.js Server Actions documentation: https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)*