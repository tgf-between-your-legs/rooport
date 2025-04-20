# Elasticsearch: Common Query DSL Examples

Illustrative examples of common search queries using Elasticsearch Query DSL.

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

*   Standard query for full-text search. Analyzes the query string using the field's analyzer (or specified `analyzer`) and finds documents matching the resulting tokens.
*   **Example:** Find documents where the `message` field contains "quick brown fox".
    ```json
    {
      "query": {
        "match": {
          "message": {
            "query": "quick brown fox",
            "operator": "and" // Optional: 'or' (default) or 'and'
            // "fuzziness": "AUTO" // Optional: Allow fuzzy matching
          }
        }
      }
    }
    ```

**2. `match_phrase` Query (Phrase Matching):**

*   Matches documents containing the exact phrase (sequence of terms) after analysis.
*   **Example:** Find documents where `message` contains the exact phrase "quick brown".
    ```json
    {
      "query": {
        "match_phrase": {
          "message": {
            "query": "quick brown",
            "slop": 0 // Optional: Allow words between terms (default 0)
          }
        }
      }
    }
    ```

**3. `term` Query (Exact Value - Keyword/Non-Analyzed):**

*   Finds documents containing the **exact** term specified in the inverted index. Use this for `keyword`, numeric, date, or boolean fields (fields that are not analyzed into multiple tokens). **Do not use `term` on `text` fields** unless you know the exact token produced by the analyzer.
*   **Example:** Find documents where `status` is exactly "published".
    ```json
    {
      "query": {
        "term": {
          "status": { // Assuming 'status' is mapped as 'keyword'
            "value": "published"
          }
        }
      }
    }
    ```

**4. `terms` Query (Multiple Exact Values):**

*   Finds documents where the field contains **any** of the exact terms specified. Use on non-analyzed fields (`keyword`, numeric, etc.).
*   **Example:** Find documents where `tags` (keyword field) is either "search" or "nosql".
    ```json
    {
      "query": {
        "terms": {
          "tags": ["search", "nosql"]
        }
      }
    }
    ```

**5. `range` Query (Numeric/Date Ranges):**

*   Finds documents where the field value falls within a specified range.
*   **Operators:** `gte` (>=), `gt` (>), `lte` (<=), `lt` (<).
*   **Example:** Find documents where `publish_date` is in 2023 and `likes` >= 100.
    ```json
    {
      "query": {
        "bool": {
          "filter": [ // Use filter context for non-scoring range queries
            {
              "range": {
                "publish_date": {
                  "gte": "2023-01-01",
                  "lt": "2024-01-01"
                }
              }
            },
            {
              "range": {
                "likes": {
                  "gte": 100
                }
              }
            }
          ]
        }
      }
    }
    ```

**6. `bool` Query (Combining Queries):**

*   Combines multiple query clauses using boolean logic. The most commonly used compound query.
*   **Clauses:**
    *   `must`: All clauses *must* match. Contributes to score. (Like `AND`)
    *   `filter`: All clauses *must* match, but executed in a non-scoring context (faster for filtering). (Like `AND`, but no score impact). **Prefer `filter` for exact matches, ranges, etc.**
    *   `should`: At least one clause *should* match. Contributes to score. If used with `must` or `filter`, it acts as a relevance booster. If used alone, at least one `should` clause must match by default (controlled by `minimum_should_match`). (Like `OR`)
    *   `must_not`: All clauses *must not* match. Executed in filter context. (Like `NOT`)
*   **Example:** Find active users whose message contains "elasticsearch" OR whose tags include "kibana", but NOT admin users. Boost relevance if message also contains "guide".
    ```json
    {
      "query": {
        "bool": {
          "must": [
            { "term": { "is_active": true } }
          ],
          "filter": [ // Non-scoring filters
            {
              "bool": {
                "should": [
                  { "match": { "message": "elasticsearch" } },
                  { "term": { "tags": "kibana" } }
                ],
                "minimum_should_match": 1 // At least one should clause must match
              }
            }
          ],
          "must_not": [
            { "term": { "role": "admin" } }
          ],
          "should": [ // Optional relevance boosting
             { "match": { "message": "guide" } }
          ]
        }
      }
    }
    ```

**7. `multi_match` Query (Search Across Multiple Fields):**

*   Performs a `match` query against multiple fields.
*   **Example:** Find "quick brown" in `title` or `body` fields.
    ```json
    {
      "query": {
        "multi_match": {
          "query": "quick brown",
          "fields": ["title", "body^2"], // Optionally boost score for title field
          "type": "best_fields" // Optional: Query type (best_fields, most_fields, phrase, etc.)
        }
      }
    }
    ```

**8. `nested` Query (Querying Arrays of Objects):**

*   Queries fields within documents mapped with the `nested` type. Ensures query conditions apply to the *same* object within the array.
*   **Example:** Find articles with comments by "userA" that have >= 5 likes (assuming `comments` is a `nested` field).
    ```json
    {
      "query": {
        "nested": {
          "path": "comments", // Path to the nested field
          "query": {
            "bool": {
              "must": [
                { "term": { "comments.username": "userA" } },
                { "range": { "comments.likes": { "gte": 5 } } }
              ]
            }
          }
          // "inner_hits": {} // Optional: Return matching nested documents
        }
      }
    }
    ```

**9. k-NN Search (Vector Similarity):**

*   Finds documents whose vector embeddings are closest to a query vector. Requires a `dense_vector` field with `index: true`. (Syntax may vary slightly across 8.x versions).
*   **Example:** Find 5 documents whose `my_vector` field is most similar to the query vector.
    ```json
    {
      "knn": {
        "field": "my_vector",
        "query_vector": [0.1, 0.5, ...], // Your query embedding
        "k": 10, // Number of neighbors to consider during search
        "num_candidates": 50 // Number of candidates on each shard
        // "filter": { ... } // Optional: Apply filter before k-NN search
      },
      "size": 5 // Number of final results to return
    }
    ```

This covers many fundamental query types. Combine them using `bool` queries for complex search logic. Always refer to the documentation for the specific Elasticsearch version you are using.

*(Refer to the official Elasticsearch Query DSL documentation.)*