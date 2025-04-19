# API Testing Strategies

Approaches for verifying the correctness, reliability, and performance of APIs.

## Core Concept: Ensuring API Quality

Testing is essential to ensure your API functions correctly, handles errors gracefully, performs well, remains secure, and meets the contract expected by consumers. Different types of tests focus on different aspects of the API.

**Key Testing Levels:**

1.  **Unit Testing:** Testing individual functions, modules, or classes in isolation (e.g., testing a specific validation function, a service logic unit, or a data transformation utility). Does not involve HTTP requests or external dependencies like databases (these are mocked).
2.  **Integration Testing:** Testing the interaction between different components of the API, often including database interactions or calls to other internal services. Typically involves making real HTTP requests to the API endpoints running in a test environment.
3.  **Contract Testing:** Verifying that the API adheres to its defined contract (e.g., OpenAPI spec or GraphQL schema). Ensures that requests and responses match the expected structure and types. Can be done provider-side (checking if the API implementation matches the spec) or consumer-side (checking if a client's usage matches the spec).
4.  **End-to-End (E2E) Testing:** Testing complete user flows that involve the API, often initiated from the UI level. Verifies the entire system integration. (Usually handled by `e2e-tester` mode).
5.  **Performance Testing:** Assessing the API's responsiveness, throughput, and stability under load. (Usually handled by `performance-optimizer` mode).
6.  **Security Testing:** Actively probing the API for vulnerabilities. (Usually handled by `security-specialist` mode).

This mode (`api-developer`) primarily focuses on **Unit Testing** and **Integration Testing**, and potentially basic **Contract Testing**.

## Unit Testing

*   **Goal:** Verify the logic of individual functions/modules in isolation.
*   **Tools:** Standard testing frameworks for the backend language (e.g., Jest/Vitest for Node.js, Pytest for Python, PHPUnit for PHP). Mocking libraries (e.g., Jest mocks, `unittest.mock` in Python).
*   **Focus:** Test business logic, validation functions, data transformations, utility functions. Mock external dependencies (database calls, external API calls).
*   **Example (Conceptual - Node.js/Jest):**
    ```javascript
    // src/validators.js
    export function isValidEmail(email) {
      if (!email) return false;
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    // src/validators.test.js
    import { isValidEmail } from './validators';

    describe('isValidEmail', () => {
      it('returns true for valid emails', () => {
        expect(isValidEmail('test@example.com')).toBe(true);
      });
      it('returns false for invalid emails', () => {
        expect(isValidEmail('test@example')).toBe(false);
        expect(isValidEmail('test.example.com')).toBe(false);
        expect(isValidEmail('')).toBe(false);
        expect(isValidEmail(null)).toBe(false);
      });
    });
    ```

## Integration Testing

*   **Goal:** Verify the interaction between API components, including routing, controllers/resolvers, services, data access, and potentially the database.
*   **Tools:** Testing framework (Jest, Vitest, Pytest), HTTP client library (Supertest for Node.js, `requests` or `httpx` for Python, Guzzle/Symfony HTTP Client for PHP), potentially a test database setup.
*   **Focus:** Make HTTP requests to the running API (in a test environment). Assert HTTP status codes, response headers, and response body structure/content. Verify data changes in the test database.
*   **Example (Conceptual - Node.js/Supertest):**
    ```javascript
    // Assuming an Express app instance is exported from app.js
    import request from 'supertest';
    import app from '../app'; // Your Express app

    describe('GET /users/:id', () => {
      it('should return user data for valid ID', async () => {
        const userId = 'user123'; // Assume this user exists in test DB
        const response = await request(app).get(`/users/${userId}`);

        expect(response.status).toBe(200);
        expect(response.headers['content-type']).toMatch(/json/);
        expect(response.body).toHaveProperty('id', userId);
        expect(response.body).toHaveProperty('name');
      });

      it('should return 404 for non-existent ID', async () => {
        const response = await request(app).get('/users/nonexistent999');
        expect(response.status).toBe(404);
        expect(response.body).toHaveProperty('error', 'User Not Found');
      });

      // Add tests for invalid ID format (e.g., 400 Bad Request)
    });
    ```

## Contract Testing

*   **Goal:** Ensure the API implementation matches its specification (OpenAPI/GraphQL Schema).
*   **Tools:** Schema validation libraries, specialized contract testing tools (Pact, PactumJS). Can sometimes be integrated into integration tests.
*   **Focus:**
    *   **Request Validation:** Does the API correctly reject requests that don't match the schema?
    *   **Response Validation:** Does the API's response match the schema defined for that endpoint/status code?
*   **Example (Conceptual - using an OpenAPI validator middleware in integration tests):** Many frameworks or libraries allow validating requests/responses against an OpenAPI spec during integration tests.

## Best Practices

*   **Test Pyramid:** Focus heavily on unit tests (fast, isolated), have a good number of integration tests (verify component interactions), and fewer E2E tests (slower, more brittle).
*   **Isolate Tests:** Ensure tests can run independently and don't rely on the state left by previous tests (e.g., clean up test database between tests).
*   **Cover Edge Cases & Errors:** Test invalid input, boundary conditions, error responses (4xx, 5xx), and security constraints (AuthN/AuthZ).
*   **CI Integration:** Run tests automatically in your Continuous Integration pipeline.

API developers should prioritize writing thorough unit and integration tests to ensure the core functionality and component interactions of the API are correct. Coordinate with QA/testing specialists for more comprehensive E2E and contract testing strategies.

*(Refer to testing documentation for your specific backend language/framework and tools like Supertest, Pytest, Pact.)*