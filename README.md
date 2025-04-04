# 👑 Roo Commander v4.5
## 🚀 Multi-Agent Workflow Modes for Roo Code Boomerang 🦘

Welcome to the Roo Commander v4.5 mode set! This repository provides a sophisticated collection of custom modes for [Roo Code](https://github.com/roocode/roo) designed to manage software development projects using a structured, multi-agent approach.

Think of it like having a virtual, specialized software development team right inside your editor, orchestrated by the **👑 Roo Commander**.

**Current Version:** v4.5 (Based on modes in `roo-modes-dev/`)

## ✨ Core Concept: The Virtual Team & Structured Journaling

Instead of relying on a single AI mode for all tasks, this system breaks down development into specialized roles:

1.  **Orchestration (Commander):** Understands high-level goals and delegates tasks.
2.  **Management (PM, Architect):** Plans, designs, and coordinates specific domains.
3.  **Specialists (Frontend, API, DB, React, etc.):** Execute specific implementation tasks.
4.  **Support (Secretary, Onboarding, Diagramer, etc.):** Handle crucial auxiliary functions like context gathering, file writing, and diagram generation.

Communication and context are primarily managed through a structured **Project Journal** (`project_journal/`) and standardized task delegation/completion protocols, ensuring a traceable and understandable project history.

## 🎯 Key Features & Benefits (v4.5)

*   **Structured Workflow:** Brings organization and process to complex development tasks.
*   **Specialized Expertise:** Leverages modes specifically tuned for different roles (frontend, backend, database, testing, etc.).
*   **Task-Based Logging:** Uses granular task logs (`project_journal/tasks/TASK-ID.md`) for detailed, context-specific history, avoiding monolithic log files.
*   **Centralized Decisions:** Key project-level decisions are captured in `project_journal/decisions/` using an ADR-like format.
*   **Formalized Outputs:** Final documents (specs, reports, guides) are stored consistently in `project_journal/formal_docs/`.
*   **Visualizations:** Encourages the use of Mermaid diagrams in `project_journal/visualizations/` for architecture, database schemas, and task status.
*   **Improved Context Management:** Creates a traceable history optimized for AI context rebuilding and human understanding.
*   **Modularity:** Use the full suite or select the modes most relevant to your project needs.
*   **System Guidelines:** A `ROO_COMMANDER_SYSTEM.md` file defines core principles and conventions for consistency.

## 🧩 Core Components & Roles (v4.5 Selection)

*   **👑 Roo Commander:** The "CEO". Your primary interaction point. Understands goals, delegates to managers/specialists, monitors progress via task logs, makes high-level decisions.
*   **📋 Project Manager:** Breaks down goals into tasks, manages plans (`project_journal/planning/project_plan.md`), assigns work to specialists, tracks progress via task logs.
*   **🏗️ Technical Architect:** Designs system architecture (`project_journal/planning/architecture.md`), selects technology, documents key decisions (`project_journal/decisions/`).
*   **🖥️/☁️/🗃️ Specialists:** Focused roles for execution (e.g., `frontend-developer`, `api-developer`, `database-specialist`, `react-specialist`, `tailwind-specialist`, `php-laravel-developer`, etc.). They receive tasks, implement them, and log their work within their assigned task log (`project_journal/tasks/TASK-ID.md`).
*   **🛠️ Support & Task-Specific Roles:**
    *   `📝 Secretary`: **Crucial role.** Handles all validated writes/appends to the `project_journal` (task logs, decisions, formal docs, visualizations) and root README/LICENSE, based on instructions from other modes. Enforces path safety.
    *   `🚦 Project Onboarding`: Handles the initial setup for new projects (including `ROO_COMMANDER_SYSTEM.md`) or context gathering for existing ones.
    *   `🔍 Discovery Agent`: Interacts with the user to gather detailed requirements (`project_journal/planning/requirements.md`).
    *   `✨ Project Initializer`: Sets up the basic directory structure, Git repo, journal structure, and config files (including `ROO_COMMANDER_SYSTEM.md`) for new projects.
    *   `📊 Diagramer`: Generates/updates Mermaid diagram syntax and delegates saving to `secretary`.
    *   `📖 Context Resolver`: Reads task logs, decisions, and planning docs to provide context summaries.
    *   `🔧 Git Manager`: Handles Git operations.
    *   `🐛 Bug Fixer`, `👀 Code Reviewer`, `🔄 Integration Tester`, `🎭 E2E Tester`, `⚡ Performance Optimizer`, `♻️ Refactor Specialist`, `♿ Accessibility Specialist`, `🔒 Security Specialist`: Address specific quality, maintenance, and testing aspects, logging their work within their task logs.
    *   `🧩 Complex Problem Solver`, `🌐 Research & Context Builder`, `🤔 Second Opinion`, `✍️ Technical Writer`: Provide analysis, research, alternative views, and documentation drafting, saving outputs to `project_journal/formal_docs/` or logging process in task logs.

## 🌊 High-Level Workflow Overview (v4.5)

1.  **1️⃣ Initiation:** Interact with **👑 Roo Commander**, stating your goal. Commander delegates to `🚦 Project Onboarding`.
2.  **2️⃣ Onboarding & Planning:** `🚦 Project Onboarding` clarifies new/existing project, gathers initial context or initializes the structure (including `ROO_COMMANDER_SYSTEM.md`), and reports back. Commander then delegates planning tasks (e.g., to `🔍 Discovery Agent`, `🏗️ Technical Architect`, `📋 Project Manager`). Each delegated task gets a unique Task ID and its own log file created in `project_journal/tasks/`.
3.  **3️⃣ Execution:** `📋 Project Manager` (or `👑 Roo Commander`) delegates specific implementation sub-tasks to **Specialist** modes, providing the Task ID and context references.
4.  **4️⃣ Logging & Completion:** Each **Specialist** performs its task, logs key steps, findings, and outcomes by delegating appends to the `📝 Secretary` for their specific task log file (`project_journal/tasks/TASK-ID.md`). Finalized documents are saved to `project_journal/formal_docs/` via `secretary`. Diagrams are updated via `diagramer` -> `secretary`.
5.  **5️⃣ Coordination & Iteration:** Managers/Commander review task logs (`read_file`), use `📖 Context Resolver` for summaries, coordinate dependencies, handle blockers (potentially logging decisions to `project_journal/decisions/`), and delegate further work.
6.  **6️⃣ Finalization:** Once all major tasks show ✅ completion in their logs, `👑 Roo Commander` reviews the overall outcome and presents it to you.

## 📓 The Project Journal (v4.5): The System's Memory

This structured directory is the cornerstone of context management.

**Structure:**

```
project_journal/
├── tasks/                   # Task-specific logs (TASK-ID.md for each delegated task)
│   └── TASK-FE-YYYYMMDD-HHMMSS.md
├── decisions/               # Project-level decisions (ADR-like files)
│   └── YYYYMMDD-technology-choice.md
├── formal_docs/           # Finalized outputs (reports, specs, guides)
│   └── api_spec_v1.yaml
├── visualizations/          # Mermaid diagrams
│   └── architecture_diagram.md
├── planning/              # Core plans
│   ├── requirements.md
│   ├── architecture.md
│   └── project_plan.md
└── technical_notes/       # Ad-hoc technical documentation
```

**Key Points:**

*   **Task Logs:** Each delegated task has its own log file in `tasks/`, tracking its goal, steps, findings, and final outcome.
*   **Decisions:** Significant, cross-cutting decisions are recorded in `decisions/`.
*   **Formal Docs:** Finalized artifacts live in `formal_docs/`.
*   **Secretary Role:** The `📝 Secretary` handles all writes/appends to the journal directories and root README/LICENSE, ensuring path validation.
*   **Context References:** Modes reference relevant planning docs, decision files, or other task logs when delegating or reporting.
*   **Completion Reports:** Modes reference their specific task log file (`project_journal/tasks/TASK-ID.md`) when reporting completion.

## 🚀 Getting Started & Onboarding Advice (v4.5)

1.  **Installation:**
    *   Ensure you have the latest Roo Code extension.
    *   Download the `roo-commander-v4.5.json` file (or the specific JSON file containing the v4.5 modes).
    *   Place it in your Roo Code configuration directory (Global modes) OR rename it to `.roomodes` and place it in the root of your specific project directory (Project-specific modes). Refer to the Roo Code documentation for exact locations.
2.  **Starting a Project:**
    *   Open your project folder in VS Code.
    *   Activate the **👑 Roo Commander** mode in Roo Code.
    *   **Be Clear with Your Goal:** Provide a concise, high-level objective.
        *   **New Project Example:** `"Start a new project named 'my-blog' to build a blog platform using React and a Node.js backend."` (The `project-initializer` will create `ROO_COMMANDER_SYSTEM.md` and the journal structure).
        *   **Existing Project Example:** `"I need help with this existing project. Add a user profile page with editing capabilities."` (The `project-onboarding` mode will check for the journal structure and `ROO_COMMANDER_SYSTEM.md`).
    *   The Commander will initiate the workflow, likely starting with `🚦 Project Onboarding`. Answer its questions clearly (new vs. existing, project name if new).
3.  **Your Role During Workflow:**
    *   **Primary Interaction:** You mainly interact with the `👑 Roo Commander` for high-level direction, status updates, and resolving major blockers.
    *   **Approvals:** You will need to approve delegated tasks (`new_task`) initiated by the modes (unless auto-approval is configured in Roo Code settings). Review the task goal and context before approving.
    *   **Review Completions:** Pay attention to `attempt_completion` messages. Check the referenced task log (`project_journal/tasks/TASK-ID.md`) and any created documents (`project_journal/formal_docs/`, `project_journal/planning/`) to understand what was done.
    *   **Clarifications:** Modes (especially `🔍 Discovery Agent`) may ask you clarifying questions using `ask_followup_question`. Provide specific answers.
    *   **Monitoring:** Observe the `project_journal/` directory. Key files to check for status:
        *   `project_journal/tasks/`: See the progress within individual task logs.
        *   `project_journal/planning/`: Review requirements, architecture, and plans.
        *   `project_journal/decisions/`: Understand key project decisions.
    *   **Guidance:** If a mode seems stuck or going in the wrong direction, provide corrective feedback to the `👑 Roo Commander`.

4.  **Getting the Best Experience:**
    *   **Start Simple:** For initial tests, try a small, well-defined task.
    *   **Clear Goals:** The clearer your initial goal for the Commander, the better the delegation.
    *   **Review Delegations:** Briefly check the tasks being delegated to ensure they align with your intent.
    *   **Check the Journal:** Periodically review the task logs and planning documents to stay informed.
    *   **Use `Context Resolver`:** Ask the Commander to use the `📖 Context Resolver` if you need a summary of the current state or a specific task's history.

## ⚙️ System Guidelines (`ROO_COMMANDER_SYSTEM.md`)

For detailed information on journaling principles, the standard journal structure, the emoji legend, and delegation guidelines used by these modes, please refer to the `ROO_COMMANDER_SYSTEM.md` file located in the project root (created by `project-initializer` for new projects).

## 🛠️ Included Modes (v4.5 Summary)

*(See `project_journal_summary.md` for a more detailed breakdown generated previously)*

| Mode                         | Role                     | Key Function                                         |
| :--------------------------- | :----------------------- | :--------------------------------------------------- |
| **Orchestration**            |                          |                                                      |
| 👑 Roo Commander             | CEO / Orchestrator       | Overall strategy, high-level delegation, coordination |
| **Management**               |                          |                                                      |
| 📋 Project Manager           | Project Management       | Task breakdown, tracking, specialist assignment    |
| 🏗️ Technical Architect       | Architecture Design      | System design, technology selection, decisions     |
| **Core Web Specialists**     |                          |                                                      |
| 🖥️ Frontend Developer       | Frontend Implementation  | UI coding, client-side logic, framework usage      |
| ☁️ API Developer             | Backend API Implementation | API design, endpoint coding, security              |
| 🗃️ Database Specialist     | Database Management      | Schema design, query optimization, migrations      |
| 🎨 UI Designer               | User Interface Design    | Wireframes, mockups, prototypes, style guides      |
| **Framework Specialists**    |                          |                                                      |
| ⚛️ React Specialist          | React Implementation     | Component architecture, state, hooks, performance    |
| 🎨 Material UI Specialist  | Material UI Integration  | MUI components, theming, customization             |
| 💨 Tailwind CSS Specialist  | Tailwind Implementation  | Utility classes, config, optimization              |
| 🐘 PHP/Laravel Developer    | PHP/Laravel Backend      | Eloquent, Blade, routing, Artisan                  |
| **DevOps Specialists**       |                          |                                                      |
| 🚀 CI/CD Specialist        | CI/CD Pipelines          | Automation, build/test/deploy configuration        |
| 🏗️ Infrastructure Specialist | Infrastructure Mgmt      | IaC (Terraform, etc.), cloud/on-prem setup, networking |
| 🐳 Containerization Dev    | Containerization         | Dockerfiles, K8s/Compose manifests, security       |
| **QA & Maintenance**       |                          |                                                      |
| 🐛 Bug Fixer                 | Bug Resolution           | Diagnosis, fixing, regression testing              |
| 👀 Code Reviewer             | Code Quality Assurance   | Reviewing standards, bugs, security                |
| 🔄 Integration Tester        | Component Interaction    | Testing integration points between system parts    |
| 🎭 E2E Testing Specialist    | End-to-End UI Testing    | Simulating user journeys, UI validation            |
| ⚡ Performance Optimizer    | Performance Tuning       | Profiling, bottleneck analysis, optimization       |
| ♻️ Refactor Specialist       | Code Improvement         | Improving structure, readability, maintainability  |
| ♿ Accessibility Specialist  | Accessibility Assurance  | WCAG compliance, testing, accessible design        |
| 🔒 Security Specialist       | Security Assurance       | Vulnerability assessment, controls, incident response |
| **Support & Utility**        |                          |                                                      |
| 🚦 Project Onboarding       | Project Setup/Context    | New project init or existing project discovery     |
| 🔍 Discovery Agent           | Requirements Gathering   | User interaction to define project scope           |
| ✨ Project Initializer       | Project Scaffolding      | Creating initial directories and config files      |
| 🔧 Git Manager               | Version Control          | Branching, merging, tagging                        |
| 🧩 Complex Problem Solver    | Advanced Analysis        | Deep reasoning, solution evaluation                |
| 🌐 Research Context Builder  | Information Gathering    | Web/repo searching, context synthesis              |
| 🤔 Second Opinion            | Alternative Perspective  | Reviewing proposed solutions/designs               |
| ✍️ Technical Writer          | Documentation Creation   | Writing user guides, API docs, etc.                |
| 📝 Secretary                 | **Journal/Doc Writing**  | **Writes/Appends to `project_journal` via delegation** |
| 📖 Context Resolver          | **Journal Reading**      | **Reads journal files to provide context summaries** |
| 📊 Diagramer                 | **Diagram Generation**   | **Generates Mermaid syntax, delegates save**       |
| 🔧 File Repair Specialist    | File Corruption Fix      | Attempts to repair malformed text files          |


## ⚙️ Customization

*   **Mode Selection:** Remove modes by deleting their objects from the `customModes` array in your `.roomodes` or global modes file.
*   **Instructions:** Tweak `customInstructions` to better suit your processes.
*   **File Permissions:** Adjust `fileRegex` patterns if modes need different access (use with caution).
*   **AI Model:** Add `apiConfiguration` to specify LLMs/parameters per mode.

## ⚠️ Important Considerations

*   **Complexity:** This is an advanced workflow requiring reliable LLM instruction following.
*   **LLM Dependence:** Effectiveness depends heavily on the chosen LLM's capabilities.
*   **Error Handling:** Modes can still fail. User oversight and intervention may be needed. Review task logs for errors (❌, 🧱).
*   **Token Usage:** Detailed logging and complex prompts consume tokens. Monitor usage.
*   **Task ID Generation:** Uses timestamps (`TASK-[MODE]-YYYYMMDD-HHMMSS`) for uniqueness.

---

Good luck commanding your virtual Roo Code team!
