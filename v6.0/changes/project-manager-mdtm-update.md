# Project Manager Mode Update: Integration of MDTM

**Date:** 2025-04-08

## Overview

The `project-manager` mode definition (`roo-modes-dev/project-manager.json`) has been updated to align with the **Markdown-Driven Task Management (MDTM) - Feature Structure** methodology. This shifts the primary task management approach from maintaining a single project plan/task board within the Project Manager's own log to managing individual, structured Markdown task files within a dedicated `tasks/` directory hierarchy.

The goal is to leverage the benefits of MDTM, such as co-location of tasks with code, enhanced AI context, Git-based traceability, and better integration with IDEs and AI assistants.

Reference MDTM Documentation:
*   `project_journal/knowledge/project-management/markdown-driven-task-management-MDTM/markdown-driven-task-management-MDTM-feature-structure/README.md`
*   `project_journal/knowledge/project-management/markdown-driven-task-management-MDTM/markdown-driven-task-management-MDTM-feature-structure/implementing.md`

## Key Changes Summary

1.  **Task Management Focus:** Shifted from a central PM log/plan to individual `.md` task files in `tasks/FEATURE_.../`.
2.  **YAML Front Matter:** Task status, assignment, priority, and other metadata are now managed via YAML front matter within each task file.
3.  **Tool Usage:** Emphasizes using `write_to_file` to create new task files and `apply_diff` (preferred) or `write_to_file` to update the status and content of existing task files.
4.  **Delegation Context:** When delegating via `new_task`, the primary context provided to specialist modes is now the *path* to the specific MDTM task file.
5.  **Monitoring:** Progress monitoring involves reading the `status` and content of individual task files using `read_file`.
6.  **PM's Own Log:** The Project Manager still maintains a log (`project_journal/tasks/[PM_TaskID].md`), but it's now focused on tracking the PM's *own* activities (task creation, delegation actions, high-level status reporting) rather than being the central task list itself.
7.  **Mode Name:** Updated to "📋 Project Manager (MDTM)" for clarity.
8.  **Role Definition:** Updated to reflect the use of MDTM and management of task files.

## Detailed Changes in `customInstructions`

*   **Operational Principles:** Added a principle emphasizing strict adherence to MDTM conventions.
*   **Step 1 (Receive Assignment & Initialize PM Log):** Clarified that the PM's log (`project_journal/tasks/[PM_TaskID].md`) is for tracking the PM's *own* activities related to managing the MDTM process, not the feature tasks themselves. Added reference to MDTM docs.
*   **Step 2 (Create & Define MDTM Tasks):** Replaced the old "Translate Requirements" step. Now instructs the PM to create individual `.md` task files in the correct `tasks/FEATURE_.../` directory using `write_to_file`. Specifies populating YAML front matter and Markdown body according to MDTM standards. Requires logging this creation action in the PM's own log.
*   **Step 3 (Plan & Track via MDTM Structure):** Replaced the old "Plan & Track" (which involved updating central plan files). Now focuses on managing the task flow by updating the `status` field within the YAML of *individual task files* using `apply_diff` or `write_to_file`. Mentions managing the `tasks/` directory structure and creating `_overview.md` files. Requires logging significant planning actions in the PM's own log.
*   **Step 4 (Delegate Tasks to Specialists):** Updated instructions to assign tasks by modifying the `assigned_to` and `status` fields in the *task file's YAML*. Crucially, the `new_task` message to the specialist must now include the *full path* to the relevant MDTM task file as the primary context. Requires logging the delegation (including task file path) in the PM's own log.
*   **Step 5 (Monitor Progress via Task Files):** Changed monitoring from reviewing a central PM log/plan to using `read_file` to check the `status` and content of *individual task files*.
*   **Step 6 (Communicate & Resolve Blockers):** Instructions now specify updating the blocked task's status (`⚪ Blocked`) directly in its YAML front matter and investigating reasons within the task file's body. Reporting to Commander should reference specific task file IDs/paths. Requires logging communication in the PM's own log and updating the relevant task file's status/notes.
*   **Step 7 (Ensure Delivery):** Reframed as driving task files through the MDTM workflow statuses towards `🟢 Done`.
*   **Step 8 (Log PM Task Completion):** Clarified that this step applies when the PM's *own high-level assignment* is done. The summary in the PM's log should reference the relevant MDTM feature directory (e.g., `tasks/FEATURE_X/`).
*   **Step 9 (Report Back to Commander):** No major change, still uses `attempt_completion` referencing the PM's own log.
*   **Task Board Example:** Removed the old Markdown task board example as task tracking is now decentralized into individual files.
*   **Error Handling Note:** Updated to reflect that failures should be logged in the PM's own log, and potentially involve updating the relevant MDTM task file's status (e.g., to `⚪ Blocked`).

These changes fundamentally integrate the Project Manager mode with the MDTM workflow, making it the orchestrator of tasks defined and tracked within the `tasks/` directory structure.