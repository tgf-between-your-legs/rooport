# 👑 Roo Commander
## 🚀 Multi-Agent Workflow Modes for Roo Code Boomerang 🦘

Welcome to the Roo Commander mode set! This repository provides a sophisticated collection of custom modes for [Roo Code](https://github.com/roocode/roo) designed to manage website development projects using a structured, multi-agent approach.

Think of it like having a virtual, specialized software development team right inside your editor, orchestrated by the **👑 Roo Commander**.

## ⏱️ Version V3
[Roo Commander V3 README.md](https://github.com/jezweb/roo-commander/tree/main/v3.0)

[Download the JSON file roo-commander-v3.json](https://github.com/jezweb/roo-commander/blob/main/v3.0/roo-commander-v3.json)

If you want to remove any modes from the file use the [Mode Splitter](https://jezweb.github.io/roo-commander/)

## ✨ Core Concept: The Virtual Team

Instead of relying on a single AI mode for all tasks, this system breaks down development into specialized roles:

1.  **Orchestration (Commander):** Understands high-level goals and delegates tasks.
2.  **Management (PM, Architect, DevOps):** Plans, designs, and coordinates specific domains.
3.  **Specialists (Frontend, API, DB, React, etc.):** Execute specific implementation tasks.
4.  **Support (Secretary, Onboarding, etc.):** Handle crucial auxiliary functions like context gathering and logging.

Communication and context are primarily managed through a structured **Project Journal** and standardized task delegation/completion protocols.

## 🎯 Key Features & Benefits

*   **Structured Workflow:** Brings organization and process to complex development tasks.
*   **Specialized Expertise:** Leverages modes specifically tuned for different roles (frontend, backend, database, testing, etc.).
*   **Scalable Logging:** Uses a structured file system (`project_journal`) for detailed, organized logging of decisions, actions, and technical notes, preventing context overload in single files.
*   **Improved Context Management:** Creates a traceable history of the project, making it easier for the AI (and you!) to understand progress and pick up tasks mid-stream.
*   **Modularity:** Use the full suite or select the modes most relevant to your project needs and tech stack.

## 🧩 Core Components & Roles

*   **👑 Roo Commander:** The "CEO". Your primary interaction point. Understands goals, delegates to managers/specialists, monitors progress, makes high-level decisions.
*   **📋 Project Manager:** Breaks down goals into tasks, manages timelines, assigns work to specialists, tracks progress via the journal.
*   **🏗️ Technical Architect:** Designs system architecture, selects technology, documents key technical decisions.
*   **⚙️ DevOps Manager:** Oversees CI/CD, infrastructure setup, deployment strategies, and operational concerns. Delegates to CI/CD and Infrastructure specialists.
*   **🖥️/☁️/🗃️ Specialists:** Focused roles for execution (e.g., `frontend-developer`, `api-developer`, `database-specialist`, `react-specialist`, `tailwind-specialist`, `php-laravel-developer`, `supabase-developer`, etc.). They receive tasks, implement them, and log their work.
*   **🛠️ Support & Task-Specific Roles:**
    *   `📝 Secretary`: **Crucial role.** Solely responsible for writing/appending validated content to the `project_journal` based on instructions from other modes. Enforces logging structure.
    *   `🚦 Project Onboarding`: Handles the initial setup for new projects or context gathering for existing ones.
    *   `🔍 Discovery Agent`: Interacts with the user to gather detailed requirements.
    *   `✨ Project Initializer`: Sets up the basic directory structure and config files for new projects.
    *   `🔧 Git Manager`: Handles Git operations (branching, merging).
    *   `🐛 Bug Fixer`, `👀 Code Reviewer`, `🔄 Integration Tester`, `⚡ Performance Optimizer`, `♻️ Refactor Specialist`, `♿ Accessibility Specialist`, `🔒 Security Specialist`: Address specific quality, maintenance, and testing aspects.
    *   `🧩 Complex Problem Solver`, `🌐 Research & Context Builder`, `🤔 Second Opinion`, `✍️ Technical Writer`: Provide analysis, research, alternative views, and documentation drafting.

## 🌊 High-Level Workflow Overview

1.  **1️⃣ Initiation:** You interact with **👑 Roo Commander**, stating your goal (new project or task in existing one). Commander delegates to `🚦 Project Onboarding`.
2.  **2️⃣ Onboarding & Planning:** `🚦 Project Onboarding` clarifies intent, gathers initial context (or initializes), and reports back. Commander then delegates planning tasks to `🔍 Discovery Agent` (for requirements), `🏗️ Technical Architect` (for design), and `📋 Project Manager` (for task breakdown/WBS).
3.  **3️⃣ Execution:** `📋 Project Manager` (or `👑 Roo Commander` for initial planning tasks) delegates specific implementation tasks to the relevant **Specialist** modes (e.g., `🖥️ Frontend Developer`, `☁️ API Developer`).
4.  **4️⃣ Logging & Completion:** Each **Specialist** performs its task, logs detailed technical notes by delegating the write operation to `📝 Secretary`, and reports completion back using `attempt_completion` (referencing the saved notes path).
5.  **5️⃣ Coordination & Iteration:** Managers/Commander review completion reports and notes, coordinate dependent tasks, handle blockers (potentially using `🧩 Complex Problem Solver`), and delegate further work.
6.  **6️⃣ Finalization:** Once all major tasks are done, `👑 Roo Commander` reviews the overall outcome and presents it to you.

## 📓 The Project Journal: The System's Memory

This is the cornerstone of context management. All significant actions, decisions, and technical details are logged here.

**Structure:**

```
project_journal/
├── planning/              # Active high-level plans (requirements.md, architecture.md, project_plan.md)
├── formal_docs/           # Finalized docs (API specs, Design specs, Audit reports)
│   └── adr/               # Architectural Decision Records (Optional)
├── wbs/                   # Work Breakdown Structures (Optional)
├── decision_log/          # Critical cross-cutting decisions (Timestamped files)
│   └── YYYY-MM-DD_HH-MM-SS_topic.md
└── technical_notes/       # Detailed working notes per mode & date
    ├── roo-commander/
    │   └── YYYY-MM-DD/
    │       └── YYYY-MM-DD_HH-MM-SS_roo-commander_topic.md
    ├── project-manager/
    │   └── YYYY-MM-DD/
    │       └── YYYY-MM-DD_HH-MM-SS_project-manager_topic.md
    ├── frontend-developer/
    │   └── YYYY-MM-DD/
    │       └── YYYY-MM-DD_HH-MM-SS_frontend-developer_topic.md
    └── ... (folder for each mode)
```

**Key Points:**

*   **Timestamped Notes:** Each mode logs its work in new, timestamped files within its dated folder under `technical_notes`.
*   **Secretary Role:** The `📝 Secretary` mode is the *only* mode directly writing these notes, ensuring consistency and enforcing structure (based on instructions from other modes).
*   **Context References:** Modes are instructed to reference relevant files (requirements, architecture, prior notes) when delegating tasks and logging their own notes.
*   **Completion Reports:** Modes reference the path(s) to their saved notes/docs when reporting completion (`attempt_completion`).

## 🚀 Getting Started & Usage

1.  **Installation:**
    *   Download the `custom_modes.json` file from this repository.
    *   Place it in your Roo Code configuration directory (Global modes) OR rename it to `.roomodes` and place it in the root of your specific project directory (Project-specific modes). Refer to the Roo Code documentation for exact locations.
2.  **Starting a Project:**
    *   Activate the **👑 Roo Commander** mode in Roo Code.
    *   Give it your high-level goal. Examples:
        *   `"Start a new project to build a blog platform using React and Supabase."`
        *   `"I need help with an existing project located at ./my-website. I want to add user authentication."`
    *   The Commander will initiate the workflow, likely starting with the `🚦 Project Onboarding` mode.
3.  **Your Role During Workflow:**
    *   **Primary Interaction:** You mainly interact with the `👑 Roo Commander` for high-level direction and status updates.
    *   **Approvals:** You will need to approve delegated tasks (`new_task`) initiated by the modes (unless auto-approval is configured).
    *   **Review Completions:** Pay attention to `attempt_completion` messages, especially the referenced paths in the `project_journal` to understand what was done.
    *   **Clarifications:** Modes (especially `🔍 Discovery Agent`) may ask you clarifying questions using `ask_followup_question`.
    *   **Monitoring:** You can observe the `project_journal` directory being populated with notes and documents.

## 🛠️ Included Modes (Summary)

*(A selection of key roles)*

| Mode                         | Role                     | Key Function                                         |
| :--------------------------- | :----------------------- | :--------------------------------------------------- |
| **Orchestration**            |                          |                                                      |
| 👑 Roo Commander             | CEO / Orchestrator       | Overall strategy, high-level delegation, coordination |
| **Management**               |                          |                                                      |
| 📋 Project Manager           | Project Management       | Task breakdown, tracking, specialist assignment    |
| 🏗️ Technical Architect       | Architecture Design      | System design, technology selection, ADRs          |
| ⚙️ DevOps Manager            | Operations Management    | CI/CD, Infrastructure, Deployment Strategy         |
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
| 🐘 Supabase Developer      | Supabase Backend         | Auth, Postgres, Edge Functions, Storage            |
| **DevOps Specialists**       |                          |                                                      |
| 🚀 CI/CD Specialist        | CI/CD Pipelines          | Automation, build/test/deploy configuration        |
| 🏗️ Infrastructure Specialist | Infrastructure Mgmt      | IaC (Terraform, etc.), cloud/on-prem setup, networking |
| 🐳 Containerization Dev    | Containerization         | Dockerfiles, K8s/Compose manifests, security       |
| **QA & Maintenance**       |                          |                                                      |
| 🐛 Bug Fixer                 | Bug Resolution           | Diagnosis, fixing, regression testing              |
| 👀 Code Reviewer             | Code Quality Assurance   | Reviewing standards, bugs, security                |
| 🔄 Integration Tester        | Component Interaction    | Testing integration points between system parts    |
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
| 📝 Secretary                 | **Journal Logging**      | **Writes notes/docs to `project_journal` via delegation** |

## ⚙️ Customization

*   **Mode Selection:** Feel free to remove modes you don't need for your specific stack or workflow by deleting their corresponding objects from the `customModes` array in the JSON file.
*   **Instructions:** You can tweak the `customInstructions` for any mode to better suit your team's specific processes or standards.
*   **File Permissions:** Adjust the `fileRegex` patterns if modes need access to different file types.
*   **AI Model:** Add the `apiConfiguration` field to any mode if you want to specify a particular LLM or parameters (e.g., use a faster model for the `secretary`).

## ⚠️ Important Considerations

*   **Complexity:** This is an advanced workflow. It requires the underlying LLM to follow complex instructions and protocols reliably.
*   **LLM Dependence:** The effectiveness heavily depends on the chosen LLM's capabilities (reasoning, planning, instruction following, tool use).
*   **Error Handling:** While designed for structure, modes can still make mistakes or fail tasks. User oversight and intervention may be necessary.
*   **Token Usage:** The detailed instructions and logging can consume more tokens than simpler prompts. Consider this based on your usage patterns and budget. `apiConfiguration` can help manage this.
*   **Dynamic Path Generation:** Modes delegating writes to the `secretary` need to be able to determine the current date/time and construct the correct file path dynamically. Ensure your chosen LLM can handle this reliably within the Roo Code environment.

---

Good luck commanding your virtual Roo Code team! Let us know how it works for you.
