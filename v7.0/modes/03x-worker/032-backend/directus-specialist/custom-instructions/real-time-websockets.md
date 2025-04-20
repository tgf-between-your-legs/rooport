# Directus: Real-Time Features (WebSockets)

Using Directus subscriptions to receive real-time data updates via WebSockets.

## Core Concept

Directus provides a built-in WebSocket server that allows clients (frontend applications, other services) to subscribe to changes in collection data (creations, updates, deletes). When an event occurs that matches a subscription, Directus pushes the relevant data to the subscribed clients over the WebSocket connection.

## Enabling WebSockets

*   **Environment Variable:** Ensure the WebSocket server is enabled via the `.env` file:
    ```dotenv
    WEBSOCKETS_ENABLED=true
    # Optional: Configure message broker if scaling beyond a single instance
    # WEBSOCKETS_BROKER_URL=redis://localhost:6379
    # MESSENGER_STORE=redis
    # CACHE_STORE=redis
    # CACHE_ENABLED=true
    ```
*   **Restart:** Restart your Directus instance after changing `.env` variables.

## Client-Side Usage (Directus SDK)

The Directus JavaScript/TypeScript SDK provides the easiest way to manage WebSocket connections and subscriptions.

```typescript
import { createDirectus, realtime, subscribe, login } from '@directus/sdk';

// Define types for your collections
type Article = { id: string; status: string; title: string; /* ... */ };
type Schema = { articles: Article[] };

const client = createDirectus<Schema>('http://your-directus-instance.com').with(realtime());
// Use wss:// for secure connections if your Directus instance uses HTTPS

async function connectAndSubscribe() {
  try {
    // 1. Login (required for non-public data)
    // Subscriptions respect user permissions
    await client.request(login('user@example.com', 'password'));
    // Or use a static token: client.setToken('your-static-token');

    console.log('WebSocket connected and authenticated.');

    // 2. Subscribe to events
    // Subscribe to all creates, updates, deletes in the 'articles' collection
    const { subscription, unsubscribe } = await client.subscribe('articles', {
      // Optional: Specify query parameters (fields, filter) for the data you receive
      query: {
        fields: ['id', 'title', 'status'],
        filter: { status: { _eq: 'published' } } // Only get updates for published articles
      },
      // Optional: Specify specific actions ('create', 'update', 'delete')
      // event: 'create', // Only subscribe to creates
    });

    // 3. Handle incoming messages
    for await (const message of subscription) {
      console.log('Received WebSocket Message:', message);
      // message object structure:
      // {
      //   type: 'subscription',
      //   event: 'create' | 'update' | 'delete',
      //   collection: 'articles',
      //   data: [...] // Array of items affected (updates contain full item based on query)
      //   key?: string | number // Single key for single item update/delete
      //   keys?: (string | number)[] // Multiple keys for batch operations
      // }

      if (message.event === 'create') {
        console.log('New article(s) created:', message.data);
        // Update UI accordingly
      } else if (message.event === 'update') {
        console.log('Article(s) updated:', message.data);
        // Update UI accordingly
      } else if (message.event === 'delete') {
        console.log('Article key(s) deleted:', message.keys || [message.key]);
        // Update UI accordingly
      }
    }

    // 4. Unsubscribe when no longer needed (e.g., component unmount)
    // unsubscribe();
    // console.log('Unsubscribed from articles.');

  } catch (error) {
    console.error('WebSocket Error:', error);
    // Handle connection errors, authentication errors, etc.
  }
}

connectAndSubscribe();

```

## Subscription Options

When calling `client.subscribe(collection, options)`, you can specify:

*   **`query`**: An object containing standard Directus query parameters (`fields`, `filter`, `limit`, `sort`, `deep`, etc.) to shape the data payload sent with update/create messages.
*   **`event`**: A specific event type (`'create'`, `'update'`, `'delete'`) to subscribe to, instead of all three.
*   **`uid`**: A custom unique identifier for the subscription (useful for managing multiple subscriptions).

## Use Cases

*   Real-time dashboards
*   Live updates in collaborative applications
*   Chat applications
*   Notifications
*   Activity feeds

## Considerations

*   **Permissions:** Subscriptions respect the permissions of the authenticated user. Users will only receive updates for data they have read access to, matching the specified filter.
*   **Scalability:** For applications with many concurrent WebSocket connections, you'll need to configure a message broker (like Redis) via environment variables (`WEBSOCKETS_BROKER_URL`, `MESSENGER_STORE`, `CACHE_STORE`) to allow multiple Directus instances to communicate WebSocket events.
*   **Connection Management:** The SDK handles basic reconnection logic, but robust applications might need additional client-side logic to manage connection state and potential errors.
*   **Data Volume:** Be mindful of the amount of data being pushed. Use specific `fields` and `filter` options in your subscription query to limit the payload size.

*(Refer to the official Directus Realtime documentation: https://docs.directus.io/guides/realtime.html and SDK Realtime docs: https://docs.directus.io/sdk/realtime.html)*