# Data Flow: `loader` & `useLoaderData`

## Core Concept: Server Data Loading

Remix's primary data loading mechanism happens on the server via the `loader` function exported from a route module. This function runs before the component renders, both on the initial server request and during client-side navigations to that route.

**Benefits:**

*   **Server-Side Execution:** Data fetching logic runs securely on the server.
*   **Simplified Data Access:** Fetched data is easily accessible via `useLoaderData`.
*   **Performance:** Data loaded in parallel with JS modules during client navigation.
*   **Error Handling:** Errors thrown are caught by the nearest `ErrorBoundary`.

## Implementation

**1. Export `loader` Function:**

*   Define and export an `async function loader` from your route module.
*   **Signature:** `export async function loader({ request, params, context }: LoaderFunctionArgs) { ... }`
    *   `request`: Standard Fetch API `Request` object.
    *   `params`: Dynamic route segment values.
    *   `context`: App-wide context.
*   **Return Value:**
    *   **Must return a `Response` object.**
    *   Use `json()` helper (from `@remix-run/node` or adapter) for JSON data. `return json({ data });`
    *   Use `redirect()` helper for redirects. `return redirect('/login');`
    *   Can `throw new Response(...)` to trigger `ErrorBoundary`.

```typescript
// app/routes/posts.$postId.tsx
import type { LoaderFunctionArgs } from "@remix-run/node";
import { json, redirect } from "@remix-run/node";
import invariant from "tiny-invariant";
// import { getPostById, getUserSession } from "~/db";

export async function loader({ request, params, context }: LoaderFunctionArgs) {
  // const session = await getUserSession(request.headers.get("Cookie"));
  // if (!session.has("userId")) return redirect("/login");

  invariant(params.postId, "Expected params.postId");
  console.log(`Loader: Fetching post ${params.postId}`);
  // const post = await getPostById(params.postId);
  const post = { id: params.postId, title: `Post ${params.postId}`, body: "..." }; // Placeholder

  if (!post) {
    throw new Response("Post Not Found", { status: 404 });
  }
  return json({ post });
}
```

**2. Access Data with `useLoaderData`:**

*   Import `useLoaderData` from `@remix-run/react`.
*   Call the hook within your route's default component.
*   Returns the **deserialized data** returned from the `loader` via `json()`.
*   TypeScript Tip: `const { post } = useLoaderData<typeof loader>();`

```typescript
// app/routes/posts.$postId.tsx
import { useLoaderData } from "@remix-run/react";
// ... loader function defined above ...

export default function PostRoute() {
  const { post } = useLoaderData<typeof loader>();
  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </div>
  );
}
```

*(Derived from `remix-data-flow-loader.md`)*