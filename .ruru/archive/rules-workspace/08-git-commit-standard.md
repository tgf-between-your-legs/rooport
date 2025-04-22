+++
id = "RURU-RULE-GIT-COMMIT-STD-V2" # Incremented Version
title = "Standard: Git Commit Message Format (Context-Aware)"
context_type = "rules"
scope = "Formatting standard for all Git commit messages"
target_audience = ["all", "dev-git"]
granularity = "standard"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "git", "commit", "standard", "conventional-commits", "traceability", "mdtm"]
related_context = [".ruru/docs/standards/mdtm_standard.md", "07-save-point-commit-policy.md"]
+++

# Standard: Git Commit Message Format (Context-Aware)

**Objective:** To ensure all Git commits are informative, consistent, and traceable back to specific tasks where applicable.

**Rule:**

1.  **Conventional Commits:** All commit messages **MUST** adhere to the Conventional Commits specification (<https://www.conventionalcommits.org/>). Format:
    ```
    type(scope): subject

    [optional body]

    [optional footer(s)]
    ```
    *   `type`: (Required) e.g., `feat`, `fix`, `build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`.
    *   `scope` (Optional): e.g., `api`, `ui`, `auth`.
    *   `subject` (Required): Concise description, present tense.

2.  **Commit Body (Encouraged):**
    *   Provide context: Motivation (Why?), Implementation Summary (How?).
    *   Separate subject from body with a blank line. Use further blank lines for paragraphs.
    *   Mention breaking changes explicitly: `BREAKING CHANGE: description`.

3.  **Commit Footer (Mandatory):**
    *   A footer section **MUST** be present.
    *   **Task Reference:**
        *   If the commit relates to specific MDTM task(s), use `Refs: TASK-TYPE-ID` or `Closes: TASK-TYPE-ID`. Multiple lines allowed.
        *   If the user confirms **no specific MDTM task applies** (as per Rule `07`), use the standard placeholder `Refs: General`. **DO NOT** omit the footer entirely.

**Responsibility:**

*   Modes initiating a commit (often Commander or Leads via Rule `07`) are responsible for *generating* a proposed message (including body) based on recent context and *confirming* the appropriate Task ID (or 'General') with the user.
*   The initiating mode **MUST** provide the final, formatted message string (including type, scope, subject, body, and footer with correct Task ID or 'General') to `dev-git` during delegation.
*   `dev-git` **MUST** use the *exact* commit message string provided by the delegator.

**Rationale:** Enforces consistency, improves changelog generation, enables traceability via Task IDs (when applicable), leverages AI context for better descriptions, and provides flexibility for non-task commits via the `Refs: General` convention.