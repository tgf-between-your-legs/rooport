# Remix: Data Flow with `loader` and `useLoaderData`

Fetching data on the server for a route using the `loader` function.

## Core Concept: Server Data Loading

Remix's primary data loading mechanism happens on the server via the `loader` function exported from a route module. This function runs before the component renders, both on the initial server request and during client-side navigations to that route.

**Benefits:**

*   **Server-Side Execution:** Data fetching logic runs securely on the server, allowing direct access to databases or backend services without exposing credentials to the client.
*   **Simplified Data Access:** Fetched data is easily accessible in the component via the `useLoaderData` hook.
*   **Performance:** Data is loaded in parallel with JavaScript module loading during client-side navigation. Remix ensures the component doesn't render until its required data is ready.
*   **Error Handling:** Errors thrown (or Responses returned with error status codes) in the `loader` are automatically caught by the nearest `ErrorBoundary`.

## Implementation

**1. Export `loader` Function:**

*   Define and export an `async function loader` from your route module (e.g., `app/routes/posts.tsx`).
*   **Signature:** `export async function loader({ request, params, context }: LoaderFunctionArgs) { ... }`
    *   `request`: Standard Fetch API `Request` object for the incoming request. Useful for reading headers, cookies (via `request.headers.get('Cookie')`), or URL parameters.
    *   `params`: An object containing values from dynamic route segments (e.g., `params.postId` for `app/routes/posts.$postId.tsx`).
    *   `context`: App-wide context provided by the Remix adapter (e.g., environment variables, services).
*   **Return Value:**
    *   **Must return a `Response` object.**
    *   Use the `json()` helper function (from `@remix-run/node` or your adapter) to easily return JSON data with the correct `Content-Type` header. `return json({ data });`
    *   Can also return `redirect()` (from `@remix-run/node` or adapter) to redirect the user. `return redirect('/login');`
    *   Can throw a `Response` (e.g., `throw new Response("Not Found", { status: 404 });`) to trigger the `ErrorBoundary`.

```typescript
// app/routes/posts.$postId.tsx
import type { LoaderFunctionArgs } from "@remix-run/node"; // or cloudflare/server-runtime
import { json, redirect } from "@remix-run/node"; // or cloudflare/server-runtime
import invariant from "tiny-invariant"; // Helper for asserting values

// Assume db function exists
// import { getPostById, getUserSession } from "~/db";

export async function loader({ request, params, context }: LoaderFunctionArgs) {
  // Check user session (example)
  // const session = await getUserSession(request.headers.get("Cookie"));
  // if (!session.has("userId")) {
  //   // Redirect to login if not authenticated
  //   return redirect("/login");
  // }

  // Validate/assert dynamic params
  invariant(params.postId, "Expected params.postId");

  console.log(`Loader: Fetching post ${params.postId}`);
  // Fetch data from database or API on the server
  // const post = await getPostById(params.postId);
  const post = { id: params.postId, title: `Post ${params.postId}`, body: "..." }; // Placeholder

  // Throw a 404 response if post not found
  if (!post) {
    throw new Response("Post Not Found", { status: 404 });
  }

  // Return data serialized as JSON
  // This data will be available via useLoaderData()
  return json({ post });
}

// ... rest of the route module (Component, ErrorBoundary, etc.)
```

**2. Access Data with `useLoaderData`:**

*   Import `useLoaderData` from `@remix-run/react`.
*   Call the hook within your route's default component export.
*   It returns the **deserialized data** that was returned from the `loader` function using `json()`.
*   TypeScript Tip: Use `typeof loader` with `useLoaderData` for type inference: `const { post } = useLoaderData<typeof loader>();`

```typescript
// app/routes/posts.$postId.tsx
// ... (imports including loader, json, useLoaderData)

// ... loader function defined above ...

// --- Default Component ---
export default function PostRoute() {
  // Use the hook to get the data returned by the loader
  const { post } = useLoaderData<typeof loader>();

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
      {/* Render other parts of the UI */}
    </div>
  );
}

// --- Error Boundary ---
// ... (ErrorBoundary to handle errors from loader, like the 404) ...
```

The `loader` function is Remix's fundamental pattern for loading data required by a route before rendering, ensuring data is fetched server-side and seamlessly provided to your component via the `useLoaderData` hook.

*(Refer to the official Remix documentation on `loader` and `useLoaderData`.)*