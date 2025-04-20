# Mode Review: infrastructure-specialist

**Mode File:** `roo-modes-dev/infrastructure-specialist.json`

## Analysis Summary

This mode handles infrastructure design, implementation via Infrastructure as Code (IaC), configuration (networking, security, monitoring, cost, DR), and troubleshooting.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain one reference to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file in Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
2.  **MDTM Alignment:** Excellent alignment. The mode correctly handles Task IDs, initializes and updates the specific task log file throughout its detailed workflow, saves formal docs appropriately, and uses `attempt_completion` correctly.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` Reference:** Modify Step 1 in `customInstructions` to remove the sentence "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."

## Other Notes/Ideas

*   The mode is comprehensive, covering many facets of infrastructure management.
*   It correctly identifies the use of various IaC and cloud CLI tools via `execute_command`.
*   The mention of coordinating with `diagramer` is good practice.

## Proposed Changes (JSON `customInstructions`)

*   **Search:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace:** (Empty string)