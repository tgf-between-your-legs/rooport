# Frontend Security: Basic Considerations

Fundamental security practices for frontend development (HTML, CSS, JS).

## Core Concept

While many critical security measures happen on the backend, frontend code plays a vital role in preventing certain vulnerabilities and ensuring data sent to the backend is handled appropriately. The primary focus is preventing **Cross-Site Scripting (XSS)** and ensuring secure communication.

**Note:** This is a basic overview. Complex security issues require consultation with the `security-specialist` via your lead.

## Key Considerations

1.  **Cross-Site Scripting (XSS) Prevention:**
    *   **What it is:** Injecting malicious scripts into a website, which then execute in the browsers of other users.
    *   **Primary Defense: Avoid `innerHTML` with User Content.** Never directly insert untrusted data (content originating from users, APIs, or URLs) into the DOM using `element.innerHTML = ...`. This allows embedded `<script>` tags or `onerror` attributes to execute.
    *   **Use `textContent`:** When inserting text data, always prefer `element.textContent = ...`. This treats the data purely as text, preventing script execution.
    *   **Framework Sanitization:** Modern frontend frameworks (React, Vue, Angular) often sanitize data automatically when rendering variables in templates (e.g., `{data}` in JSX). Rely on framework mechanisms where possible.
    *   **Attribute Injection:** Be cautious when setting attributes like `href`, `src`, or event handlers (`onclick`) dynamically based on user input. Sanitize URLs (e.g., ensure they start with `http:`, `https:`, or `/`) and avoid constructing JavaScript directly in attributes.
        ```javascript
        // Potentially unsafe if 'userInput' contains 'javascript:alert("XSS")'
        // link.href = userInput;

        // Safer (basic check, more robust validation might be needed)
        if (userInput.startsWith('http:') || userInput.startsWith('https:') || userInput.startsWith('/')) {
          link.href = userInput;
        }

        // Avoid: element.setAttribute('onclick', 'doSomething("' + userInput + '")');
        ```
    *   **JSON Parsing:** When handling JSON from APIs, use `JSON.parse()`. Avoid `eval()`.

2.  **Secure API Communication:**
    *   **HTTPS:** Always use HTTPS for API endpoints to encrypt data in transit.
    *   **Authentication Tokens:** When calling protected APIs, send authentication tokens (like JWTs obtained from auth providers) securely, typically in the `Authorization: Bearer <token>` HTTP header. Avoid sending tokens directly in URL parameters.
    *   **Don't Expose Secrets:** Never embed API keys, secret tokens, or other sensitive credentials directly in frontend JavaScript code. These should be handled by the backend or via secure configuration mechanisms (e.g., backend-for-frontend pattern, secure environment variables for server-side rendering).

3.  **Input Validation (Client-Side vs. Server-Side):**
    *   **Client-Side Validation:** Use HTML5 attributes (`required`, `type="email"`, `pattern`, `minlength`) and JavaScript checks for immediate user feedback and better UX.
    *   **Server-Side Validation is CRUCIAL:** **Never rely solely on client-side validation.** Malicious users can bypass frontend checks. The backend *must* always re-validate all incoming data before processing it or saving it to a database.

4.  **Third-Party Libraries:**
    *   Be mindful of the security implications of including third-party scripts or libraries. Use reputable sources and keep libraries updated to patch known vulnerabilities.
    *   Consider using Subresource Integrity (SRI) hashes (`<script src="..." integrity="..." crossorigin="anonymous">`) for scripts loaded from CDNs to ensure they haven't been tampered with.

5.  **Clickjacking Prevention (Basic):**
    *   While primarily a server-side header concern (`X-Frame-Options` or `Content-Security-Policy: frame-ancestors`), basic frontend checks can sometimes prevent framing if necessary, though less robust.
    ```javascript
    // Basic check, easily bypassed, server headers are better
    // if (window.top !== window.self) {
    //   // Application is potentially framed
    //   window.top.location = window.self.location;
    // }
    ```

**When to Escalate:**

*   Handling sensitive data input/display (credit cards, PII).
*   Implementing complex authorization logic on the frontend.
*   Dealing with file uploads.
*   Concerns about specific XSS vectors or other vulnerabilities.
*   Implementing Content Security Policy (CSP).
*   Any uncertainty about security best practices.

Escalate these situations to your `frontend-lead`, suggesting consultation with the `security-specialist`. Security is critical and requires careful implementation.