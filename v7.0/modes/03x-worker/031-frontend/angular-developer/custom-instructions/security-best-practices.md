# Angular: Security Best Practices

Key security considerations when developing Angular applications.

## Core Concept: Built-in Protections

Angular incorporates several built-in protections against common web vulnerabilities, particularly Cross-Site Scripting (XSS). Understanding these protections and knowing when *not* to bypass them is crucial.

## Key Security Areas

1.  **Cross-Site Scripting (XSS) Prevention:**
    *   **Concept:** XSS occurs when attackers inject malicious scripts into your application, which then execute in users' browsers.
    *   **Angular's Protection:** Angular treats all values bound into the DOM (via interpolation `{{}}`, property binding `[]`) as untrusted by default. It automatically **sanitizes** these values before rendering them, removing potentially harmful content like `<script>` tags or `onerror` attributes.
    *   **Interpolation (`{{ value }}`):** Automatically sanitized. Safe for displaying user-provided text content.
    *   **Property Binding (`[property]="value"`):** Automatically sanitized for most safe properties (e.g., `[src]`, `[href]`, `[alt]`). Binding to potentially dangerous properties like `[innerHTML]` or `[outerHTML]` requires explicit trust.
    *   **`[innerHTML]` Binding:** **Avoid binding user-provided content directly to `innerHTML`.** This bypasses Angular's sanitization and creates a significant XSS risk. If you *must* render HTML content that you *know* is safe (e.g., from a trusted CMS using a strict sanitizer), you need to explicitly bypass Angular's sanitization using `DomSanitizer`.
    *   **`DomSanitizer`:** An injectable service used to mark values as trusted for specific contexts (HTML, styles, scripts, URLs, resource URLs). Use it **only** when you are certain the content is safe and cannot be manipulated by users.
        ```typescript
        import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
        import { inject } from '@angular/core';

        // In your component:
        private sanitizer = inject(DomSanitizer);
        trustedHtmlContent: SafeHtml;

        constructor() {
          const unsafeHtmlFromTrustedSource = '<p>This is <b>trusted</b> HTML.</p>';
          // Explicitly trust the HTML
          this.trustedHtmlContent = this.sanitizer.bypassSecurityTrustHtml(unsafeHtmlFromTrustedSource);
        }
        ```
        ```html
        <!-- In the template -->
        <div [innerHTML]="trustedHtmlContent"></div> <!-- Binds the trusted HTML -->
        ```
    *   **Template Security:** Avoid generating Angular templates dynamically on the server or client using user input, as this can also lead to injection vulnerabilities.

2.  **HTTP-Level Vulnerabilities:**
    *   **Cross-Site Request Forgery (XSRF/CSRF):** Angular's `HttpClient` has built-in support for a common mechanism where the server sends a token in a cookie (`XSRF-TOKEN`), and `HttpClient` automatically reads this token and sends it back in a custom HTTP header (`X-XSRF-TOKEN`) on subsequent requests (especially non-GET requests). Your backend needs to be configured to generate the cookie token and validate the header token on state-changing requests.
    *   **Cross-Site Script Inclusion (XSSI):** Angular's `HttpClient` automatically prefixes JSON responses with `)]}',\n` before parsing to mitigate certain XSSI attacks. Your backend framework might do this automatically, or you may need to configure it.

3.  **API Security:**
    *   **Authentication/Authorization:** Secure your backend APIs properly. Angular itself doesn't handle backend authentication, but `HttpClient` interceptors (see `httpclient-interceptors.md`) are commonly used to attach authentication tokens (like JWT Bearer tokens) to outgoing requests. Implement authorization checks on the *server-side*.
    *   **HTTPS:** Always use HTTPS for communication between the Angular app and backend APIs to encrypt data in transit.

4.  **Dependency Management:**
    *   Keep Angular and third-party libraries updated to patch known security vulnerabilities. Regularly run `npm audit` or `yarn audit`.

5.  **Content Security Policy (CSP):**
    *   Consider implementing a strict Content Security Policy via HTTP headers on your web server to define trusted sources for scripts, styles, images, etc., further mitigating XSS risks.

## Summary

*   Trust Angular's default sanitization for DOM bindings.
*   **Never bind user input directly to `innerHTML`**. Use `DomSanitizer.bypassSecurityTrustHtml` only for content you absolutely trust and control.
*   Leverage `HttpClient`'s built-in XSRF protection by coordinating with your backend.
*   Secure your backend APIs independently (authentication, authorization).
*   Use HTTPS.
*   Keep dependencies updated.
*   Consider using CSP.

By following these practices, you can significantly reduce the risk of common web security vulnerabilities in your Angular applications.

*(Refer to the official Angular Security documentation.)*