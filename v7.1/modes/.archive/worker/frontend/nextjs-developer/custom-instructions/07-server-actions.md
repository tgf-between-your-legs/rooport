# App Router: Server Actions

Performing server-side mutations and data fetching directly from components using Server Actions.

## Core Concept: Server Actions

Server Actions are functions, marked with the `'use server'` directive, that execute **only on the server**. They allow client components (or server components via forms) to trigger server-side logic (like database updates, API calls) without needing to manually create separate API route handlers.

**Key Features:**

*   **Server-Side Execution:** Code runs securely on the server, never exposed to the client.
*   **Simplified Mutations:** Ideal for handling form submissions and data mutations (create, update, delete).
*   **Progressive Enhancement:** Work with standard HTML `<form>` elements even if JavaScript is disabled.
*   **Type Safety (with Zod):** Can be combined with libraries like Zod for input validation.
*   **Return Values:** Can return serializable data back to the client.
*   **Revalidation:** Can use `revalidatePath` or `revalidateTag` to update cached data after a mutation.
*   **Error Handling:** Use `try...catch` and return structured error objects or throw errors.

## Defining Server Actions

1.  **Inline (in Client Components):** Define an `async` function directly within a Client Component (`'use client'`) and place the `'use server'` directive *at the top* of the function body. (Less common for complex actions).

    ```jsx
    // components/AddItemButton.tsx
    'use client';
    import { revalidatePath } from 'next/cache';

    export default function AddItemButton({ itemName }) {
      async function handleAddItem() {
        'use server'; // Directive inside the async function
        console.log('Server Action: Adding item', itemName);
        try {
          // await addItemToDb({ name: itemName });
          revalidatePath('/items'); // Revalidate the items page cache
          return { success: true, message: 'Item added!' };
        } catch (error) {
          console.error('Server Action Error:', error);
          return { success: false, message: 'Failed to add item.' };
        }
      }
      // ... button calling handleAddItem ...
    }
    ```

2.  **Separate File (Recommended):** Define actions in a separate file (e.g., `app/actions.ts` or `lib/actions.ts`) and place the `'use server'` directive *at the top of the file*. Export the action functions.

    ```typescript
    // lib/actions.ts
    'use server'; // Directive at the top of the file

    import { revalidatePath } from 'next/cache';
    import { z } from 'zod';
    // import { createPostInDb } from '@/lib/db';

    const PostSchema = z.object({ /* ... schema ... */ });

    export async function createPostAction(prevState: any, formData: FormData) {
      const validatedFields = PostSchema.safeParse({ /* ... parse formData ... */ });

      if (!validatedFields.success) {
        return { errors: validatedFields.error.flatten().fieldErrors, message: 'Validation failed.' };
      }

      try {
        // await createPostInDb(validatedFields.data);
        revalidatePath('/blog');
        return { success: true, message: 'Post created!' };
      } catch (error) {
        return { success: false, message: 'Database error.' };
      }
    }
    ```

## Invoking Server Actions

**1. From Forms (`<form action={...}>`):**
*   Pass the Server Action function directly to the `action` prop.
*   Works with or without JavaScript.
*   Use `useFormState` (from `react-dom`) in Client Components to handle pending states and display responses/errors without page refresh. Action must accept `prevState` as first arg.
*   Use `useFormStatus` (from `react-dom`) in Client Components to show pending states (e.g., disable submit button).

```jsx
// components/CreatePostForm.tsx
'use client';
import { useFormState, useFormStatus } from 'react-dom';
import { createPostAction } from '@/lib/actions';

const initialState = { message: null, errors: {} };

function SubmitButton() {
  const { pending } = useFormStatus();
  return <button type="submit" disabled={pending}>{pending ? 'Creating...' : 'Create Post'}</button>;
}

export function CreatePostForm() {
  const [state, formAction] = useFormState(createPostAction, initialState);

  return (
    <form action={formAction}>
      {/* ... form fields ... */}
      {state?.message && <p>{state.message}</p>}
      <SubmitButton />
    </form>
  );
}
```

**2. Programmatically (e.g., `onClick`):**
*   Import the action function into a Client Component.
*   Call it like a regular `async` function from an event handler.
*   Use `startTransition` (from React) to mark the update as non-urgent and manage pending UI states.

```jsx
// components/DeleteButton.tsx
'use client';
import React, { useTransition } from 'react';
import { deletePostAction } from '@/lib/actions';

export default function DeleteButton({ postId }) {
  const [isPending, startTransition] = useTransition();

  const handleDelete = () => {
    startTransition(async () => { // Wrap async action call
      const result = await deletePostAction(postId);
      // Handle result...
    });
  };

  return <button onClick={handleDelete} disabled={isPending}>{isPending ? 'Deleting...' : 'Delete'}</button>;
}
```

## Security & Best Practices

*   Server Actions run on the server, protecting sensitive logic.
*   **Always validate data** passed to Server Actions (e.g., using Zod).
*   **Always perform authorization checks** within actions (e.g., check user roles/permissions).
*   Use `revalidatePath` or `revalidateTag` after successful mutations to update cached data.

*(Refer to the official Next.js documentation on Server Actions.)*