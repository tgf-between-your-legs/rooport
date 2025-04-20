+++
id = "ROO-CMD-PROCESS-CREATION-RULE"
title = "Rule: Creating Process Documents (SOPs)"
context_type = "rules"
scope = "Procedure for creating standard operating procedure (SOP) documents"
target_audience = ["roo-commander"]
granularity = "ruleset"
status = "active"
last_updated = "2025-04-19"
tags = ["rules", "process", "sop", "creation", "template", "documentation", "roo-commander"]
related_context = [
  ".templates/toml-md/15_sop.md",
  ".templates/workflows/00_workflow_boilerplate.md", # For complex SOPs
  ".processes/"
]
+++

# Rule: Creating Process Documents (SOPs)

This rule defines the procedure for creating new Standard Operating Procedure (SOP) documents, typically stored in the `.processes/` directory.

**Procedure:**

1.  **Identify Need:** Determine that a specific, repeatable procedure needs to be formally documented as an SOP.
2.  **Assess Complexity & Choose Boilerplate:**
    *   For **simple, linear procedures**, start by copying the SOP template: `.templates/toml-md/15_sop.md`.
    *   For **complex, multi-step, or multi-agent procedures**, use the more comprehensive workflow boilerplate: `.templates/workflows/00_workflow_boilerplate.md`.
3.  **Define Metadata:** Carefully fill in the TOML frontmatter (`+++` block) according to the chosen boilerplate's schema. Ensure `id`, `title`, `objective`, `scope`, `roles`, `trigger`, `success_criteria`, and `failure_criteria` are clearly defined.
4.  **Detail Steps:** In the Markdown body, clearly outline each step of the procedure.
    *   Use clear, imperative language.
    *   Specify the responsible role for each step if applicable (especially when using the workflow template).
    *   Reference relevant tools (`execute_command`, `read_file`, etc.).
    *   Reference related documents or rules.
5.  **Define Conditions:** Clearly state preconditions (what must be true before starting) and postconditions (what must be true after successful completion).
6.  **Error Handling:** Outline error handling for key steps and any overall escalation paths.
7.  **Save File:** Save the new process document in the `.processes/` directory, using a descriptive filename (e.g., `XYZ-brief-description-process.md`).
8.  **Review (Self/Peer):** Review the process for clarity, accuracy, completeness, and correctness before considering it active. (PAL validation is recommended).