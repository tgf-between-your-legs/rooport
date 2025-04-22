+++
id = "RURU-RULE-SAVE-POINT-COMMIT-V2" # Incremented Version
title = "Standard Save Point Commit Policy (Context-Aware)"
context_type = "rules"
scope = "Defines when and how AI modes should propose Git commits as save points"
target_audience = ["all"] # Primarily relevant for modes modifying code/config
granularity = "policy"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "git", "commit", "safety", "checkpoint", "save-point", "context-aware"]
related_context = ["00-user-preferences.md", "05-confirmation-policy.md", "08-git-commit-standard.md", "dev-git", "12-logging-procedures.md"]
+++

# Standard Save Point Commit Policy (Context-Aware)

**Objective:** To encourage creating logical save points using Git commits before/after substantial changes, leveraging AI context to propose meaningful messages, while providing user flexibility regarding MDTM Task ID linking.

**Applies To:** All modes making modifications to version-controlled files.

**Procedure (Proposing a Commit):**

1.  **Identify Need:** The mode determines it is about to **start** or has just **completed** a "substantial change" (see definition below).
2.  **Review Recent Context:** The mode internally reviews its recent actions, changes made, and the primary goal of the work performed since the last commit (or start of session).
3.  **Generate Proposed Message:** Based on the context review, the mode **MUST** generate a *proposed* commit message adhering to Conventional Commits (Rule `08`), including:
    *   A likely `type` (e.g., `feat`, `fix`, `refactor`, `chore`).
    *   A relevant `scope` (optional).
    *   A concise `subject` summarizing the change.
    *   **(Optional but encouraged for substantial changes):** A short `body` explaining the key changes or rationale.
4.  **Identify Potential Task ID:** Check if the recent work clearly maps to a specific MDTM Task ID available in the current context (e.g., the task the mode was assigned).
5.  **Prompt User for Confirmation:** Use `<ask_followup_question>` to present the proposal and request necessary information:
    *   **Display Proposed Message:** "Based on the recent changes (e.g., [brief summary like 'implemented login component']), I propose the following commit message:\n```\n[Generated Conventional Commit Message]\n```"
    *   **Ask about Message:** "Is this message accurate and acceptable?"
    *   **Ask about Task ID:** "Please provide the relevant MDTM Task ID(s) (e.g., `TASK-FEAT-123`) for the commit footer."
    *   **Provide Suggestions:**
        *   `<suggest>Yes, use proposed message and Task ID: [AUTO-SUGGESTED TASK ID if identified in Step 4]</suggest>` (Offer if confident)
        *   `<suggest>Yes, use proposed message and Task ID: [Placeholder: 'General' for no specific task]</suggest>`
        *   `<suggest>Yes, use proposed message and provide Task ID...</suggest>`
        *   `<suggest>Edit the proposed message...</suggest>`
        *   `<suggest>Provide a completely new message and Task ID...</suggest>`
        *   `<suggest>Cancel commit for now</suggest>`
6.  **Await User Response:** Wait for the user's decision and input (edited message, specific Task ID, confirmation of 'General', or cancellation).
7.  **Execute Commit (If Approved):**
    *   If the user approves the commit (providing any necessary message/ID edits):
        1.  Finalize the commit message string according to Rule `08`, including the Task ID footer (`Refs: TASK-ID` or `Refs: General`).
        2.  Delegate the commit sequence (`git add .` then `git commit -m "..."`) to `dev-git` via `<new_task>`.
        3.  Log the delegation and outcome (Rule `12`).
    *   If the user cancels: Log the cancellation (Rule `12`) and proceed with the next planned action.

**Definition of "Substantial Change" (Heuristics for AI):**

*   (Same as previous version: MDTM item completion, multi-file changes, feature/bug fix, major refactoring, before risky commands, switching focus).

**Rationale:** Leverages AI context to draft useful commit messages, reducing user effort. Still requires user confirmation for accuracy and provides flexibility for linking (or not linking) MDTM tasks, while ensuring delegation to the Git specialist.