## Elasticsearch (Version Unknown) - Condensed Context Index

### Overall Purpose

Elasticsearch is a distributed search and analytics engine built on Apache Lucene. It provides scalable full-text search, structured search, analytics, and data visualization capabilities for various use cases including log analysis, application monitoring, security analytics, and general search applications. This index summarizes key concepts and API patterns based on provided examples.

### Core Concepts & Capabilities

*   **Index Mapping & Field Types:** Define index structure using `mappings`, specifying field types (`text`, `keyword`, `date`, `ip`, `nested`, `dense_vector`, `completion`, `percolator`, `range`, `aggregate_metric_double`, `match_only_text`) and analysis settings. Control how data is stored and indexed.
*   **Querying:** Utilize diverse query types (`match`, `bool`, `terms`, `prefix`, `nested`, `multi_match`, `simple_query_string`, `semantic`, `rank_feature`, `combined_fields`, `dis_max`, `match_phrase_prefix`) via the `_search` endpoint to retrieve relevant documents based on complex criteria.
*   **Aggregations:** Summarize data using `aggregations` (`aggs`) like `terms`, `significant_terms`, `avg`, `min`, `top_hits`, `variable_width_histogram`, often within nested structures, to gain insights from data.
*   **Text Analysis:** Configure text processing using built-in (`simple`) or custom `analyzer` definitions in index `settings`, controlling tokenization and filtering (e.g., `lowercase`, `stop`, `stemmer`, language-specific). Use `search_analyzer` and `search_quote_analyzer` for query-time analysis.
*   **Vector Search:** Map `dense_vector` fields with specified `dims` and `similarity` metrics for indexing and searching vector embeddings, enabling semantic search and k-NN operations.
*   **ESQL (Elasticsearch Query Language):** Employ a pipe-based syntax (`FROM ... | STATS ... | WHERE ...`) for advanced data exploration, transformation (`EVAL`), enrichment (`ENRICH`), and filtering (`CIDR_MATCH`).
*   **Advanced Features:** Leverage `runtime` fields for on-the-fly calculations during queries, `percolator` queries for matching documents against stored queries, and `retriever` rules for modifying search results dynamically.

### Key APIs / Components / Configuration / Patterns

*   `PUT /<index>`: Create or update an index, often defining `mappings` and `settings`.
*   `POST /<index>/_doc/<id>` or `PUT /<index>/_doc/<id>`: Index or update a single document.
*   `POST /<index>/_bulk`: Index, update, or delete multiple documents efficiently.
*   `GET /<index>/_search` or `POST /<index>/_search`: Execute search queries and aggregations. Can target multiple indices (e.g., `GET /index1,index2/_search`).
*   `POST _analyze`: Test analyzers on sample text.
*   `mappings`: Section within index creation/update defining fields and their types/properties.
    *   `properties`: Contains field definitions (e.g., `"message": {"type": "text"}`).
    *   `runtime`: Define fields calculated at query time using `script`.
    *   `type`: Specifies field data type (e.g., `keyword`, `date`, `ip`, `nested`, `dense_vector`, `completion`, `percolator`, `integer_range`, `date_range`, `aggregate_metric_double`, `match_only_text`).
    *   `analyzer`, `search_analyzer`, `search_quote_analyzer`: Specify analyzers for indexing and searching.
    *   `format`: Define custom date formats (e.g., `"yyyy-MM-dd"`).
    *   `dims`, `index`, `similarity`: Parameters for `dense_vector` fields.
*   `settings`: Section for index-level configurations, including `analysis` (custom analyzers, filters, tokenizers).
*   `query`: The main container for search criteria within `_search` requests.
    *   `match`: Standard full-text search on a field.
    *   `bool`: Combines clauses (`must`, `filter`, `should`, `must_not`). `minimum_should_match` controls `should` clause logic.
    *   `terms`: Matches documents containing any of the specified terms in a field.
    *   `prefix`: Matches documents containing terms starting with a specified prefix.
    *   `nested`: Queries fields within nested objects, requires `path`.
    *   `multi_match`: Performs a `match` query across multiple `fields`.
    *   `simple_query_string`: Lucene-like query syntax with operators (`+`, `|`, `-`) across specified `fields`.
    *   `semantic`: Performs semantic search on `semantic_text` fields.
    *   `rank_feature`: Boosts relevance based on numeric feature fields (e.g., `pagerank`).
    *   `combined_fields`: Searches across multiple fields treating them as one combined field.
    *   `dis_max`: Runs multiple queries, scoring based on the best match (`tie_breaker` adjusts scores).
    *   `match_phrase_prefix`: Matches phrases starting with a given prefix.
*   `aggs` (or `aggregations`): Container for aggregation definitions.
    *   `terms`: Bucket aggregation based on field values.
    *   `significant_terms`: Finds terms that are unusually frequent in a subset compared to the background.
    *   `avg`, `min`, `max`, `sum`: Metric aggregations.
    *   `top_hits`: Returns the top matching documents per bucket. Allows `sort` and `_source` filtering.
    *   `nested`: Aggregates on nested documents, requires `path`.
    *   `variable_width_histogram`: Creates buckets of varying widths based on data distribution.
*   `retriever`: Apply rules (`ruleset_ids`) to modify search results based on `match_criteria`.
*   `ESQL`: Uses commands like `FROM`, `WHERE`, `STATS`, `ENRICH`, `EVAL`, `KEEP`, `SORT`. `CIDR_MATCH` for IP filtering.

### Common Patterns & Best Practices / Pitfalls

*   **Mapping is Crucial:** Define explicit mappings for fields to ensure correct indexing and search behavior (e.g., `text` vs. `keyword`, `date` formats, `nested` for arrays of objects).
*   **Analyzer Configuration:** Carefully choose or configure analyzers (`simple`, `standard`, language-specific, custom) based on search requirements (e.g., case sensitivity, stop words, stemming). Use `_analyze` endpoint for testing.
*   **Query Selection:** Select the appropriate query type (`match`, `term`, `bool`, `multi_match`, etc.) based on the desired search logic (full-text, exact match, boolean combinations).
*   **Nested Data:** Use `nested` field type and `nested` queries/aggregations for arrays of objects where object independence is important.
*   **Performance:** Use `match_only_text` for space efficiency when only matching is needed. Be mindful of query complexity. Use `_bulk` API for efficient indexing.

This index summarizes the core concepts, APIs, and patterns for Elasticsearch based on the provided examples. Consult the full source documentation (`project_journal/context/source_docs/elasticsearch-specialist-llms-context-20250406.md`) for exhaustive details.