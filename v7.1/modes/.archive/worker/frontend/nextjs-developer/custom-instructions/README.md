# Custom Instructions for 🚀 Next.js Developer

This directory contains specific instructions and guidelines for the `nextjs-developer` mode.

## Files

*   **`01-core-principles-workflow.md`**: General operational guidelines, best practices, tool usage, and standard workflow steps.
*   **`02-app-router-basics.md`**: Fundamental concepts of the App Router (`app/` directory), including special file conventions (`layout.tsx`, `page.tsx`, `loading.tsx`, `error.tsx`, etc.).
*   **`03-routing-navigation.md`**: Details on defining static and dynamic routes, route groups, parallel routes, and using `<Link>` and `useRouter` for navigation.
*   **`04-rendering-strategies.md`**: Explanation of different rendering methods: Static Site Generation (SSG), Server-Side Rendering (SSR), Incremental Static Regeneration (ISR), Streaming UI with Suspense, and Partial Prerendering (PPR).
*   **`05-data-fetching-caching.md`**: Strategies for fetching data (in Server Components, Route Handlers, Client Components) and understanding Next.js caching layers (Request Memoization, Data Cache, Full Route Cache, Router Cache) and revalidation (`revalidatePath`, `revalidateTag`).
*   **`06-server-client-components.md`**: Detailed comparison of Server Components (default) and Client Components (`'use client'`), their capabilities, limitations, and how they interact.
*   **`07-server-actions.md`**: How to define and use Server Actions (`'use server'`) for handling mutations and server-side logic, especially with forms (`useFormState`, `useFormStatus`).
*   **`08-api-route-handlers.md`**: Creating API endpoints using Route Handlers (`route.ts`) for traditional API needs, fetching from Client Components, or handling webhooks.
*   **`09-middleware.md`**: Using `middleware.ts` to intercept requests for authentication, redirects, rewrites, or header modifications. Includes `matcher` configuration.
*   **`10-image-optimization.md`**: Using the built-in `next/image` component for optimized image delivery (resizing, formats, lazy loading, CLS prevention).
*   **`11-error-handling.md`**: Handling runtime errors using `error.tsx` boundaries and handling "Not Found" states using `notFound()` and `not-found.tsx`.
*   **`12-vercel-deployment.md`**: Basics of deploying Next.js applications to the Vercel platform, including configuration, environment variables, and key Vercel concepts.
*   **`13-collaboration-escalation.md`**: Guidelines on collaborating with other specialist modes and when/how to escalate tasks.