# App Router: Server vs. Client Components

Understanding the difference and when to use each type in the Next.js App Router.

## Core Concept: React Server Components (RSC)

The App Router uses RSCs, allowing components to render differently based on environment (server or client).

**1. Server Components (Default):**

*   **Location:** Any component in `app/` not marked `'use client'`. Includes `layout.tsx`, `page.tsx`.
*   **Execution:** Render **only on the server** (build time or request time). Code *never* sent to client.
*   **Capabilities:**
    *   Direct access to server resources (DBs, filesystem, APIs, env vars).
    *   Use `async/await` directly for data fetching.
    *   Import server-only libraries.
    *   Keep sensitive logic/keys on the server.
    *   Reduce client-side JS bundle.
*   **Limitations:**
    *   **No Hooks:** Cannot use `useState`, `useEffect`, `useReducer`, `useContext`, etc.
    *   **No Browser APIs:** Cannot use `window`, `localStorage`, DOM manipulation.
    *   **No Event Handlers:** Cannot use `onClick`, `onChange` directly on DOM elements.

**2. Client Components (`'use client'`):**

*   **Declaration:** Add `'use client'` directive at the **very top** of the file.
*   **Execution:** Pre-rendered on server, then hydrated and made interactive on the client. Code *is* sent to client bundle.
*   **Capabilities:**
    *   Use state/lifecycle hooks (`useState`, `useEffect`, etc.).
    *   Use browser-only APIs (`window`, DOM).
    *   Use event listeners (`onClick`, `onChange`).
    *   Use React Context.
    *   Use custom hooks relying on state/effects/browser APIs.
*   **Limitations:**
    *   Cannot directly access server resources (must fetch via Route Handlers, Server Actions, or props).
    *   Cannot be `async` functions directly (use `useEffect` for client-side fetching).
    *   Increase client-side JS bundle size.

## When to Use Which

*   **Server Components (Default):**
    *   Fetching server data.
    *   Accessing backend resources.
    *   Keeping sensitive logic/keys server-side.
    *   Reducing client JS.
    *   Rendering static or non-interactive UI.
*   **Client Components (`'use client'`):**
    *   Adding interactivity (event listeners).
    *   Using state and lifecycle hooks.
    *   Using browser-only APIs.
    *   Using React Context.
    *   Using custom hooks with state/effects/browser APIs.
    *   Using class components.

**Best Practice: Server Components First**

Default to Server Components. Only use `'use client'` when client-side capabilities are essential. Keep Client Components small and low in the component tree.

## Interaction Between Server and Client Components

*   **Server Components can import and render Client Components.**
*   **Client Components *cannot* directly import Server Components** (but can receive them as `children` or props).
*   **Props:** Data passed from Server to Client Components must be **serializable** (plain objects, arrays, primitives - no functions, Dates, complex classes).

```typescript
// app/page.tsx (Server Component)
import ClientButton from '@/components/ClientButton';
import ServerInfo from '@/components/ServerInfo'; // Another Server Component

async function getData() { /* ... fetch server data ... */ return { message: 'Data from Server!' }; }

export default async function HomePage() {
  const serverData = await getData();
  return (
    <div>
      <h1>Server/Client Demo</h1>
      <ServerInfo />
      {/* Pass serializable props and Server Component children to Client Component */}
      <ClientButton initialCount={5} serverMessage={serverData.message}>
         <p>Server-rendered children.</p>
         <ServerInfo /> {/* Server Component passed as children */}
      </ClientButton>
    </div>
  );
}

// components/ClientButton.tsx
'use client';
import React, { useState, useEffect } from 'react';

export default function ClientButton({ initialCount, serverMessage, children }) {
  const [count, setCount] = useState(initialCount);
  useEffect(() => { console.log('Window width:', window.innerWidth); }, []);

  return (
    <div>
      <p>Server Message: {serverMessage}</p>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
      <hr />
      {children} {/* Render children passed from Server Component */}
    </div>
  );
}

// components/ServerInfo.tsx (Server Component)
export default function ServerInfo() {
    const serverTime = new Date().toLocaleTimeString();
    return <p>Server Info - Rendered: {serverTime}</p>;
}
```

*(Refer to the official Next.js documentation on Server and Client Components.)*