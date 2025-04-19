# Remix: Client Loader (`clientLoader`, `useClientLoaderData`)

Fetching data on the client-side within Remix routes.

## Core Concept: Client-Side Data Needs

While Remix prioritizes server-side data loading via the `loader` function for the initial request and most navigations, there are scenarios where fetching or preparing data *only* on the client makes sense:

*   **Device-Specific Data:** Accessing browser APIs not available on the server (e.g., `window.matchMedia`, `navigator.geolocation`).
*   **User Preferences (Client-Side):** Reading data stored only in `localStorage`.
*   **Performance Optimization:** Avoiding server execution for data that is cheap to compute/fetch on the client and not needed for the initial server render.
*   **Component-Level Data:** Loading data specific to a component that might not map directly to a route boundary (though `useFetcher` might also be suitable here).

Remix provides the `clientLoader` function and `useClientLoaderData` hook for these client-only data needs.

## Implementation

**1. Export `clientLoader` Function:**

*   Define and export an `async function clientLoader` from your route module.
*   **Execution:** Runs **only on the client-side** during hydration (after initial server render) and during client-side navigations *after* the server `loader` has run (if one exists). It does **not** run on the server.
*   **Signature:** `export async function clientLoader({ request, params, serverLoader }) { ... }`
    *   `request`: Standard Fetch API `Request` object for the current navigation.
    *   `params`: Dynamic route segment values.
    *   `serverLoader`: A function that, when called (`await serverLoader()`), executes the route's `loader` function on the server and returns its data. Useful if client data depends on server data.
*   **Return Value:** Can return any value (including non-serializable data like functions or complex objects, as it doesn't cross the network boundary). Often returns data fetched from browser APIs or `localStorage`.
*   **Error Handling:** Errors thrown are caught by the nearest `ErrorBoundary`.

**2. Access Data with `useClientLoaderData`:**

*   Import `useClientLoaderData` from `@remix-run/react`.
*   Call the hook within your route's default component export.
*   It returns the data returned by the `clientLoader` function.
*   TypeScript Tip: Use `typeof clientLoader` for type inference: `const clientData = useClientLoaderData<typeof clientLoader>();`

## Example

```typescript
// app/routes/settings.tsx
import type { LoaderFunctionArgs, ClientLoaderFunctionArgs } from "@remix-run/node"; // or adapter
import { json } from "@remix-run/node";
import { useLoaderData, useClientLoaderData } from "@remix-run/react";
// import { getUserSettings } from "~/db"; // Server function

// --- Server Loader ---
// Fetches data needed for initial render (SSR)
export async function loader({ request }: LoaderFunctionArgs) {
  // const userId = await requireUserId(request);
  // const settings = await getUserSettings(userId);
  const settings = { theme: 'dark', notifications: true }; // Placeholder
  return json({ settings });
}

// --- Client Loader ---
// Runs only on the client after hydration/navigation
export async function clientLoader({ serverLoader }: ClientLoaderFunctionArgs) {
  console.log("Client Loader Running!");
  // Access server data if needed
  const { settings } = await serverLoader<typeof loader>();

  // Access browser APIs
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const lastVisit = localStorage.getItem('lastVisit');

  // Return client-specific data (can include non-serializable values)
  return {
    prefersReducedMotion,
    lastVisit: lastVisit ? new Date(lastVisit) : null,
    // Combine with server data if needed
    initialTheme: settings.theme,
    logToConsole: () => console.log("Hello from client loader data!"),
  };
}

// --- Default Component ---
export default function SettingsRoute() {
  // Server data is still available via useLoaderData
  const { settings } = useLoaderData<typeof loader>();
  // Client data is available via useClientLoaderData
  const clientData = useClientLoaderData<typeof clientLoader>();

  useEffect(() => {
    // Update localStorage on mount/update (example side effect)
    localStorage.setItem('lastVisit', new Date().toISOString());
    // Call function returned from clientLoader
    clientData?.logToConsole();
  }, [clientData]);

  return (
    <div>
      <h2>Settings</h2>
      <p>Server-loaded Theme: {settings.theme}</p>
      <p>Client-detected Reduced Motion: {clientData?.prefersReducedMotion ? 'Yes' : 'No'}</p>
      <p>Last Visit (from localStorage): {clientData?.lastVisit?.toLocaleString() ?? 'N/A'}</p>
      {/* UI based on combined server and client data */}
    </div>
  );
}

// --- Error Boundary ---
// export function ErrorBoundary() { ... } // Catches errors from both loaders and component
```

## Considerations

*   **Execution Timing:** `clientLoader` runs *after* the server `loader`. Data from `clientLoader` is not available for the initial server render, potentially causing a flicker if the UI depends heavily on it before hydration.
*   **Use Cases:** Best suited for enhancing the UI with client-specific information or capabilities *after* the initial render, or for data that *must* come from the browser environment.
*   **Alternative (`useFetcher`):** For loading data on demand based on user interaction *without* navigation, `useFetcher` might be more appropriate than `clientLoader`.

`clientLoader` provides an escape hatch for accessing client-side information or APIs within Remix's server-centric data loading model, complementing the primary `loader` function.

*(Refer to the official Remix documentation on `clientLoader`.)*