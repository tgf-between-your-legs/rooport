# Custom Instructions: Backend Integration & Protection

Using Clerk's backend SDK (`clerkClient`) and server-side helpers/middleware for protection and management.

## 1. Backend Protection (Overview)

Protecting backend API routes and server-side logic involves:
1.  **Authenticating the Request:** Verifying the session token (JWT) from the `__session` cookie or `Authorization` header using Clerk's backend SDK/middleware and your **Secret Key**.
2.  **Accessing Auth State:** Retrieving `userId`, `sessionId`, `orgId`, `sessionClaims`, etc.
3.  **Enforcing Protection:** Checking for a valid `userId` (or roles/permissions from `sessionClaims`) and returning 401/403 errors, redirecting, or filtering data.

*(See `06-route-protection.md` for framework-specific protection examples using middleware and helpers like `auth()` and `getAuth()`)*.

## 2. Backend SDK (`clerkClient`)

While middleware/helpers handle *authentication* (verifying who the user is), the **Clerk Backend SDK** (`@clerk/backend` or framework exports like `@clerk/nextjs/server`) provides direct access to the Clerk API for server-side *management* operations using your **Secret Key**.

**Use Cases:**
*   Programmatically creating, reading, updating, deleting users (`clerkClient.users.*`).
*   Managing organizations, memberships, roles (`clerkClient.organizations.*`).
*   Sending invitations (`clerkClient.invitations.*`).
*   Managing sessions, bans (`clerkClient.sessions.*`, `clerkClient.bans.*`).
*   Accessing detailed user data not in the standard session token.

**Setup:**
*   Install the appropriate Clerk SDK (e.g., `@clerk/nextjs`).
*   Ensure `CLERK_SECRET_KEY` environment variable is set on the server.

**Common Examples (within server-side context):**

**a) Getting User Details:**
```typescript
import { clerkClient } from '@clerk/nextjs/server'; // Or appropriate SDK import

async function getUserDetails(userId: string) {
  try {
    const user = await clerkClient.users.getUser(userId);
    // Access user.firstName, user.emailAddresses, user.publicMetadata, etc.
    return user;
  } catch (error) { console.error('Error fetching user:', error); return null; }
}
```

**b) Updating User Metadata:**
*   `publicMetadata`: Accessible on frontend via `useUser()`.
*   `privateMetadata`: Accessible only on backend.
*   `unsafeMetadata`: Settable by user (e.g., via `<UserProfile>`).

```typescript
import { clerkClient, auth } from '@clerk/nextjs/server'; // Or appropriate SDK/auth import

export async function updateUserRole(targetUserId: string, newRole: string) {
  'use server'; // Example: Next.js Server Action
  const { userId: adminUserId, orgRole } = auth(); // Get current admin user's auth state
  if (!adminUserId || orgRole !== 'org:admin') { throw new Error("Not authorized"); }

  try {
    const updatedUser = await clerkClient.users.updateUserMetadata(targetUserId, {
      publicMetadata: { role: newRole } // Update or add the 'role' field
      // privateMetadata: { internal_id: '...' }
    });
    return { success: true };
  } catch (error) { console.error('Error updating metadata:', error); return { success: false }; }
}
```

**c) Creating an Organization Programmatically:**
```typescript
import { clerkClient, auth } from '@clerk/nextjs/server';

export async function createTeam(teamName: string) {
  'use server';
  const { userId } = auth();
  if (!userId) { throw new Error("Not authenticated"); }

  try {
    const organization = await clerkClient.organizations.createOrganization({
      name: teamName,
      createdBy: userId,
    });
    // Optionally add creator as admin
    await clerkClient.organizations.createOrganizationMembership({
      organizationId: organization.id,
      userId: userId,
      role: 'org:admin', // Use role key from Clerk dashboard
    });
    return { success: true, organizationId: organization.id };
  } catch (error) { console.error('Error creating org:', error); return { success: false }; }
}
```

**d) Listing Organization Members:**
```typescript
import { clerkClient, auth } from '@clerk/nextjs/server';

export async function getTeamMembers() {
  'use server';
  const { orgId, orgRole } = auth();
  if (!orgId || orgRole !== 'org:admin') { throw new Error("Not authorized"); }

  try {
    const memberships = await clerkClient.organizations.getOrganizationMembershipList({
      organizationId: orgId, limit: 100, // Add pagination if needed
    });
    // memberships is array, each item has publicUserData (id, firstName, etc.) and role
    return { success: true, members: memberships };
  } catch (error) { console.error('Error fetching members:', error); return { success: false }; }
}
```

**Security:**
*   **Secret Key:** Only use `clerkClient` in secure server-side environments where `CLERK_SECRET_KEY` is available.
*   **Authorization:** Always perform authorization checks (using `userId`, `orgId`, `orgRole`, `sessionClaims` from the verified request context) before executing sensitive `clerkClient` operations. Do not trust data passed directly from the client for authorization decisions.

The Backend SDK provides powerful server-side management capabilities, complementing the authentication handled by middleware and helpers.

*(Refer to the official Clerk Backend SDK documentation.)*