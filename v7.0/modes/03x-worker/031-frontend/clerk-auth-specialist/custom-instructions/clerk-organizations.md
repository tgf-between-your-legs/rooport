# Clerk: Organizations

Implementing multi-tenancy and team features using Clerk Organizations.

## Core Concept

Clerk Organizations allow you to model B2B (Business-to-Business) scenarios or applications where users belong to teams, companies, or groups. Users can be members of multiple organizations and have different roles within each.

**Key Features:**

*   **Multi-Tenancy:** Isolate data and access based on the active organization.
*   **Membership Management:** Invite users, manage memberships (roles, permissions).
*   **Roles & Permissions:** Define custom roles (e.g., `admin`, `member`) and permissions within organizations. These can be stored in Clerk metadata and included in session tokens via JWT Templates.
*   **UI Components:** Pre-built components like `<OrganizationSwitcher>`, `<OrganizationProfile>`, `<CreateOrganization>`.
*   **Backend API Access:** Manage organizations and memberships programmatically using the Clerk Backend SDK (`clerkClient.organizations`, `clerkClient.users`).

## Setup

1.  **Enable Organizations:** Turn on the Organizations feature in your Clerk Dashboard settings (**Organizations** section).
2.  **Configure Roles/Permissions (Optional):** Define custom organization roles and permissions in the Clerk Dashboard if needed.
3.  **Frontend Setup:** Ensure `<ClerkProvider>` is set up.

## Using Organization Components & Hooks

**1. `<OrganizationSwitcher>`:**

*   Allows authenticated users to view their organizations and switch between them (or create a new one).
*   Typically placed in the application header or user menu.
*   Handles updating the user's active organization session state.

```jsx
import { OrganizationSwitcher, SignedIn } from "@clerk/nextjs"; // or @clerk/clerk-react

function Header() {
  return (
    <header>
      {/* ... other header content ... */}
      <SignedIn>
        <OrganizationSwitcher afterCreateOrganizationUrl="/dashboard" /> {/* Example prop */}
      </SignedIn>
    </header>
  );
}
```

**2. `<OrganizationProfile>`:**

*   Provides a UI for users to manage the settings of the *currently active* organization (if they have permission). Includes member management, role assignments, etc.
*   Typically rendered on a dedicated organization settings page.

```jsx
// Example Org Settings Page (Next.js App Router)
// src/app/organization-settings/[[...organization-profile]]/page.tsx
import { OrganizationProfile } from "@clerk/nextjs";

export default function OrgSettingsPage() {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', padding: '2rem' }}>
      <OrganizationProfile path="/organization-settings" routing="path" />
    </div>
  );
}
```

**3. `<CreateOrganization>`:**

*   Provides a UI for users to create a new organization.

```jsx
// Example Create Org Page (Next.js App Router)
// src/app/create-organization/[[...create-organization]]/page.tsx
import { CreateOrganization } from "@clerk/nextjs";

export default function CreateOrgPage() {
  return (
     <div style={{ display: 'flex', justifyContent: 'center', padding: '2rem' }}>
       <CreateOrganization path="/create-organization" routing="path" />
     </div>
  );
}
```

**4. Accessing Organization State (Hooks):**

*   **`useAuth()`:** Provides `orgId`, `orgRole`, `orgSlug` for the *currently active* organization in the user's session.
*   **`useOrganization()`:** Provides details about the *currently active* organization (`organization`, `isLoaded`, `membership`).
*   **`useOrganizationList()`:** Provides a list of all organizations the user is a member of (`organizationList`, `isLoaded`, `setActive`).

```jsx
import React from 'react';
import { useAuth, useOrganization, useOrganizationList } from '@clerk/nextjs'; // or @clerk/clerk-react

function OrgInfo() {
  const { isLoaded: isAuthLoaded, orgId, orgRole } = useAuth();
  const { organization, isLoaded: isOrgLoaded } = useOrganization(); // Current active org
  const { organizationList, isLoaded: isListLoaded, setActive } = useOrganizationList(); // List of all user's orgs

  if (!isAuthLoaded || !isOrgLoaded || !isListLoaded) {
    return <div>Loading organization data...</div>;
  }

  if (!orgId || !organization) {
    return <div>No active organization selected.</div>;
  }

  return (
    <div>
      <h2>Active Organization: {organization.name}</h2>
      <p>Your Role: {orgRole}</p>
      <p>Org ID: {orgId}</p>

      <h3>Your Organizations:</h3>
      <ul>
        {organizationList.map(({ organization: org }) => (
          <li key={org.id}>
            {org.name}
            {/* Button to switch active organization */}
            {org.id !== orgId && (
              <button onClick={() => setActive({ organization: org.id })}>
                Switch to {org.name}
              </button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
```

## Protecting Routes Based on Organization/Role

*   **Middleware (`clerkMiddleware`):** Use the `protect()` function with a condition checking `orgId`, `orgRole`, or `orgPermission`.

```typescript
// middleware.ts (App Router Example)
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

const isAdminRoute = createRouteMatcher(['/admin(.*)']);

export default clerkMiddleware((auth, req) => {
  if (isAdminRoute(req)) {
    // Protects /admin routes, requires sign-in AND admin role in the active org
    auth().protect((has) => {
      return has({ role: 'org:admin' }); // Assumes 'admin' role defined in Clerk
    });
  }
  // Add other public/protected routes as needed...
});

export const config = { matcher: [ /* ... */ ] };
```

*   **Server Components/Loaders (`auth()` / `getAuth()`):** Check the `orgId`, `orgRole`, or `orgPermission` properties returned by the auth helpers.

```typescript
// Example Server Component check
import { auth } from '@clerk/nextjs/server';

function AdminOnlyComponent() {
  const { orgRole } = auth();

  if (orgRole !== 'org:admin') {
    return <p>Access Denied.</p>;
  }

  return <div>Admin Content</div>;
}
```

Clerk Organizations provide a robust foundation for building multi-tenant applications with role-based access control.

*(Refer to the official Clerk Organizations documentation.)*