# Integration Testing: Overview

Understanding the purpose, scope, and goals of integration testing.

## Core Concept: Testing Interactions Between Units

Integration testing focuses on verifying the communication and data flow **between** different software components, services, or systems after they have been integrated. Unlike unit tests, which test individual functions or classes in isolation, integration tests check if these units work together as expected.

**Key Goals:**

*   **Verify Interfaces:** Ensure that components correctly call each other's APIs or interfaces according to defined contracts.
*   **Validate Data Flow:** Check that data passed between components is correctly formatted, transmitted, and interpreted.
*   **Detect Interaction Bugs:** Find defects that only arise when components interact (e.g., mismatched data formats, incorrect handling of responses, race conditions between services).
*   **Confirm Contract Adherence:** Ensure components adhere to the agreed-upon contracts (API specifications, data schemas).

## Scope: What Integration Tests Cover (and Don't Cover)

*   **In Scope:**
    *   Interactions between different modules/classes within the *same* application (sometimes called component integration testing).
    *   Interactions between different microservices or backend services via APIs (REST, gRPC, message queues).
    *   Interactions between an application and external services (e.g., payment gateways, email services, third-party APIs) - often using test doubles.
    *   Interactions between an application layer and the database (verifying data persistence and retrieval).
    *   Interactions between frontend components and backend APIs (often tested via API calls, not full UI automation).
*   **Out of Scope:**
    *   **Unit Testing:** Testing individual functions/classes/modules in isolation (often mocking their dependencies). Focus is on internal logic.
    *   **End-to-End (E2E) Testing:** Testing complete user workflows through the entire application stack, usually via the UI. Focus is on the user journey.
    *   **Performance Testing:** Measuring response times, throughput, and resource usage under load.
    *   **UI/Visual Testing:** Verifying the visual appearance of the user interface.

## Why Integration Testing?

*   **Finds bugs early:** Catches issues at integration points before they reach E2E testing or production.
*   **Increases confidence:** Provides confidence that major components of the system can communicate correctly.
*   **Faster than E2E:** Generally faster and less flaky than full E2E tests because they often bypass the UI layer.
*   **Validates architecture:** Helps verify that the designed interactions between components work in practice.

## Common Approaches & Techniques

*   **API Testing:** Directly calling API endpoints of one service and verifying the response, or checking the side effects on another service or database. Tools: Postman/Newman, `requests`/`httpx` (Python), `fetch`/`axios` (JS), framework test clients.
*   **Database Integration Testing:** Verifying that data saved through one component/service can be correctly retrieved or processed by another, or checking database state after an interaction.
*   **Using Test Doubles (Mocks, Stubs, Fakes):** Replacing real dependencies (especially external services or complex internal components) with controlled substitutes to isolate the interaction being tested.
*   **Contract Testing:** Defining and verifying contracts (expected requests/responses) between services (e.g., using Pact). Ensures consumers and providers adhere to agreed-upon interfaces without needing fully integrated environments.
*   **Message Queue Testing:** Verifying that messages are correctly published to and consumed from message queues (like RabbitMQ, Kafka) between services.

Integration testing is a critical layer in the testing pyramid, bridging the gap between unit tests and E2E tests by focusing specifically on the interactions between different parts of the system.