# Mode Review: material-ui-specialist

**Mode File:** `roo-modes-dev/material-ui-specialist.json`

## Analysis Summary

This mode specializes in implementing React UIs using the Material UI (MUI) component library, including component usage, theming, and styling (`sx`, `styled`).

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain one reference to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file in Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
2.  **MDTM Alignment:** Excellent alignment. The mode correctly handles Task IDs, initializes and updates the specific task log file throughout its workflow, and uses `attempt_completion` correctly.
3.  **Embedded Context:** The mode definition includes a large embedded "Condensed Context Index" for MUI.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` Reference:** Modify Step 1 in `customInstructions` to remove the sentence "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."

## Other Notes/Ideas

*   Consider refactoring the embedded context index into a separate file within `project_journal/context/` and having the mode read it if needed, to reduce the size of the mode definition JSON. (Future enhancement)

## Proposed Changes (JSON `customInstructions`)

*   **Search:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace:** (Empty string)