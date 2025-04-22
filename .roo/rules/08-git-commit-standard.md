+++
id = "RURU-RULE-GIT-COMMIT-STD-V1"
title = "Standard: Git Commit Message Format"
context_type = "rules"
scope = "Formatting standard for all Git commit messages"
target_audience = ["all", "dev-git"] # All modes that might *generate* commit messages, especially dev-git
granularity = "standard"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "git", "commit", "standard", "conventional-commits", "traceability", "mdtm"]
related_context = [".docs/standards/mdtm_standard.md"] # Reference MDTM standard
+++

# Standard: Git Commit Message Format

**Objective:** To ensure all Git commits are informative, consistent, and traceable back to specific tasks.

**Rule:**

1.  **Conventional Commits:** All commit messages **MUST** adhere to the Conventional Commits specification (<https://www.conventionalcommits.org/>). The basic format is:
    ```
    type(scope): subject

    [optional body]

    [optional footer(s)]
    ```
    *   `type`: Must be one of the standard types (e.g., `feat`, `fix`, `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`).
    *   `scope` (Optional): The part of the codebase affected (e.g., `api`, `ui`, `auth`).
    *   `subject`: Concise description of the change in present tense (e.g., "Add login endpoint"). Max 50-72 chars recommended.

2.  **MDTM Task Reference (Mandatory Footer):**
    *   Every commit **MUST** include a footer referencing the relevant MDTM Task ID(s).
    *   Use the format: `Refs: TASK-TYPE-ID` or `Closes: TASK-TYPE-ID` (if the commit fully resolves the task). Multiple tasks can be listed.
    *   **Example Footer:**
        ```
        Refs: TASK-FEAT-123
        Closes: TASK-BUG-456
        ```

3.  **Optional Body:**
    *   Use the commit body to provide more context: motivation for the change, implementation details, breaking changes (`BREAKING CHANGE:`). This is **highly encouraged** for non-trivial changes to enhance the Git history as a knowledge source.

**Responsibility:**

*   Modes performing commits directly (rare) must follow this format.
*   Modes delegating commits to `dev-git` **MUST** provide the necessary information (type, scope, subject, task IDs, optional body details) so `dev-git` can construct the correct message.
*   `dev-git` **MUST** format commit messages according to this standard using the provided information.

**Rationale:** Enforces consistency, improves changelog generation, and critically enables tracing code changes back to specific tasks documented in the MDTM system.