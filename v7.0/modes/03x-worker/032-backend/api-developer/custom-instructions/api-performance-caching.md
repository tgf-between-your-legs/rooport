# API Performance: Caching Strategies

Leveraging caching to improve API response times and reduce server load.

## Core Concept: Avoiding Redundant Work

Caching involves storing the results of expensive operations (like database queries or complex computations) temporarily so that subsequent requests for the same data can be served faster from the cache, avoiding the need to repeat the original work.

**Benefits:**

*   **Reduced Latency:** Clients receive responses much faster for cached data.
*   **Reduced Server Load:** Fewer database queries and computations reduce CPU, memory, and I/O load on the server.
*   **Reduced External API Calls:** Caching responses from downstream APIs reduces costs and reliance on external services.
*   **Improved Scalability:** Caching allows the API to handle more requests with the same server resources.

**Types of Caching Relevant to APIs:**

1.  **HTTP Caching (Client-Side / Intermediary):** Using standard HTTP headers (`Cache-Control`, `ETag`, `Expires`, `Last-Modified`) to instruct clients and intermediary caches (like CDNs or proxies) on how to cache responses. Primarily for `GET` requests.
2.  **Server-Side Caching:** Storing data or computed results within the API's infrastructure.
    *   **In-Memory Cache:** Storing data directly in the application server's memory (e.g., using variables, maps, or dedicated libraries like `node-cache`). Fastest access but limited by server RAM and not shared across multiple server instances. Volatile (lost on restart).
    *   **Distributed Cache:** Using external caching systems like Redis or Memcached. Data is stored centrally and accessible by multiple API server instances. More scalable and persistent than in-memory caches.
    *   **Database Caching:** Some databases have built-in caching layers.
    *   **Full Response Caching:** Caching the entire generated API response.
    *   **Data Caching:** Caching specific data retrieved from databases or other sources before it's formatted into the API response.

## HTTP Caching Headers (for REST APIs)

These headers control how clients and proxies cache `GET` responses:

*   **`Cache-Control`:** The primary header. Directives include:
    *   `public`: Response can be cached by any cache (client, proxy, CDN).
    *   `private`: Response is specific to a single user and should only be cached by the client's browser (not shared caches).
    *   `no-cache`: Cache must revalidate with the origin server (using `ETag` or `Last-Modified`) before serving a cached response. Doesn't mean "don't cache", means "check first".
    *   `no-store`: Response should not be stored in any cache. Use for sensitive data.
    *   `max-age=<seconds>`: Maximum time the response is considered fresh.
    *   `s-maxage=<seconds>`: Like `max-age`, but specifically for shared caches (proxies, CDNs).
    *   `must-revalidate`: Cache must revalidate once stale, even if configured to serve stale content.
*   **`ETag` (Entity Tag):** An identifier for a specific version of a resource (often a hash of the content). The client sends this back in an `If-None-Match` header. If the resource hasn't changed, the server responds with `304 Not Modified` (empty body), saving bandwidth.
*   **`Last-Modified`:** Timestamp indicating when the resource was last changed. The client sends this back in an `If-Modified-Since` header. If the resource hasn't changed since that time, the server responds with `304 Not Modified`. `ETag` is generally preferred as it's more precise.
*   **`Expires`:** (Legacy HTTP/1.0) A specific date/time after which the response is considered stale. Overridden by `Cache-Control: max-age`.

**Example HTTP Cache Headers:**

```
// Cache publicly for 1 hour
Cache-Control: public, max-age=3600

// Cache privately for 5 minutes, must revalidate after
Cache-Control: private, max-age=300, must-revalidate
ETag: "xyz789"

// Do not cache at all
Cache-Control: no-store
```

## Server-Side Caching Strategies

*   **Identify Cacheable Data:** Determine which data changes infrequently and is expensive to compute or fetch. User-specific data often requires careful cache key design or might be less suitable for shared caches.
*   **Choose Cache Store:** Select in-memory (simple, fast, single-instance) or distributed (Redis/Memcached - scalable, shared, persistent).
*   **Cache Key Design:** Create unique keys based on the parameters that define the data being cached (e.g., `user:${userId}:profile`, `products:category:${categoryId}:page:${page}`).
*   **Cache Invalidation:** This is the hardest part of caching. Decide how to remove or update stale data in the cache when the underlying source changes.
    *   **Time-To-Live (TTL):** Automatically expire cache entries after a set duration (`max-age`). Simple but might serve stale data until expiry.
    *   **Explicit Invalidation:** When data is updated (e.g., via `POST`, `PUT`, `DELETE`), explicitly delete or update the corresponding cache entries. More complex but ensures freshness.
    *   **Write-Through Cache:** Write updates to both the cache and the primary data store simultaneously.
    *   **Write-Back Cache:** Write updates only to the cache initially, then asynchronously write to the primary store later (faster writes, but risk of data loss if cache fails).
*   **Cache Stampede Prevention:** Implement mechanisms (like locking) to prevent multiple concurrent requests for the same expired cache key from all hitting the database simultaneously.

**Example (Conceptual - Node.js/Redis):**

```javascript
// Using ioredis library (example)
import Redis from 'ioredis';
const redis = new Redis(); // Connects to localhost:6379 by default

async function getUserProfile(userId: string) {
  const cacheKey = `user:${userId}:profile`;

  // 1. Try fetching from cache
  try {
    const cachedData = await redis.get(cacheKey);
    if (cachedData) {
      console.log(`Cache HIT for ${cacheKey}`);
      return JSON.parse(cachedData);
    }
  } catch (err) {
    console.error('Redis GET error:', err); // Log error but continue
  }

  // 2. Cache MISS - Fetch from database
  console.log(`Cache MISS for ${cacheKey}`);
  const userProfile = await db.fetchUserProfile(userId); // Assume DB call

  // 3. Store in cache (with TTL, e.g., 1 hour)
  if (userProfile) {
    try {
      // Use 'EX' for seconds TTL
      await redis.set(cacheKey, JSON.stringify(userProfile), 'EX', 3600);
    } catch (err) {
      console.error('Redis SET error:', err); // Log error
    }
  }

  return userProfile;
}

// Invalidate cache when user profile is updated
async function updateUserProfile(userId: string, updates: any) {
    await db.updateUserProfile(userId, updates); // Update DB
    const cacheKey = `user:${userId}:profile`;
    try {
        await redis.del(cacheKey); // Delete cache entry
        console.log(`Cache invalidated for ${cacheKey}`);
    } catch (err) {
        console.error('Redis DEL error:', err);
    }
}
```

Caching is a powerful performance tool. Use HTTP caching headers for client-side/proxy caching of `GET` requests. Implement server-side caching (in-memory or distributed) for expensive operations, paying close attention to cache key design and invalidation strategies. Coordinate with `performance-optimizer` and `infrastructure-specialist` for complex caching setups.