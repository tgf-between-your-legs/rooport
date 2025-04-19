# Integration Testing: API Interactions

Techniques and tools for testing the integration between services via their APIs (REST, GraphQL).

## Core Concept: Verifying API Contracts and Communication

API integration testing focuses on verifying that services can communicate correctly by making requests to one service's API and asserting on the response received, or checking the resulting state change in another service or database. It ensures that the "contract" (expected request/response format, status codes, behavior) between services is met.

**Scope:**

*   Testing calls *between* your own internal microservices.
*   Testing calls from your service to essential third-party APIs (though these might be mocked/stubbed more often).
*   Testing calls from a frontend application's backend-for-frontend (BFF) to downstream services.
*   Testing how a service interacts with a database after receiving an API call.

## Common Tools & Techniques

1.  **HTTP Client Libraries within Test Frameworks:**
    *   **How:** Use standard HTTP client libraries within your preferred testing framework (`pytest`, `jest`, `unittest`, etc.) to make requests to the running service's API endpoint.
    *   **Tools:**
        *   Python: `requests` (synchronous), `httpx` (sync/async). Often used with `pytest`.
        *   JavaScript/Node.js: `axios`, `node-fetch`, `supertest`. Often used with `jest` or `mocha`.
    *   **Pros:** Flexible, allows complex test logic in familiar programming languages, integrates well with existing unit/integration test suites.
    *   **Cons:** Requires writing boilerplate code for requests and assertions. Need to manage the running state of the service(s) under test.
    *   **Example (`pytest` with `httpx`):**
        ```python
        # tests/integration/test_user_api.py
        import pytest
        import httpx

        # Assume service is running at BASE_URL (e.g., via docker-compose)
        BASE_URL = "http://localhost:8001/api/v1"

        @pytest.mark.asyncio # For async tests with httpx
        async def test_create_user_success():
            async with httpx.AsyncClient() as client:
                user_data = {"username": "test_integ", "email": "integ@test.com", "password": "password123"}
                response = await client.post(f"{BASE_URL}/users/", json=user_data)

                assert response.status_code == 201 # Check status code
                response_data = response.json()
                assert response_data["username"] == user_data["username"]
                assert response_data["email"] == user_data["email"]
                assert "id" in response_data # Check if ID was generated
                # Optionally: Verify user exists in DB via another API call or direct check

        @pytest.mark.asyncio
        async def test_get_user_not_found():
             async with httpx.AsyncClient() as client:
                response = await client.get(f"{BASE_URL}/users/nonexistent_user_id")
                assert response.status_code == 404
        ```

2.  **API Testing Tools (Postman/Newman):**
    *   **How:** Use tools like Postman to manually define and run API requests and assertions. Collections can be exported and run automatically from the command line using Newman.
    *   **Pros:** User-friendly interface for creating requests. Good for exploratory testing. Newman allows CI integration. Built-in assertion capabilities.
    *   **Cons:** Test logic can become complex within the tool's scripting environment. Managing test data and dependencies between requests can be cumbersome. Less flexible for complex setup/teardown logic compared to code-based tests.
    *   **Example (Newman CLI):**
        ```bash
        newman run my_api_collection.json -e production.postman_environment.json --reporters cli,html
        ```

3.  **Framework-Specific Test Clients:**
    *   **How:** Many web frameworks provide test clients that allow making requests to the application *without* needing a running HTTP server (often by directly calling the application's request handling logic).
    *   **Tools:** Django `TestClient`, FastAPI `TestClient`, Flask `test_client()`.
    *   **Pros:** Faster execution as no real HTTP server is involved. Easier setup. Good for testing interactions *within* a single service or between tightly coupled components.
    *   **Cons:** Doesn't test the full network stack (load balancers, web servers). Less suitable for testing interactions *between* separate microservices deployed independently.

## Key Assertions in API Integration Tests

*   **Status Code:** Verify the correct HTTP status code is returned (e.g., 200, 201, 400, 404, 500).
*   **Response Body:**
    *   Check if the body matches the expected schema (presence/absence of fields, data types).
    *   Verify specific values within the response body.
    *   For lists, check the length or specific items.
*   **Response Headers:** Verify important headers like `Content-Type`, `Location` (for redirects), caching headers.
*   **Side Effects:** Check the expected state change in the database or other downstream systems (e.g., was a record created/updated? Was a message published?). This might involve making additional API calls or querying the database directly (use with caution).
*   **Performance (Basic):** Assert that the response time is within an acceptable threshold (though dedicated performance tests are better for this).

## Considerations

*   **Environment:** Run integration tests against a dedicated, stable test environment that mirrors production as closely as possible.
*   **Dependencies:** Decide whether to test against live dependencies (other services, databases) or use test doubles (mocks/stubs). Testing against live dependencies provides higher confidence but can be slower and more complex to set up and manage. Mocks provide isolation but don't verify the real integration. A mix is often used.
*   **Authentication:** Ensure tests handle authentication correctly, obtaining and using necessary tokens or credentials.
*   **Data Setup/Teardown:** Implement reliable mechanisms to set up required data before tests and clean up afterwards.

API integration testing is crucial for verifying that different parts of your distributed system or application components communicate correctly. Choose the right tools and techniques based on the specific interaction points and testing goals.