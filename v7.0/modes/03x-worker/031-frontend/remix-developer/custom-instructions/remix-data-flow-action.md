# Remix: Data Flow with `action` and `useActionData`

Handling data mutations (form submissions) on the server using the `action` function.

## Core Concept: Server Data Mutations

Remix handles data mutations (like creating, updating, or deleting data via form submissions) primarily through the `action` function exported from a route module. This function runs **only on the server** when a non-GET request (typically POST from a `<Form>`) is made to the route's URL.

**Benefits:**

*   **Server-Side Logic:** Mutation logic runs securely on the server, allowing direct database access or calls to protected backend services.
*   **Progressive Enhancement:** Works seamlessly with standard HTML `<Form>` submissions even if JavaScript fails or is disabled.
*   **Simplified Data Flow:** Remix automatically revalidates data (`loader` functions) after successful actions, ensuring the UI updates.
*   **Feedback Mechanism:** Actions can return data (using `json()`) that components can access via `useActionData` to display success messages or validation errors.
*   **Error Handling:** Errors thrown (or error Responses returned) are caught by the nearest `ErrorBoundary`.

## Implementation

**1. Export `action` Function:**

*   Define and export an `async function action` from your route module (e.g., `app/routes/posts.new.tsx`).
*   **Signature:** `export async function action({ request, params, context }: ActionFunctionArgs) { ... }`
    *   `request`: Standard Fetch API `Request` object. Use `await request.formData()` to access submitted form data.
    *   `params`: Dynamic route segment values.
    *   `context`: App-wide context.
*   **Return Value:**
    *   **Must return a `Response` or `null`.**
    *   Use `json()` to return data (e.g., validation errors, success messages) back to the component via `useActionData`. `return json({ errors: validationErrors });`
    *   Use `redirect()` to navigate the user to a different page after a successful mutation. `return redirect(`/posts/${newPost.id}`);`
    *   Throw a `Response` to trigger the `ErrorBoundary`.

```typescript
// app/routes/posts.new.tsx
import type { ActionFunctionArgs } from "@remix-run/node"; // or adapter
import { json, redirect } from "@remix-run/node"; // or adapter
import { Form, useActionData, useNavigation } from "@remix-run/react";
import invariant from "tiny-invariant";

// Assume db function exists
// import { createPost } from "~/db/posts";

// --- Action ---
// Handles POST requests to /posts/new
export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const title = formData.get("title");
  const body = formData.get("body");

  // Basic server-side validation
  const errors: { title?: string; body?: string } = {};
  if (typeof title !== "string" || title.length < 3) {
    errors.title = "Title must be at least 3 characters long";
  }
  if (typeof body !== "string" || body.length < 10) {
    errors.body = "Body must be at least 10 characters long";
  }

  // If errors, return them via json()
  if (Object.keys(errors).length > 0) {
    return json({ errors }, { status: 400 }); // Bad Request
  }

  // Perform the mutation (e.g., save to database)
  try {
    console.log("Action: Creating post", { title, body });
    // const newPost = await createPost({ title, body });
    const newPost = { id: Date.now().toString(), title, body }; // Placeholder

    // Redirect to the new post's page on success
    return redirect(`/posts/${newPost.id}`);
  } catch (error) {
    console.error("Failed to create post:", error);
    // Return a generic error message or throw for ErrorBoundary
    return json({ errors: { form: "Failed to create post. Please try again." } }, { status: 500 });
  }
}

// --- Default Component ---
export default function NewPostRoute() {
  // Get data returned by the action (e.g., validation errors)
  const actionData = useActionData<typeof action>();
  // Get navigation state for pending UI
  const navigation = useNavigation();
  const isSubmitting = navigation.state === "submitting" && navigation.formData?.get("intent") === "createPost";

  return (
    <div>
      <h2>Create New Post</h2>
      {/* Use Remix <Form> component */}
      <Form method="post"> {/* Defaults to POST to the current route */}
        <input type="hidden" name="intent" value="createPost" /> {/* Optional: Identify action */}
        <div>
          <label> Title: <input type="text" name="title" required /> </label>
          {actionData?.errors?.title && (
            <em style={{ color: 'red' }}>{actionData.errors.title}</em>
          )}
        </div>
        <div>
          <label> Body: <textarea name="body" rows={5} required /> </label>
          {actionData?.errors?.body && (
            <em style={{ color: 'red' }}>{actionData.errors.body}</em>
          )}
        </div>
        {actionData?.errors?.form && (
          <p style={{ color: 'red' }}>{actionData.errors.form}</p>
        )}
        <div>
          <button type="submit" disabled={isSubmitting}>
            {isSubmitting ? "Creating..." : "Create Post"}
          </button>
        </div>
      </Form>
    </div>
  );
}
```

**2. Access Action Data with `useActionData`:**

*   Import `useActionData` from `@remix-run/react`.
*   Call the hook in your route component.
*   It returns the **deserialized data** returned via `json()` from the *most recent* action submission for that route, or `undefined` if no action has run or if the action redirected.
*   Useful for displaying validation errors or success messages directly related to the form submission.
*   TypeScript Tip: Use `typeof action` for type inference: `const actionData = useActionData<typeof action>();`

**3. Tracking Pending States (`useNavigation`):**

*   Import `useNavigation` from `@remix-run/react`.
*   Call the hook: `const navigation = useNavigation();`
*   Check `navigation.state`:
    *   `'idle'`: No navigation/submission active.
    *   `'loading'`: Navigating to a new route, loaders are running.
    *   `'submitting'`: A `<Form>` or `fetcher` is submitting data to an `action`.
*   Check `navigation.formData` during `'submitting'` state to see the data being submitted (useful for disabling specific buttons if multiple forms exist).

The `action` function provides a robust, server-centric way to handle data mutations in Remix, working seamlessly with HTML forms and providing hooks like `useActionData` and `useNavigation` for enhanced client-side feedback.

*(Refer to the official Remix documentation on `action`, `useActionData`, `<Form>`, and `useNavigation`.)*