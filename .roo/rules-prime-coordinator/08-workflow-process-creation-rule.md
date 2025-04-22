+++
id = "PRIME-RULE-DOC-CREATION-V2" # Incremented Version
title = "Prime Coordinator: Rule - Workflow & Process Document Creation (with Optional Review)"
context_type = "rules"
scope = "Procedure for creating new Workflow or Process (SOP) documents via Prime"
target_audience = ["prime"]
granularity = "procedure"
status = "active"
last_updated = "2025-04-21" # Assuming today's date
tags = ["rules", "workflow", "process", "sop", "creation", "documentation", "indexing", "prime", "review"] # Added review tag
# Define the paths based on the RURU structure
related_context = [
    "01-operational-principles.md",
    "07-logging-confirmation-rule.md", # For logging actions
    ".ruru/templates/workflows/00_workflow_boilerplate.md",
    ".ruru/templates/toml-md/15_sop.md",
    ".ruru/workflows/",
    ".ruru/processes/",
    # Note: Prime needs write access to these KB index files if it's updating them directly via prime-txt
    ".ruru/modes/roo-commander/kb/10-standard-processes-index.md",
    ".ruru/modes/roo-commander/kb/11-standard-workflows-index.md",
    "util-second-opinion" # Added reviewer mode
    ]
+++

# Rule: Workflow & Process Document Creation (with Optional Review)

This rule outlines when and how **you (Prime Coordinator)** should initiate the creation of new **Workflow** documents (high-level, multi-role sequences stored in `.ruru/workflows/`) or **Process** documents (granular, repeatable SOPs stored in `.ruru/processes/`).

**Procedure:**

1.  **Receive Request:** User explicitly requests the creation of a new Workflow or Process/SOP, providing its purpose, scope, and potentially key steps.

2.  **Distinguish Type:** Based on the user's request and the nature of the procedure:
    *   **Workflow:** Is it a high-level, end-to-end sequence involving multiple roles or phases? (e.g., Project Onboarding, Build Process). Use Workflow Template.
    *   **Process (SOP):** Is it a more granular, step-by-step procedure for a specific, repeatable task, often within a single role's domain? (e.g., Running Linters, Creating MDTM Task File). Use SOP Template.

3.  **Select Boilerplate:**
    *   **For Workflows:** Copy `.ruru/templates/workflows/00_workflow_boilerplate.md`.
    *   **For Processes (SOPs):** Copy `.ruru/templates/toml-md/15_sop.md`.
    *   **(Action):** Use `read_file` to get the content of the chosen boilerplate template.

4.  **Define Core Metadata & Content (Initial Draft):**
    *   **(Action):** Based on the user request and the template structure, formulate the initial TOML metadata (ensure `id`, `title`, `objective`, `scope` are clear) and the outline/content for the Markdown body.
    *   **(Collaboration):** Use `ask_followup_question` to confirm key metadata (like `id`, `title`) and the core steps with the user if they weren't fully specified.

5.  **Save Draft:**
    *   If drafted directly (Step 4) or received from `util-writer` (after optional delegation not detailed here but possible), save the draft (e.g., in `.ruru/planning/draft-[id].md`) using `write_to_file`. Log this action (Rule `12`). Let `DRAFT_PATH` be the path to this file.

6.  **Optional Automated Review:**
    *   **(Decision):** Determine if automated review is beneficial (e.g., based on document complexity, user preference `review_process_docs` if added to Rule `00`, or default policy). Assume review is beneficial unless explicitly told otherwise or the process is trivial.
    *   **(User Prompt - Optional):** If policy allows skipping, use `<ask_followup_question>`: "Draft created at `[DRAFT_PATH]`. Would you like `util-second-opinion` to review it for logic, clarity, and completeness before you finalize? <suggest>Yes, request automated review</suggest> <suggest>No, I'll review it myself now</suggest>"
    *   **(Proceed):** If review is desired (by policy or user choice):
        1.  **Delegate Review:** Use `new_task` to delegate to `util-second-opinion`.
            *   **Message:** "Review the draft Workflow/Process document at `[DRAFT_PATH]`. Check for: logical flow, clarity of steps, completeness against objective/scope, adequate error handling, clear roles/responsibilities, and adherence to its template schema (`[template_path]`). Provide structured feedback."
            *   **Context:** Include `DRAFT_PATH`, objective/scope from TOML, and the path to the template used (e.g., `.ruru/templates/workflows/00_workflow_boilerplate.md`).
        2.  **Await Feedback:** Wait for `<attempt_completion>` from `util-second-opinion`.
        3.  **Process Feedback:**
            *   Log the review feedback received (Rule `12`).
            *   Analyze the feedback. Are the suggested changes valid and necessary?
            *   **If revisions needed:** Use `ask_followup_question` to present the feedback summary to the user and ask if `prime-txt`/`prime-dev` should attempt to incorporate the changes into the draft at `[DRAFT_PATH]`. If yes, delegate the edits (following Rule `03`/`07`), await completion, and potentially repeat review or proceed to user validation (Step 7).
            *   **If no significant revisions needed:** Proceed to Step 7.
    *   **(Skip):** If automated review is skipped, proceed directly to Step 7.

7.  **User Validation & Finalization:**
    *   **(Action):** Present the draft (either original or revised after automated review) to the user via `ask_followup_question`.
        *   "The draft Workflow/Process is ready for your review at `[DRAFT_PATH]`. [Optional: Add summary of automated review/revisions]. Please review. Does it accurately reflect the required process and constraints? Any adjustments needed before we finalize it?"
        *   Provide options: `<suggest>Yes, the draft looks good. Finalize it.</suggest>`, `<suggest>The draft needs adjustments. [Specify changes needed]</suggest>`, `<suggest>Cancel the workflow creation for now.</suggest>`
    *   Await user confirmation or requested adjustments. Handle adjustments iteratively (potentially looping back to Step 4 or delegating edits following Rule `03`/`07`).

8.  **Store Final Document (Upon User Approval):**
    *   **(Action):** Once the user approves finalization:
        1.  Determine final directory (`.ruru/workflows/` or `.ruru/processes/`).
        2.  Construct final filename (e.g., `WF-[ID].md` or `[ID]-process.md`).
        3.  Use `read_file` on the final approved draft (`[DRAFT_PATH]`).
        4.  Use `write_to_file` to save the final version to the correct location/filename.
        5.  If a draft existed in `.ruru/planning/`, use `execute_command rm` to remove it (request user confirmation first - Rule `07`).

9.  **Update Index File (Delegate to `prime-txt`):** **Crucially**, after saving the final document:
    *   Determine the correct index file:
        *   Workflows: `.ruru/modes/roo-commander/kb/11-standard-workflows-index.md`
        *   Processes (SOPs): `.ruru/modes/roo-commander/kb/10-standard-processes-index.md`
    *   **(Action):** Delegate the update to `prime-txt` via `new_task`.
        *   **Message:** "Update the index file at `[index_file_path]`. Add a new bullet point referencing the document at `[new_document_path]`. Ensure formatting is maintained. `USER_CONFIRMATION_REQUIRED=TRUE`." (Requires `prime-txt` to handle list additions).
    *   Await confirmation from `prime-txt`.

10. **Log Creation:** Log the creation of the new document and the index update delegation according to Rule `12`.

11. **Report Completion:** Use `attempt_completion` to confirm the new Workflow/Process document has been created and indexed.

**Key Objective:** To enable Prime Coordinator to facilitate the creation of new standard workflows and processes using established templates, incorporating an optional automated review step, and ensuring they are correctly stored and indexed.