# 4. Key Considerations / Safety Protocols

- **Security:** Implement Angular security best practices, including input sanitization (using `DomSanitizer` if needed) and preventing common vulnerabilities. Angular provides built-in XSS protection; be cautious when bypassing it (e.g., with `[innerHTML]`).
- **Performance:** Write efficient code. Use `OnPush` change detection where appropriate. Implement lazy loading for feature modules. Optimize RxJS pipelines. Use Signals for fine-grained reactivity.
- **Maintainability:** Follow Angular style guides and project conventions. Create reusable components and services. Write clear, testable code.