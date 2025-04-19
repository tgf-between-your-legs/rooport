# Routing & Route Modules

## Core Concept: Route Modules & File-System Routing

In Remix, each route is typically defined by a single file within the `app/routes/` directory. This file, called a **Route Module**, can export specific functions and a default component that Remix uses to handle different aspects of the route: data loading, data mutations, UI rendering, error handling, and metadata. Remix uses a file-based routing system where files and folders within the `app/routes/` directory map directly to URL paths.

**File Naming Convention:**

*   **Route Modules:** Each file (`.tsx`, `.jsx`, `.js`, `.mdx`, etc.) in `app/routes/` potentially defines a route.
*   **Path Segments:** Folder names and filenames become URL segments.
*   **Index Routes:** Files named `_index.tsx` (or `.js`, etc.) represent the index route for a directory (e.g., `app/routes/_index.tsx` -> `/`, `app/routes/dashboard._index.tsx` -> `/dashboard`).
*   **Nested Routes:** Folders create nested URL paths. A layout route is defined by a file matching the folder name (e.g., `app/routes/dashboard.tsx`), and child routes are placed inside the folder (e.g., `app/routes/dashboard/settings.tsx` -> `/dashboard/settings`).
*   **Dynamic Segments:** Use a `$` prefix for dynamic parameters (e.g., `app/routes/users.$userId.tsx` -> `/users/:userId`). The value is available in `loader`/`action` via `params.userId`.
*   **Splats (Wildcards):** Use a `$` at the end of a filename to match all subsequent URL segments (e.g., `app/routes/files.$.tsx` -> `/files/*`). The matched part is available as `params['*']`.
*   **Pathless Layout Routes:** Use underscores `_` prefixing a folder name (e.g., `app/routes/_auth/login.tsx`) or filename (`app/routes/_auth.tsx`) to create layout routes that *don't* add segments to the URL path. Useful for grouping routes under a shared layout (like auth pages) without affecting their URLs.

## Key Exports from Route Modules

These are the main functions and components you can export from a route module (`.tsx` or `.jsx`):

1.  **`loader` Function (Server-Side):** Loads data for the route on the server. (See `03-data-flow-loader.md`)
2.  **`action` Function (Server-Side):** Handles data mutations (POST, PUT, etc.) on the server. (See `04-data-flow-action.md`)
3.  **`default` Export (Component):** The React component rendering the UI for this route segment.
4.  **`ErrorBoundary` Component:** Catches errors from rendering, loader, or action. (See `06-error-handling.md`)
5.  **`headers` Function (Server-Side):** Sets HTTP headers (e.g., `Cache-Control`). (See `08-caching-headers.md`)
6.  **`meta` Function:** Sets meta tags (`<title>`, `<meta name="description">`).
7.  **`links` Function:** Adds `<link>` tags (stylesheets, preloads).

## Nested Routing & `<Outlet>`

*   Remix excels at nested routing, where parts of the UI persist while child segments change.
*   Parent route components (layout routes or index routes with children) **must render an `<Outlet />` component** (imported from `@remix-run/react`).
*   The `<Outlet />` acts as a placeholder where the matching child route component will be rendered.
*   Loaders and actions run in parallel for all matched nested routes on navigation.

```typescript
// app/routes/dashboard.tsx (Parent Layout Route)
import { Outlet, Link } from "@remix-run/react";

export default function DashboardLayout() {
  return (
    <div>
      <h1>Dashboard Layout</h1>
      <nav>
        <Link to="/dashboard">Overview</Link> | {' '}
        <Link to="/dashboard/settings">Settings</Link>
      </nav>
      <hr />
      {/* Child route component renders here */}
      <Outlet />
    </div>
  );
}

// app/routes/dashboard._index.tsx (Child Index Route - /dashboard)
export default function DashboardIndex() { return <h2>Dashboard Overview</h2>; }

// app/routes/dashboard.settings.tsx (Child Route - /dashboard/settings)
export default function DashboardSettings() { return <h2>Account Settings</h2>; }
```

## Navigation (`<Link>`, `useNavigate`)

*   **`<Link>` Component:**
    *   Import from `@remix-run/react`. Primary way to navigate. Renders `<a>`.
    *   Handles client-side navigation.
    *   `to` prop: Destination path.
    *   `reloadDocument`: Force full page reload.
    *   `preventScrollReset`: Prevent scrolling to top.
    *   `prefetch="intent"` (default) / `"render"` / `"none"`: Control prefetching behavior.
*   **`<NavLink>` Component:**
    *   Like `<Link>` but adds styling hooks (`className`/`style` functions receiving `{ isActive, isPending }`).
*   **`useNavigate()` Hook:**
    *   Programmatically navigate: `const navigate = useNavigate(); navigate('/path'); navigate(-1);`

```jsx
import { Link, NavLink, useNavigate } from "@remix-run/react";

function NavigationExample() {
  const navigate = useNavigate();
  return (
    <nav>
      <Link to="/">Home</Link>
      <NavLink to="/about" className={({ isActive }) => isActive ? "active" : ""}>About</NavLink>
      <button onClick={() => navigate('/contact')}>Go to Contact</button>
    </nav>
  );
}
```

*(Combined from `remix-route-modules.md` and `remix-routing-nested.md`)*