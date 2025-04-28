+++
# --- Basic Metadata ---
id = "WF-CREATE-ROO-CMD-BUILD-001"
title = "Workflow: Create Roo Commander Distribution Builds" # Changed
status = "active"
created_date = "2025-04-20"
updated_date = "2025-04-28" # Update date
version = "2.0" # Incremented
tags = ["workflow", "build", "distribution", "temporary", "release", "archive", "zip", "roo-commander"] # Updated

# --- Ownership & Context ---
owner = "Roo Commander"
related_docs = [
  "scripts/create_build.js",
  "scripts/create_kilocode_build.js",
  "scripts/run_collection_builds.js"
]
related_templates = []

# --- Workflow Specific Fields ---
objective = "Creates various Roo Commander distribution builds (Complete, Kilocode, Collections) safely within temporary directories, verifying output before cleanup." # Changed
scope = "Applies when generating distributable builds without modifying the main workspace or creating official releases." # Changed
roles = [
  "Coordinator (Roo Commander)",
  "Executor (Terminal via `execute_command`)"
] # Simplified
trigger = "Manual initiation by the Coordinator when temporary builds are required." # Changed
success_criteria = [
  "Temporary directories (`./tmp_build`, `./tmp_kilocode`, `./tmp_collections`) are created successfully.",
  "The `create_build.js` script executes successfully, placing output in `./tmp_build/`.",
  "The `create_kilocode_build.js` script executes successfully, placing output in `./tmp_kilocode/`.",
  "The `run_collection_builds.js` script executes successfully, placing output in `./tmp_collections/`.",
  "Expected build artifacts are verified to exist within the temporary directories.",
  "Temporary directories are successfully removed after verification."
] # Changed
failure_criteria = [
  "Failed to create temporary directories.",
  "Any build script fails or produces errors.",
  "Build artifacts are not found in the expected temporary directories during verification.",
  "Failed to remove temporary directories during cleanup."
] # Changed

# --- Integration ---
acqa_applicable = false
pal_validated = false
validation_notes = "Workflow needs testing with build scripts modified/confirmed to support output directories." # Updated

# --- AI Interaction Hints (Optional) ---
# context_type = "workflow_definition"
+++

# Workflow: Create Roo Commander Distribution Builds

## 1. Objective 🎯
*   To create various Roo Commander distribution builds (Complete, Kilocode, Collections) in isolated temporary directories.
*   To ensure build processes do not modify the main workspace.
*   To verify the presence of build artifacts before cleaning up temporary files.

## 2. Scope ↔️
*   This workflow is triggered manually when temporary, isolated builds are needed (e.g., for testing, previews). It does *not* create official releases or modify the Git history.

## 3. Roles & Responsibilities 👤
*   **Coordinator (Roo Commander):** Initiates the workflow, executes commands via the Executor.
*   **Executor (Terminal):** Runs the directory creation, build script, verification, and cleanup commands provided by the Coordinator.

## 4. Preconditions🚦
*   Necessary tools (`node`, standard shell commands like `mkdir`, `ls`, `rm`) are available.
*   Build scripts (`scripts/create_build.js`, `scripts/create_kilocode_build.js`, `scripts/run_collection_builds.js`) exist and are functional.
*   *(Assumption)* Build scripts accept an output directory argument (e.g., `--output <path>`) or reliably place output in a predictable location relative to execution.

## 5. Reference Documents & Tools 📚🛠️
*   `scripts/create_build.js`
*   `scripts/create_kilocode_build.js`
*   `scripts/run_collection_builds.js`
*   `execute_command`: Tool to run shell commands and Node.js scripts.
*   `list_files` (Optional): Alternative tool for verification.

## 6. Workflow Steps 🪜

*   **Step 1: Setup Temporary Directories (Coordinator delegates to Executor via `execute_command`)**
    *   **Description:** Create the temporary directories for the builds.
    *   **Tool:** `execute_command`
    *   **Command Example (Linux/macOS):** `mkdir -p ./tmp_build ./tmp_kilocode ./tmp_collections`
    *   **Validation:** Check for exit code 0.
    *   **Error Handling:** If creation fails, check permissions. Report failure.

*   **Step 2: Execute Complete Build (Coordinator delegates to Executor via `execute_command`)**
    *   **Description:** Run the script to create the complete build in its temporary directory.
    *   **Tool:** `execute_command`
    *   **Command Example:** `node scripts/create_build.js --output ./tmp_build/` (Note: Adjust command based on actual script arguments if `--output` is not supported)
    *   **Validation:** Check for exit code 0 and success messages from the script.
    *   **Error Handling:** If the script fails, analyze its output. Check dependencies, paths. Report failure.

*   **Step 3: Execute Kilocode Build (Coordinator delegates to Executor via `execute_command`)**
    *   **Description:** Run the script to create the Kilocode build in its temporary directory.
    *   **Tool:** `execute_command`
    *   **Command Example:** `node scripts/create_kilocode_build.js --output ./tmp_kilocode/` (Note: Adjust command based on actual script arguments if `--output` is not supported)
    *   **Validation:** Check for exit code 0 and success messages from the script.
    *   **Error Handling:** If the script fails, analyze its output. Check dependencies, paths. Report failure.

*   **Step 4: Execute Collection Builds (Coordinator delegates to Executor via `execute_command`)**
    *   **Description:** Run the script to create the collection builds in their temporary directory.
    *   **Tool:** `execute_command`
    *   **Command Example:** `node scripts/run_collection_builds.js --output ./tmp_collections/` (Note: Adjust command based on actual script arguments if `--output` is not supported)
    *   **Validation:** Check for exit code 0 and success messages from the script.
    *   **Error Handling:** If the script fails, analyze its output. Check dependencies, paths. Report failure.

*   **Step 5: Verify Build Artifacts (Coordinator delegates to Executor via `execute_command`)**
    *   **Description:** Check if the expected primary build artifacts exist in the temporary directories. This step is crucial before cleanup.
    *   **Tool:** `execute_command`
    *   **Command Example (Linux/macOS using `ls`):**
        ```bash
        echo "Verifying builds..." && \
        ls ./tmp_build/*.zip && \
        ls ./tmp_kilocode/*.zip && \
        ls ./tmp_collections/*.zip && \
        echo "Verification successful."
        # Adjust *.zip patterns based on actual expected output filenames/types if needed.
        ```
    *   **Alternative Command (Linux/macOS using `test`):**
        ```bash
        echo "Verifying builds..." && \
        test -f ./tmp_build/expected_complete.zip && \
        test -f ./tmp_kilocode/expected_kilocode.zip && \
        test -f ./tmp_collections/expected_collection1.zip && \
        echo "Verification successful."
        # Add more specific 'test -f' checks for key files as needed.
        ```
    *   **Validation:** Check for exit code 0 (indicates all commands succeeded). Non-zero indicates failure. Review output for specific errors (e.g., "No such file or directory").
    *   **Error Handling:** If verification fails, report which artifacts appear missing based on the command output. **Crucially, do not proceed to the cleanup step.**

*   **Step 6: Cleanup Temporary Directories (Coordinator delegates to Executor via `execute_command`)**
    *   **Description:** Remove the temporary directories *only if* verification in Step 5 was successful.
    *   **Tool:** `execute_command`
    *   **Command Example (Linux/macOS):** `rm -rf ./tmp_build ./tmp_kilocode ./tmp_collections`
    *   **Validation:** Check for exit code 0.
    *   **Error Handling:** If cleanup fails, check permissions or if files are locked. Report failure.

## 7. Postconditions ✅
*   Build artifacts were successfully generated in temporary directories (and subsequently removed after successful verification).
*   The main workspace directory remains unmodified by the build process.

## 8. Error Handling & Escalation (Overall) ⚠️
*   If directory creation fails, check permissions.
*   If any build script fails, analyze its output. Check script dependencies and paths.
*   If verification fails, investigate the relevant build script's execution and output. **Do not clean up temporary directories.** Report the failure.
*   If cleanup fails (after successful verification), check permissions or if files are locked. Report the issue.
*   Escalate to the user if steps fail and cannot be resolved.

## 9. PAL Validation Record 🧪
*   (Details omitted as per revision focus)

## 10. Revision History 📜
*   v2.0 (2025-04-28): Refocused workflow on creating builds in temporary directories only. Removed Git, GitHub release, CHANGELOG, and build log steps. Added setup, verification, and cleanup steps for temporary directories. Updated metadata, objective, scope, roles, criteria, and descriptions accordingly.
*   v1.2 (2025-04-21): Inserted Git add, commit, push steps (5-7) before build (8) and release (9). Moved build log update to Step 4. Renumbered steps accordingly. Added `git` to tools list and updated descriptions/examples. Corrected build script example command and archive name format. Updated objective, preconditions, and postconditions.
*   v1.1 (2025-04-20): Added Step 6 for GitHub Release creation using `gh` CLI. Updated roles, criteria, and tools list.
*   v1.0 (2025-04-20): Initial draft incorporating versioning, build log, CHANGELOG, distribution README, and suggestion for an automated build script.