# 🚀 Roo Code Website Development Modes

This repository contains a set of sophisticated custom modes for Roo Code, designed to work together as a multi-agent system for planning, developing, testing, and deploying websites.

This system utilizes a hierarchical approach with specialized modes coordinated by a central `roo-commander`.

**Note:** This is an advanced setup. Understanding Roo Code's core concepts (modes, tools, delegation) is recommended.

## ✨ Core Concepts

This mode set operates on a few key principles:

1.  **Orchestration (`roo-commander`):** You initiate tasks by talking to the `roo-commander`. It understands the high-level goal and delegates tasks to specialist modes.
2.  **Specialization:** Each mode (e.g., `frontend-developer`, `api-developer`, `technical-architect`) has a specific role and expertise.
3.  **Delegation (`new_task`):** Modes assign work to each other using the `new_task` tool, passing necessary context.
4.  **Project Journal (`project_journal/`):** This directory is the central "memory" and communication hub. Modes read context from it and save detailed notes about their work here. **It is crucial that modes reference files within this journal when delegating tasks.**
5.  **Secretary (`secretary`):** A dedicated, simple mode responsible for *all* writes to the `project_journal`. Other modes delegate writing tasks (notes, documents) to the `secretary` to ensure consistency and control.
6.  **Completion Protocol (`attempt_completion`):** When a mode finishes its delegated task, it uses `attempt_completion` to report back, summarizing its work and **explicitly referencing the path(s)** to any notes or documents saved in the `project_journal` via the `secretary`.

## 📂 Getting Started

1.  **Download:** Obtain the `website-modes.json` file (or your customized version) from this repository or your generator website.
2.  **Load Modes:** Follow the instructions for your Roo Code setup to load custom modes from a JSON file. This usually involves:
    *   Opening the Roo Code Prompts Tab (󠮯 icon).
    *   Accessing the Mode settings (󬏿 icon next to "Modes").
    *   Choosing "Edit Global Modes" or "Edit Project Modes".
    *   Copying the JSON content into the appropriate file (`custom_modes.json` for global, `.roomodes` for project-specific).
    *   Saving the file. Roo Code should automatically detect the new modes.
3.  **Verify:** Check the mode dropdown list in the Roo Code chat input to ensure modes like `👑 Roo Commander` are available.

## 🏁 Initiating a Project

**Always start by selecting the `👑 Roo Commander` mode.**

Provide a clear, high-level description of the website project you want to build or modify. The Commander will then initiate the onboarding process.

> **Generic Prompt Structure:**
>
> ```
> Create/Modify a website for [purpose/domain]. Key goals are [goal 1], [goal 2]. [Add any other high-level context like target audience or essential features].
> ```

The `roo-commander` will immediately delegate to the `project-onboarding` mode, which will ask you clarifying questions to determine if it's a new or existing project and gather initial context.

## 💡 Example Project Scenarios

Here are examples of how to start different types of website projects:

---

### Scenario 1: Simple Static Portfolio Website

**Goal:** Create a basic, single-page website to showcase personal projects.

> **Example Initial Prompt to `👑 Roo Commander`:**
>
> ```
> Build a simple one-page portfolio website for a web developer. It should have sections for About Me, Projects (with placeholders for images/links), and Contact Info. Use clean HTML, CSS, and maybe a little JavaScript for basic interactions.
> ```

*   **Initial Workflow:**
    1.  `roo-commander` receives the prompt.
    2.  Delegates to `project-onboarding`.
    3.  `project-onboarding` asks: "New or existing project?". You reply "New".
    4.  `project-onboarding` asks for a project name (e.g., "my-portfolio").
    5.  `project-onboarding` delegates requirements gathering to `discovery-agent`.
    6.  `discovery-agent` asks you clarifying questions about the portfolio content, style, etc.
    7.  `discovery-agent` delegates saving requirements to `secretary` (`project_journal/planning/requirements.md`).
    8.  `project-onboarding` delegates project structure creation to `project-initializer` (creates `./my-portfolio/` dir, basic `src`, `docs`, `project_journal` folders, `README.md`, `.gitignore`, runs `git init`).
    9.  `project-initializer` delegates saving its setup notes to `secretary`.
    10. `project-onboarding` reports completion back to `roo-commander`.
*   **Expected Initial Outcome:**
    *   A new directory `./my-portfolio/` created.
    *   Basic folder structure inside (`src/`, `docs/`, `project_journal/planning/`, `project_journal/technical_notes/`, etc.).
    *   A `project_journal/planning/requirements.md` file containing the details gathered by the `discovery-agent`.
    *   Technical notes saved by the `project-initializer` regarding the setup.
    *   The `roo-commander` is ready to delegate the next steps (e.g., detailed planning to `project-manager` or architecture to `technical-architect`).

---

### Scenario 2: Blog with Backend (e.g., PHP/Laravel)

**Goal:** Create a dynamic blog website where posts can be managed via a simple backend.

> **Example Initial Prompt to `👑 Roo Commander`:**
>
> ```
> Develop a blog website. The frontend should display posts (title, content, author, date). There needs to be a backend, preferably using PHP and Laravel, to manage creating, editing, and deleting posts (authentication for admin actions is required).
> ```

*   **Initial Workflow:** Similar to Scenario 1 (Commander -> Onboarding -> Discovery -> Initializer). The `discovery-agent` will focus questions on blog features, admin requirements, data needed per post, etc. The `project-initializer` might create a basic Laravel project structure using `execute_command` (e.g., `laravel new my-blog`) in addition to the journal setup.
*   **Expected Initial Outcome:**
    *   A new directory `./my-blog/` (potentially with basic Laravel structure).
    *   `project_journal/` structure created within it.
    *   `project_journal/planning/requirements.md` detailing blog features, admin requirements, etc.
    *   Technical notes from the initializer.
    *   `roo-commander` ready for planning (likely involving `technical-architect`, `project-manager`, `database-specialist`).

---

### Scenario 3: Interactive SPA (e.g., React)

**Goal:** Build a single-page application using React to display data fetched from an external API.

> **Example Initial Prompt to `👑 Roo Commander`:**
>
> ```
> Create an interactive Single Page Application (SPA) using React. It needs to fetch user data from `https://api.example.com/users` and display a list of user profiles with their names and emails. Include a simple search bar to filter users by name.
> ```

*   **Initial Workflow:** Similar again (Commander -> Onboarding -> Discovery -> Initializer). Discovery focuses on UI interaction, API details, search functionality. Initializer might use `execute_command` to run `npx create-react-app my-react-app --template typescript` alongside setting up the journal.
*   **Expected Initial Outcome:**
    *   A new directory `./my-react-app/` with basic React/TS structure.
    *   `project_journal/` structure created.
    *   `project_journal/planning/requirements.md` detailing SPA features, API endpoint, filtering logic.
    *   Technical notes from the initializer.
    *   `roo-commander` ready for planning (likely involving `technical-architect` for structure, `project-manager` for tasks, then `react-specialist` / `frontend-developer`).

---

### Scenario 4: Add Feature to Existing Website

**Goal:** Add a new 'wishlist' feature to an existing e-commerce site.

> **Example Initial Prompt to `👑 Roo Commander`:**
>
> ```
> I need to add a 'wishlist' feature to my existing e-commerce project located at `./my-online-shop`. Users should be able to add products to a wishlist, view their wishlist, and remove items. The backend likely needs API endpoints and database changes.
> ```

*   **Initial Workflow:**
    1.  `roo-commander` receives the prompt.
    2.  Delegates to `project-onboarding`.
    3.  `project-onboarding` asks: "New or existing project?". You reply "Existing".
    4.  `project-onboarding` asks for the project path. You provide `./my-online-shop`.
    5.  `project-onboarding` *might* ask for optional context paths.
    6.  `project-onboarding` uses `list_files` and attempts `read_file` on key files in `./my-online-shop` to understand the project type.
    7.  `project-onboarding` checks for `project_journal/`. If missing, delegates creation to `project-initializer`.
    8.  `project-onboarding` reports completion back to `roo-commander`.
*   **Expected Initial Outcome:**
    *   No *new* project directory created (it uses the existing `./my-online-shop`).
    *   The `project_journal/` directory inside `./my-online-shop` is confirmed to exist (or created if it was missing).
    *   An `attempt_completion` message from `project-onboarding` to `roo-commander` summarizing the context found (e.g., "Context gathered for existing project at ./my-online-shop. Appears to be a React/Node project. Journal ensured at project_journal/. Ready for planning the 'wishlist' feature.").
    *   The `roo-commander` is now ready to delegate planning for the *new feature* based on your initial request (e.g., involving `discovery-agent` specifically for wishlist details, then `technical-architect`, `project-manager`, etc.).

---

## Next Steps

After the initial onboarding phase described above, the `roo-commander` (often guided by you or potentially the `project-manager`) will proceed to delegate tasks for:

*   Detailed Architecture Design (`technical-architect`)
*   Work Breakdown Structure / Task Planning (`project-manager`)
*   UI/UX Design (`ui-designer`)
*   Backend Development (`api-developer`, `database-specialist`, framework specialists)
*   Frontend Development (`frontend-developer`, framework specialists)
*   Testing (`integration-tester`, `bug-fixer`)
*   Deployment (`devops-manager`, `cicd-specialist`, `infrastructure-specialist`)
*   ...and other relevant steps based on the project plan.

Remember to interact with the modes when they ask questions (`ask_followup_question`) and review the results (`attempt_completion`) of delegated tasks, especially the references to saved notes in the `project_journal`.

## ⚠️ Important Notes

*   **Journaling is Key:** The quality of the project depends heavily on modes diligently saving their notes via the `secretary`. This shared context is vital.
*   **Clear Prompts:** Provide clear instructions, especially when initially prompting the `roo-commander` and when responding to clarifying questions from modes like `discovery-agent`.
*   **Review Outputs:** Pay attention to the `attempt_completion` messages, especially the paths to saved notes/documents. Use `read_file` to check the contents if needed.
*   **Patience:** Complex tasks are broken down. Allow the system time to delegate, execute, and report back through the defined workflow.

Happy building! 🚀
