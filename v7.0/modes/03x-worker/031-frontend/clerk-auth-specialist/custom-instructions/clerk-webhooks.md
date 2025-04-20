# Clerk: Handling Webhooks

Receiving and verifying webhook events from Clerk.

## Core Concept

Webhooks allow Clerk to send real-time notifications to your backend application when specific events occur within your Clerk instance (e.g., user created, user updated, session ended, organization created). This enables you to synchronize data with your own database, trigger custom workflows, or react to authentication events.

**Key Features:**

*   **Event-Driven:** Receive notifications for various user, session, and organization events.
*   **Backend Integration:** Requires a dedicated API endpoint in your backend to receive webhook POST requests from Clerk.
*   **Security:** Webhook requests must be verified using a signing secret to ensure they genuinely originated from Clerk.
*   **Payload:** Each webhook event contains a JSON payload with details about the event type and associated data.

## Setup

1.  **Create a Webhook Endpoint:**
    *   Create a new API route in your backend application (e.g., `/api/webhooks/clerk` in Next.js, `/webhooks/clerk` in Express). This endpoint must be publicly accessible.
    *   This endpoint will receive POST requests from Clerk.
2.  **Configure Webhook in Clerk Dashboard:**
    *   Go to your Clerk Dashboard -> **Webhooks**.
    *   Click "Add Endpoint".
    *   Enter the **URL** of the API route you created in step 1.
    *   Select the **event types** you want to subscribe to (e.g., `user.created`, `user.updated`, `session.created`, `organization.created`).
    *   **Important:** Copy the **Signing Secret** provided after creating the endpoint.
3.  **Set Signing Secret Environment Variable:**
    *   Add the copied Signing Secret to your backend environment variables, typically named `CLERK_WEBHOOK_SECRET`.
    *   **DO NOT** commit this secret to version control.

    ```dotenv
    # .env.local (Example)
    CLERK_WEBHOOK_SECRET=whsec_YOUR_SIGNING_SECRET_HERE
    ```

## Implementing the Webhook Handler

The handler needs to:

1.  **Verify the Signature:** Use Clerk's webhook verification utilities (`Webhook` class from `svix` package, often re-exported or wrapped by Clerk SDKs) along with the `CLERK_WEBHOOK_SECRET` to ensure the request is authentic. This involves checking headers like `svix-id`, `svix-timestamp`, and `svix-signature`.
2.  **Parse the Payload:** Read the JSON body of the POST request.
3.  **Process the Event:** Implement logic based on the `type` of the event received (e.g., `user.created`, `session.ended`). Update your database, send notifications, etc.
4.  **Return Success Response:** Respond to Clerk with a `2xx` status code (e.g., `200 OK`) to acknowledge receipt. If Clerk receives an error or timeout, it will retry sending the webhook.

**Example: Next.js App Router API Route (`app/api/webhooks/clerk/route.ts`)**

```typescript
import { Webhook } from 'svix'; // Library used by Clerk for webhooks
import { headers } from 'next/headers'; // Next.js utility to read headers
import { WebhookEvent } from '@clerk/nextjs/server'; // Clerk type for event payload
import { NextResponse } from 'next/server';
// Assume db functions exist for user creation/update
// import { createUser, updateUser, deleteUser } from '@/lib/db';

export async function POST(req: Request) {
  // --- Verification ---
  const WEBHOOK_SECRET = process.env.CLERK_WEBHOOK_SECRET;

  if (!WEBHOOK_SECRET) {
    console.error('CLERK_WEBHOOK_SECRET is not set');
    return new NextResponse('Webhook secret not configured', { status: 500 });
  }

  // Get the headers
  const headerPayload = headers();
  const svix_id = headerPayload.get("svix-id");
  const svix_timestamp = headerPayload.get("svix-timestamp");
  const svix_signature = headerPayload.get("svix-signature");

  // If there are no headers, error out
  if (!svix_id || !svix_timestamp || !svix_signature) {
    return new NextResponse('Error occurred -- no svix headers', { status: 400 });
  }

  // Get the body
  let payload: WebhookEvent;
  try {
    payload = await req.json();
  } catch (err) {
    console.error('Error parsing webhook payload:', err);
    return new NextResponse('Invalid request body', { status: 400 });
  }
  const body = JSON.stringify(payload); // svix needs the raw string body

  // Create a new Svix instance with your secret.
  const wh = new Webhook(WEBHOOK_SECRET);

  let evt: WebhookEvent;

  // Verify the payload with the headers
  try {
    evt = wh.verify(body, {
      "svix-id": svix_id,
      "svix-timestamp": svix_timestamp,
      "svix-signature": svix_signature,
    }) as WebhookEvent;
  } catch (err) {
    console.error('Error verifying webhook:', err);
    return new NextResponse('Error occurred during verification', { status: 400 });
  }

  // --- Process Event ---
  const eventType = evt.type;
  console.log(`Webhook received: ${eventType}`);

  try {
    switch (eventType) {
      case 'user.created':
        console.log('User created:', evt.data.id);
        // Example: Create user in your own database
        // await createUser({ clerkId: evt.data.id, email: evt.data.email_addresses[0]?.email_address });
        break;
      case 'user.updated':
        console.log('User updated:', evt.data.id);
        // Example: Update user data in your database
        // await updateUser(evt.data.id, { /* updated fields */ });
        break;
      case 'user.deleted':
        console.log('User deleted:', evt.data.id);
        // Example: Mark user as deleted in your database
        // await deleteUser(evt.data.id);
        break;
      case 'session.created':
        console.log('Session created:', evt.data.id, 'for user:', evt.data.user_id);
        // Example: Log user login activity
        break;
      case 'session.ended':
        console.log('Session ended:', evt.data.id);
        // Example: Log user logout activity
        break;
      // Add cases for other events you subscribed to (organization.*, etc.)
      default:
        console.log(`Unhandled event type: ${eventType}`);
    }

    // Return a 200 response to acknowledge receipt
    return new NextResponse('Webhook processed successfully', { status: 200 });

  } catch (error) {
    console.error(`Error processing webhook ${eventType}:`, error);
    return new NextResponse('Internal Server Error processing webhook', { status: 500 });
  }
}
```

**Important Considerations:**

*   **Idempotency:** Your webhook handler should ideally be idempotent, meaning processing the same event multiple times should not cause unintended side effects (Clerk might retry delivery). Check if you've already processed an event ID if necessary.
*   **Security:** Always verify the webhook signature. Protect your webhook endpoint URL if possible, although signature verification is the primary security mechanism.
*   **Error Handling:** Implement robust error handling and logging within your handler. Return appropriate status codes (2xx for success, 4xx/5xx for errors).
*   **Asynchronous Processing:** For long-running tasks triggered by webhooks, consider acknowledging the webhook immediately (return 200) and then processing the task asynchronously using a queue or background job system to avoid timeouts.

Webhooks are essential for keeping your application's data synchronized with Clerk events and triggering custom server-side workflows based on user activity.

*(Refer to the official Clerk Webhooks documentation.)*