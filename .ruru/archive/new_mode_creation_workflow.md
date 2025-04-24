+++
# --- Basic Metadata ---
id = "WF-MODE-001"
title = "Interactive New Mode Creation Workflow (.ruru/modes/ Structure)"
status = "draft" # Reverted to draft for revision
created_date = "2025-04-16"
updated_date = "2025-04-24" # Date updated
version = "3.0" # Version incremented
tags = ["workflow", "mode-creation", "interactive", "modes-structure", "naming-convention", "manifest", "kb-population", "readme-enhancement", "kb-generation", "template-enforcement"]

# --- Ownership & Context ---
owner = "Roo Commander"
related_docs = [
    ".ruru/modes/roo-commander/kb/available-modes-summary.md", # Added reference for classification
    # ".ruru/templates/modes/mode_specification.md", # Superseded by standard template
    ".ruru/rules/00-standard-toml-md-format.md",
    ".ruru/processes/acqa-process.md",
    ".ruru/processes/afr-process.md",
    ".ruru/processes/pal-process.md"
]
related_templates = [
    ".ruru/templates/modes/00_standard_mode.md", # Standard Mode Template (v1.1)
    ".ruru/templates/toml-md/16_ai_rule.md" # For KB lookup rule
    # ".ruru/templates/modes/kb_placeholders/" # Placeholders superseded by generation
]

# --- Workflow Specific Fields ---
objective = "To guide the creation of a new Roo Commander mode from scratch, using the `.ruru/modes/` structure, applying predefined naming conventions, separating knowledge base (KB) content (with option to generate basic KB if missing), creating mode-specific rules, generating an enhanced KB README, updating the central manifest, and **enforcing the standard mode template structure**, maximizing delegation."
scope = "Applies when creating a new mode not based on a direct migration. Assumes user interaction is available. Creates structure in `.ruru/modes/` and `.roo/rules-<slug>/`, updates `.ruru/modes/manifest.toml`. Uses naming convention document for guidance, prompts for KB population if needed, generates an enhanced KB README, and **populates the standard mode template**."
roles = ["User", "Coordinator (Roo Commander)", "Context Gatherer (e.g., research-context-builder)", "Context Synthesizer (e.g., context-condenser)", "Mode Structure Agent (e.g., mode-maintainer, technical-writer, toml-specialist)", "QA Agent (e.g., code-reviewer)"]
trigger = "User request to create a new mode, specifying its purpose and basic identification."
success_criteria = [
    "Mode definition file exists in `.ruru/modes/<new-slug>/<new-slug>.mode.md`, **adhering to the standard template structure** and containing gathered/generated data with the correct `id`.",
    "KB directory exists at `.ruru/modes/<new-slug>/kb/`.",
    "KB directory contains either generated content from provided sources or generated basic KB content (unless explicitly skipped).",
    "KB README (`.ruru/modes/<new-slug>/kb/README.md`) exists and contains an overview, file list with summaries and line counts (or indicates pending/skipped population).",
    "Mode-specific rule directory exists at `.roo/rules-<new-slug>/`.",
    "KB lookup rule file exists at `.roo/rules-<new-slug>/01-kb-lookup-rule.md` with enhanced instructions.",
    "The created structure passes QA review against specifications (including template structure).",
    "User confirms the generated mode meets initial requirements."
]
failure_criteria = [
    "Unable to determine a valid `prefix-topic` slug with user.",
    "Unable to gather sufficient context.",
    "Failure during optional KB population/generation sub-process.",
    "Worker Agent fails to correctly populate the standard mode template.",
    "Worker Agent fails critical file/directory operations.",
    "Worker Agent fails to generate enhanced KB README.",
    "Generated structure repeatedly fails QA.",
    "User rejects the final mode structure."
]

# --- Integration ---
acqa_applicable = true
pal_validated = false # Needs re-validation
validation_notes = ""

# --- AI Interaction Hints (Optional) ---
# context_type = "workflow_definition"
+++

# Interactive New Mode Creation Workflow (v2.8 - .modes/ Structure)

## 1. Objective 🎯
To guide the creation of a new Roo Commander mode from scratch, using the `.ruru/modes/` structure, applying predefined naming conventions, separating knowledge base (KB) content (with an interactive option to generate basic KB if missing/insufficient), creating mode-specific rules, generating an **enhanced KB README**, updating the central manifest, and **enforcing the standard mode template structure**, maximizing delegation.

## 2. Scope ↔️
Applies when creating a new mode not based on a direct migration. Assumes user interaction is available. Creates structure in `.ruru/modes/` and `.roo/rules-<slug>/`. Uses the naming convention document for guidance, prompts for KB population if needed, generates an enhanced KB README, and **populates the standard mode template**.

## 3. Roles & Responsibilities 👤
*   (No change from v2.7)

## 4. Preconditions🚦
*   (No change from v2.7)

## 5. Reference Documents & Tools 📚🛠️
*   (No change from v2.7)

## 6. Workflow Steps 🪜

*   **Step 1: Initiation & Requirements Gathering (Coordinator, User)**
    *   Coordinator confirms the mode's purpose and target audience with the User.
    *   Coordinator consults `.ruru/modes/roo-commander/kb/available-modes-summary.md` (for classification examples) to determine the appropriate `prefix-topic` slug and `classification`.
    *   Coordinator confirms the proposed slug and classification with the User.

*   **Step 2: Context Gathering (Coordinator delegates to Context Gatherer)**
    *   (No change from v2.7)

*   **Step 3: Context Synthesis (Coordinator delegates to Context Synthesizer)**
    *   (No change from v2.7)

*   **Step 3b: Optional KB Population Prompt (Coordinator, User)**
    *   (No change from v2.7 - includes refined "Generate basic KB" option)

*   **Step 4: Delegate Directory Creation (Coordinator delegates to Worker Agent)**
    *   (No change from v2.7)

*   **Step 5: Delegate Initial Mode File Creation using Template (Coordinator delegates to Worker Agent)**
    *   (No change from v2.7 - already uses standard template path)

*   **Step 6: Delegate Instruction File Creation (Coordinator delegates to Worker Agent)**
    *   (No change from v2.7 - handles synthesized, generated basic, or skipped KB)

*   **Step 7: Delegate Enhanced KB README Update (Coordinator delegates to Worker Agent)**
    *   (No change from v2.7)

*   **Step 8: Delegate KB Rule Creation (Coordinator delegates to Worker Agent)**
    *   (No change from v2.7 - uses enhanced rule template)

*   **Step 9: Quality Assurance (Coordinator applies ACQA)**
    *   (No change from v2.7 - already checks template structure)

*   **Step 10: User Review & Refinement (Coordinator, User)**
    *   (No change from v2.7)

*   **Step 11: Build Mode Registry (Coordinator)**
    *   Coordinator uses `execute_command` to run `node build_roomodes.js`.
    *   Coordinator verifies the command executed successfully (exit code 0).

*   **Step 12: Reload Window (User Action - IMPORTANT)**
    *   Coordinator informs the user: "The mode structure is complete and the registry has been rebuilt. **Please reload the VS Code window now** for the changes to take effect. You can do this via the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and searching for 'Developer: Reload Window'."
    *   Coordinator waits for user confirmation that the window has been reloaded before proceeding.

*   **Step 13: Finalization (Coordinator)**
    *   Coordinator confirms with the user that the new mode is now available and functioning as expected (e.g., by attempting to switch to it or use its initial prompt if applicable).
    *   Coordinator closes the workflow task.

## 7. Postconditions ✅
*   (No change from v2.7)

## 8. Error Handling & Escalation (Overall) ⚠️
*   (No change from v2.7)

## 9. PAL Validation Record 🧪
*   Date Validated: (Needs re-validation)
*   Method:
*   Test Case(s):
*   Findings/Refinements:

## 10. Revision History 📜
*   v3.0 (2025-04-24): Added Step 11 to run `build_roomodes.js` and Step 12 to remind user to reload VS Code window. Renumbered Finalization to Step 13.
*   v3.0 (2025-04-24): Added Step 11 to run `build_roomodes.js` and Step 12 to remind user to reload VS Code window. Renumbered Finalization to Step 13.
*   v2.9 (2025-04-24): Removed manifest steps/references. Added explicit reference to `available-modes-summary.md` for classification guidance in `related_docs` and Step 1. Corrected path for naming convention doc.
*   v2.8 (2025-04-18): Updated `related_templates` to reflect standard template v1.1 (containing refined KB guidance). No change to workflow steps themselves.
*   v2.7 (2025-04-18): Updated Step 5 to enforce population of the standard template. Updated verification check 3.
*   v2.6 (2025-04-18): Refined the "Generate basic KB" instruction in Step 6.
*   v2.5 (2025-04-18): Modified Step 3b prompt to offer "Generate basic KB content". Updated Step 6, 7, and 10.
*   v2.4 (2025-04-18): Enhanced Step 7 (README generation) and Step 8 (KB lookup rule). Adjusted verification check 5.
*   v2.3 (2025-04-18): Added Step 3b to handle insufficient initial context. Adjusted Step 6, 7, and 10.
*   v2.2 (2025-04-18): Updated Step 1/3 to use naming convention doc. Status back to draft.
*   v2.1 (2025-04-18): Incorporated conceptual review feedback. Added `domain`. Clarified manifest creation. Added `new_task`. Embedded KB rule content. Updated error handling. Added template compatibility note.
*   v2.0 (2025-04-18): Major revision for `.ruru/modes/` structure. Updated paths, added manifest/README/rule steps, refined naming.
*   v1.1 (2025-04-16): Incorporated conceptual review feedback.
*   v1.0 (2025-04-16): Initial draft.