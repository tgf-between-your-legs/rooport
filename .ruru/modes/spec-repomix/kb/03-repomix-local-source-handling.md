+++
# --- Basic Metadata ---
id = "KB-REPOMIX-LOCAL-V1"
title = "Repomix Specialist: Handling Local Directory Sources"
context_type = "knowledge_base"
scope = "Procedure for handling local path inputs"
target_audience = ["spec-repomix"]
status = "active"
last_updated = "2025-05-01"
tags = ["repomix", "kb", "local", "configuration", "procedure"]
related_context = [".roo/rules-spec-repomix/02-repomix-decision-tree.md", ".ruru/modes/spec-repomix/kb/02-repomix-github-source-handling.md"]
# version = "1.0" # Optional: Add version if needed
# relevance = "High" # Optional: Assess relevance
template_schema_doc = ".ruru/templates/toml-md/14_kb_article.README.md" # Points to schema documentation

# --- Knowledge Base Specific Fields ---
# category = "Procedure" # Optional: Categorize the KB article
# keywords = ["local path", "directory source", "repomix config"] # Optional: Additional keywords
# confidence_level = "High" # Optional: Confidence in the information
# applicability = "Specific to local directory inputs for Repomix" # Optional: Describe when this KB is applicable
+++

# Handling Local Directory Sources

When the input source provided for Repomix is identified as a local directory path:

1.  **Identify Path:** Confirm the input string is a valid-looking local directory path. Use filesystem tools (`list_files` or MCP filesystem tools) to verify the path exists if unsure.
2.  **Prepare Configuration:** Generate a temporary JSON configuration file.
3.  **Populate `sources`:** In the configuration file, the `sources` array MUST contain an object specifically formatted for a local path:
    ```json
    {
      "type": "local",
      "path": "[THE_LOCAL_PATH]"
    }
    ```
    Replace `[THE_LOCAL_PATH]` with the actual, validated local path provided in the input. Ensure the path is relative to the workspace root or absolute, as appropriate for the `repomix` tool.
4.  **Populate `output`:** Define the `output` object, specifying the `path` (e.g., `.ruru/temp/repomix_output/[DIR_NAME]_[TIMESTAMP]`), `format` (e.g., `"json"`), and `style`.
    *   The `style` key determines the output structure. Valid values are `"xml"`, `"markdown"`, or `"plain"`.
    *   **Note:** `"tree"` is **not** a valid value for `output.style` in the configuration file, although it might be a command-line option. Use `"markdown"` or `"plain"` for similar hierarchical text output.
5.  **Execute Command:** Use the `execute_command` tool with the command `repomix --config [PATH_TO_TEMP_CONFIG_JSON]`.
6.  **Verification:** After execution, verify the output directory was created and contains the expected files.
7.  **Cleanup:** Remember to handle cleanup of the temporary config file if required by the workflow.