# Custom Instructions: 06 - Performance Tuning & Relevance

This instruction covers key aspects of optimizing Elasticsearch performance and search relevance.

## Core Principles

*   **Efficiency First:** Design efficient mappings and write performant queries/aggregations from the start.
*   **Understand Implications:** Be aware of the performance impact of mapping choices (e.g., field types, indexing options), query structure (e.g., filter context vs. query context, query complexity), cluster topology (sharding, replication), and indexing strategies (e.g., refresh interval, bulk sizing).
*   **Measure and Monitor:** Use monitoring tools (Elasticsearch APIs, Kibana Stack Monitoring, external tools) to identify bottlenecks in indexing and querying. Use the `_nodes/hot_threads` API to diagnose CPU-intensive operations.

## Key Areas for Tuning

**1. Mapping & Indexing:**
*   **Choose Appropriate Field Types:** Use `keyword` for exact matches/sorting/aggs, `text` for full-text search. Use appropriate numeric types. Avoid using `text` fields for sorting/aggs directly; use a `keyword` multi-field instead.
*   **Disable Unneeded Features:** If sorting or aggregations are not needed on a field, consider setting `doc_values: false`. If scoring is not needed (`filter` context only), consider `index: false` for specific fields (use with caution).
*   **Analyzers:** Simple analyzers are faster than complex ones. Test analyzer performance if needed.
*   **Refresh Interval:** The `index.refresh_interval` setting controls how often changes become visible to search. Increasing it (e.g., from `1s` to `30s`) reduces indexing overhead but increases search latency for new data. Set to `-1` to disable automatic refreshes and refresh manually via API after bulk indexing.
*   **Bulk Indexing:** Use the `_bulk` API for indexing large amounts of data. Tune the bulk request size and concurrency for optimal throughput.
*   **Segment Merging:** Elasticsearch automatically merges segments. While `_forcemerge` can reduce segment count (improving search speed), it's resource-intensive. Use it judiciously, typically during off-peak hours on read-heavy indices. Monitor segment count via `_cat/indices` or `_index/stats`.

**2. Query Performance:**
*   **Filter Context:** Use the `filter` clause within a `bool` query for non-scoring criteria (exact matches, range queries, existence checks). Filters are cacheable and generally faster than scored queries.
*   **Avoid Leading Wildcards:** Queries like `*term` or `?term` are slow as they require scanning many terms. Prefer prefix queries (`term*`) or structure data differently if possible.
*   **Query Complexity:** Deeply nested `bool` queries or complex script queries can be slow. Simplify where possible.
*   **Date Math:** Use date math (`now-1d/d`) in range queries instead of calculating dates client-side, allowing better caching.
*   **Shard Request Cache:** Elasticsearch caches results for `filter` clauses and queries where `size: 0`. Ensure queries are cacheable where appropriate. Monitor cache usage via `_nodes/stats`.
*   **Profile API:** Use the `_search` Profile API (`"profile": true` in the request) to get detailed timing information for query execution phases and identify bottlenecks within a query.

**3. Relevance Tuning:**
*   **Understand Scoring:** Familiarize yourself with TF/IDF and BM25 scoring algorithms (defaults).
*   **Query Types:** Use appropriate query types (`match`, `match_phrase`, `multi_match` with `best_fields` vs `most_fields`) for desired relevance.
*   **Boosting:** Use boost parameters within queries (e.g., `fields: ["title^3", "body"]` in `multi_match`) or `boosting` queries to influence scores.
*   **Function Score Query:** Use `function_score` for fine-grained control over scoring, incorporating factors like recency, popularity, or geo-location.
*   **Explain API:** Use the `_explain` API to understand how the score for a specific document was calculated for a given query.

**4. Cluster & Sharding:**
*   **Sharding Strategy:** Choose an appropriate number of primary shards when creating an index. Too few can limit scalability; too many can increase overhead. Consider data volume, growth rate, and query patterns. (Note: Changing primary shard count requires reindexing).
*   **Replicas:** Replicas improve search throughput and provide high availability. Adjust `number_of_replicas` based on query load and HA requirements.
*   **Hardware:** Ensure nodes have sufficient RAM (especially for heap), CPU, and fast disk I/O (SSDs recommended).
*   **JVM Heap:** Allocate appropriate JVM heap size (typically up to 50% of RAM, capped around 30-31GB). Monitor heap usage and garbage collection via `_nodes/stats` or monitoring tools.

Performance tuning is an iterative process involving analysis, changes, and measurement.

*(Refer to the official Elasticsearch documentation on Performance Tuning, Query Profiling, and Relevance Scoring.)*