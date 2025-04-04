# Roo Commander System Guidelines

This document outlines the standard conventions, principles, and structures used by Roo Commander modes within this project. All modes should adhere to these guidelines.

## 1. Core Journaling Principles

*   **🎯 Purpose-Driven:** Documentation primarily serves AI context rebuilding and secondarily aids human understanding. Avoid logging for logging's sake. Focus on information needed to resume work or understand history.
*   **🤖 AI Context Focus:** Structure information for efficient AI loading. Use clear headings, concise summaries, and references. Avoid large, unstructured text dumps.
*   **🧑‍💻 Human Navigability:** Employ clear file/directory names, consistent formatting (Markdown), diagrams, and emojis to facilitate quick understanding.
*   **📄 Granular Logs:** Utilize task-specific log files (`project_journal/tasks/`) instead of a single monolithic activity log.
*   **🗂️ Centralized Information:** Group related information logically (plans, decisions, formal outputs, visualizations, task details).

## 2. Standard `project_journal/` Structure

*   **`tasks/`**: Contains `TASK-ID.md` files, logging the detailed history (goal, steps, findings, outcome) of individual delegated tasks.
*   **`decisions/`**: Contains `YYYYMMDD-topic.md` files documenting significant, project-level decisions (ADR-like format).
*   **`formal_docs/`**: Stores finalized outputs (reports, specs, guides, research summaries, API specs, audit reports, test plans, finalized configs, etc.).
*   **`visualizations/`**: Stores Mermaid diagrams (architecture, DB schema, task status, workflows).
*   **`planning/`**: Stores core planning documents (`requirements.md`, `architecture.md`, `project_plan.md`).
*   **`technical_notes/`**: For ad-hoc technical documentation not fitting neatly elsewhere.

*(Note: The `memories/` directory is intentionally omitted; detailed rationale should be integrated into task logs, code comments, or formal docs.)*

## 3. Standard Emoji Legend

Use these emojis consistently to prefix relevant entries or summaries:

*   🎯 Goal / Task Start / Objective
*   ✅ Completion / Success / Done
*   ❌ Failure / Error / Bug
*   🧱 Blocker / Issue / Dependency Problem
*   💡 Decision / Idea / Rationale / Suggestion
*   ✨ New Feature / Initialization / Creation
*   🐛 Bug Fix / Investigation
*   ♻️ Refactor / Optimization / Improvement
*   🚀 Deployment / Release / CI/CD Action
*   📊 Diagram / Visualization / Report / Metrics
*   📝 Documentation / Notes / Content / Text
*   🤔 Question / Clarification Needed / Ambiguity
*   🔒 Security Action / Finding / Vulnerability
*   ♿ Accessibility Action / Finding / WCAG Issue
*   ⚙️ Configuration / Setup / Infrastructure / Environment
*   🔍 Research / Analysis / Review / Audit
*   💾 File Write / Save Action (by Secretary/Diagramer)

## 4. General Delegation Guidelines (via `new_task`)

*   **Task ID:** Always include the relevant Task ID in the delegation message.
*   **Clarity:** Provide clear, actionable goals and specific acceptance criteria.
*   **Context:** Reference necessary context files (e.g., `project_journal/planning/requirements.md#section-3`, `project_journal/tasks/TASK-ABC.md`) or previous Task IDs.
*   **Paths:** For file creation/updates via `secretary` or `diagramer`, specify the exact, full relative target path.

## 5. File Management

*   **Code:** Modes responsible for specific code types (e.g., frontend, API, tests) write/edit code files directly using `write_to_file` or `apply_diff`.
*   **Project Journal & Root Docs:** All writes *within* `project_journal/` (except the old `activity_log.md`) and to root `README.md`/`LICENSE.md` files **must** be delegated to the `secretary` mode for path validation and consistency.
*   **Diagrams:** The `diagramer` mode generates/updates Mermaid syntax and delegates the file write to the `secretary`.