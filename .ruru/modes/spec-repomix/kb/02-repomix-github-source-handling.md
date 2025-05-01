+++
# --- Basic Metadata ---
id = "KB-REPOMIX-GITHUB-V1"
title = "Repomix Specialist: Handling GitHub Repository Sources"
context_type = "knowledge_base"
scope = "Procedure for handling GitHub URL inputs"
target_audience = ["spec-repomix"]
status = "active"
last_updated = "2025-05-01"
tags = ["repomix", "kb", "github", "configuration", "procedure"]
related_context = [".roo/rules-spec-repomix/02-repomix-decision-tree.md", ".ruru/modes/spec-repomix/kb/03-repomix-local-source-handling.md"]
template_schema_doc = ".ruru/templates/toml-md/14_kb_article.README.md" # Points to schema documentation
# version = "1.0" # Optional: Add version if needed
# relevance = "High" # Optional: Add relevance if needed
# author = "Prime Documenter" # Optional: Add author if needed
+++

# Handling GitHub Repository Sources

When the input source provided for Repomix is identified as a GitHub URL (e.g., starts with `https://github.com/`):

1.  **Identify URL:** Confirm the input string is a valid-looking GitHub repository URL.
2.  **Prepare Configuration:** Generate a temporary JSON configuration file.
3.  **Populate `sources`:** In the configuration file, the `sources` array MUST contain an object specifically formatted for GitHub:
    ```json
    {
      "type": "github",
      "url": "[THE_GITHUB_URL]"
    }
    ```
    Replace `[THE_GITHUB_URL]` with the actual URL provided in the input.
4.  **Populate `output`:** Define the `output` object, specifying the `path`, `format`, and `style`.
    *   `path`: The desired output file path (e.g., `.ruru/temp/repomix_output/[REPO_NAME]_[TIMESTAMP].md`).
    *   `format`: The output format (e.g., `"markdown"`).
    *   `style`: The output style. **Valid values for the configuration file are `"xml"`, `"markdown"`, or `"plain"`.**
        *   **Note:** While `"tree"` might be used elsewhere (e.g., as a command-line argument), it is **not** a valid value for `style` within the configuration file JSON. Using `"tree"` here will cause an error.
    *   Example:
        ```json
        {
          "output": {
            "path": ".ruru/temp/repomix_output/my_repo_20250502061500.md",
            "format": "markdown",
            "style": "markdown"
          }
        }
        ```
5.  **Execute Command:** Use the `execute_command` tool with the command `repomix --config [PATH_TO_TEMP_CONFIG_JSON]`.
6.  **Verification:** After execution, verify the output directory was created and contains the expected files.
7.  **Cleanup:** Remember to handle cleanup of the temporary config file if required by the workflow.