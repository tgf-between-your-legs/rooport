# Remix Data Flow: `loader` & `action`

Understanding how data is loaded and mutated in Remix route modules.

## Core Concept: Server/Client Colocation

Remix allows you to define both the server-side data logic (`loader`, `action`) and the client-side UI rendering (`Component`) within the same route module file (e.g., `app/routes/my-route.tsx`). Remix handles separating the server code so it's never sent to the browser.

## 1. `loader` Function (Data Loading)

*   **Purpose:** Runs **only on the server** before the route component renders (both on initial server render and client-side navigations). Used to fetch data required by the component.
*   **Syntax:** Export an `async` function named `loader`. It receives an object containing `request` (standard Fetch Request object) and `params` (dynamic route parameters).
*   **Return Value:** Must return data (often using the `json()` helper from `@remix-run/node` or your adapter) or a `Response` object (e.g., for redirects). The returned data is made available to the component via the `useLoaderData` hook.
*   **Caching:** Control HTTP caching by exporting a `headers` function from the route module.
    ```typescript
    // app/routes/posts.$postId.tsx
    import { json, LoaderFunctionArgs } from "@remix-run/node"; // or cloudflare, deno
    import { useLoaderData } from "@remix-run/react";
    // import { db } from "~/utils/db.server"; // Example DB import

    // Loader runs on the server
    export async function loader({ params, request }: LoaderFunctionArgs) {
      console.log("Loader running on server...");
      const postId = params.postId;
      // TODO: Fetch post from database based on postId
      // const post = await db.post.findUnique({ where: { id: postId } });
      const post = { id: postId, title: `Post ${postId}`, body: "Content..." }; // Placeholder

      if (!post) {
        // Throwing a Response triggers the nearest ErrorBoundary
        throw new Response("Post Not Found", { status: 404 });
      }

      // Return data as JSON
      return json({ post });
      // Or return a standard Response: return new Response(JSON.stringify({ post }), { headers: { 'Content-Type': 'application/json' } });
    }

    // Component runs on the client (and server for initial render)
    export default function PostRoute() {
      // Access loader data via hook
      const { post } = useLoaderData<typeof loader>();

      return (
        <article>
          <h1>{post.title}</h1>
          <p>{post.body}</p>
        </article>
      );
    }

    // Optional: Define caching headers
    export function headers({ loaderHeaders }: { loaderHeaders: Headers }) {
        return {
            "Cache-Control": loaderHeaders.get("Cache-Control") ?? "public, max-age=60", // Example: Cache for 60s
        };
    }
    ```

## 2. `action` Function (Data Mutations)

*   **Purpose:** Runs **only on the server** when a non-GET request (POST, PUT, DELETE, PATCH) is made to the route, typically via a Remix `<Form>` submission. Used to handle data mutations (creating, updating, deleting data).
*   **Syntax:** Export an `async` function named `action`. It receives `request` and `params` similar to the `loader`.
*   **Return Value:** Can return data (using `json()`), a `Response` (e.g., `redirect()` from `@remix-run/node`), or `null`. Returned data is accessible via the `useActionData` hook. Actions typically trigger loaders to re-run after completion to fetch updated data.
    ```typescript
    // app/routes/comments.tsx
    import { json, redirect, ActionFunctionArgs } from "@remix-run/node";
    import { Form, useActionData, useNavigation } from "@remix-run/react";
    // import { db } from "~/utils/db.server";

    // Action runs on the server for POST requests
    export async function action({ request }: ActionFunctionArgs) {
      console.log("Action running on server...");
      const formData = await request.formData();
      const comment = formData.get("comment") as string;
      const author = formData.get("author") as string;

      // TODO: Validate data
      if (!comment || !author) {
        return json({ error: "Comment and author are required." }, { status: 400 });
      }

      // TODO: Save comment to database
      // await db.comment.create({ data: { text: comment, author } });
      console.log("Saving comment:", { comment, author });

      // Option 1: Redirect after successful action
      // return redirect("/comments");

      // Option 2: Return success message (or created data)
      return json({ success: true, message: "Comment added!" });
    }

    // Component
    export default function CommentsRoute() {
      // Access data returned from the action (if any)
      const actionData = useActionData<typeof action>();
      const navigation = useNavigation(); // Get form submission state
      const isSubmitting = navigation.state === "submitting";

      return (
        <div>
          <h2>Add Comment</h2>
          {/* Remix Form handles submission to the action */}
          <Form method="post"> {/* Default method is POST */}
            <input type="text" name="author" placeholder="Your Name" required />
            <textarea name="comment" placeholder="Your Comment" required />
            <button type="submit" disabled={isSubmitting}>
              {isSubmitting ? "Adding..." : "Add Comment"}
            </button>
          </Form>

          {/* Display action results */}
          {actionData?.error && <p style={{ color: 'red' }}>Error: {actionData.error}</p>}
          {actionData?.success && <p style={{ color: 'green' }}>{actionData.message}</p>}

          {/* ... display existing comments (loaded via loader) ... */}
        </div>
      );
    }
    ```

## Data Flow Summary

1.  **Navigation/Load:** User navigates to a route.
2.  **`loader` Runs (Server):** The `loader` function for the matching route (and parent routes) executes on the server, fetching necessary data.
3.  **Component Renders:** The route `Component` renders (initially on the server, then potentially hydrates on the client).
4.  **`useLoaderData`:** The component accesses the data returned by its corresponding `loader` via `useLoaderData`.
5.  **Mutation (e.g., Form Submit):** User submits a `<Form method="post">`.
6.  **`action` Runs (Server):** The `action` function for the route executes on the server, handling the form data and performing the mutation.
7.  **`action` Returns:** The `action` returns a `Response` (e.g., redirect) or JSON data.
8.  **Loaders Re-run:** After the action completes successfully (and doesn't redirect), Remix automatically re-runs the loaders for the current page to fetch fresh data reflecting the mutation.
9.  **Component Re-renders:** The component re-renders with the updated loader data.
10. **`useActionData`:** If the action returned JSON data, it's accessible via `useActionData` during the re-render triggered by the action completion (before loaders re-run).

*(Refer to the official Remix Data Flow documentation: https://remix.run/docs/en/main/discussion/data-flow)*