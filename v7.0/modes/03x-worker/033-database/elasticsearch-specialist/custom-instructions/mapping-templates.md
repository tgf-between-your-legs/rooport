# Elasticsearch: Common Mapping Templates & Field Types

Examples of defining index mappings and common field types in Elasticsearch.

## Core Concept: Mapping

Mapping is the process of defining how documents and their fields are stored and indexed within an Elasticsearch index. Explicit mapping is crucial for controlling search behavior, storage efficiency, and enabling specific features like aggregations, sorting, and vector search.

**Endpoint:** `PUT /<index>` (often with `mappings` in the request body) or `PUT /<index>/_mapping` (to update mappings on an existing index - limited changes allowed).

**Basic Structure:**

```json
{
  "settings": {
    "index": {
      "number_of_shards": 1, // Example setting
      "number_of_replicas": 1 // Example setting
    },
    "analysis": { // Optional: Define custom analyzers, tokenizers, filters
      "analyzer": { ... },
      "tokenizer": { ... },
      "filter": { ... }
    }
  },
  "mappings": {
    "properties": {
      "<field_name>": {
        "type": "<field_type>",
        // ... other parameters based on type ...
      },
      "<another_field>": { ... }
    }
    // "_meta": { ... } // Optional: Store custom metadata
    // "dynamic": "strict" // Optional: Control handling of unmapped fields ('true', 'false', 'strict')
  }
}
```

## Common Field Types & Parameters

**1. `keyword`:**

*   **Purpose:** Stores exact string values. Used for filtering, sorting, and aggregations on exact terms (e.g., status codes, tags, IDs, categories). Not analyzed (treated as a single token).
*   **Example:**
    ```json
    "status_code": { "type": "keyword" },
    "tags": { "type": "keyword" }, // For an array of exact tags
    "user_id": {
      "type": "keyword",
      "index": true, // Default, enable indexing
      "doc_values": true // Default, enable for sorting/aggregations
    }
    ```

**2. `text`:**

*   **Purpose:** Stores full-text content. Analyzed during indexing (broken into tokens, lowercased, etc.) to enable flexible full-text search. Use `match`, `match_phrase`, `query_string` queries. Not typically used directly for sorting or aggregations (use `keyword` sub-field instead).
*   **Parameters:**
    *   `analyzer`: Specify the analyzer used at index time (default: `standard`).
    *   `search_analyzer`: Specify the analyzer used at query time (defaults to `analyzer`).
    *   `fields`: Define multi-fields, often a `keyword` sub-field for exact matching/sorting/aggregation.
*   **Example:**
    ```json
    "title": {
      "type": "text",
      "analyzer": "english", // Use English language analyzer
      "fields": {
        "keyword": { // Add a keyword sub-field for sorting/aggregation
          "type": "keyword",
          "ignore_above": 256 // Optional: Don't index if string > 256 chars
        }
      }
    },
    "body_content": {
      "type": "text",
      "analyzer": "standard"
    }
    ```

**3. Numeric Types (`integer`, `long`, `float`, `double`, `short`, `byte`, `scaled_float`):**

*   **Purpose:** Stores numeric values. Optimized for range queries, sorting, and aggregations.
*   **Example:**
    ```json
    "view_count": { "type": "integer" },
    "price": { "type": "float" },
    "score": {
      "type": "scaled_float", // For floating points needing scaling factor
      "scaling_factor": 100
    }
    ```

**4. `date`:**

*   **Purpose:** Stores date/time values. Indexed for range queries, sorting, and date-based aggregations. Can parse various formats.
*   **Parameters:**
    *   `format`: Specify expected date formats (e.g., `"yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||epoch_millis"`). Default includes common ISO8601 formats.
*   **Example:**
    ```json
    "created_at": {
      "type": "date",
      "format": "strict_date_optional_time||epoch_millis"
    },
    "event_date": {
      "type": "date",
      "format": "yyyy/MM/dd"
    }
    ```

**5. `boolean`:**

*   **Purpose:** Stores `true` or `false`.
*   **Example:**
    ```json
    "is_published": { "type": "boolean" }
    ```

**6. `object`:**

*   **Purpose:** Stores standard JSON objects. Default type for nested objects if not specified otherwise.
*   **Example:**
    ```json
    "author": {
      "properties": { // Implicitly 'object' type
        "name": { "type": "text" },
        "user_id": { "type": "keyword" }
      }
    }
    ```

**7. `nested`:**

*   **Purpose:** Stores arrays of objects where each object needs to be indexed and queried independently. Prevents cross-object matching issues that can occur with the default `object` type for arrays. Requires using `nested` queries/aggregations.
*   **Example:**
    ```json
    "comments": {
      "type": "nested", // Use nested type for arrays of objects
      "properties": {
        "username": { "type": "keyword" },
        "comment": { "type": "text" },
        "timestamp": { "type": "date" }
      }
    }
    ```

**8. `dense_vector`:**

*   **Purpose:** Stores dense floating-point vectors for vector similarity search (k-NN).
*   **Parameters:**
    *   `dims`: Number of dimensions in the vector. **Required.**
    *   `index`: `true` (default) or `false`. Set to `true` to enable k-NN search.
    *   `similarity`: Distance metric used for indexing (`l2_norm` (default), `dot_product`, `cosine`). Choose based on your embedding model.
    *   `index_options`: (Optional, for HNSW index type) Contains `type: "hnsw"` and parameters like `m` and `ef_construction`.
*   **Example:**
    ```json
    "text_embedding": {
      "type": "dense_vector",
      "dims": 768,
      "index": true,
      "similarity": "cosine" // Or dot_product if vectors are normalized
      // Optional HNSW index options:
      // "index_options": {
      //   "type": "hnsw",
      //   "m": 32,
      //   "ef_construction": 128
      // }
    }
    ```

**9. Other Types:** `ip` (IPv4/v6), `geo_point`, `geo_shape`, `completion` (for suggest), `range` types (`integer_range`, `date_range`, etc.), `alias`.

Choosing the correct field types and configuring them appropriately in your mapping is fundamental to effective use of Elasticsearch.

*(Refer to the official Elasticsearch Mapping documentation and Field data types.)*