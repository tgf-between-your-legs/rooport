# Next.js: Server Actions

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

1.  **Inline (in Client Components):** Define an `async` function directly within a Client Component (`'use client'`) and place the `'use server'` directive *at the top* of the function body.

    ```jsx
    // components/AddItemButton.tsx
    'use client';

    import { revalidatePath } from 'next/cache';
    // import { addItemToDb } from '@/lib/db'; // Your server-side DB logic

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

      return (
        <button onClick={async () => {
          const result = await handleAddItem();
          alert(result.message);
        }}>
          Add {itemName}
        </button>
      );
    }
    ```

2.  **Separate File (Recommended for Reusability):** Define actions in a separate file (e.g., `app/actions.ts`) and place the `'use server'` directive *at the top of the file*. Export the action functions.

    ```typescript
    // app/actions.ts
    'use server'; // Directive at the top of the file

    import { revalidatePath } from 'next/cache';
    import { z } from 'zod'; // Example using Zod for validation
    // import { createPost } from '@/lib/db';

    const PostSchema = z.object({
      title: z.string().min(3, "Title must be at least 3 characters"),
      content: z.string().min(10, "Content must be at least 10 characters"),
    });

    export async function createPostAction(prevState: any, formData: FormData) {
      // prevState is used with useFormState hook

      const validatedFields = PostSchema.safeParse({
        title: formData.get('title'),
        content: formData.get('content'),
      });

      // Return validation errors
      if (!validatedFields.success) {
        return {
          errors: validatedFields.error.flatten().fieldErrors,
          message: 'Validation failed.',
        };
      }

      // If validation passes, perform the mutation
      try {
        console.log('Server Action: Creating post', validatedFields.data);
        // await createPost(validatedFields.data);
        revalidatePath('/blog'); // Revalidate blog index
        return { success: true, message: 'Post created successfully!' };
      } catch (error) {
        console.error('Database Error:', error);
        return { success: false, message: 'Database error occurred.' };
      }
    }

    export async function deletePostAction(postId: string) {
       try {
         console.log('Server Action: Deleting post', postId);
         // await deletePostFromDb(postId);
         revalidatePath('/blog');
         revalidatePath(`/blog/${postId}`); // Revalidate specific post page too
         return { success: true };
       } catch (error) {
         console.error('Error deleting post:', error);
         return { success: false, message: 'Failed to delete post.' };
       }
    }
    ```

## Invoking Server Actions

**1. From Forms (`<form action={...}>`):**

*   Pass the Server Action function directly to the `action` prop of a standard HTML `<form>`.
*   Next.js automatically handles the request when the form is submitted. Works with or without JavaScript enabled.
*   Use the `useFormState` hook (from `react-dom`) to handle pending states and display responses/errors from the action without a page refresh (requires Client Component).
*   Use the `useFormStatus` hook (from `react-dom`) to show pending states specifically for form submissions (e.g., disabling the submit button).

```jsx
// components/CreatePostForm.tsx
'use client';

import { useFormState, useFormStatus } from 'react-dom';
import { createPostAction } from '@/app/actions'; // Import action from separate file
import Button from '@mui/material/Button'; // Example UI component
import TextField from '@mui/material/TextField';
import Alert from '@mui/material/Alert';

const initialState = { message: null, errors: {} };

function SubmitButton() {
  const { pending } = useFormStatus(); // Hook to get form pending state
  return <Button type="submit" variant="contained" disabled={pending}>{pending ? 'Creating...' : 'Create Post'}</Button>;
}

export function CreatePostForm() {
  // useFormState manages state updates based on action return value
  const [state, formAction] = useFormState(createPostAction, initialState);

  return (
    <form action={formAction}> {/* Pass the action */}
      <h2>Create New Post</h2>
      <TextField name="title" label="Title" fullWidth margin="normal" required error={!!state?.errors?.title} helperText={state?.errors?.title?.[0]} />
      <TextField name="content" label="Content" fullWidth margin="normal" multiline rows={4} required error={!!state?.errors?.content} helperText={state?.errors?.content?.[0]} />

      {state?.message && !state.success && <Alert severity="error" sx={{ mt: 2 }}>{state.message}</Alert>}
      {state?.message && state.success && <Alert severity="success" sx={{ mt: 2 }}>{state.message}</Alert>}

      <SubmitButton /> {/* Use component with useFormStatus */}
    </form>
  );
}
```

**2. Programmatically (e.g., `onClick`):**

*   Import the action function.
*   Call it like a regular `async` function from an event handler in a Client Component.
*   Use `startTransition` (from React) to mark the update as non-urgent, preventing the UI from freezing during the action's execution.

```jsx
// components/DeleteButton.tsx
'use client';
import React, { useTransition } from 'react';
import { deletePostAction } from '@/app/actions';
import Button from '@mui/material/Button';

export default function DeleteButton({ postId }) {
  const [isPending, startTransition] = useTransition();

  const handleDelete = () => {
    startTransition(async () => { // Wrap the async action call
      const result = await deletePostAction(postId);
      if (!result.success) {
        alert(result.message || 'Failed to delete');
      }
      // UI updates based on revalidation will happen automatically
    });
  };

  return <Button color="error" onClick={handleDelete} disabled={isPending}>{isPending ? 'Deleting...' : 'Delete'}</Button>;
}
```

Server Actions provide a powerful and integrated way to handle data mutations and server-side logic triggered from the client in Next.js App Router applications.

*(Refer to the official Next.js documentation on Server Actions.)*