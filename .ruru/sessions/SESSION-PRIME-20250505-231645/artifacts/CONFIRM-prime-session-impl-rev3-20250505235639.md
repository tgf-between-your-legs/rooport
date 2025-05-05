+++
# --- Basic Metadata ---
id = "PRIME-RULE-SESSION-IMPL-V3" # Incremented version
title = "Prime Coordinator: Session Management V5 Implementation (Revised Confirmation)"
context_type = "rules"
scope = "Mode-specific implementation of the workspace session management standard."
target_audience = ["prime-coordinator"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-05" # Updated date
tags = ["session", "logging", "implementation", "prime-coordinator", "confirmation", "skip-confirm"]
related_context = [
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules-prime-coordinator/03-meta-dev-workflow-simplified.md" # Now reflects V9
    ]
# template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md" # Optional, can add if needed
+++

# Prime Coordinator: Session Management V5 Implementation

This rule details how `prime-coordinator` implements the standard Session Management Workflow V5 (`.roo/rules/11-session-management.md`).

1.  **Session State Detection:** Implement logic to detect session state (New, Continue, New-Ref, None) based on chat history or future system signals. Maintain the active `RooComSessionID` if applicable.
2.  **Session Initiation (New Session):**
    *   **Prompting First:** Unless the initial task is clearly trivial, **MUST** first prompt the user regarding session log creation (per Rule 11, Section 3) using `ask_followup_question` with options like: "Create log with goal: [Suggest goal]", "Create log (no goal)", "Proceed without log (default)".
    *   **Default Behavior:** If the user selects the default option ("Proceed without log") or doesn't explicitly opt-in via the prompt, the default is **not** to create a session log.
    *   **Creation:** If user explicitly opts-in via the prompt, follow Rule 11, Section 3 procedure (create folder `.ruru/sessions/[RooComSessionID]/`, subfolder `artifacts/`, `session_log.md` using template `19_mdtm_session.md`, log initiation). Retain `RooComSessionID`.
3.  **Logging:** If a session is active (`RooComSessionID` is set), append concise log entries for events listed in Rule 11, Section 5 to the `session_log.md` using `insert_content` (line 0). Ensure artifact paths are relative (e.g., `artifacts/CONFIRM-...`) and update `related_artifacts` in the TOML header via `apply_diff` or similar.
4.  **Confirmation Workflow (Prime Edits via `prime-txt`/`dev`):**
    *   Follow Rule 11, Section 6 & 7: Prepare `TARGET_PATH`, `NEW_CONTENT`.
    *   **Assess Risk/Complexity:** Evaluate the proposed edit (`NEW_CONTENT` for `TARGET_PATH`).
    *   **Confirmation Skip Logic (Revised):**
        *   **Default Behavior:** Skip confirmation for edits assessed by Coordinator as **highly routine, simple, AND low-risk**. This should be the common case for Prime Coordinator edits. Log the decision and rationale (e.g., "Skipped confirm - low risk edit") to the active Session Log (if any). Proceed directly to Delegation (Step 4.3).
        *   **MUST Confirm** if the edit is assessed as complex, high-risk, potentially destructive, or if user confirmation is explicitly desired for traceability. If confirming, proceed to Artifact Creation (Step 4.1).
    *   **4.1. Artifact Creation (If Confirming):** Write content to session artifact file (`.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-...`) or temp file (`.ruru/temp/CONFIRM-...` if no active session). Store the `ARTIFACT_PATH`. Log artifact creation (if session active).
    *   **4.2. Confirmation Process (If Confirming):** Use `ask_followup_question` referencing `ARTIFACT_PATH`. Log request/response (if session active). If No, stop.
    *   **4.3. Delegation:** Instruct `prime-txt`/`dev` via `new_task`.
        *   If confirmation was skipped: "Apply changes to `[TARGET_PATH]`: [Provide NEW_CONTENT or clear instructions]. **Confirmation skipped by Coordinator - low risk.** No re-confirm needed."
        *   If confirmation was done via artifact: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **User confirmed. No re-confirm needed.**"
        *   Log delegation (if session active).
    *   **4.4. Await & Log Result:** Await `attempt_completion` from the executor. Log the outcome (success/failure) in `session_log.md` (if session active). Clean up temp file if used.
5.  **Continuing/Referencing:** Implement logic to handle user requests or future commands (`/continue_session`) to load and use existing `RooComSessionID`s.