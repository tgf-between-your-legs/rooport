+++
# --- Step Metadata ---
step_id = "WF-CREATE-ROO-CMD-BUILD-V1-03-RUN-BUILDS" # (String, Required) Unique ID for this step.
title = "Step 03: Run Build Scripts" # (String, Required) Title of this specific step.
description = """
(String, Required) Executes the three primary build scripts (`create_build.js`,
`create_kilocode_build.js`, `run_collection_builds.js`) for Roo Commander
within the prepared environment. Captures logs and checks for success of each.
"""

# --- Flow Control ---
depends_on = ["WF-CREATE-ROO-CMD-BUILD-V1-02-SETUP-ENVIRONMENT"] # (Array of Strings, Required) step_ids this step needs completed first.
next_step = "04_verify_artifacts.md" # (String, Optional) Filename of the next step on successful completion.
error_step = "EE_handle_build_error.md" # (String, Optional) Filename to jump to if this step fails.

# --- Execution ---
delegate_to = "lead-devops" # (String, Optional) Mode responsible for executing the core logic of this step.

# --- Interface ---
inputs = [ # (Array of Strings, Optional) Data/artifacts needed. Can reference outputs from 'depends_on' steps.
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-01-VALIDATE-PARAMS: validated_build_params",
    "Output from step WF-CREATE-ROO-CMD-BUILD-V1-02-SETUP-ENVIRONMENT: build_directory_path",
]
outputs = [ # (Array of Strings, Optional) Data/artifacts produced by this step.
    "build_logs: Paths to the build output logs for each script.",
    "build_status: Success or Failure (overall).",
    "raw_artifacts_path: Path to the directory containing raw build output.",
]

# --- Housekeeping ---
last_updated = "{{DATE}}" # (String, Required) Date of last modification. Use placeholder.
template_schema_doc = ".ruru/templates/toml-md/25_workflow_step_standard.md" # (String, Required) Link to this template definition.
+++

# Step 03: Run Build Scripts

## Actions

1.  **Receive Context:** Get `validated_build_params` and `build_directory_path` from previous steps.
2.  **Navigate to Build Directory:** Change the working directory to `build_directory_path`.
3.  **Execute Build Script 1 (`create_build.js`):** Run `node scripts/create_build.js`. Redirect output to a log file (e.g., `build_main.log`). Check exit code.
4.  **Execute Build Script 2 (`create_kilocode_build.js`):** Run `node scripts/create_kilocode_build.js`. Redirect output to a log file (e.g., `build_kilocode.log`). Check exit code.
5.  **Execute Build Script 3 (`run_collection_builds.js`):** Run `node scripts/run_collection_builds.js`. Redirect output to a log file (e.g., `build_collections.log`). Check exit code.
6.  **Check Overall Success:** Determine overall `build_status` based on the success of all three scripts.
7.  **Prepare Output:** Provide the paths to the build logs, the overall build status, and the location of raw artifacts.

## Acceptance Criteria

*   All three build scripts are executed in the correct directory.
*   Each build script completes.
*   Exit codes for each script are checked.
*   Overall `build_status` is set correctly (Success only if all scripts succeed).
*   `build_logs` paths are generated.
*   `raw_artifacts_path` is identified.

## Error Handling

*   If any build script fails (non-zero exit code), set overall `build_status` to Failure and proceed to `EE_handle_build_error.md` (if defined).