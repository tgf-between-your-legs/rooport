# Error Handling (`ErrorBoundary`, `useRouteError`)

## Core Concept: Route-Level Error Boundaries

Remix uses a special component export, `ErrorBoundary`, within route modules to catch errors that occur during rendering or data loading/mutation for that specific route segment and its children.

**How it Works:**

*   **Catching Errors:** A route's `ErrorBoundary` catches errors that occur:
    *   During the rendering of that route's `Component`.
    *   When an error is **thrown** from that route's `loader` or `action`.
    *   When a `Response` with an error status code (4xx or 5xx) is **thrown** from the `loader` or `action`.
*   **Nearest Boundary:** Errors bubble up and are caught by the *nearest* `ErrorBoundary` defined in the route hierarchy.
*   **UI Replacement:** The `ErrorBoundary` replaces the UI of the component that threw the error (or the component whose loader/action threw). Layouts *above* the boundary remain rendered.

## Implementation

**1. Export `ErrorBoundary` Component:**

*   Define and export a function component named `ErrorBoundary` from your route module.
*   **Access Error:** Use the `useRouteError()` hook inside the `ErrorBoundary` component to get the error object or Response that was thrown.

**2. Use `useRouteError()` Hook:**

*   Import `useRouteError` from `@remix-run/react`.
*   Call it inside your `ErrorBoundary`.
*   Returns the `Error` object or `Response` object caught.
*   Use `isRouteErrorResponse` (from `@remix-run/react`) to check if the caught error is a Response object (e.g., a 404 thrown from a loader).

```typescript
// app/routes/posts.$postId.tsx
import type { LoaderFunctionArgs } from "@remix-run/node";
import { json } from "@remix-run/node";
import { useLoaderData, useRouteError, isRouteErrorResponse, Link } from "@remix-run/react";
import invariant from "tiny-invariant";
// import { getPostById } from "~/db";

export async function loader({ params }: LoaderFunctionArgs) {
  invariant(params.postId, "Expected params.postId");
  // const post = await getPostById(params.postId);
  const post = params.postId === 'exists' ? { id: params.postId, title: `Post ${params.postId}` } : null; // Placeholder

  if (!post) {
    // Throwing a Response triggers the ErrorBoundary
    throw new Response("Post Not Found", { status: 404 });
  }
  return json({ post });
}

export default function PostRoute() {
  const { post } = useLoaderData<typeof loader>();
  // Simulate a rendering error
  // if (post.id === 'error') throw new Error("Render error!");
  return ( <div> <h1>{post.title}</h1> {/* ... */} </div> );
}

// --- Error Boundary ---
export function ErrorBoundary() {
  const error = useRouteError(); // Get the caught error/response

  // Check if it's an error Response (e.g., 404)
  if (isRouteErrorResponse(error)) {
    return (
      <div>
        <h1>{error.status} {error.statusText}</h1>
        <p>{error.data}</p> {/* Access data passed in the Response body */}
        <Link to="/posts">Back to Posts</Link>
      </div>
    );
  }

  // Handle unexpected JavaScript errors
  const errorMessage = error instanceof Error ? error.message : "Unknown error";
  console.error("Route Error Boundary Caught:", error); // Log error

  return (
    <div>
      <h1>Application Error</h1>
      <p>Sorry, something went wrong.</p>
      {/* Avoid raw errors in production */}
      {process.env.NODE_ENV === 'development' && (<pre>{errorMessage}</pre>)}
    </div>
  );
}
```

## Key Considerations

*   **Placement:** Error boundaries catch errors in their segment and *below*. A root error boundary (`app/root.tsx`) acts as a global fallback.
*   **Error Types:**
    *   Use `throw new Response(...)` in loaders/actions for expected errors (e.g., 404). Access via `error.status`, `error.data` using `isRouteErrorResponse`.
    *   Standard JS errors (`throw new Error()` or render errors) are caught as `Error` objects. Access via `error.message`.
*   **User Experience:** Provide clear fallback UIs. Avoid raw stack traces in production.
*   **Logging:** Log errors within the `ErrorBoundary` to a reporting service.

*(Combined from `error-handling.md` and `remix-error-handling.md`)*