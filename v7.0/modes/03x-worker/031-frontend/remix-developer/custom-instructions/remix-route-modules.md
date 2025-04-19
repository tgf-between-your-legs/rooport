# Remix: Route Modules

Understanding the structure and exports of Remix route files.

## Core Concept: Route Modules

In Remix, each route is typically defined by a single file within the `app/routes/` directory. This file, called a **Route Module**, can export specific functions and a default component that Remix uses to handle different aspects of the route: data loading, data mutations, UI rendering, error handling, and metadata.

**File Naming Convention:**

*   Files map directly to URL paths (e.g., `app/routes/about.tsx` -> `/about`).
*   Index routes use `_index.tsx` (e.g., `app/routes/_index.tsx` -> `/`, `app/routes/dashboard._index.tsx` -> `/dashboard`).
*   Dynamic segments use `$` prefix (e.g., `app/routes/users.$userId.tsx` -> `/users/:userId`).
*   Splats use `$` suffix (e.g., `app/routes/files.$.tsx` -> `/files/*`).
*   See `remix-routing-nested.md` for more details.

## Key Exports from Route Modules

These are the main functions and components you can export from a route module (`.tsx` or `.jsx`):

1.  **`loader` Function (Server-Side):**
    *   **Purpose:** Loads data for the route **on the server** before the component renders. Runs on initial server render and client-side navigations.
    *   **Signature:** `export async function loader({ request, params, context }) { ... }`
    *   Receives `request` (standard Fetch Request object), `params` (dynamic segment values), and `context` (app-wide context, e.g., from adapter).
    *   **Must return:** A `Response` object, often created using Remix helpers like `json()` or `redirect()`.
    *   **Data Access:** Use `useLoaderData()` hook in the component to access the data returned by `json()`.

2.  **`action` Function (Server-Side):**
    *   **Purpose:** Handles data mutations (POST, PUT, PATCH, DELETE requests), typically from form submissions. Runs **only on the server**.
    *   **Signature:** `export async function action({ request, params, context }) { ... }`
    *   Receives `request`, `params`, `context`. Can access form data via `await request.formData()`.
    *   **Must return:** A `Response` (using `json()` or `redirect()`) or `null`.
    *   **Data Access:** Use `useActionData()` hook in the component to access data returned by `json()` from the action *after* a submission.

3.  **`default` Export (Component):**
    *   **Purpose:** The React component that renders the UI for this specific route segment.
    *   **Signature:** `export default function MyRouteComponent() { ... }`
    *   **Data Access:** Uses hooks like `useLoaderData()` and `useActionData()`.
    *   **Nested Routes:** Renders child routes using the `<Outlet />` component from `@remix-run/react`.

4.  **`ErrorBoundary` Component:**
    *   **Purpose:** Catches errors thrown during rendering *or* from the `loader` or `action` functions of *this specific route* and its children *before* parent boundaries. Renders a fallback UI.
    *   **Signature:** `export function ErrorBoundary() { ... }`
    *   **Data Access:** Use `useRouteError()` hook to access the error object.
    *   **Note:** Unlike React's `componentDidCatch`, Remix ErrorBoundaries *do* catch errors from loaders/actions.

5.  **`headers` Function (Server-Side):**
    *   **Purpose:** Set HTTP headers (like `Cache-Control`) for the route's response.
    *   **Signature:** `export function headers({ loaderHeaders, parentHeaders, actionHeaders }) { ... }`
    *   Receives headers objects from the loader, parent routes, and action.
    *   **Must return:** A `Headers` object or plain object literal.

6.  **`meta` Function:**
    *   **Purpose:** Set meta tags (`<title>`, `<meta name="description">`, etc.) for the route. Merged with parent route meta functions.
    *   **Signature:** `export function meta({ data, params, location, matches }) { ... }`
    *   Receives loader `data`, `params`, `location`, and `matches` (info about parent routes).
    *   **Must return:** An object mapping meta tag names/properties to their content.

7.  **`links` Function:**
    *   **Purpose:** Add `<link>` tags (stylesheets, preloads, etc.) to the document `<head>`. Merged with parent route links.
    *   **Signature:** `export function links() { ... }`
    *   **Must return:** An array of link descriptor objects (e.g., `{ rel: 'stylesheet', href: stylesHref }`).

## Example Route Module

```typescript
// app/routes/products.$productId.tsx

import type { LoaderFunctionArgs, ActionFunctionArgs, MetaFunction, LinksFunction } from "@remix-run/node"; // or appropriate adapter
import { json, redirect } from "@remix-run/node"; // or appropriate adapter
import { useLoaderData, useActionData, Form, useNavigation, Outlet, useRouteError, isRouteErrorResponse } from "@remix-run/react";
import invariant from "tiny-invariant";

// Import components, db functions, styles, etc.
// import { getProduct, updateProduct } from "~/db/products";
// import ProductStyles from "~/styles/product.css";
// import ProductDetails from "~/components/ProductDetails";

// --- Links ---
// export const links: LinksFunction = () => [
//   { rel: "stylesheet", href: ProductStyles },
// ];

// --- Meta ---
// export const meta: MetaFunction<typeof loader> = ({ data }) => {
//   return [{ title: data?.product?.name ?? "Product Not Found" }];
// };

// --- Loader ---
export async function loader({ params }: LoaderFunctionArgs) {
  invariant(params.productId, "Missing productId param"); // Ensure param exists
  // const product = await getProduct(params.productId);
  const product = { id: params.productId, name: `Product ${params.productId}` }; // Placeholder
  if (!product) {
    throw new Response("Product Not Found", { status: 404 }); // Throw response for ErrorBoundary
  }
  // Return data using json helper
  return json({ product });
}

// --- Action ---
export async function action({ request, params }: ActionFunctionArgs) {
  invariant(params.productId, "Missing productId param");
  const formData = await request.formData();
  const intent = formData.get("intent");

  if (intent === "updateName") {
    const newName = formData.get("newName") as string;
    // const updatedProduct = await updateProduct(params.productId, { name: newName });
    // return json({ success: true, product: updatedProduct });
    return json({ success: true, message: `Name updated for ${params.productId}` });
  }

  // Handle other intents or throw error
  return json({ success: false, message: "Invalid intent" }, { status: 400 });
}

// --- Headers ---
// export function headers({ loaderHeaders }) {
//   // Example: Cache for 1 hour
//   return { "Cache-Control": "public, max-age=3600" };
// }

// --- Default Component ---
export default function ProductRoute() {
  // Get data returned from loader
  const { product } = useLoaderData<typeof loader>();
  // Get data returned from action (if any)
  const actionData = useActionData<typeof action>();
  // Get navigation state (idle, submitting, loading)
  const navigation = useNavigation();
  const isSubmitting = navigation.state === "submitting";

  return (
    <div>
      {/* <ProductDetails product={product} /> */}
      <h2>Product: {product.name} (ID: {product.id})</h2>

      {actionData?.message && (
        <p style={{ color: actionData.success ? 'green' : 'red' }}>{actionData.message}</p>
      )}

      <Form method="post"> {/* POSTs to the action function */}
        <input type="hidden" name="intent" value="updateName" />
        <label> New Name: <input type="text" name="newName" required /> </label>
        <button type="submit" disabled={isSubmitting}>
          {isSubmitting ? "Updating..." : "Update Name"}
        </button>
      </Form>

      {/* Renders nested routes if any */}
      {/* <Outlet /> */}
    </div>
  );
}

// --- Error Boundary ---
export function ErrorBoundary() {
  const error = useRouteError();

  // Check if it's an error response thrown from loader/action
  if (isRouteErrorResponse(error)) {
    return (
      <div>
        <h1>{error.status} {error.statusText}</h1>
        <p>{error.data}</p>
      </div>
    );
  }

  // Handle other unexpected errors
  const errorMessage = error instanceof Error ? error.message : "Unknown error";
  return (
    <div>
      <h1>Uh oh! An Error Occurred</h1>
      <p>Something went wrong loading this product.</p>
      <pre>{errorMessage}</pre>
    </div>
  );
}
```

Route modules are the core building blocks in Remix, colocating server logic (data loading/mutation) with the client UI component for a specific URL path.

*(Refer to the official Remix documentation on Route Modules.)*