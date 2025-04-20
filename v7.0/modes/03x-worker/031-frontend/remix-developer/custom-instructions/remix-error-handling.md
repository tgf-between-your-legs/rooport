# Remix: Error Handling (`ErrorBoundary`, `useRouteError`)

Catching and handling errors gracefully in Remix applications.

## Core Concept: Route-Level Error Boundaries

Remix has a built-in error handling mechanism based on React Error Boundaries, but specifically tailored for its route modules. Each route can export an `ErrorBoundary` component.

**How it Works:**

*   **Catching Errors:** A route's `ErrorBoundary` catches errors that occur:
    *   During the rendering of that route's **`Component`**.
    *   When an error is **thrown** from that route's **`loader`** or **`action`** function.
    *   When a `Response` with an error status code (4xx or 5xx) is **thrown** from the `loader` or `action`.
*   **Nearest Boundary:** Errors bubble up and are caught by the *nearest* `ErrorBoundary` defined in the route hierarchy (including parent layout routes). If no custom boundary is found, Remix provides a default error screen.
*   **UI Replacement:** The `ErrorBoundary` replaces the UI of the component that threw the error (or the component whose loader/action threw). Layouts *above* the boundary remain rendered and interactive.

## Implementation

**1. Export `ErrorBoundary` Component:**

*   Define and export a function component named `ErrorBoundary` from your route module.
*   **No Props:** Unlike class component error boundaries, Remix's `ErrorBoundary` does not receive `error` or `reset` as props directly.
*   **Access Error:** Use the `useRouteError()` hook inside the `ErrorBoundary` component to get the error object or Response that was thrown.

**2. Use `useRouteError()` Hook:**

*   Import `useRouteError` from `@remix-run/react`.
*   Call it inside your `ErrorBoundary` component.
*   It returns the `Error` object or `Response` object that was caught.
*   Use `isRouteErrorResponse` (from `@remix-run/react`) to check if the caught error is a Response object (e.g., a 404 thrown from a loader).

```typescript
// app/routes/posts.$postId.tsx
import type { LoaderFunctionArgs } from "@remix-run/node";
import { json } from "@remix-run/node";
import { useLoaderData, useRouteError, isRouteErrorResponse, Link } from "@remix-run/react";
import invariant from "tiny-invariant";

// Assume db function exists
// import { getPostById } from "~/db";

export async function loader({ params }: LoaderFunctionArgs) {
  invariant(params.postId, "Expected params.postId");
  // const post = await getPostById(params.postId);
  const post = params.postId === 'exists' ? { id: params.postId, title: `Post ${params.postId}` } : null; // Placeholder

  if (!post) {
    // Throwing a Response triggers the ErrorBoundary with status info
    throw new Response("Post Not Found", { status: 404 });
  }
  return json({ post });
}

export default function PostRoute() {
  const { post } = useLoaderData<typeof loader>();

  // Simulate a rendering error for demonstration
  // if (post.id === 'error') {
  //   throw new Error("Oh no! Something broke during render.");
  // }

  return (
    <div>
      <h1>{post.title}</h1>
      {/* ... post content ... */}
    </div>
  );
}

// --- Error Boundary ---
// Catches errors from loader, action (if defined), and component render
export function ErrorBoundary() {
  const error = useRouteError(); // Get the caught error/response

  // Check if it's an error Response (e.g., 404)
  if (isRouteErrorResponse(error)) {
    if (error.status === 404) {
      return (
        <div>
          <h1>Post Not Found</h1>
          <p>Sorry, we couldn't find the post you were looking for (Status: {error.status}).</p>
          <Link to="/posts">Back to Posts</Link>
        </div>
      );
    }

    // Handle other specific status codes if needed
    return (
      <div>
        <h1>{error.status} {error.statusText}</h1>
        <p>Something went wrong processing your request.</p>
        <pre>{error.data}</pre> {/* Display data returned in the thrown Response */}
      </div>
    );
  }

  // Handle unexpected JavaScript errors (e.g., from rendering)
  const errorMessage = error instanceof Error ? error.message : "Unknown error";
  // Log the error server-side or to an error reporting service
  console.error("Route Error Boundary Caught:", error);

  return (
    <div>
      <h1>Application Error</h1>
      <p>Sorry, something went wrong.</p>
      {/* Avoid displaying raw error messages in production */}
      {process.env.NODE_ENV === 'development' && (
        <pre style={{ color: 'red' }}>{errorMessage}</pre>
      )}
    </div>
  );
}
```

## Root Error Boundary

You can define an `ErrorBoundary` in your root route (`app/root.tsx`) to catch any errors not handled by more specific boundaries lower down the tree. This acts as a global fallback.

Remix's built-in `ErrorBoundary` convention provides a robust and granular way to handle errors originating from data loading, mutations, or rendering within specific route segments, preventing full application crashes and allowing for user-friendly fallback UIs.

*(Refer to the official Remix documentation on Error Handling and `ErrorBoundary`.)*