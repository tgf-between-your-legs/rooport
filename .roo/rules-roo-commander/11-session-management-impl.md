+++
# --- Basic Metadata ---
id = "CMD-RULE-SESSION-IMPL-V2" # Incremented version
title = "Roo Commander: Session Management V5 Implementation (No Protected Paths)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["roo-commander"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-02" # Updated date
tags = ["session", "logging", "implementation", "roo-commander", "confirmation", "skip-confirm"] # Added tag
related_context = [
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Reference to the simplified workflow rule
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Assuming standard AI rule template schema
relevance = "High: Defines how roo-commander handles sessions and confirmations"
+++

# Roo Commander: Session Management V5 Implementation

This rule details how `roo-commander` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Prompting First:** Unless the initial task is clearly trivial, **MUST** first prompt the user regarding session log creation (per Rule 11, Section 3) using `ask_followup_question` with options like: "Create log with goal: [Suggest goal]", "Create log (no goal) (default)", "Proceed without log".
    *   **Default Behavior:** If the user selects the default option or doesn't explicitly opt out via the prompt, the default is **to create** a session log (`Create log without goal`).
    *   **Creation:** If user opts-in (via prompt or default), follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`. Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **Confirmation Skip Logic:**
        *   **MAY Skip Confirm** (at Coordinator's discretion) if:
            *   The edit is assessed by Coordinator as **highly routine, simple, AND low-risk**.
        *   **MUST Confirm** in all other cases.
        *   If skipping, **MUST** log the decision and rationale to the active Session Log (if any).
    *   **Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **Delegation:** Instruct `prime-txt`/`dev` via `new_task`: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**". Log delegation (if session active).
    *   Await result. Log result (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.
