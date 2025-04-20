# Custom Instructions: Handling Webhooks

Receiving and verifying webhook events from Clerk.

## Core Concept

Webhooks allow Clerk to send real-time notifications to your backend application when specific events occur (e.g., `user.created`, `session.ended`). This enables data synchronization and custom workflows.

**Key Features:**
*   **Event-Driven:** Receive notifications for user, session, organization events.
*   **Backend Integration:** Requires a public API endpoint in your backend.
*   **Security:** Requests must be verified using a signing secret.
*   **Payload:** JSON payload with event type and data.

## Setup

1.  **Create Webhook Endpoint:** Create a publicly accessible API route in your backend (e.g., `/api/webhooks/clerk`).
2.  **Configure in Clerk Dashboard:**
    *   Go to **Webhooks** -> **Add Endpoint**.
    *   Enter the endpoint **URL**.
    *   Select desired **event types**.
    *   Copy the **Signing Secret**.
3.  **Set Environment Variable:** Add the Signing Secret to your backend environment variables (e.g., `CLERK_WEBHOOK_SECRET`). **Do not commit this secret.**

    ```dotenv
    # .env.local (Example)
    CLERK_WEBHOOK_SECRET=whsec_YOUR_SIGNING_SECRET_HERE
    ```

## Implementing the Webhook Handler

The handler must:
1.  **Verify Signature:** Use the `Webhook` class from `svix` (or Clerk SDK wrappers) and the `CLERK_WEBHOOK_SECRET` to verify headers (`svix-id`, `svix-timestamp`, `svix-signature`).
2.  **Parse Payload:** Read the JSON body.
3.  **Process Event:** Implement logic based on the event `type`.
4.  **Return Success Response:** Respond with `2xx` status code promptly.

**Example: Next.js App Router API Route (`app/api/webhooks/clerk/route.ts`)**

```typescript
import { Webhook } from 'svix';
import { headers } from 'next/headers';
import { WebhookEvent } from '@clerk/nextjs/server';
import { NextResponse } from 'next/server';
// import { createUser, updateUser, deleteUser } from '@/lib/db'; // Example DB functions

export async function POST(req: Request) {
  // --- Verification ---
  const WEBHOOK_SECRET = process.env.CLERK_WEBHOOK_SECRET;
  if (!WEBHOOK_SECRET) {
    console.error('CLERK_WEBHOOK_SECRET is not set');
    return new NextResponse('Webhook secret not configured', { status: 500 });
  }

  const headerPayload = headers();
  const svix_id = headerPayload.get("svix-id");
  const svix_timestamp = headerPayload.get("svix-timestamp");
  const svix_signature = headerPayload.get("svix-signature");

  if (!svix_id || !svix_timestamp || !svix_signature) {
    return new NextResponse('Missing svix headers', { status: 400 });
  }

  let payload: WebhookEvent;
  let body: string;
  try {
    payload = await req.json();
    body = JSON.stringify(payload); // svix needs the raw string body
  } catch (err) {
    console.error('Error parsing webhook payload:', err);
    return new NextResponse('Invalid request body', { status: 400 });
  }

  const wh = new Webhook(WEBHOOK_SECRET);
  let evt: WebhookEvent;
  try {
    evt = wh.verify(body, {
      "svix-id": svix_id,
      "svix-timestamp": svix_timestamp,
      "svix-signature": svix_signature,
    }) as WebhookEvent;
  } catch (err) {
    console.error('Error verifying webhook:', err);
    return new NextResponse('Webhook verification failed', { status: 400 });
  }

  // --- Process Event ---
  const eventType = evt.type;
  console.log(`Webhook received: ${eventType}`);

  try {
    switch (eventType) {
      case 'user.created':
        console.log('User created:', evt.data.id);
        // await createUser({ clerkId: evt.data.id, /* ... */ });
        break;
      case 'user.updated':
        console.log('User updated:', evt.data.id);
        // await updateUser(evt.data.id, { /* ... */ });
        break;
      case 'user.deleted':
        console.log('User deleted:', evt.data.id);
        // await deleteUser(evt.data.id);
        break;
      // Add other event types...
      default:
        console.log(`Unhandled event type: ${eventType}`);
    }
    return new NextResponse('Webhook processed', { status: 200 });
  } catch (error) {
    console.error(`Error processing webhook ${eventType}:`, error);
    return new NextResponse('Internal Server Error', { status: 500 });
  }
}
```

**Important Considerations:**
*   **Idempotency:** Design handlers to safely process the same event multiple times.
*   **Security:** Always verify the signature.
*   **Error Handling:** Implement robust error handling and logging.
*   **Asynchronous Processing:** Acknowledge webhook quickly (return 200) and perform long tasks asynchronously (e.g., via queues).

Webhooks are crucial for synchronizing data and triggering server-side workflows based on Clerk events.

*(Refer to the official Clerk Webhooks documentation.)*