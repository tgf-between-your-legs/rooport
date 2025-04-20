# Custom Instructions: Frontend Integration (React/Next.js)

This document covers setting up the Clerk provider, using pre-built components, and leveraging hooks for frontend integration, primarily focusing on React and Next.js.

## 1. Setup: `<ClerkProvider>`

The `<ClerkProvider>` component is the root of Clerk's functionality in your frontend application. It wraps your application and provides context for Clerk components and hooks.

**Key Responsibilities:**
*   Initializes the Clerk frontend SDK.
*   Requires your **Publishable Key** (`pk_test_...` or `pk_live_...`).
*   Manages the active session and user state on the client-side.
*   Provides configuration options for appearance, routing, and localization.

**Setup Examples:**

**Next.js (App Router - `layout.tsx`):**
```typescript
// src/app/layout.tsx
import { ClerkProvider } from '@clerk/nextjs';
import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = { /* ... */ };

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode; }>) {
  return (
    <ClerkProvider
      // publishableKey={process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY} // Optional: Key read automatically if env var set
      // appearance={{ baseTheme: dark }} // Example customization
    >
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  );
}
```

**Next.js (Pages Router - `_app.tsx`):**
```typescript
// src/pages/_app.tsx
import { ClerkProvider } from '@clerk/nextjs';
import type { AppProps } from 'next/app';
import '../styles/globals.css';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ClerkProvider
      {...pageProps}
      publishableKey={process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY}
    >
      <Component {...pageProps} />
    </ClerkProvider>
  );
}
export default MyApp;
```

**Create React App (CRA) / Vite React (`main.tsx` / `index.tsx`):**
```typescript
// src/main.tsx (Vite example)
import React from 'react';
import ReactDOM from 'react-dom/client';
import { ClerkProvider, SignedIn, SignedOut, RedirectToSignIn } from '@clerk/clerk-react';
import { BrowserRouter, Routes, Route, useNavigate } from 'react-router-dom';
import App from './App';
import './index.css';

const PUBLISHABLE_KEY = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY;
if (!PUBLISHABLE_KEY) { throw new Error("Missing Publishable Key"); }

function ClerkProviderWithRoutes() {
  const navigate = useNavigate();
  return (
    <ClerkProvider
      routerPush={(to) => navigate(to)}
      routerReplace={(to) => navigate(to, { replace: true })}
      publishableKey={PUBLISHABLE_KEY}
    >
      {/* Define Routes here, potentially wrapping protected routes */}
      <Routes>
        <Route path="/" element={<App />} />
        {/* Add SignIn/SignUp routes */}
        <Route path="/protected" element={
          <> <SignedIn> <ProtectedPage /> </SignedIn> <SignedOut> <RedirectToSignIn /> </SignedOut> </>
        }/>
      </Routes>
    </ClerkProvider>
  );
}
function ProtectedPage() { return <h2>Protected Content</h2>; }

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter> <ClerkProviderWithRoutes /> </BrowserRouter>
  </React.StrictMode>,
);
```

**Remix (`root.tsx`):** Requires `rootAuthLoader` and wrapping the `App` with `ClerkApp`. See `clerk-provider-frontend.md` for the full example.

**Key Props for `<ClerkProvider>`:**
*   `publishableKey`: Your publishable API key (required if not using Next.js env var).
*   `routerPush`, `routerReplace`: (For non-Next.js routers) Functions to integrate with your router's navigation methods.
*   `appearance`: Object for customizing the look and feel.
*   `localization`: Object for customizing text and language.

## 2. Pre-built UI Components

Use Clerk's components for standard auth flows: `<SignIn>`, `<SignUp>`, `<UserButton>`, `<UserProfile>`, `<OrganizationSwitcher>`, `<OrganizationProfile>`, `<CreateOrganization>`.

**Control Components:** `<SignedIn>`, `<SignedOut>`, `<Protect>` - Used to conditionally render content based on authentication state or required roles/permissions.

**Example Usage (Header):**
```tsx
import { UserButton, SignedIn, SignedOut, SignInButton, SignUpButton } from "@clerk/nextjs"; // or @clerk/clerk-react
import Link from "next/link";

function Header() {
  return (
    <header style={{ display: 'flex', justifyContent: 'space-between', padding: '1rem' }}>
      <Link href="/">My App</Link>
      <nav>
        <SignedIn>
          <Link href="/dashboard" style={{ marginRight: '1rem' }}>Dashboard</Link>
          <UserButton afterSignOutUrl="/" />
        </SignedIn>
        <SignedOut>
          <SignInButton mode="modal"> <button>Sign In</button> </SignInButton>
          <SignUpButton mode="redirect" redirectUrl="/dashboard"> <button>Sign Up</button> </SignUpButton>
        </SignedOut>
      </nav>
    </header>
  );
}
export default Header;
```

**Sign-In/Sign-Up Pages (Next.js App Router):**
Create pages like `app/sign-in/[[...sign-in]]/page.tsx` that render only the Clerk component:
```tsx
// app/sign-in/[[...sign-in]]/page.tsx
import { SignIn } from "@clerk/nextjs";
export default function Page() { return <SignIn />; }
```
(Similarly for `<SignUp>`, `<UserProfile>`, etc.)

**Conditional Rendering:**
```tsx
import { SignedIn, SignedOut, Protect } from "@clerk/nextjs";

function MyComponent() {
  return (
    <div>
      <SignedIn>
        <p>Welcome back!</p>
        <Protect role="org:admin"> <button>Admin Action</button> </Protect>
      </SignedIn>
      <SignedOut> <p>Please sign in.</p> </SignedOut>
    </div>
  );
}
```

## 3. Hooks for Auth State & User Data

Access authentication status and user information within your components. **Always check `isLoaded` before using other values.**

**Key Hooks:**
*   **`useAuth()`:** Provides `isLoaded`, `isSignedIn`, `userId`, `sessionId`, `orgId`, `orgRole`, `orgSlug`, `getToken()`, `signOut()`.
*   **`useUser()`:** Provides `isLoaded`, `isSignedIn`, `user` object (with `id`, `firstName`, `emailAddresses`, `publicMetadata`, etc.).
*   **`useSession()`:** Provides `isLoaded`, `isSignedIn`, `session` object.
*   **`useClerk()`:** Provides ClerkJS instance for `openSignIn()`, `openSignUp()`, `signOut()`, `navigate()`.

**Example Usage:**
```tsx
import React from 'react';
import { useUser, useAuth } from '@clerk/nextjs'; // or @clerk/clerk-react

function UserInfo() {
  const { isLoaded: isAuthLoaded, isSignedIn, userId, getToken } = useAuth();
  const { isLoaded: isUserLoaded, user } = useUser();

  if (!isAuthLoaded || !isUserLoaded) {
    return <div>Loading...</div>;
  }

  const handleFetch = async () => {
    if (!isSignedIn) return;
    try {
      const token = await getToken();
      const response = await fetch('/api/protected-data', {
        headers: { Authorization: `Bearer ${token}` },
      });
      // ... handle response
    } catch (error) { console.error(error); }
  };

  if (isSignedIn) {
    return (
      <div>
        <p>Welcome, {user?.firstName || 'User'}! (ID: {userId})</p>
        <button onClick={handleFetch}>Fetch Data</button>
      </div>
    );
  } else {
    return <p>You are not signed in.</p>;
  }
}
export default UserInfo;
```

*(Refer to the official Clerk documentation for Components and Hooks.)*