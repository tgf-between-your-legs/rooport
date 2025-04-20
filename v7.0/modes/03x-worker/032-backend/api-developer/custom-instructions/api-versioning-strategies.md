# API Versioning Strategies

Approaches for managing changes and introducing new versions of an API without breaking existing clients.

## Core Concept: Managing Breaking Changes

As APIs evolve, you'll inevitably need to introduce changes. Some changes are non-breaking (e.g., adding a new optional field or a new endpoint), while others are **breaking changes** (e.g., removing a field, changing a data type, altering endpoint behavior) that would cause existing clients to fail.

API versioning provides a way for clients to opt-in to specific versions of the API, allowing you to introduce breaking changes in new versions while maintaining older versions for existing clients until they can migrate.

## Common Versioning Strategies

1.  **URI Path Versioning (Most Common):**
    *   **How:** Include the major version number directly in the URI path, typically at the beginning.
    *   **Example:**
        *   `https://api.example.com/v1/users`
        *   `https://api.example.com/v2/users`
    *   **Pros:** Very explicit and clear. Easy to see the version being used in logs, browser bars, and documentation. Simple routing on the server. Easy to cache.
    *   **Cons:** "Pollutes" the URI. Doesn't strictly adhere to the REST principle that a URI identifies a unique resource (the resource itself hasn't changed, only its representation/behavior).

2.  **Query Parameter Versioning:**
    *   **How:** Include the version number as a query parameter.
    *   **Example:**
        *   `https://api.example.com/users?version=1`
        *   `https://api.example.com/users?version=2` (or `?api-version=2`)
    *   **Pros:** Keeps the base URI clean. Relatively easy to implement and test in browsers.
    *   **Cons:** Query parameters can be less obvious than path segments. Can make caching slightly more complex if caches don't respect the version parameter properly. Easy for clients to forget to include it, potentially defaulting to the latest (breaking) or oldest version.

3.  **Custom Header Versioning:**
    *   **How:** Include the version number in a custom HTTP request header (e.g., `X-API-Version`, `Api-Version`).
    *   **Example:**
        *   `GET /users HTTP/1.1`
        *   `Host: api.example.com`
        *   `X-API-Version: 1`
    *   **Pros:** Keeps the URI clean. Semantically separates versioning information from resource identification.
    *   **Cons:** Less visible/discoverable than URI versioning. Cannot be easily tested directly in a browser address bar. Requires clients to correctly set the header.

4.  **Accept Header Versioning (Media Type Versioning):**
    *   **How:** Use the standard `Accept` header with a custom media type that includes the version.
    *   **Example:**
        *   `GET /users HTTP/1.1`
        *   `Host: api.example.com`
        *   `Accept: application/vnd.example.v1+json` (Requesting v1)
        *   `Accept: application/vnd.example.v2+json` (Requesting v2)
    *   **Pros:** Considered the "most RESTful" approach by some, as it uses standard HTTP mechanisms for content negotiation. Keeps URIs clean.
    *   **Cons:** Can be cumbersome to use and test. Less intuitive for many developers compared to URI versioning. Requires careful handling of media types on both client and server.

## Choosing a Strategy

*   **URI Path Versioning (`/v1/`)** is the most widely used and generally understood approach. It's pragmatic and easy to implement, route, and document, despite not being the "purest" REST approach. **Often the recommended default unless specific needs dictate otherwise.**
*   **Header/Query Parameter Versioning** can be good alternatives if keeping URIs clean is a high priority, but they come with discoverability/usability trade-offs.
*   **Accept Header Versioning** is technically sound but often considered overly complex for typical use cases.

## Best Practices

*   **Version Only for Breaking Changes:** Avoid introducing new versions for non-breaking changes (like adding optional fields or new endpoints).
*   **Major Versions:** Typically, only increment the major version number (`v1`, `v2`) for breaking changes. Minor/patch changes should be backward compatible within a major version.
*   **Documentation:** Clearly document the current version, changes between versions, and any deprecation timelines for older versions.
*   **Deprecation Strategy:** Plan how you will phase out old API versions. Provide clear timelines and communicate them to clients. Consider returning `Warning` headers or specific response codes for deprecated endpoints.
*   **Default Version:** Decide whether requests without an explicit version should default to the oldest supported version (safer for existing clients) or the latest version (forces clients to be explicit). Explicit versioning is generally preferred.

Choose a versioning strategy early in the API design process and apply it consistently. URI path versioning is often the most practical choice.

*(Refer to API design guides and articles discussing versioning trade-offs.)*