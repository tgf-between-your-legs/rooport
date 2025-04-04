# Project Journal Structure Summary

This document summarizes the standard directories and types of files created within the `project_journal/` directory by the various Roo Commander modes (v4.5).

## Standard Directories

The `project-initializer` mode is responsible for creating the following core structure using `mkdir -p`:

- `project_journal/`
  - `planning/`
  - `technical_notes/`
  - `formal_docs/`
    - `adr/` (Intended for Architecture Decision Records, created by `technical-architect` via `secretary`)
  - `decision_log/` (*Note: Directory created, but ADRs are typically placed in `formal_docs/adr/`*)
  - `visualizations/`
  - `memories/`
    - `accessibility-specialist/`
    - `api-developer/`
    - `bug-fixer/`
    - `cicd-specialist/`
    - `code-reviewer/`
    - `complex-problem-solver/`
    - `containerization-developer/`
    - `database-specialist/`
    - `e2e-tester/`
    - `file-repair-specialist/`
    - `frontend-developer/`
    - `git-manager/`
    - `infrastructure-specialist/`
    - `integration-tester/`
    - `material-ui-specialist/`
    - `performance-optimizer/`
    - `php-laravel-developer/`
    - `react-specialist/`
    - `refactor-specialist/`
    - `research-context-builder/`
    - `second-opinion/`
    - `security-specialist/`
    - `tailwind-specialist/`
    - `ui-designer/`

## Key Files and Content Types

### `project_journal/activity_log.md`
- **Purpose:** Central log for all significant actions, decisions, delegations, and outcomes performed by modes.
- **Managed By:** Appended to by most modes (implicitly via logging actions). Direct writes are forbidden (enforced by `secretary`).

### `project_journal/planning/`
- `requirements.md`: Created by `discovery-agent` (via `secretary`), potentially copied by `project-initializer`. Contains project/feature requirements.
- `project_plan.md`: Created/updated by `project-manager` (via `secretary`). Contains project timelines, tasks, etc.
- `architecture.md`: Created/updated by `technical-architect` (via `secretary`). Contains high-level system architecture.
- Other planning documents may be created here by `project-manager` or `technical-architect` (via `secretary`).

### `project_journal/wbs/`
- `work_breakdown_structure.md`: Created/updated by `project-manager` (via `secretary`). Contains detailed task breakdowns.
- Other WBS-related files may be created here by `project-manager` (via `secretary`).

### `project_journal/formal_docs/`
- **Purpose:** Stores finalized, formal documentation artifacts.
- **Content Examples (Created via `secretary` delegation):**
  - API Specifications (e.g., `openapi_spec_vX.yaml`) (`api-developer`)
  - Security Audit Reports, Compliance Docs (`security-specialist`)
  - Accessibility Audit Reports, VPAT (`accessibility-specialist`)
  - Test Plans/Reports (`integration-tester`, `e2e-tester`)
  - Infrastructure Diagrams, DR Plans, Detailed Configs (`infrastructure-specialist`)
  - CI/CD Pipeline Designs/Strategies (`cicd-specialist`)
  - Database Schema Documentation (`database-specialist`)
  - Design Specifications, Style Guides (`ui-designer`)
  - User Guides, Formal Specs (`technical-writer`)
- `adr/`: Contains Architecture Decision Records (`technical-architect` via `secretary`).

### `project_journal/visualizations/`
- **Purpose:** Stores diagrams generated using Mermaid syntax.
- **Content Examples (Created/Updated via `diagramer` -> `secretary` delegation):**
  - `architecture_diagram.md` (`technical-architect`)
  - `database_schema.md` (`database-specialist`)
  - Other diagrams (workflow, sequence, C4) requested by various modes.

### `project_journal/memories/`
- **Purpose:** Stores detailed notes, rationale, complex analysis, or research findings specific to a mode's task execution. Not typically considered formal project documentation but aids context and debugging.
- **Managed By:** Each specialist mode saves its own memories within its respective subdirectory (e.g., `project_journal/memories/react-specialist/`) via delegation to the `secretary`.

### `project_journal/technical_notes/`
- **Purpose:** Intended for general technical notes (directory created by `project-initializer`).
- **Managed By:** No specific mode is explicitly instructed to write here by default, but it's available for ad-hoc technical documentation (likely via `technical-writer` -> `secretary`).

### `project_journal/decision_log/`
- **Purpose:** Intended for logging decisions (directory created by `project-initializer`).
- **Managed By:** While the directory exists, the `technical-architect` mode specifically places ADRs in `project_journal/formal_docs/adr/`. Other modes log decisions in the main `activity_log.md`.