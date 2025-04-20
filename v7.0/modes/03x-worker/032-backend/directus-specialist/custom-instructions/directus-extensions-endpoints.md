# Directus: Extension Endpoints

Creating custom REST API endpoints within your Directus instance.

## Core Concept: Extending the API

While Directus automatically generates comprehensive REST and GraphQL APIs for your collections, sometimes you need custom API routes for specific business logic, integrations with third-party services, or complex operations that don't map directly to simple CRUD actions on a single collection.

Endpoint extensions allow you to define custom routes (e.g., `/my-custom-route/do-something`) within the Directus API, handled by your own Node.js/TypeScript code.

## Creating an Endpoint Extension

1.  **Setup:** Use the Directus extensions SDK (`npx create-directus-extension`) or manually create the directory structure: `extensions/endpoints/{your-endpoint-name}/`.
2.  **Create `index.ts`:** This is the entry point for your endpoint definition.
3.  **Register Routes:** Export a default function that takes a `router` object (an Express Router instance) and a `context` object (`{ services, database, getSchema, logger }`) as arguments. Use standard Express routing methods (`router.get`, `router.post`, etc.) to define your custom routes and their handlers.

```typescript
// extensions/endpoints/custom-reports/index.ts
import { defineEndpoint } from '@directus/extensions-sdk';
import { ForbiddenException, InvalidPayloadException } from '@directus/errors'; // Import relevant error classes

export default defineEndpoint((router, { services, database, getSchema, logger }) => {
    // The router is an Express router instance.
    // 'services' provides access to Directus services (ItemsService, UsersService, etc.)
    // 'database' is the Knex instance for direct DB access (use cautiously)
    // 'getSchema' returns the current Directus schema information
    // 'logger' is the Directus logger instance

    const { ItemsService } = services;

    // Example: GET /custom-reports/summary
    router.get('/summary', async (req, res, next) => {
        // --- Authentication & Authorization ---
        // Access accountability (user info, role) from the request
        // Directus middleware usually handles authentication before your endpoint runs
        const accountability = req.accountability;

        if (!accountability?.user) {
            // Example: Block unauthenticated access
            return next(new ForbiddenException('Authentication required for this report.'));
        }
        // Example: Check for specific role
        // const adminRole = await getAdminRoleId(); // Function to get admin role UUID
        // if (accountability.role !== adminRole) {
        //     return next(new ForbiddenException('Admin role required.'));
        // }

        logger.info(`Generating summary report for user ${accountability.user}`);

        // --- Access Services ---
        // Always get a fresh schema and pass accountability/knex
        const schema = await getSchema();
        const articlesService = new ItemsService('articles', {
            schema: schema,
            knex: database,
            accountability: accountability, // Pass accountability for permission checks
        });

        try {
            // --- Perform Logic ---
            // Example: Get counts of articles by status
            const publishedCountResult = await articlesService.readByQuery({
                filter: { status: { _eq: 'published' } },
                aggregate: { count: '*' },
            });

            const draftCountResult = await articlesService.readByQuery({
                filter: { status: { _eq: 'draft' } },
                aggregate: { count: '*' },
            });

            // Ensure counts are numbers
            const publishedCount = parseInt(publishedCountResult[0]?.count || '0', 10);
            const draftCount = parseInt(draftCountResult[0]?.count || '0', 10);


            const summary = {
                published: publishedCount,
                drafts: draftCount,
                generatedAt: new Date().toISOString(),
            };

            // --- Send Response ---
            res.json(summary);

        } catch (error) {
            logger.error(error, `Error generating summary report`);
            // Use next(error) to pass the error to Directus's default error handler
            next(error);
        }
    });

    // Example: POST /custom-reports/trigger-action
    router.post('/trigger-action', (req, res, next) => {
        // Access request body
        const payload = req.body;

        // --- Input Validation ---
        if (!payload || typeof payload.actionType !== 'string') {
             return next(new InvalidPayloadException('Missing or invalid actionType in request body'));
        }

        logger.info('Trigger action received with payload:', payload);

        // Perform custom action based on payload
        // e.g., call external API, queue a background job
        console.log(`Performing action: ${payload.actionType}`);

        // Send response
        res.status(202).json({ message: `Action '${payload.actionType}' triggered successfully.` });
    });

    // Add more routes (GET, POST, PUT, PATCH, DELETE) as needed...
    // router.get('/:id', ...)
    // router.patch('/:id', ...)

});
```

## Key Considerations

*   **Authentication/Authorization:** Directus authentication middleware runs *before* your custom endpoint handlers. Access `req.accountability` for user/role info. Implement specific authorization checks within your handler. Use `services` with `accountability` passed in to respect Directus permissions when fetching data.
*   **Error Handling:** Use `try...catch`. Throw Directus error classes (e.g., `InvalidPayloadException`, `ForbiddenException` from `@directus/errors`) or pass errors to `next(error)` for consistent responses.
*   **Accessing Services:** Use the `services` context object (e.g., `ItemsService`). Always pass `schema`, `database` (Knex), and `accountability` when creating service instances.
*   **Direct Database Access:** Use the `database` (Knex instance) cautiously for complex queries not covered by services.
*   **Async Handlers:** Use `async/await` for asynchronous operations.
*   **Input Validation:** Validate `req.body`, `req.query`, `req.params`. Throw `InvalidPayloadException` on failure.
*   **Deployment:** Build (`directus-extension build`) and place output in `extensions/endpoints/{endpoint-name}/`. Restart Directus. Access via `/your-base-path/{endpoint-name}/your-route`.

Custom endpoints add bespoke server-side logic and API routes, integrating with Directus's auth and services.

*(Refer to the official Directus documentation on Endpoints.)*