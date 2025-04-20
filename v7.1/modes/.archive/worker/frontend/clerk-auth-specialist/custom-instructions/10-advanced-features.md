# Custom Instructions: Advanced Features (Organizations, MFA)

Implementing multi-tenancy with Organizations and enhancing security with Multi-Factor Authentication (MFA).

## 1. Organizations

Clerk Organizations enable multi-tenancy (B2B, teams) by grouping users and managing roles/permissions within those groups.

**Key Concepts:**
*   **Multi-Tenancy:** Isolate data/access based on the active organization.
*   **Membership Management:** Invite users, manage roles.
*   **Roles & Permissions:** Define custom roles (e.g., `admin`, `member`) in the Clerk Dashboard. Map these to JWT claims for backend authorization.

**Setup:**
1.  Enable Organizations in Clerk Dashboard (**Organizations** section).
2.  Define custom roles/permissions if needed.

**Frontend Components & Hooks:**
*   **`<OrganizationSwitcher>`:** Allows users to switch between/create organizations. Place in header/menu.
    ```jsx
    <OrganizationSwitcher afterCreateOrganizationUrl="/dashboard" />
    ```
*   **`<OrganizationProfile>`:** UI for managing the active organization's settings (members, roles). Use on a dedicated page (e.g., `/organization-settings`).
    ```jsx
    <OrganizationProfile path="/organization-settings" routing="path" />
    ```
*   **`<CreateOrganization>`:** UI for creating new organizations. Use on a dedicated page (e.g., `/create-organization`).
    ```jsx
    <CreateOrganization path="/create-organization" routing="path" />
    ```
*   **`useAuth()`:** Provides `orgId`, `orgRole`, `orgSlug` for the active organization.
*   **`useOrganization()`:** Provides details of the active organization (`organization`, `isLoaded`, `membership`).
*   **`useOrganizationList()`:** Lists all user's organizations (`organizationList`, `isLoaded`, `setActive`).

**Example Hook Usage:**
```jsx
import { useAuth, useOrganization, useOrganizationList } from '@clerk/nextjs';

function OrgInfo() {
  const { isLoaded: isAuthLoaded, orgId, orgRole } = useAuth();
  const { organization, isLoaded: isOrgLoaded } = useOrganization();
  const { organizationList, isLoaded: isListLoaded, setActive } = useOrganizationList();

  if (!isAuthLoaded || !isOrgLoaded || !isListLoaded) return <div>Loading...</div>;
  if (!orgId || !organization) return <div>No active organization.</div>;

  return (
    <div>
      <h2>Active: {organization.name} (Role: {orgRole})</h2>
      {/* Button to switch orgs using setActive({ organization: org.id }) */}
    </div>
  );
}
```

**Backend/Server Protection:**
*   Use middleware (`clerkMiddleware`) or server helpers (`auth()`, `getAuth()`) to check `orgId`, `orgRole`, or permissions from `sessionClaims`.
    ```typescript
    // Middleware example
    auth().protect(has => has({ role: 'org:admin' }));

    // Server Component/API example
    const { orgId, orgRole } = auth();
    if (orgRole !== 'org:admin') { /* Deny access */ }
    ```
*   Use `clerkClient.organizations.*` for programmatic management (create org, add members, etc.). See `08-backend-integration.md`.

## 2. Multi-Factor Authentication (MFA)

Adds an extra verification step (e.g., TOTP app, SMS code).

**Setup:**
1.  Enable desired MFA factors (Authenticator App, SMS) in Clerk Dashboard (**Multi-factor authentication** section).
2.  Configure if MFA is optional or required (for all users or specific roles).

**Frontend Integration:**
*   **Pre-built Components (`<SignIn>`, `<UserProfile>`):** Automatically handle MFA enrollment and verification steps if enabled. `<UserProfile>` allows users to manage their MFA methods.
*   **Clerk Elements:** Use `<SignIn.Step name="verifications">` and elements like `<SignIn.Action strategy="verification_code">` or `<SignIn.Action strategy="backup_code">` with `<Clerk.Input name="code">`.

**Example MFA Step with Elements:**
```jsx
// Inside <SignIn.Root>
<SignIn.Step name="verifications" asChild>
  <form>
    <p>Enter the code from your authenticator app or SMS.</p>
    <SignIn.Action strategy="verification_code" submit>
      <Clerk.Field name="code">
        <Clerk.Label>Verification Code</Clerk.Label>
        <Clerk.Input type="text" required inputMode="numeric" />
        <Clerk.FieldError />
      </Clerk.Field>
      <button type="submit">Verify Code</button>
      <SignIn.GlobalError />
    </SignIn.Action>
    <SignIn.Action navigate="choose-strategy" strategy="backup_code">
      <button type="button">Use Backup Code</button>
    </SignIn.Action>
    {/* ... Back button ... */}
  </form>
</SignIn.Step>
// Add <SignIn.Step name="backup_code"> similarly
```

**Backend Considerations:**
*   MFA status is typically handled automatically by Clerk's session verification. The session token is usually only considered fully valid if required MFA checks passed.
*   No specific backend code is usually needed *just* for MFA verification during sign-in.

*(Refer to the official Clerk documentation for Organizations and MFA.)*