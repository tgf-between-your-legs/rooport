# 08 - Rule: Creating Workflow Documents

This rule defines the procedure for creating new **Workflow** documents, which represent high-level, potentially multi-role, end-to-end sequences of activities designed to achieve a significant outcome (e.g., creating a build, onboarding a project). Workflows typically orchestrate multiple processes and are stored in the `.workflows/` directory. Contrast this with **Processes/SOPs** (see `09-process-creation-rule.md`) which detail granular, repeatable steps often within a single role's domain.

**Procedure:**

1.  **Identify Need:** Determine that a new high-level workflow (as defined above) needs to be formally documented.
2.  **Use Boilerplate:** Always start by copying the standard workflow boilerplate template: `.templates/workflows/00_workflow_boilerplate.md`.
3.  **Define Metadata:** Carefully fill in the TOML frontmatter (`+++` block) according to the boilerplate's schema. Pay close attention to `id`, `title`, `objective`, `scope`, `roles`, `trigger`, `success_criteria`, and `failure_criteria`.
4.  **Detail Steps:** In the Markdown body, clearly outline each major step or phase of the workflow.
    *   Focus on the sequence of activities and handoffs between roles.
    *   Distinguish between Coordinator actions and delegated tasks/phases.
    *   For delegated steps, specify the delegate role/mode, high-level inputs, expected outcomes, and how completion is verified.
    *   Reference relevant tools (`execute_command`, `new_task`, `read_file`, etc.) and specific processes/SOPs (from `.processes/`) where applicable.
    *   Reference related documents (e.g., ADRs, planning docs) or rules.
5.  **Define Conditions:** Clearly state preconditions (what must be true before starting) and postconditions (what must be true after successful completion).
6.  **Error Handling:** Outline overall error handling strategies and escalation paths relevant to this specific workflow, referencing the general procedure in `05-collaboration-escalation.md`.
7.  **Save File:** Save the new workflow document in the `.workflows/` directory, using a descriptive filename (e.g., `WF-XYZ-brief-description.md`).
8.  **Update Index:** **Crucially**, update the master workflow index file `11-standard-workflows-index.md` to include a reference to the newly created workflow. Log this update according to `12-logging-procedures.md`.
9.  **Review (Self/Peer):** Review the workflow for clarity, completeness, and correctness before considering it active. (PAL validation is recommended).
