# Neon: Using the `pgvector` Extension

Storing and querying vector embeddings in Neon PostgreSQL using the `pgvector` extension.

## Core Concept

`pgvector` is a PostgreSQL extension that adds support for storing vector embeddings and performing efficient vector similarity searches (Approximate Nearest Neighbor - ANN). Neon supports `pgvector`, allowing you to build applications involving semantic search, recommendations, image retrieval, etc., directly within your database.

## Setup

1.  **Enable Extension:** Connect to your Neon database (e.g., using `psql`) and enable the extension. This needs to be done once per database.
    ```sql
    CREATE EXTENSION IF NOT EXISTS vector;
    ```
2.  **Create Table with Vector Column:** Define a table with a column of type `vector`. Specify the number of dimensions for your embeddings.
    ```sql
    CREATE TABLE items (
        id SERIAL PRIMARY KEY,
        name TEXT,
        embedding vector(1536) -- Example: 1536 dimensions for OpenAI embeddings
    );

    -- Or add to existing table
    -- ALTER TABLE items ADD COLUMN embedding vector(1536);
    ```

## Storing Vectors

*   Insert vector data as arrays of floating-point numbers. Ensure the array length matches the dimension specified in the column definition.

```sql
-- Example: Inserting data (vector values are placeholders)
INSERT INTO items (name, embedding) VALUES
('Item A', '[0.1, 0.2, ..., 0.9]'), -- Replace with actual embedding array
('Item B', '[-0.5, 0.8, ..., 0.1]');
```

*   **From Application Code:** Use your PostgreSQL driver to pass the embedding as an array of numbers.
    ```python
    # Example using psycopg (Python)
    import psycopg
    import numpy as np # Example using numpy for embeddings

    conn_str = "postgres://user:pass@host/db?sslmode=require"
    embedding = np.random.rand(1536).tolist() # Your actual embedding vector

    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO items (name, embedding) VALUES (%s, %s)",
                ('Item C', embedding) # Pass embedding as list or numpy array
            )
        conn.commit()
    ```

## Querying Vectors (Similarity Search)

`pgvector` provides distance operators for finding vectors similar to a query vector.

*   **Operators:**
    *   `<->`: Euclidean distance (L2).
    *   `<#>`: Negative Inner Product. For normalized vectors (like many embedding models produce), this is equivalent to sorting by Cosine Similarity in descending order (most similar first). **Often preferred for semantic search.**
    *   `<=>`: Cosine Distance (1 - Cosine Similarity). Lower values mean more similar for normalized vectors.
*   **Basic Similarity Search:** Use the distance operator in the `ORDER BY` clause.
    ```sql
    -- Find items most similar to a query vector using Inner Product (Cosine Similarity)
    -- Replace '[...]' with your actual query vector
    SELECT id, name
    FROM items
    ORDER BY embedding <#> '[0.15, 0.25, ..., 0.85]'
    LIMIT 5;

    -- Find items closest using Euclidean distance
    SELECT id, name
    FROM items
    ORDER BY embedding <-> '[0.15, 0.25, ..., 0.85]'
    LIMIT 5;
    ```

## Indexing for Performance (ANN)

*   Simple `ORDER BY` performs an exact, sequential scan, which is slow on large datasets.
*   `pgvector` supports **Approximate Nearest Neighbor (ANN)** indexes for much faster similarity searches, trading perfect accuracy for speed.
*   **Index Type: `ivfflat`**
    *   Inverted File with Flat compression. Good balance of speed and accuracy, relatively fast build time.
    *   Requires setting the number of `lists` (partitions). A good starting point is `rows / 1000` for up to 1M rows, or `sqrt(rows)` for larger datasets. Tune based on performance.
    ```sql
    -- Create IVFFlat index
    -- Ensure you have enough data before creating (e.g., > 1000 rows)
    CREATE INDEX ON items USING ivfflat (embedding vector_ip_ops) -- Use vector_ip_ops for <#>
    WITH (lists = 100); -- Adjust 'lists' based on your data size

    -- For L2 distance (<->), use vector_l2_ops
    -- CREATE INDEX ON items USING ivfflat (embedding vector_l2_ops) WITH (lists = 100);

    -- For Cosine Distance (<=>), use vector_cosine_ops
    -- CREATE INDEX ON items USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
    ```
*   **Index Type: `hnsw`**
    *   Hierarchical Navigable Small World. Often higher accuracy and faster query speed than `ivfflat`, but slower build time and higher memory usage.
    *   Parameters: `m` (max connections per layer), `ef_construction` (size of dynamic list during build).
    ```sql
    -- Create HNSW index
    CREATE INDEX ON items USING hnsw (embedding vector_ip_ops) -- Use appropriate ops
    WITH (m = 16, ef_construction = 64);
    ```
*   **Querying with ANN Indexes:** The same query syntax (`ORDER BY embedding <#> '...'`) automatically uses the appropriate index if available and deemed efficient by the PostgreSQL query planner.
*   **Tuning ANN Queries:**
    *   `ivfflat`: Control the trade-off between speed and accuracy at query time using `SET ivf.probes = N;` (default 1). Higher values check more lists, increasing accuracy but slowing down the query. Set per session or transaction.
    *   `hnsw`: Control the trade-off using `SET hnsw.ef_search = N;` (default 40). Higher values increase accuracy but slow down the query.

## Considerations

*   **Normalization:** Many embedding models (e.g., OpenAI) produce normalized vectors (length 1). For these, use Inner Product (`<#>`) for Cosine Similarity search and index with `vector_ip_ops`. If vectors are not normalized, use Euclidean (`<->` / `vector_l2_ops`) or Cosine Distance (`<=>` / `vector_cosine_ops`).
*   **Index Building:** Creating ANN indexes can take time and consume resources, especially `hnsw`. Build indexes during low traffic periods.
*   **Tuning:** Finding the optimal index parameters (`lists`, `m`, `ef_construction`) and query parameters (`ivf.probes`, `hnsw.ef_search`) often requires experimentation based on your specific dataset and performance/accuracy requirements. Use `EXPLAIN ANALYZE` to check index usage and performance.

Neon's support for `pgvector` makes it a powerful platform for building AI-powered applications with vector search capabilities directly within PostgreSQL.

*(Refer to the official `pgvector` documentation: https://github.com/pgvector/pgvector and Neon's `pgvector` guide.)*