# Frontend Security: Basic Considerations

Fundamental security practices for frontend development (HTML, CSS, JS). While backend security is paramount, frontend code must prevent client-side vulnerabilities like XSS.

**Note:** This is a basic overview. Escalate complex security issues or uncertainties to `frontend-lead`, suggesting consultation with the `security-specialist`.

## Key Considerations

1.  **Cross-Site Scripting (XSS) Prevention:**
    *   **Goal:** Prevent injection and execution of malicious scripts in users' browsers.
    *   **Primary Defense: Avoid `innerHTML` with Untrusted Data.** Never insert data from users, APIs, or URLs directly using `element.innerHTML = ...`.
    *   **Use `textContent`:** Always prefer `element.textContent = ...` for inserting text data. It treats input as plain text, preventing script execution.
    *   **Framework Sanitization:** Rely on built-in sanitization mechanisms provided by frameworks (React, Vue, Angular) when rendering data in templates (e.g., `{data}` in JSX).
    *   **Attribute Injection:** Be cautious setting attributes like `href`, `src`, or event handlers (`onclick`) dynamically.
        *   Sanitize URLs (ensure they start with `http:`, `https:`, `/`, or are relative paths within the application). Avoid `javascript:` URLs from untrusted sources.
        *   Avoid constructing JS directly in attributes (e.g., `onclick="doSomething('{{userInput}}')" `). Use `addEventListener` instead.
    *   **JSON Parsing:** Use `JSON.parse()` to parse JSON from APIs. **Never use `eval()`**.

    ```javascript
    // Unsafe if userInput could be 'javascript:alert("XSS")'
    // link.href = userInput;

    // Safer (basic check)
    function isValidUrl(url) {
        return url.startsWith('http:') || url.startsWith('https:') || url.startsWith('/') || url.startsWith('#');
    }
    if (isValidUrl(userInput)) {
      link.href = userInput;
    }

    // Unsafe:
    // element.innerHTML = untrustedData;
    // element.setAttribute('onclick', 'alert("' + untrustedData + '")');

    // Safer:
    element.textContent = untrustedData;
    element.addEventListener('click', () => { alert(someSafeValue); });
    ```

2.  **Secure API Communication:**
    *   **HTTPS:** Always use HTTPS for API endpoints.
    *   **Authentication Tokens (e.g., JWT):** Send tokens securely in the `Authorization: Bearer <token>` HTTP header. Avoid sending tokens in URL parameters.
    *   **Don't Expose Secrets:** Never embed API keys, secret tokens, or other credentials directly in frontend JavaScript code. These belong on the backend or in secure configuration.

3.  **Input Validation:**
    *   **Client-Side:** Use HTML5 attributes (`required`, `type="email"`, `pattern`, `minlength`) and JavaScript for immediate user feedback (UX).
    *   **Server-Side is CRUCIAL:** **Never rely solely on client-side validation.** The backend *must* always re-validate *all* incoming data.

4.  **Third-Party Libraries:**
    *   Use reputable sources (npm, CDNs).
    *   Keep libraries updated to patch known vulnerabilities.
    *   Consider using Subresource Integrity (SRI) hashes (`<script src="..." integrity="..." crossorigin="anonymous">`) for CDN scripts.

5.  **Clickjacking Prevention (Basic Awareness):**
    *   Primarily handled server-side via `X-Frame-Options` or `Content-Security-Policy: frame-ancestors` headers. Frontend checks are generally insufficient. Be aware of the risk if embedding external content or allowing your site to be framed.

## When to Escalate

*   Handling sensitive data input/display (credit cards, PII).
*   Implementing complex authorization logic on the frontend.
*   Dealing with file uploads.
*   Concerns about specific XSS vectors or other vulnerabilities (CSRF, etc.).
*   Implementing Content Security Policy (CSP).
*   Any uncertainty about security best practices.

Report these situations to your `frontend-lead`, suggesting consultation with the `security-specialist`.