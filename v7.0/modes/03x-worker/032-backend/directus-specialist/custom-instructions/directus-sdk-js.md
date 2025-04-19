# Directus: JavaScript SDK Usage

Interacting with the Directus API programmatically using the official JavaScript SDK (`@directus/sdk`).

## Core Concept: Programmatic API Interaction

The Directus JavaScript SDK provides a convenient and type-safe way to interact with your Directus instance's REST API from JavaScript/TypeScript applications (frontend or backend Node.js). It handles authentication, request formatting, and response parsing.

**Key Features:**

*   **Type Safety:** Provides TypeScript types for API responses and SDK methods.
*   **Authentication Handling:** Supports various authentication methods (static tokens, JWT login/refresh, session cookies).
*   **CRUD Operations:** Methods for reading, creating, updating, and deleting items (`readItems`, `createItems`, `updateItem`, `deleteItems`, etc.).
*   **Query Parameters:** Supports passing parameters for filtering, sorting, field selection, etc., mirroring the REST API parameters.
*   **Files & Assets:** Methods for uploading and managing files (`uploadFiles`).
*   **Users & Roles:** Methods for managing users and roles (requires appropriate permissions).
*   **Utilities:** Helper functions for various tasks.

## Installation

```bash
npm install @directus/sdk
# or
yarn add @directus/sdk
```

## Initialization

Create an SDK client instance, providing the URL of your Directus instance.

```typescript
import { createDirectus, rest, staticToken, readItems } from '@directus/sdk';

// Define types for your collections (optional but recommended)
interface Article {
  id: string;
  status: 'published' | 'draft' | 'archived';
  title: string;
  author: string | User; // Can be ID or related User object if fetched
  publish_date: string | null;
}
interface User {
    id: string;
    first_name: string;
    last_name: string;
}
type Schema = {
    articles: Article[];
    users: User[];
}

// Create the client instance
const client = createDirectus<Schema>('https://your-directus-instance.com').with(rest());

// --- Authentication ---

// Option 1: Using a Static Token (for server-side or specific integrations)
// const clientWithStaticToken = createDirectus<Schema>('...')
//   .with(rest())
//   .with(staticToken('YOUR_STATIC_TOKEN'));

// Option 2: Login/Password (JWT - typically for frontend)
// async function loginAndGetClient() {
//   const clientForAuth = createDirectus<Schema>('...').with(rest());
//   await clientForAuth.login('user@example.com', 'password123');
//   // The clientForAuth instance now automatically includes the auth token
//   return clientForAuth;
// }

// Option 3: Using existing Access Token (JWT)
// const clientWithToken = createDirectus<Schema>('...')
//   .with(rest())
//   .with(async (request) => {
//      // Interceptor to add the token dynamically
//      const token = getMyAccessToken(); // Function to retrieve your stored token
//      if (!token) throw new Error("User not logged in");
//      request.headers = {
//          ...request.headers,
//          Authorization: `Bearer ${token}`,
//      };
//      return request;
//   });
```

## Common Operations

```typescript
// Assuming 'client' is an initialized and potentially authenticated SDK instance

// --- Read Items ---
async function fetchPublishedArticles() {
  try {
    const articles = await client.request(
      readItems('articles', {
        filter: {
          status: { _eq: 'published' },
        },
        sort: ['-publish_date'],
        limit: 10,
        fields: ['id', 'title', 'publish_date', 'author.first_name', 'author.last_name'], // Select specific fields, including relational
      })
    );
    console.log('Fetched Articles:', articles);
    // articles will be typed as Partial<Article>[] based on 'fields'
    return articles;
  } catch (error) {
    console.error('Error fetching articles:', error);
  }
}

// --- Read Single Item ---
async function fetchArticleById(id: string) {
  try {
    const article = await client.request(
        readItem('articles', id, {
            fields: ['*', 'author.*'] // Get all article fields and all related author fields
        })
    );
    console.log('Fetched Article:', article);
    // article will be typed as Partial<Article>
    return article;
  } catch (error) {
      console.error(`Error fetching article ${id}:`, error);
  }
}

// --- Create Item ---
async function createArticle(title: string, authorId: string) {
  try {
    const newItem = await client.request(
      createItems('articles', [{ // Can create multiple items in one request
        title: title,
        status: 'draft',
        author: authorId, // Provide the related user's ID
      }])
    );
    console.log('Created Item:', newItem);
    // newItem will be typed based on the collection structure
    return newItem;
  } catch (error) {
    console.error('Error creating article:', error);
  }
}

// --- Update Item ---
async function publishArticle(id: string) {
  try {
    const updatedItem = await client.request(
      updateItem('articles', id, {
        status: 'published',
        publish_date: new Date().toISOString(),
      })
    );
    console.log('Updated Item:', updatedItem);
    return updatedItem;
  } catch (error) {
    console.error(`Error updating article ${id}:`, error);
  }
}

// --- Delete Item ---
async function deleteArticle(id: string) {
  try {
    await client.request(deleteItems('articles', [id])); // Pass array of IDs
    console.log(`Deleted article ${id}`);
  } catch (error) {
    console.error(`Error deleting article ${id}:`, error);
  }
}

// --- File Upload ---
// async function uploadImage(fileData: FormData) {
//   try {
//     const result = await client.request(uploadFiles(fileData));
//     console.log('Uploaded File:', result);
//     // Use result.id to link the file in another collection item
//     return result;
//   } catch (error) {
//     console.error('Error uploading file:', error);
//   }
// }
```

The Directus SDK simplifies interacting with the API from JavaScript/TypeScript environments. Initialize the client with your Directus URL, configure authentication, and use the provided request functions (`readItems`, `createItems`, etc.) with query parameters to manage your data. Leverage TypeScript for enhanced type safety.

*(Refer to the official Directus SDK documentation.)*