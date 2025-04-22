+++
id = "PRIME-RULE-OPS-RESULT-V1"
title = "Prime Coordinator: Rule - Operational Delegate Result Handling"
context_type = "rules"
scope = "Processing completion signals from delegated operational tasks"
target_audience = ["prime"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21"
tags = ["rules", "delegation", "result-handling", "monitoring", "operational", "prime"]
related_context = ["01-operational-principles.md", "04-operational-delegation-rule.md", "05-research-procedure-rule.md", "07-logging-confirmation-rule.md", "12-logging-procedures.md"]
+++

# Rule: Operational Delegate Result Handling

This rule defines how you (Prime Coordinator) process the completion signal (`<attempt_completion>`) received after delegating a standard operational task (via Rule `04`).

**Procedure:**

1.  **Await Completion Signal:** After delegating an operational task (using `new_task` per Rule `04`), wait for the specialist mode to respond with `<attempt_completion>`.

2.  **Process Completion Signal:** Upon receiving `<attempt_completion>`:
    *   **Extract Result:** Parse the `<result>` tag content.
    *   **Assess Outcome:** Determine if the specialist reported **success** (✅), **failure** (❌), or **blocker** (🧱) based on the message content and structure.

3.  **Log Outcome:** Log the reported outcome (success or failure details) from the specialist according to Rule `07` / KB `12`.

4.  **Handle Failure/Blocker:**
    *   **If** the specialist reported failure or a blocker:
        1.  **DO NOT RETRY** the exact same task automatically.
        2.  **Analyze Failure (Simple):** Review the error message provided by the specialist. Is the cause clear (e.g., "no changes staged", "file not found", "permission denied")?
        3.  **Report to User:** Use `<ask_followup_question>` to inform the user about the specific failure reported by the delegate. Example: "The attempt to commit changes failed. `dev-git` reported: '[Delegate's Error Message]'. How would you like to proceed?"
        4.  **Provide Options:** Suggest relevant next steps based on the failure. Examples:
            *   For "no changes staged": `<suggest>Check git status</suggest>`, `<suggest>Stage specific files first</suggest>`, `<suggest>Cancel commit</suggest>`
            *   For other errors: `<suggest>Retry the task</suggest>`, `<suggest>Try a different approach</suggest>`, `<suggest>Investigate the error further</suggest>`, `<suggest>Cancel</suggest>`
        5.  Await user direction before proceeding.

5.  **Handle Success:**
    *   **If** the specialist reported success:
        1.  Review the success message and any provided artifact paths or summaries.
        2.  Determine the next logical step in the overall user goal or workflow.
        3.  Report success and the next step (or task completion) to the user using `<attempt_completion>` or `<ask_followup_question>` as appropriate.

**Key Objective:** To ensure Prime Coordinator correctly interprets the success or failure status reported by operational delegates and takes appropriate action (reporting failure to user, proceeding on success) instead of blindly retrying failed tasks.