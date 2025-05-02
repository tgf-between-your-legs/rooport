+++
# --- Session Metadata ---
session_id = "" # (String, Required) Unique ID for the session (e.g., "SESSION-YYYYMMDD-HHMMSS"). << Placeholder: Must be generated at runtime >>
title = "" # (String, Required) User-defined goal or auto-generated title for the session. << Placeholder: Must be defined at runtime >>
status = "🟢 Active" # (String, Required) Current status (e.g., "🟢 Active", "🟡 Paused", "⚪ Completed", "🔴 Error"). << Default: Active >>
start_time = "" # (Datetime, Required) Timestamp when the session log was created. << Placeholder: Must be generated at runtime >>
end_time = "" # (Datetime, Optional) Timestamp when the session was marked Paused or Completed. << Placeholder: Optional, set at runtime >>
coordinator_mode = "" # (String, Required) Slug of the Coordinator mode that initiated the session (e.g., "prime-coordinator", "roo-commander"). << Placeholder: Must be set at runtime >>
related_tasks = [
    # (Array of Strings, Optional) List of formal MDTM Task IDs (e.g., "TASK-...") related to this session.
]
related_artifacts = [
    # (Array of Strings, Optional) List of relative paths (from session root) to artifacts created/used during the session (e.g., "artifacts/CONFIRM-...", "artifacts/research-...").
]
tags = [
    # (Array of Strings, Optional) Keywords relevant to the session goal or content.
    "session", "log",
]
+++

# Session Log

*This section is primarily for **append-only** logging of events by the Coordinator.*

## Log Entries

- [YYYY-MM-DD HH:MM:SS] Initiated session with goal: [Goal Text]
- [YYYY-MM-DD HH:MM:SS] Created confirmation artifact: [artifacts/path]
- [YYYY-MM-DD HH:MM:SS] User confirmed edit for [target_file] from [artifact_path]
- [YYYY-MM-DD HH:MM:SS] Delegated task [TASK-ID (if applicable)] to [mode_slug]: [Brief Objective]
- [YYYY-MM-DD HH:MM:SS] Received result from [mode_slug]/[TASK-ID]: [Success/Failure Summary]