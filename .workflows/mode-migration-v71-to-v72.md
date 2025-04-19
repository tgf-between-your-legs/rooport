+++
# --- Basic Metadata ---
id = "WF-MODE-MIGRATE-001"
title = "Workflow: Migrate Mode from v7.1 to .modes/ Structure"
status = "active" # Updated to reflect new tracking steps
created_date = "2025-04-18"
updated_date = "2025-04-18" # Date updated
version = "1.12" # Version incremented for tracking/archiving steps
tags = ["workflow", "sop", "modes", "migration", "v7.1", "refactoring", "delegation", "context-optimization", "naming-convention", "manifest", "kb-population", "readme-enhancement", "kb-generation", "template-enforcement", "tracking", "archiving"]

# --- Ownership & Context ---
owner = "Roo Commander"
related_docs = [
  ".decisions/ADR-001_mode_source_reorganisation.md",
  ".docs/standards/mode_naming_convention_v7.2.md",
  ".context/mode_migration_status_v71_to_v72.md", # Added tracking file
  ".docs/roo-code/custom-modes.md",
  ".docs/roo-code/custom-instructions.md",
  ".processes/acqa-process.md",
  ".processes/afr-process.md",
  ".processes/pal-process.md"
]
related_templates = [
  ".templates/toml-md/16_ai_rule.md", # For the KB lookup rule
  ".templates/modes/00_standard_mode.md" # Standard Mode Template (v1.1)
]

# --- Workflow Specific Fields ---
objective = "To migrate a single mode definition from the v7.1 directory structure to the new `.modes/` structure, applying predefined naming conventions, separating knowledge base (KB) content (with option to generate basic KB if missing), creating mode-specific rules, generating an enhanced KB README, updating the central manifest, **enforcing the standard mode template structure**, archiving the original source, updating the migration tracking status, and maximizing delegation."
scope = "Applies to each individual mode located within the `v7.1/modes/` directory structure (excluding `v7.1/modes/.archive/`). Covers identifying source files, looking up naming/paths, **populating the standard mode template** using source data, handling potentially empty source KBs, generating an enhanced KB README, delegating verification, delegating manifest updates, archiving the original source folder, and updating the migration status file."
roles = [
  "Coordinator (Roo Commander)",
  "Worker Agent (e.g., `mode-maintainer`, `toml-specialist`, `technical-writer`, `research-context-builder`, `context-condenser`)",
  "Verification Agent (e.g., `code-reviewer`, `second-opinion`)"
]
trigger = "Manual initiation by the Coordinator for each mode requiring migration."
success_criteria = [
  "Mode definition file exists in `.modes/<new-slug>/<new-slug>.mode.md`, **adhering to the standard template structure** and containing migrated data with the correct `id`.",
  "Knowledge base directory exists at `.modes/<new-slug>/kb/`.",
  "KB directory contains either migrated content, newly generated content from provided sources, or generated basic KB content (unless explicitly skipped).",
  "KB README (`.modes/<new-slug>/kb/README.md`) exists and contains an overview, file list with summaries and line counts (or indicates pending/skipped population).",
  "Mode-specific rule directory exists at `.roo/rules-<new-slug>/`.",
  "KB lookup rule file exists at `.roo/rules-<new-slug>/01-kb-lookup-rule.md` with enhanced instructions.",
  "The mode is correctly represented with its new slug and paths in `.modes/manifest.toml`.",
  "Verification Agent confirms successful migration according to checks (including template structure).",
  "The migration status file (`.context/mode_migration_status_v71_to_v72.md`) is updated to reflect the mode's completion.",
  "The original v7.1 mode source directory has been moved to the `v7.1/modes/.archive/` directory."
]
failure_criteria = [
  "Worker Agent fails to read/validate source file or TOML.",
  "Coordinator fails to find mapping for the mode in the naming convention document.",
  "Worker Agent fails to create required files or directories.",
  "Worker Agent fails to correctly populate the standard template or update the `id`.",
  "Failure during optional KB population/generation sub-process.",
  "Worker Agent fails to generate enhanced KB README.",
  "Worker Agent fails to update `.modes/manifest.toml` correctly.",
  "Verification Agent reports failures."
]

# --- Integration ---
acqa_applicable = true
pal_validated = false # Needs re-validation
validation_notes = ""

# --- AI Interaction Hints (Optional) ---
# context_type = "workflow_definition"
+++

# Workflow: Migrate Mode from v7.1 to .modes/ Structure (v1.11)

## 1. Objective 🎯
*   To migrate a single mode definition from the v7.1 directory structure to the new `.modes/` structure, applying predefined naming conventions, separating knowledge base (KB) content (with an interactive option to generate basic KB if missing/insufficient), creating mode-specific rules, generating an **enhanced KB README**, updating the central manifest, and **enforcing the standard mode template structure**, maximizing delegation.

## 2. Scope ↔️
*   Applies to each individual mode located within the `v7.1/modes/` directory structure.
*   Covers identifying source files, looking up naming/paths, **populating the standard mode template** using source data, handling potentially empty source KBs, generating an enhanced KB README, delegating verification, and delegating manifest updates.

## 3. Roles & Responsibilities 👤
*   (No change from v1.10)

## 4. Preconditions🚦
*   (No change from v1.10)

## 5. Reference Documents & Tools 📚🛠️
*   (No change from v1.10)

## 6. Workflow Steps 🪜

*   **Step 1: Select Mode & Identify Paths (Coordinator Task)**
    *   (No change)

*   **Step 2: Delegate Source Read & Validation (Coordinator delegates to Worker Agent)**
    *   (No change)

*   **Step 3: Determine New Slug & Paths (Coordinator Task)**
    *   (No change)

*   **Step 4: Delegate Directory Creation (Coordinator delegates to Worker Agent)**
    *   (No change)

*   **Step 5: Delegate Mode Definition Migration using Template (Coordinator delegates to Worker Agent)**
    *   (No change from v1.10 - already uses standard template path)

*   **Step 6: Delegate KB Content Migration & Optional Population (Coordinator delegates to Worker Agent, potentially involves User interaction)**
    *   (No change from v1.10 - includes refined "Generate basic KB" instruction)

*   **Step 7: Delegate Enhanced KB README Update (Coordinator delegates to Worker Agent)**
    *   (No change from v1.10)

*   **Step 8: Delegate KB Rule Creation (Coordinator delegates to Worker Agent)**
    *   (No change from v1.10 - uses enhanced rule template)

*   **Step 9: Delegate Manifest Update (Coordinator delegates to Worker Agent)**
    *   (No change)

*   **Step 10: Delegate Verification (Coordinator delegates to Verification Agent)**
    *   (No change from v1.10 - already checks template structure)

*   **Step 11: Delegate Tracking File Update (Coordinator delegates to Worker Agent)**
    *   **Action:** Instruct a Worker Agent (e.g., `technical-writer` or `mode-maintainer`) to update the `.context/mode_migration_status_v71_to_v72.md` file.
    *   **Details:** Mark the current mode as "Migrated", add the completion date, and any relevant notes (e.g., "KB generated", "Emoji updated").
    *   **Tool:** `apply_diff` or `search_and_replace`.

*   **Step 12: Delegate Archiving of v7.1 Source (Coordinator delegates to Worker Agent)**
    *   **Action:** Instruct a Worker Agent (e.g., `git-manager` or `mode-maintainer`) to move the original v7.1 mode directory to the archive.
    *   **Details:** Use `execute_command` with `mkdir -p` for the target archive path (preserving structure) and `mv` for the source directory. Example: `mkdir -p v7.1/modes/.archive/<original_path_structure>/ && mv <original_v7.1_mode_path> v7.1/modes/.archive/<original_path_structure>/`
    *   **Tool:** `execute_command`.

*   **Step 13: Final Report (Coordinator Task)**
    *   (No change)

## 7. Postconditions ✅
*   (No change)

## 8. Error Handling & Escalation (Overall) ⚠️
*   (No change from v1.10)

## 9. PAL Validation Record 🧪
*   Date Validated: (Needs re-validation)
*   Method:
*   Test Case(s):
*   Findings/Refinements:

## 10. Revision History 📜
*   v1.12 (2025-04-18): Added Step 11 (Update Tracking File) and Step 12 (Archive Source). Renumbered Final Report to Step 13. Updated objective, scope, success criteria, tags, and related docs to reflect tracking/archiving. Set status to active.
*   v1.11 (2025-04-18): Updated `related_templates` to reflect standard template v1.1 (containing refined KB guidance). No change to workflow steps themselves.
*   v1.10 (2025-04-18): Updated Step 5 to enforce population of the standard template. Updated verification check 3.
*   v1.9 (2025-04-18): Refined the "Generate basic KB" instruction in Step 6b.
*   v1.8 (2025-04-18): Modified Step 6b prompt to offer "Generate basic KB content". Updated Step 7 and 10.
*   v1.7 (2025-04-18): Enhanced Step 7 (README generation) and Step 8 (KB lookup rule). Adjusted verification check 5.
*   v1.6 (2025-04-18): Added Step 6b to handle empty/insufficient source KBs. Adjusted Step 7 and Verification Step 10. Added context agents.
*   v1.5 (2025-04-18): Updated Step 3 to use mapping doc. Updated references. Status back to draft.
*   v1.4 (2025-04-18): Changed target dir to `.modes/`. Refined naming. Added Step 7 (KB README). Updated paths. Status back to draft.
*   v1.3 (2025-04-18): Delegated source read/validation and manifest update. Renumbered steps. Added KB rule template.
*   v1.2 (2025-04-18): Revised for delegation, added process refs, clarified roles/errors.
*   v1.1 (2025-04-18): Initial draft.