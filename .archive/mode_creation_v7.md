# Standard Operating Procedure (SOP): Creating/Migrating Roo Commander Modes (v7.1)

**Version:** 1.0
**Date:** 2025-04-15

**Objective:** To provide a reliable, step-by-step process for creating the **v7.1 source structure** for new Roo Commander modes or migrating existing ones (e.g., from v7.0). This source structure serves as the organized definition and requires a separate build process to generate runtime files.

**Reference Documents:**

*   `.templates/modes/mode_specification.md` (Defines the required format and fields for mode definitions)
*   `.templates/modes/example_mode_template/` (Provides a concrete example structure)
*   `.roo/rules/` directory (Contains workspace-wide rules, e.g., for TOML formatting, which MUST be followed)

**Inputs:**

*   **Source Material:** EITHER:
    *   Path to the existing primary mode definition file (e.g., `v7.0/modes/.../*.mode.md`).
    *   Path to any accompanying source custom instructions directory (e.g., `v7.0/modes/.../custom-instructions/`), if it exists.
    *   OR Draft content provided by the user (system prompt, description, instructions, metadata ideas).
    *   List of relevant external URLs (documentation, APIs, GitHub repos) for context gathering, especially for tech-specific modes.
*   **Mode Identification:** (Confirm with user if unclear)
    *   `id`: Unique kebab-case identifier (e.g., `technical-writer`).
    *   `name`: Human-friendly display name (e.g., `✍️ Technical Writer`).
    *   `classification`: Hierarchical level (e.g., `executive`, `director`, `lead`, `worker`, `assistant`, `footgun`).
    *   `domain`: Primary functional area (e.g., `core`, `design`, `frontend`, `backend`, `devops`, `data`, `utility`).
    *   `sub_domain` (Optional): Further specialization (e.g., `cloud`, `ci-cd`, `react-ecosystem`).

**Process:**

**Phase 1: Preparation & `{id}.mode.md` Creation**

1.  **Identify Source & Target:**
    *   User provides the source material (path to v7.0 file or draft content).
    *   User confirms the `id`, `name`, `classification`, `domain`, and optional `sub_domain`.
    *   Determine the target directory: `v7.1/modes/[classification]/[domain]/` (add `[sub_domain]/` if applicable) `/[id]/`.

2.  **Verify Exact Source Paths (Coordinator Task):**
    *   Before delegating, the Coordinator (Roo Commander) **must** verify the exact source paths.
    *   Use `list_files` on the specific v7.0 mode directory (e.g., `v7.0/modes/04x-assistant/context-resolver/`) to identify the exact filename of the primary definition file (e.g., `040-asst-context-resolver.mode.md`).
    *   Confirm the existence (or non-existence) and path of any accompanying `custom-instructions` directory within the source mode folder.

3.  **Read Source Material (Delegated Task - Mode Maintainer):**
    *   The Coordinator delegates the task to the `mode-maintainer`, providing the **verified exact paths** identified in Step 2.
    *   The `mode-maintainer` uses `read_file` on the provided primary definition file path. Waits for confirmation.
    *   If a source `custom-instructions` directory path was provided, use `list_files` (recursive) on that path, then `read_file` for each relevant file found. Waits for confirmation.

4.  **Gather External Context (Delegated Task - Mode Maintainer, if applicable):**
    *   If external URLs are provided by the Coordinator:
        *   Use appropriate tools (`execute_command` with `curl`, or MCP tools like `fetch`/`firecrawl` if available) to retrieve content from each URL.
        *   Analyze the retrieved content for key concepts, APIs, best practices relevant to the mode.
        *   Synthesize this information for later inclusion in `custom-instructions` or `context` files.

5.  **Gather Core Information (Delegated Task - Mode Maintainer):**
    *   Extract/define `summary` (concise description) from source/drafts.
    *   Extract/define the main `system_prompt`.

6.  **Gather Metadata (Delegated Task - Mode Maintainer):**
    *   Determine `version` ("1.0.0").
    *   Extract/define `tags`, `categories`, `delegate_to`, `escalate_to`, `reports_to`, `documentation_urls`, `context_files` (ensure paths are workspace-relative, e.g., `v7.1/modes/[...]/context/file.md`), `context_urls`. Refer to `mode_specification.md` for details.

7.  **Determine Tool & File Access (Delegated Task - Mode Maintainer):**
    *   Decide on `allowed_tool_groups` / `allowed_tools`.
    *   Decide on `[file_access]` restrictions (`read_allow`, `write_allow`).

8.  **Construct `{id}.mode.md` Content (Delegated Task - Mode Maintainer):**
    *   Combine gathered info into TOML frontmatter (`+++ ... +++`). Ensure `custom_instructions_source_dir = "custom-instructions"` is included.
    *   Add concise Markdown documentation (`## Description`, `## Capabilities`, etc.).

9.  **Write `{id}.mode.md` (Delegated Task - Mode Maintainer):**
    *   Use `write_to_file` for the target path `v7.1/modes/[...]/[id]/{id}.mode.md` (e.g., `v7.1/modes/assistant/utility/context-condenser/context-condenser.mode.md`).
    *   Provide full `content` and accurately calculated `line_count`.
    *   **Wait for user confirmation** of success before proceeding.

**Phase 2: Populating Subdirectories**

10. **Process Custom Instructions (Delegated Task - Mode Maintainer):**
    *   Analyze **all** source instruction material (from the source `{id}.mode.md` file, any source `custom-instructions` files, and synthesized external context).
    *   Break down into logical, numbered topics following the recommended pattern (`01-principles.md`, `02-workflow.md`, `03-collaboration...`, `04-safety...`, `05-error...`) plus any mode-specific files needed (e.g., `06-tool-usage.md`). Ensure content is refined, clear, and uses workspace-relative paths for any file references.
    *   For *each* topic file:
        *   Use `write_to_file` targeting `v7.1/modes/[...]/[id]/custom-instructions/[NN-topic-name].md`.
        *   Provide refined `content` and `line_count`.
        *   **Wait for user confirmation** of success.
    *   Create/Update `custom-instructions/README.md`:
        *   Use `write_to_file` to list the created instruction files and their purpose.
        *   Provide `content` and `line_count`.
        *   **Wait for user confirmation** of success.

11. **Process Context Files (Delegated Task - Mode Maintainer):**
    *   Identify potential static context files listed in the `{id}.mode.md` file's `context_files` metadata or derived from synthesized external context.
    *   For *each* context file:
        *   Use `write_to_file` targeting the full workspace-relative path specified in `context_files` (e.g., `v7.1/modes/[...]/[id]/context/[filename].md`).
        *   Provide placeholder or synthesized `content` (e.g., API cheatsheet, best practices summary) and `line_count`.
        *   **Wait for user confirmation** of success.

12. **Process Examples (Delegated Task - Mode Maintainer):**
    *   Identify or create 1-2 simple usage examples for the mode.
    *   For *each* example file:
        *   Use `write_to_file` targeting `v7.1/modes/[...]/[id]/examples/[example-name].md`. Ensure any file paths mentioned in the example use workspace-relative paths.
        *   Provide example `content` (e.g., user prompt, expected actions) and `line_count`.
        *   **Wait for user confirmation** of success.

**Phase 3: Quality Assurance (Conceptual - Manual Application)**

*Note: This phase outlines the QA process. Full automation depends on implementing the ACQA system (`.planning/adaptive-confidence-quality-assurance-acqa-proposal.md`). Apply these steps manually/conceptually for now.*

13. **Initiate QA Review (Coordinator Task):** After Phase 2 (steps 10-12) is reported complete by the `mode-maintainer`, the Coordinator triggers a QA review of the created mode source structure (`v7.1/modes/[...]/[id]/`).
14. **Delegate Review Task (Coordinator Task):**
    *   Assign the review task to an appropriate QA agent (e.g., `code-reviewer`, `second-opinion`) via `new_task`.
    *   **Provide Context:** Crucially, the delegation message MUST include:
        *   The path to the mode directory being reviewed.
        *   The path to the Mode Specification (`.templates/modes/mode_specification.md`).
        *   The path to the TOML+MD Specification (`.templates/toml-md/README.md`, if applicable/created).
        *   A clear checklist of what to review (adherence to specs, content quality, path correctness, etc.).
15. **Receive QA Feedback (Coordinator Task):** Obtain the structured feedback report from the QA agent.
16. **Critically Analyze Feedback (Coordinator Task):**
    *   Review the QA feedback carefully.
    *   Compare findings against the provided specifications.
    *   Determine if reported issues are valid, significant, and require correction. Avoid acting on flawed or trivial feedback. (Consider using `second-opinion` if unsure about the initial QA feedback).
17. **Initiate Revisions (Coordinator Task, if Necessary):**
    *   If corrections are needed, delegate a revision task back to the `mode-maintainer`.
    *   Provide *specific* instructions based on the analyzed, validated feedback.
    *   Repeat the QA cycle (Steps 11-15) for the revised artifacts if changes were significant.

**Phase 4: Completion**

18. **Final Check (Coordinator Task):** Once QA is passed (or issues are acknowledged/deferred by the user), ensure all artifacts are in the correct state.
19. **Report Completion (Coordinator Task):** Use `attempt_completion` summarizing the creation/migration, mentioning that a QA review was performed (and whether revisions were made), and listing the key created files/directories. Add the reminder about the separate build step.

**Error Handling:** If any `write_to_file` or delegated task (creation, QA, revision) fails, stop and report the specific error to the user. Do not proceed until the failed step is resolved or skipped upon user instruction. Analyze QA feedback critically before initiating revisions.