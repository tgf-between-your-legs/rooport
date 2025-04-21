+++
id = "CTX-RURU-SIMPLEREFACTOR-OVERVIEW"
title = "Roo Commander Path Refactor (Simplified): Overview & Rationale"
context_type = "conceptual"
scope = "High-level explanation of consolidating paths under a fixed .ruru/ directory"
target_audience = ["ai_dev_team", "roo-commander", "core-architect"]
granularity = "overview"
status = "proposal"
last_updated = "2025-04-21"
tags = ["refactoring", "paths", "ruru", "consolidation", "fixed-path"]
+++

# Roo Commander Path Refactor (Simplified): Overview & Rationale

## 1. Problem Statement

The current Roo Commander system utilizes several hidden directories (e.g., `.tasks/`, `.docs/`, `.modes/`, `.roo/`) directly in the workspace root. While functional, this can clutter the root directory, especially in complex projects. Furthermore, adapting the system for forks that might use slightly different naming conventions (e.g., `.kilocode` instead of `.roo`) requires manual path adjustments across many files.

## 2. Goal

The goal of this **simplified refactoring** is to consolidate all standard Roo Commander operational directories under a **single, fixed parent directory named `.ruru/`** at the workspace root. This aims to:

*   Clean up the workspace root directory.
*   Organize all Roo Commander artifacts logically together.
*   Provide a *basic* level of adaptability (changing `.ruru/.roo` to `.ruru/.kilocode` involves simpler find/replace than the fully configurable approach).

**Note:** This simplified approach *does not* aim to make the base directory (`.ruru/`) itself configurable via a central file or allow users to easily switch between root-level and nested structures.

## 3. Proposed Solution Summary

This refactoring involves:

1.  **Moving Directories:** Physically move existing standard hidden directories (`.tasks`, `.docs`, `.modes`, `.roo`, `.templates`, `.workflows`, `.processes`, `.decisions`, `.context`, `.logs`, `.planning`, `.reports`, `.archive`, `.snippets`) into the new `.ruru/` directory.
2.  **Updating Paths (Find/Replace):** Perform careful, global search-and-replace operations across all relevant source files (`.md`, `.js`) to prepend `.ruru/` to existing relative path references (e.g., change `".tasks/"` to `".ruru/.tasks/"`).
3.  **Updating Build Scripts:** Modify constants and logic within `build_roomodes.js`, `build_mode_summary.js`, and `create_build.js` to reflect the new fixed paths under `.ruru/`.
4.  **No Placeholders/Substitution:** This approach avoids the complexity of placeholders (e.g., `{{RURU_TASKS_DIR}}`) and the associated build-time substitution script required by the fully configurable path proposal. All paths within the codebase will be updated to the new fixed structure under `.ruru/`.

## 4. Benefits

*   **Cleaner Workspace:** Reduces the number of hidden directories directly in the root.
*   **Logical Grouping:** Keeps all Roo Commander system files organized together.
*   **Simpler Refactoring:** Less complex to implement than the fully configurable path solution.

## 5. Trade-offs

*   **Loss of Flexibility:** Users cannot choose to keep the folders at the root level; the `.ruru/` structure becomes mandatory.
*   **Search/Replace Risk:** Relies on careful search-and-replace operations, which carry a risk of incorrect or incomplete updates if not reviewed thoroughly.