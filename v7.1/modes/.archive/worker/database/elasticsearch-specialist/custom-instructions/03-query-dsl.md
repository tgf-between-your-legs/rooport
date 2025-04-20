# Custom Instructions: 03 - Query DSL

This instruction covers common search queries using Elasticsearch Query DSL.

## Core Concept

Elasticsearch Query DSL (Domain Specific Language) is a flexible, JSON-based language used to define queries. Queries are typically placed within the `query` key of a search request body sent to the `_search` API endpoint.

**Endpoint:** `GET /<index>/_search` or `POST /<index>/_search`

**Basic Structure:**

```json
{
  "query": {
    "<query_type>": {
      "<field_name>": {
        "<parameter>": "<value>",
        ...
      }
      // Or for compound queries like bool:
      // "<clause>": [ ... query objects ... ]
    }
  },
  "from": 0, // Optional: Offset for pagination
  "size": 10, // Optional: Number of hits to return
  "sort": [ ... ], // Optional: Sorting criteria
  "_source": [ ... ] // Optional: Fields to include/exclude
}
```

## Common Query Types

**1. `match` Query (Full-text Search):**
*   Standard query for full-text search. Analyzes the query string and finds documents matching the resulting tokens.
*   **Example:** Find documents where `message` contains "quick brown fox".
    ```json
    { "query": { "match": { "message": { "query": "quick brown fox", "operator": "and" } } } }
    ```

**2. `match_phrase` Query (Phrase Matching):**
*   Matches documents containing the exact phrase after analysis.
*   **Example:** Find documents where `message` contains the exact phrase "quick brown".
    ```json
    { "query": { "match_phrase": { "message": { "query": "quick brown", "slop": 0 } } } }
    ```

**3. `term` Query (Exact Value - Keyword/Non-Analyzed):**
*   Finds documents containing the **exact** term. Use for `keyword`, numeric, date, or boolean fields. **Do not use on `text` fields.**
*   **Example:** Find documents where `status` is exactly "published".
    ```json
    { "query": { "term": { "status": { "value": "published" } } } } // Assumes 'status' is 'keyword'
    ```

**4. `terms` Query (Multiple Exact Values):**
*   Finds documents where the field contains **any** of the exact terms. Use on non-analyzed fields.
*   **Example:** Find documents where `tags` (keyword) is "search" or "nosql".
    ```json
    { "query": { "terms": { "tags": ["search", "nosql"] } } }
    ```

**5. `range` Query (Numeric/Date Ranges):**
*   Finds documents where the field value falls within a specified range (`gte`, `gt`, `lte`, `lt`).
*   **Example:** Find documents where `publish_date` is in 2023 and `likes` >= 100.
    ```json
    { "query": { "bool": { "filter": [
        { "range": { "publish_date": { "gte": "2023-01-01", "lt": "2024-01-01" } } },
        { "range": { "likes": { "gte": 100 } } }
    ] } } }
    ```

**6. `bool` Query (Combining Queries):**
*   Combines multiple query clauses using boolean logic. Most common compound query.
*   **Clauses:**
    *   `must`: All clauses *must* match. Contributes to score. (Like `AND`)
    *   `filter`: All clauses *must* match, but executed in a non-scoring context (faster). **Prefer `filter` for exact matches, ranges.** (Like `AND`, no score impact).
    *   `should`: At least one clause *should* match. Contributes to score. If used with `must`/`filter`, acts as booster. If alone, `minimum_should_match` applies. (Like `OR`)
    *   `must_not`: All clauses *must not* match. Filter context. (Like `NOT`)
*   **Example:** Find active users whose message contains "elasticsearch" OR tags include "kibana", but NOT admin users. Boost if message contains "guide".
    ```json
    { "query": { "bool": {
        "must": [ { "term": { "is_active": true } } ],
        "filter": [ { "bool": {
            "should": [
                { "match": { "message": "elasticsearch" } },
                { "term": { "tags": "kibana" } }
            ],
            "minimum_should_match": 1
        } } ],
        "must_not": [ { "term": { "role": "admin" } } ],
        "should": [ { "match": { "message": "guide" } } ] // Optional booster
    } } }
    ```

**7. `multi_match` Query (Search Across Multiple Fields):**
*   Performs a `match` query against multiple fields.
*   **Example:** Find "quick brown" in `title` or `body` (boost title).
    ```json
    { "query": { "multi_match": { "query": "quick brown", "fields": ["title^2", "body"] } } }
    ```

**8. `nested` Query (Querying Arrays of Objects):**
*   Queries fields within documents mapped with the `nested` type. Ensures conditions apply to the *same* object in the array.
*   **Example:** Find articles with comments by "userA" having >= 5 likes.
    ```json
    { "query": { "nested": {
        "path": "comments",
        "query": { "bool": { "must": [
            { "term": { "comments.username": "userA" } },
            { "range": { "comments.likes": { "gte": 5 } } }
        ] } }
        // "inner_hits": {} // Optional: Return matching nested documents
    } } }
    ```

**9. k-NN Search (Vector Similarity):** (See `08-vector-search.md` for details)
*   Finds documents whose `dense_vector` embeddings are closest to a query vector.
*   **Key Parameters:** `field`, `query_vector`, `k`, `num_candidates`.
*   **Example:** Find 5 docs similar to `query_vector`.
    ```json
    {
      "knn": {
        "field": "embedding",
        "query_vector": [0.15, ...],
        "k": 10,
        "num_candidates": 100
        // "filter": [ ... ] // Optional pre-filtering
      },
      "size": 5
    }
    ```

Combine these using `bool` queries for complex logic. Always refer to the documentation for your specific Elasticsearch version.

*(Refer to the official Elasticsearch Query DSL documentation.)*