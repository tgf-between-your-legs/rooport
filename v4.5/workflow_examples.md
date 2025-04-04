# Roo Commander v4.5 - New Project Workflow Examples

This document illustrates the typical user experience and workflow when initiating new development projects using the Roo Commander v4.5 mode set.

**Core Concepts:**

*   **User Interaction:** Primarily with `👑 Roo Commander`.
*   **Delegation:** Commander delegates tasks to specialized modes.
*   **Task Logs:** Each significant delegated task gets its own log file in `project_journal/tasks/TASK-ID.md`.
*   **Approvals:** User typically needs to approve `new_task` delegations.
*   **Journaling:** Key steps, decisions, and outcomes are recorded in task logs or dedicated files (`decisions/`, `formal_docs/`, etc.) via the `📝 Secretary`.

---

## Example 1: Simple Static Portfolio Website

**Goal:** Create a basic single-page portfolio website using HTML, CSS, and maybe a little JavaScript.

1.  **User:** (Activates `👑 Roo Commander`)
    > "Start a new project for a simple personal portfolio website called 'my-portfolio'."

2.  **Roo Commander:** (Recognizes new project request)
    > Delegates to `🚦 Project Onboarding`.
    > *(User approves `new_task`)*

3.  **Project Onboarding:**
    > Asks: "Welcome! Are we starting a brand new project or working on an existing one?"
    > Suggestions: ["🚀 Start a new project.", "📂 Work on an existing project."]

4.  **User:** Selects "🚀 Start a new project."

5.  **Project Onboarding:**
    > Asks: "Great! What should we name this new project? ..." (User confirms 'my-portfolio').
    > Delegates to `🔍 Discovery Agent` (Task ID: TASK-DISC-...) with message: "🎯 New Project: 'my-portfolio'. Gather detailed requirements for a simple static portfolio website. Save output via `secretary` to `project_journal/planning/requirements.md`. Initialize task log..."
    > *(User approves `new_task`)*

6.  **Discovery Agent:**
    > Interacts with User via `ask_followup_question` to define sections (About, Projects, Contact), content details, desired style.
    > Logs interaction details to `project_journal/tasks/TASK-DISC-...md` via `secretary`.
    *   *(User approves `secretary` writes)*
    > Summarizes requirements.
    > Delegates save to `📝 Secretary`: "Action: Write File\nPath: `project_journal/planning/requirements.md`\nContent: ```markdown\n# Project Requirements: my-portfolio\n...\n```"
    *   *(User approves `new_task`)*
    > Logs completion to `project_journal/tasks/TASK-DISC-...md` via `secretary`.
    *   *(User approves `secretary` writes)*
    > Reports back to `Project Onboarding` using `attempt_completion` with the requirements summary.

7.  **Project Onboarding:** (Receives confirmation from Discovery Agent)
    > Delegates to `✨ Project Initializer` (Task ID: TASK-INIT-...) with message: "✨ Initialize project structure for 'my-portfolio'... Create standard `project_journal/`..., `.gitignore`, `README.md`, and `ROO_COMMANDER_SYSTEM.md`. Copy requirements..."
    > *(User approves `new_task`)*

8.  **Project Initializer:**
    > Executes `mkdir` for `project_journal/tasks/`, `decisions/`, etc., and `src/`, `css/`, `js/`.
    > Executes `git init`.
    > Delegates creation of `.gitignore`, `README.md`, `ROO_COMMANDER_SYSTEM.md` to `📝 Secretary`.
    *   *(User approves `secretary` writes)*
    > Copies `project_journal/planning/requirements.md`.
    > Reports completion back to `Project Onboarding`.

9.  **Project Onboarding:** (Receives confirmation from Initializer)
    > Reports back to `👑 Roo Commander` using `attempt_completion`: "✅ Onboarding Complete: New project 'my-portfolio' initialized... Requirements gathered... Ready for planning."

10. **Roo Commander:** (Takes over)
    > "Okay, the 'my-portfolio' project is set up with basic requirements. Since it's a simple static site, I'll delegate directly to the frontend developer. Task ID: TASK-FE-..."
    > Delegates to `🖥️ Frontend Developer` using `new_task`: "🎯 Implement the static portfolio website based on `project_journal/planning/requirements.md`. Create `index.html`, `css/style.css`, `js/script.js`. Initialize task log `project_journal/tasks/TASK-FE-...md`."
    > *(User approves `new_task`)*

11. **Frontend Developer:**
    > Creates/appends initial goal to `project_journal/tasks/TASK-FE-...md` via `secretary`.
    *   *(User approves `secretary` writes)*
    > Reads requirements.
    > Writes `index.html`, `css/style.css`, `js/script.js` using `write_to_file`.
    *   *(User approves `write_to_file` actions)*
    > Logs completion details (files created) to `project_journal/tasks/TASK-FE-...md` via `secretary`.
    *   *(User approves `secretary` writes)*
    > Reports completion to `👑 Roo Commander`.

12. **Roo Commander:**
    > Reviews task log.
    > Reports back to User using `attempt_completion`: "✅ The basic portfolio website files (`index.html`, `css/style.css`, `js/script.js`) have been created based on the requirements. Task log: `project_journal/tasks/TASK-FE-...md`."

---

## Example 2: React Blog Platform with Node.js API

**Goal:** Create a new blog platform with a React frontend and a Node.js/Express backend API.

1.  **User:** (Activates `👑 Roo Commander`)
    > "Start a new project called 'react-node-blog'. It needs a React frontend and a Node.js/Express API for managing blog posts."

2.  **Roo Commander:** Delegates to `🚦 Project Onboarding`. *(User approves)*
3.  **Project Onboarding:** Clarifies "New Project". Gets project name 'react-node-blog'.
4.  **Project Onboarding:** Delegates to `🔍 Discovery Agent` (TASK-DISC-...) for requirements (post structure, user roles, API needs, UI features). *(User approves)*
5.  **Discovery Agent:** Interacts with User, logs interactions/summary to its task log (`tasks/TASK-DISC-...md`), saves final requirements to `planning/requirements.md` via `secretary`. *(User approves writes)* Reports completion.
6.  **Project Onboarding:** Delegates to `✨ Project Initializer` (TASK-INIT-...) to set up structure (including `ROO_COMMANDER_SYSTEM.md`, `src/frontend`, `src/backend`, journal dirs). *(User approves)*
7.  **Project Initializer:** Creates dirs, inits Git, creates root files via `secretary`. *(User approves writes)* Reports completion.
8.  **Project Onboarding:** Reports back to `👑 Roo Commander`.
9.  **Roo Commander:** (Takes over)
    > "Project 'react-node-blog' initialized. Requirements gathered. This is more complex, so I'll involve the Project Manager and Technical Architect."
    > Delegates planning to `📋 Project Manager` (TASK-PM-...) using `new_task`: "🎯 Create a project plan and WBS for 'react-node-blog' based on `planning/requirements.md`. Delegate initial architecture design. Initialize task log..."
    > *(User approves `new_task`)*

10. **Project Manager:**
    > Initializes its task log (`tasks/TASK-PM-...md`) via `secretary`. *(User approves)*
    > Reads requirements.
    > Creates initial `planning/project_plan.md` content (task list, maybe simple WBS). Delegates save to `secretary`. *(User approves)*
    > Delegates architecture design to `🏗️ Technical Architect` (TASK-ARCH-...) using `new_task`: "🎯 Design architecture for 'react-node-blog' based on `planning/requirements.md`. Document in `planning/architecture.md` and log key decisions in `decisions/`. Initialize task log..." *(User approves)*
    > Logs delegation in its own task log via `secretary`. *(User approves)*

11. **Technical Architect:**
    > Initializes its task log (`tasks/TASK-ARCH-...md`) via `secretary`. *(User approves)*
    > Reads requirements. Designs architecture (e.g., REST API, React SPA, DB choice).
    > Logs design progress in its task log via `secretary`. *(User approves)*
    > Makes a key decision (e.g., use PostgreSQL). Delegates creation of `decisions/YYYYMMDD-database-choice.md` to `secretary`. *(User approves)* Logs decision reference in task log via `secretary`. *(User approves)*
    > Creates `planning/architecture.md` content. Delegates save to `secretary`. *(User approves)*
    > Requests diagram update from `📊 Diagramer` via `new_task`. *(User approves)*
    > Logs completion in its task log via `secretary`. *(User approves)*
    > Reports completion to `Project Manager`.

12. **Project Manager:** (Receives Architect completion)
    > Logs Architect completion in its task log via `secretary`. *(User approves)*
    > Breaks down implementation into tasks based on plan/architecture.
    > Delegates API implementation to `☁️ API Developer` (TASK-API-...) using `new_task`. *(User approves)*
    > Delegates Frontend implementation to `⚛️ React Specialist` (TASK-FE-...) using `new_task`. *(User approves)*
    > Logs delegations in its task log via `secretary`. *(User approves)*
    > Reports status update (planning complete, dev tasks delegated) to `👑 Roo Commander`.

13. **API Developer / React Specialist:** (Work in parallel)
    > Initialize their respective task logs (`tasks/TASK-API-...md`, `tasks/TASK-FE-...md`) via `secretary`. *(User approves)*
    > Implement features, write code (`write_to_file`), run tests (`execute_command`), log progress/details in their task logs via `secretary`. *(User approves writes/commands)*
    > Report completion to `Project Manager`.

14. **Project Manager:** Monitors task logs, coordinates, reports final completion (or blockers) to `👑 Roo Commander`.
15. **Roo Commander:** Reviews overall status, reports final outcome to User.

---