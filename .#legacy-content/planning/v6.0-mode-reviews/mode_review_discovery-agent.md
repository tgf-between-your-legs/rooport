# Mode Review: discovery-agent

**Mode File:** `roo-modes-dev/discovery-agent.json`

## Analysis Summary

This mode interacts with the user to gather and document detailed project or feature requirements, including functional, non-functional, and design aspects. It saves the final requirements to the project journal.

## Findings & Concerns

1.  **Obsolete File Reference:** The `customInstructions` contain one reference to the now-obsolete `ROO_COMMANDER_SYSTEM.md` file in Step 1: "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."
2.  **MDTM Alignment:** Excellent alignment. The mode correctly handles Task IDs, initializes and updates the specific task log file, saves its formal output correctly, and uses `attempt_completion` appropriately, referencing relevant artifacts.

## Recommendations for Change

1.  **Remove `ROO_COMMANDER_SYSTEM.md` Reference:** Modify Step 1 in `customInstructions` to remove the sentence "Adhere to guidelines in `ROO_COMMANDER_SYSTEM.md`."

## Other Notes/Ideas

*   The mode includes specific prompts for gathering design/aesthetic requirements, which addresses earlier feedback.
*   The iterative questioning approach using `ask_followup_question` is suitable for this role.

## Proposed Changes (JSON `customInstructions`)

*   **Search:** `Adhere to guidelines in \\\`ROO_COMMANDER_SYSTEM\\.md\\\`. ` (Note the trailing space)
*   **Replace:** (Empty string)