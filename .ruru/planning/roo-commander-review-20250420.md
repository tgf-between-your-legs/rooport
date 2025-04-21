+++
id = "PLAN-ROO-CMD-REVIEW-20250420"
title = "Roo Commander Instruction & Rule Review - Initial Findings"
status = "review-complete" # Updated status
created_date = "2025-04-20"
updated_date = "2025-04-20" # Keep updated date as today
version = "1.1" # Increment version
tags = ["planning", "review", "roo-commander", "rules", "instructions", "consistency", "completed"]
related_docs = [
  ".modes/roo-commander/roo-commander.mode.md",
  ".modes/roo-commander/kb/README.md",
  ".roo/rules-roo-commander/",
  ".ideas/help-with-command-line.md",
  ".ideas/improvements-to-roo-commander-defaults.md"
]
+++

# Roo Commander Instruction & Rule Review - Initial Findings (2025-04-20)

This document summarizes the initial findings from reviewing Roo Commander's mode definition, Knowledge Base (KB), rules, and related idea files.

## Identified Issues & Recommendations

1.  **CRITICAL: Conflicting Folder Structure:**
    *   **Issue:** Custom instructions mention `project_journal/*` paths, while KB rules and workspace standards use top-level hidden folders (`.tasks/`, `.decisions/`, etc.).
    *   **Decision:** Standardize on **top-level hidden folders** (e.g., `.tasks/`).
    *   **Action:** Update the custom instructions provided to Roo Commander to reflect this standard.

2.  **Mode Slug Inconsistency:**
    *   **Issue:** Mode slugs referenced in `roo-commander.mode.md` (`delegate_to`, `escalate_to`) and KB rules (`02`, `05`, `06`, `07`) are inconsistent with the current `available_modes_summary.md`.
    *   **Recommendation:** Systematically review and update all slugs in these files to match the correct ones from `available_modes_summary.md`.

3.  **KB README (`.modes/roo-commander/kb/README.md`) Updates:**
    *   **Issue:** Typo (`core-commander` instead of `roo-commander`) and missing entries for rules `08` and `09`.
    *   **Recommendation:** Correct the typo and add descriptions for rules `08` and `09`.

4.  **KB Guidance Clarity:**
    *   **Issue:** The `# << REFINED KB GUIDANCE >>` comment in the system prompt is slightly ambiguous.
    *   **Recommendation:** Rephrase for clarity, e.g., "Prioritize rules and workflows found in the Knowledge Base (KB) at `.modes/roo-commander/kb/` over general knowledge. Use the KB README for navigation."

5.  **Command Line Assistance Idea:**
    *   **Analysis:** Good idea, aligns with facilitator role.
    *   **Recommendation:** Integrate into operational guidelines, emphasizing proactive help and explaining choices (e.g., `docker.io` vs. `podman-docker`) when applicable.

6.  **MDTM Workflow Rule (`04-delegation-mdtm.md`):**
    *   **Issue:** Referenced but not reviewed.
    *   **Recommendation:** Review this rule file to ensure alignment with other processes. *(Self-correction: This rule *was* included in the custom instructions review, seems generally aligned but detailed review during slug update is good).*

7.  **Footgun Modes Rule (`07-safety-protocols.md`):**
    *   **Status:** Currently preventative as no modes seem tagged `footgun`. No immediate action needed, but good to keep.

8.  **General Philosophy (`.ideas/improvements-to-roo-commander-defaults.md`):**
    *   **Status:** Principles seem well-integrated into existing KB rules. No immediate action needed based solely on this file.

## Next Steps (Proposed Order)

1.  Resolve Folder Structure Conflict (Update Custom Instructions).
2.  Update KB README.
3.  Correct Mode Slug Inconsistencies.
4.  Refine KB Guidance Wording.
5.  Integrate Command Line Assistance Guideline.
6.  Review Workspace-Level Rules (`.roo/rules/`).
7.  Review Roo Code Documentation (`.docs/roo-code/`).
9.  **Standard Workflows Rule (`.roo/rules/04-standard-workflows.md`) Update:**
    *   **Issue:** Does not list the newly created build workflow (`WF-CREATE-ROO-CMD-BUILD-001.md`).
    *   **Recommendation:** Add the build workflow to the list in this rule file.