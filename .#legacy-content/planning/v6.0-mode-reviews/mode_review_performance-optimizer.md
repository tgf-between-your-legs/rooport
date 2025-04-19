# Mode Review: performance-optimizer

**Mode File:** `roo-modes-dev/performance-optimizer.json`

## Analysis Summary

This mode focuses on identifying, analyzing, and resolving performance bottlenecks across the application stack (frontend, backend, database, infrastructure). It uses profiling tools, implements optimizations, and verifies the impact.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain one reference to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file in Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
2.  **MDTM Alignment:** Excellent alignment. The mode correctly handles Task IDs, initializes and updates the specific task log file throughout its detailed workflow, saves formal reports appropriately, and uses `attempt_completion` correctly.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` Reference:** Modify Step 1 in `customInstructions` to remove the sentence "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."

## Other Notes/Ideas

*   The mode correctly identifies the need for various profiling and testing tools via `execute_command` and `browser`.
*   The mention of coordinating with other specialists (database, infrastructure) is good practice.
*   The inclusion of recommending monitoring metrics is valuable.

## Proposed Changes (JSON `customInstructions`)

*   **Search:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace:** (Empty string)