+++
# --- Metadata ---
id = "PLAN-KB-ENRICH-PHASE3-V1"
title = "KB Enrichment Plan: Phase 3 - Organization & Indexing"
status = "draft"
created_date = "2025-04-24"
updated_date = "2025-04-24"
version = "1.0"
tags = ["plan", "kb", "enrichment", "phase3", "indexing", "organization", "toml"]
related_docs = [".ruru/planning/kb-enrichment/00-kb-enrichment-plan.md", ".ruru/planning/kb-enrichment/02-ai-synthesis.md"]
objective = "Create TOML-based index files for the synthesized knowledge base documents within the target mode's directory structure to make them discoverable."
scope = "Scanning synthesized documents, extracting metadata, and generating `index.toml` files."
# --- Plan Specific Fields ---
synthesized_kb_dir_template = ".ruru/modes/{mode_slug}/kb/{library_name}/synthesized/"
library_index_file_template = ".ruru/modes/{mode_slug}/kb/{library_name}/index.toml"
mode_master_index_file_template = ".ruru/modes/{mode_slug}/kb/index.toml"
+++

# KB Enrichment Plan: Phase 3 - Organization & Indexing

**Objective:** Generate `index.toml` files for the AI-synthesized KB documents stored in the target mode's directory (`[synthesized_kb_dir_template]`).

**Procedure (for a given `[library_name]` and `[mode_slug]`):**

1.  **Scan Synthesized Files (Coordinator Task):**
    *   Tool: `list_files`
    *   Action: List all `.md` files within `[synthesized_kb_dir_template]`. Store the list as `[Synthesized Files]`. Handle errors if directory not found.

2.  **Generate Library Index Data (Coordinator Task):**
    *   Tool: `read_file`
    *   Action:
        *   Initialize an empty array `library_index_entries = []`.
        *   For each `file_path` in `[Synthesized Files]`:
            *   Read the file content: `<read_file><path>[file_path]</path></read_file>`.
            *   Parse the TOML frontmatter. Use a reliable TOML parser or regex matching `+++...+++`. Handle parsing errors gracefully (log warning, skip file).
            *   Extract `title`, `summary`, and `tags` from the frontmatter. Use fallback values (like filename for title) if fields are missing.
            *   Create an index entry object: `{ title = "...", summary = "...", tags = [...], file = "synthesized/[filename]" }`.
            *   Append the entry to `library_index_entries`.
    *   Output: `library_index_entries` array populated.

3.  **Write Library `index.toml` (Coordinator Task):**
    *   Tool: `write_to_file`
    *   Action:
        *   Format the `library_index_entries` array into a valid TOML string. Each entry should likely be a TOML table within an array of tables. Example:
            ```toml
            # Index for [library_name] Synthesized KB

            [[documents]]
            title = "Core Concepts Overview"
            summary = "High-level summary of core ideas..."
            tags = ["concept", "reactivity", "state"]
            file = "synthesized/core-concepts.md"

            [[documents]]
            title = "API Overview"
            summary = "Summary of key modules/functions..."
            tags = ["api", "modules", "functions"]
            file = "synthesized/api-overview.md"

            # ... more entries
            ```
        *   Calculate line count.
        *   Write the TOML string to `[library_index_file_template]`. Handle errors.
    *   Output: `index.toml` file for the specific library within the mode's KB.

4.  **Update Mode Master Index (Coordinator Task - Optional but Recommended):**
    *   Tool: `read_file`, `write_to_file`
    *   Action:
        *   Read the mode's master index `[mode_master_index_file_template]`. If it doesn't exist, initialize as an empty TOML structure (e.g., `[libraries]` array). Handle read/parse errors.
        *   Check if an entry for `[library_name]` already exists in the `libraries` array.
        *   If not, add a new entry: `{ name = "[library_name]", description = "Synthesized KB for [library_name]", index_file = "[library_name]/index.toml", last_updated = "[current_date]" }`.
        *   If it exists, update the `last_updated` field.
        *   Format the updated master index data into a valid TOML string.
        *   Write the TOML string back to `[mode_master_index_file_template]`. Handle errors.
    *   Output: Updated master `index.toml` for the mode.

**Completion:** Synthesized documents are indexed within the mode's KB. Proceed to Phase 4 (`04-mode-integration.md`).