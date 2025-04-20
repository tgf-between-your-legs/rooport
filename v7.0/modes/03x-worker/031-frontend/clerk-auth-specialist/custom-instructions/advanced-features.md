# Clerk Advanced Features

Notes on implementing Organizations, Multi-Factor Authentication (MFA), and Webhooks with Clerk.

## 1. Organizations

*   **Concept:** Allows grouping users into organizations, managing roles/permissions within those organizations, and handling invitations.
*   **Use Cases:** B2B SaaS applications, team collaboration tools.
*   **Frontend Components:**
    *   `<OrganizationSwitcher>`: Allows users to switch between organizations they belong to.
    *   `<OrganizationProfile>`: UI for managing organization settings (members, roles).
    *   `<CreateOrganization>`: UI for creating new organizations.
*   **Frontend Hooks:**
    *   `useOrganization()`: Access details about the currently active organization.
    *   `useOrganizationList()`: Access the list of organizations the user belongs to or can join.
    *   `useInvitations()`: Manage organization invitations.
*   **Backend/Server:**
    *   `auth().orgId`, `auth().orgRole`, `auth().orgSlug`: Access organization details in middleware/server components/API routes (Next.js).
    *   `getAuth(req).orgId`, etc. (Pages Router).
    *   `clerkClient.organizations.*`: Backend API methods for managing organizations, memberships, roles, invitations programmatically.
*   **Setup:** Enable Organizations in the Clerk Dashboard ("User & Authentication" -> "Organizations"). Configure roles and permissions.

## 2. Multi-Factor Authentication (MFA)

*   **Concept:** Adds an extra layer of security by requiring users to provide a second form of verification (e.g., TOTP app, SMS code) in addition to their password.
*   **Setup:** Enable desired MFA methods in the Clerk Dashboard ("User & Authentication" -> "Multi-factor").
*   **Frontend Integration:**
    *   Clerk's pre-built `<SignIn>` and `<UserProfile>` components automatically handle MFA enrollment and verification steps if enabled in the dashboard.
    *   For custom flows with Clerk Elements, specific steps and strategies related to MFA (e.g., `SignIn.Step name="verifications"` with `SignIn.Strategy name="phone_code"` or `SignIn.Strategy name="totp"`) will appear based on user configuration and dashboard settings.
*   **Backend:** No specific backend changes are usually required just to *enforce* MFA during sign-in, as Clerk handles the flow. Backend API protection remains the same (checking for a valid session).

## 3. Webhooks

*   **Concept:** Allow your backend application to receive real-time notifications from Clerk about events happening in your Clerk instance (e.g., user created, user updated, session ended, organization created).
*   **Use Cases:** Syncing user data to your own database, triggering custom workflows on user events, provisioning resources.
*   **Setup:**
    1.  Create an API endpoint (Webhook handler) in your backend application to receive POST requests from Clerk.
    2.  Register the endpoint URL in the Clerk Dashboard ("Webhooks" section).
    3.  Obtain the Webhook Signing Secret from the dashboard.
*   **Implementation (Webhook Handler):**
    *   **Verify Signature:** **Crucially**, verify the signature of incoming requests using the Signing Secret and headers provided by Clerk (`svix-id`, `svix-timestamp`, `svix-signature`) to ensure the request genuinely came from Clerk. Use Clerk's backend SDK helpers or the `svix` library.
    *   **Process Event:** Parse the JSON payload, check the `type` field (e.g., `user.created`, `session.ended`), and perform necessary actions in your backend (e.g., update database).
    *   **Respond Quickly:** Respond to Clerk with a `2xx` status code promptly to acknowledge receipt. Perform time-consuming tasks asynchronously (e.g., using a queue).
    ```typescript
    // Example: Next.js API Route Handler (Pages Router)
    import type { NextApiRequest, NextApiResponse } from 'next';
    import { Webhook } from 'svix'; // svix library for verification
    import { buffer } from 'micro'; // Helper to read raw body

    export const config = { api: { bodyParser: false } }; // Disable default body parser

    const webhookSecret = process.env.CLERK_WEBHOOK_SECRET || '';

    export default async function handler(req: NextApiRequest, res: NextApiResponse) {
      if (req.method !== 'POST') {
        return res.status(405).end('Method Not Allowed');
      }

      const payload = (await buffer(req)).toString();
      const headers = req.headers;

      const wh = new Webhook(webhookSecret);
      let msg: any; // Type according to Svix or Clerk event types
      try {
        msg = wh.verify(payload, headers as any);
      } catch (err) {
        console.error('Webhook verification failed:', err);
        return res.status(400).json({});
      }

      // Handle the event type
      const eventType = msg.type;
      console.log(`Received webhook event: ${eventType}`);

      if (eventType === 'user.created') {
        console.log('User created:', msg.data.id);
        // TODO: Sync user to your database
      } else if (eventType === 'user.updated') {
        console.log('User updated:', msg.data.id);
        // TODO: Update user in your database
      } // ... handle other event types

      res.status(200).json({}); // Respond to acknowledge receipt
    }
    ```

*(These are overviews. Always consult the detailed Clerk documentation for each feature.)*