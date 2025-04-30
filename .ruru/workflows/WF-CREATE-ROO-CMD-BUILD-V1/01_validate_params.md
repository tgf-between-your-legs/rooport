+++
# --- Step Metadata ---
step_id = "WF-CREATE-ROO-CMD-BUILD-V1-01-VALIDATE-PARAMS" # (String, Required) Unique ID for this step.
title = "Step 01: Validate Build Parameters" # (String, Required) Title of this specific step.
description = """
(String, Required) Performs detailed validation on the build parameters received from the start step.
Checks for valid version format, recognized target platforms, etc.
"""

# --- Flow Control ---
depends_on = ["WF-CREATE-ROO-CMD-BUILD-V1-00-START"] # (Array of Strings, Required) step_ids this step needs completed first.
next_step = "02_setup_environment.md" # (String, Optional) Filename of the next step on successful completion.
error_step = "EE_handle_validation_error.md" # (String, Optional) Filename to jump to if this step fails.

# --- Execution ---
delegate_to = "lead-devops" # (String, Optional) Mode responsible for executing the core logic of this step.

# --- Interface ---
inputs = [ # (Array of Strings, Optional) Data/artifacts needed. Can reference outputs from 'depends_on' steps.
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-00-START: build_params",
]
outputs = [ # (Array of Strings, Optional) Data/artifacts produced by this step.
    "validated_build_params: The validated build parameters object.",
]

# --- Housekeeping ---
last_updated = "{{DATE}}" # (String, Required) Date of last modification. Use placeholder.
template_schema_doc = ".ruru/templates/toml-md/25_workflow_step_standard.md" # (String, Required) Link to this template definition.
+++

# Step 01: Validate Build Parameters

## Actions

1.  **Receive Parameters:** Get the `build_params` object from the previous step's output.
2.  **Validate Version:** Check if the version string follows semantic versioning rules.
3.  **Validate Platform:** Ensure the target platform(s) are supported/recognized.
4.  **Validate Flags:** Check any additional build flags for validity.
5.  **Prepare Output:** Structure the validated parameters into `validated_build_params`.

## Acceptance Criteria

*   `build_params` are received successfully.
*   Version, platform, and flags are confirmed as valid.
*   `validated_build_params` object is created for the next step.

## Error Handling

*   If any validation check fails (invalid version, unsupported platform, etc.), proceed to `EE_handle_validation_error.md` (if defined).