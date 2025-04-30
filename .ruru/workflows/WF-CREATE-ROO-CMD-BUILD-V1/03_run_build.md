+++
# --- Step Metadata ---
step_id = "WF-CREATE-ROO-CMD-BUILD-V1-03-RUN-BUILD" # (String, Required) Unique ID for this step.
title = "Step 03: Run Build Command" # (String, Required) Title of this specific step.
description = """
(String, Required) Executes the primary build command(s) for Roo Commander
within the prepared environment. Captures logs and checks for success.
"""

# --- Flow Control ---
depends_on = ["WF-CREATE-ROO-CMD-BUILD-V1-02-SETUP-ENVIRONMENT"] # (Array of Strings, Required) step_ids this step needs completed first.
next_step = "04_package_artifacts.md" # (String, Optional) Filename of the next step on successful completion.
error_step = "EE_handle_build_error.md" # (String, Optional) Filename to jump to if this step fails.

# --- Execution ---
delegate_to = "lead-devops" # (String, Optional) Mode responsible for executing the core logic of this step.

# --- Interface ---
inputs = [ # (Array of Strings, Optional) Data/artifacts needed. Can reference outputs from 'depends_on' steps.
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-01-VALIDATE-PARAMS: validated_build_params",
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-02-SETUP-ENVIRONMENT: build_directory_path",
]
outputs = [ # (Array of Strings, Optional) Data/artifacts produced by this step.
    "build_log: Path to the build output log.",
    "build_status: Success or Failure.",
    "raw_artifacts_path: Path to the directory containing raw build output.",
]

# --- Housekeeping ---
last_updated = "{{DATE}}" # (String, Required) Date of last modification. Use placeholder.
template_schema_doc = ".ruru/templates/toml-md/25_workflow_step_standard.md" # (String, Required) Link to this template definition.
+++

# Step 03: Run Build Command

## Actions

1.  **Receive Context:** Get `validated_build_params` and `build_directory_path` from previous steps.
2.  **Navigate to Build Directory:** Change the working directory to `build_directory_path`.
3.  **Execute Build:** Run the appropriate build command (e.g., `npm run build`, `make`, `go build`) using the validated parameters. Redirect output to a log file.
4.  **Check Exit Code:** Verify the build command completed successfully (typically exit code 0).
5.  **Prepare Output:** Provide the path to the build log, the build status, and the location of raw artifacts.

## Acceptance Criteria

*   Build command is executed in the correct directory.
*   Build command completes.
*   Exit code is checked and `build_status` is set accordingly.
*   `build_log` path is generated.
*   `raw_artifacts_path` is identified.

## Error Handling

*   If the build command fails (non-zero exit code), set `build_status` to Failure and proceed to `EE_handle_build_error.md` (if defined).