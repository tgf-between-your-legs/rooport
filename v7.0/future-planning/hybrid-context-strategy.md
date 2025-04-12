# Hybrid Context Strategy for Roo Commander v7.x+

**Version:** 0.1
**Date:** 2025-04-13
**Status:** Proposed

## 1. Introduction

This document outlines a proposed hybrid strategy for managing project context and mode-specific information within the Roo Commander system, leveraging both the established `project_journal` directory and the new capabilities of the workspace-local `.roo` directory introduced by Roo Code.

**Goal:** To utilize the strengths of both locations – the visibility and human-centric nature of `project_journal` for core project artifacts, and the flexibility and mode-scoping of `.roo` for specialized knowledge, large context files, and potentially learned data – creating a more powerful and adaptable system.

## 2. Directory Roles and Scope

### 2.1. `project_journal/` (The Shared Project Record)

*   **Purpose:** Remains the primary, **visible**, and **version-controlled** repository for core project artifacts intended for both human and AI consumption. Analogy: The central project wiki/documentation/task board.
*   **Scope:**
    *   `tasks/`: MDTM task files (e.g., `TASK-MODE-YYYYMMDD-HHMMSS.md`). The central record of work items.
    *   `decisions/`: Architecture Decision Records (ADRs) documenting significant choices.
    *   `planning/`: High-level planning documents (e.g., `requirements.md`, `architecture.md`, `project_plan.md`, `team_structure.md` [New - See Mode Manifest Doc]).
    *   `visualizations/`: Mermaid diagrams or other visual artifacts referenced by documentation.
    *   `context/`: General project context files not specific to one mode (e.g., `stack_profile.md`, `user_profile.md`).
    *   `formal_docs/`: Final, polished project outputs or documentation.
*   **Accessibility:** Should be easily browsable by the user. Modes like `roo-commander`, `project-manager`, `technical-architect`, and `context-resolver` will primarily interact with this directory for core project state.

### 2.2. `.roo/` (The Workspace Configuration & Mode Internals)

*   **Purpose:** A workspace-specific directory managed by Roo Code, primarily for configuration and potentially "internal" or specialized mode data. Analogy: A team member's local configuration, notes, or cached data.
*   **Scope:**
    *   `context/{mode-slug}/`: **Mode-Specific Knowledge & Cache.**
        *   **Use Cases:** Storing large knowledge base documents referenced in a mode's `customInstructions`, cached API schemas, complex prompt templates, potentially learned patterns or preferences specific to *that mode* within *that project*.
        *   **Format:** Can be `.md`, `.txt`, `.yaml`, `.json` as needed by the mode.
        *   **Referencing:** Modes should reference these files using relative paths from the workspace root (e.g., `.roo/context/react-specialist/common-patterns.md`) within their `customInstructions`.
        *   **Mutability:** Primarily intended to be read by the mode. Allowing modes to *write* to their context folder is a powerful future possibility but requires careful consideration of permissions and state management (Deferred Decision).
    *   `rules/` & `.roorules`: **Workspace-Wide Rules.** As defined by Roo Code, for applying general instructions/guidelines to all modes in the workspace.
    *   `system-prompt-{mode-slug}`: **System Prompt Overrides.** As defined by Roo Code ("Footgun Prompting").
    *   `docs/` (Proposed): **System Documentation.** Could potentially house generated documentation like the Mode Manifest / Org Chart if keeping it separate from `project_journal` is desired.
*   **Accessibility:** Hidden by default (`.` prefix). Primarily intended for Roo Code and advanced user/AI interaction. Less emphasis on direct human browsing compared to `project_journal`.
*   **.gitignore:** Crucial decision needed.
    *   Option A (Default): `.roo` is often ignored. This is fine for cached data or truly transient mode context but **unsuitable** if `.roo/context/` stores essential, project-specific knowledge bases or configurations that need to be shared/versioned.
    *   Option B (Recommended for Hybrid): Add exceptions to `.gitignore` to explicitly *include* `.roo/context/`, `.roo/rules/`, `.roo/docs/` (if used), and any other non-transient subdirectories, while potentially still ignoring cache or temporary files within `.roo`. Example:
        ```gitignore
        # Ignore .roo generally
        .roo/

        # But DO NOT ignore specific subdirectories needed for project context/config
        !.roo/context/
        !.roo/rules/
        !.roo/docs/
        # Add other specific exceptions as needed
        ```

## 3. Mode Interaction & Context Referencing

*   **Delegation:** When delegating tasks (`new_task`), the orchestrating mode (e.g., Commander) should provide references to relevant context from *both* locations as needed:
    *   Core artifacts: `project_journal/tasks/TASK-XYZ.md`, `project_journal/planning/architecture.md`
    *   Mode-specific context: `.roo/context/react-specialist/style-guide.md` (if the task involves React and styling).
*   **Context Resolution (`context-resolver`):** This mode needs enhancement. When asked for a summary, it should:
    1.  Prioritize reading specified files from `project_journal`.
    2.  Potentially be instructed to *also* look for relevant context in `.roo/context/{relevant-mode-slug}/` if applicable to the query (e.g., "Summarize React component guidelines" might check `.roo/context/react-specialist/`). This requires careful prompting.
*   **Mode Awareness:** Modes should be primarily designed to work with the context *provided* to them during task delegation. They can reference their *own* context files (`.roo/context/{self-slug}/`) directly within their instructions. Referencing *other* modes' context files should generally be avoided; needed information should be passed via the orchestrator or summarized by `context-resolver`.

## 4. Future Considerations & Potential Migration

*   **Mode Write Access to `.roo/context/`:** Allowing modes to update their own context files could enable learning and adaptation within a project but introduces complexity in managing state and potential conflicts. This requires further design.
*   **Full Migration to `.roo`:** If the hybrid model proves successful and user discoverability concerns are addressed (perhaps through better tooling or documentation), migrating `project_journal` contents into a structured `.roo/project/` subdirectory could be considered for ultimate centralization. This would be a major breaking change requiring significant updates to all modes referencing `project_journal`.

## 5. Conclusion

The proposed hybrid strategy aims to balance the visibility and established conventions of `project_journal` with the enhanced flexibility and mode-specific context capabilities of the `.roo` directory. It allows modes to access larger, specialized knowledge bases without cluttering the main project record, while keeping core tasks, decisions, and plans accessible to the user. Key next steps involve defining the Mode Manifest, refining the Communication Plan, adapting MDTM, and updating key modes like `context-resolver` and `roo-commander` to operate within this hybrid model. Careful management of `.gitignore` is essential if versioning `.roo` subdirectories.