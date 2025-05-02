+++
# --- Basic Metadata ---
id = "RULE-REPOMIX-DECISION-TREE-V3" # Updated ID for version change
title = "Rule: Repomix Source Identification & Config Workflow" # Updated title
context_type = "rules"
scope = "Mandatory workflow for identifying sources and executing repomix via configuration file within spec-repomix mode" # Updated scope
target_audience = ["spec-repomix"]
granularity = "procedure"
status = "active"
last_updated = "2025-05-01" # Updated date
tags = ["rules", "repomix", "workflow", "config-file", "cli", "spec-repomix", "source-handling"] # Updated tags
related_context = [
    ".ruru/modes/spec-repomix/kb/01-repomix-usage-corrections.md", # KB for general usage details
    ".ruru/modes/spec-repomix/kb/02-repomix-github-source-handling.md", # KB for GitHub sources
    ".ruru/modes/spec-repomix/kb/03-repomix-local-source-handling.md", # KB for Local sources
    ".roo/rules/05-os-aware-commands.md" # For command generation
    ]
template_schema_doc = ".ruru/templates/toml-md/16_ai_rule.README.md"
relevance = "High: Defines the mandatory repomix execution logic, including source handling and KB delegation" # Updated relevance description
+++

# Rule: Repomix Source Identification & Config Workflow

This rule outlines the standard procedure for the `spec-repomix` mode to process **all** requests involving the `repomix` tool.

**Objective:** To ensure all `repomix` executions use a configuration file (`repomix --config <path>`) for consistency, robustness, and proper handling of all source types. The mode must first identify the source type and then consult the relevant Knowledge Base (KB) article for the specific procedure to generate the configuration file and execute the command. Direct CLI argument usage for sources or complex parameters is **prohibited**.

**Workflow:**

1.  **Identify Source Type:**
    *   Analyze the input source string(s) provided in the request.
    *   If a source string starts with `https://github.com/`, identify it as a **GitHub URL**.
    *   If a source string appears to be a local filesystem path (e.g., starts with `./`, `/`, `../`, contains OS-specific separators, or is explicitly described as local), identify it as a **Local Path**.
    *   If the source type is unclear or ambiguous (e.g., just `owner/repo`, a generic name), identify it as **Ambiguous**.

2.  **Consult KB & Prepare Config Data:**
    *   Based on the source type identified in Step 1:
        *   **GitHub URL:** **MUST** consult KB `.ruru/modes/spec-repomix/kb/02-repomix-github-source-handling.md`. Follow the procedure outlined there to gather necessary parameters (like `style`, `output`, `filters`) and construct the JSON configuration data object.
        *   **Local Path:** **MUST** consult KB `.ruru/modes/spec-repomix/kb/03-repomix-local-source-handling.md`. Follow the procedure outlined there to gather necessary parameters and construct the JSON configuration data object.
        *   **Ambiguous:** **MUST** use the `ask_followup_question` tool to clarify with the user whether the source is a GitHub reference or a local path. **DO NOT** default to assuming it's in the workspace or any other location. Once the user clarifies, proceed by consulting the appropriate KB (GitHub or Local) as described above.
    *   The referenced KB article contains the specific details on how to format the `sources` array and other necessary keys (`style`, `output`, `include`, `exclude`, `filters`, etc.) within the JSON configuration.

3.  **Create Configuration File:**
    *   Determine a temporary file path, e.g., `.ruru/temp/repomix_config_[YYYYMMDDHHMMSS].json`.
    *   Use the `write_to_file` tool to save the generated JSON configuration object (obtained by following the KB procedure in Step 2) to the temporary file path. Ensure the directory `.ruru/temp/` exists.

4.  **Construct CLI Command:**
    *   Construct the `repomix` command string using the `--config` flag pointing to the temporary file created in Step 3:
        *   `repomix --config .ruru/temp/repomix_config_[YYYYMMDDHHMMSS].json`

5.  **Execute Command:**
    *   Use the `execute_command` tool with the constructed command string (from Step 4).
    *   Ensure the command is OS-aware (Rule `05-os-aware-commands.md`).

6.  **Result Handling:**
    *   Check the `exit_code` and output from the `execute_command` result.
    *   **Success (Exit Code 0):** Report successful execution, mentioning the output file path specified in the configuration.
    *   **Failure (Non-zero Exit Code):**
        *   Analyze the error output.
        *   Consult KB `.ruru/modes/spec-repomix/kb/01-repomix-usage-corrections.md` for known issues or common errors related to configuration files or general usage.
        *   Consult relevant general rules (e.g., command syntax, file permissions).
        *   Attempt correction if possible (e.g., fix config JSON syntax by re-consulting the relevant KB and regenerating the config file - Step 2 & 3) and retry, OR report the failure and error details to the coordinator.

7.  **Cleanup Step (Recommended):**
    *   After execution (successful or failed, if the config is no longer needed for debugging):
        *   Delete the temporary config file created in Step 3.
        *   Use `execute_command` with the appropriate OS command (`rm .ruru/temp/repomix_config_[YYYYMMDDHHMMSS].json` for Linux/macOS, `Remove-Item .ruru/temp/repomix_config_[YYYYMMDDHHMMSS].json` for Windows PowerShell).
        *   Log the cleanup action.