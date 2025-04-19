# Clerk: Backend SDK (`clerkClient`)

Using the Clerk Backend SDK for server-side user and resource management.

## Core Concept

While much of Clerk's functionality is handled automatically by frontend components and backend middleware/helpers, the **Clerk Backend SDK** (`@clerk/backend` or framework-specific exports like from `@clerk/nextjs/server`) provides direct access to the Clerk API for server-side operations.

This is necessary for tasks like:

*   Programmatically creating, reading, updating, or deleting users.
*   Managing organization memberships and roles.
*   Sending invitations.
*   Managing session tokens or user bans.
*   Accessing user metadata or authentication details not included in the standard session token.

**Key Components:**

*   **`clerkClient`:** The main entry point for interacting with the Backend API. It's typically pre-configured and exported by framework SDKs (e.g., `@clerk/nextjs/server`) or can be created manually using your Secret Key.
*   **Resource Objects:** The SDK provides methods grouped by resource type (e.g., `clerkClient.users`, `clerkClient.organizations`, `clerkClient.invitations`, `clerkClient.sessions`).
*   **Methods:** Each resource object has methods corresponding to API actions (e.g., `clerkClient.users.getUser(userId)`, `clerkClient.users.createUser(params)`, `clerkClient.organizations.createOrganization(params)`).

**Setup:**

*   Install the appropriate Clerk SDK for your backend framework (e.g., `@clerk/nextjs`, `@clerk/remix`, `@clerk/clerk-sdk-node` for generic Node).
*   Ensure your `CLERK_SECRET_KEY` environment variable is set correctly on the server. The SDK usually reads this automatically.

## Common Use Cases & Examples

**Note:** These examples assume usage within a server-side context (API route, server component action, loader, etc.) where the SDK can securely access the secret key.

**1. Getting User Details:**

```typescript
// Example: Next.js API Route Handler
import { clerkClient } from '@clerk/nextjs/server';
import { NextResponse } from 'next/server';

export async function GET(req: Request) {
  // Assume userId is obtained securely, e.g., from auth() or a validated request param
  const userId = 'user_...'; // Replace with actual user ID logic

  try {
    const user = await clerkClient.users.getUser(userId);
    console.log('User Data:', user);
    // Access details like user.firstName, user.emailAddresses, user.publicMetadata, etc.
    return NextResponse.json(user);
  } catch (error) {
    console.error('Error fetching user:', error);
    return new NextResponse('Failed to fetch user', { status: 500 });
  }
}
```

**2. Updating User Metadata:**

*   Use `publicMetadata` for data accessible on the frontend via `useUser()`.
*   Use `privateMetadata` for sensitive data accessible only on the backend.
*   Use `unsafeMetadata` for data that can be set by the user (e.g., via `<UserProfile>`).

```typescript
// Example: Server Action (e.g., in Next.js or Astro)
import { clerkClient } from '@clerk/nextjs/server'; // Or appropriate SDK import
import { auth } from '@clerk/nextjs/server'; // Or getAuth, etc.

export async function updateUserRole(newRole: string) {
  'use server'; // If using Next.js Server Actions

  const { userId } = auth(); // Get current user's ID securely
  if (!userId) { throw new Error("Not authenticated"); }

  try {
    const updatedUser = await clerkClient.users.updateUserMetadata(userId, {
      publicMetadata: {
        // Spread existing metadata if needed: ...user.publicMetadata,
        role: newRole // Update or add the 'role' field
      }
      // Can also update privateMetadata or unsafeMetadata here
    });
    console.log('Updated user metadata:', updatedUser.publicMetadata);
    return { success: true };
  } catch (error) {
    console.error('Error updating metadata:', error);
    return { success: false, error: 'Failed to update role' };
  }
}
```

**3. Creating an Organization Programmatically:**

```typescript
import { clerkClient } from '@clerk/nextjs/server';
import { auth } from '@clerk/nextjs/server';

export async function createTeam(teamName: string) {
  'use server';
  const { userId } = auth();
  if (!userId) { throw new Error("Not authenticated"); }

  try {
    const organization = await clerkClient.organizations.createOrganization({
      name: teamName,
      createdBy: userId, // Associate the creator
    });

    // Optionally add the creator as an admin member immediately
    await clerkClient.organizations.createOrganizationMembership({
      organizationId: organization.id,
      userId: userId,
      role: 'org:admin', // Use role key defined in Clerk dashboard
    });

    console.log('Created organization:', organization.id);
    return { success: true, organizationId: organization.id };
  } catch (error) {
    console.error('Error creating organization:', error);
    return { success: false, error: 'Failed to create team' };
  }
}
```

**4. Listing Organization Members:**

```typescript
import { clerkClient } from '@clerk/nextjs/server';
import { auth } from '@clerk/nextjs/server';

export async function getTeamMembers() {
  'use server';
  const { orgId, orgRole } = auth(); // Get active org context

  if (!orgId || orgRole !== 'org:admin') {
    throw new Error("Not authorized or no active organization");
  }

  try {
    const memberships = await clerkClient.organizations.getOrganizationMembershipList({
      organizationId: orgId,
      limit: 100, // Add pagination if needed
    });
    console.log('Memberships:', memberships);
    // memberships is an array, each item has publicUserData (id, firstName, etc.) and role
    return { success: true, members: memberships };
  } catch (error) {
    console.error('Error fetching members:', error);
    return { success: false, error: 'Failed to fetch members' };
  }
}
```

## Security

*   **Secret Key:** The Backend SDK requires your `CLERK_SECRET_KEY`. Ensure it's only used in secure server-side environments and never exposed client-side.
*   **Authorization:** Always perform authorization checks within your backend code before executing sensitive operations via `clerkClient`. Verify the `userId`, `orgId`, `orgRole`, or custom claims obtained from the authenticated request context (`auth()`, `getAuth()`, `req.auth`). Do not solely rely on data passed from the client.

The Clerk Backend SDK provides comprehensive control over users, organizations, sessions, and more, enabling advanced server-side logic and integrations.

*(Refer to the official Clerk Backend SDK documentation.)*