# Custom Instructions: 08 - Vector Search (`dense_vector` & k-NN)

This instruction covers implementing vector similarity search using the `dense_vector` field type and k-NN search API.

## Core Concept

Vector search finds documents whose vector embeddings are most similar to a query vector, enabling semantic search, recommendations, etc. Elasticsearch supports this via the `dense_vector` field type and the k-Nearest Neighbor (k-NN) search API.

## 1. Mapping Setup (`dense_vector`)

*   Define a field with type `dense_vector`.
*   Specify `dims` matching your embedding model's dimensions. **Required.**
*   Set `index: true` to enable approximate k-NN search (required for performance).
*   Choose the appropriate `similarity` metric:
    *   `cosine`: For normalized vectors where orientation matters (common for text).
    *   `dot_product`: Alternative for normalized vectors (can be faster).
    *   `l2_norm`: Euclidean distance (for non-normalized vectors or where magnitude matters).
    *   `max_inner_product`: For specific recommendation scenarios.
*   Optionally configure `index_options` for the ANN index (e.g., HNSW `type`, `m`, `ef_construction`).

```json
// Example Mapping
// PUT /docs
{
  "mappings": {
    "properties": {
      // ... other fields ...
      "embedding": {
        "type": "dense_vector",
        "dims": 768,          // Match your model's dimensions
        "index": true,         // MUST be true for k-NN search
        "similarity": "cosine" // Or dot_product, l2_norm
        // Optional HNSW index options:
        // "index_options": { "type": "hnsw", "m": 16, "ef_construction": 100 }
      }
    }
  }
}
```

## 2. Indexing Documents

*   Index documents providing the vector embedding as an array of floats in the `dense_vector` field.

```json
// Example Indexing Request
// POST /docs/_doc/1
{
  "title": "Vector Search Intro",
  "embedding": [0.12, -0.34, ..., 0.89] // Array of 768 floats
}
```

## 3. Performing k-NN Search

*   Use the `knn` query clause in the `_search` API.
*   **Required Parameters:**
    *   `field`: Name of the `dense_vector` field.
    *   `query_vector`: The vector embedding to search for.
    *   `k`: Number of nearest neighbors to find *per shard* (<= 10,000). Final results controlled by top-level `size`.
    *   `num_candidates`: Number of candidates to consider on each shard (>= `k`). Higher values increase accuracy but decrease speed.
*   **Optional Parameters:**
    *   `filter`: Apply a filter query *before* the k-NN search runs (restricts search space). Can be placed inside `knn` or in the top-level `query`.

```json
// Example k-NN Search Request
// GET /docs/_search
{
  "knn": {
    "field": "embedding",
    "query_vector": [0.15, -0.30, ..., 0.91], // Query vector
    "k": 10,           // Find 10 nearest neighbors per shard
    "num_candidates": 100 // Consider 100 candidates per shard
    // Optional filter:
    // "filter": [ { "term": { "status": "published" } } ]
  },
  "size": 5, // Return top 5 overall results
  "_source": ["title"]
}
```

**k-NN Search with Filtering (Alternative Placement):**

```json
// GET /docs/_search
{
  "query": { // Filter runs before knn if placed here
    "bool": {
      "filter": [ { "term": { "status": "published" } } ]
    }
  },
  "knn": {
    "field": "embedding",
    "query_vector": [0.15, -0.30, ..., 0.91],
    "k": 10,
    "num_candidates": 100
  },
  "size": 5
}
```

## Considerations

*   **Embedding Model:** Match `dims` and `similarity` to your model.
*   **Indexing:** `index: true` is required for k-NN. Indexing vectors consumes resources.
*   **Performance Tuning:** Adjust `k` and `num_candidates`. Use filtering effectively.
*   **Hybrid Search:** Combine k-NN with traditional search (`match`) using `bool` query or Reciprocal Rank Fusion (`rrf`).

*(Refer to the official Elasticsearch k-NN search documentation.)*