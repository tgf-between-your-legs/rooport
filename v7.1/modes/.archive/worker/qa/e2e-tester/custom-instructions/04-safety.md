# 4. Key Considerations / Safety Protocols

*   **Test Environment:** Ensure tests run against a stable, dedicated test environment. Avoid running destructive tests against production.
*   **Test Data Management:** Develop strategies for creating and cleaning up test data to ensure tests are repeatable.
*   **Selector Strategy:** Prioritize user-facing attributes (`role`, `label`, `text`) and test IDs (`data-testid`) over brittle selectors (CSS classes, XPath).
*   **Flakiness:** Actively investigate and fix flaky tests (tests that pass sometimes and fail sometimes without code changes). Implement proper waits and assertions.
*   **Secrets Management:** Handle test user credentials or API keys securely (e.g., environment variables, secrets management tools). Do not hardcode secrets in tests.