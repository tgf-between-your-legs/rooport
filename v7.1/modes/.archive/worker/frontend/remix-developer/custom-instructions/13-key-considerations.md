# Key Considerations / Safety Protocols

*   **Route Modules:** Master `loader`, `action`, `Component`, `ErrorBoundary` exports. (See `02-routing-route-modules.md`)
*   **Data Flow:** Use `loader`/`useLoaderData` and `action`/`useActionData` correctly. (See `03-data-flow-loader.md`, `04-data-flow-action.md`)
*   **Forms & Progressive Enhancement:** Use `<Form>` and `useFetcher` effectively, managing pending states. (See `05-forms-mutations-fetcher.md`)
*   **Routing:** Implement nested routing (`<Outlet>`). (See `02-routing-route-modules.md`)
*   **Web Standards:** Leverage Fetch API, Request/Response. (See `09-web-standards.md`)
*   **Server/Client Colocation:** Keep server logic (`loader`/`action`) separate from client UI (`Component`) within route files.
*   **Error Handling:** Implement `ErrorBoundary` and use `useRouteError`. Handle errors in loaders/actions gracefully. (See `06-error-handling.md`)
*   **Session Management:** Use Remix utilities securely (coordinate with auth specialists). Commit sessions after changes. (See `07-sessions.md`)
*   **Caching:** Use `headers` export for HTTP caching. (See `08-caching-headers.md`)
*   **Adapters & Versions:** Be aware of the target deployment adapter (Node, Vercel, Cloudflare, etc.) and Remix version/`future` flags.
*   **Vite Integration:** Understand `vite.config.ts` and build process. (See `10-vite-integration.md`)
*   **Client Loader:** Use `clientLoader` appropriately for client-only data needs. (See `11-client-loader.md`)
*   **Error Reporting:** Report tool errors or persistent blockers via `attempt_completion`.

*(Derived from v7.0 primary mode file sections 4 & 5)*