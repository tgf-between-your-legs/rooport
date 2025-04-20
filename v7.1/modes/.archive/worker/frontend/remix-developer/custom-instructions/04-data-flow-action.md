# Data Flow: `action` & `useActionData`

## Core Concept: Server Data Mutations

Remix handles data mutations (like creating, updating, or deleting data via form submissions) primarily through the `action` function exported from a route module. This function runs **only on the server** when a non-GET request (typically POST from a `<Form>`) is made to the route's URL.

**Benefits:**

*   **Server-Side Logic:** Mutation logic runs securely on the server.
*   **Progressive Enhancement:** Works with standard HTML `<Form>` submissions.
*   **Simplified Data Flow:** Remix automatically revalidates data (`loader` functions) after successful actions.
*   **Feedback Mechanism:** Actions can return data (using `json()`) accessible via `useActionData` for success/error messages.
*   **Error Handling:** Errors thrown are caught by the nearest `ErrorBoundary`.

## Implementation

**1. Export `action` Function:**

*   Define and export an `async function action` from your route module.
*   **Signature:** `export async function action({ request, params, context }: ActionFunctionArgs) { ... }`
    *   `request`: Standard Fetch API `Request`. Use `await request.formData()` to access submitted form data.
    *   `params`: Dynamic route segment values.
    *   `context`: App-wide context.
*   **Return Value:**
    *   **Must return a `Response` or `null`.**
    *   Use `json()` to return data (validation errors, success messages) back to the component via `useActionData`. `return json({ errors: validationErrors });`
    *   Use `redirect()` to navigate after a successful mutation. `return redirect(`/posts/${newPost.id}`);`
    *   Throw a `Response` to trigger the `ErrorBoundary`.

```typescript
// app/routes/posts.new.tsx
import type { ActionFunctionArgs } from "@remix-run/node";
import { json, redirect } from "@remix-run/node";
import { Form, useActionData, useNavigation } from "@remix-run/react";
// import { createPost } from "~/db/posts";

export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const title = formData.get("title") as string;
  const body = formData.get("body") as string;

  const errors: { title?: string; body?: string } = {};
  if (!title || title.length < 3) errors.title = "Title too short";
  if (!body || body.length < 10) errors.body = "Body too short";

  if (Object.keys(errors).length > 0) {
    return json({ errors }, { status: 400 });
  }

  try {
    console.log("Action: Creating post", { title, body });
    // const newPost = await createPost({ title, body });
    const newPost = { id: Date.now().toString(), title, body }; // Placeholder
    return redirect(`/posts/${newPost.id}`);
  } catch (error) {
    console.error("Failed to create post:", error);
    return json({ errors: { form: "Failed to create post." } }, { status: 500 });
  }
}
```

**2. Access Action Data with `useActionData`:**

*   Import `useActionData` from `@remix-run/react`.
*   Call the hook in your route component.
*   Returns the **deserialized data** returned via `json()` from the *most recent* action submission for that route, or `undefined` if no action has run or if the action redirected.
*   Useful for displaying validation errors or success messages.
*   TypeScript Tip: `const actionData = useActionData<typeof action>();`

```typescript
// In component part of app/routes/posts.new.tsx
import { useActionData } from "@remix-run/react";

export default function NewPostRoute() {
  const actionData = useActionData<typeof action>();
  // ...
  return (
    <Form method="post">
      {/* ... form fields ... */}
      {actionData?.errors?.title && (
        <em style={{ color: 'red' }}>{actionData.errors.title}</em>
      )}
      {/* ... other fields and errors ... */}
      <button type="submit">Create</button>
    </Form>
  );
}
```

## Data Flow Summary (Mutation)

1.  **Mutation (e.g., Form Submit):** User submits a `<Form method="post">`.
2.  **`action` Runs (Server):** The `action` function for the route executes on the server.
3.  **`action` Returns:** The `action` returns a `Response` (e.g., redirect) or JSON data.
4.  **Loaders Re-run:** After the action completes successfully (and doesn't redirect), Remix automatically re-runs the loaders for the current page.
5.  **Component Re-renders:** The component re-renders with the updated loader data.
6.  **`useActionData`:** If the action returned JSON data, it's accessible via `useActionData` during the re-render triggered by the action completion (before loaders re-run).

*(Combined from `data-flow.md` and `remix-data-flow-action.md`)*