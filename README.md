# 👑 Roo Commander: Multi-Agent Workflow Modes for Roo Code

Welcome to Roo Commander! This repository provides a sophisticated collection of custom modes for [Roo Code](https://github.com/roocode/roo) designed to manage software development projects using a structured, multi-agent approach. Think of it like having a virtual, specialized software development team orchestrated by the **👑 Roo Commander**.

## ✨ Latest Version: v5.2

This version introduces a more proactive **👑 Roo Commander** for smoother initial interactions and removes the dedicated `📝 Secretary` mode, empowering other modes to handle their own documentation tasks directly.

*   **🎬 Watch the v5.2 Demo:** [Roo Commander v5.2 Demo on Vimeo](https://vimeo.com/1072760663/d57759626d?share=copy)
*   **➡️ Get the Modes:** Download the v5.2 bundled mode definition file:
    *   **[`v5.2/roo_commander_modes_v5.2.json`](https://github.com/jezweb/roo-commander/blob/main/v5.2/roo_commander_modes_v5.2.json)** (Copy the content of this file into your Roo Code custom modes settings or save as `.roomodes` in your project).
*   **📚 Learn More:**
    *   [System Guidelines (`ROO_COMMANDER_SYSTEM.md`)](./ROO_MODE_SYSTEM.md) (This file is created in your project by the `project-initializer` mode).

*(Previous versions are available in the `modes_archive/` directory.)*

## Core Concept: The Virtual Team & Structured Journaling

Instead of a single AI mode, this system uses specialized roles:

1.  **Orchestration (Commander):** Understands goals, delegates tasks.
2.  **Management (PM, Architect):** Plans, designs, coordinates.
3.  **Specialists (Frontend, API, DB, etc.):** Execute implementation tasks.
4.  **Support (Onboarding, Diagramer, etc.):** Handle auxiliary functions.

Context is managed through a structured **Project Journal** (`project_journal/`) and standardized task delegation.

## Key Features & Benefits (v5.2)

*   **Structured Workflow:** Organizes complex development tasks.
*   **Specialized Expertise:** Leverages modes tuned for different roles.
*   **Proactive Commander:** More intelligent initial interaction flow.
*   **Direct Documentation:** Modes handle their own logging and documentation writes.
*   **Task-Based Logging:** Granular task logs (`project_journal/tasks/`) provide detailed history.
*   **Centralized Decisions:** Key decisions captured in `project_journal/decisions/`.
*   **Formalized Outputs:** Final documents stored in `project_journal/formal_docs/`.
*   **Visualizations:** Mermaid diagrams encouraged in `project_journal/visualizations/`.
*   **Improved Context:** Creates a traceable history optimized for AI and humans.
*   **System Guidelines:** `ROO_COMMANDER_SYSTEM.md` defines conventions.

## Included Modes (v5.2 Summary)

This system includes modes for various roles like Commander, Project Manager, Technical Architect, Frontend/API/Database Developers, Testers, DevOps, QA, and Utility functions. See the bundled JSON file for the full list and details.

## Getting Started

1.  **Installation:**
    *   Ensure you have the latest Roo Code extension.
    *   Download the **[`v5.2/roo_commander_modes_v5.2.json`](https://github.com/jezweb/roo-commander/blob/main/v5.2/roo_commander_modes_v5.2.json)** file.
    *   Place it in your Roo Code configuration directory OR rename it to `.roomodes` and place it in your project root.
2.  **Starting a Project:**
    *   Open your project folder in VS Code.
    *   Activate the **👑 Roo Commander** mode.
    *   **Be Clear with Your Goal:** Provide a concise objective (e.g., "Start a new project...", "Fix a bug in...", "Add feature X...").
    *   The Commander will guide the next steps, potentially asking clarifying questions or suggesting a mode.
3.  **Your Role:**
    *   Interact primarily with the **👑 Roo Commander**.
    *   Approve delegated tasks (`new_task`).
    *   Review `attempt_completion` messages and check referenced journal files (`project_journal/`).
    *   Answer clarifying questions from modes.
    *   Provide corrective feedback to the Commander if needed.

## Customization

*   **Mode Selection:** Remove modes by deleting their objects from the bundled JSON file.
*   **Instructions:** Tweak `customInstructions` within the JSON.
*   **File Permissions:** Adjust `fileRegex` patterns if needed (use caution).
*   **AI Model:** Add `apiConfiguration` per mode.

## Important Considerations

*   **Complexity:** Advanced workflow requiring reliable LLM instruction following.
*   **LLM Dependence:** Effectiveness depends on the chosen LLM.
*   **Error Handling:** User oversight may be needed. Review task logs for errors (❌, 🧱).
*   **Token Usage:** Monitor usage, especially with detailed logging.

---

Good luck commanding your virtual Roo Code team!
