# Mode Review: database-specialist

**Mode File:** `roo-modes-dev/database-specialist.json`

## Analysis Summary

This mode handles database schema design, implementation (SQL DDL, ORM models, Prisma), migration script generation, query optimization, and diagram generation/updates.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain one reference to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file in Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
2.  **MDTM Alignment:** Excellent alignment. The mode correctly handles Task IDs, initializes and updates the specific task log file throughout its workflow, saves formal docs appropriately, handles diagram updates, and uses `attempt_completion` correctly.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` Reference:** Modify Step 1 in `customInstructions` to remove the sentence "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."

## Other Notes/Ideas

*   The mode correctly includes generating Mermaid syntax and then handling the diagram update (preferably via delegation to `diagramer`).
*   The mode is well-structured for database-related tasks.

## Proposed Changes (JSON `customInstructions`)

*   **Search:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace:** (Empty string)