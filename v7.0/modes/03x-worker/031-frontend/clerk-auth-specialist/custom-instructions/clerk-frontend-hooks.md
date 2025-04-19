# Clerk: Frontend Hooks (`useUser`, `useAuth`, `useSession`)

Accessing user and authentication state in React components using Clerk hooks.

## Core Concept

Clerk provides several React hooks (within `@clerk/nextjs` or `@clerk/clerk-react`) to easily access authentication status, user information, and session details within your functional components. These hooks interact with the context provided by `<ClerkProvider>`.

**Key Hooks:**

*   **`useAuth()`:** Provides access to the core authentication state and methods.
    *   `isLoaded`: Boolean indicating if Clerk has finished loading. Crucial for preventing flicker or rendering based on incomplete state.
    *   `isSignedIn`: Boolean (`true`, `false`) or `undefined` (during loading). Indicates if a user is currently signed in.
    *   `userId`: String containing the authenticated user's ID, or `null` if signed out / loading.
    *   `sessionId`: String containing the active session ID, or `null`.
    *   `orgId`, `orgRole`, `orgSlug`: Organization context if the user is active in an organization.
    *   `getToken()`: Async function to retrieve the current session token (JWT).
    *   `signOut()`: Function to sign the user out.
*   **`useUser()`:** Provides access to the currently signed-in user's information.
    *   `isLoaded`: Boolean indicating if the user data has loaded.
    *   `isSignedIn`: Boolean indicating if a user is signed in.
    *   `user`: The user object containing details like `id`, `firstName`, `lastName`, `emailAddresses`, `profileImageUrl`, `publicMetadata`, etc., or `null` if signed out / loading.
*   **`useSession()`:** Provides access to details about the active session.
    *   `isLoaded`: Boolean indicating if the session data has loaded.
    *   `isSignedIn`: Boolean indicating if a user is signed in.
    *   `session`: The session object containing details like `id`, `status`, `lastActiveAt`, etc., or `null`.
*   **`useClerk()`:** Provides access to the ClerkJS instance for advanced use cases like navigating programmatically or opening Clerk components.
    *   `openSignIn()`, `openSignUp()`, `openUserProfile()`
    *   `signOut()`
    *   `navigate()`

**Setup:**

*   Ensure `<ClerkProvider>` is set up correctly at the root of your application.
*   Import the desired hooks from the relevant Clerk package (`@clerk/nextjs` or `@clerk/clerk-react`).

## Using Hooks

**1. Checking Authentication State & User Info:**

*   **Important:** Always check `isLoaded` before relying on `isSignedIn` or `user`/`session` data to avoid rendering based on intermediate loading states.

```jsx
import React from 'react';
import { useUser, useAuth } from '@clerk/nextjs'; // or @clerk/clerk-react

function UserInfo() {
  const { isLoaded: isAuthLoaded, isSignedIn, userId } = useAuth();
  const { isLoaded: isUserLoaded, user } = useUser();

  // Wait for both auth state and user data to load
  if (!isAuthLoaded || !isUserLoaded) {
    return <div>Loading authentication state...</div>;
  }

  if (isSignedIn) {
    return (
      <div>
        <p>Welcome, {user?.firstName || 'User'}!</p>
        <p>Your User ID is: {userId}</p>
        {/* Access other user properties safely */}
        <p>Email: {user?.primaryEmailAddress?.emailAddress}</p>
      </div>
    );
  } else {
    return <p>You are not signed in.</p>;
  }
}

export default UserInfo;
```

**2. Programmatic Sign Out & Navigation:**

```jsx
import React from 'react';
import { useClerk } from '@clerk/nextjs'; // or @clerk/clerk-react
import { useRouter } from 'next/navigation'; // Example using Next.js App Router

function SignOutButton() {
  const { signOut } = useClerk();
  const router = useRouter(); // Get router instance

  const handleSignOut = async () => {
    await signOut();
    router.push('/'); // Redirect after sign out
  };

  return <button onClick={handleSignOut}>Sign Out</button>;
}

export default SignOutButton;
```

**3. Getting Session Token for API Requests:**

*   Use `getToken()` from `useAuth` to retrieve the JWT for authenticating requests to your backend API.

```jsx
import React from 'react';
import { useAuth } from '@clerk/nextjs'; // or @clerk/clerk-react

function FetchProtectedData() {
  const { getToken, isSignedIn, isLoaded } = useAuth();
  const [data, setData] = React.useState(null);
  const [error, setError] = React.useState('');

  const fetchData = async () => {
    setError('');
    setData(null);
    if (!isSignedIn) {
      setError('You must be signed in to fetch data.');
      return;
    }

    try {
      const token = await getToken(); // Get the session token
      const response = await fetch('/api/protected-data', { // Your backend API endpoint
        headers: { Authorization: `Bearer ${token}` }, // Send token in header
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const result = await response.json();
      setData(result);
    } catch (err) {
      console.error(err);
      setError('Failed to fetch data.');
    }
  };

  if (!isLoaded) return <p>Loading...</p>;

  return (
    <div>
      <button onClick={fetchData} disabled={!isSignedIn}>Fetch Protected Data</button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
    </div>
  );
}

export default FetchProtectedData;
```

Clerk hooks provide a convenient and reactive way to access authentication state and user information within your React components, simplifying the process of building dynamic UIs based on user status. Remember to handle the `isLoaded` state appropriately.

*(Refer to the official Clerk documentation for Frontend Hooks.)*