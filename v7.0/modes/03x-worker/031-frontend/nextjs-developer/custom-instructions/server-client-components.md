# Next.js: Server vs. Client Components (App Router)

Understanding the difference and when to use each type in the Next.js App Router.

## Server Components (Default)

*   **Execution:** Render **only** on the server (at build time for static routes, or on-demand for dynamic routes/SSR). Their code is **never** sent to the client browser.
*   **Capabilities:**
    *   Directly access backend resources (databases, file system, external APIs) using `async/await`.
    *   Keep sensitive data and logic on the server (API keys, database queries).
    *   Reduce client-side JavaScript bundle size.
    *   Render quickly on the server and stream HTML to the client.
    *   Can import and render Client Components.
*   **Limitations:**
    *   **Cannot** use React hooks like `useState`, `useEffect`, `useContext`.
    *   **Cannot** use browser-only APIs (e.g., `window`, `localStorage`).
    *   **Cannot** use event listeners (`onClick`, `onChange`, etc.). Interactivity requires Client Components.
*   **Example (`app/page.tsx`):**
    ```tsx
    // This is a Server Component by default
    async function getData() {
      const res = await fetch('https://api.example.com/data', { cache: 'no-store' }); // Server-side fetch
      if (!res.ok) throw new Error('Failed to fetch');
      return res.json();
    }

    export default async function HomePage() {
      const data = await getData(); // Data fetching directly

      return (
        <main>
          <h1>Welcome (Server Component)</h1>
          <p>Data from server: {JSON.stringify(data)}</p>
          {/* Cannot use onClick here directly */}
          {/* <button onClick={() => alert('Hi!')}>Click Me</button> */}

          {/* Render a Client Component for interactivity */}
          <Counter client:load />
        </main>
      );
    }
    ```

## Client Components (`'use client'`)

*   **Execution:** Pre-rendered on the server (for initial HTML), then hydrated and executed **on the client** browser. Their JavaScript code **is** sent to the client.
*   **Directive:** Mark a component as a Client Component by adding the `'use client'` directive at the **very top** of the file.
*   **Capabilities:**
    *   Use React hooks (`useState`, `useEffect`, `useContext`, `useReducer`, etc.).
    *   Use browser-only APIs (`window`, `document`, `localStorage`).
    *   Add interactivity using event listeners (`onClick`, `onChange`, etc.).
*   **Limitations:**
    *   **Cannot** directly use `async/await` for data fetching in the component function body (use `useEffect` for client-side fetching, or receive data as props from a Server Component parent).
    *   **Cannot** directly access backend resources (file system, databases). Must fetch data via API routes or Server Actions.
    *   Increase the client-side JavaScript bundle size.
*   **Example (`app/components/Counter.tsx`):**
    ```tsx
    'use client'; // Mark as a Client Component

    import React, { useState } from 'react';

    export default function Counter() {
      const [count, setCount] = useState(0);

      return (
        <div>
          <p>Count: {count}</p>
          <button onClick={() => setCount(c => c + 1)}>Increment</button>
        </div>
      );
    }
    ```

## Key Principles & Best Practices

*   **Server Components First:** Start by building your UI with Server Components by default. Opt-into Client Components (`'use client'`) only when you specifically need client-side interactivity, state, lifecycle effects, or browser-only APIs.
*   **Keep Client Components Small:** Move Client Components down the component tree as far as possible. Instead of making a whole layout a Client Component just for one interactive button, make only the button (or its direct interactive parent) a Client Component and pass server-rendered components as children.
*   **Props Serialization:** Data passed as props from Server Components to Client Components must be serializable (plain objects, arrays, primitives - no functions, Dates, Maps, Sets, etc.).
*   **Importing:**
    *   Server Components can import and render Client Components.
    *   Client Components **cannot** directly import Server Components (but can receive them as props, e.g., `children`).
*   **Shared Components:** Components used by *both* Server and Client components must themselves be Client Components (or contain only logic compatible with both environments, which is rare for UI components).

*(Refer to the official Next.js documentation on Server and Client Components: https://nextjs.org/docs/app/building-your-application/rendering/server-components)*