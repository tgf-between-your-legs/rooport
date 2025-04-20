# 4. Key Considerations / Safety Protocols

*   **Test Isolation:** Ensure integration tests are properly isolated from production environments. Never run tests against production databases or services without explicit authorization.
*   **Test Data Management:** Be cautious with test data generation and cleanup. Ensure proper teardown of test resources to prevent orphaned data or resource leaks.
*   **API Rate Limits:** Be aware of rate limits when testing external APIs. Implement appropriate delays or throttling in test suites to avoid triggering rate limit blocks.
*   **Authentication Credentials:** Handle test credentials securely. Never commit real credentials to source control; use environment variables or secure credential stores.
*   **Mock External Dependencies:** When testing integrations with external services, prefer mocks/stubs over real connections unless specifically testing the actual integration.
*   **Avoid Test Flakiness:** Design tests to be deterministic and reliable. Identify and address sources of flakiness (timing issues, resource contention, external dependencies).