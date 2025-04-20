# Custom Instructions: 02 - Indexing, Mapping & Analysis

This instruction covers defining index structure (mapping), choosing appropriate field types, and configuring text analysis.

## Mapping: Core Concept

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
*   **Example:** `"is_published": { "type": "boolean" }`

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
*   **Purpose:** Stores arrays of objects where each object needs to be indexed and queried independently. Prevents cross-object matching issues. Requires using `nested` queries/aggregations.
*   **Example:**
    ```json
    "comments": {
      "type": "nested",
      "properties": {
        "username": { "type": "keyword" },
        "comment": { "type": "text" },
        "timestamp": { "type": "date" }
      }
    }
    ```

**8. `dense_vector`:** (See `08-vector-search.md` for details)
*   **Purpose:** Stores dense floating-point vectors for vector similarity search (k-NN).
*   **Key Parameters:** `dims`, `index`, `similarity`.

**9. Other Types:** `ip`, `geo_point`, `geo_shape`, `completion`, `range` types, `alias`.

## Text Analysis: Core Concept

Analysis is the process Elasticsearch uses to convert `text` fields into a structured format (the inverted index) for searching. It involves:
1.  **Character Filter(s) (Optional):** Pre-process text (e.g., strip HTML).
2.  **Tokenizer (Required):** Split text into tokens (words).
3.  **Token Filter(s) (Optional):** Process tokens (e.g., lowercase, stem, remove stop words).

## Built-in Analyzers

*   **`standard` (Default):** Grammar-based tokenizer, lowercase, stop words. Good general purpose.
*   **`simple`:** Lowercase tokenizer (splits on non-letters).
*   **`whitespace`:** Splits only on whitespace. No lowercasing.
*   **`stop`:** Like `simple`, plus stop words removal.
*   **`keyword`:** No-op analyzer (treats input as single token).
*   **`pattern`:** Uses regex for tokenization.
*   **`fingerprint`:** Creates a single normalized token.
*   **Language Analyzers:** (`english`, `french`, etc.) Optimized with language-specific stop words and stemming.

## Custom Analyzers

Define in index `settings.analysis` by combining character filters, tokenizers, and token filters.

```json
"settings": {
  "analysis": {
    "analyzer": {
      "my_custom_analyzer": {
        "type": "custom",
        "tokenizer": "standard",
        "char_filter": [ "html_strip" ],
        "filter": [ "lowercase", "my_custom_stop_filter", "my_custom_stemmer" ]
      }
    },
    "filter": {
      "my_custom_stop_filter": { "type": "stop", "stopwords": [...] },
      "my_custom_stemmer": { "type": "stemmer", "language": "english" }
    }
    // Define custom tokenizers or char_filters if needed
  }
}
```

Apply using `"analyzer": "my_custom_analyzer"` in the field mapping.

## Testing Analyzers (`_analyze` API)

Use the `_analyze` API to test how text is tokenized.

```json
// Test standard analyzer
// POST /_analyze
// { "analyzer": "standard", "text": "Test Text!" }

// Test custom analyzer from an index
// POST /my-custom-index/_analyze
// { "analyzer": "my_custom_analyzer", "text": "<p>Test</p>" }

// Test components
// POST /_analyze
// { "tokenizer": "whitespace", "filter": ["lowercase"], "text": "Test Text" }
```

## Analysis Key Considerations

*   **Index vs. Search Analyzers:** Can specify `analyzer` (index time) and `search_analyzer` (query time). Ensure compatibility.
*   **`keyword` vs `text`:** `keyword` is for exact matches/sorting/aggs (not analyzed). `text` is for full-text search (analyzed).
*   **Consistency:** Query-time analysis should be compatible with index-time analysis.
*   **Performance:** Complex analysis adds overhead.

*(Refer to the official Elasticsearch Mapping, Field data types, and Text Analysis documentation.)*