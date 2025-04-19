# Integration Testing: Test Data Strategies

Managing data setup and teardown for reliable integration tests.

## Core Concept: Controlled State for Interactions

Integration tests verify interactions between components, and these interactions often depend on specific data existing in one or both components (e.g., a user record, a product entry, a configuration setting). Managing this test data effectively is crucial for ensuring tests are reliable, repeatable, and isolated.

**Challenges:**

*   **State Pollution:** One test modifying data that causes another unrelated test to fail.
*   **Data Dependencies:** Tests failing because the specific data they expect doesn't exist or has changed.
*   **Slow Setup/Teardown:** Complex data requirements slowing down the entire test suite.
*   **Data Consistency:** Ensuring data across integrated components (e.g., user ID in service A matches user ID in service B) is consistent for the test scenario.

## Common Strategies for Integration Tests

1.  **API-Driven Setup & Teardown (Often Preferred):**
    *   **How:** Use the APIs of the services under test to create necessary data before a test (`beforeEach`/`setup`) and delete it afterwards (`afterEach`/`teardown`).
    *   **Pros:** Tests the APIs themselves. Relatively fast. Promotes test isolation if data is created uniquely per test. Decouples tests from database schema details.
    *   **Cons:** Relies on stable and functional create/delete API endpoints. Can be complex if multiple dependent resources need creation.
    *   **Example:** Before testing adding an item to a cart, call the `/products` API to create the product and the `/users` API to create the user. After the test, call the corresponding DELETE endpoints.

2.  **Backend Seeding Scripts/Commands:**
    *   **How:** Execute dedicated scripts or commands (e.g., `manage.py seed_scenario_X`, custom scripts using an ORM) that directly manipulate the database(s) to insert the required data before tests and potentially clean it up after.
    *   **Pros:** Can handle complex data relationships efficiently. Bypasses API layers. Can be faster than API setup for large amounts of data.
    *   **Cons:** Tightly couples tests to database schema. Requires execution access in the test environment. Cleanup scripts need careful implementation.
    *   **Example:** Run a script `seed_database.py --scenario order_processing` before the test suite.

3.  **Database Reset / Transaction Rollback:**
    *   **How:**
        *   **Reset:** Wipe the test database(s) and re-apply schema/base fixtures before each test run or suite.
        *   **Rollback:** Run each test within a database transaction and roll it back afterwards (common in framework test runners like Django `TestCase`).
    *   **Pros:** Provides strong isolation. Ensures a clean state for each test. Rollback is often very fast.
    *   **Cons:** Full reset can be slow. Rollback might not work across *multiple* services/databases unless using distributed transactions (which are complex). Doesn't test data persistence explicitly if always rolled back.

4.  **Fixtures (Static Data Files):**
    *   **How:** Load pre-defined data from files (JSON, YAML) into the database before tests run.
    *   **Tools:** Django `loaddata`, `pytest-django` fixtures.
    *   **Pros:** Simple for defining static, reusable datasets. Version controllable.
    *   **Cons:** Can become difficult to manage for complex relationships. Data is static, making it harder to test variations. Loading large fixtures can be slow. Risk of state pollution if not reset between tests.

5.  **Factories (e.g., `factory-boy`):**
    *   **How:** Use factory libraries to programmatically generate model instances with default or customized attributes. Often used within test setup methods.
    *   **Pros:** Highly flexible for creating data variations. Reduces boilerplate code for object creation. Can handle relationships. More maintainable than large static fixtures.
    *   **Cons:** Adds a library dependency. Requires writing factory definitions.

## Cleanup Strategies

*   **Explicit Deletion (API/Script):** Call DELETE endpoints or run cleanup scripts corresponding to the setup method.
*   **Transaction Rollback:** Automatically handled by some test frameworks/runners.
*   **Database Reset:** Wipes data as part of the reset process.
*   **Data Marking:** Flag test data and use a separate process for cleanup (less ideal for isolation).

## Best Practices

*   **Prioritize Isolation:** Aim for tests that don't depend on each other's data. API-driven setup/teardown per test or transaction rollback often provide good isolation.
*   **Use Unique Data:** Generate unique identifiers (names, emails, IDs using timestamps or random strings) within tests to prevent collisions, especially when running in parallel or if cleanup fails.
*   **Setup in `beforeEach`/`setup`:** Create data needed for a specific test just before it runs.
*   **Teardown in `afterEach`/`teardown`:** Clean up data created by a test immediately after it runs. Use `try...finally` or equivalent constructs to ensure cleanup happens even if the test fails.
*   **Balance Speed and Reliability:** Choose the strategy that provides the necessary isolation and reliability without making the test suite impractically slow. API setup or factories within transactional tests often strike a good balance.
*   **Document Data Needs:** Clearly document the data prerequisites for complex integration tests.

Choosing the right test data strategy depends on the system architecture, the type of integration being tested, and the desired balance between test speed, isolation, and realism.