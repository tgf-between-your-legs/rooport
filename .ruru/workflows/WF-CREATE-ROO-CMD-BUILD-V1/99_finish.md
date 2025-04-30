send the +++
# --- Step Metadata ---
step_id = "WF-CREATE-ROO-CMD-BUILD-V1-99-FINISH" # (String, Required) Unique ID for this step.
# Convention: The final step in a workflow should always use step_number = 99
step_number = 99
title = "Step 99: Finish Build Workflow" # (String, Required) Title of this specific step.
description = """
(String, Required) Finalizes the build workflow. Aggregates results,
performs cleanup, and reports the final status and artifact location.
"""

# --- Flow Control ---
depends_on = ["WF-CREATE-ROO-CMD-BUILD-V1-04-PACKAGE-ARTIFACTS"] # (Array of Strings, Required) step_ids this step needs completed first.
next_step = "" # (String, Required) Always empty for the finish step.
error_step = "EE_handle_finish_error.md" # (String, Optional) Filename to jump to if finalization fails.

# --- Execution ---
delegate_to = "lead-devops" # (String, Optional) Mode responsible for executing the core logic of this step.

# --- Interface ---
inputs = [ # (Array of Strings, Optional) Data/artifacts needed from previous steps.
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-04-PACKAGE-ARTIFACTS: packaged_artifact_path",
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-03-RUN-BUILD: build_status",
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-03-RUN-BUILD: build_log",
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-04-PACKAGE-ARTIFACTS: packaging_log",
]
outputs = [ # (Array of Strings, Optional) Final workflow outputs.
    "workflow_result: Summary object, e.g., { status: 'Success'|'Failure', artifact_path: string, build_log_path: string, packaging_log_path: string }.",
]

# --- Housekeeping ---
last_updated = "{{DATE}}" # (String, Required) Date of last modification. Use placeholder.
template_schema_doc = ".ruru/templates/toml-md/26_workflow_step_finish.md" # (String, Required) Link to this template definition.
+++

# Step 99: Finish Build Workflow

## Actions

1.  **Aggregate Results:** Collect `packaged_artifact_path`, `build_status`, `build_log`, and `packaging_log` from previous steps.
2.  **Perform Cleanup:** Remove temporary build directories or files if necessary.
3.  **Generate Final Report:** Create a summary message including the build status and paths to artifacts/logs.
4.  **Determine Final Status:** Confirm overall success based on `build_status`.
5.  **Report Outcome:** Prepare the final `workflow_result` output containing the summary.

## Acceptance Criteria

*   All required outputs from previous steps are aggregated.
*   Cleanup actions (if any) are completed.
*   A final summary (`workflow_result`) is generated containing status and relevant paths.

## Error Handling

*   If aggregation or cleanup fails, proceed to `EE_handle_finish_error.md` (if defined).