+++
# --- Basic Metadata ---
id = "KB-REPOMIX-LOCAL-V2" # Updated ID
title = "Repomix Specialist: Handling Local Filesystem Sources (Reference)" # Updated title
context_type = "knowledge_base"
scope = "Guidance on handling local path inputs by referencing the standard SOP" # Updated scope
target_audience = ["spec-repomix"]
status = "active"
last_updated = "2025-05-03" # Updated date
tags = ["repomix", "kb", "local", "sop-reference", "procedure"] # Updated tags
related_context = [
    ".roo/rules-spec-repomix/02-repomix-decision-tree.md",
    ".ruru/processes/SOP-REPOMIX-LOCAL-V1.md" # Link to the SOP
    ]
template_schema_doc = ".ruru/templates/toml-md/14_kb_article.README.md" # Points to schema documentation
# version = "2.0" # Optional: Add version if needed
# relevance = "High" # Optional: Add relevance if needed
# author = "Prime Coordinator" # Optional: Add author if needed
+++

# Handling Local Filesystem Sources

When the input source provided for Repomix is identified as a local filesystem path (e.g., starts with `./`, `/`, `../`, or is explicitly described as local), the `spec-repomix` mode **MUST** follow the detailed procedure outlined in the Standard Operating Procedure (SOP):

*   **SOP:** `.ruru/processes/SOP-REPOMIX-LOCAL-V1.md`

This SOP covers all necessary steps, including:
*   Validating the local path(s).
*   Generating the correct `repomix.config.json` content, including appropriate `sources` pointing to the local path(s).
*   Executing `repomix` using the `--config` flag.
*   Handling errors and performing cleanup.

**Do not implement the logic directly; strictly adhere to the referenced SOP.**