# Clerk Integration: React & Next.js Examples

Common patterns for integrating Clerk's frontend components and hooks.

## 1. Setup: `<ClerkProvider>`

Wrap your application root with `<ClerkProvider>` and provide your **Publishable Key**.

**Next.js (App Router - `layout.tsx`):**
```tsx
import { ClerkProvider } from '@clerk/nextjs';
import './globals.css';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider publishableKey={process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY}>
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  );
}
```

**React (e.g., `main.tsx` or `index.tsx`):**
```tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import { ClerkProvider } from '@clerk/clerk-react';
import App from './App';

const PUBLISHABLE_KEY = process.env.REACT_APP_CLERK_PUBLISHABLE_KEY; // Or Vite's import.meta.env...

if (!PUBLISHABLE_KEY) {
  throw new Error("Missing Clerk Publishable Key");
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <ClerkProvider publishableKey={PUBLISHABLE_KEY}>
      <App />
    </ClerkProvider>
  </React.StrictMode>,
);
```

## 2. Pre-built UI Components

Use Clerk's components for standard auth flows.

```tsx
import { SignInButton, SignUpButton, SignedIn, SignedOut, UserButton } from "@clerk/nextjs"; // or @clerk/clerk-react

function Header() {
  return (
    <header style={{ display: 'flex', justifyContent: 'space-between', padding: '1rem' }}>
      <h1>My App</h1>
      <div>
        <SignedOut>
          <Space> {/* Example using Ant Design Space */}
             <SignInButton mode="modal" /> {/* Can be modal or redirect */}
             <SignUpButton mode="redirect" redirectUrl="/dashboard" />
          </Space>
        </SignedOut>
        <SignedIn>
          {/* Mount the UserButton component */}
          <UserButton afterSignOutUrl="/" />
        </SignedIn>
      </div>
    </header>
  );
}

// --- Sign-in/Sign-up Pages (if using redirect flow) ---
// pages/sign-in/[[...index]].tsx (Next.js Pages Router example)
import { SignIn } from "@clerk/nextjs";

const SignInPage = () => (
  <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
    <SignIn path="/sign-in" routing="path" signUpUrl="/sign-up" />
  </div>
);
export default SignInPage;

// app/sign-in/[[...sign-in]]/page.tsx (Next.js App Router example)
import { SignIn } from "@clerk/nextjs";

export default function Page() {
  return <SignIn />;
}
```

## 3. Hooks for Auth State & User Data

Access authentication status and user information within your components.

```tsx
import { useUser, useAuth } from "@clerk/nextjs"; // or @clerk/clerk-react

function UserProfileInfo() {
  const { isLoaded, isSignedIn, user } = useUser();
  const { userId, sessionId, getToken } = useAuth(); // More auth details

  if (!isLoaded) {
    // Handle loading state however you like
    return <div>Loading...</div>;
  }

  if (isSignedIn) {
    return (
      <div>
        <p>Hello, {user.firstName}!</p>
        <p>Your User ID: {userId}</p>
        {/* <button onClick={async () => console.log(await getToken())}>Get Token</button> */}
      </div>
    );
  }

  return <p>Please sign in.</p>;
}
```

## 4. Conditional Rendering (`<SignedIn>`, `<SignedOut>`)

Convenience components to render content based on authentication status.

```tsx
import { SignedIn, SignedOut } from "@clerk/nextjs"; // or @clerk/clerk-react

function ConditionalContent() {
  return (
    <div>
      <SignedIn>
        <p>Welcome back! View your <a href="/dashboard">Dashboard</a>.</p>
      </SignedIn>
      <SignedOut>
        <p>Please <a href="/sign-in">Sign In</a> to continue.</p>
      </SignedOut>
    </div>
  );
}
```

*(Refer to the specific Clerk SDK documentation for your framework for detailed usage and advanced options.)*