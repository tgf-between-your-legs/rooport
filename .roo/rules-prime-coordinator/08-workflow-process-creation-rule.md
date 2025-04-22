+++
id = "PRIME-RULE-DOC-CREATION-V2" # Incremented Version
title = "Prime Coordinator: Rule - Workflow & Process Document Creation (with Optional Review)"
# ... (keep other metadata, update last_updated date) ...
tags = ["rules", "workflow", "process", "sop", "creation", "documentation", "indexing", "prime", "review"] # Added review tag
related_context = [
    # ... (previous context) ...
    "util-second-opinion" # Added reviewer mode
    ]
+++

# Rule: Workflow & Process Document Creation

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

5.  **Delegate Drafting (Optional):**
    *   If the content requires significant writing beyond simple outlining based on user input, consider delegating the drafting to `util-writer` via `new_task`. Provide the chosen template content, required metadata, core steps outline, and target save path (e.g., in `.ruru/planning/draft-[id].md`). Await completion.

6.  **Save Draft & Validate:**
    *   If drafted directly (Step 4) or received from `util-writer`, save the draft (e.g., in `.ruru/planning/draft-[id].md`) using `write_to_file`.
    *   **(Action):** Inform the user the draft is ready. Recommend review or applying the Process Assurance Lifecycle (PAL) defined in `.ruru/processes/pal-process.md` before finalizing.

7.  **Finalize & Store (Upon User Confirmation/Approval):**
    *   **(Action):** Once the user confirms the content is ready for finalization:
        1.  Determine the correct final directory: `.ruru/workflows/` for Workflows, `.ruru/processes/` for Processes.
        2.  Construct the final filename (e.g., `WF-[ID].md` or `[ID]-process.md`).
        3.  Use `read_file` on the final draft (from `.ruru/planning/` or user-provided path).
        4.  Use `write_to_file` to save the final version to the correct location/filename.
        5.  If a draft existed in `.ruru/planning/`, use `execute_command rm` to remove it (request user confirmation first - Rule `07`).

8.  **Update Index File (Delegate to `prime-txt`):** **Crucially**, after saving the final document:
    *   Determine the correct index file:
        *   Workflows: `.ruru/modes/roo-commander/kb/11-standard-workflows-index.md`
        *   Processes (SOPs): `.ruru/modes/roo-commander/kb/10-standard-processes-index.md`
    *   **(Action):** Delegate the update to `prime-txt` via `new_task`.
        *   **Message:** "Update the index file at `[index_file_path]`. Add a new bullet point referencing the document at `[new_document_path]`. Ensure formatting is maintained. `USER_CONFIRMATION_REQUIRED=TRUE`." (Requires `prime-txt` to handle list additions).
    *   Await confirmation from `prime-txt`.

9.  **Log Creation:** Log the creation of the new document and the index update delegation according to Rule `07`.

10. **Report Completion:** Use `attempt_completion` to confirm the new Workflow/Process document has been created and indexed.

**Key Objective:** To enable Prime Coordinator to facilitate the creation of new standard workflows and processes using established templates and ensure they are correctly stored and indexed.