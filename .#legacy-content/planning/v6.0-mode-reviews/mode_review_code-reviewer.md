# Mode Review: code-reviewer

**Mode File:** `roo-modes-dev/code-reviewer.json`

## Analysis Summary

This mode reviews code changes for quality, standards, bugs, security, and maintainability, providing structured feedback. It saves the detailed review as a formal document.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain two references to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file:
    *   Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
    *   Step 3: "...use standard emojis (see `ROO_COMMANDER_SYSTEM.md`)."
2.  **MDTM Alignment:** Excellent alignment. The mode correctly handles Task IDs, initializes and updates the specific task log file, saves its formal output correctly, and uses `attempt_completion` appropriately, referencing relevant artifacts.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` References:** Modify the `customInstructions` to remove the two identified references to `ROO_COMMANDER_SYSTEM.md`. The instruction to use standard emojis in Step 3 can remain as a general guideline without the specific file reference.

## Other Notes/Ideas

*   The mode is well-defined for its purpose.

## Proposed Changes (JSON `customInstructions`)

*   **Search 1:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace 1:** (Empty string)
*   **Search 2:** `(see \\\`ROO_COMMANDER_SYSTEM\\.md\\\`)`
*   **Replace 2:** (Empty string)