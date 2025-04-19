# SvelteKit Dev: Service Workers

Service workers enable offline support, background sync, and push notifications by running a script in the background, separate from the web page.

## 1. Setup

1.  **Create `src/service-worker.js` (or `.ts`):** This is the entry point for service worker logic. It runs in a separate thread and uses standard Service Worker APIs (`self`, `caches`, `fetch`, etc.).
2.  **SvelteKit Integration:** SvelteKit automatically registers the service worker if the file exists. Configuration in `svelte.config.js` under `kit.serviceWorker` is usually not needed unless customizing registration or file inclusion.
3.  **`$service-worker` Modules:** SvelteKit provides virtual modules for use within `src/service-worker.js`:
    *   `import { build, files, prerendered, version } from '$service-worker';`
    *   `build`: Array of URLs for SvelteKit/Vite generated assets (JS/CSS chunks).
    *   `files`: Array of URLs for files in your `static` directory.
    *   `prerendered`: Array of URLs for pre-rendered pages.
    *   `version`: Unique build identifier string, useful for cache naming and cleanup.

## 2. Service Worker Lifecycle & Caching

**a) `install` Event:**

*   Fires when the worker is first installed or updated.
*   Use `event.waitUntil()` to ensure caching completes before activation.
*   **Primary Use:** Precache essential application assets (`build`, `files`, `prerendered`) using the Cache API.

```typescript
// src/service-worker.ts
/// <reference types="@sveltejs/kit" />
import { build, files, version } from '$service-worker';

const CACHE_NAME = `cache-${version}`;
const ASSETS_TO_CACHE = [...build, ...files]; // Combine build artifacts and static files

self.addEventListener('install', (event) => {
  const sw = self as unknown as ServiceWorkerGlobalScope;
  console.log('[SW] Install event');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[SW] Caching app shell');
        return cache.addAll(ASSETS_TO_CACHE);
      })
      .then(() => {
        sw.skipWaiting(); // Activate the new worker immediately
      })
  );
});
```

**b) `activate` Event:**

*   Fires after installation when the worker takes control.
*   Use `event.waitUntil()` to ensure cleanup completes.
*   **Primary Use:** Clean up old caches associated with previous versions.

```typescript
// src/service-worker.ts (continued)
self.addEventListener('activate', (event) => {
  const sw = self as unknown as ServiceWorkerGlobalScope;
  console.log('[SW] Activate event');
  event.waitUntil(
    caches.keys().then(async (cacheNames) => {
      await Promise.all(
        cacheNames.map(async (cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('[SW] Deleting old cache:', cacheName);
            await caches.delete(cacheName);
          }
        })
      );
    }).then(() => {
      sw.clients.claim(); // Take control of existing clients
    })
  );
});
```

**c) `fetch` Event:**

*   Fires for every network request made by controlled pages.
*   Use `event.respondWith()` to intercept the request and provide a custom response (from cache or network).
*   Implement caching strategies here (Cache First, Network First, Stale-While-Revalidate).

```typescript
// src/service-worker.ts (continued)
// Example: Cache First strategy for GET requests
self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return; // Ignore non-GET

  event.respondWith(
    caches.match(req).then((cachedResponse) => {
      // Return from cache if found
      if (cachedResponse) {
        console.log(`[SW] Cache hit: ${req.url}`);
        return cachedResponse;
      }

      // Otherwise, fetch from network
      console.log(`[SW] Network fetch: ${req.url}`);
      return fetch(req).then(async (networkResponse) => {
        // Optional: Cache successful network responses
        if (networkResponse.ok) {
          try {
            const cache = await caches.open(CACHE_NAME);
            // Clone response as it's a one-time use stream
            await cache.put(req, networkResponse.clone());
            console.log(`[SW] Cached network response: ${req.url}`);
          } catch (cacheError) {
            console.error(`[SW] Failed to cache ${req.url}:`, cacheError);
          }
        }
        return networkResponse;
      }).catch(error => {
        console.error(`[SW] Network fetch failed: ${req.url}`, error);
        // Optional: Return an offline fallback page
        // return caches.match('/offline.html');
        throw error;
      });
    })
  );
});
```

## 3. Caching Strategies

*   **Cache First (Offline First):** Try cache, fallback to network. Good for app shell, static assets. (Example above).
*   **Network First:** Try network, fallback to cache. Good for frequently changing data where freshness is key.
*   **Stale-While-Revalidate:** Serve from cache immediately (stale), fetch update in background. Good balance for non-critical, updating content.

## 4. Updating

*   New builds generate a new `version`.
*   Browser detects the change, runs `install` for the new worker.
*   New worker waits until old worker's clients are closed, unless `self.skipWaiting()` is called.
*   `activate` runs, cleaning old caches.

## 5. Considerations

*   **Scope:** Controls pages under its scope (usually `/`).
*   **HTTPS:** Required (except `localhost`).
*   **Debugging:** Use browser dev tools (Application -> Service Workers). Enable "Update on reload" during development.
*   **Complexity:** Can become complex quickly. Consider libraries like Workbox for advanced scenarios.