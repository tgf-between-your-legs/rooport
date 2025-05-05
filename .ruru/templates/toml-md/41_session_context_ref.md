+++
# --- Session Artifact: Context Reference ---
id = "" # (String, Required) Unique ID for this artifact (e.g., "CTX-REF-YYYYMMDD-HHMMSS"). << Placeholder: Must be generated at runtime >>
session_id = "" # (String, Required) ID of the parent session log. << Placeholder: Must be set at runtime >>
type = "context_ref" # (String, Required) Fixed type for this artifact.
created_time = "" # (Datetime, Required) Timestamp when the artifact was created. << Placeholder: Must be generated at runtime >>
related_task_id = "" # (String, Optional) ID of a related MDTM task, if applicable.
ref_path = "" # (String, Required) The relative path to the referenced file or resource within the workspace.
summary = "" # (String, Required) A brief summary of the referenced context and its relevance to the session.
tags = [
    # (Array of Strings, Optional) Keywords relevant to the context reference.
    "session", "artifact", "context", "reference",
]
+++

# Session Context Reference: [Brief Title]

## Referenced Path

`[Specify the relative path to the file or resource being referenced.]`

## Summary

[Provide a concise summary explaining what the referenced context is and why it's relevant to the current session or task.]

## Key Points (Optional)

[List specific key points or details from the referenced context.]
- Point 1
- Point 2