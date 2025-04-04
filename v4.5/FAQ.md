# Roo Commander v4.5 - Frequently Asked Questions (FAQ)

This FAQ addresses common questions about using the Roo Commander v4.5 mode set for managing software development projects within Roo Code.

**1. What is Roo Commander?**

Roo Commander is a collection of specialized AI modes designed to work together like a virtual software development team. It uses a structured workflow, orchestrated by the main `👑 Roo Commander` mode, to handle tasks like planning, design, coding, testing, and documentation.

**2. How do I get started?**

*   **Install:** Download the `roo-commander-v4.5.json` file (or the specific JSON file containing the v4.5 modes).
*   Place it in your Roo Code configuration directory (Global modes) OR rename it to `.roomodes` and place it in the root of your specific project directory (Project-specific modes). Refer to the Roo Code documentation for exact locations.
*   **Activate:** Select the `👑 Roo Commander` mode in Roo Code.
*   **State Your Goal:** Clearly tell the Commander what you want to achieve (e.g., "Start a new project for a portfolio website", "Add authentication to this existing project").
*   **Follow Onboarding:** The `🚦 Project Onboarding` mode will likely activate to clarify if it's a new or existing project and perform initial setup. Answer its questions.

**3. What is the `project_journal/` directory?**

This is the central "memory" and documentation hub for your project when using Roo Commander. It's created automatically for new projects by the `✨ Project Initializer` mode. It contains structured information about the project's progress, plans, decisions, and outputs.

**4. What are the key subdirectories in `project_journal/`?**

*   **`tasks/`:** Contains individual Markdown files (`TASK-ID.md`) for each delegated task. These logs track the goal, steps taken, findings, and final outcome of specific work items. This replaces the old single `activity_log.md`.
*   **`decisions/`:** Stores significant project-level decisions (like technology choices or major architectural changes) in timestamped Markdown files, often following an ADR (Architecture Decision Record) format.
*   **`formal_docs/`:** Holds finalized documents generated during the project, such as requirements specifications, API documentation, design specs, audit reports, research summaries, etc.
*   **`visualizations/`:** Contains Mermaid diagrams illustrating architecture, database schemas, workflows, task status, etc.
*   **`planning/`:** Stores core planning documents like `requirements.md`, `architecture.md`, and `project_plan.md`.
*   **`technical_notes/`:** Intended for general, ad-hoc technical notes that don't fit neatly elsewhere.

**5. What happened to the `memories/` directory?**

The `memories/` directory structure has been removed in v4.5 to reduce clutter and redundancy. Detailed rationale, complex analysis, or troubleshooting steps that might have previously gone into `memories/` should now be:
    *   Included concisely within the relevant `project_journal/tasks/TASK-ID.md` file.
    *   Added as comments directly in the code where applicable.
    *   Synthesized into a report or specification saved in `project_journal/formal_docs/`.

**6. What is `ROO_COMMANDER_SYSTEM.md`?**

This file (created at the project root by `project-initializer` for new projects) defines the standard operating principles, journaling structure, emoji legend, and delegation guidelines used by all Roo Commander modes. It ensures consistency across the system. Modes will refer to it conceptually in their instructions.

**7. Who do I primarily interact with?**

Your main point of contact is the **`👑 Roo Commander`** mode. Give it high-level goals and instructions. It will delegate tasks to the appropriate specialist modes. While other modes might ask clarifying questions (`ask_followup_question`), strategic direction should go through the Commander.

**8. What if a task fails or a mode gets stuck?**

*   Modes are designed to log failures (❌) or blockers (🧱) in their respective task logs (`project_journal/tasks/TASK-ID.md`).
*   They should report the failure back to their delegator (usually the Project Manager or Commander) via `attempt_completion`.
*   The `👑 Roo Commander` or `📋 Project Manager` should analyze the failure (potentially using `📖 Context Resolver`) and decide on the next steps: retry, delegate analysis to `🧩 Complex Problem Solver`, assign to a different specialist, or report the blocker to you.
*   You may need to provide guidance or clarification to the Commander to resolve the issue.

**9. Can I customize the modes or workflow?**

Yes:
*   **Mode Selection:** You can remove unused modes from your `.roomodes` file.
*   **Instructions:** You can edit the `customInstructions` within the JSON definition for any mode to tailor its behavior (do this carefully).
*   **File Access:** You can modify the `fileRegex` patterns if needed, but be cautious not to grant overly broad permissions.
*   **System File:** You can manually edit `ROO_COMMANDER_SYSTEM.md` to adjust global conventions for your project.

**10. What are the limitations?**

*   **LLM Dependence:** The system's success heavily relies on the underlying Large Language Model's ability to follow complex instructions, manage context, and use tools correctly. Performance may vary between models.
*   **Complexity:** It's an advanced workflow. Misunderstandings or errors can still occur.
*   **Token Usage:** The structured approach and detailed prompts can consume more tokens than single-prompt methods.
*   **User Oversight:** It's not fully autonomous. User approval for delegations and intervention for complex errors or strategic shifts is often required.

**11. Why use emojis?**

Emojis (like ✅, ❌, 🧱, 💡) are used in task logs and summaries to provide quick visual cues for both humans scanning the logs and potentially as semantic anchors for the AI to understand the status or type of information presented. The standard legend is in `ROO_COMMANDER_SYSTEM.md`.