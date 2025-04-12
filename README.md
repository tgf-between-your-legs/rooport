# 👑 Roo Commander: Multi-Agent Workflow Modes for Roo Code

Welcome to Roo Commander! This repository provides a sophisticated collection of custom modes for [Roo Code](https://github.com/roocode/roo) designed to manage software development projects using a structured, multi-agent approach. Think of it like having a virtual, specialized software development team orchestrated by the **👑 Roo Commander**.

## ✨ Latest Version: v6.5

This version refines the mode structure, introduces many new specialist modes, and enhances the capabilities and instructions for core modes like the Commander and Technical Architect, based on learnings from previous versions. Mode collections allow for more granular loading based on project needs.

*   **������ Get the Modes:** v6.5 uses mode collections. Download the relevant JSON file(s) for your project needs from the `v6.5/modes/` directory (assuming `[collection_name]_modes.json` naming):
    *   **Core & Utility:**
        *   [`v6.5/modes/core/core_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/core/core_modes.json)
        *   [`v6.5/modes/utility/utility_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/utility/utility_modes.json)
    *   **Domains:**
        *   [`v6.5/modes/auth/auth_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/auth/auth_modes.json)
        *   [`v6.5/modes/backend_php/backend_php_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/backend_php/backend_php_modes.json)
        *   [`v6.5/modes/backend_python/backend_python_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/backend_python/backend_python_modes.json)
        *   [`v6.5/modes/data/data_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/data/data_modes.json)
        *   [`v6.5/modes/data_vis/data_vis_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/data_vis/data_vis_modes.json)
        *   [`v6.5/modes/devops/devops_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/devops/devops_modes.json)
        *   [`v6.5/modes/frontend_angular/frontend_angular_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/frontend_angular/frontend_angular_modes.json)
        *   [`v6.5/modes/frontend_astro/frontend_astro_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/frontend_astro/frontend_astro_modes.json)
        *   [`v6.5/modes/frontend_general/frontend_general_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/frontend_general/frontend_general_modes.json)
        *   [`v6.5/modes/frontend_react/frontend_react_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/frontend_react/frontend_react_modes.json)
        *   [`v6.5/modes/frontend_svelte/frontend_svelte_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/frontend_svelte/frontend_svelte_modes.json)
        *   [`v6.5/modes/frontend_vue/frontend_vue_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/frontend_vue/frontend_vue_modes.json)
        *   [`v6.5/modes/mode_dev/mode_dev_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/mode_dev/mode_dev_modes.json)
        *   [`v6.5/modes/testing/testing_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/testing/testing_modes.json)
    *   **Stacks:** (Combine Core + Utility + Relevant Domain/Stack collections)
        *   [`v6.5/modes/stack_astro_tailwind/stack_astro_tailwind_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_astro_tailwind/stack_astro_tailwind_modes.json)
        *   [`v6.5/modes/stack_dashboard/stack_dashboard_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_dashboard/stack_dashboard_modes.json)
        *   [`v6.5/modes/stack_ecommerce/stack_ecommerce_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_ecommerce/stack_ecommerce_modes.json)
        *   [`v6.5/modes/stack_fullstack_js/stack_fullstack_js_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_fullstack_js/stack_fullstack_js_modes.json)
        *   [`v6.5/modes/stack_fullstack_python/stack_fullstack_python_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_fullstack_python/stack_fullstack_python_modes.json)
        *   [`v6.5/modes/stack_jamstack/stack_jamstack_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_jamstack/stack_jamstack_modes.json)
        *   [`v6.5/modes/stack_mobile_app/stack_mobile_app_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_mobile_app/stack_mobile_app_modes.json)
        *   [`v6.5/modes/stack_nextjs_firebase/stack_nextjs_firebase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_nextjs_firebase/stack_nextjs_firebase_modes.json)
        *   [`v6.5/modes/stack_nextjs_shadcn/stack_nextjs_shadcn_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_nextjs_shadcn/stack_nextjs_shadcn_modes.json)
        *   [`v6.5/modes/stack_nextjs_supabase/stack_nextjs_supabase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_nextjs_supabase/stack_nextjs_supabase_modes.json)
        *   [`v6.5/modes/stack_nextjs_tailwind_firebase/stack_nextjs_tailwind_firebase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_nextjs_tailwind_firebase/stack_nextjs_tailwind_firebase_modes.json)
        *   [`v6.5/modes/stack_nextjs_tailwind_supabase/stack_nextjs_tailwind_supabase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_nextjs_tailwind_supabase/stack_nextjs_tailwind_supabase_modes.json)
        *   [`v6.5/modes/stack_react_firebase/stack_react_firebase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_react_firebase/stack_react_firebase_modes.json)
        *   [`v6.5/modes/stack_react_materialui_firebase/stack_react_materialui_firebase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_react_materialui_firebase/stack_react_materialui_firebase_modes.json)
        *   [`v6.5/modes/stack_react_supabase/stack_react_supabase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_react_supabase/stack_react_supabase_modes.json)
        *   [`v6.5/modes/stack_react_tailwind_firebase/stack_react_tailwind_firebase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_react_tailwind_firebase/stack_react_tailwind_firebase_modes.json)
        *   [`v6.5/modes/stack_react_tailwind_supabase/stack_react_tailwind_supabase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_react_tailwind_supabase/stack_react_tailwind_supabase_modes.json)
        *   [`v6.5/modes/stack_sveltekit_firebase/stack_sveltekit_firebase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_sveltekit_firebase/stack_sveltekit_firebase_modes.json)
        *   [`v6.5/modes/stack_sveltekit_supabase/stack_sveltekit_supabase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_sveltekit_supabase/stack_sveltekit_supabase_modes.json)
        *   [`v6.5/modes/stack_t3/stack_t3_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_t3/stack_t3_modes.json)
        *   [`v6.5/modes/stack_vue_firebase/stack_vue_firebase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_vue_firebase/stack_vue_firebase_modes.json)
        *   [`v6.5/modes/stack_vue_supabase/stack_vue_supabase_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/stack_vue_supabase/stack_vue_supabase_modes.json)
*   **📚 Learn More:**
    *   [System Guidelines (`ROO_MODE_SYSTEM.md`)](./ROO_MODE_SYSTEM.md) (This file is created in your project by the `project-onboarding` mode).

*(Previous versions are available in the `modes_archive/` directory.)*

## Core Concept: The Virtual Team & Structured Journaling

Instead of a single AI mode, this system uses specialized roles:

1.  **Orchestration (Commander):** Understands goals, delegates tasks.
2.  **Management (PM, Architect):** Plans, designs, coordinates.
3.  **Specialists (Frontend, API, DB, etc.):** Execute implementation tasks.
4.  **Support (Onboarding, Diagramer, etc.):** Handle auxiliary functions.

Context is managed through a structured **Project Journal** (`project_journal/`) and standardized task delegation.

## Key Features & Benefits (v6.5)

*   **Structured Workflow:** Organizes complex development tasks.
*   **Specialized Expertise:** Leverages modes tuned for different roles.
*   **Proactive Commander:** More intelligent initial interaction flow.
*   **Direct Documentation:** Modes handle their own logging and documentation writes.
*   **Task-Based Logging:** Granular task logs (`project_journal/tasks/`) provide detailed history.
*   **Centralized Decisions:** Key decisions captured in `project_journal/decisions/`.
*   **Formalized Outputs:** Final documents stored in `project_journal/formal_docs/`.
*   **Visualizations:** Mermaid diagrams encouraged in `project_journal/visualizations/`.
*   **Improved Context:** Creates a traceable history optimized for AI and humans.
*   **System Guidelines:** `ROO_MODE_SYSTEM.md` defines conventions.
*   **Mode Collections:** Allows loading only necessary modes for specific projects/stacks.

## Included Modes (v6.5 Summary)

This system includes modes for various roles like Commander, Project Manager, Technical Architect, Frontend/API/Database Developers, Testers, DevOps, QA, and Utility functions, organized into domain and stack collections. See the collection JSON files linked above for details.

## Getting Started

1.  **Installation:**
    *   Ensure you have the latest Roo Code extension.
    *   Download the relevant **v6.5 mode collection JSON file(s)** (e.g., [`v6.5/modes/core/frontend_vue_modes.json`](https://github.com/jezweb/roo-commander/blob/main/v6.5/modes/frontend_vue/frontend_vue_modes.json).
    *   Place the downloaded JSON file(s) in your Roo Code configuration directory OR save them individually as `.roomodes` files in your project root (or a `.roo/modes/` subdirectory). Roo Code will load all `.roomodes` files found.
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

*   **Mode Selection:** Load only the `.roomodes` collection files you need.
*   **Instructions:** Tweak `customInstructions` within the JSON files.
*   **File Permissions:** Adjust `fileRegex` patterns if needed (use caution).
*   **AI Model:** Add `apiConfiguration` per mode.

## Important Considerations

*   **Complexity:** Advanced workflow requiring reliable LLM instruction following.
*   **LLM Dependence:** Effectiveness depends on the chosen LLM.
*   **Error Handling:** User oversight may be needed. Review task logs for errors (❌, 🧱).
*   **Token Usage:** Monitor usage, especially with detailed logging and multiple loaded modes.

---

Good luck commanding your virtual Roo Code team!
