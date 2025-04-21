+++
id = "PRIME-RULE-METADEV-V2" # Incremented Version
title = "Prime Coordinator: Rule - Meta-Development Workflow (Config Changes)"
context_type = "rules"
scope = "Handling requests to modify Roo Commander configuration files with conditional staging"
target_audience = ["prime"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Use today's date
tags = ["rules", "workflow", "meta-development", "configuration", "staging", "safety", "conditional", "prime"] # Added conditional
related_context = ["07-logging-confirmation-rule.md", "prime-txt", "prime-dev", ".staging/"] # Added staging dir
+++

# Rule: Meta-Development Workflow (Config Changes)

This rule defines the procedure for handling requests to modify Roo Commander configuration files, using staging only for protected core files.

**Procedure:**

1.  **Receive Request:** Obtain the target file path (`TARGET_PATH`) and the desired changes from the user or previous steps.
2.  **Define Protected Paths:** Identify the set of critical core files:
    *   `PROTECTED_PATHS` = patterns matching: `.roo/rules/**`, `.modes/roo-commander/**`, `.roo/rules-roo-commander/**`, `.modes/prime*/**`, `.roo/rules-prime*/**`, `.roomodes*`, `build_*.js`, `create_build.js`.
3.  **Check Protection Status:** Determine if `TARGET_PATH` matches any pattern in `PROTECTED_PATHS` (case-sensitive match on the pattern, case-insensitive likely on the filesystem check depending on OS).
4.  **Execute Workflow:**

    *   **IF `TARGET_PATH` IS PROTECTED:**
        1.  **(Staging Workflow): Initiate Staging:**
            *   Define `STAGING_PATH` (e.g., `.staging/` + relative path of `TARGET_PATH`). Ensure `.staging/` parent directories exist (or create them - consider adding `mkdir -p` logic if needed, though simple copy usually handles one level).
            *   Use `execute_command` to copy `TARGET_PATH` to `STAGING_PATH` (`cp "<TARGET_PATH>" "<STAGING_PATH>"` - quote paths). Log this action (Rule `07`). Handle copy errors (e.g., source not found).
        2.  **(Staging Workflow): Assess Staging Edit Risk:** Before delegating, assess if the requested change to the protected file seems particularly risky, complex, or has unclear instructions.
        3.  **(Staging Workflow): Delegate Staging Edit:**
            *   Determine worker: `prime-txt` (for `.md`) or `prime-dev` (for others).
            *   Prepare message: Include clear editing instructions and the `STAGING_PATH`.
            *   If Step 4.IF.2 assessed high risk/ambiguity, add `USER_CONFIRMATION_REQUIRED=TRUE` to the message.
            *   Use `new_task` to delegate to the worker. Log delegation (Rule `07`).
        4.  **(Staging Workflow): Await Completion:** Wait for `attempt_completion` from the worker. Handle worker errors (log and report failure).
        5.  **(Staging Workflow): Generate Diff:** If worker succeeded, use `execute_command` to generate a diff (`diff -u "<TARGET_PATH>" "<STAGING_PATH>"` - quote paths). Handle diff errors (e.g., if staging file wasn't created/modified).
        6.  **(Staging Workflow): Present Diff & Instruct:**
            *   If diff generated successfully, use `ask_followup_question` to:
                *   Present the generated diff clearly.
                *   State explicitly: "Changes were applied to the STAGING file (`<STAGING_PATH>`). Review the diff above. If approved, **you must MANUALLY APPLY these changes** to the original file (`<TARGET_PATH>`)."
                *   Ask: "Shall I remove the staging file (`<STAGING_PATH>`) now?" Suggest "Yes, remove staging file" and "No, keep staging file".
            *   If diff failed (e.g., no changes made by worker), inform the user no changes were made in staging.
        7.  **(Staging Workflow): Cleanup (If Confirmed):** If user confirms removal, use `execute_command` (`rm "<STAGING_PATH>"` - quote path). Log cleanup (Rule `07`).
        8.  **(Staging Workflow): Report Outcome:** Inform user the staging workflow is complete (changes staged, user needs to apply manually) using `attempt_completion`.

    *   **ELSE (`TARGET_PATH` IS NOT PROTECTED):**
        1.  **(Direct Edit Workflow): Assess Direct Edit Risk:** Before delegating, assess if the requested change to the operational file seems particularly risky (e.g., large deletion, core logic change in script), complex, has unclear instructions, or if the *user specifically asked you (Prime) to be cautious*.
        2.  **(Direct Edit Workflow): Delegate Direct Edit:**
            *   Determine worker: `prime-txt` (for `.md`) or `prime-dev` (for others).
            *   Prepare message: Include clear editing instructions and the **direct operational `TARGET_PATH`**.
            *   If Step 4.ELSE.1 assessed high risk/ambiguity OR user requested caution, add `USER_CONFIRMATION_REQUIRED=TRUE` to the message.
            *   Remind the worker that *they* must still perform their confidence check (as per their own rules).
            *   Use `new_task` to delegate to the worker. Log delegation (Rule `07`).
        3.  **(Direct Edit Workflow): Await Completion:** Wait for `attempt_completion` from the worker.
        4.  **(Direct Edit Workflow): Report Outcome:** Report the success or failure (including any confirmation rejections or permission errors reported by the worker) back to the user using `attempt_completion`.

**Safety Note:** The safety of the "Direct Edit Workflow" relies on the confirmation logic within `prime-txt` and `prime-dev` rules AND the user's global auto-approval settings. The "Staging Workflow" provides maximum safety for protected files by requiring manual application.