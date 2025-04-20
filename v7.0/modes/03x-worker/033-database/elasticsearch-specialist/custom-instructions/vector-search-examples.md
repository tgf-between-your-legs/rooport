# Elasticsearch: Vector Search Examples (`dense_vector` & k-NN)

Implementing vector similarity search using the `dense_vector` field type and k-NN search API.

## Core Concept

Vector search allows finding documents whose vector embeddings are most similar to a given query vector, enabling semantic search, recommendation engines, image similarity, and other AI-powered features. Elasticsearch supports this via the `dense_vector` field type and the k-Nearest Neighbor (k-NN) search API.

## 1. Mapping Setup

*   Define a field with type `dense_vector`.
*   Specify the number of `dims` (dimensions) matching your embedding model.
*   Set `index: true` to enable approximate k-NN search (required for performance on large datasets).
*   Choose the appropriate `similarity` metric based on your embeddings:
    *   `cosine`: For vectors where orientation matters most (common for text embeddings). Use if vectors are normalized.
    *   `dot_product`: Can also be used for normalized vectors (mathematically related to cosine similarity). Sometimes slightly faster.
    *   `l2_norm`: Euclidean distance. Use if vector magnitude matters or vectors aren't normalized.
    *   `max_inner_product`: Maximum inner product, useful for specific recommendation scenarios.
*   Optionally configure `index_options` for the underlying ANN index (typically HNSW).

```json
// Example Mapping for an index named 'docs'
// PUT /docs
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text"
      },
      "content": {
        "type": "text"
      },
      "embedding": {
        "type": "dense_vector",
        "dims": 768,          // Dimension of your embedding model (e.g., 768 for some sentence-transformers)
        "index": true,         // MUST be true for k-NN search
        "similarity": "cosine" // Or "dot_product" for normalized vectors, or "l2_norm"
        // Optional HNSW index configuration (defaults are often reasonable)
        // "index_options": {
        //   "type": "hnsw",
        //   "m": 16,
        //   "ef_construction": 100
        // }
      }
    }
  }
}
```

## 2. Indexing Documents

*   Index documents as usual, providing the vector embedding as an array of floating-point numbers in the `dense_vector` field.

```json
// Example Indexing Request
// POST /docs/_doc/1
{
  "title": "Introduction to Elasticsearch",
  "content": "Elasticsearch is a distributed search engine...",
  "embedding": [0.12, -0.34, ..., 0.89] // Array of 768 floats
}

// POST /docs/_doc/2
{
  "title": "Vector Search Basics",
  "content": "k-NN search finds nearest neighbors in vector space...",
  "embedding": [-0.56, 0.11, ..., 0.45] // Another array of 768 floats
}
```

## 3. Performing k-NN Search

*   Use the `knn` query clause in the `_search` API.
*   **Required Parameters:**
    *   `field`: The name of your `dense_vector` field.
    *   `query_vector`: The vector embedding you want to find similar documents for.
    *   `k`: The number of nearest neighbors to find *per shard*. The final result size is controlled by the top-level `size` parameter. `k` must be <= 10,000.
    *   `num_candidates`: The number of candidates to consider on each shard during the search. Higher values increase accuracy but decrease speed. Must be >= `k`.
*   **Optional Parameters:**
    *   `filter`: Apply a filter query *before* the k-NN search runs. This restricts the search space to only documents matching the filter, improving performance and relevance.

```json
// Example k-NN Search Request
// GET /docs/_search
{
  "knn": {
    "field": "embedding",
    "query_vector": [0.15, -0.30, ..., 0.91], // Vector for "search engine concepts"
    "k": 10,           // Find 10 nearest neighbors per shard
    "num_candidates": 100 // Consider 100 candidates per shard
  },
  "size": 5, // Return the top 5 overall results
  "_source": ["title"] // Only return the title field
}
```

**k-NN Search with Filtering:**

*   Apply a standard filter query alongside the `knn` query. The filter runs first.

```json
// Example k-NN Search with Filter
// GET /docs/_search
{
  "query": { // Optional: Combine knn with other queries using bool (filter runs first)
    "bool": {
      "filter": [
        { "term": { "status": "published" } } // Only search published documents
      ]
    }
  },
  "knn": {
    "field": "embedding",
    "query_vector": [0.15, -0.30, ..., 0.91],
    "k": 10,
    "num_candidates": 100,
    "filter": [ // Alternative filter placement directly within knn (more efficient in some cases)
       { "term": { "status": "published" } }
    ]
  },
  "size": 5,
  "_source": ["title", "status"]
}
```

## Considerations

*   **Embedding Model:** Ensure the `dims` in your mapping match the output dimension of your chosen embedding model. Use the `similarity` metric appropriate for that model (often `cosine` or `dot_product` for normalized vectors).
*   **Indexing:** `dense_vector` fields must have `index: true` for k-NN search. Indexing vectors (especially with HNSW) consumes resources and time.
*   **Performance Tuning:** Adjust `k` and `num_candidates` to balance speed and accuracy. Higher `num_candidates` generally yields better accuracy but is slower. Use filtering effectively to reduce the search space.
*   **Hybrid Search:** Combine k-NN search with traditional full-text search (e.g., `match`) using a `bool` query or Reciprocal Rank Fusion (`rrf`) for hybrid semantic and keyword search.

Vector search in Elasticsearch provides powerful capabilities for similarity-based retrieval.

*(Refer to the official Elasticsearch k-NN search documentation.)*