# Directus: GraphQL API Usage

Leveraging Directus's automatically generated GraphQL API for flexible data fetching.

## Core Concept: Querying Your Data Graph

Alongside its REST API, Directus provides a powerful GraphQL endpoint (usually `/graphql`) that allows clients to request exactly the data they need in a structured way. The GraphQL schema is dynamically generated based on your collections, fields, and relationships.

**Key Characteristics:**

*   **Single Endpoint:** Typically all GraphQL operations (queries, mutations) are sent to a single endpoint (`/graphql`).
*   **Schema Introspection:** The schema is self-documenting and can be explored using tools like GraphiQL or Apollo Studio.
*   **Client-Specified Queries:** Clients define the shape of the data they want, including nested relational data, reducing over-fetching and under-fetching.
*   **Strongly Typed:** Queries are validated against the schema, ensuring type safety.
*   **Permissions Enforcement:** Like the REST API, all GraphQL requests respect the permissions configured for the user's role.

## Common Operations

**1. Reading Data (Queries):**

*   Use the `query` operation type.
*   Entry points are typically named after your collections (e.g., `articles`, `products`).
*   Use arguments within the query fields for filtering, sorting, pagination, etc. (similar parameters to REST but using GraphQL argument syntax).
*   Select the specific fields you need, including nested fields for relationships.

```graphql
# Example: Fetch published articles with author names, sorted by date

query GetPublishedArticles {
  articles(
    filter: { status: { _eq: "published" } }
    sort: ["-publish_date"]
    limit: 10
  ) {
    # Fields to retrieve for each article
    id
    title
    publish_date
    author { # Fetch related author data
      first_name
      last_name
    }
    tags(limit: 5) { # Fetch related tags (M2M example)
        tags_id { # Access fields within the junction collection if needed
            id
            tag_name
        }
    }
  }
  # Can also query aggregated data
  articles_aggregated(filter: { status: { _eq: "published" } }) {
    count {
      id
    }
  }
}
```

**2. Creating Data (Mutations):**

*   Use the `mutation` operation type.
*   Entry points are typically named `create_{collection_name}_item` (e.g., `create_articles_item`).
*   Pass the data for the new item via an `data` argument (often an input type matching the collection structure).
*   Select the fields you want returned from the created item in the response.

```graphql
# Example: Create a new draft article

mutation CreateDraftArticle {
  create_articles_item(
    data: {
      title: "My New Draft"
      status: "draft"
      author: "user-uuid-goes-here" # Link to related user
      # Omit fields that should use defaults or are auto-generated
    }
  ) {
    # Fields to return after creation
    id
    title
    status
    author {
      id
      first_name
    }
  }
}
```

**3. Updating Data (Mutations):**

*   Use the `mutation` operation type.
*   Entry points are typically named `update_{collection_name}_item` (e.g., `update_articles_item`).
*   Requires the `id` of the item to update and a `data` argument with the fields to change.
*   Select the fields you want returned from the updated item.

```graphql
# Example: Publish an article

mutation PublishArticle {
  update_articles_item(
    id: "article-uuid-goes-here"
    data: {
      status: "published"
      publish_date: "2023-10-27T14:00:00Z"
    }
  ) {
    id
    status
    publish_date
    title
  }
}
```

**4. Deleting Data (Mutations):**

*   Use the `mutation` operation type.
*   Entry points are typically named `delete_{collection_name}_item` (e.g., `delete_articles_item`).
*   Requires the `id` of the item to delete.
*   Select fields to return from the deleted item (often just the `id`).

```graphql
# Example: Delete an article

mutation DeleteArticle {
  delete_articles_item(id: "article-uuid-to-delete") {
    id # Confirm deletion by returning the ID
  }
}
```

## Query Arguments (Filtering, Sorting, etc.)

Arguments within query fields mirror the REST query parameters:

*   `filter: { field: { operator: value } }` (e.g., `filter: { status: { _eq: "published" } }`)
*   `sort: ["field_name", "-other_field"]`
*   `limit: Int`
*   `offset: Int`
*   `page: Int`
*   `search: String`

## Authentication

*   Similar to REST, send the access token (JWT or Static Token) in the `Authorization` header:
    `Authorization: Bearer <your_token>`
*   GraphQL requests are typically `POST` requests to the `/graphql` endpoint, with the query/mutation sent in the JSON request body.

The Directus GraphQL API offers a type-safe and efficient way to interact with your data, especially useful for complex data fetching requirements or when clients need precise control over the response shape. Use GraphiQL or similar tools connected to your Directus `/graphql` endpoint to explore the schema and test queries/mutations.

*(Refer to the official Directus documentation on API Reference - GraphQL.)*