# Remix Error Handling (`ErrorBoundary`)

Catching and handling errors gracefully in Remix applications.

## Core Concept: Route `ErrorBoundary`

Remix uses a special component export, `ErrorBoundary`, within route modules to catch errors that occur during rendering or data loading/mutation for that specific route segment and its children. This allows for granular error handling and prevents a single error from crashing the entire application.

## How it Works

1.  **Error Occurs:** An error is thrown during:
    *   Rendering the route's `Component`.
    *   Executing the route's `loader` function (e.g., data fetch fails, `throw new Response(...)` is used).
    *   Executing the route's `action` function (e.g., mutation fails, `throw new Response(...)` is used).
2.  **Boundary Search:** Remix looks for the nearest `ErrorBoundary` component defined in the route hierarchy (starting from the route where the error occurred and moving up towards the root).
3.  **Fallback UI Render:** The identified `ErrorBoundary` component is rendered instead of the regular `Component`.
4.  **`useRouteError()` Hook:** Inside the `ErrorBoundary`, use the `useRouteError` hook to access the error object that was caught.

## Implementation

*   Export a component named `ErrorBoundary` from your route module (`app/routes/some-route.tsx`).
*   Use the `useRouteError` hook from `@remix-run/react` inside the `ErrorBoundary` to get error details.
*   Check the error type (e.g., using `isRouteErrorResponse` for errors thrown via `throw new Response(...)`) to display appropriate messages.

```typescript
// app/routes/posts.$postId.tsx
import {
  json,
  LoaderFunctionArgs,
  isRouteErrorResponse, // Helper to check error type
  useRouteError,        // Hook to access the error
  useLoaderData
} from "@remix-run/react";
// import { db } from "~/utils/db.server";

export async function loader({ params }: LoaderFunctionArgs) {
  const postId = params.postId;
  // const post = await db.post.findUnique({ where: { id: postId } });
  const post = postId === 'exists' ? { id: postId, title: `Post ${postId}` } : null; // Placeholder

  if (!post) {
    // Throwing a Response triggers the ErrorBoundary with status info
    throw new Response("Post Not Found", { status: 404 });
  }
  // Example of throwing a standard Error (less common from loader/action)
  // if (someOtherCondition) {
  //   throw new Error("Something else went wrong during loading");
  // }
  return json({ post });
}

export default function PostRoute() {
  const { post } = useLoaderData<typeof loader>();
  return (
    <article>
      <h1>{post.title}</h1>
      {/* Component might throw an error during render */}
      {/* <PotentiallyBuggyComponent data={post.body} /> */}
      <p>{post.body}</p>
    </article>
  );
}

// ErrorBoundary catches errors from loader, action, and component render
export function ErrorBoundary() {
  const error = useRouteError(); // Get the caught error

  // Check if it's an error response thrown from loader/action
  if (isRouteErrorResponse(error)) {
    return (
      <div>
        <h1>{error.status} {error.statusText}</h1>
        <p>{error.data}</p> {/* Access data passed in the Response body */}
      </div>
    );
  }

  // Handle other JavaScript errors (e.g., from component render)
  let errorMessage = "Unknown error";
  if (error instanceof Error) {
    errorMessage = error.message;
  }

  return (
    <div>
      <h1>Uh oh...</h1>
      <p>Something went wrong rendering this post.</p>
      <pre>{errorMessage}</pre> {/* Display error message (consider for dev only) */}
    </div>
  );
}
```

## Key Considerations

*   **Placement:** Error boundaries catch errors in their segment and *below*. Place them strategically. A root error boundary (`app/root.tsx`) can catch errors not handled by nested boundaries.
*   **Error Types:**
    *   Use `throw new Response("Not Found", { status: 404 })` in loaders/actions for expected errors like "not found". Access status and data via `error.status` and `error.data` in the boundary using `isRouteErrorResponse`.
    *   Standard JavaScript errors (`throw new Error(...)` or runtime errors during render) are caught as `Error` objects. Access message via `error.message`.
*   **User Experience:** Provide clear, user-friendly fallback UIs. Avoid showing raw stack traces in production. Include options to retry or navigate elsewhere.
*   **Logging:** Use the `ErrorBoundary` (or `componentDidCatch` if using a class component, though functional is preferred) to log errors to a reporting service.

*(Refer to the official Remix Error Handling documentation: https://remix.run/docs/en/main/route/error-boundary)*