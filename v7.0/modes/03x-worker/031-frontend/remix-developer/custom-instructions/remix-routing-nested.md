# Remix: Routing (File Conventions, Nested Routes, Links)

Defining routes, dynamic segments, and handling navigation in Remix.

## Core Concept: File-System Routing (`app/routes/`)

Remix uses a file-based routing system where files and folders within the `app/routes/` directory map directly to URL paths.

**Key Conventions:**

*   **Route Modules:** Each file (`.tsx`, `.jsx`, `.js`, `.mdx`, etc.) in `app/routes/` potentially defines a route.
*   **Path Segments:** Folder names and filenames become URL segments.
*   **Index Routes:** Files named `_index.tsx` (or `.js`, etc.) represent the index route for a directory (e.g., `app/routes/_index.tsx` -> `/`, `app/routes/dashboard._index.tsx` -> `/dashboard`).
*   **Nested Routes:** Folders create nested URL paths. A layout route is defined by a file matching the folder name (e.g., `app/routes/dashboard.tsx`), and child routes are placed inside the folder (e.g., `app/routes/dashboard/settings.tsx` -> `/dashboard/settings`).
*   **Dynamic Segments:** Use a `$` prefix for dynamic parameters (e.g., `app/routes/users.$userId.tsx` -> `/users/:userId`). The value is available in `loader`/`action` via `params.userId`.
*   **Splats (Wildcards):** Use a `$` at the end of a filename to match all subsequent URL segments (e.g., `app/routes/files.$.tsx` -> `/files/*`). The matched part is available as `params['*']`.
*   **Pathless Layout Routes:** Use underscores `_` prefixing a folder name (e.g., `app/routes/_auth/login.tsx`) or filename (`app/routes/_auth.tsx`) to create layout routes that *don't* add segments to the URL path. Useful for grouping routes under a shared layout (like auth pages) without affecting their URLs.

## Nested Routing & `<Outlet>`

*   Remix excels at nested routing, where parts of the UI persist while child segments change.
*   Parent route components (layout routes or index routes with children) **must render an `<Outlet />` component** (imported from `@remix-run/react`).
*   The `<Outlet />` acts as a placeholder where the matching child route component will be rendered.
*   Loaders and actions run in parallel for all matched nested routes on navigation.

```typescript
// app/routes/dashboard.tsx (Parent Layout Route)
import { Outlet, Link } from "@remix-run/react";
// export function loader() { /* data for dashboard layout */ }

export default function DashboardLayout() {
  // const data = useLoaderData<typeof loader>();
  return (
    <div>
      <h1>Dashboard Layout</h1>
      <nav>
        <Link to="/dashboard">Overview</Link> | {' '}
        <Link to="/dashboard/settings">Settings</Link> | {' '}
        <Link to="/dashboard/profile">Profile</Link>
      </nav>
      <hr />
      {/* Child route component renders here */}
      <Outlet />
    </div>
  );
}

// app/routes/dashboard._index.tsx (Child Index Route - /dashboard)
export default function DashboardIndex() {
  return <h2>Dashboard Overview</h2>;
}

// app/routes/dashboard.settings.tsx (Child Route - /dashboard/settings)
export default function DashboardSettings() {
  return <h2>Account Settings</h2>;
}

// app/routes/dashboard.profile.tsx (Child Route - /dashboard/profile)
// export function loader() { /* data for profile */ }
export default function DashboardProfile() {
  // const data = useLoaderData<typeof loader>();
  return <h2>User Profile</h2>;
}
```

## Navigation (`<Link>`, `useNavigate`)

*   **`<Link>` Component:**
    *   Import from `@remix-run/react`.
    *   Primary way to navigate between Remix routes.
    *   Renders an `<a>` tag.
    *   Handles client-side navigation without full page reloads.
    *   `to` prop: Destination path (e.g., `/posts/123`, `../sibling-route`, `.?index` to target index route).
    *   `reloadDocument`: Prop to force a full page reload (disables client-side routing).
    *   `preventScrollReset`: Prop to prevent scrolling to the top on navigation.
    *   `prefetch="intent"` (default) / `"render"` / `"none"`: Controls when Remix prefetches route data and modules (on hover/focus, on render, or never).
*   **`<NavLink>` Component:**
    *   Similar to `<Link>` but adds styling hooks (`className`/`style` can be functions receiving `{ isActive, isPending }`) for indicating active or pending navigation states.
*   **`useNavigate()` Hook:**
    *   Programmatically navigate. `const navigate = useNavigate(); navigate('/path'); navigate(-1);`

```jsx
import { Link, NavLink, useNavigate } from "@remix-run/react";

function NavigationExample() {
  const navigate = useNavigate();

  return (
    <nav>
      <Link to="/">Home</Link>
      {/* NavLink with active styling */}
      <NavLink
        to="/about"
        className={({ isActive, isPending }) =>
          isPending ? "pending" : isActive ? "active" : ""
        }
      >
        About
      </NavLink>
      <Link to="/posts/abc" prefetch="render">Post ABC (Prefetch)</Link>
      <button onClick={() => navigate('/contact')}>Go to Contact</button>
      <button onClick={() => navigate(-1)}>Go Back</button>
    </nav>
  );
}
```

Remix's file-based routing, combined with the `<Outlet>` component for nesting and the `<Link>`/`<NavLink>` components for client-side transitions, provides a powerful and intuitive way to structure application navigation and UI layouts.

*(Refer to the official Remix documentation on Routing and components like `<Link>`, `<NavLink>`, `<Outlet>`.)*