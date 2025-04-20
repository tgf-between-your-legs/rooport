# Mode Review: security-specialist

**Mode File:** `roo-modes-dev/security-specialist.json`

## Analysis Summary

This mode focuses on security assessment, vulnerability scanning, implementing fixes/controls, and potentially incident response. It uses scanning tools and manual review techniques.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain one reference to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file in Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
2.  **MDTM Alignment:** Excellent alignment. The mode correctly handles Task IDs, initializes and updates the specific task log file throughout its detailed workflow, saves formal reports appropriately, and uses `attempt_completion` correctly.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` Reference:** Modify Step 1 in `customInstructions` to remove the sentence "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."

## Other Notes/Ideas

*   The mode covers a good range of security activities, from scanning to fixing and reporting.
*   The inclusion of incident response steps adds value, though it might be a complex task for the mode to handle fully without significant context or more specialized sub-modes.
*   Coordination with infrastructure specialist is correctly noted.

## Proposed Changes (JSON `customInstructions`)

*   **Search:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace:** (Empty string)