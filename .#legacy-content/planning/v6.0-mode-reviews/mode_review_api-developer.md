# Mode Review: api-developer

**Mode File:** `roo-modes-dev/api-developer.json`

## Analysis Summary

This mode handles the design, implementation, testing, optimization, and documentation of APIs. It follows a standard development lifecycle and includes considerations for testing, documentation (OpenAPI), and potential coordination with other specialists like the database specialist.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain one reference to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file in Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
2.  **MDTM Alignment:** The mode adheres well to the MDTM principles, including Task ID handling, logging significant steps and completion to the specific task file, and using `attempt_completion`.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` Reference:** Modify Step 1 in `customInstructions` to remove the sentence "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."

## Other Notes/Ideas

*   The mode is quite generic regarding language/framework. While this provides flexibility, specific framework modes (like `fastapi-developer`, `php-laravel-developer`) might be preferred for more targeted tasks. This mode could serve as a good fallback or for less common frameworks.

## Proposed Changes (JSON `customInstructions`)

*   **Search:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace:** (Empty string)