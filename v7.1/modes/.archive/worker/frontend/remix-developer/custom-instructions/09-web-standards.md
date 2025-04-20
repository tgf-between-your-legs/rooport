# Leveraging Web Standards (Fetch API)

## Core Concept: Built on Web Fundamentals

Remix embraces standard Web APIs like `Request`, `Response`, `Headers`, `URLSearchParams`, `FormData`, and `fetch`. This aligns Remix code with standard web development practices.

**Key APIs Used:**

*   **`Request` Object:**
    *   Received by `loader` and `action` (`{ request }`).
    *   Standard Fetch API `Request` interface.
    *   Access details: `request.method`, `request.url`, `request.headers`, `await request.formData()`, `await request.json()`, `await request.text()`, `request.signal`.
*   **`Response` Object:**
    *   Returned by `loader` and `action` (or `null` for actions).
    *   Standard Fetch API `Response` interface.
    *   Create manually: `new Response(body, { status, statusText, headers })`.
    *   Remix helpers: `json(data, options)`, `redirect(url, options)`.
*   **`Headers` Object:**
    *   Standard Web API for HTTP headers.
    *   Used in `request.headers`, `new Response(..., { headers })`, and returned by the `headers` export.
    *   Methods: `get()`, `set()`, `append()`, `has()`, `delete()`.
*   **`fetch()` API:**
    *   Standard API for making HTTP requests.
    *   Use within loaders/actions to call external APIs or other Remix routes.

## Benefits

*   **Familiarity:** Easier learning curve for web developers.
*   **Interoperability:** Portable code across JS environments.
*   **Future-Proofing:** Aligns with the web platform.
*   **Leveraging Platform Features:** Directly uses features like streaming responses.

## Examples

**Accessing Request Data in `loader`:**

```typescript
import type { LoaderFunctionArgs } from "@remix-run/node";
import { json } from "@remix-run/node";

export async function loader({ request }: LoaderFunctionArgs) {
  const url = new URL(request.url);
  const query = url.searchParams.get("q");
  const userAgent = request.headers.get("User-Agent");
  // const results = await performSearch(query);
  return json({ results: query ? [`Result for ${query}`] : [] });
}
```

**Parsing Form Data in `action`:**

```typescript
import type { ActionFunctionArgs } from "@remix-run/node";
import { json, redirect } from "@remix-run/node";

export async function action({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const name = formData.get("name") as string;
  // ... validation ...
  // await updateUserProfile(userId, { name });
  return redirect("/profile");
}
```

**Returning Custom Headers:**

```typescript
import type { LoaderFunctionArgs, HeadersFunction } from "@remix-run/node";
import { json } from "@remix-run/node";

export async function loader({ request }: LoaderFunctionArgs) {
  const data = { message: "Hello" };
  return json(data, { headers: { "X-Custom-Loader": "Value" } });
}

export const headers: HeadersFunction = ({ loaderHeaders }) => {
  loaderHeaders.set("Cache-Control", "private, max-age=60");
  return loaderHeaders;
};
```

Remix provides a powerful foundation by building upon familiar web standards.

*(Combined from `remix-web-standards.md` and `web-standards.md`)*