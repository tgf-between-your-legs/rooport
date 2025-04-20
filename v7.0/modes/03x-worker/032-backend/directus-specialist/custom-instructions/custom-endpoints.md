# Directus: Custom API Endpoints

Creating custom API routes and logic within Directus using the Extension SDK.

## Core Concept

While Directus automatically provides powerful REST and GraphQL APIs for CRUD operations on your collections, sometimes you need custom endpoints for:

*   Performing complex business logic not easily mapped to simple CRUD.
*   Integrating with third-party services.
*   Aggregating data from multiple collections in a specific way.
*   Providing simplified endpoints for specific client needs.

Custom endpoints allow you to define your own routes (e.g., `/my-custom-route/process-data`) and implement server-side logic using JavaScript/TypeScript.

## Implementation (`extensions/endpoints/.../index.js`)

1.  **Directory Structure:** Create a folder for your endpoint extension within `directus/extensions/endpoints/`.
    ```
    your-directus-project/
    └── extensions/
        └── endpoints/
            └── my-custom-logic/
                ├── index.js       # Entry point
                └── package.json
    ```
2.  **`package.json`:** Define the extension type and entry point.
    ```json
    // extensions/endpoints/my-custom-logic/package.json
    {
      "name": "directus-extension-my-custom-logic",
      "version": "1.0.0",
      "type": "module",
      "directus:extension": {
        "type": "endpoint",
        "entrypoint": "index.js",
        "host": "^10.8.0" // Compatible Directus version
      },
      "dependencies": {
        // Add dependencies if needed
      }
    }
    ```
3.  **`index.js` (or `.ts`):** Export a function (often default) that takes the router instance (similar to Express) and Directus services context. Define your routes and handlers within this function.

```typescript
// extensions/endpoints/my-custom-logic/index.js
// (Assuming TypeScript setup for type safety)
import { ForbiddenError } from '@directus/errors';

export default function registerEndpoint(router, context) {
  // 'router' is an Express-like router instance
  // 'context' provides access to services, database, schema, logger, etc.
  const { services, database, getSchema, logger } = context;
  const { ItemsService } = services;

  // Example: GET endpoint
  router.get('/report', async (req, res, next) => {
    // Access services using the current schema and accountability (permissions)
    const schema = await getSchema();
    const articlesService = new ItemsService('articles', { schema: schema, accountability: req.accountability });

    try {
      // Check permissions (optional, depends on endpoint needs)
      // if (!req.accountability?.user) {
      //   throw new ForbiddenError('Authentication required');
      // }
      // if (req.accountability?.role !== 'admin-uuid') { // Check specific role
      //    throw new ForbiddenError('Admin role required');
      // }

      // Perform custom logic (e.g., aggregate data)
      const publishedCount = await articlesService.readByQuery({
        filter: { status: { _eq: 'published' } },
        aggregate: { count: '*' }
      }).then(results => results[0]?.count ?? 0);

      const draftCount = await articlesService.readByQuery({
        filter: { status: { _eq: 'draft' } },
        aggregate: { count: '*' }
      }).then(results => results[0]?.count ?? 0);

      // Send response
      res.json({
        published: publishedCount,
        drafts: draftCount,
        generated_at: new Date().toISOString()
      });

    } catch (error) {
      logger.error(error, `Failed to generate report`);
      // Use 'next(error)' to pass errors to Directus's default error handler
      // This ensures consistent error formatting (e.g., JSON response)
      return next(error);
      // Or send a custom response: res.status(500).send('Error generating report');
    }
  });

  // Example: POST endpoint
  router.post('/process/:id', async (req, res, next) => {
    const schema = await getSchema();
    const itemsService = new ItemsService('some_collection', { schema: schema, accountability: req.accountability });
    const itemId = req.params.id;
    const requestData = req.body; // Assumes body-parser middleware is used (usually is by Directus)

    try {
      logger.info(`Processing item ${itemId} with data:`, requestData);

      // TODO: Perform complex processing based on itemId and requestData
      // Example: Call external API, update multiple items, etc.
      // await externalService.process(itemId, requestData);
      await itemsService.updateOne(itemId, { status: 'processed', processed_at: new Date() });

      res.status(200).json({ message: `Item ${itemId} processed successfully.` });

    } catch (error) {
      logger.error(error, `Failed processing item ${itemId}`);
      return next(error);
    }
  });

  // Register other routes (PUT, DELETE, etc.) as needed
  // router.put(...)
  // router.delete(...)
}
```

## Key Concepts

*   **Router:** The `router` object passed to your extension function is typically an instance of the Express router. You use methods like `router.get()`, `router.post()`, `router.put()`, `router.delete()`, etc., to define routes.
*   **Handlers:** Your route handler functions receive `req` (request), `res` (response), and `next` (middleware control) objects, similar to Express middleware.
*   **Context:** The `context` object provides access to:
    *   `services`: Core Directus services (`ItemsService`, `UsersService`, `FilesService`, `MailService`, etc.). Instantiate them with the current `schema` and `req.accountability`.
    *   `database`: Knex.js instance for direct database access (use services where possible).
    *   `getSchema()`: Async function to get the current collection schema.
    *   `logger`: Directus logger instance.
    *   `env`: Access to environment variables.
*   **`req.accountability`:** Contains information about the authenticated user and their role, crucial for permission checks. If the request is unauthenticated, `req.accountability.user` will be `null`.
*   **Error Handling:** Use `try...catch` blocks. Pass errors to `next(error)` to let the Directus default error handler format the response consistently (recommended). Import specific error classes from `@directus/errors` (e.g., `InvalidPayloadError`, `ForbiddenError`) for standard HTTP status codes.
*   **Middleware:** You can register Express-compatible middleware using `router.use()`. Directus already includes common middleware like `body-parser`.

Custom endpoints provide immense flexibility to tailor Directus to complex backend requirements.

*(Refer to the official Directus Endpoints documentation: https://docs.directus.io/extensions/endpoints.html)*