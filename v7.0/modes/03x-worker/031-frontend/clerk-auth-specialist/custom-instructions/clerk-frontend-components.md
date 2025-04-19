# Clerk: Frontend Components

Using Clerk's pre-built UI components for authentication and user management.

## Core Concept

Clerk provides several pre-built React components (within `@clerk/nextjs` or `@clerk/clerk-react`) that handle common authentication UI flows out-of-the-box. These components interact with the context provided by `<ClerkProvider>`.

**Key Components:**

*   **`<SignIn>`:** Renders a complete sign-in form, handling various authentication methods (password, social login, magic links, etc.) configured in your Clerk dashboard.
*   **`<SignUp>`:** Renders a complete sign-up form.
*   **`<UserButton>`:** Displays the user's avatar and provides a dropdown menu for managing the account (e.g., "Manage Account", "Sign Out"). Automatically shows a "Sign In" button if the user is logged out.
*   **`<UserProfile>`:** Renders a full user profile management interface where users can update their profile information, manage connected accounts, change passwords, enable MFA, etc.
*   **`<OrganizationSwitcher>`:** Allows users to switch between organizations they belong to (requires Organizations feature enabled).
*   **`<OrganizationProfile>`:** Interface for managing organization settings.
*   **`<CreateOrganization>`:** Component to allow users to create new organizations.
*   **Control Components:** `<SignedIn>`, `<SignedOut>`, `<Protect>` - Used to conditionally render content based on authentication state or required roles/permissions.

**Setup:**

*   Ensure `<ClerkProvider>` is set up correctly at the root of your application.
*   Import the desired components from the relevant Clerk package (`@clerk/nextjs` or `@clerk/clerk-react`).

## Using Pre-built Components

**1. Sign-In & Sign-Up Pages:**

*   Clerk components often manage their own routing internally when used with `routing="path"`. Create pages that render *only* the respective Clerk component.
*   Configure sign-in/sign-up redirect URLs in your Clerk Dashboard settings or via component props (`afterSignInUrl`, `afterSignUpUrl`).

```typescript
// Example for Next.js App Router: src/app/sign-in/[[...sign-in]]/page.tsx
// The [[...sign-in]] catches all sub-routes Clerk might use internally.
import { SignIn } from "@clerk/nextjs";

export default function Page() {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <SignIn path="/sign-in" routing="path" />
    </div>
  );
}

// Example for Next.js App Router: src/app/sign-up/[[...sign-up]]/page.tsx
import { SignUp } from "@clerk/nextjs";

export default function Page() {
   return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <SignUp path="/sign-up" routing="path" />
     </div>
  );
}
```

**2. User Button & Profile:**

*   Place `<UserButton>` typically in your application header or navigation bar.
*   Create a dedicated page for `<UserProfile>`.

```typescript
// Example Header Component (React/Next.js)
import { UserButton, SignedIn, SignedOut, SignInButton } from "@clerk/nextjs";
import Link from "next/link";

function Header() {
  return (
    <header style={{ display: 'flex', justifyContent: 'space-between', padding: '1rem', borderBottom: '1px solid #eee' }}>
      <Link href="/">My App</Link>
      <nav>
        <SignedIn> {/* Content shown only when signed in */}
          <Link href="/dashboard" style={{ marginRight: '1rem' }}>Dashboard</Link>
          <UserButton afterSignOutUrl="/" /> {/* Redirect to home after sign out */}
        </SignedIn>
        <SignedOut> {/* Content shown only when signed out */}
          <SignInButton mode="modal"> {/* Can open modal or redirect */}
             <button className="btn btn-primary">Sign In</button> {/* Example styling */}
          </SignInButton>
        </SignedOut>
      </nav>
    </header>
  );
}
export default Header;

// Example User Profile Page (Next.js App Router): src/app/user-profile/[[...user-profile]]/page.tsx
import { UserProfile } from "@clerk/nextjs";

export default function UserProfilePage() {
  return (
     <div style={{ display: 'flex', justifyContent: 'center', padding: '2rem' }}>
       <UserProfile path="/user-profile" routing="path" />
     </div>
  );
}
```

**3. Control Components (`<SignedIn>`, `<SignedOut>`, `<Protect>`):**

*   Conditionally render parts of your UI based on authentication status or permissions.
*   `<Protect>` allows checking roles or permissions defined in Clerk.

```jsx
import { SignedIn, SignedOut, Protect } from "@clerk/nextjs"; // or @clerk/clerk-react

function MyComponent() {
  return (
    <div>
      <SignedIn>
        <p>Welcome back, authenticated user!</p>
        {/* Protect content based on role */}
        <Protect role="org:admin">
          <button>Admin Action</button>
        </Protect>
        {/* Protect content based on permission */}
        <Protect permission="org:posts:create">
           <button>Create Post</button>
        </Protect>
      </SignedIn>
      <SignedOut>
        <p>Please sign in to access content.</p>
      </SignedOut>
    </div>
  );
}
```

Clerk's pre-built components significantly accelerate the implementation of standard authentication and user management UIs. For more custom experiences, consider using Clerk Elements or the frontend hooks (`useUser`, `useAuth`).

*(Refer to the official Clerk documentation for Components.)*