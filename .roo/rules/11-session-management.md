+++
# --- Basic Metadata ---
id = "RULE-SESSION-MGMT-STANDARD-V7" # Incremented version
title = "Standard: Session Management Workflow V7" # Incremented version
context_type = "rules"
scope = "Workspace-wide standard for session initiation, logging, and artifact management"
target_audience = ["all"] # Coordinators, Specialists, Leads
granularity = "procedure"
status = "active"
last_updated = "2025-06-05" # Use current date
tags = ["session", "logging", "standard", "workflow", "artifacts", "traceability", "context", "v7"] # Updated tag
related_context = [
    ".ruru/docs/concepts/session_management_v6_whitepaper.md", # Concept doc (still relevant)
    ".ruru/docs/standards/session_artifact_guidelines_v1.md", # Artifact guidelines
    ".ruru/templates/toml-md/19_mdtm_session.md", # Session log template
    ".ruru/templates/plain-md/session_artifact_subdir_readme.md", # New README template
    ".roo/rules/08-logging-procedure-simplified.md",
    ".ruru/modes/roo-commander/kb/12-logging-procedures.md"
]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "Critical: Defines the standard session workflow for all modes"
+++

# Standard: Session Management Workflow V7

## 1. Introduction & Goal

This document defines the standard "Session Management V7" workflow applicable to all modes within the Roo Commander workspace, particularly coordinators like `roo-commander` and `prime-coordinator`.

**Goal:** To enhance traceability, context management, and continuity across user interactions by providing a structured, persistent record of a user's interaction focused on achieving a particular objective, complementing MDTM tasks.

## 2. Core Idea: The Session Log

The central concept is the optional, structured **Session Log** (`session_log.md`), implemented using the TOML+Markdown format. It's associated with a specific user goal or interaction period and resides in a dedicated session directory, acting as a hub linking related activities, artifacts (contextual notes), and decisions.

## 3. Session Initiation (New Session)

*   **Responsibility:** Session initiation (detecting the need for a new session, prompting the user, and creating the initial log file and directory structure) is the responsibility of designated **Coordinator modes** (e.g., `roo-commander`, `prime-coordinator`).
*   **Procedure:** Coordinators handle session initiation according to their specific implementation rules. These rules define state detection, user prompting logic, default behaviors, and the creation procedure. Specialist modes do not initiate sessions but **MUST** be aware of how to log events (Section 5) and handle artifacts (Section 6) within an active session.
*   **Outcome:** If a session is initiated, the Coordinator **MUST**:
    1.  Create the main session directory (e.g., `.ruru/sessions/SESSION-[SanitizedGoal]-[YYMMDDHHMM]/`).
    2.  Create the `artifacts/` subdirectory within it.
    3.  Create the standard artifact subdirectories (e.g., `notes/`, `learnings/`, `code/`, etc.) within `artifacts/` as defined in `.ruru/docs/standards/session_artifact_guidelines_v1.md`.
    4.  Place a copy of the standard README template (`.ruru/templates/plain-md/session_artifact_subdir_readme.md`) into *each* created standard subdirectory, renaming it to `README.md`. The Coordinator should replace the placeholder `[This Subdirectory Type]` in the README content with the actual subdirectory name (e.g., "Notes", "Learnings").
    5.  Create the `session_log.md` file using the template `.ruru/templates/toml-md/19_mdtm_session.md`, populating initial metadata.
    6.  Retain the active `RooComSessionID`.

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
    *   `related_artifacts`: Array of relative paths to contextual note files within the `artifacts/` subdirectories (e.g., `["artifacts/notes/NOTE-initial_plan-2506050100.md", "artifacts/learnings/LEARNING-api_rate_limit-2506050130.md"]`).
    *   `tags`: Keywords related to the session goal.
*   **Markdown Body:**
    *   **Goal/Description:** Expanded description of the session's objective.
    *   **Log Entries:** Chronologically ordered, timestamped list of significant events (see Section 5).

## 5. Logging Events

If a session is active (`RooComSessionID` is set), modes **MUST** log significant events concisely to the `session_log.md` (typically using `insert_content` line 0 for chronological order). Key events include:

*   Session start/end/pause.
*   User prompts and significant decisions/responses.
*   Delegations (including target mode and MDTM Task ID if applicable).
*   Artifact creation (contextual notes, including path relative to session dir, e.g., `artifacts/notes/NOTE-...`).
*   Confirmation requests and responses (via `ask_followup_question`).
*   Confirmation skip decisions and rationale (by Coordinator, regarding `ask_followup_question`).
*   Results/completions received from delegates.
*   Errors encountered (source, message).
*   Key decisions made (link to ADRs if applicable).

Refer to KB `.ruru/modes/roo-commander/kb/12-logging-procedures.md` for detailed guidance on logging tools.

## 6. Artifact Management

*   The `.ruru/sessions/[RooComSessionID]/artifacts/` directory stores contextual notes generated or relevant during the session. These notes capture key information like decisions, learnings, environment details, research findings, code snippets, etc., providing richer context beyond the main log.
*   Refer to `.ruru/docs/standards/session_artifact_guidelines_v1.md` for standard subdirectories (e.g., `notes/`, `learnings/`) and naming conventions.
*   Paths referenced in `related_artifacts` **MUST** be relative to the session directory (e.g., `artifacts/notes/NOTE-decision_xyz-2506050115.md`).
*   This ensures persistence and linkage to the session context.

## 7. Continuing/Referencing Sessions

Modes (especially coordinators) **MUST** implement logic to handle user requests or system commands (e.g., `/continue_session [RooComSessionID]`) to load and resume logging to an existing session log.

## 8. Relationship to MDTM Tasks

*   **Session Logs:** Track the overall user interaction narrative, linking activities.
*   **MDTM Tasks:** Track specific, delegated work units.
*   They are complementary. A session can contain multiple MDTM tasks, linked via `related_tasks`.