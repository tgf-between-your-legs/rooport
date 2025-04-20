# Remix: Forms (`<Form>`) and Fetchers (`useFetcher`)

Handling data mutations and background data loading/mutations in Remix.

## Core Concept: Progressive Enhancement & Data Mutations

Remix handles data mutations primarily through HTML `<form>` submissions directed at route `action` functions. It provides components and hooks that build upon this foundation, offering progressive enhancement (works without JavaScript) and ways to manage UI state during submissions.

**Key Tools:**

1.  **`<Form>` Component:**
    *   Import from `@remix-run/react`.
    *   Renders a standard HTML `<form>` but enhances it for client-side routing and state management.
    *   Handles serialization and submission to the correct route `action` (defaults to the current route, can be changed with `action="/other/route"` prop).
    *   Supports `method="post"` (default), `method="put"`, `method="patch"`, `method="delete"`.
    *   Triggers full page navigation state updates (data revalidation, UI updates).
2.  **`useFetcher()` Hook:**
    *   **Purpose:** Allows components to communicate with loaders and actions *without* causing a full route navigation. Ideal for:
        *   Submitting data in the background (e.g., "add to cart", "like" button).
        *   Loading data for a specific component based on user interaction (e.g., typeahead suggestions).
        *   Submitting to a *different* route's action than the current one.
    *   **Returns:** An object (`fetcher`) with:
        *   `fetcher.Form`: A component similar to `<Form>`, but submissions managed by this fetcher instance.
        *   `fetcher.submit(formData, options)`: Programmatically submit data.
        *   `fetcher.load(href)`: Programmatically call a `loader` function from a different route.
        *   `fetcher.state`: `'idle'`, `'loading'` (calling a loader), or `'submitting'` (calling an action).
        *   `fetcher.data`: Data returned via `json()` from the loader or action called by this fetcher.
        *   `fetcher.formData`: The `FormData` object during submission.
3.  **`useNavigation()` Hook:**
    *   Provides global information about pending page navigations or `<Form>` submissions (state: `'idle'`, `'loading'`, `'submitting'`). Useful for global loading indicators or disabling forms during submission.
4.  **`useSubmit()` Hook:**
    *   Programmatically submit data using a specific HTTP method, often used outside of a standard `<Form>`.

## 1. Using `<Form>` for Page Mutations

Use `<Form>` for actions that logically result in a navigation or require full page data revalidation (e.g., creating a new resource and redirecting to it, deleting an item from a list).

```jsx
// app/routes/posts.new.tsx (See remix-data-flow-action.md for full example)
import { Form, useActionData, useNavigation } from "@remix-run/react";

export default function NewPostRoute() {
  const actionData = useActionData<typeof action>();
  const navigation = useNavigation();
  // Check if THIS form is submitting (useful if multiple forms exist)
  const isSubmitting = navigation.state === "submitting" &&
                       navigation.formData?.get("intent") === "createPost";

  return (
    <Form method="post"> {/* Submits POST to /posts/new action */}
      <input type="hidden" name="intent" value="createPost" />
      {/* ... form fields ... */}
      {actionData?.errors?.title && <span>{actionData.errors.title}</span>}
      {/* ... other fields and errors ... */}
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? "Creating..." : "Create Post"}
      </button>
    </Form>
  );
}
```

## 2. Using `useFetcher()` for Background Actions/Loads

Use `useFetcher` when you want to interact with an `action` or `loader` without changing the URL or disrupting the current page's state significantly.

**Example: "Add to Cart" Button**

```jsx
// app/routes/cart.tsx (Defines the action)
import type { ActionFunctionArgs } from "@remix-run/node";
import { json } from "@remix-run/node";
// import { addToCart } from "~/models/cart.server";

export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const productId = formData.get("productId") as string;
  const quantity = Number(formData.get("quantity") || 1);

  if (!productId) {
    return json({ success: false, error: "Missing product ID" }, { status: 400 });
  }

  try {
    // await addToCart(request, productId, quantity);
    console.log(`Fetcher Action: Adding ${quantity} of ${productId} to cart`);
    return json({ success: true, productId });
  } catch (error) {
    return json({ success: false, error: "Failed to add item" }, { status: 500 });
  }
}

// app/components/AddToCartButton.tsx (Uses the fetcher)
import { useFetcher } from "@remix-run/react";
import { useEffect } from "react";

export default function AddToCartButton({ productId }: { productId: string }) {
  const fetcher = useFetcher<typeof action>(); // Typed fetcher (optional)

  const isAdding = fetcher.state === "submitting" &&
                   fetcher.formData?.get("productId") === productId;

  // Optional: Show feedback based on fetcher.data
  useEffect(() => {
    if (fetcher.data && fetcher.data.success === true && fetcher.state === 'idle') {
      alert(`Product ${fetcher.data.productId} added!`);
    } else if (fetcher.data && fetcher.data.success === false) {
       alert(`Error: ${fetcher.data.error}`);
    }
  }, [fetcher.data, fetcher.state]);

  return (
    // fetcher.Form submits to the specified action without navigation
    <fetcher.Form method="post" action="/cart"> {/* Target the cart action */}
      <input type="hidden" name="productId" value={productId} />
      <input type="hidden" name="quantity" value="1" />
      <button type="submit" disabled={isAdding}>
        {isAdding ? "Adding..." : "Add to Cart"}
      </button>
    </fetcher.Form>
  );
}
```

**Example: Loading Data with Fetcher**

```jsx
// app/routes/api.user-search.ts (Loader for search)
// export async function loader({ request }: LoaderFunctionArgs) {
//   const url = new URL(request.url);
//   const query = url.searchParams.get("q");
//   const users = await searchUsers(query);
//   return json({ users });
// }

// app/components/UserSearch.tsx
import { useFetcher } from "@remix-run/react";
import { useState, useEffect } from "react";

export default function UserSearch() {
  const fetcher = useFetcher<typeof loader>(); // Type from the loader
  const [query, setQuery] = useState("");

  // Trigger fetcher.load when query changes (debounced ideally)
  useEffect(() => {
    if (!query) return;
    // fetcher.load calls the loader at this path
    fetcher.load(`/api/user-search?q=${encodeURIComponent(query)}`);
  }, [query, fetcher]); // Include fetcher in deps

  const isLoading = fetcher.state === "loading";

  return (
    <div>
      <input
        type="search"
        placeholder="Search users..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      {isLoading && <p>Searching...</p>}
      {fetcher.data?.users && (
        <ul>
          {fetcher.data.users.map((user: any) => (
            <li key={user.id}>{user.name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
```

Choose `<Form>` for navigational mutations and `useFetcher` for non-navigational data interactions or loading component-specific data. Both leverage Remix's server-centric data flow and progressive enhancement.

*(Refer to the official Remix documentation on `<Form>`, `useFetcher`, `useNavigation`, `useSubmit`.)*