# Client Loader (`clientLoader`, `useClientLoaderData`)

## Core Concept: Client-Side Data Needs

While Remix prioritizes server-side data loading (`loader`), `clientLoader` allows fetching or preparing data *only* on the client-side.

**Use Cases:**

*   **Device-Specific Data:** Accessing browser APIs (`window.matchMedia`, `navigator.geolocation`).
*   **User Preferences (Client-Side):** Reading from `localStorage`.
*   **Performance Optimization:** Avoiding server execution for cheap client-side computation/fetching not needed for initial render.

## Implementation

**1. Export `clientLoader` Function:**

*   Define and export `async function clientLoader` from your route module.
*   **Execution:** Runs **only on the client** during hydration and client-side navigations *after* the server `loader` (if one exists). Does **not** run on the server.
*   **Signature:** `export async function clientLoader({ request, params, serverLoader }: ClientLoaderFunctionArgs) { ... }`
    *   `request`: Standard Fetch `Request`.
    *   `params`: Dynamic route parameters.
    *   `serverLoader`: Function to call the route's server `loader` (`await serverLoader()`).
*   **Return Value:** Can return any value (including non-serializable data).
*   **Error Handling:** Errors caught by nearest `ErrorBoundary`.

**2. Access Data with `useClientLoaderData`:**

*   Import `useClientLoaderData` from `@remix-run/react`.
*   Call hook in the route component.
*   Returns data from `clientLoader`.
*   TypeScript Tip: `const clientData = useClientLoaderData<typeof clientLoader>();`

## Example

```typescript
// app/routes/settings.tsx
import type { LoaderFunctionArgs, ClientLoaderFunctionArgs } from "@remix-run/node";
import { json } from "@remix-run/node";
import { useLoaderData, useClientLoaderData } from "@remix-run/react";

// --- Server Loader ---
export async function loader({ request }: LoaderFunctionArgs) {
  // const settings = await getUserSettings(userId);
  const settings = { theme: 'dark' }; // Placeholder
  return json({ settings });
}

// --- Client Loader ---
export async function clientLoader({ serverLoader }: ClientLoaderFunctionArgs) {
  console.log("Client Loader Running!");
  const { settings } = await serverLoader<typeof loader>(); // Access server data
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const lastVisit = localStorage.getItem('lastVisit');

  return {
    prefersReducedMotion,
    lastVisit: lastVisit ? new Date(lastVisit) : null,
    initialTheme: settings.theme, // Combine data
  };
}

// --- Default Component ---
export default function SettingsRoute() {
  const { settings } = useLoaderData<typeof loader>(); // Server data
  const clientData = useClientLoaderData<typeof clientLoader>(); // Client data

  useEffect(() => {
    localStorage.setItem('lastVisit', new Date().toISOString());
  }, []);

  return (
    <div>
      <h2>Settings</h2>
      <p>Server Theme: {settings.theme}</p>
      <p>Reduced Motion: {clientData?.prefersReducedMotion ? 'Yes' : 'No'}</p>
      <p>Last Visit: {clientData?.lastVisit?.toLocaleString() ?? 'N/A'}</p>
    </div>
  );
}
```

## Considerations

*   **Execution Timing:** `clientLoader` runs *after* server `loader`. Data isn't available for initial server render (potential flicker).
*   **Use Cases:** Best for enhancing UI with client-specific info *after* initial render or data that *must* come from the browser.
*   **Alternative (`useFetcher`):** For on-demand loading based on user interaction *without* navigation, `useFetcher` might be better.

*(Derived from `remix-client-loader.md`)*