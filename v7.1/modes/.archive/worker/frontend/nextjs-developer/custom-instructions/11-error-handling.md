# App Router: Error Handling

Handling runtime errors gracefully in Next.js App Router applications.

## Core Concept: Error Boundaries with `error.tsx`

The App Router uses React Error Boundaries via `error.tsx` files to catch runtime errors during rendering within a route segment and its children.

*   **File Convention:** Create `error.tsx` (or `.js`) alongside `page.tsx` or `layout.tsx`.
*   **Automatic Wrapping:** Next.js wraps the segment's `page.tsx`/`layout.tsx` and children in an Error Boundary using your `error.tsx`.
*   **Client Component Requirement:** `error.tsx` **must** be a Client Component (`'use client'`).
*   **Props:** Receives `error` (Error object, possibly with `digest`) and `reset` (function to attempt re-rendering the segment).
*   **Granularity:** Catches errors in the segment *below* it. Nearest boundary *above* the error source handles it.
*   **Layout Preservation:** Layouts *above* the boundary remain interactive.

## Implementing `error.tsx`

```typescript
// app/dashboard/error.tsx
'use client'; // Must be a Client Component

import { useEffect } from 'react';
import Button from '@mui/material/Button'; // Example UI
import Alert from '@mui/material/Alert';

export default function DashboardError({
  error,
  reset,
}: {
  error: Error & { digest?: string }; // Error object
  reset: () => void; // Retry function
}) {
  useEffect(() => {
    // Log error to reporting service (e.g., Sentry)
    console.error('Dashboard Segment Error:', error);
  }, [error]);

  return (
    <Alert severity="error">
      <h2>Oops! Dashboard Error</h2>
      <p>{process.env.NODE_ENV === 'development' ? error.message : 'Please try again.'}</p>
      <Button variant="contained" onClick={() => reset()}>
        Try again
      </Button>
    </Alert>
  );
}
```

## Global Error Handling (`global-error.tsx`)

*   **Purpose:** Handles errors specifically in the *root* `layout.tsx`.
*   **Location:** `app/global-error.tsx`.
*   **Behavior:** Replaces the *entire* root layout. **Must** define its own `<html>` and `<body>` tags.
*   **Use Case:** Fallback UI for root layout errors. Less common than segment `error.tsx`.
*   **Client Component:** Must be `'use client'`.

```typescript
// app/global-error.tsx
'use client';

export default function GlobalError({ error, reset }) {
  useEffect(() => { console.error("Global Error:", error); }, [error]);
  return (
    <html>
      <body>
        <h2>Something went wrong globally!</h2>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  );
}
```

## Handling Not Found Errors (`notFound()`)

*   **Purpose:** Programmatically trigger a "Not Found" state (e.g., data for dynamic segment doesn't exist).
*   **Usage:** Import `notFound` from `next/navigation`. Call `notFound()` in Server Components, Route Handlers, or Server Actions.
*   **Behavior:** Stops rendering, searches upwards for nearest `not-found.tsx` file. Renders default 404 if none found.

```typescript
// app/products/[id]/page.tsx
import { notFound } from 'next/navigation';

async function getProduct(id: string) {
  const res = await fetch(`https://.../products/${id}`);
  if (!res.ok) {
    if (res.status === 404) {
      notFound(); // Trigger not-found UI
    }
    throw new Error('Failed to fetch product'); // For error.tsx
  }
  return res.json();
}

export default async function ProductPage({ params }) {
  const product = await getProduct(params.id);
  // Rendering stops before here if notFound() was called
  return <div>{/* Render product */}</div>;
}

// Optional: app/products/[id]/not-found.tsx
export default function ProductNotFound() {
  return <h1>Product Not Found!</h1>;
}
```

Use `error.tsx` for runtime errors and `notFound()` for missing data/routes.

*(Refer to the official Next.js documentation on Error Handling and `notFound`.)*