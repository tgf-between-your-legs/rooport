# Session Management

## Core Concept: Server-Side Sessions

Remix typically handles sessions on the **server-side**. It provides utilities to create session storage adapters that manage how session data is stored (e.g., cookies, database, Redis) and how it's accessed in `loader` and `action` functions.

**Key Ideas:**

*   **Session Storage:** An adapter configured (often in `app/session.server.ts`) defining *where* session data lives (e.g., `createCookieSessionStorage`, `createMemorySessionStorage`, database, Redis).
*   **Session Object:** Represents data for a single user's session.
*   **Session Data:** Key-value pairs stored within the session object (e.g., `userId`, `themePreference`, flash messages).
*   **Getting Session:** Use `storage.getSession(request.headers.get("Cookie"))` in loaders/actions.
*   **Accessing Data:** `session.get("key")`.
*   **Setting Data:** `session.set("key", value)`.
*   **Flash Messages:** `session.flash("key", value)` stores data until the *next* read with `session.get()`. Useful for messages after redirects.
*   **Destroying Session:** `session.unset("key")` or `storage.destroySession(session)`.
*   **Committing Session:** **Crucial:** After modifying session data, **must commit** using `storage.commitSession(session)`. This generates a `Set-Cookie` header for the `Response`.

## Implementation Steps (Conceptual - using Cookie Storage)

**1. Create Session Storage:**

```typescript
// app/session.server.ts
import { createCookieSessionStorage } from "@remix-run/node"; // or adapter

if (!process.env.SESSION_SECRET) throw new Error("SESSION_SECRET must be set");

export const sessionStorage = createCookieSessionStorage({
  cookie: {
    name: "__session",
    httpOnly: true,
    path: "/",
    sameSite: "lax",
    secrets: [process.env.SESSION_SECRET], // Required
    secure: process.env.NODE_ENV === "production",
    // maxAge: 60 * 60 * 24 * 30, // Optional: 30 days
  },
});

// Helper functions (recommended)
export async function getSession(request: Request) {
  return sessionStorage.getSession(request.headers.get("Cookie"));
}

export async function getUserId(request: Request): Promise<string | undefined> {
  const session = await getSession(request);
  return session.get("userId");
}

// ... other helpers like requireUserId, createUserSession, logout ...
```

**2. Use Session in Loaders/Actions:**

```typescript
// app/routes/some-protected-route.tsx
import type { LoaderFunctionArgs, ActionFunctionArgs } from "@remix-run/node";
import { json, redirect } from "@remix-run/node";
import { getSession, sessionStorage, getUserId } from "~/session.server";

export async function loader({ request }: LoaderFunctionArgs) {
  const userId = await getUserId(request);
  if (!userId) return redirect("/login");
  // const userData = await getUserData(userId);
  return json({ userId /*, userData */ });
}

export async function action({ request }: ActionFunctionArgs) {
  const session = await getSession(request);
  const formData = await request.formData();
  const message = formData.get("message") as string;

  // Example: Setting a flash message
  session.flash("globalMessage", `Message "${message}" processed!`);

  // Commit the session to get the Set-Cookie header
  return redirect("/some-protected-route", {
    headers: { "Set-Cookie": await sessionStorage.commitSession(session) },
  });
}

// --- Component ---
// (Flash messages are typically read in the loader after redirect)
```

**3. Logout Example:**

```typescript
// app/routes/logout.tsx
import type { ActionFunctionArgs } from "@remix-run/node";
import { redirect } from "@remix-run/node";
import { getSession, sessionStorage } from "~/session.server";

export async function action({ request }: ActionFunctionArgs) {
  const session = await getSession(request);
  return redirect("/login", {
    headers: { "Set-Cookie": await sessionStorage.destroySession(session) },
  });
}
// Optional: Loader to redirect if already logged out
export async function loader() { return redirect("/"); }
```

Choose an appropriate storage adapter. Handle secrets securely. Always commit the session after modifications. Coordinate with authentication specialists.

*(Derived from `remix-sessions.md`)*