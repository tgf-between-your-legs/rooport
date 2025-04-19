# Directus: Custom Hooks

Extending Directus behavior by running custom code during specific events using the Extension SDK.

## Core Concept

Hooks allow you to inject custom server-side logic (written in TypeScript/JavaScript) into the Directus data flow and event lifecycle. They run in response to specific triggers (actions, filters, schedules, initialization).

## Hook Types & Triggers

1.  **Action Hooks:**
    *   **Trigger:** Run *after* a specific action completes successfully (e.g., an item is created, a user logs in).
    *   **Purpose:** Perform side effects based on the action (e.g., send a notification, call an external API, log an audit event). They **cannot** modify the data related to the triggering event.
    *   **Examples:** `items.create`, `items.update`, `items.delete`, `auth.login`, `users.create`.
2.  **Filter Hooks:**
    *   **Trigger:** Run *during* an action, allowing you to modify the data before or after the core operation.
    *   **Purpose:** Validate data, modify payloads before saving, transform data before sending it to the client, implement custom authorization logic.
    *   **Timing:** Can run `.before`, `.after`, or synchronously (`.` without suffix).
    *   **Return Value:** Filter hooks **must** return the (potentially modified) payload or data.
    *   **Examples:** `items.create.before`, `items.read.after`, `items.update.before`, `users.read`.
3.  **Init Hooks:**
    *   **Trigger:** Run once during Directus server initialization.
    *   **Purpose:** Register custom routes, set up external connections, perform initial setup tasks.
    *   **Examples:** `routes.register`, `app.before`, `server.start`.
4.  **Schedule Hooks:**
    *   **Trigger:** Run based on a CRON schedule defined in the hook's configuration.
    *   **Purpose:** Perform recurring background tasks (e.g., cleanup, reporting, scheduled jobs).
    *   **Example:** `schedule`.

## Hook Implementation (`extensions/hooks/.../index.js`)

*   **Structure:** Export a function that takes the hook trigger name and returns a handler function.
*   **Handler Function:** The handler function receives context-specific arguments depending on the hook type (e.g., `payload`, `meta`, `context`, `services`).
*   **Accessing Services:** Use the `services` object (available in the handler's context argument) to interact with core Directus features (e.g., `ItemsService`, `UsersService`, `MailService`).
*   **Error Handling:** Throw errors within hooks to halt execution and potentially roll back transactions (for relevant hooks).

**Example: Action Hook (After Item Create)**

```typescript
// extensions/hooks/notify-on-create/index.js
// (Assuming TypeScript setup for type safety)
import type { ActionHandler } from '@directus/shared/types'; // Adjust import based on actual SDK structure

// Define the handler function type if using TS
type ItemCreatePayload = { collection: string; key: string | number; payload: Record<string, any> };
type ItemCreateMeta = { accountability: any; schema: any; /* ... other meta */ };

const handler: ActionHandler<ItemCreatePayload, ItemCreateMeta> = (payload, meta, context) => {
  console.log(`Item created in collection: ${payload.collection}`);
  console.log(`Item Key: ${payload.key}`);
  console.log(`Item Payload:`, payload.payload);

  // Example: Send an email using MailService
  const { MailService } = context.services;
  const mailService = new MailService({ schema: context.schema, knex: context.database });

  mailService.send({
      to: 'admin@example.com',
      subject: `New item created in ${payload.collection}`,
      text: `Item ${payload.key} was created: ${JSON.stringify(payload.payload)}`
  }).catch(err => console.error('Failed to send email:', err));

  // Action hooks don't return anything to modify the flow
};

export default function registerHook({ action }) {
  // Register the handler for the 'items.create' action event
	action('items.create', handler);

  // Can register multiple handlers
  // action('items.update', otherHandler);
}
```

**Example: Filter Hook (Before Item Update - Validation)**

```typescript
// extensions/hooks/validate-article-update/index.js
import type { FilterHandler } from '@directus/shared/types';
import { InvalidPayloadError } from '@directus/errors'; // Import Directus error types

type ItemUpdatePayload = Record<string, any>; // Payload being updated
type ItemUpdateMeta = { collection: string; keys: (string | number)[]; accountability: any; schema: any; /* ... */ };

const handler: FilterHandler<ItemUpdatePayload, ItemUpdateMeta> = (payload, meta, context) => {
  // Only apply to 'articles' collection
  if (meta.collection !== 'articles') {
    return payload; // Pass through payload for other collections
  }

  console.log(`Validating update for article keys: ${meta.keys.join(', ')}`);
  console.log('Update Payload:', payload);

  // Example Validation: Ensure title is not empty if being updated
  if (payload.title !== undefined && payload.title.trim() === '') {
    // Throwing a specific Directus error provides better client feedback
    throw new InvalidPayloadError('Article title cannot be empty.');
  }

  // Modify payload if needed
  // payload.last_validated_by = meta.accountability?.user;

  // Filter hooks MUST return the payload
  return payload;
};

export default function registerHook({ filter }) {
  // Register the handler for the 'items.update.before' filter event
	filter('items.update.before', handler);
}
```

## Considerations

*   **Performance:** Hooks execute within the API request cycle. Keep hook logic efficient to avoid slowing down responses. Offload long-running tasks to background jobs if possible (potentially triggered by an action hook).
*   **Error Handling:** Uncaught errors in hooks can break API requests. Use `try...catch` and throw appropriate Directus errors (`InvalidPayloadError`, `ForbiddenError`, etc.) for expected issues.
*   **Security:** Be mindful of security when accessing services or modifying data within hooks. Respect the `accountability` object provided in the context.
*   **Order:** The execution order of multiple hooks registered for the same event is not guaranteed unless explicitly managed.
*   **Testing:** Test hooks thoroughly, including edge cases and error conditions.

*(Refer to the official Directus Hooks documentation: https://docs.directus.io/extensions/hooks.html)*