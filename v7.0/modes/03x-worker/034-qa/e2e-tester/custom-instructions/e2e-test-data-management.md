# E2E Testing: Test Data Management Strategies

Approaches for creating, managing, and cleaning up data used in E2E tests.

## Core Concept: Reliable & Isolated Test State

E2E tests often require specific data to exist in the application state (database, user accounts, etc.) to execute user flows correctly. Managing this test data effectively is crucial for creating reliable, repeatable, and isolated tests. Poor data management leads to flaky tests and maintenance headaches.

**Goals:**

*   **Isolation:** Tests should not interfere with each other due to shared or leftover data.
*   **Repeatability:** Tests should produce the same result every time they run against the same code version.
*   **Control:** Easily create the specific data state needed for a given test scenario.
*   **Performance:** Data setup/teardown shouldn't significantly slow down the test suite.

## Common Strategies

1.  **Programmatic Setup via API (Often Preferred):**
    *   **How:** Before a test or test suite runs (`beforeEach`/`beforeAll`), use API calls (via `cy.request()`, Playwright's `request` context, or a dedicated API client) to create the necessary users, resources, or configurations needed for the test scenario.
    *   **Pros:** Decouples tests from UI changes for setup. Generally faster than UI-based setup. Promotes testing the API alongside the UI. Test data is created specifically for the test, improving isolation.
    *   **Cons:** Requires a stable API for setup. Tests might depend on API functionality working correctly.
    *   **Example (Conceptual Cypress):**
        ```javascript
        beforeEach(() => {
          // Create a user via API before logging in through UI
          cy.request('POST', '/api/test/users', { username: 'testuser', role: 'editor' })
            .then((response) => {
              const userId = response.body.id;
              // Create an article belonging to this user
              cy.request('POST', '/api/test/articles', { title: 'Test Article', authorId: userId });
            });
          // Log in via UI or API token
          cy.login('testuser', 'password'); // Assuming a custom login command
        });
        ```

2.  **Programmatic Setup via Backend Scripts/Commands:**
    *   **How:** Execute backend commands or scripts (e.g., Django `manage.py` commands, database seeding scripts) before tests run to set up the required database state.
    *   **Pros:** Can handle complex data setup efficiently. Bypasses UI and potentially API layers.
    *   **Cons:** Requires access to execute backend commands from the test environment. Tightly couples tests to backend implementation details.
    *   **Example (Conceptual):**
        ```bash
        # In CI or test setup script
        docker-compose exec backend python manage.py seed_test_data --scenario=editor_with_articles
        npx playwright test
        ```

3.  **Database Reset/Snapshotting:**
    *   **How:** Reset the test database to a known clean state before each test or suite. Alternatively, restore the database from a snapshot.
    *   **Pros:** Provides strong isolation. Ensures a consistent starting point.
    *   **Cons:** Can be slow, especially for large databases. Requires infrastructure/tooling for efficient resets or snapshots.

4.  **UI-Based Setup (Use Sparingly):**
    *   **How:** Use UI automation steps within your tests (or `beforeEach` hooks) to create the necessary data (e.g., navigate to an "add product" page, fill the form, save).
    *   **Pros:** Tests the creation UI itself. Doesn't require API access.
    *   **Cons:** **Slowest and most brittle approach.** Setup steps are prone to breaking if the UI changes. Makes tests longer and harder to debug. Should generally be avoided for data setup if API/backend methods are available. Only use it when testing the creation flow *is* the primary goal of the test.

5.  **Using Existing Data (Least Recommended):**
    *   **How:** Relying on data that is assumed to already exist in the test environment database.
    *   **Pros:** Simplest setup (no setup needed).
    *   **Cons:** **Extremely brittle and unreliable.** Tests break if data changes or is deleted. Leads to inter-test dependencies and makes parallel execution difficult. Hard to ensure the required state exists. **Avoid this.**

## Cleanup Strategies

*   **API-Based Cleanup:** Use API calls in `afterEach`/`afterAll` hooks to delete the specific data created during the test.
*   **Backend Script Cleanup:** Run backend commands to clean up test-specific data.
*   **Database Reset/Snapshot Restore:** If using this for setup, it also handles cleanup.
*   **Marking Data:** Add a specific flag (e.g., `is_test_data=true`) to created data and have a separate process to clean up marked data periodically (less reliable for immediate isolation).

## Best Practices

*   **Prefer Programmatic Setup:** Use API calls or backend scripts for data setup whenever possible.
*   **Isolate Data:** Aim for each test to create the specific data it needs and clean it up afterwards, or use database resets.
*   **Unique Identifiers:** Use unique names/identifiers for test data (e.g., timestamps, random strings) to avoid collisions if cleanup fails or when running tests in parallel.
*   **Helper Functions/Commands:** Encapsulate common data setup/teardown logic into reusable helper functions or custom framework commands (like Cypress custom commands).
*   **Balance Speed and Isolation:** Choose the strategy that provides sufficient isolation without making the test suite prohibitively slow. API setup is often a good balance.

Effective test data management is key to reliable E2E testing. Prioritize programmatic setup and cleanup via APIs or backend scripts for better isolation and maintainability compared to UI-based setup or relying on existing data.