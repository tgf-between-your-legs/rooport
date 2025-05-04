+++
# --- Basic Metadata ---
id = "SOP-REPOMIX-GITHUB-V1.1" # Incremented version
title = "SOP: Repomix GitHub Source Processing (Repo & Subfolder)"
status = "active" # Changed from draft after review
created_date = "2025-05-03" # Placeholder, use actual date
updated_date = "2025-05-10" # Placeholder, use actual revision date
version = "1.1" # Incremented version
tags = ["sop", "workflow", "repomix", "github", "spec-repomix", "error-handling"] # Added tag
template_schema_doc = ".ruru/templates/toml-md/15_sop.README.md" # Link to schema documentation

# --- Ownership & Context ---
# author = "Prime Coordinator"
owner = "Roo Commander"
related_docs = [
    ".roo/rules-spec-repomix/02-repomix-decision-tree.md",
    ".ruru/modes/spec-repomix/kb/01-repomix-usage-corrections.md",
    ".roo/rules/05-os-aware-commands.md"
    ]
# related_tasks = []

# --- SOP Specific Fields ---
objective = "To define the standard procedure for the `spec-repomix` mode to process GitHub URL sources (both full repositories and specific subfolders) reliably using the `repomix` tool via a temporary configuration file, ensuring correct sequencing and preventing unsafe fallback actions." # Refined objective
scope = "This SOP applies exclusively when the `spec-repomix` mode identifies the input source as a GitHub URL. It covers URL parsing, prerequisite checks, repository cloning, conditional configuration generation based on URL type (repo vs. subfolder) using the clone path, execution strictly via `repomix --config`, robust error handling, and cleanup." # Refined scope
roles = ["spec-repomix"]

# --- AI Interaction Hints (Optional) ---
# context_type = "process_definition"
# target_audience = ["spec-repomix"]
# granularity = "detailed"
+++

# SOP: Repomix GitHub Source Processing (Repo & Subfolder)

## 1. Objective 🎯

*   To standardize the process for `spec-repomix` to handle GitHub repository URLs, correctly identifying and processing either the entire repository or specific subfolders within it, using the `repomix --config` method **reliably and safely**.
*   To ensure the repository is cloned *before* the configuration file referencing it is generated.
*   To explicitly prevent fallback execution modes (e.g., `repomix .`) if the primary configuration-based execution fails.

## 2. Scope Boundaries ↔️

*   **In Scope:** Processing `https://github.com/...` URLs provided as input to `spec-repomix`. Prerequisite tool checks (`git`, `repomix`). Differentiating between full repository URLs and subfolder URLs (containing `/tree/branch/...`). Cloning the repository to a temporary location. Generating a temporary `repomix.config.json` referencing the *local clone path*. Executing `repomix` **only** via the `--config` flag pointing to this temporary file. Generating `repomix` outputs (e.g., XML, Markdown). Handling specific errors related to this workflow. Cleaning up temporary resources.
*   **Out of Scope:** Processing local filesystem paths (covered by `SOP-REPOMIX-LOCAL-V1.md`). Processing non-GitHub URLs. Complex `repomix` configuration options beyond basic source (fixed to local clone), output, and include/exclude filters derived from the URL or user request. Direct execution of `repomix` with CLI arguments for sources/filters (e.g., `repomix <path>`). Automatic handling of private repositories requiring authentication (cloning is expected to fail unless credentials are pre-configured in the environment). Fallback execution attempts if `repomix --config` fails.

## 3. Roles & Responsibilities 👤

*   **`spec-repomix`:**
    *   Verify prerequisites (`git`, `repomix` commands available).
    *   Parse the input GitHub URL.
    *   Clone the repository to a unique temporary location.
    *   **Verify clone success before proceeding.**
    *   Determine if the target is the full repo or specific subfolder(s) based on the URL.
    *   Generate the `repomix.config.json` content, **critically using the temporary clone path**.
    *   Write the config to a temporary file.
    *   **Verify config write success.**
    *   Ensure output directories exist.
    *   Execute `repomix --config` using the temporary config file. **No other `repomix` execution methods should be attempted within this SOP.**
    *   Handle results and errors according to this SOP, reporting failures clearly.
    *   Perform cleanup of temporary files and directories.

## 4. Reference Documents 📚

*   `spec-repomix` Mode Definition (`.roomodes`)
*   Rule: Repomix Source Identification & Config Workflow (`.roo/rules-spec-repomix/02-repomix-decision-tree.md`)
*   KB: Repomix Usage Corrections (`.ruru/modes/spec-repomix/kb/01-repomix-usage-corrections.md`)
*   Rule: Generate OS-Aware Commands (`.roo/rules/05-os-aware-commands.md`)
*   `git` command documentation (`git clone --help`)
*   `repomix` tool documentation (`repomix --help`, if available)

## 5. Procedure Steps 🪜

**Step 0: Prerequisite Check (`spec-repomix`)**
1.  **Action:** Verify that the necessary command-line tools (`git`, `repomix`) are available in the execution environment's PATH.
2.  **Inputs:** N/A.
3.  **Tools:** `execute_command` (e.g., `git --version`, `repomix --version` or `repomix --help`).
4.  **Context:** OS type.
5.  **Outputs:** Confirmation of tool availability.
6.  **Decision:** If `git` or `repomix` is not found, report error "Prerequisite tool missing: [tool_name]" and stop.

**Step 1: Parse Input URL (`spec-repomix`)**
1.  **Action:** Analyze the provided GitHub URL string.
2.  **Inputs:** GitHub URL string (e.g., `https://github.com/owner/repo`, `https://github.com/owner/repo/tree/main/path/to/folder`).
3.  **Tools:** Internal logic/parsing library.
4.  **Context:** N/A.
5.  **Outputs:** Parsed components: `repo_url` (base clone URL like `https://github.com/owner/repo.git`), `branch` (if specified, e.g., `main`, otherwise default branch will be cloned), `subfolder_path` (relative path within repo, e.g., `path/to/folder`, or `null` if none).
6.  **Decision:** If URL is not a valid GitHub URL format, report error "Invalid GitHub URL format" and stop. If `subfolder_path` is present, note it's a subfolder request. Otherwise, it's a full repo request.

**Step 2: Clone Repository (`spec-repomix`)**
1.  **Action:** Clone the identified repository to a unique temporary local directory. Use shallow clone (`--depth 1`) for efficiency unless full history is explicitly needed (outside standard scope). If a specific branch was identified in the URL, clone that branch.
2.  **Inputs:** `repo_url`, `branch` (optional) from Step 1.
3.  **Tools:** `execute_command`.
4.  **Context:** OS type (for command syntax and temporary directory path generation).
5.  **Outputs:** Path to the temporary local clone (`temp_clone_path`, e.g., `.ruru/temp/repomix_clone_[timestamp_uuid]/repo_name`). Exit code and stderr/stdout from the `git clone` command.
    *   Example Command (adjust for OS/quoting):
        ```bash
        # Define unique temp_clone_path
        TEMP_CLONE_PATH=".ruru/temp/repomix_clone_$(date +%s)_$RANDOM/myrepo" 
        mkdir -p $(dirname "$TEMP_CLONE_PATH") # Ensure parent temp dir exists
        # Basic clone:
        # git clone --depth 1 [repo_url] "$TEMP_CLONE_PATH"
        # Clone specific branch:
        # git clone --depth 1 --branch [branch] [repo_url] "$TEMP_CLONE_PATH" 
        ```
6.  **Decision:** **CRITICAL:** Check the exit code of `git clone`. If clone fails (non-zero exit code), report error "Git clone failed for [repo_url]" including relevant `git` command output (stderr) and **stop**. Do *not* proceed to configuration generation. If successful, store `temp_clone_path` for the next step.

**Step 3: Generate Configuration JSON (`spec-repomix`)**
1.  **Action:** Construct the JSON object for the `repomix.config.json` file. **This step depends entirely on the successful completion of Step 2 and the availability of `temp_clone_path`.**
2.  **Inputs:** `repo_url`, `subfolder_path` (if any) from Step 1, **`temp_clone_path` (validated output from Step 2)**, user-requested parameters (e.g., output style, specific includes/excludes beyond the subfolder).
3.  **Tools:** Internal logic (JSON object construction).
4.  **Context:** N/A.
5.  **Outputs:** JSON configuration object (`config_json`).
    *   **`sources` Array:** MUST contain exactly one object pointing to the local clone:
        ```json
        {
          "type": "local", // CRITICAL: Always use "local" type
          "path": "[temp_clone_path]" // CRITICAL: Use the actual path from Step 2
        }
        ```
    *   **`include` Array (Conditional):**
        *   If `subfolder_path` **is present** (from Step 1): Add `"[subfolder_path]/**"` to the `include` array. Example: `"include": ["path/to/folder/**"]`. *Note: Consider adding a check here or in Step 5/6 to verify if `[temp_clone_path]/[subfolder_path]` actually exists, reporting a warning or error if not.*
        *   If `subfolder_path` **is null**: Do not add a subfolder-specific `include` pattern by default (process entire cloned repo).
    *   **`output` Object:** Define `path`, `format`, and `style` as requested (generating absolute or relative paths for outputs, e.g., `.ruru/repomix/[repo_name]/output.md`). Ensure output paths are well-defined.
    *   **Other Fields:** Add `exclude`, `filters` (like `useGitignore`, `useDefaultPatterns`), etc., based on user request, ensuring they are compatible with the `repomix` config schema.
6.  **Decision:** N/A (Proceed to next step with the generated `config_json`).

**Step 4: Write Configuration File (`spec-repomix`)**
1.  **Action:** Write the generated `config_json` object to a temporary file.
2.  **Inputs:** `config_json` from Step 3.
3.  **Tools:** `write_to_file`.
4.  **Context:** OS type (for temporary file path generation).
5.  **Outputs:** Path to the temporary config file (`temp_config_path`, e.g., `.ruru/temp/repomix_config_[timestamp_uuid].json`). Result status of `write_to_file`.
6.  **Decision:** Check the result of the file write operation. If write fails, report error "Failed to write temporary config file to [temp_config_path]" including any OS error, perform cleanup (Step 7), and stop.

**Step 5: Execute Repomix (`spec-repomix`)**
1.  **Action:** Run the `repomix` command **strictly using the `--config` option** pointing to the temporary configuration file. Ensure output directories specified within the config file exist *before* execution.
2.  **Inputs:** `temp_config_path` from Step 4. Output paths defined within the config (needed for `mkdir`).
3.  **Tools:** `execute_command`.
4.  **Context:** OS type (for `mkdir` and `repomix` command syntax).
5.  **Outputs:** Exit code, stdout, and stderr from the `repomix` command. Repomix output file(s) at the location(s) specified in the config.
    *   Example Command (adjust for OS/quoting):
        ```bash
        # Extract output directories from config_json if needed, e.g., OUT_DIR_MD, OUT_DIR_XML
        mkdir -p "$OUT_DIR_MD" # Check exit code
        mkdir -p "$OUT_DIR_XML" # Check exit code
        # Execute repomix ONLY with --config
        repomix --config "$TEMP_CONFIG_PATH" 
        ```
6.  **Decision:** Check the exit code(s) of `mkdir`. If directory creation fails, report error "Failed to create output directory [dir_path]", perform cleanup (Step 7), and stop. Proceed to Step 6 (Result Handling) to analyze the `repomix` command's result.

**Step 6: Result Handling (`spec-repomix`)**
1.  **Action:** Analyze the exit code and output (stderr) of the `repomix --config` command executed in Step 5.
2.  **Inputs:** Exit code, stdout, stderr from Step 5.
3.  **Tools:** Internal logic.
4.  **Context:** KB `.ruru/modes/spec-repomix/kb/01-repomix-usage-corrections.md`.
5.  **Outputs:** Success or failure status, relevant messages (including `repomix` stderr on failure).
6.  **Decision:**
    *   **If Exit Code is 0:** The command succeeded. Proceed to Step 7 (Cleanup).
    *   **If Exit Code is non-zero:** The `repomix --config` command failed.
        *   **CRITICAL:** **DO NOT attempt any alternative `repomix` execution (e.g., `repomix .`). This is an explicit failure condition.**
        *   Analyze stderr from `repomix`. Consult the KB for known error patterns (e.g., config syntax error, path not found within clone, filter issues).
        *   If the error suggests a *correctable configuration issue* (e.g., typo in generated config, non-existent subfolder path that should be handled gracefully), and a retry mechanism is deemed appropriate *for specific, known errors only*:
            *   Optionally, attempt to regenerate the config (Step 3) with corrections and retry Steps 4-5 **once**. Log this retry attempt clearly.
            *   If retry fails or is not applicable, proceed as below.
        *   Report failure: "Repomix execution failed with exit code [exit_code]" including the full `repomix` stderr.
        *   Proceed to Step 7 (Cleanup).

**Step 7: Cleanup (`spec-repomix`)**
1.  **Action:** Remove the temporary configuration file and the temporary cloned repository directory, regardless of success or failure in previous steps (ensure this step runs reliably).
2.  **Inputs:** `temp_config_path` from Step 4, `temp_clone_path` from Step 2.
3.  **Tools:** `execute_command`.
4.  **Context:** OS type (for `rm -f` or `Remove-Item -Force` for the file, and `rm -rf` or `Remove-Item -Recurse -Force` for the directory).
5.  **Outputs:** Exit code/output from cleanup commands.
6.  **Decision:** Log cleanup success or failure. If cleanup fails, log a warning "Failed to clean up temporary resource: [path]" including OS error (this is usually non-critical for the primary task outcome but should be noted). Report the final outcome (Success or Failure determined in Step 6) to the coordinator using `attempt_completion`.

## 6. Error Handling & Escalation ⚠️

*   **Prerequisite Failure:** (`git` or `repomix` not found): Report specific missing tool. Stop.
*   **URL Parsing Failure:** Report "Invalid GitHub URL format". Stop.
*   **Git Clone Failure:** Report "Git clone failed for [repo_url]" with `git` stderr. Stop. (Common causes: invalid URL, non-existent repo/branch, network issue, permissions/authentication required for private repo).
*   **Config Write Failure:** Report "Failed to write temporary config file" with OS error. Cleanup and stop.
*   **Output Directory Creation Failure:** Report "Failed to create output directory [dir_path]" with OS error. Cleanup and stop.
*   **Repomix Execution Failure (`repomix --config`):**
    *   **Explicit Rule:** **Never fall back to `repomix .` or any other execution form.**
    *   Report "Repomix execution failed" with exit code and full `repomix` stderr.
    *   Consult KB `01-repomix-usage-corrections.md` for diagnosis.
    *   Retry (Steps 3-5) **only once** if a specific, known, correctable config error is identified. Log the attempt.
    *   If retry is not applicable or fails, report the persistent error. Proceed to cleanup.
*   **Non-Existent Subfolder:** If a subfolder URL is provided but the path doesn't exist in the cloned repo, `repomix` (via the `include` filter) might process nothing or error. The error handling in Step 6 should catch this. Consider adding an explicit check after clone or making the error message clearer if `repomix` fails due to this.
*   **Cleanup Failure:** Log warning "Failed to clean up temporary resource: [path]" with OS error. Report original task outcome.
*   **Escalation:** For persistent, unresolvable, or unexpected errors not covered by the KB, escalate detailed failure information (input URL, temporary config content, `repomix` stderr, environment details) to the delegating coordinator (`roo-commander` or `prime-coordinator`).

## 7. Validation (PAL) ✅

*   This SOP should be reviewed and validated according to the standard PAL process.
*   Test cases:
    *   Valid public GitHub repo URL (full repo).
    *   Valid public GitHub repo URL (single existing subfolder).
    *   Valid public GitHub repo URL (specific existing branch).
    *   Invalid GitHub URL format.
    *   URL pointing to a non-existent repository.
    *   URL pointing to a non-existent branch.
    *   URL pointing to a non-existent subfolder within an existing repo/branch.
    *   Repo requiring authentication (expected to fail at clone step).
    *   Request with additional valid `repomix` include/exclude filters.
    *   Simulate failure during `git clone`.
    *   Simulate failure during `repomix --config` execution (e.g., invalid config syntax, invalid filter). Verify **no fallback** occurs.
    *   Simulate failure during temporary file writing.
    *   Simulate failure during output directory creation.

## 8. Revision History Memento 📜 (Optional)

*   **v1.1 (2025-05-10):** Revised by AI Assistant. Strengthened error handling, added prerequisite checks, explicitly prohibited fallback execution on `repomix --config` failure, clarified step dependencies (clone before config gen), added detail to commands, refined validation cases. Addressed reported failure mode.
*   **v1.0 (2025-05-03):** Initial draft based on discussion to handle GitHub repos/subfolders via config file and include filters.