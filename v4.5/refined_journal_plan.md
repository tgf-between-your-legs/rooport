# Refined Project Journal Plan (v4.5 Modes)

This document outlines the agreed-upon structure and conventions for the `project_journal/` directory and related documentation practices.

**Core Principles:**

1.  **Purpose-Driven:** Documentation serves primarily for AI context rebuilding and secondarily for human understanding. Avoid logging for logging's sake.
2.  **AI Context Focus:** Structure information for efficient AI loading without overwhelming noise.
3.  **Human Navigability:** Use clear structures, naming, diagrams, and emojis.
4.  **Avoid Large Append-Only Files:** Replace single large logs with granular files.
5.  **Centralize Information Types:** Group related information logically.

**Revised Structure:**

*   **`project_journal/tasks/TASK-ID.md`:**
    *   **Purpose:** Detailed, chronological history of individual tasks (goal, steps, findings, outcome). Replaces the central `activity_log.md`.
    *   **Managed By:** Created/appended by the assigned specialist mode via delegation to `secretary`.
*   **`project_journal/decisions/YYYYMMDD-topic.md`:**
    *   **Purpose:** Record significant, project-level decisions (ADR-like format).
    *   **Managed By:** Created by `technical-architect` or `roo-commander` via delegation to `secretary`.
*   **`project_journal/formal_docs/`:**
    *   **Purpose:** Store finalized outputs (reports, specs, guides, research summaries, API specs, audit reports, test plans, finalized configs, etc.).
    *   **Managed By:** Created by relevant modes (e.g., `api-developer`, `security-specialist`, `technical-writer`) via delegation to `secretary`.
*   **`project_journal/visualizations/`:**
    *   **Purpose:** Store Mermaid diagrams (architecture, database, task status, workflows).
    *   **Managed By:** Created/updated by `diagramer` via delegation to `secretary`.
*   **`project_journal/planning/`:**
    *   **Purpose:** Store core planning documents.
    *   **Files:** `requirements.md`, `architecture.md`, `project_plan.md`.
    *   **Managed By:** Created/updated by relevant modes (`discovery-agent`, `technical-architect`, `project-manager`) via delegation to `secretary`.
*   **`project_journal/technical_notes/`:**
    *   **Purpose:** For ad-hoc technical documentation not fitting elsewhere.
    *   **Managed By:** Available for use, likely by `technical-writer` via `secretary`.
*   **Eliminated Directories:**
    *   `project_journal/memories/` (Details integrated into task logs, code comments, formal docs).
    *   `project_journal/decision_log/` (Superseded by `project_journal/decisions/`).
    *   `project_journal/formal_docs/adr/` (Superseded by `project_journal/decisions/`).

**System Guidelines File:**

*   **File:** `ROO_COMMANDER_SYSTEM.md` (at project root).
*   **Purpose:** Define global principles, structure overview, emoji legend, delegation guidelines. Reduces redundancy in mode prompts.
*   **Creation:** Created with standard content by `project-initializer` for new projects.
*   **Checking:** Checked once by `project-onboarding` for existing projects; absence noted to `roo-commander`.
*   **Updates:** Treated as static by default. Updates require manual user intervention or a future dedicated process. Modes reference it conceptually.

**Other Conventions:**

*   **Mode Instructions:** Use positive guidance for documentation paths.
*   **`secretary` Role:** Enforces path safety for writes *within* `project_journal` and root README/LICENSE. Does *not* write code files.
*   **`diagramer` Role:** Generates/updates Mermaid syntax, delegates write/overwrite to `secretary`.
*   **Emojis:** Standardized usage encouraged (legend in `ROO_COMMANDER_SYSTEM.md`).