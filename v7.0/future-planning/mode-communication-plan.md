# Mode Communication & Interaction Plan (Hybrid Context)

**Version:** 0.1
**Date:** 2025-04-13
**Status:** Proposed

## 1. Introduction

This document outlines the communication protocols and interaction patterns for modes operating within the Roo Commander system, specifically considering the hybrid context model utilizing both `project_journal` and `.roo` directories.

**Goal:** To ensure clear, efficient, and contextually appropriate communication between modes, leveraging the strengths of the hybrid context strategy.

## 2. Core Principles

*   **Hierarchy Matters:** Delegation generally flows downwards (Commander -> Director -> Lead -> Worker). Reporting and escalations flow upwards. Assistants can be called by most levels.
*   **Explicit Context:** Modes should rely primarily on the context explicitly provided during task delegation (`new_task` message, referenced files).
*   **Centralized Orchestration:** `roo-commander` remains the primary orchestrator, initiating top-level tasks and managing complex cross-functional workflows. Directors and Leads manage their respective domains.
*   **Task-Driven Communication:** Most detailed communication should occur within the context of specific MDTM tasks (`project_journal/tasks/`).
*   **Use the Right Tool:** Modes should use appropriate tools for communication (e.g., `attempt_completion` for results, `ask_followup_question` for clarification, `new_task` for delegation).

## 3. Communication Patterns

### 3.1. Task Delegation (`new_task`)

*   **Initiator:** Typically Commander, Directors, or Leads.
*   **Recipient:** Lower-level modes (Directors, Leads, Workers, Assistants).
*   **Content:**
    *   Clear `goal` and `acceptance criteria`.
    *   Reference to the MDTM task file (`project_journal/tasks/TASK-XYZ.md`) for complex tasks.
    *   References to **all** necessary context files, including:
        *   Core project artifacts (e.g., `project_journal/planning/requirements.md`).
        *   Relevant mode-specific context (e.g., `.roo/context/react-specialist/coding-standards.md`).
        *   Workspace rules (e.g., `.roo/rules/general-guidelines.md`).
    *   Coordinator's Task ID for reference.
    *   Relevant specialist tags (if applicable, helps recipient understand context).

### 3.2. Reporting Completion (`attempt_completion`)

*   **Initiator:** Any mode completing its assigned task.
*   **Recipient:** The mode that originally delegated the task (tracked via Coordinator ID or context).
*   **Content:**
    *   Clear statement of outcome (Success, Failure, Escalated, NeedsMoreInfo, etc.).
    *   Concise summary of work performed.
    *   References to key outputs (created/modified files in `project_journal` or source code).
    *   Reference to the completed MDTM task log file (`project_journal/tasks/TASK-XYZ.md`).
    *   If escalating, clearly state the reason and the suggested target mode/level.

### 3.3. Requesting Clarification (`ask_followup_question`)

*   **Initiator:** Any mode encountering ambiguity or needing confirmation.
*   **Recipient:** The mode that delegated the current task.
*   **Content:**
    *   Specific question addressing the ambiguity or missing information.
    *   Context of why the clarification is needed.
    *   Suggested answers to guide the response.
    *   **Crucial for Footgun Modes:** Use this proactively if instructions seem unsafe or incomplete without explicit override acknowledgement.

### 3.4. Context Retrieval (`context-resolver`)

*   **Initiator:** Typically Commander, Directors, or Leads needing a status summary.
*   **Recipient:** `context-resolver`.
*   **Content:**
    *   Specific query (e.g., "Summarize status of TASK-ABC", "List recent decisions on database").
    *   References to known relevant files/directories in `project_journal`.
    *   **(Enhancement):** Potentially instruct it to *also* check specific `.roo/context/{mode-slug}/` directories if relevant to the query.
*   **Response:** `context-resolver` uses `attempt_completion` to return a synthesized summary based *only* on read files, citing sources.

### 3.5. Mode-Specific Context Usage

*   **Reading Own Context:** Modes can freely reference and instruct the LLM to use files within their *own* `.roo/context/{self-slug}/` directory as part of their internal reasoning and `customInstructions`.
*   **Reading Other Modes' Context:** Direct reading of another mode's specific context (`.roo/context/{other-mode}/`) should be **avoided**. Necessary shared information should either be:
    *   Passed explicitly during delegation.
    *   Summarized and provided by `context-resolver`.
    *   Defined in workspace-wide `.roo/rules/`.
*   **Writing Own Context (Future):** If implemented, modes could potentially use `write_to_file` or `apply_diff` on files within their *own* `.roo/context/{self-slug}/` directory to store learned information or cache results. This requires careful permission scoping and state management protocols.

## 4. MDTM Integration

*   **Task Files as Communication Hub:** For complex tasks delegated via MDTM, the task file in `project_journal/tasks/` becomes the central communication record.
*   **Logging:** Modes working on an MDTM task should log significant actions, findings, decisions, and prompts used directly into the task file using `insert_content`.
*   **Status Updates:** The `status` field in the task file's YAML front matter should be kept up-to-date by the mode currently working on it.
*   **Handoffs:** When delegating a sub-task or escalating, reference the main MDTM task ID.

## 5. Considerations

*   **Context Length:** Passing numerous file references during delegation can increase context size. Encourage referencing summary documents (like `_overview.md` or `architecture.md`) where possible. `context-resolver` plays a key role here.
*   **Mode Updates:** Modes relying on specific paths (especially `context-resolver` and `roo-commander`) will need updates to correctly handle searching/referencing both `project_journal` and potentially `.roo/context/`.
*   **User Understanding:** The hybrid model needs clear explanation for the user (e.g., via the Mode Manifest and potentially onboarding messages).

## 6. Conclusion

This hybrid communication plan leverages the strengths of both `project_journal` and `.roo`. It maintains `project_journal` for visible, core project tracking while enabling modes to utilize specialized, potentially large or dynamic context via `.roo/context/`. Clear delegation messages providing necessary context from both locations, along with an enhanced `context-resolver`, are key to making this work effectively. Strict adherence to tool usage and requesting clarification remain paramount, especially for "footgun" modes.