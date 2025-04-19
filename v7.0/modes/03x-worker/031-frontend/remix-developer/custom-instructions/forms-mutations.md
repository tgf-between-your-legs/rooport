# Remix Forms & Mutations

Handling data mutations (POST, PUT, DELETE) using Remix's built-in form handling and progressive enhancement features.

## Core Concept: Progressive Enhancement

Remix forms work even if JavaScript is disabled or fails to load. The browser performs a full-page navigation and form submission. When JavaScript loads, Remix hijacks the form submission, performs it via `fetch` in the background, revalidates data by calling loaders, and updates the UI without a full page refresh.

## 1. `<Form>` Component

*   **Purpose:** The primary way to trigger data mutations (`action` functions). Renders a standard HTML `<form>` but adds progressive enhancement.
*   **Usage:** Import from `@remix-run/react`. Use standard HTML form elements (`<input>`, `<textarea>`, `<button type="submit">`).
*   **`method` Prop:** Specify the HTTP method (`post`, `put`, `delete`, `patch`). Defaults to `GET` if omitted (which calls the `loader`, not the `action`).
*   **`action` Prop (Optional):** Specify a different route URL to send the submission to. Defaults to the current route.
    ```tsx
    // app/routes/new-item.tsx
    import { Form } from "@remix-run/react";
    import { ActionFunctionArgs, json, redirect } from "@remix-run/node";

    export async function action({ request }: ActionFunctionArgs) {
      const formData = await request.formData();
      const itemName = formData.get("itemName") as string;
      // TODO: Validate itemName
      // TODO: Save item to database
      console.log("Creating item:", itemName);
      // Redirect after successful creation
      return redirect("/items");
    }

    export default function NewItemRoute() {
      return (
        <div>
          <h2>Create New Item</h2>
          {/* Submits POST request to the current route's action */}
          <Form method="post">
            <label>
              Item Name:
              <input type="text" name="itemName" required />
            </label>
            <button type="submit">Create</button>
          </Form>
        </div>
      );
    }
    ```

## 2. `useNavigation()` Hook

*   **Purpose:** Provides information about pending navigations or form submissions initiated by Remix (`<Link>`, `<Form>`, `useSubmit`, `fetcher.load`, `fetcher.submit`).
*   **Returns:** An object with properties:
    *   `state`: `'idle' | 'submitting' | 'loading'` (Indicates if a loader is running or an action is submitting).
    *   `formData`: The `FormData` object being submitted (if `state` is 'submitting').
    *   `location`: The target location of the navigation (if `state` is 'loading').
*   **Use Case:** Disabling forms during submission, showing loading indicators.
    ```tsx
    import { useNavigation } from "@remix-run/react";
    // ... inside component ...
    const navigation = useNavigation();
    const isSubmitting = navigation.state === "submitting";
    // const isLoadingData = navigation.state === "loading";

    return (
      <Form method="post">
        {/* ... form inputs ... */}
        <button type="submit" disabled={isSubmitting}>
          {isSubmitting ? "Saving..." : "Save"}
        </button>
      </Form>
    );
    ```

## 3. `useActionData<typeof action>()` Hook

*   **Purpose:** Accesses the data returned from the most recent `action` function call for the current route *after* a non-redirecting submission.
*   **Returns:** The JSON data returned by the `action`, or `undefined` if there hasn't been an action submission or if the action redirected.
*   **Use Case:** Displaying validation errors or success messages returned from the `action`.
    ```tsx
    // In the component part of app/routes/comments.tsx from data-flow.md example
    import { useActionData } from "@remix-run/react";
    // ...
    const actionData = useActionData<typeof action>();
    // ...
    {actionData?.error && <p style={{ color: 'red' }}>Error: {actionData.error}</p>}
    ```

## 4. `useFetcher()` Hook ("Fetcher Form")

*   **Purpose:** Allows components to communicate with loaders and actions (load data or submit mutations) **without** causing a full route navigation. Useful for interactions that update parts of a page without changing the URL (e.g., adding to cart, liking a post, fetching data for autocomplete).
*   **Syntax:** `const fetcher = useFetcher();`
*   **Returns:** An object with:
    *   `fetcher.Form`: A component similar to `<Form>`, but submissions update the `fetcher` state instead of causing navigation.
    *   `fetcher.submit(formData, options)`: Programmatically submit data.
    *   `fetcher.load(href)`: Programmatically call a `loader` from a different route.
    *   `fetcher.data`: Data returned from the `loader` (via `fetcher.load`) or `action` (via `fetcher.Form`/`fetcher.submit`).
    *   `fetcher.state`: `'idle' | 'submitting' | 'loading'`.
    *   `fetcher.formData`: The submitted data during submission.
*   **Example (Liking a Post):**
    ```tsx
    // app/components/LikeButton.tsx
    import { useFetcher } from "@remix-run/react";

    export function LikeButton({ postId, initialLikes, isLiked }) {
      const fetcher = useFetcher();
      const optimisticLiked = fetcher.formData?.get("intent") === "like";
      const optimisticUnlike = fetcher.formData?.get("intent") === "unlike";

      // Determine current state considering optimistic updates
      const currentLiked = optimisticLiked ? true : (optimisticUnlike ? false : isLiked);
      // You might also optimistically update the like count

      return (
        // fetcher.Form submits to the action of the route where it's rendered,
        // or specify a different action URL: <fetcher.Form method="post" action="/api/likes">
        <fetcher.Form method="post">
          <input type="hidden" name="postId" value={postId} />
          <button
            type="submit"
            name="intent"
            value={currentLiked ? "unlike" : "like"}
            disabled={fetcher.state !== 'idle'}
          >
            {currentLiked ? "Unlike" : "Like"} ({initialLikes}) {/* Display initial count, update via loader data */}
          </button>
        </fetcher.Form>
      );
    }

    // In app/routes/some-route.tsx (where LikeButton is used)
    export async function action({ request }: ActionFunctionArgs) {
        const formData = await request.formData();
        const intent = formData.get("intent");
        const postId = formData.get("postId");
        // TODO: Update like status in DB based on intent and postId
        // Return null or json({ success: true }) - no redirect needed
        return null;
    }
    ```

*(Refer to the official Remix documentation on Forms, Mutations, and Fetchers: https://remix.run/docs/en/main/guides/data-writes)*