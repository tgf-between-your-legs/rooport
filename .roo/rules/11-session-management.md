+++
# --- Basic Metadata ---
id = "RULE-SESSION-MGMT-STANDARD-V5"
title = "Standard: Session Management Workflow V5"
context_type = "rules"
scope = "Workspace-wide standard for session initiation, logging, confirmation, and artifact management"
target_audience = ["all"] # Coordinators, Specialists, Leads
granularity = "procedure"
status = "active"
last_updated = "2025-05-03" # Use current date
tags = ["session", "logging", "standard", "workflow", "confirmation", "artifacts", "traceability", "context", "v5"]
related_context = [
    ".ruru/docs/concepts/session_management_whitepaper_v1.md",
    ".roo/rules-roo-commander/11-session-management-impl.md",
    ".roo/rules-prime-coordinator/11-session-management-impl.md",
    ".ruru/templates/toml-md/19_mdtm_session.md",
    ".roo/rules/08-logging-procedure-simplified.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md"
]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the standard session workflow for all modes"
+++

# Standard: Session Management Workflow V5

## 1. Introduction & Goal

This document defines the standard "Session Management V5" workflow applicable to all modes within the Roo Commander workspace, particularly coordinators like `roo-commander` and `prime-coordinator`.

**Goal:** To enhance traceability, context management, and continuity across user interactions by providing a structured, persistent record of a user's interaction focused on achieving a particular objective, complementing MDTM tasks.

## 2. Core Idea: The Session Log

The central concept is the optional, structured **Session Log** (`session_log.md`), implemented using the TOML+Markdown format. It's associated with a specific user goal or interaction period and resides in a dedicated session directory, acting as a hub linking related activities, artifacts, and decisions.

## 3. Session Initiation (New Session)

*   **Responsibility:** Session initiation (detecting the need for a new session, prompting the user, and creating the initial log file and directory structure) is the responsibility of designated **Coordinator modes** (e.g., `roo-commander`, `prime-coordinator`).
*   **Procedure:** Coordinators handle session initiation according to their specific implementation rules (e.g., `.roo/rules-roo-commander/11-session-management-impl.md`, `.roo/rules-prime-coordinator/11-session-management-impl.md`). These rules define state detection, user prompting logic, default behaviors, and the creation procedure. Specialist modes do not initiate sessions but **MUST** be aware of how to log events (Section 5) and handle artifacts (Section 6 & 7) within an active session.
*   **Outcome:** If a session is initiated, the Coordinator creates the `.ruru/sessions/[RooComSessionID]/artifacts/` directory and the `session_log.md` file, populating initial metadata and retaining the active `RooComSessionID`.

## 4. Session Log File (`session_log.md`)

This file uses the TOML+Markdown format.

*   **TOML Frontmatter:**
    *   `id`: The unique `RooComSessionID`.
    *   `title`: User-defined goal for the session.
    *   `status`: Tracks the session state (`"🟢 Active"`, `"⏸️ Paused"`, `"🏁 Completed"`, `"🔴 Error"`).
    *   `start_time`: Timestamp of session creation.
    *   `end_time`: Timestamp of session completion/pausing.
    *   `coordinator`: ID of the coordinating mode.
    *   `related_tasks`: Array of MDTM Task IDs spawned during the session (e.g., `["TASK-DEV-PY-..." ]`).
    *   `related_artifacts`: Array of relative paths to files in the `artifacts/` directory (e.g., `["artifacts/confirm_edit_abc.md"]`).
    *   `tags`: Keywords related to the session goal.
*   **Markdown Body:**
    *   **Goal/Description:** Expanded description of the session's objective.
    *   **Log Entries:** Chronologically ordered, timestamped list of significant events (see Section 5).

## 5. Logging Events

If a session is active (`RooComSessionID` is set), modes **MUST** log significant events concisely to the `session_log.md` (typically using `insert_content` line 0 for chronological order). Key events include:

*   Session start/end/pause.
*   User prompts and significant decisions/responses.
*   Delegations (including target mode and MDTM Task ID if applicable).
*   Artifact creation (including path relative to session dir).
*   Confirmation requests and responses (referencing artifact path).
*   Confirmation skip decisions and rationale (by Coordinator).
*   Results/completions received from delegates.
*   Errors encountered (source, message).
*   Key decisions made (link to ADRs if applicable).

Refer to KB `.ruru/modes/roo-commander/kb/12-logging-procedures.md` for detailed guidance on logging tools.

## 6. Artifact Management

*   The `.ruru/sessions/[RooComSessionID]/artifacts/` directory stores files generated or relevant during the session (proposed edits, research notes, config snippets, diagrams, etc.).
*   Paths referenced in `related_artifacts` **MUST** be relative to the session directory (e.g., `artifacts/research_notes.txt`).
*   This ensures persistence and linkage to the session context.

## 7. Confirmation Workflow (Standard for Coordinator-Managed Edits via Artifacts)

This workflow leverages session artifacts for traceable and safe edits performed by designated executor modes capable of file modification.

1.  **Coordinator Prepares:** Identify `TARGET_PATH` and `NEW_CONTENT` for the edit.
2.  **Write to Artifact:** Write the `NEW_CONTENT` (or a diff) to an artifact file: `.ruru/sessions/[RooComSessionID]/artifacts/CONFIRM-[sanitized_target_name]-[timestamp].md` (or `.ruru/temp/...` if no active session). Store the `ARTIFACT_PATH`.
3.  **Log Artifact Creation:** Log the event and update `related_artifacts` in `session_log.md` (if session active).
4.  **Assess Confirmation Need:**
    *   **MAY Skip Confirm** (Coordinator discretion) if the edit is assessed as **highly routine, simple, AND low-risk**. Log skip decision and rationale (if session active).
    *   **MUST Confirm** in all other cases.
5.  **Confirmation Process (If Confirming):**
    *   Use `ask_followup_question` referencing the `ARTIFACT_PATH`: "Please review the proposed changes in `[ARTIFACT_PATH]`. Do you approve?".
    *   Log request/response (if session active).
    *   If user responds "No", log rejection and stop this workflow branch. Discuss alternatives.
6.  **Delegation to Executor:**
    *   Use `new_task` targeting the appropriate executor mode (selected by the Coordinator).
    *   Message **MUST** include: "Read `[ARTIFACT_PATH]`, write to `[TARGET_PATH]`. **[User confirmed / Confirmation skipped by Coordinator - low risk]. No re-confirm needed.**"
    *   Log delegation (if session active).
7.  **Await & Log Result:** Await `attempt_completion` from the executor. Log the outcome (success/failure) in `session_log.md` (if session active).
8.  **Cleanup:** Delete the temporary artifact file if it was created in `.ruru/temp/`.

## 8. Continuing/Referencing Sessions

Modes (especially coordinators) **MUST** implement logic to handle user requests or system commands (e.g., `/continue_session [RooComSessionID]`) to load and resume logging to an existing session log.

## 9. Relationship to MDTM Tasks

*   **Session Logs:** Track the overall user interaction narrative, linking activities.
*   **MDTM Tasks:** Track specific, delegated work units.
*   They are complementary. A session can contain multiple MDTM tasks, linked via `related_tasks`.