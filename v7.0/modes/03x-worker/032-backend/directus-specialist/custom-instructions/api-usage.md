# Directus: API Usage (REST & GraphQL)

Querying and manipulating data using the automatically generated Directus APIs.

## Core Concept

Directus automatically generates powerful REST and GraphQL APIs based on the collections (data models) you define. These APIs allow frontend applications and other services to interact with your content.

## REST API

*   **Endpoint Structure:** Typically follows `/items/{collection_name}`.
    *   `GET /items/{collection_name}`: List items (with filtering, sorting, pagination).
    *   `POST /items/{collection_name}`: Create a new item.
    *   `GET /items/{collection_name}/{item_id}`: Retrieve a single item by ID.
    *   `PATCH /items/{collection_name}/{item_id}`: Update an item partially.
    *   `DELETE /items/{collection_name}/{item_id}`: Delete an item.
*   **Authentication:** Requires an access token (Static Token, Session Token, JWT) passed typically as a `Bearer` token in the `Authorization` header. Public roles might allow unauthenticated access for specific collections/operations.
*   **Query Parameters (for GET requests):**
    *   **Filtering (`filter`):** Use a JSON-based filter object (e.g., `?filter={"status":{"_eq":"published"}}`). Supports various operators (`_eq`, `_neq`, `_gt`, `_in`, `_contains`, logical `_and`/`_or`, relational filters).
    *   **Sorting (`sort`):** Comma-separated list of fields (e.g., `?sort=title` for ascending, `?sort=-published_on` for descending).
    *   **Field Selection (`fields`):** Comma-separated list of fields to return (e.g., `?fields=id,title,author.name`). Supports nested fields using dot notation and wildcards (`*`, `author.*`).
    *   **Pagination (`limit`, `page`, `offset`):** Control the number of items returned (e.g., `?limit=10&page=2`). `limit=-1` retrieves all items (use with caution).
    *   **Deep (Relational Data):** Use nested `fields` or the `deep` parameter with filters/sorts to work with related data (e.g., `?fields=*,author.*&deep={"author":{"_filter":{"name":{"_eq":"Alice"}}}}`).
    *   **Aggregation (`aggregate`):** Perform aggregate functions (count, sum, avg, min, max) (e.g., `?aggregate[count]=*&aggregate[avg]=rating`).
    *   **Grouping (`groupBy`):** Group results by specific fields (e.g., `?groupBy=status`).
*   **Response Format:** Typically returns JSON with a `data` property containing the result (single object or array of objects). Metadata (like total count for pagination) might be included under a `meta` property if requested (`?meta=total_count`).

**Example (REST GET):**
```
GET /items/articles?fields=id,title,author.name&filter={"status":{"_eq":"published"}}&sort=-published_on&limit=10
Authorization: Bearer <YOUR_ACCESS_TOKEN>
```

## GraphQL API

*   **Endpoint:** A single endpoint, usually `/graphql`.
*   **Schema:** Automatically generated based on your collections and fields. Introspectable via standard GraphQL tools.
*   **Queries:** Use standard GraphQL query syntax to fetch data. Supports filtering (`filter`), sorting (`sort`), pagination (`limit`, `page`, `offset`), and aggregation (`_aggregated`) via arguments on fields.
*   **Mutations:** Use standard GraphQL mutations for creating (`create_{collection_name}_item`), updating (`update_{collection_name}_item`), and deleting (`delete_{collection_name}_item`) items. Input types are generated based on collection fields.
*   **Authentication:** Same as REST - pass the token in the `Authorization` header.

**Example (GraphQL Query):**
```graphql
query GetPublishedArticles {
  articles(
    filter: { status: { _eq: "published" } }
    sort: ["-published_on"]
    limit: 10
  ) {
    id
    title
    published_on
    author {
      name
    }
  }
  # Example Aggregation
  articles_aggregated(filter: { status: { _eq: "published" } }) {
    count {
      id
    }
  }
}
```

**Example (GraphQL Mutation):**
```graphql
mutation CreateArticle($newData: create_articles_input!) {
  create_articles_item(data: $newData) {
    id
    title
    status
  }
}
# Variables:
# {
#   "newData": {
#     "title": "My New Article",
#     "content": "...",
#     "status": "draft"
#   }
# }
```

## Directus SDK (JavaScript/TypeScript)

*   **Purpose:** Provides a convenient way to interact with the Directus API from JavaScript/TypeScript applications (frontend or Node.js). Handles authentication, type safety (if using TypeScript SDK), and simplifies requests.
*   **Installation:** `npm install @directus/sdk`
*   **Usage:**
    ```typescript
    import { createDirectus, rest, readItems, createItem } from '@directus/sdk';

    // Define types for your collections (optional but recommended)
    type Article = {
      id: string;
      status: 'published' | 'draft';
      title: string;
      // ... other fields
    };
    type Schema = {
      articles: Article[];
    };

    const client = createDirectus<Schema>('http://your-directus-instance.com').with(rest());
    // Or .with(graphql())

    async function fetchArticles() {
      try {
        const articles = await client.request(readItems('articles', {
          fields: ['id', 'title', 'author.name'], // Nested fields work
          filter: { status: { _eq: 'published' } },
          sort: ['-published_on'],
          limit: 10,
        }));
        console.log(articles); // Type is Article[]
      } catch (error) {
        console.error('Error fetching articles:', error);
      }
    }

    async function addArticle() {
        try {
            const newItem = await client.request(createItem('articles', {
                title: 'Article via SDK',
                status: 'draft',
                content: '...'
            }));
            console.log('Created:', newItem);
        } catch(error) {
            console.error('Error creating article:', error);
        }
    }
    ```

Choose the API style (REST, GraphQL, SDK) that best fits the needs of the consuming application.

*(Refer to the official Directus API Reference: https://docs.directus.io/reference/introduction.html and SDK documentation: https://docs.directus.io/sdk/introduction.html)*