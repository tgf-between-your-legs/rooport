# E2E Testing: Identifying and Mitigating Flaky Tests

Strategies for dealing with E2E tests that intermittently pass and fail without code changes.

## Core Concept: Unreliable Test Outcomes

Flaky tests are a major problem in E2E test suites. They pass sometimes and fail other times when run against the *same* application code, making it difficult to trust the test results and diagnose real regressions. Identifying and fixing the root cause of flakiness is crucial for maintaining a reliable and valuable test suite.

## Common Causes of Flakiness

1.  **Timing Issues / Race Conditions:**
    *   **Problem:** The test script tries to interact with an element before it's fully loaded, visible, interactive, or updated after an action. The application state might change unpredictably relative to the test execution speed.
    *   **Mitigation:**
        *   **Use Explicit Waits:** Wait for specific conditions (element visibility, text content, network request completion, absence of loading indicators) before proceeding. Avoid fixed `sleep()` calls.
        *   **Leverage Framework Auto-Waiting:** Understand and utilize the built-in waiting mechanisms of Cypress and Playwright.
        *   **Wait for Network Requests:** If an action triggers an API call that updates the UI, wait for that call to complete before asserting on the updated UI state (using `cy.intercept`/`cy.wait` or `page.waitForResponse`).
2.  **Brittle Selectors:**
    *   **Problem:** Selectors based on dynamic classes, complex CSS paths, or exact text content break easily when unrelated UI changes occur.
    *   **Mitigation:** Use robust selectors: `data-testid`, ARIA roles, labels, placeholder text (see `e2e-selector-strategies.md`).
3.  **Test Data Issues:**
    *   **Problem:** Tests depend on shared, mutable data in the test environment. One test might modify or delete data needed by another, causing intermittent failures depending on execution order. Hardcoded IDs might become invalid.
    *   **Mitigation:**
        *   **Isolate Data:** Create necessary data programmatically before each test/suite and clean it up afterwards (API calls, DB scripts).
        *   **Unique Data:** Use unique identifiers (timestamps, random strings) for data created within tests to avoid collisions.
        *   **Database Reset/Snapshots:** Reset the database to a known state before test runs.
4.  **Environment Instability:**
    *   **Problem:** The test environment itself (backend server, database, network, third-party services) might be slow, unresponsive, or experiencing intermittent errors.
    *   **Mitigation:** Monitor test environment stability. Implement retries (with caution) in CI for known intermittent infrastructure issues. Collaborate with `infrastructure-specialist`/`devops-lead`.
5.  **Asynchronous Operations:**
    *   **Problem:** Not properly waiting for asynchronous operations within the application (e.g., animations, debounced updates, background processes) to complete before making assertions.
    *   **Mitigation:** Use explicit waits for UI changes, network calls, or specific application states that indicate the async operation is finished. Sometimes requires adding specific test hooks or status indicators in the application code.
6.  **Test Order Dependency:**
    *   **Problem:** One test implicitly relies on the state created or modified by a previous test. Running tests individually or in a different order causes failures.
    *   **Mitigation:** Ensure each test is self-contained and sets up its own required state. Avoid sharing state between tests.
7.  **Resource Contention (Parallel Execution):**
    *   **Problem:** When running tests in parallel, multiple tests might try to access or modify the same shared resource (e.g., a specific user account, a limited pool of test data) simultaneously, leading to conflicts.
    *   **Mitigation:** Design tests to use unique resources where possible. Implement locking mechanisms or use separate environments/databases for parallel runs if necessary.

## Investigating Flakiness

1.  **Reproduce Locally:** Try running the failing test multiple times locally. Can you reproduce the failure consistently or intermittently?
2.  **Analyze Artifacts:** Examine logs, screenshots, and videos (if available) from the failed runs. Look for timing differences, unexpected UI states, or console errors. Playwright's Trace Viewer is particularly useful here.
3.  **Isolate the Failure:** Run the single failing test file or even the single failing test block repeatedly (`.only` in Cypress/Playwright).
4.  **Add Logging/Debugging:** Add `cy.log()`, `console.log`, or debugger statements in your test script to understand the state at different points. Use `cy.pause()` or Playwright Inspector to step through execution.
5.  **Check Waits/Assertions:** Are there missing waits? Are assertions checking for the correct state *after* an action should have completed? Add more specific waits or assertions.
6.  **Review Selectors:** Are the selectors robust? Could they be matching multiple elements intermittently?
7.  **Examine Test Data:** Is the test relying on specific data that might not always be present or might be modified by other processes?
8.  **Consider Environment:** Could network latency or server performance be a factor?

Addressing flaky tests requires patience and systematic debugging. Prioritize fixing them, as a flaky test suite quickly loses its value. Implement robust waits, reliable selectors, and isolated test data strategies from the start to minimize flakiness.