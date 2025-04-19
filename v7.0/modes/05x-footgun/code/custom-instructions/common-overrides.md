# Common Override Scenarios

This document lists scenarios where standard safeguards might be intentionally bypassed when using `footgun-code`. Instructions invoking these overrides should explicitly reference this document or the specific scenario.

## Scenarios

1.  **Rapid Prototyping - Deferred Error Handling:**
    *   **Description:** During early prototyping, comprehensive error handling might be temporarily deferred to speed up development.
    *   **Override:** Instructions might request code generation without full try/catch blocks or detailed error logging for non-critical paths.
    *   **Required Acknowledgment:** "Generate prototype function X, deferring full error handling per `common-overrides.md#Scenario1`."
    *   **Follow-up:** A subsequent task should be created to add proper error handling before merging.
2.  **Test-Specific Configuration/Data:**
    *   **Description:** Setting up specific test environments might require temporarily hardcoding test credentials, disabling certain checks, or inserting specific test data directly.
    *   **Override:** Instructions might request hardcoding test API keys, disabling authentication middleware for specific test routes, or running direct DB inserts for test fixtures.
    *   **Required Acknowledgment:** "Configure test environment for feature Y: Hardcode test user credentials per `common-overrides.md#Scenario2`, acknowledging this is for testing only."
    *   **Cleanup:** Ensure test-specific configurations do not leak into production code or builds.
3.  **One-Off Data Migration/Cleanup Scripts:**
    *   **Description:** Writing scripts for specific data migration or cleanup tasks might involve direct database access or file operations that bypass standard application logic.
    *   **Override:** Instructions might request generating SQL update scripts or file deletion commands based on specific criteria.
    *   **Required Acknowledgment:** "Generate data cleanup script Z, using direct DB access per `common-overrides.md#Scenario3`. Acknowledge risk and confirm script will be reviewed before execution."
    *   **Review:** Such scripts require careful review and testing before execution.

*(Add more specific, approved override scenarios relevant to the project's workflow. Each scenario should clearly define the context, the allowed override, the required acknowledgment, and any necessary follow-up or cleanup actions.)*