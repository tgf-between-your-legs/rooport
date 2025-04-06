## Next.js - Condensed Context Index

### Overall Purpose
Next.js is a React framework for building full-stack web applications. It enables features like Server Components, file-based routing (App Router), diverse rendering strategies (SSR, SSG, ISR, PPR), integrated API routes (Route Handlers), Server Actions, and built-in optimizations for performance and developer experience.

### Core Concepts & Capabilities
*   **Project Setup & Tooling:** Initialize projects (`create-next-app`), manage dependencies (`npm`), configure debugging (`launch.json`). Supports TypeScript/JavaScript.
*   **App Router & Routing:** File-based routing (`app/` dir), layouts (`layout.js`), pages (`page.js`), dynamic segments (`[slug]`), client-side navigation (`next/link`), parallel routes (e.g., modals). Key concepts: `RootLayout`, nested layouts, `params` prop.
*   **Rendering Models:** Server Components (default, async), Client Components (`'use client'`, state/hooks), Static Generation (`generateStaticParams`), Server-Side Rendering (default for dynamic data), Partial Prerendering (`experimental_ppr`), Streaming (`Suspense`).
*   **Data Fetching & Caching:** Server-side `fetch`, client-side `fetch`, ORM/DB access in Server Components, caching strategies (`fetch` options, `force-static`), cache revalidation (`revalidatePath`).
*   **Server Actions:** Define server-side logic callable from components (`'use server'`), handle form submissions, data mutations, validation (`zod`). Key concepts: `FormData`.
*   **Built-in Components & APIs:** Image optimization (`next/image`), client navigation (`next/link`), font optimization (`next/font`), accessing request data (`next/headers`, `next/cookies`, `NextRequest`).
*   **Styling & Configuration:** CSS Modules (`*.module.css`), global styles, configuring Next.js (`next.config.js` for static export, etc.).
*   **Error Handling:** Component-level errors (`error.js`), global errors (`global-error.js`), handling fetch errors. Key concepts: Error Boundaries, `reset` function.

### Key APIs / Components / Configuration / Patterns
*   `create-next-app`: CLI tool for project initialization (e.g., `npx create-next-app@latest`).
*   `next/link`: Component for client-side navigation. Usage: `<Link href="/path">`.
*   `next/image`: Component for optimized images (local/remote). Usage: `<Image src={...} alt="..." />`.
*   `layout.js`/`layout.tsx`: File convention for shared UI. Exports default component receiving `children`. Root layout requires `<html>` & `<body>`.
*   `page.js`/`page.tsx`: File convention for route segment UI. Exports default async/sync component.
*   `'use client'`: Directive marking module/component for client-side execution (enables hooks, browser APIs).
*   `'use server'`: Directive marking functions as Server Actions, callable from client or server.
*   `async function Component()`: Server Components are async by default, allowing `await` for data fetching.
*   `fetch()`: Native API used for data fetching, extended by Next.js for caching/revalidation control.
*   `generateStaticParams()`: Function in dynamic route segments (`[slug]/page.js`) to define params for static generation at build time.
*   `next/headers`: Function to access request headers. Usage: `headers().get('...')`.
*   `next/cookies`: Function to access request cookies. Usage: `cookies().get('...')`.
*   `NextRequest`: Extended Web Request API object passed to Route Handlers.
*   `revalidatePath()`: Function (from `next/cache`) to manually invalidate cache for a specific path.
*   `Suspense` (from `react`): Wraps components to enable streaming rendering with a fallback UI. Usage: `<Suspense fallback={...}>`.
*   `error.js`/`error.tsx`: File convention for UI error boundaries. Must be a Client Component.
*   `global-error.js`/`global-error.tsx`: File convention for root error boundary. Must be Client Component with `<html>`/`<body>`.
*   `next.config.js`: Configuration file (e.g., `output: 'export'` for static sites).
*   `next/font`: Functions for optimizing local and Google Fonts (e.g., `Inter()`, `localFont()`).
*   Route Handlers (`route.js`/`route.ts`): Files defining API endpoints using HTTP methods (e.g., `export async function GET(request: NextRequest)`).

### Common Patterns & Best Practices / Pitfalls
*   **Server vs. Client:** Use Server Components by default; opt into Client Components (`'use client'`) only when interactivity/browser APIs are needed.
*   **Data Fetching:** Fetch in Server Components where possible. Use Route Handlers for dedicated APIs.
*   **Caching:** Leverage `fetch` caching. Use `revalidatePath`/`revalidateTag` after mutations.
*   **Error Handling:** Implement `error.js` boundaries. Check `res.ok` for fetch errors.
*   **Layouts:** Use `layout.js` for shared UI; nest for specific segments. Root layout is mandatory.
*   **Server Actions:** Prefer for form submissions/mutations over API routes. Use validation (`zod`).
*   **Static Exports:** Use `output: 'export'` and `generateStaticParams` for fully static sites.

---
This index summarizes the core concepts, APIs, and patterns for Next.js based on the provided snippets. Consult the full source documentation (`project_journal/context/source_docs/nextjs-developer-llms-context-20250406.md`) for exhaustive details.