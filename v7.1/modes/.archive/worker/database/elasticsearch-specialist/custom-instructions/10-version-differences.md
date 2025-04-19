# Custom Instructions: 10 - Key Version Differences (e.g., 7.x vs 8.x)

This instruction highlights significant changes between major Elasticsearch versions relevant to development.

## Core Concept

Elasticsearch evolves, introducing new features, changing APIs, and sometimes removing old functionality. Being aware of the target version is crucial for writing compatible queries, mappings, and using appropriate features. **Always confirm the target ES version.**

## Key Differences (Focus on 7.x vs 8.x)

*(Note: High-level summary. Consult official migration guides for specifics.)*

**1. Mapping & Index Templates:**
*   **Removal of Mapping Types (8.x):** 7.x deprecated types, 8.x removed them. Indices now have a single, implicit type (`_doc`). APIs omit the type (e.g., `PUT /my-index/_doc/1`).
*   **Index Templates:** 8.x favors **Composable Index Templates**. Legacy templates (`_template`) are deprecated. Composable templates use `index_patterns`, `template` (with `settings`, `mappings`, `aliases`), `priority`, `component_templates`.

**2. Query DSL & APIs:**
*   **API Compatibility Headers:** 8.x clients often need strict `Accept` and `Content-Type` headers (e.g., `application/json`).
*   **New Features (8.x):** k-NN search, ESQL, improved relevance tuning.
*   **Deprecated/Removed APIs:** Check deprecation logs and migration guides.

**3. Security:**
*   **Enabled by Default (8.x):** Security (authentication, TLS) is default ON in 8.x, requiring initial setup (passwords, certs). 7.x often had it OFF by default.
*   **API Keys:** Preferred over basic auth for programmatic access in 8.x.

**4. Cluster Coordination:**
*   **Master -> Master-eligible Node:** Terminology change.
*   **Internal Changes:** Significant internal coordination changes in 8.x.

**5. Vector Search (`dense_vector`):**
*   Capabilities significantly developed in later 7.x and especially 8.x. Indexing options (`hnsw`) and query syntax may differ.

**6. ESQL (Elasticsearch Query Language):**
*   Newer, pipe-based query language, more prominent in 8.x.

## Migration Considerations

*   **Reindex:** Often required between major versions (esp. 7.x to 8.x due to type removal). Use `_reindex` API or Logstash.
*   **Upgrade Assistant:** Use Kibana's tool to identify potential issues.
*   **Client Compatibility:** Ensure client library versions match the cluster version.
*   **Test Thoroughly:** Always test in non-production environments first.

Understanding the version is critical for compatibility and feature usage.

*(Refer to the official Elasticsearch Migration Guides for specific versions.)*