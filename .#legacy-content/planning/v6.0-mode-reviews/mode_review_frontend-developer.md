# Mode Review: frontend-developer

**Mode File:** `roo-modes-dev/frontend-developer.json`

## Analysis Summary

This mode handles general frontend development tasks, including implementing UIs, integrating APIs, testing, and optimizing, potentially using various frameworks or libraries.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain one reference to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file in Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
2.  **MDTM Alignment:** Excellent alignment. The mode correctly handles Task IDs, initializes and updates the specific task log file throughout its workflow, and uses `attempt_completion` correctly.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` Reference:** Modify Step 1 in `customInstructions` to remove the sentence "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."

## Other Notes/Ideas

*   This mode is quite generic. For projects using specific, well-supported frameworks (React, Vue, Angular, Svelte, etc.), delegating to the corresponding specialist mode (e.g., `react-specialist`) might yield better results due to more tailored instructions and context. This mode remains useful as a fallback or for simpler HTML/CSS/JS tasks.

## Proposed Changes (JSON `customInstructions`)

*   **Search:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace:** (Empty string)