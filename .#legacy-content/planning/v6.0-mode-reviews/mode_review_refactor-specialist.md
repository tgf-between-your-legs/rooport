# Mode Review: refactor-specialist

**Mode File:** `roo-modes-dev/refactor-specialist.json`

## Analysis Summary

This mode focuses on improving existing code structure and quality without changing external behavior. It emphasizes identifying code smells, applying refactoring patterns, and verifying changes using existing tests.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain one reference to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file in Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
2.  **MDTM Alignment:** Excellent alignment. The mode correctly handles Task IDs, initializes and updates the specific task log file throughout its workflow, and uses `attempt_completion` correctly with different outcome types.
3.  **Safety Emphasis:** The instructions correctly and strongly emphasize the importance of verifying changes with existing tests after each small step and halting if tests fail or are missing.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` Reference:** Modify Step 1 in `customInstructions` to remove the sentence "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."

## Other Notes/Ideas

*   This mode's focus on safety through iterative testing is excellent.
*   The handling of missing tests as a blocker is appropriate.

## Proposed Changes (JSON `customInstructions`)

*   **Search:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace:** (Empty string)