# Mode Review: ui-designer

**Mode File:** `roo-modes-dev/ui-designer.json`

## Analysis Summary

This mode focuses on the UI design process, including understanding requirements, creating wireframes/mockups (conceptually), defining style guides, documenting designs, and iterating based on feedback.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain two references to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file:
    *   Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
    *   Step 4: "...Use standard emojis (see `ROO_COMMANDER_SYSTEM.md`)."
2.  **MDTM Alignment:** Excellent alignment. The mode correctly handles Task IDs, initializes and updates the specific task log file throughout its detailed workflow, saves formal documents correctly, logs decisions, and uses `attempt_completion` appropriately, referencing relevant artifacts.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` References:** Modify the `customInstructions` to remove the two identified references to `ROO_COMMANDER_SYSTEM.md`. The instruction to use standard emojis in Step 4 can remain as a general guideline without the specific file reference.

## Other Notes/Ideas

*   The workflow accurately reflects a standard UI design process, including research, conceptual design stages, documentation, and collaboration.
*   The distinction between logging design progress in the task log and saving final specs/guides to formal docs is well-defined.

## Proposed Changes (JSON `customInstructions`)

*   **Search 1:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace 1:** (Empty string)
*   **Search 2:** `(see \\\`ROO_COMMANDER_SYSTEM\\.md\\\`)`
*   **Replace 2:** (Empty string)