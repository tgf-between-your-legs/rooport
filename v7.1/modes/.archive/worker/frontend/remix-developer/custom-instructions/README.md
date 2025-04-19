# Custom Instructions for 💿 Remix Developer

This directory contains specific instructions and guidelines for the `remix-developer` mode.

## Instruction Files

1.  **`01-core-workflow.md`**: General operational principles and standard workflow steps.
2.  **`02-routing-route-modules.md`**: Covers file-system routing conventions, nested routes (`<Outlet>`), dynamic segments, and navigation (`<Link>`, `<NavLink>`, `useNavigate`).
3.  **`03-data-flow-loader.md`**: Details server-side data loading using the `loader` function and accessing data with `useLoaderData`.
4.  **`04-data-flow-action.md`**: Explains server-side data mutations using the `action` function and accessing results with `useActionData`.
5.  **`05-forms-mutations-fetcher.md`**: Focuses on using `<Form>` for page mutations and `useFetcher` for background actions/loads without navigation.
6.  **`06-error-handling.md`**: Describes Remix's route-level `ErrorBoundary` component and the `useRouteError` hook.
7.  **`07-sessions.md`**: Covers server-side session management concepts, including storage, getting/setting data, flash messages, and committing sessions.
8.  **`08-caching-headers.md`**: Explains how to control HTTP caching using the `headers` export and `Cache-Control` directives.
9.  **`09-web-standards.md`**: Highlights Remix's use of standard Web APIs like `Request`, `Response`, `Headers`, and `fetch`.
10. **`10-vite-integration.md`**: Details using Vite as the build tool and development server, including configuration (`vite.config.ts`) and workflow.
11. **`11-client-loader.md`**: Explains the use cases and implementation of `clientLoader` for client-side only data fetching/preparation.
12. **`12-collaboration-escalation.md`**: Outlines collaboration points with other specialists and the escalation path via the `frontend-lead`.
13. **`13-key-considerations.md`**: Summarizes crucial points and best practices for Remix development.