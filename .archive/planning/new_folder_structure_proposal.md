# Proposed New Folder Structure (Replacing project_journal/)

This document outlines the proposed new hidden folder structure intended to replace the existing `project_journal/` directory and consolidate other scattered resources like `v7.0/context/`, `v7.0/templates/`, etc. The goal is a flatter, more organized structure at the workspace root.

## Proposed Root-Level Folders

*   **`.tasks/`**
    *   **Purpose:** Stores active operational task files, primarily following the Markdown-Driven Task Management (MDTM) standard.
    *   **Interaction:** `project-manager` creates/updates tasks here. All modes read/update their assigned task files. `roo-commander` monitors this folder. `context-resolver` may read for status summaries.
    *   **Subfolders:** Potentially subfolders by status (e.g., `pending/`, `in-progress/`, `completed/`) could be added later, but start flat.
*   **`.decisions/`**
    *   **Purpose:** Stores Architecture Decision Records (ADRs) documenting significant technical choices.
    *   **Interaction:** `technical-architect` or `roo-commander` creates ADRs here. All modes may reference ADRs for context. `context-resolver` reads for status summaries.
    *   **Subfolders:** None typically needed; dated filenames provide organization.
*   **`.context/`**
    *   **Purpose:** Holds generated context summaries, the Stack Profile, user profile information, and other transient or derived context useful for modes.
    *   **Interaction:** `context-resolver` and `discovery-agent` write summaries/profiles here. `research-context-builder` might store intermediate findings. All modes read for situational awareness. `roo-commander` may store user profile info.
    *   **Subfolders:** Maybe `profiles/`, `summaries/`.
*   **`.docs/`**
    *   **Purpose:** Central repository for relatively stable documentation, standards, guides, and knowledge.
    *   **Interaction:** `technical-writer` primarily creates/updates content. `project-manager` might update standards. All modes reference for guidance.
    *   **Subfolders:**
        *   `standards/` (e.g., MDTM, coding style)
        *   `guides/` (e.g., How-to guides for modes/tools)
        *   `knowledge/` (e.g., Framework summaries, research findings)
        *   `reviews/` (Formal review documents)
        *   `diagrams/` (Generated architecture/workflow diagrams - Mermaid, PlantUML etc. `diagramer` writes here)
*   **`.templates/`**
    *   **Purpose:** Contains templates for various artifacts, like new mode definitions, ADR formats, task file structures.
    *   **Interaction:** `mode-maintainer` uses mode templates. `technical-architect` might use ADR templates. `project-manager` might use task templates.
    *   **Subfolders:** Maybe `modes/`, `adr/`, `tasks/`.
*   **`.planning/`**
    *   **Purpose:** Holds high-level project plans, strategic documents, roadmaps, and planning artifacts for initiatives like this refactoring.
    *   **Interaction:** `roo-commander`, `project-manager`, `technical-architect` create/update plans. All modes may reference for project direction.
    *   **Subfolders:** Potentially by quarter (e.g., `2025-Q2/`) or initiative.
*   **`.logs/`**
    *   **Purpose:** Stores output logs from commands executed by modes or build/test processes. Useful for debugging.
    *   **Interaction:** Modes using `execute_command` might direct output here. `cicd-specialist` or testers might store build/test logs. `bug-fixer` might read logs.
    *   **Subfolders:** Maybe by mode slug or date.
*   **`.reports/`**
    *   **Purpose:** Contains generated reports like test coverage, performance benchmarks, security scans.
    *   **Interaction:** Testing modes (`e2e-tester`, `integration-tester`), `performance-optimizer`, `security-specialist` would write reports here. `project-manager` or `roo-commander` might review.
    *   **Subfolders:** Maybe `coverage/`, `performance/`, `security/`.
*   **`.ideas/`**
    *   **Purpose:** A less formal space for brainstorming, future feature ideas, quick notes, and scratchpad content.
    *   **Interaction:** Any mode or the user can contribute ideas here.
    *   **Subfolders:** Unlikely needed.
*   **`.archive/`**
    *   **Purpose:** Location for moving completed or obsolete items from other folders (e.g., old tasks, superseded plans, previous logs) to keep active directories clean.
    *   **Interaction:** `project-manager` or potentially an automated cleanup process would move files here. Rarely read unless historical research is needed.
    *   **Subfolders:** Could mirror the main structure (e.g., `archive/tasks/`, `archive/logs/`).

## Benefits

*   Clear separation of concerns between different types of project artifacts.
*   Flatter structure compared to deep nesting within `project_journal`.
*   Uses hidden folders (`.`) to reduce clutter in the main file explorer view for users primarily interested in source code.
*   Provides dedicated places for generated outputs like logs and reports.

## Next Steps

1.  Assess existing modes for references to old paths (`project_journal/`, `v7.0/...`).
2.  Refactor modes and core guidance to use these new paths.
3.  Establish workflows for managing content (e.g., task cleanup/archival).