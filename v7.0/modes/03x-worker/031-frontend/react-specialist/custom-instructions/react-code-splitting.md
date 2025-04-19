# React: Code Splitting (`React.lazy`, `Suspense`)

Improving initial load performance by splitting code into smaller chunks and loading them on demand.

## Core Concept: Code Splitting

By default, most React build tools (like Create React App, Next.js, Vite) bundle all the application's JavaScript code into a single file (or a few core files). While simple, this means users download *all* the code upfront, even for parts of the application they might not visit immediately, leading to slower initial page loads.

**Code Splitting** is the process of breaking down this large bundle into smaller chunks that can be loaded dynamically or in parallel. React provides built-in support for code splitting via dynamic `import()` syntax combined with `React.lazy` and `React.Suspense`.

**Benefits:**

*   **Faster Initial Load:** Users only download the essential code needed for the initial view.
*   **Improved Performance:** Reduces the amount of JavaScript that needs to be parsed and executed upfront.
*   **On-Demand Loading:** Load code for specific features or routes only when the user navigates to them.

## Implementation

**1. Dynamic `import()`:**

*   Instead of a static import (`import MyComponent from './MyComponent'`), use the dynamic `import('./MyComponent')` syntax.
*   This tells the build tool (Webpack, Vite) to create a separate chunk for `./MyComponent` and its dependencies.
*   Dynamic `import()` returns a **Promise** that resolves to the module containing the default export.

**2. `React.lazy(loadFn)`:**

*   A function that lets you render a dynamically imported component as a regular component.
*   Takes a function `loadFn` that **must** call a dynamic `import()`.
*   Returns a special React component that knows how to load the chunk when it's first rendered.

**3. `<Suspense fallback={...}>`:**

*   A component that lets you specify a **loading indicator** (the `fallback` prop) while lazy-loaded components are being fetched and loaded.
*   Wrap the `React.lazy` component (or any part of the tree that might suspend during data fetching in frameworks like Next.js) with `<Suspense>`.
*   You can place multiple lazy components under a single Suspense boundary.

## Example

```jsx
import React, { Suspense, useState } from 'react';

// Static import for components always needed initially
import LoadingSpinner from './LoadingSpinner';
import Header from './Header';

// --- Dynamic Import using React.lazy ---
// The component './components/AdminPanel' will be in a separate chunk
const AdminPanel = React.lazy(() => import('./components/AdminPanel'));
const UserProfile = React.lazy(() => import('./components/UserProfile'));

function App() {
  const [showAdmin, setShowAdmin] = useState(false);
  const [showProfile, setShowProfile] = useState(false);

  return (
    <div>
      <Header />
      <h1>Code Splitting Demo</h1>

      <button onClick={() => setShowAdmin(prev => !prev)}>Toggle Admin Panel</button>
      <button onClick={() => setShowProfile(prev => !prev)}>Toggle User Profile</button>

      <hr />

      {/* --- Use Suspense to provide fallback UI --- */}
      <Suspense fallback={<LoadingSpinner />}>
        {/* AdminPanel code is loaded only when showAdmin becomes true */}
        {showAdmin && <AdminPanel />}
      </Suspense>

      <hr />

      <Suspense fallback={<p>Loading profile...</p>}>
        {/* UserProfile code is loaded only when showProfile becomes true */}
        {showProfile && <UserProfile userId={123} />}
      </Suspense>

    </div>
  );
}

export default App;

// --- Example components (in separate files) ---

// components/AdminPanel.tsx
// export default function AdminPanel() {
//   // ... complex admin UI ...
//   return <div>Admin Section</div>;
// }

// components/UserProfile.tsx
// export default function UserProfile({ userId }) {
//   // ... fetch user data, display profile ...
//   return <div>Profile for User {userId}</div>;
// }

// components/LoadingSpinner.tsx
// export default function LoadingSpinner() {
//   return <div>Loading...</div>;
// }
```

## Route-Based Code Splitting

Code splitting is most effective when applied at the route level. Most React frameworks and routers offer built-in support:

*   **Next.js (App Router):** Code splitting is automatic based on `page.tsx` files. `loading.tsx` integrates with `Suspense`.
*   **Next.js (Pages Router):** Use dynamic `import()` with `next/dynamic`.
*   **React Router:** Use `React.lazy` and `Suspense` directly within your route configuration.

```jsx
// Example with React Router v6
import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

const HomePage = lazy(() => import('./routes/Home'));
const AboutPage = lazy(() => import('./routes/About'));

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link> | <Link to="/about">About</Link>
      </nav>
      <Suspense fallback={<div>Loading page...</div>}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
        </Routes>
      </Suspense>
    </Router>
  );
}
```

Code splitting with `React.lazy` and `Suspense` is a powerful technique for improving the initial load performance of React applications by deferring the loading of non-critical code.

*(Refer to the official React documentation on Code Splitting.)*