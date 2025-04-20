# Mode Review: accessibility-specialist

**Mode File:** `roo-modes-dev/accessibility-specialist.json`

## Analysis Summary

This mode audits web applications for WCAG compliance and optionally implements fixes. It follows a logical workflow: receive task, audit (manual/automated), fix code (if tasked), verify fixes, document findings, and report completion.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain two references to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file:
    *   Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
    *   Step 5: "...use standard emojis (see `ROO_COMMANDER_SYSTEM.md`)."
2.  **MDTM Alignment:** The mode adheres well to the MDTM principles, including Task ID handling, logging to the specific task file, and using `attempt_completion`.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` References:** Modify the `customInstructions` to remove the two identified references to `ROO_COMMANDER_SYSTEM.md`. The instruction to use standard emojis in Step 5 can remain as a general guideline without the specific file reference.

## Other Notes/Ideas

*   Consider clarifying *how* findings should be structured in logs/reports for better readability (e.g., grouped by WCAG criteria). (Minor enhancement)
*   Future integration with advanced browser automation tools via MCP could enhance auditing capabilities. (Future enhancement)

## Proposed Changes (JSON `customInstructions`)

*   **Search 1:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace 1:** (Empty string)
*   **Search 2:** `(see \\\`ROO_COMMANDER_SYSTEM\\.md\\\`)`
*   **Replace 2:** (Empty string)