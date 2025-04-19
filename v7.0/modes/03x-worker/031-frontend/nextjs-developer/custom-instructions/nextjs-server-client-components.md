# Next.js: Server vs. Client Components (App Router)

Understanding the difference between Server and Client Components in the Next.js App Router.

## Core Concept: React Server Components (RSC)

The Next.js App Router is built on React Server Components (RSC), a new architecture that allows rendering components differently based on where they run (server or client).

**1. Server Components (Default):**

*   **Location:** Any React component inside the `app/` directory (and not marked with `'use client'`) is a Server Component by default. This includes `layout.tsx` and `page.tsx`.
*   **Execution:** Render **only on the server** (at build time for static routes, or request time for dynamic routes/SSR). Their code is *never* sent to the client browser.
*   **Capabilities:**
    *   Can directly access server-side resources (databases, file system, backend APIs, environment variables) without needing an extra API layer.
    *   Can use `async/await` directly for data fetching within the component.
    *   Can import server-only libraries or utilities.
    *   Render to a static description (React Server Component Payload) sent to the client.
*   **Limitations:**
    *   **Cannot use hooks** that depend on browser state or interactivity (`useState`, `useEffect`, `useReducer`, etc.).
    *   **Cannot use browser-only APIs** (`window`, `localStorage`, DOM manipulation).
    *   **Cannot use React Context** directly (Context providers need to be Client Components).
    *   Event handlers (`onClick`, `onChange`, etc.) cannot be passed directly to DOM elements.

**2. Client Components:**

*   **Declaration:** Mark a component as a Client Component by adding the **`'use client'` directive** at the very top of the file.
*   **Execution:** Pre-rendered on the server (for initial load), then "hydrated" and made interactive on the client using JavaScript. Their code *is* sent to the client bundle.
*   **Capabilities:**
    *   Can use React state hooks (`useState`, `useEffect`, `useReducer`, `useContext`, etc.).
    *   Can use browser-only APIs (`window`, DOM).
    *   Can use event listeners (`onClick`, `onChange`, etc.).
*   **Limitations:**
    *   Cannot directly access server-side resources (must fetch data via Route Handlers, Server Actions, or props passed from Server Components).
    *   Cannot be `async` functions directly (use `useEffect` for data fetching if needed client-side).

## When to Use Which

*   **Server Components (Default):**
    *   Fetching server-side data.
    *   Accessing backend resources directly (databases, file system).
    *   Keeping sensitive information/logic on the server (API keys, business logic).
    *   Reducing client-side JavaScript bundle size.
    *   Rendering static content or UI that doesn't require interactivity or state.
*   **Client Components (`'use client'`):**
    *   Adding interactivity (event listeners like `onClick`, `onChange`).
    *   Using state and lifecycle hooks (`useState`, `useEffect`, `useReducer`).
    *   Using browser-only APIs (`window`, `localStorage`, `navigator`).
    *   Using React Context.
    *   Using custom hooks that rely on state, effects, or browser APIs.
    *   Using class components (which inherently rely on state).

**Best Practice: Server Components First**

Start by building components as Server Components. Only add the `'use client'` directive when you specifically need client-side capabilities (interactivity, state, effects, browser APIs). Keep Client Components as small and specific as possible ("move client components down the tree").

## Interaction Between Server and Client Components

*   **Server Components can import and render Client Components.**
*   **Client Components *cannot* directly import Server Components.** (You can pass Server Components as `children` or props to Client Components).
*   **Props:** Data passed from a Server Component to a Client Component must be **serializable** (convertible to JSON). Functions, Dates, complex classes, etc., cannot be passed directly.

```typescript
// app/page.tsx (Server Component)
import ClientButton from '@/components/ClientButton';
import ServerInfo from '@/components/ServerInfo'; // Another Server Component

async function getData() { /* ... fetch server data ... */ return { message: 'Hello from Server!' }; }

export default async function HomePage() {
  const serverData = await getData();

  return (
    <div>
      <h1>Server/Client Demo</h1>
      <ServerInfo /> {/* Render another Server Component */}

      {/* Render a Client Component, passing serializable props */}
      <ClientButton initialCount={5} serverMessage={serverData.message}>
         {/* You CAN pass Server Components as children to Client Components */}
         <p>This paragraph is rendered on the server and passed as children.</p>
         <ServerInfo /> {/* This Server Component is passed as children */}
      </ClientButton>
    </div>
  );
}

// components/ClientButton.tsx
'use client'; // Mark as Client Component

import React, { useState, useEffect } from 'react';

// Props received must be serializable
export default function ClientButton({ initialCount, serverMessage, children }) {
  const [count, setCount] = useState(initialCount);

  useEffect(() => {
    // Can use browser APIs
    console.log('Window width:', window.innerWidth);
  }, []);

  return (
    <div>
      <p>Message from server prop: {serverMessage}</p>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
      <hr />
      {/* Render children passed from Server Component */}
      {children}
    </div>
  );
}

// components/ServerInfo.tsx (Server Component)
// No 'use client' directive
export default function ServerInfo() {
    // Cannot use useState, useEffect, etc.
    const serverTime = new Date().toLocaleTimeString();
    return <p>Server Info Component - Rendered at: {serverTime}</p>;
}
```

Understanding the distinction and appropriate use cases for Server and Client Components is fundamental to building efficient and interactive applications with the Next.js App Router.

*(Refer to the official Next.js documentation on Server Components and Client Components.)*