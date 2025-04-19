# Handover Summary Approach

## 1. Purpose

To define a mechanism for capturing the essential state of an ongoing coordination effort, allowing work to be paused and resumed effectively, potentially by a different instance or user, mitigating context window limitations.

## 2. Mechanism: `session-summarizer` Mode

A new dedicated Assistant mode, `session-summarizer`, will be created. Its sole purpose is to read relevant project state artifacts and generate a structured handover summary document.

**Workflow:**
1.  Roo Commander (or user) identifies the need for a handover summary (e.g., context window nearing limit, end of work session).
2.  Roo Commander delegates a task to `session-summarizer`, providing necessary inputs (see below).
3.  `session-summarizer` reads the specified files (`read_file`, `list_files`).
4.  `session-summarizer` synthesizes the information according to the defined template.
5.  `session-summarizer` writes the summary to a timestamped file in `.context/` (`write_to_file`).
6.  `session-summarizer` reports completion, providing the path to the generated summary.

**Inputs for `session-summarizer`:**
*   Path to the primary coordination task log (e.g., `.tasks/TASK-CMD-...`).
*   Path to the active planning document (e.g., `.planning/context_file_creation_plan.md`).
*   (Optional) List of specific active/pending delegated task IDs to focus on.

## 3. Handover Document Structure

**Location:** `.context/`
**Filename:** `handover_YYYYMMDD_HHMMSS.md` (Timestamp ensures unique files for history).

**Content Template:**

```markdown
# Session Handover Summary

**Generated:** YYYY-MM-DD HH:MM:SS UTC

**Context Window:** [Current Token Count] Tokens ([Percentage]%)

## 1. Current High-Level Goal(s)

*   (Extracted from coordination task Goal section)
*   *Source:* [Link to coordination task]

## 2. Last Key Action(s) Completed

*   (Summarized from recent coordination task Notes/Checklist updates)
*   *Source:* [Link to coordination task]

## 3. Active / Pending Delegated Tasks

*   **TASK-ID:** [Task Title] - **Status:** [Status] - **Assigned:** [Mode Slug]
*   *(Repeat for key active/pending tasks)*
*   *Source:* Requires reading status from relevant `.tasks/TASK-[MODE]-...` files or coordination log.

## 4. Next Planned Step(s)

*   (Identified from the active planning document)
*   *Source:* [Link to planning document]

## 5. Key Document Links

*   **Coordination Log:** [Link to primary `.tasks/TASK-CMD-....md`]
*   **Active Plan:** [Link to `.planning/...` document being followed]
*   **Structure Inventory:** `.docs/project_structure_inventory.md`
*   **Mode Hierarchy:** `.templates/mode_hierarchy.md`

## 6. Blockers / Open Questions

*   (Extracted from coordination task Notes or explicitly stated)

---
*This summary is intended to facilitate handover between sessions or instances.*
```

## 4. Implementation Plan

1.  **Create Handover Template:** Create `.templates/handover_summary_template.md` based on the structure above. (Task for `technical-writer`)
2.  **Create `session-summarizer` Mode:** Define the new mode (`session-summarizer.mode.md`), including its role, instructions to read inputs and generate the summary using the template, and necessary tool permissions (`read_file`, `list_files`, `write_to_file`). (Task for `technical-writer` or `mode-developer`)

This approach provides a dedicated, structured way to manage session state for handover.