# Forms & Mutations (`<Form>`, `useFetcher`)

## Core Concept: Progressive Enhancement & Data Mutations

Remix handles data mutations primarily through HTML `<form>` submissions directed at route `action` functions. It provides components and hooks that build upon this foundation, offering progressive enhancement and ways to manage UI state during submissions.

**Key Tools:**

1.  **`<Form>` Component:**
    *   Import from `@remix-run/react`. Renders HTML `<form>`, enhances for client-side routing.
    *   Handles submission to the correct route `action`.
    *   Supports `method="post"` (default), `put`, `patch`, `delete`.
    *   Triggers full page navigation state updates (data revalidation).
2.  **`useFetcher()` Hook:**
    *   **Purpose:** Communicate with loaders/actions *without* causing full route navigation. Ideal for background submissions (e.g., "add to cart"), component-specific data loading (e.g., typeahead), or submitting to a different route's action.
    *   **Returns:** `fetcher` object with:
        *   `fetcher.Form`: Component like `<Form>`, but submissions managed by this fetcher.
        *   `fetcher.submit(formData, options)`: Programmatically submit.
        *   `fetcher.load(href)`: Programmatically call a `loader`.
        *   `fetcher.state`: `'idle'`, `'loading'`, `'submitting'`.
        *   `fetcher.data`: Data returned from the loader/action called by this fetcher.
        *   `fetcher.formData`: `FormData` during submission.
3.  **`useNavigation()` Hook:**
    *   Provides global info about pending page navigations or `<Form>` submissions (state: `'idle'`, `'loading'`, `'submitting'`). Useful for global loading indicators.
4.  **`useSubmit()` Hook:**
    *   Programmatically submit data, often outside a standard `<Form>`.

## 1. Using `<Form>` for Page Mutations

Use `<Form>` for actions that logically result in a navigation or require full page data revalidation.

```jsx
// app/routes/posts.new.tsx
import { Form, useActionData, useNavigation } from "@remix-run/react";

export default function NewPostRoute() {
  const actionData = useActionData<typeof action>(); // Get validation errors
  const navigation = useNavigation();
  const isSubmitting = navigation.state === "submitting";

  return (
    <Form method="post"> {/* Submits POST to /posts/new action */}
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

Use `useFetcher` for interactions without changing the URL or disrupting page state.

**Example: "Add to Cart" Button**

```jsx
// app/routes/cart.tsx (Defines the action)
import type { ActionFunctionArgs } from "@remix-run/node";
import { json } from "@remix-run/node";
// import { addToCart } from "~/models/cart.server";

export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const productId = formData.get("productId") as string;
  // ... validation and logic ...
  try {
    // await addToCart(request, productId, 1);
    console.log(`Fetcher Action: Adding ${productId} to cart`);
    return json({ success: true, productId });
  } catch (error) {
    return json({ success: false, error: "Failed to add item" }, { status: 500 });
  }
}

// app/components/AddToCartButton.tsx (Uses the fetcher)
import { useFetcher } from "@remix-run/react";

export default function AddToCartButton({ productId }: { productId: string }) {
  const fetcher = useFetcher<typeof action>();
  const isAdding = fetcher.state === "submitting";

  return (
    // fetcher.Form submits to the specified action without navigation
    <fetcher.Form method="post" action="/cart">
      <input type="hidden" name="productId" value={productId} />
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
// export async function loader({ request }: LoaderFunctionArgs) { ... return json({ users }); }

// app/components/UserSearch.tsx
import { useFetcher } from "@remix-run/react";
import { useState, useEffect } from "react";

export default function UserSearch() {
  const fetcher = useFetcher<typeof loader>();
  const [query, setQuery] = useState("");

  useEffect(() => {
    if (!query) return;
    // fetcher.load calls the loader at this path
    fetcher.load(`/api/user-search?q=${encodeURIComponent(query)}`);
  }, [query, fetcher]);

  return (
    <div>
      <input type="search" value={query} onChange={(e) => setQuery(e.target.value)} />
      {fetcher.state === "loading" && <p>Searching...</p>}
      {fetcher.data?.users && ( /* Display fetcher.data.users */ )}
    </div>
  );
}
```

Choose `<Form>` for navigational mutations and `useFetcher` for non-navigational interactions.

*(Combined from `forms-mutations.md` and `remix-forms-fetcher.md`)*