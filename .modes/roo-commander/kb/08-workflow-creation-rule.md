+++
id = "ROO-CMD-WORKFLOW-CREATION-RULE"
title = "Rule: Creating Workflow Documents"
context_type = "rules"
scope = "Procedure for creating high-level workflow documents"
target_audience = ["roo-commander"]
granularity = "ruleset"
status = "active"
last_updated = "2025-04-19"
tags = ["rules", "workflow", "creation", "template", "documentation", "roo-commander"]
related_context = [".templates/workflows/00_workflow_boilerplate.md", ".workflows/"]
+++

# Rule: Creating Workflow Documents

This rule defines the procedure for creating new high-level workflow documents, typically stored in the `.workflows/` directory.

**Procedure:**

1.  **Identify Need:** Determine that a new, potentially complex, multi-step, or multi-agent workflow needs to be formally documented.
2.  **Use Boilerplate:** Always start by copying the standard workflow boilerplate template: `.templates/workflows/00_workflow_boilerplate.md`.
3.  **Define Metadata:** Carefully fill in the TOML frontmatter (`+++` block) according to the boilerplate's schema. Pay close attention to `id`, `title`, `objective`, `scope`, `roles`, `trigger`, `success_criteria`, and `failure_criteria`.
4.  **Detail Steps:** In the Markdown body, clearly outline each step of the workflow.
    *   Distinguish between Coordinator actions and delegated tasks.
    *   For delegated steps, specify the delegate role, inputs provided, clear instructions, expected outputs, and coordinator actions upon completion/failure.
    *   Reference relevant tools (`execute_command`, `new_task`, `read_file`, etc.).
    *   Reference related documents, processes (e.g., ACQA, PAL), or rules where applicable.
5.  **Define Conditions:** Clearly state preconditions (what must be true before starting) and postconditions (what must be true after successful completion).
6.  **Error Handling:** Outline overall error handling strategies and escalation paths for the workflow.
7.  **Save File:** Save the new workflow document in the `.workflows/` directory, using a descriptive filename (e.g., `WF-XYZ-brief-description.md`).
8.  **Review (Self/Peer):** Review the workflow for clarity, completeness, and correctness before considering it active. (PAL validation is recommended).