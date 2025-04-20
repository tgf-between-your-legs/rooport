# Directus: Extension Hooks

Executing custom server-side logic in response to Directus events using Hooks.

## Core Concept: Event-Driven Logic

Directus Hooks allow you to tap into the lifecycle of various actions within the Directus API and Data Studio. They enable you to run custom Node.js/TypeScript code automatically when specific events occur, such as creating an item, updating a user, or uploading a file.

**Use Cases:**

*   **Data Validation:** Implement complex validation rules beyond standard field validation.
*   **Data Augmentation:** Modify or add data before an item is saved or after it's retrieved.
*   **Side Effects:** Trigger external actions like sending emails, calling webhooks, updating search indexes, or interacting with other APIs.
*   **Custom Business Logic:** Enforce specific workflows or calculations based on data changes.
*   **Access Control:** Implement fine-grained, dynamic access control logic (though standard Permissions should be preferred where possible).

## Hook Types & Triggers

Hooks are registered for specific **actions** and **events**.

*   **Actions:** The operation being performed (e.g., `items.create`, `items.update`, `items.delete`, `files.upload`, `auth.login`, `users.create`).
*   **Events:** When the hook should run relative to the action:
    *   **`before`:** Runs *before* the main action executes. Can be used to validate input, modify the payload before it's processed, or block the action by throwing an error.
    *   **`after`:** Runs *after* the main action successfully completes. Receives the result of the action. Used for side effects that depend on the action being successful (e.g., sending a welcome email after user creation).
    *   **`filter`:** Runs *during* an action, allowing modification of the data being processed. Receives a value and must return a potentially modified value. (e.g., modify query parameters in `items.query.filter`, change item data before saving in `items.create.filter`).
    *   **`async`:** Runs *after* the main action completes and the HTTP response has been sent to the client. Suitable for longer-running background tasks or side effects that shouldn't delay the API response (e.g., updating a search index, complex reporting).

## Creating a Hook (TypeScript Example)

1.  **Setup:** Use the Directus extensions SDK or manually create the directory structure: `extensions/hooks/{your-hook-name}/`.
2.  **Create `index.ts`:** This is the entry point for your hook.
3.  **Register Hook:** Export a default function that takes the `registerHook` function (and optionally `env`) as arguments. Call `registerHook` for each event you want to listen to.

```typescript
// extensions/hooks/article-validation/index.ts
import { defineHook } from '@directus/extensions-sdk';
import { InvalidPayloadException } from '@directus/errors'; // Import Directus error classes

// Define the hook using defineHook for type safety
export default defineHook(({ filter, action, schedule }, { services, getSchema }) => { // Added 'schedule'

    // --- Filter Hook Example: Modify data before creation ---
    filter('items.create.filter', (payload, meta, { collection }) => {
        if (collection === 'articles') {
            console.log('Filtering article creation payload:', payload);
            // Example: Ensure title is always uppercase
            if (payload.title && typeof payload.title === 'string') {
                payload.title = payload.title.toUpperCase();
            }
        }
        return payload; // Always return the (potentially modified) payload
    });

    // --- Action Hook Example: Validate before creation ---
    action('items.create.before', async (input, { collection, database, schema }) => {
        if (collection !== 'articles') return; // Only act on 'articles' collection

        console.log(`Hook triggered: ${collection}.create.before`);
        console.log('Input data:', input); // Data being created

        // Example: Complex validation - Title cannot contain "forbidden"
        if (input.title && typeof input.title === 'string' && input.title.toLowerCase().includes('forbidden')) {
            // Throw a Directus error to block the action and inform the user
            throw new InvalidPayloadException('Article title cannot contain the word "forbidden"');
        }

        // Example: Check for uniqueness across multiple fields (requires DB query)
        const { ItemsService } = services;
        const articlesService = new ItemsService('articles', { database, schema });
        const existing = await articlesService.readByQuery({
            filter: {
                // Assuming 'slug' and 'language' fields exist
                slug: { _eq: input.slug },
                language: { _eq: input.language }
            },
            limit: 1
        });
        if (existing.length > 0) {
            throw new InvalidPayloadException('Article with this slug and language already exists.');
        }
    });

    // --- Action Hook Example: Side effect after creation ---
    action('items.create.after', async (output, { collection, key }) => {
        // Note: 'output' contains the result of the action (often the created item ID or object)
        // 'key' contains the primary key of the item involved (if applicable)
        if (collection === 'articles' && output?.status === 'published') {
            console.log(`Hook triggered: ${collection}.create.after`);
            console.log('Created article ID:', key);
            console.log('Created article data:', output);

            // Example: Send a notification or call an external webhook
            // await sendNotification(`New article published: ${output.title} (ID: ${key})`);
            console.log(`Simulating notification for published article: ${key}`);
        }
    });

    // --- Schedule Hook Example: Run a task periodically ---
    schedule('*/5 * * * *', async () => { // Every 5 minutes (cron syntax)
        console.log('Scheduled hook running...');
        // Perform tasks like cleanup, report generation, etc.
    });

});
```

**Hook Function Parameters:**

*   **`filter` hooks:** `(payload, meta, context)` - Return the modified `payload`.
*   **`action` hooks:** `(input, context)` for `before`, `(output, context)` for `after`. `input`/`output` vary by action.
*   **`schedule` hooks:** `()`
*   **`context` object:** Contains useful properties like:
    *   `collection`: The collection name involved.
    *   `schema`: The full Directus schema.
    *   `database`: Knex instance for direct database access (use with caution).
    *   `services`: Access to Directus internal services (ItemsService, UsersService, etc.).
    *   `accountability`: Information about the user/role performing the action.
    *   `key`/`keys`: Primary key(s) of the item(s) involved.
    *   `meta` (for filter/action): Original payload, query parameters, event trigger info.

**Deployment:** Build the hook (`directus-extension build`) and place the output in `extensions/hooks/{hook-name}/`. Restart Directus.

Hooks are essential for adding custom server-side logic and integrations to Directus. Use `before` hooks for validation/blocking, `filter` hooks for data modification during actions, and `after`/`async` hooks for side effects. Leverage the `context` object to access schema, services, and request details.

*(Refer to the official Directus documentation on Hooks.)*