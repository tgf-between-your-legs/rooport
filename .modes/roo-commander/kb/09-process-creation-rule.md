# 09 - Rule: Creating Process Documents (SOPs)

This rule defines the procedure for creating new **Process** documents, also known as Standard Operating Procedures (SOPs). Processes detail the specific, step-by-step instructions for performing a repeatable task, usually within a single role's domain (e.g., running code quality checks, refactoring a specific pattern). They are stored in the `.processes/` directory. Contrast this with **Workflows** (see `08-workflow-creation-rule.md`) which define higher-level, end-to-end sequences.

**Procedure:**

1.  **Identify Need:** Determine that a specific, repeatable procedure needs to be formally documented as an SOP.
2.  **Use Boilerplate:** Start by copying the standard SOP template: `.templates/toml-md/15_sop.md`. While the *structure* of other templates might be adaptable for very complex procedures, the focus must remain on granular, procedural steps characteristic of an SOP, and the primary SOP template should be sufficient for most cases.
3.  **Define Metadata:** Carefully fill in the TOML frontmatter (`+++` block) according to the SOP template's schema. Ensure `id`, `title`, `objective`, `scope`, `roles` (if applicable), `trigger`, `success_criteria`, and `failure_criteria` are clearly defined.
4.  **Detail Steps:** In the Markdown body, clearly outline each step of the procedure using clear, imperative language.
    *   Focus on the specific actions to be taken.
    *   Specify the responsible role for each step if the process involves handoffs (though most SOPs are single-role).
    *   Reference relevant tools (`execute_command`, `read_file`, etc.).
    *   Reference related documents or rules.
5.  **Define Conditions:** Clearly state preconditions (what must be true before starting) and postconditions (what must be true after successful completion).
6.  **Error Handling:** Outline error handling for key steps and any specific escalation paths relevant to this process, referencing the general procedure in `05-collaboration-escalation.md`.
7.  **Save File:** Save the new process document **strictly** in the `.processes/` directory, using a descriptive filename (e.g., `XYZ-brief-description-process.md`).
8.  **Update Index:** **Crucially**, update the master process index file `10-standard-processes-index.md` to include a reference to the newly created process. Log this update according to `12-logging-procedures.md`.
9.  **Review (Self/Peer):** Review the process for clarity, accuracy, completeness, and correctness before considering it active. (PAL validation is recommended).