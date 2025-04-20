# Remix Caching (`headers` Export)

Controlling HTTP caching behavior for Remix routes using the `headers` function.

## Core Concept

Remix allows you to define standard HTTP caching headers (`Cache-Control`, `ETag`, etc.) for each route by exporting a `headers` function from the route module. This function runs **only on the server** after your `loader` or `action` has successfully executed (and didn't throw or redirect).

These headers instruct browsers and CDNs on how to cache the response for the specific route.

## `headers` Function

*   **Syntax:** Export a function named `headers`. It receives an object containing references to the headers returned by parent routes (`parentHeaders`), the current route's loader (`loaderHeaders`), and the current route's action (`actionHeaders`).
*   **Return Value:** Must return a `HeadersInit` object (either a `Headers` object or a plain object literal with string values). These headers will be merged with headers set on any `Response` object returned by the `loader` or `action`.
    ```typescript
    // app/routes/some-data.tsx
    import { json, LoaderFunctionArgs, HeadersFunction } from "@remix-run/node";

    export async function loader({ request }: LoaderFunctionArgs) {
      // Fetch data that changes infrequently
      // const data = await getInfrequentData();
      const data = { message: "Cached for 1 hour", timestamp: Date.now() }; // Placeholder

      // Return data with potential cache headers from the source
      return json(data, {
        headers: {
          // Example: Source might suggest a cache duration
          "Cache-Control": "private, max-age=3600",
          "X-Source": "Database",
        },
      });
    }

    // Define headers for this specific route
    export const headers: HeadersFunction = ({
      loaderHeaders, // Headers returned by the loader above
      parentHeaders, // Headers from parent routes (e.g., root.tsx)
      // actionHeaders // Headers returned by the action (if applicable)
    }) => {
      console.log("Loader Headers:", loaderHeaders.get("Cache-Control"));
      console.log("Parent Headers:", parentHeaders.get("Cache-Control"));

      // Merge or override headers
      // Example: Prioritize loader's Cache-Control, fallback to 1 minute
      const cacheControl = loaderHeaders.get("Cache-Control") ?? "public, max-age=60";

      return {
        "Cache-Control": cacheControl,
        "X-Custom-Route-Header": "My Value",
        // You can merge headers from parents if needed
        // "X-Parent-Data": parentHeaders.get("X-Parent-Data") ?? "default",
      };
    };

    // Component...
    export default function SomeDataRoute() {
      // ... useLoaderData ...
      return <div>...</div>;
    }
    ```

## Common `Cache-Control` Directives

*   **`public`**: Allows caching by intermediate caches (like CDNs).
*   **`private`**: Allows caching only by the end user's browser (for personalized content).
*   **`no-cache`**: Requires the cache to revalidate with the origin server before serving a cached response (checks if content changed using `ETag` or `Last-Modified`).
*   **`no-store`**: Disallows caching completely. The response must be fetched from the origin server every time.
*   **`max-age=<seconds>`**: Specifies the maximum time the response can be considered fresh.
*   **`s-maxage=<seconds>`**: Like `max-age`, but specifically for shared caches (CDNs). Often overrides `max-age`.
*   **`stale-while-revalidate=<seconds>`**: Allows a cache to serve a stale response while it revalidates in the background.
*   **`must-revalidate`**: Tells caches they must revalidate stale responses and not serve them.

## Strategy

*   **Static Content:** For routes with content that rarely changes, use long `max-age` or `s-maxage` values (e.g., `public, max-age=31536000` - 1 year).
*   **Infrequently Changing Content:** Use moderate `max-age`/`s-maxage` (e.g., minutes or hours) combined with `stale-while-revalidate` for a good balance of freshness and speed.
*   **Personalized Content:** Use `private, no-cache` or `private, max-age=0, must-revalidate` to ensure freshness for the specific user while allowing browser caching for revalidation.
*   **Highly Dynamic Content:** Use `no-store` if the data must be absolutely fresh on every request (though this impacts performance).

## Interaction with Loader/Action Headers

*   Headers set directly on the `Response` returned by `loader` or `action` are available within the `headers` function via `loaderHeaders` or `actionHeaders`.
*   The headers returned by the `headers` function are **merged** with the headers from the `loader`/`action` response. If the same header key exists in both, the value returned by the `headers` function takes precedence.

*(Refer to the official Remix Headers documentation: https://remix.run/docs/en/main/route/headers and MDN Cache-Control docs: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control)*