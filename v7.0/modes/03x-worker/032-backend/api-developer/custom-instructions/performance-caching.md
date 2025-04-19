# API Performance & Caching Strategies

Basic considerations for optimizing API performance and implementing caching.

## Performance Optimization (General)

*   **Database Query Optimization:**
    *   **Indexing:** Ensure database tables have appropriate indexes on columns used in `WHERE` clauses, `JOIN` conditions, and `ORDER BY` clauses. (Coordinate with `database-specialist`).
    *   **Selective Fetching:** Only select the necessary columns from the database (`SELECT col1, col2` instead of `SELECT *`).
    *   **N+1 Problem:** Avoid fetching related data in loops. Use techniques like:
        *   **Eager Loading:** Fetch related data in a single query using `JOIN`s (supported by many ORMs).
        *   **Batching (DataLoader):** Especially relevant for GraphQL. Collect IDs in one pass, then fetch all related data in a single batch query.
*   **Efficient Data Processing:** Minimize complex computations or data transformations within the API request cycle. Perform heavy processing asynchronously in background jobs if possible.
*   **Payload Size:**
    *   Avoid returning excessively large amounts of data.
    *   Implement pagination for list endpoints.
    *   Allow clients to request specific fields (native in GraphQL, possible via query parameters like `?fields=id,name` in REST).
*   **Serialization/Deserialization:** Choose efficient libraries for handling JSON (or other formats) if performance is critical, though built-in methods are often sufficient.
*   **Asynchronous Operations:** Use asynchronous programming models effectively (async/await, Promises, goroutines, etc.) to avoid blocking the server thread during I/O operations (database calls, external API requests).

## Caching Strategies

Caching stores frequently accessed data temporarily to reduce the need to fetch or compute it repeatedly.

*   **HTTP Caching (Client-Side / Intermediate Caches):**
    *   **Focus:** Primarily for `GET` requests in REST APIs. Less applicable directly in GraphQL (which typically uses POST).
    *   **Mechanism:** Use standard HTTP headers returned by the API:
        *   `Cache-Control`: Specifies caching directives (e.g., `public`, `private`, `max-age=<seconds>`, `s-maxage=<seconds>`, `no-cache`, `no-store`).
        *   `ETag`: An identifier for a specific version of a resource. The client can send `If-None-Match` header; if the ETag matches, the server returns `304 Not Modified` without the body.
        *   `Last-Modified`: Timestamp of the last modification. Client sends `If-Modified-Since`; server returns `304` if not modified.
    *   **Implementation:** Set these headers in your API responses based on the data's volatility. Frameworks often provide helpers.
*   **Server-Side Caching (Application Level):**
    *   **Focus:** Caching data within the API application itself or using external caching systems (Redis, Memcached).
    *   **Mechanism:**
        *   **In-Memory Cache:** Store frequently accessed, non-sensitive data directly in the application's memory (simple but limited by server memory and not shared across instances). Use libraries like `node-cache` or simple objects/maps carefully.
        *   **Distributed Cache (Redis/Memcached):** Store data in an external, fast key-value store. Shared across multiple API instances. More scalable. Requires setup and management of the cache server.
    *   **What to Cache:** Results of expensive database queries, computed data, responses from external APIs.
    *   **Cache Invalidation:** Crucial! Define a strategy for removing or updating stale data in the cache when the underlying source data changes (e.g., time-based expiration, event-based invalidation after mutations).
*   **Database Caching:** Databases often have their own internal caching mechanisms. (Managed by `database-specialist`).
*   **CDN Caching:** Content Delivery Networks can cache API responses closer to users, especially for public, infrequently changing data. Controlled via HTTP `Cache-Control` headers (especially `s-maxage`).

## Considerations

*   **Cache Appropriateness:** Don't cache everything. Cache data that is expensive to fetch/compute and doesn't change too frequently. Caching rapidly changing or sensitive user-specific data requires careful consideration.
*   **Stale Data:** Caching introduces the possibility of serving stale data. Balance freshness requirements with performance gains.
*   **Cache Invalidation Complexity:** This is often the hardest part of caching. Ensure your invalidation strategy is robust.
*   **Monitoring:** Monitor cache hit rates and performance impact.

Consult with `performance-optimizer`, `database-specialist`, and `infrastructure-specialist` (via lead) for complex performance tuning and caching implementations.