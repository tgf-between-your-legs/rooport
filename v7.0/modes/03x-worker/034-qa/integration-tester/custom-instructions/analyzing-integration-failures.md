# Integration Testing: Analyzing Failures

Debugging common issues encountered during integration testing.

## Core Concept: Pinpointing Interaction Problems

Failures in integration tests indicate a problem in how two or more components interact. Unlike unit test failures (which usually point to a bug within a single unit) or E2E failures (which could be anywhere in the stack), integration test failures specifically highlight issues at the boundaries between components.

## Common Causes of Integration Failures

1.  **Contract Mismatches (API Tests):**
    *   **Symptom:** Unexpected status codes (e.g., 400 Bad Request, 500 Internal Server Error), response body doesn't match expected schema, required fields missing, data types incorrect.
    *   **Cause:** Consumer sends a request the provider doesn't understand, or the provider returns a response the consumer can't handle. The API contract has changed on one side but not the other.
    *   **Debugging:** Compare the actual request/response (from test logs or tools like Postman) against the API specification (OpenAPI/Swagger) or the contract file (Pact). Check serialization/deserialization logic on both consumer and provider. Verify API documentation.
2.  **Incorrect Data Flow:**
    *   **Symptom:** Data created/updated via one component's API isn't reflected correctly when queried via another component's API or directly in the database. Incorrect side effects occur (or don't occur).
    *   **Cause:** Logic errors in how data is processed and passed between components, issues with database persistence, problems with message queue handling, race conditions.
    *   **Debugging:** Trace the data flow step-by-step. Check logs on all involved services. Inspect database state before and after the interaction. Verify message queue contents.
3.  **Environment/Configuration Issues:**
    *   **Symptom:** Connection errors, timeouts, authentication failures (401/403), service unavailability (503), configuration-related errors in logs. Tests fail consistently or intermittently depending on environment state.
    *   **Cause:** Incorrect service URLs, wrong credentials, network connectivity problems between services, database connection issues, missing environment variables, resource exhaustion in the test environment.
    *   **Debugging:** Verify environment configuration (URLs, ports, credentials). Check network connectivity between test runner and services, and between services themselves (e.g., using `ping`, `curl` within containers). Check service logs for startup or configuration errors. Monitor resource usage. Collaborate with `infrastructure-specialist`/`devops-lead`.
4.  **Test Double Misconfiguration (Mocks/Stubs):**
    *   **Symptom:** Tests fail because the mock/stub isn't returning the expected value, or mock verification fails (`assert_called_once_with` fails).
    *   **Cause:** Mock/stub not set up correctly, incorrect return value specified, expected call signature in mock doesn't match actual call, mock patching applied at the wrong scope.
    *   **Debugging:** Double-check mock setup logic. Print arguments received by the mock. Ensure the mock is patching the correct object/function in the correct location.
5.  **Test Data Problems:**
    *   **Symptom:** Tests fail because prerequisite data doesn't exist or is in an unexpected state. `404 Not Found` errors when expecting data. Unique constraint violations.
    *   **Cause:** Flaws in test data setup or teardown logic. Interference from other tests modifying shared data.
    *   **Debugging:** Verify data setup steps are running correctly before the test. Check database state manually. Ensure unique data is used where necessary. Review teardown logic. (See `integration-test-data-strategies.md`).
6.  **Asynchronous Timing Issues:**
    *   **Symptom:** Intermittent failures where assertions run before an asynchronous operation between components (e.g., message queue processing, background job) has completed.
    *   **Debugging:** Implement appropriate waiting strategies. This might involve polling an API status endpoint, checking the database for an expected state change, or using framework-specific waits if testing within a single service boundary. Avoid fixed `sleep()` calls.

## Debugging Workflow

1.  **Reproduce:** Can the failure be reproduced consistently?
2.  **Isolate:** Run the failing test in isolation.
3.  **Examine Logs:** Check logs from the test runner *and* all involved services/components for errors or relevant messages during the test execution timeframe.
4.  **Inspect Network:** If testing APIs, examine the exact HTTP requests and responses (headers, body, status code). Tools like Postman, `curl`, or browser dev tools (if applicable) can help.
5.  **Check Database/State:** Inspect the state of databases, message queues, or other relevant infrastructure before and after the interaction.
6.  **Simplify:** Temporarily simplify the test or the interaction to pinpoint the failing part. Remove mocks one by one if used.
7.  **Add Debugging:** Add logging or use debuggers within the service code or test code.

Analyzing integration failures often requires looking beyond a single component and understanding the communication flow and contracts between them. Check configurations, data, network communication, and logs across the involved systems.