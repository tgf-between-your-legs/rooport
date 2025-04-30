+++
# --- Step Metadata ---
step_id = "WF-CREATE-ROO-CMD-BUILD-V1-04-PACKAGE-ARTIFACTS" # (String, Required) Unique ID for this step.
title = "Step 04: Package Build Artifacts" # (String, Required) Title of this specific step.
description = """
(String, Required) Packages the raw build artifacts generated in the previous step
into a distributable format (e.g., zip, tar.gz, installer).
"""

# --- Flow Control ---
depends_on = ["WF-CREATE-ROO-CMD-BUILD-V1-03-RUN-BUILD"] # (Array of Strings, Required) step_ids this step needs completed first.
next_step = "99_finish.md" # (String, Optional) Filename of the next step on successful completion.
error_step = "EE_handle_packaging_error.md" # (String, Optional) Filename to jump to if this step fails.

# --- Execution ---
delegate_to = "lead-devops" # (String, Optional) Mode responsible for executing the core logic of this step.

# --- Interface ---
inputs = [ # (Array of Strings, Optional) Data/artifacts needed. Can reference outputs from 'depends_on' steps.
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-03-RUN-BUILD: raw_artifacts_path",
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-01-VALIDATE-PARAMS: validated_build_params", # Needed for naming conventions etc.
]
outputs = [ # (Array of Strings, Optional) Data/artifacts produced by this step.
    "packaged_artifact_path: Path to the final packaged artifact.",
    "packaging_log: Path to the packaging log file.",
]

# --- Housekeeping ---
last_updated = "{{DATE}}" # (String, Required) Date of last modification. Use placeholder.
template_schema_doc = ".ruru/templates/toml-md/25_workflow_step_standard.md" # (String, Required) Link to this template definition.
+++

# Step 04: Package Build Artifacts

## Actions

1.  **Receive Context:** Get `raw_artifacts_path` and `validated_build_params` from previous steps.
2.  **Create Package:** Use appropriate tools (e.g., `zip`, `tar`, installer creator) to package the contents of `raw_artifacts_path`. Use version/platform info from `validated_build_params` for naming.
3.  **Log Packaging:** Capture the output of the packaging process to a log file.
4.  **Verify Package:** Perform a basic check to ensure the package file exists and is not empty.
5.  **Prepare Output:** Provide the path to the final `packaged_artifact_path` and the `packaging_log`.

## Acceptance Criteria

*   Raw artifacts are correctly packaged based on parameters.
*   Packaging process is logged.
*   Final package file exists and is accessible.
*   `packaged_artifact_path` and `packaging_log` are provided.

## Error Handling

*   If packaging commands fail or the final package is invalid, proceed to `EE_handle_packaging_error.md` (if defined).