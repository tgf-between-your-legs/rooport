# Next.js App Router Basics

Core concepts for file-system based routing in the Next.js App Router (`app/` directory).

## File Conventions

Special files define UI for route segments:

*   **`layout.tsx` (or `.js`)**: Defines shared UI for a segment and its children. Requires `<html>` and `<body>` tags in the root layout. Layouts nest automatically.
*   **`page.tsx` (or `.js`)**: Defines the unique UI for a route segment, making the path publicly accessible.
*   **`loading.tsx` (or `.js`)**: Defines loading UI (e.g., a spinner) shown during Server Component data fetching within a segment, using React Suspense.
*   **`error.tsx` (or `.js`)**: Defines UI boundary for runtime errors within a segment. Must be a Client Component (`'use client'`). Receives `error` and `reset` props.
*   **`global-error.tsx` (or `.js`)**: Defines a global error boundary for the root layout. Must be a Client Component.
*   **`template.tsx` (or `.js`)**: Similar to `layout.tsx`, but re-mounts components on navigation (state is not preserved). Less common.
*   **`route.ts` (or `.js`)**: Defines API endpoints (Route Handlers) instead of UI pages.

## Folder Structure & Routing

*   Folders within `app/` define route segments.
*   `app/page.tsx` -> `/`
*   `app/dashboard/page.tsx` -> `/dashboard`
*   `app/blog/[slug]/page.tsx` -> `/blog/:slug` (e.g., `/blog/my-post`)
*   `app/shop/[...categories]/page.tsx` -> `/shop/*` (e.g., `/shop/a/b/c`)
*   `app/(marketing)/about/page.tsx` -> `/about` (Route Groups `(...)` don't affect URL path, used for organization or shared layouts).
*   `app/@modal/(.)photo/[id]/page.tsx` -> Intercepted route for modals (Parallel Routes `@`).

## Layouts

*   Define shared UI (headers, footers, sidebars).
*   Receive `children` prop representing child layouts or pages.
*   Data fetched in a layout is available to all child segments.
*   Root Layout (`app/layout.tsx`) is required and must include `<html>` and `<body>`.

```tsx
// app/dashboard/layout.tsx
export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return (
    <section>
      {/* Include shared UI here e.g., sidebar */}
      <nav>Dashboard Nav</nav>
      {children} {/* Child page or nested layout renders here */}
    </section>
  );
}
```

## Pages

*   Define the unique UI of a route.
*   Server Components by default. Can fetch data directly using `async/await`.
*   Can be Client Components using `'use client'`.

```tsx
// app/dashboard/settings/page.tsx
// Server Component by default
async function getSettings() {
  // const settings = await db.query...
  return { theme: 'dark' }; // Placeholder
}

export default async function SettingsPage() {
  const settings = await getSettings();
  return (
    <div>
      <h1>Settings</h1>
      <p>Theme: {settings.theme}</p>
      {/* Use Client Components for interactivity */}
      {/* <ThemeSwitcher client:load initialTheme={settings.theme} /> */}
    </div>
  );
}
```

## Linking & Navigation

*   Use the `<Link>` component from `next/link` for client-side navigation between routes.
    ```tsx
    import Link from 'next/link';
    <Link href="/dashboard/settings">Go to Settings</Link>
    ```
*   Use the `useRouter` hook (from `next/navigation`) for programmatic navigation within Client Components.
    ```tsx
    'use client';
    import { useRouter } from 'next/navigation';
    // ...
    const router = useRouter();
    router.push('/dashboard');
    ```

## Dynamic Routes

*   Use brackets `[]` for dynamic segments (`[slug]`) and `[...catchAll]` for catch-all segments.
*   Access parameters via the `params` prop in layouts, pages, and `generateStaticParams`.
    ```tsx
    // app/blog/[slug]/page.tsx
    export default function BlogPostPage({ params }: { params: { slug: string } }) {
      return <h1>Post: {params.slug}</h1>;
    }
    ```
*   Use `generateStaticParams` to statically generate routes at build time for dynamic segments (SSG).

*(Refer to the official Next.js Routing documentation for full details: https://nextjs.org/docs/app/building-your-application/routing)*