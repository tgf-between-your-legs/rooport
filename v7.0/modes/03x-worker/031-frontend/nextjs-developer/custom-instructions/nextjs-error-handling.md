# Next.js: Error Handling (App Router)

Handling runtime errors gracefully in Next.js App Router applications.

## Core Concept: Error Boundaries with `error.tsx`

The App Router uses React Error Boundaries to catch runtime errors that occur during rendering within a specific route segment and its children.

*   **`error.tsx` File Convention:** Create an `error.tsx` (or `.js`) file alongside a `page.tsx` or `layout.tsx` to define an error UI boundary for that segment.
*   **Automatic Wrapping:** Next.js automatically wraps the segment's `page.tsx` (or nested `layout.tsx`) and its children within an Error Boundary using your `error.tsx` component.
*   **Client Component Requirement:** Error components **must** be Client Components (`'use client'`).
*   **Props:** The `error.tsx` component receives two props:
    *   `error`: The JavaScript `Error` object that was caught. Includes `error.message` and potentially `error.digest` (a server-generated hash for correlating server logs).
    *   `reset`: A function that, when called, attempts to re-render the Error Boundary's contents (the segment that threw the error). Useful for attempting recovery from temporary issues.
*   **Granularity:** Errors are caught by the *nearest* `error.tsx` boundary *above* the component that threw the error in the component tree. This allows for granular error UI specific to parts of your application.
*   **Layout Preservation:** The `error.tsx` boundary replaces only the UI of the segment *below* it where the error occurred. Shared layouts *above* the boundary remain interactive.

## Implementing `error.tsx`

```typescript
// app/dashboard/error.tsx
'use client'; // Error components must be Client Components

import { useEffect } from 'react';
import Button from '@mui/material/Button'; // Example using MUI
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';

export default function DashboardError({
  error,
  reset,
}: {
  error: Error & { digest?: string }; // Error object with optional digest
  reset: () => void; // Function to attempt re-render
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error('Dashboard Segment Error:', error);
    // You could send error.message and error.digest to Sentry, LogRocket, etc.
  }, [error]);

  return (
    <div style={{ padding: '2rem' }}>
      <Alert severity="error">
        <AlertTitle>Oops! Something went wrong in the dashboard.</AlertTitle>
        <p>We encountered an error while loading this section.</p>
        <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-all', fontSize: '0.8em' }}>
          {/* Displaying error message in dev, consider hiding in prod */}
          {process.env.NODE_ENV === 'development' ? error.message : 'Please try again later.'}
          {error.digest && process.env.NODE_ENV === 'development' ? ` (Digest: ${error.digest})` : ''}
        </pre>
        <Button
          variant="contained"
          color="warning"
          onClick={
            // Attempt to recover by trying to re-render the segment
            () => reset()
          }
          sx={{ mt: 1 }}
        >
          Try again
        </Button>
      </Alert>
    </div>
  );
}
```

## Global Error Handling (`global-error.tsx`)

*   **Purpose:** To handle errors specifically within the *root* `layout.tsx`.
*   **Location:** Create `app/global-error.tsx`.
*   **Behavior:** Wraps the entire application. If it triggers, it replaces the root layout. Because of this, it **must** define its own `<html>` and `<body>` tags.
*   **Use Case:** Provides a fallback UI for errors occurring in the root layout itself, which cannot be caught by nested `error.tsx` boundaries. Less commonly needed than segment-level `error.tsx`.
*   **Client Component:** Must also be a Client Component (`'use client'`).

```typescript
// app/global-error.tsx
'use client';

import { useEffect } from 'react';

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error("Global Error:", error);
  }, [error]);

  return (
    <html>
      <body>
        <h2>Something went wrong globally!</h2>
        <p>An error occurred in the root layout.</p>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  );
}
```

## Handling Not Found Errors (`notFound()`)

*   **Purpose:** Programmatically trigger a "Not Found" state, typically when data for a dynamic segment doesn't exist.
*   **Usage:** Import `notFound` from `next/navigation`. Call `notFound()` within a Server Component or Route Handler.
*   **Behavior:** Stops rendering the current segment and searches upwards for the nearest `not-found.tsx` file to render. If no custom `not-found.tsx` exists, Next.js renders a default 404 page.

```typescript
// app/products/[id]/page.tsx
import { notFound } from 'next/navigation';

async function getProduct(id: string) {
  const res = await fetch(`https://api.example.com/products/${id}`);
  if (!res.ok) {
    // If status is 404 or similar, trigger notFound
    if (res.status === 404) {
      notFound(); // Renders nearest not-found.tsx or default 404
    }
    // Handle other fetch errors
    throw new Error('Failed to fetch product');
  }
  return res.json();
}

export default async function ProductPage({ params }: { params: { id: string } }) {
  const product = await getProduct(params.id);
  // If getProduct called notFound(), rendering stops before here

  return <div>{/* Render product details */}</div>;
}

// Optional: app/products/[id]/not-found.tsx (Custom Not Found UI for this segment)
export default function ProductNotFound() {
  return <h1>Sorry, that product could not be found!</h1>;
}
```

By using `error.tsx` for runtime errors and `notFound()` for missing data, you can create more resilient and user-friendly Next.js applications.

*(Refer to the official Next.js documentation on Error Handling and `notFound`.)*