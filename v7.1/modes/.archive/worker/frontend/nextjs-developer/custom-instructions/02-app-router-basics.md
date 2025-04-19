# App Router: Basics & File Conventions

Understanding the fundamental file conventions and concepts of the Next.js App Router (`app/` directory).

## Core Concept: App Router (`app/` Directory)

Introduced in Next.js 13, the App Router uses a file-system based routing mechanism within the `app/` directory, centered around React Server Components.

**Key Principles:**

*   **Server Components by Default:** Components within `app/` are React Server Components (RSCs) unless marked with `'use client'`. RSCs render on the server and their code isn't sent to the client.
*   **File Conventions:** Special file names define UI and behavior for route segments:
    *   `layout.tsx` / `.js`: Shared UI for a segment and its children. Required at the root (`app/layout.tsx`).
    *   `page.tsx` / `.js`: Unique UI for a route segment, making it publicly accessible.
    *   `loading.tsx` / `.js`: Loading UI shown via React Suspense during data fetching/rendering.
    *   `error.tsx` / `.js`: Error UI boundary for a segment. Must be a Client Component (`'use client'`). Catches errors in nested children.
    *   `global-error.tsx` / `.js`: Global error boundary specifically for the root layout. Must be a Client Component and define `<html>`/`<body>`.
    *   `not-found.tsx` / `.js`: UI shown when `notFound()` is called or a route doesn't match.
    *   `template.tsx` / `.js`: Similar to `layout`, but re-mounts on navigation (state isn't preserved). Less common.
    *   `route.ts` / `.js`: Defines API endpoints (Route Handlers) instead of UI.
*   **Colocation:** Components, styles, tests, etc., can be placed within route segment folders.

## Basic Structure Example

```
app/
├── layout.tsx        # Root Layout (Required: <html>, <body>)
├── page.tsx          # Root Page (Homepage UI at '/')
├── globals.css       # Global Styles
│
├── dashboard/        # Route Segment for '/dashboard'
│   ├── layout.tsx    # Layout specific to '/dashboard' and children
│   ├── page.tsx      # Page UI for '/dashboard'
│   ├── settings/     # Nested Route Segment for '/dashboard/settings'
│   │   └── page.tsx  # Page UI for '/dashboard/settings'
│   └── loading.tsx   # Loading UI for '/dashboard' segment children
│
├── blog/             # Route Segment for '/blog'
│   ├── [slug]/       # Dynamic Route Segment for '/blog/[slug]'
│   │   ├── page.tsx  # Page UI for individual blog posts
│   │   └── error.tsx # Error UI specific to blog post rendering
│   └── page.tsx      # Page UI for '/blog' (listing posts)
│
└── api/              # Route Segment for API endpoints
    └── users/
        └── route.ts  # API endpoint at '/api/users'
```

## Special Files Explained

*   **`layout.tsx`:**
    *   Defines shared UI (headers, footers, sidebars).
    *   Receives `children` prop (child layout or page).
    *   Root Layout (`app/layout.tsx`) is required, must include `<html>` and `<body>`.
    *   Must be a Server Component.

*   **`page.tsx`:**
    *   Defines the unique UI of a route.
    *   Server Component by default (can be `async` for data fetching).
    *   Can be a Client Component using `'use client'`.

*   **`loading.tsx`:**
    *   Automatically wraps `page.tsx` and children in `<Suspense>`.
    *   Displays instantly while route content loads.

*   **`error.tsx`:**
    *   Creates React Error Boundary for the segment.
    *   Must be a Client Component (`'use client'`).
    *   Receives `error` (Error object) and `reset` (function to retry rendering) props.
    *   Catches errors from nested segments/pages. Layouts *above* the boundary remain interactive.

*   **`global-error.tsx`:**
    *   Catches errors in the *root* `layout.tsx`.
    *   Must be a Client Component and define its own `<html>`/`<body>`.

*   **`not-found.tsx`:**
    *   Renders UI when the `notFound()` function is called within a segment, or if a URL path doesn't match any route.

*(Refer to the official Next.js documentation on the App Router, Routing, Layouts, Pages, Loading UI, and Error Handling.)*