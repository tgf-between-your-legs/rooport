+++
id = "ADR-001"
title = "Mode Source Reorganisation and Dynamic KB Loading"
status = "proposed"
decision_date = "2025-04-18"
authors = ["Roo Commander"]
template_schema_doc = ".templates/toml-md/07_adr.README.md" # Link to schema documentation
# affected_components = ["mode-definitions", "mode-loading-system", "ai-context-pipeline"] # Example, refine later
tags = ["modes", "architecture", "refactoring", "knowledge-base", "context-management"]
# supersedes_adr = ""
+++

# ADR-001: Mode Source Reorganisation and Dynamic KB Loading

**Status:** proposed

**Date:** 2025-04-18

## Context 🤔

*   **Problem:** The current structure and custom instruction context for modes (e.g., within `vX.Y/modes/.../custom-instructions/`) are becoming large, monolithic, and potentially inefficient. Updating modes requires significant context changes. The nested directory structure can be complex. Naming conventions are verbose and sometimes inconsistent (e.g., use of "Specialist", "Developer"). Emoji usage is not unique.
*   **Goal:** Improve mode maintainability, reduce context size, enhance context relevance through dynamic loading, simplify the directory structure, and establish clearer naming conventions.
*   **Constraints:** Changes must be compatible with the overall Roo Commander system and minimize disruption during transition. The solution should be scalable and potentially adaptable to future database storage.
*   **Source Documents:**
    *   `.docs/notes/changing-the-organising-of-mode-sources.md`
    *   `.docs/notes/changing-the-organising-of-mode-sources-qna.md`

## Decision ✅ / ❌

1.  **Adopt a flat directory structure:** All mode source files will reside under a single root `.mode/` directory (e.g., `.mode/<mode-slug>/`).
2.  **Implement a manifest file:** Create `.mode/manifest.toml` to store mode metadata, including version, description, relationships (delegation targets), grouping/categorization tags, and potentially links to external resources.
3.  **Rename `custom-instructions` to `kb`:** Use `.mode/<mode-slug>/kb/` for knowledge base articles. Retain `context/` and `examples/` subdirectories for potential future use.
4.  **Implement dynamic KB loading:** Modes will dynamically load relevant articles from their `kb/` directory based on the assigned task. The mechanism will involve prompt-based self-assessment by the mode, allowing flexibility rather than rigid rules. Modes should still function without KB input.
5.  **Adopt a new naming convention:** Use a `role-topic` or `area-specialty` format (e.g., `core-code`, `manager-projects`, `lead-backend`, `dev-angular`, `design-ui`). Define a standard set of prefixes.
6.  **Standardize unique emojis:** Assign a unique emoji to each mode where feasible, starting with core roles.
7.  **(Optional) Create default mode folders:** Allow for `.modes/code/`, `.modes/ask/`, etc., to potentially hold KB/context for core modes.
8.  **(Decision) Remove 'Footgun' modes:** These modes will be removed to simplify the mode list.

## Rationale / Justification 💡

*   **Simplicity & Maintainability:** A flat structure and manifest simplify navigation and management compared to deep nesting. Renaming to `kb` is more intuitive.
*   **Efficiency & Cost:** Dynamic KB loading reduces the initial context size sent to the AI, potentially improving performance and lowering costs. It allows for more targeted and up-to-date information (e.g., new API details not in training data).
*   **Clarity:** The new naming convention is more concise and clearly indicates the mode's role and domain. Standard prefixes aid discoverability.
*   **Scalability:** The manifest file provides a structured way to manage metadata and relationships, paving the way for potential future database integration.
*   **Flexibility:** The prompt-based KB loading allows modes autonomy in selecting relevant context.

## Consequences / Implications ➡️

*   **Refactoring Effort:** Significant effort required to rename mode directories, update mode definition files (JSON/YAML), update references in workflows, documentation, and potentially user configurations.
*   **Tooling Updates:** Any scripts or tools relying on the old structure/naming will need modification.
*   **KB Loading Mechanism:** Requires careful design and implementation of the prompt strategy and potentially supporting system logic to ensure modes reliably load relevant context.
*   **Manifest Management:** The `.modes/manifest.toml` file becomes a critical piece of infrastructure requiring careful maintenance.
*   **Transition Plan:** A phased rollout (pilot project) is recommended to mitigate risks. Clear mapping from old to new names is needed.
*   **New Work:**
    *   Define standard naming prefixes.
    *   Design and implement the `manifest.toml` structure and content.
    *   Develop and test the prompt-based KB loading mechanism.
    *   Perform the refactoring of mode directories and definitions.
    *   Update documentation and workflows.
    *   Assign unique emojis.

## Alternatives Considered (Optional Detail) 📝

*   **Retain Versioned Structure:** Keep `vX.Y/modes/` but implement KB loading and new naming within it. (Rejected: Doesn't fully address structural complexity).
*   **Rule-Based KB Loading:** Use strict rules or indexing instead of prompt-based assessment. (Rejected: Less flexible, harder to adapt to diverse tasks).
*   **Hierarchical Structure under `.modes/`:** Group modes by type (e.g., `.modes/backend/django-dev/`). (Considered: Adds some structure back, but manifest tags might suffice).

## Related Links 🔗 (Optional)

*   `.docs/notes/changing-the-organising-of-mode-sources.md`
*   `.docs/notes/changing-the-organising-of-mode-sources-qna.md`
*   `.templates/toml-md/07_adr.md`