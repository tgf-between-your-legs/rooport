# Summary of Roo Commander Mode Journaling & Documentation Updates (v4.5 Refinement)

This document outlines the recent changes made to the `customInstructions` for all Roo Commander modes within the `roo-modes-dev/` directory. These updates refine the project journaling and documentation strategy to improve clarity, efficiency, AI context rebuilding, and human readability.

## 1. Initial State & Problems Addressed

*   **Obsolete `logger` Mode:** The previous instructions referenced a `logger` mode (delegated via `new_task`) for appending entries to a central log. This mode was removed, requiring updates across all modes that used it.
*   **Single `activity_log.md`:** The reliance on a single, append-only `activity_log.md` was identified as a scalability issue. Large projects would generate massive log files, making it difficult for both AI and humans to parse relevant context efficiently.
*   **Ambiguous `memories/` Directory:** The purpose and structure of the `project_journal/memories/` subdirectories were unclear, leading to potential redundancy, unstructured data dumps, and unnecessary noise for context loading.
*   **Inconsistent Logging:** Different modes had slightly varying logging protocols and levels of detail.

## 2. Core Principles Guiding the Refinement

The changes were driven by the following principles:

*   **🎯 Purpose-Driven:** Documentation should primarily serve AI context rebuilding and secondarily aid human understanding. Avoid logging for logging's sake.
*   **🤖 AI Context Focus:** Structure information for efficient AI loading, minimizing noise and maximizing relevant signal.
*   **🧑‍💻 Human Navigability:** Use clear structures, file naming conventions, diagrams, and emojis to help humans quickly grasp project status and history.
*   **📄 Granular Logs:** Replace monolithic logs with context-specific files (e.g., per task).
*   **🗂️ Centralized Information Types:** Group related information logically (plans, decisions, formal outputs, visualizations, task details).
*   **🛡️ Safety & Consistency:** Use dedicated modes (`secretary`) to enforce path validation for journal writes.

## 3. Summary of Structural Changes (`project_journal/`)

The standard `project_journal/` directory structure has been refined:

*   **`tasks/` (New):** Contains `TASK-ID.md` files. Each file logs the detailed history (goal, steps, findings, outcome) of a specific delegated task. This replaces the central `activity_log.md`.
*   **`decisions/` (New):** Contains `YYYYMMDD-topic.md` files documenting significant, project-level decisions using an ADR-like format. This centralizes key strategic choices.
*   **`formal_docs/`:** Stores finalized outputs (reports, specs, guides, research summaries, API specs, audit reports, test plans, finalized configs, etc.). The `adr/` subdirectory was removed, with ADRs now residing in `decisions/`.
*   **`visualizations/`:** Stores Mermaid diagrams (architecture, DB schema, task status, workflows).
*   **`planning/`:** Stores core planning documents (`requirements.md`, `architecture.md`, `project_plan.md`).
*   **`technical_notes/`:** For ad-hoc technical documentation not fitting neatly elsewhere.
*   **Eliminated Directories:**
    *   `project_journal/memories/` (Rationale integrated elsewhere).
    *   `project_journal/decision_log/` (Superseded by `project_journal/decisions/`).
    *   `project_journal/formal_docs/adr/` (Superseded by `project_journal/decisions/`).

## 4. Introduction of Task-Based Logging

*   Instead of appending all actions to `activity_log.md`, modes now log the progress and outcome of specific tasks within dedicated files: `project_journal/tasks/[TaskID].md`.
*   The mode assigned the task is responsible for initializing this log (via `secretary`) and appending key steps, findings, and the final completion status.
*   This allows AI and humans to easily retrieve the full history of a specific piece of work.

## 5. Consolidated Decision Records

*   Significant, cross-cutting decisions (architecture, technology choices) are now recorded in individual files within `project_journal/decisions/`, following an ADR-like structure.
*   This provides a clear, central location for understanding key project directions and their rationale.

## 6. Elimination of `memories/`

*   The `memories/` directories were removed to reduce clutter and redundancy.
*   Modes are now instructed to integrate detailed rationale or complex findings directly into the most relevant location:
    *   Code comments for code-specific rationale.
    *   The relevant `project_journal/tasks/TASK-ID.md` file for task-specific details, analysis steps, or troubleshooting notes.
    *   `project_journal/formal_docs/` for finalized, synthesized outputs like research summaries or detailed reports.

## 7. Role of `ROO_COMMANDER_SYSTEM.md`

*   A new file, `ROO_COMMANDER_SYSTEM.md`, is created at the project root by `project-initializer`.
*   It contains standard guidelines, principles, the journal structure overview, and the emoji legend.
*   Modes conceptually refer to this file in their instructions, reducing prompt length and ensuring consistency.
*   This file is intended to be static by default, with updates managed manually by the user if needed.

## 8. Roles of `secretary` and `diagramer`

*   **`secretary`:** Acts as the gatekeeper for all file writes *within* the `project_journal` structure (tasks, decisions, formal_docs, visualizations, planning, technical_notes) and specific root files (README, LICENSE, ROO_COMMANDER_SYSTEM.md). It validates paths and performs writes/appends as instructed. It does *not* write code files.
*   **`diagramer`:** Focuses solely on generating/updating Mermaid diagram syntax based on conceptual requests. It then delegates the actual file writing (to `project_journal/visualizations/`) to the `secretary`.

## 9. Emoji Usage Standardization

*   A standard legend of emojis is defined in `ROO_COMMANDER_SYSTEM.md`.
*   Modes are encouraged to use these emojis consistently to prefix summaries and log entries, improving human scannability and providing potential semantic anchors for AI.

## 10. Benefits of the New Structure

*   **Improved AI Context Loading:** Smaller, focused files (task logs, decision records) allow AI to load more relevant context without exceeding limits or being overwhelmed by irrelevant history.
*   **Enhanced Human Readability:** Clearer structure, dedicated files for specific information types, and visual aids (diagrams, emojis) make it easier for humans to navigate and understand project status and history.
*   **Reduced Redundancy:** Eliminating `memories` encourages information consolidation.
*   **Increased Scalability:** The system is less likely to be bogged down by a single massive log file.
*   **Better Maintainability:** Centralized guidelines in `ROO_COMMANDER_SYSTEM.md` simplify future updates to core principles.
*   **Enhanced Safety:** The `secretary` mode provides a safety layer for journal writes.