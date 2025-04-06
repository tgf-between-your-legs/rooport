# 🗂️ Markdown-Driven Task Management (MDTM) - Feature Structure

**Version:** 1.0
**Date:** 2025-04-05

## 1. Overview: Tasks Living with Your Code ✨

Welcome to **Markdown-Driven Task Management (MDTM) - Feature Structure**! This is a practical, lightweight way to manage your software project tasks directly within your codebase using simple Markdown (`.md`) files.

**The Core Idea:** Treat your project tasks (features, bugs, chores) like documentation or configuration – keep them **co-located** 🏠 with your source code, make them **readable by humans** 🧑‍💻 and **understandable by AI assistants** 🤖, and organize them logically **by feature or component** 📂.

Instead of context-switching to external tools, MDTM uses:
*   **Markdown Files (`.md`)** 📄: Each file is a single task.
*   **YAML Front Matter (`---`)** ⚙️: Structured data (status, priority, assignee) at the top of each file for machines (and humans!) to read.
*   **Feature-Based Folders** 🗂️: Grouping task files by the feature or component they belong to.
*   **Version Control (Git)** <0xF0><0x9F><0x9A><0xB2>️: Tracking task changes alongside code changes.

This approach is particularly effective when working with AI coding assistants integrated into your IDE, as it provides clear, structured context directly within the project environment.

## 2. Why Choose MDTM - Feature Structure? 🤔

This specific flavor of MDTM offers significant benefits:

*   **🧩 Seamless IDE Integration:** Tasks live where you work. No need to jump to separate websites or apps.
*   **🧠 Direct AI Parsability:** Structured YAML + Markdown is ideal for AI assistants to understand requirements, context, and status accurately.
*   **🎯 Enhanced AI Context:** Provides focused context (`related_docs` links, clear descriptions) for better AI prompts and code generation.
*   **📈 Scalability:** Organizes tasks logically by feature, making it manageable even as the project grows large. Easily navigate work for specific components.
*   **🔄 Aligned with Iterative Workflows:** Perfectly suits the `generate -> review -> test -> refine` loop common in AI development. Track micro-steps within a task file.
*   ** Git Transparency & Traceability:** Every change to a task is tracked by Git. See who changed what, when, and why – just like your code.
*   **⚙️ Simplicity & Low Overhead:** Uses tools you already know (text editor, Markdown, Git). No complex setup needed.
*   **🔧 Flexibility & Adaptability:** Easily add custom fields or tweak workflows by modifying the YAML structure and conventions.
*   **🏠 Co-location:** Tasks live near the code they affect, improving context and reducing information silos.

## 3. Core Concepts 🧱

MDTM Feature Structure relies on these building blocks:

1.  **📄 Task Files:** Standard Markdown (`.md`) files, each representing one actionable work item (e.g., `001-create-login-button.md`).
2.  **⚙️ YAML Front Matter:** A block at the very top of each task file, enclosed by `---`, containing `key: value` pairs for structured metadata.
3.  **🗂️ Feature-Based Folder Structure:** A main `tasks/` directory at the project root, with subdirectories named after features, epics, or major components (e.g., `tasks/authentication/`, `tasks/user-profile/`). Task files reside within these feature folders.
4.  **<0xF0><0x9F><0x9A><0xB2>️ Version Control (Git):** The entire `tasks/` directory and its contents are committed to your Git repository.

## 4. How It Works: The Workflow ⚙️➡️🚀

Here’s a typical lifecycle of a task using MDTM Feature Structure:

1.  **➕ Task Creation:** Identify a piece of work. Create a new `.md` file inside the relevant feature folder (e.g., `tasks/authentication/001_login_ui.md`). Use a consistent naming convention (e.g., `NNN_short_description.md`).
2.  **✍️ Task Definition:**
    *   Fill in the **YAML front matter** with initial metadata (e.g., assign a unique `id`, set `status: To Do`, `priority: Medium`, link `related_docs`).
    *   Write a clear **Description** in the Markdown body.
    *   Define specific **Acceptance Criteria** using Markdown checklists (`- [ ]`).
3.  **▶️ Assignment & Start:** Assign the task (`assigned_to: AI` or `assigned_to: User:DevName`). Update the `status` to `In Progress` (or `Generating` if the AI is starting). Commit the new task file.
4.  **🤖➡️💻 AI Interaction (If Applicable):**
    *   Prompt your AI assistant, clearly referencing the task file path or ID.
    *   Instruct the AI to use the task file (including `related_docs`) for requirements and context.
5.  **🔄 Development & Updates:**
    *   The AI (or human developer) works on the task.
    *   Notes, code snippets, or sub-task checklist updates (`- [x]`) might be added to the Markdown body.
    *   The `status` is updated as progress is made (e.g., `Generating` -> `Review`). Commit changes frequently.
6.  **✅ Review & Testing:**
    *   The designated reviewer examines the work against the `Acceptance Criteria` checklist in the task file.
    *   Feedback can be added as comments in the Markdown body.
    *   Checklist items are marked complete (`- [x]`). Update `status` (e.g., `Testing`).
7.  **♻️ Iteration:** If changes are needed, update the status back to `In Progress` or similar, add notes, and repeat the relevant steps.
8.  **🎉 Completion:** Once all Acceptance Criteria are met and the work is integrated, update the final `status` to `Done`. Commit the final state.
9.  **🧹 Archival (Optional):** Periodically move completed (`Done`) task files from feature folders to a separate `archive/` directory to keep active areas clean.
10. **💡 IDE Support:** Your AI-integrated IDE should enhance this workflow by parsing these files to:
    *   Display filterable/sortable task lists or Kanban-like boards.
    *   Validate required YAML fields.
    *   Provide UI elements to easily update task status.
    *   Help link tasks to code or prompts.

## 5. Detailed Components 🔍

### 5.1. Folder Structure Example

Organize tasks logically within a top-level `tasks/` directory:

```
PROJECT_ROOT/
├── src/
│   └── ... your source code ...
├── docs/
│   ├── PRD.md
│   └── API_Spec.md
├── tasks/                      # <== Main directory for all tasks
│   ├── _templates/             # Optional: Templates for different task types
│   │   ├── feature_task.md
│   │   └── bug_report.md
│   ├── authentication/         # <== Folder for the Authentication Feature
│   │   ├── _overview.md        # Optional: Markdown summary of the feature/epic
│   │   ├── 001_login_ui.md     # <== Task file
│   │   ├── 002_login_logic.md
│   │   └── 003_password_reset.md
│   ├── user_profile/           # <== Folder for User Profile Feature
│   │   ├── _overview.md
│   │   └── 004_display_data.md
│   └── bugs/                   # <== Folder for bug reports
│       └── 005_login_crash_on_safari.md
├── archive/                    # <== Optional: Completed tasks moved here
│   └── authentication/
│       └── ... completed auth tasks ...
└── README.md
```

### 5.2. Task File (`.md`) Anatomy

Each task file combines machine-readable metadata with human-readable details:

```markdown
---
# YAML Front Matter (Metadata for machines & humans)
id: FEAT-AUTH-001
title: "Implement User Login UI (Vue)"
status: "To Do"  # <-- CRITICAL for workflow tracking
priority: High
type: Feature
assigned_to: "AI"
created_date: 2025-04-05
updated_date: 2025-04-05
estimated_effort: "M"
parent_task: "authentication/_overview.md" # Links to feature overview
related_docs:
  - "docs/PRD.md#Login Requirements"
  - "docs/DesignMockups.md#Login Screen"
tags: ["ui", "vue", "authentication", "frontend"]
---

# Implement User Login UI (Vue)  <== Human-friendly title (optional redundancy)

## Description ✍️
Detailed explanation of the task goals, background, and rationale.
Why is this needed? What problem does it solve?

## Acceptance Criteria ✅
Use checklists for clear, verifiable completion conditions.
- [ ] Criterion 1: Component renders correctly per mockups.
- [ ] Criterion 2: Input fields capture data.
- [ ] Criterion 3: Basic validation implemented.
- [ ] Criterion 4: Button click handler exists and is stubbed.

## Implementation Notes / Sub-Tasks / Discussion 📝
- Use Vue 3 Composition API.
- Break down steps if needed:
  - [ ] Create component file.
  - [ ] Add input fields.
  - [ ] Add button.
- Link to relevant code: `src/components/auth/LoginView.vue` (once created)

## AI Prompt Log (Optional Traceability) 🤖
```prompt
Generate a Vue 3 Composition API component named 'LoginView.vue'. Include labeled input fields for username (text) and password (password type), and a submit button labeled 'Login'. Add a placeholder link for 'Forgot Password?'. Implement a basic 'handleLogin' method triggered by the button click that logs the input values to the console and prevents default form submission. Include simple non-empty validation on the fields before logging. Use Tailwind CSS for basic styling.
``````

### 5.3. Key YAML Fields (Examples) 🔑

Choose fields relevant to your workflow. Here are common and recommended ones:

*   `id`: (String) **Required.** Unique task identifier (e.g., `FEAT-AUTH-001`, `BUG-123`). *Convention needed!*
*   `title`: (String) **Required.** Concise, human-readable title.
*   `status`: (String) **Required.** Current workflow state. Define a standard set, e.g.:
    *   `To Do`: Not started.
    *   `In Progress`: Actively being worked on (by human).
    *   `Generating`: AI is actively generating code/content for this.
    *   `Review`: Output generated, needs human review.
    *   `Testing`: Passed review, undergoing testing.
    *   `Blocked`: Cannot proceed (add reason in body).
    *   `Done`: Completed and verified.
*   `priority`: (String) Task priority (e.g., `Highest`, `High`, `Medium`, `Low`, `Lowest`).
*   `type`: (String) Category of work (e.g., `Feature`, `Bug`, `Chore`, `Epic`, `Story`, `Spike`, `Refactor`, `Documentation`).
*   `assigned_to`: (String) Who is responsible for the *next* action (e.g., `AI`, `User:Alice`, `Team:Backend`).
*   `created_date`: (Date) `YYYY-MM-DD`. When task was created.
*   `updated_date`: (Date) `YYYY-MM-DD`. When task was last modified.
*   `due_date`: (Date) `YYYY-MM-DD`. Optional target completion date.
*   `estimated_effort`: (String/Number) Size/complexity estimate (e.g., T-Shirt `S`, `M`, `L` or Points `1`, `2`, `3`, `5`).
*   `parent_task`: (String) Path/ID of a parent feature/epic file (e.g., `authentication/_overview.md`). Creates hierarchy.
*   `depends_on`: (List of Strings) List of task `id`s that must be `Done` before this one starts (e.g., `["FEAT-AUTH-002"]`).
*   `related_docs`: (List of Strings) **Crucial for context.** Relative paths to documents or specific sections (e.g., `["docs/PRD.md#section-3.1", "../shared/API.md#auth-endpoint"]`).
*   `tags`: (List of Strings) Keywords for filtering/searching (e.g., `["ui", "performance", "critical"]`).

*(**Consistency is vital!** Agree on standard values and which fields are mandatory).*

## 6. Getting Started Checklist ✔️

1.  **[ ] Create `tasks/` Directory:** Add a `tasks/` folder at the root of your Git repository. Add it to `.gitignore` if needed (e.g., if using specific IDE metadata files you don't want tracked). *Usually, you DO want tasks tracked by Git.*
2.  **[ ] Choose Feature Folders:** Create initial subdirectories within `tasks/` for your main features or components.
3.  **[ ] Define Templates (Optional but Recommended):** Create template `.md` files in `tasks/_templates/` (e.g., `feature.md`, `bug.md`) with standard YAML fields pre-filled.
4.  **[ ] Create Your First Task:** Copy a template or create a new `.md` file in the appropriate feature folder. Assign a unique `id`, set initial `status: To Do`.
5.  **[ ] Define Clearly:** Write a concise `title`, detailed `Description`, and specific `Acceptance Criteria` (checklist). Link related docs/designs.
6.  **[ ] Commit:** Add the new task file to Git and commit it.
7.  **[ ] Integrate with AI/Start Work:** Reference the task file/ID when prompting your AI or starting manual work. Update `status` and `assigned_to`.
8.  **[ ] Track Progress:** Update the `status` field, checklists (`- [x]`), and add notes as work progresses. Commit changes regularly.

## 7. Best Practices for Success 🏆

*   **🤝 Consistency is King:** Agree on and document your standard `status` values, `priority` levels, `type` categories, date formats, and ID conventions. Use templates!
*   **🏷️ Unique & Readable IDs:** Use a clear convention (e.g., `FEAT-AUTH-001`, `BUG-123`).
*   **✅ Define AC Upfront:** Write clear, specific, and testable Acceptance Criteria *before* work begins. How do you know it's *done*?
*   **🤏 Keep Tasks Manageable:** Break down large epics/features into smaller, focused task files. A task should ideally represent a single commit or PR.
*   **🔗 Leverage Linking:** Make heavy use of `related_docs`, `parent_task`, and `depends_on` to build context and relationships. Use inline Markdown links (`[link text](path/to/file)`) too.
*   **💾 Commit Frequently:** Treat task file updates like code changes. Commit them often with meaningful messages, potentially alongside related code changes.
*   **✨ Keep YAML Clean:** Ensure correct YAML syntax (indentation matters!). Use linters if available. Add `# comments` in YAML for clarification if needed.
*   **🤖🔧 Automate/Support via IDE:** Leverage IDE features (see below) to make managing tasks easier – status updates, template usage, validation, visualization.

## 8. IDE Integration: Making MDTM Shine 💡

The real power of MDTM comes alive with good IDE support. Your AI-integrated IDE should ideally:

*   **📊 Task View:** Parse `tasks/**/*.md` files to display interactive lists or Kanban-style boards based on `status`, `priority`, `assignee`, `tags`, etc. Allow filtering and sorting.
*   **📝✅ YAML Assistance:** Provide syntax highlighting, auto-completion, and validation for YAML front matter based on defined standards. Warn about missing required fields.
*   **📄➡️📄 Template Usage:** Offer commands to quickly create new tasks from files in the `_templates/` directory.
*   **🔗🤖 Prompt Context Linking:** Allow easy ways to link a task file/ID to an AI prompt session, and potentially log prompts back to the task file.
*   **▶️⏹️ Status Update UI:** Provide buttons or commands within the IDE (e.g., right-click on file, button in task view) to quickly update the `status` field in the YAML.
*   **⛓️‍💥 Dependency Checks:** Optionally warn if a user tries to start a task whose `depends_on` tasks are not yet `Done`.
*   **👀 Visualization:** Render Mermaid diagrams embedded within task descriptions.

## 9. Conclusion 🚀

**MDTM - Feature Structure** offers a developer-centric, scalable, and AI-friendly approach to task management. By keeping tasks as structured Markdown files within your project repository and organizing them by feature, you create a single source of truth that enhances context, improves traceability, and integrates seamlessly with modern development workflows, especially those involving AI assistants. It's simple, flexible, and puts task management right where the code lives.