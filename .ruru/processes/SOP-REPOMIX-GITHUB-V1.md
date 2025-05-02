+++
# --- Basic Metadata ---
id = "SOP-REPOMIX-GITHUB-V1"
title = "SOP: Repomix GitHub Source Processing (Repo & Subfolder)"
status = "draft"
created_date = "2025-05-03" # Placeholder, use actual date
updated_date = "2025-05-03" # Placeholder, use actual date
version = "1.0"
tags = ["sop", "workflow", "repomix", "github", "spec-repomix"]
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
objective = "To define the standard procedure for the `spec-repomix` mode to process GitHub URL sources (both full repositories and specific subfolders) using the `repomix` tool via a configuration file."
scope = "This SOP applies exclusively when the `spec-repomix` mode identifies the input source as a GitHub URL. It covers URL parsing, cloning, conditional configuration generation based on URL type (repo vs. subfolder), execution via `--config`, and cleanup."
roles = ["spec-repomix"]

# --- AI Interaction Hints (Optional) ---
# context_type = "process_definition"
# target_audience = ["spec-repomix"]
# granularity = "detailed"
+++

# SOP: Repomix GitHub Source Processing (Repo & Subfolder)

## 1. Objective 🎯

*   To standardize the process for `spec-repomix` to handle GitHub repository URLs, correctly identifying and processing either the entire repository or specific subfolders within it, using the `repomix --config` method.

## 2. Scope Boundaries ↔️

*   **In Scope:** Processing `https://github.com/...` URLs provided as input to `spec-repomix`. Differentiating between full repository URLs and subfolder URLs (containing `/tree/branch/...`). Generating `repomix` outputs (XML and Markdown) via a temporary configuration file.
*   **Out of Scope:** Processing local filesystem paths (covered by `SOP-REPOMIX-LOCAL-V1.md`). Processing non-GitHub URLs. Complex `repomix` configuration options beyond basic source, output, and include/exclude filters defined here. Direct execution of `repomix` with CLI arguments for sources/filters.

## 3. Roles & Responsibilities 👤

*   **`spec-repomix`:**
    *   Parse the input GitHub URL.
    *   Clone the repository to a temporary location.
    *   Determine if the target is the full repo or specific subfolder(s).
    *   Generate the appropriate `repomix.config.json` content.
    *   Write the config to a temporary file.
    *   Execute `repomix --config`.
    *   Handle results and errors.
    *   Perform cleanup.

## 4. Reference Documents 📚

*   `spec-repomix` Mode Definition (`.roomodes`)
*   Rule: Repomix Source Identification & Config Workflow (`.roo/rules-spec-repomix/02-repomix-decision-tree.md`)
*   KB: Repomix Usage Corrections (`.ruru/modes/spec-repomix/kb/01-repomix-usage-corrections.md`)
*   Rule: Generate OS-Aware Commands (`.roo/rules/05-os-aware-commands.md`)
*   `repomix` tool documentation (if available externally/via help command).

## 5. Procedure Steps 🪜

**Step 1: Parse Input URL (`spec-repomix`)**
1.  **Action:** Analyze the provided GitHub URL string.
2.  **Inputs:** GitHub URL string (e.g., `https://github.com/owner/repo`, `https://github.com/owner/repo/tree/main/path/to/folder`).
3.  **Tools:** Internal logic/parsing.
4.  **Context:** N/A.
5.  **Outputs:** Parsed components: `repo_url` (base URL like `https://github.com/owner/repo`), `branch` (if specified, e.g., `main`), `subfolder_path` (relative path within repo, e.g., `path/to/folder`, or `null` if none).
6.  **Decision:** If URL is not a valid GitHub URL, report error and stop. If `subfolder_path` is present, note it's a subfolder request. Otherwise, it's a full repo request.

**Step 2: Clone Repository (`spec-repomix`)**
1.  **Action:** Clone the identified repository to a unique temporary local directory.
2.  **Inputs:** `repo_url` from Step 1.
3.  **Tools:** `execute_command`.
4.  **Context:** OS type (for command syntax).
5.  **Outputs:** Temporary local path (`temp_clone_path`, e.g., `.ruru/temp/repomix_clone_[timestamp]/repo_name`). Exit code/output from `git clone`.
6.  **Decision:** If clone fails (non-zero exit code), report error (including git output) and stop.

**Step 3: Generate Configuration JSON (`spec-repomix`)**
1.  **Action:** Construct the JSON object for the `repomix.config.json` file based on the original request and parsed URL.
2.  **Inputs:** `repo_url`, `subfolder_path` (if any) from Step 1, `temp_clone_path` from Step 2, user-requested parameters (e.g., output style, specific includes/excludes beyond the subfolder).
3.  **Tools:** Internal logic.
4.  **Context:** N/A.
5.  **Outputs:** JSON configuration object (`config_json`).
    *   **`sources` Array:** Always contains **one** object:
        ```json
        {
          "type": "local", // CRITICAL: Use "local" type as we are pointing to the temporary clone
          "path": "[temp_clone_path]" // Path to the root of the temporary clone
        }
        ```
    *   **`include` Array (Conditional):**
        *   If `subfolder_path` **is present** (from Step 1): Add `"[subfolder_path]/**"` to the `include` array. Example: `"include": ["path/to/folder/**"]`. If multiple subfolders were requested via separate URLs to the same repo, add multiple patterns.
        *   If `subfolder_path` **is null**: Do not add a subfolder-specific `include` pattern by default (unless other include filters were explicitly requested).
    *   **`output` Object:** Define `path`, `format`, and `style` as requested (generating paths for both XML and Markdown, e.g., `.ruru/repomix/[repo_name]/output.md`, `.ruru/repomix/[repo_name]/output.xml`). Ensure `style` is `"markdown"` or `"xml"`.
    *   **Other Fields:** Add `exclude`, `filters`, etc., as requested by the user.
6.  **Decision:** N/A.

**Step 4: Write Configuration File (`spec-repomix`)**
1.  **Action:** Write the generated JSON configuration to a temporary file.
2.  **Inputs:** `config_json` from Step 3.
3.  **Tools:** `write_to_file`.
4.  **Context:** N/A.
5.  **Outputs:** Temporary config file path (`temp_config_path`, e.g., `.ruru/temp/repomix_config_[timestamp].json`). Result of `write_to_file`.
6.  **Decision:** If write fails, report error and stop.

**Step 5: Execute Repomix (`spec-repomix`)**
1.  **Action:** Run the `repomix` command using the temporary configuration file. Ensure output directories exist.
2.  **Inputs:** `temp_config_path` from Step 4. Output paths defined within the config.
3.  **Tools:** `execute_command`.
4.  **Context:** OS type (for command syntax).
5.  **Outputs:** Exit code and output from `repomix` command. Repomix output file(s) at the specified location(s).
    *   Command: `mkdir -p [output_directory_for_md] && mkdir -p [output_directory_for_xml] && repomix --config [temp_config_path]` (adjust `mkdir` for OS).
6.  **Decision:** Proceed to Step 6 (Result Handling).

**Step 6: Result Handling (`spec-repomix`)**
1.  **Action:** Analyze the result of the `repomix` execution.
2.  **Inputs:** Exit code and output from Step 5.
3.  **Tools:** Internal logic.
4.  **Context:** KB `.ruru/modes/spec-repomix/kb/01-repomix-usage-corrections.md`.
5.  **Outputs:** Success or failure status, relevant messages.
6.  **Decision:** If Exit Code is 0, proceed to Step 7 (Cleanup). If non-zero, analyze error, consult KB, attempt correction (e.g., regenerate config if syntax error) and loop back to Step 4/5 if feasible, otherwise report failure and error details to coordinator and proceed to Step 7.

**Step 7: Cleanup (`spec-repomix`)**
1.  **Action:** Remove the temporary configuration file and the temporary cloned repository directory.
2.  **Inputs:** `temp_config_path` from Step 4, `temp_clone_path` from Step 2.
3.  **Tools:** `execute_command`.
4.  **Context:** OS type (for `rm -rf` or `Remove-Item -Recurse -Force`).
5.  **Outputs:** Exit code/output from cleanup commands.
6.  **Decision:** Log cleanup success/failure. Report final outcome (success or failure from Step 6) to the coordinator using `attempt_completion`.

## 6. Error Handling & Escalation ⚠️

*   **Git Clone Failure:** Report error message from `git` to coordinator. May indicate invalid URL, permissions issue, or network problem.
*   **URL Parsing Failure:** Report inability to parse URL to coordinator.
*   **Config Write Failure:** Report file system error to coordinator.
*   **Repomix Execution Failure:** Analyze stderr from `repomix`. Consult KB `01-repomix-usage-corrections.md`. If known config issue, attempt to fix config (Step 3) and retry Step 4-5 once. If unknown or persistent error, report details to coordinator.
*   **Cleanup Failure:** Report error message to coordinator (less critical, but indicates potential leftover temp files).
*   **Escalation:** For persistent or unresolvable issues, escalate to the delegating coordinator (`roo-commander` or `prime-coordinator`).

## 7. Validation (PAL) ✅

*   This SOP should be reviewed and validated according to the standard PAL process.
*   Test cases:
    *   Valid public GitHub repo URL (full repo).
    *   Valid public GitHub repo URL (single subfolder).
    *   Valid public GitHub repo URL (multiple subfolders - if supported by request format).
    *   Invalid GitHub URL.
    *   URL pointing to a non-existent subfolder.
    *   Repo requiring authentication (expected to fail at clone unless credentials configured externally).
    *   Request with specific include/exclude filters.

## 8. Revision History Memento 📜 (Optional)

*   **v1.0 (2025-05-03):** Initial draft based on discussion to handle GitHub repos/subfolders via config file and include filters.