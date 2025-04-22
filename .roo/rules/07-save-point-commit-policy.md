+++
id = "RURU-RULE-SAVE-POINT-COMMIT-V1"
title = "Standard Save Point Commit Policy"
context_type = "rules"
scope = "Defines when AI modes should propose Git commits as save points"
target_audience = ["all"] # Primarily relevant for modes modifying code/config
granularity = "policy"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "git", "commit", "safety", "checkpoint", "save-point"]
related_context = ["00-user-preferences.md", "05-confirmation-policy.md", "dev-git"]
+++

# Standard Save Point Commit Policy

**Objective:** To encourage creating logical save points using Git commits before and after potentially substantial changes, enhancing safety and providing rollback capability.

**Applies To:** All modes making modifications to version-controlled files (code, configuration, documentation, etc.).

**Core Principles:**

1.  **Safety Net:** Commits act as backups before potentially complex or risky operations.
2.  **Logical Grouping:** Commits should ideally represent complete, logical units of work (e.g., a feature increment, a refactoring step, a bug fix).
3.  **User Control:** Offer the user the option to create save points, don't force it unless critical.

**Procedure (Proposing a Commit):**

1.  **Identify Need:** A mode determines that it is about to **start** OR has just **completed** a "substantial change" (see Definition below).
2.  **Check User Preference:** Consult `auto_execute_commands` in Rule `00`. If `false`, prompting is generally preferred anyway.
3.  **Formulate Proposal:** If a commit seems appropriate, use `<ask_followup_question>` to propose it to the user.
    *   **Proposal Content:** Clearly state *why* a commit is being suggested (e.g., "About to refactor multiple files", "Just completed implementing the user profile component").
    *   **Suggested Action:** Offer clear suggestions.
        *   *Before Change:* `<suggest>Yes, create a commit before starting</suggest>` `<suggest>No, proceed without committing now</suggest>`
        *   *After Change:* `<suggest>Yes, commit these changes</suggest>` `<suggest>No, I'll commit manually later</suggest>`
    *   **(Optional) Suggest Commit Message:** Propose a conventional commit message (e.g., `feat: Implement user profile component`, `refactor: Extract validation logic`). `<suggest>Use suggested message: '...'</suggest>` `<suggest>Let me provide a custom message</suggest>`
4.  **Await User Response:** Wait for the user's decision.
5.  **Execute Commit (If Approved):**
    *   **If** the user approves the commit:
        1.  Determine the necessary Git commands (`git add .` followed by `git commit -m "..."`).
        2.  **Delegate to `dev-git`:** Use `<new_task>` to delegate the commit sequence to the `dev-git` mode, providing the exact commands and commit message (either suggested or user-provided). Ensure `dev-git` reports success/failure.
        3.  Log the delegation and outcome (Rule `12`).
    *   **If** the user declines: Proceed with the next planned action (either starting the substantial change or moving on after completing it). Log the user's decision.

**Definition of "Substantial Change" (Heuristics for AI):**

A commit should be *considered* (and potentially proposed to the user) before/after:

*   Completing an MDTM task/checklist item involving non-trivial code changes.
*   Modifying multiple files as part of a single logical change.
*   Implementing a distinct feature or fixing a named bug.
*   Significant refactoring efforts.
*   Before executing commands flagged as high-risk by Rule `05` (if not already committed).
*   When switching focus between different features or large tasks.

**Note:** Modes should use judgment. Do not propose commits for every minor file save or trivial change. Focus on logical breakpoints in the development process.

**Rationale:** Promotes safer development practices by creating restore points, encourages logical grouping of changes, and keeps the user informed and in control of the commit history. Delegation to `dev-git` ensures consistency and safety in Git operations.