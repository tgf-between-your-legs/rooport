# Directus: Real-time Data with WebSockets

Using Directus subscriptions to receive real-time updates when data changes.

## Core Concept: Pushing Data Updates

While REST and GraphQL APIs are typically request-response based (client asks, server responds), Directus also supports real-time communication using **WebSockets**. This allows the server to *push* updates to connected clients immediately when data changes, without the client needing to constantly poll for updates.

Directus implements this using **GraphQL Subscriptions**.

**Use Cases:**

*   Live dashboards showing updated statistics.
*   Real-time chat applications.
*   Collaborative editing features.
*   Notifications when specific data changes.
*   Live activity feeds.

## How it Works (GraphQL Subscriptions)

1.  **Client Subscribes:** A client connects to the Directus GraphQL endpoint (`/graphql`) via a WebSocket connection and sends a GraphQL `subscription` query. This query specifies:
    *   The collection to watch (e.g., `articles`).
    *   The action(s) to watch (`create`, `update`, `delete`).
    *   Optional filters to only receive updates for specific items.
    *   The data fields to receive when an update occurs.
2.  **Server Listens:** Directus keeps the WebSocket connection open and monitors the specified collection for changes that match the subscription criteria.
3.  **Data Changes:** When an item is created, updated, or deleted (via API or Data Studio) that matches the subscription's collection, action, and filter:
4.  **Server Pushes:** Directus sends a message over the WebSocket connection to the subscribed client containing the data specified in the subscription query.

## Subscribing with the JavaScript SDK

The Directus JS SDK provides helpers for managing WebSocket connections and subscriptions.

```typescript
import { createDirectus, realtime, graphql, readItems, subscribe } from '@directus/sdk';

// Assuming 'client' is an initialized SDK instance (e.g., from directus-sdk-js.md)
// Add the realtime() and graphql() transports
const clientWithRealtime = createDirectus<Schema>('...') // Use wss:// for secure connections
  .with(realtime()) // WebSocket transport
  .with(graphql()); // GraphQL transport (needed for subscriptions)
  // Add authentication if needed (e.g., .with(staticToken(...)))

async function subscribeToArticleUpdates() {
  try {
    // Connect the WebSocket (if not already connected)
    await clientWithRealtime.connect();

    // Define the subscription query (using GraphQL syntax within the SDK)
    const subscriptionQuery = {
      query: `
        subscription ArticleUpdates($limit: Int) {
          articles(limit: $limit) { # Specify collection and optional arguments like limit
            event # Type of event: create, update, delete
            data { # Data payload for the event
              id
              title
              status
            }
            # key # Single primary key (for update/delete)
            # keys # Multiple primary keys (for batch operations)
          }
        }
      `,
      variables: { // Variables for the GraphQL query
        limit: 10 // Example variable
      }
    };

    // Start the subscription
    // The callback function receives messages pushed from the server
    const { subscription, unsubscribe } = await clientWithRealtime.request(
        subscribe(subscriptionQuery, (message) => {
            console.log('Real-time Update Received:', message);
            // Process the message based on message.data.articles.event
            // Update UI, show notification, etc.
            if (message.data?.articles) {
                const eventData = message.data.articles;
                console.log(`Event: ${eventData.event}`);
                console.log(`Data:`, eventData.data);
            }
        })
    );

    console.log('Subscribed to article updates!');

    // To stop listening later:
    // unsubscribe();
    // console.log('Unsubscribed from article updates.');

    // Keep the connection alive or handle disconnection/reconnection logic as needed

  } catch (error) {
    console.error('Subscription error:', error);
  }
}

// Call the function to start subscribing
// subscribeToArticleUpdates();

// Remember to handle disconnection and potential resubscription logic
// clientWithRealtime.onWebSocket('close', () => { console.log('WebSocket closed'); });
// clientWithRealtime.onWebSocket('error', (err) => { console.error('WebSocket error:', err); });

```

## Key Considerations

*   **WebSocket Protocol:** Use `ws://` for local development and `wss://` (secure WebSocket) for production deployments over HTTPS. Ensure your server/proxy is configured to handle WebSocket connections.
*   **Authentication:** If subscribing to non-public data, the WebSocket connection needs to be authenticated. The JS SDK typically handles passing the authentication token (if configured via `staticToken` or `login`) during the WebSocket handshake.
*   **Permissions:** Subscriptions respect Directus role permissions. Users will only receive updates for data they have read access to.
*   **Filtering:** Use the `filter` argument within the subscription query (similar to regular GraphQL queries) to limit updates to specific items (e.g., subscribe to updates only for articles with `status: 'published'`).
*   **Payload:** The `data` field in the subscription message contains the fields requested in your GraphQL subscription query. The `event` field indicates `create`, `update`, or `delete`.
*   **Scalability:** Managing a large number of persistent WebSocket connections can consume server resources. Consider the expected number of concurrent real-time users. Horizontal scaling of Directus instances requires appropriate infrastructure (e.g., sticky sessions or a shared message bus like Redis) for WebSocket connections. Coordinate with `infrastructure-specialist`/`devops-lead`.
*   **Client-Side Handling:** Implement logic in your client application to handle incoming messages, update the UI reactively, and manage the subscription lifecycle (including unsubscribing when components unmount or the feature is no longer needed). Handle potential connection errors and implement reconnection logic if necessary.

Directus GraphQL Subscriptions provide a powerful mechanism for building real-time features. Use the JS SDK's `realtime()` transport and `subscribe()` function to manage the WebSocket connection and receive data updates.

*(Refer to the official Directus documentation on Realtime Data and GraphQL Subscriptions.)*