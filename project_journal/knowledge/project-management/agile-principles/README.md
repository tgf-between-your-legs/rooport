# 🚀 MDTM for Agile Principles: A Practical Guide

**Version:** 1.0
**Date:** 2025-04-05

## 1. Overview: Agile Values Meet Markdown Tasks ✨

Welcome! This guide shows how to implement **Agile Principles** using the **Markdown-Driven Task Management (MDTM)** system. We adapt MDTM's core ideas (Markdown files 📄, YAML metadata ⚙️, Git tracking <0xF0><0x9F><0x9A><0xB2>️) to support the iterative, collaborative, and value-focused nature of Agile software development.

**The Core Idea:** Leverage MDTM's flexibility to manage work items like **User Stories** 📖, **Tasks** 🛠️, and **Bugs** 🐞 within an iterative flow. Organize work primarily by **feature or value stream** 📂, prioritize based on value 🏆, and track progress through flexible workflow statuses reflected in YAML. Embrace change and frequent delivery, supported by a version-controlled task system living alongside your code.

This approach provides a lightweight, developer-centric way to manage Agile projects, especially effective when paired with AI coding assistants 🤖 requiring clear, manageable work chunks.

**Agile Principles We Support:**
*   **Individuals and interactions** over processes and tools (MDTM is simple, focus is on content).
*   **Working software** over comprehensive documentation (Tasks linked closely to code).
*   **Customer collaboration** over contract negotiation (User stories focus on user value).
*   **Responding to change** over following a plan (Flexible structure, easy prioritization changes).

**❗ Note:** MDTM provides the *system for tracking work items*. Agile ceremonies like Stand-ups, Sprint Planning, Reviews, and Retrospectives are **team processes** that *use* the information stored in these MDTM files.

## 2. Why Adapt MDTM for Agile? 🤔

MDTM aligns well with Agile principles:

*   **🧩 Seamless IDE Integration:** Keep focus within the development environment.
*   **🔄 Supports Iteration:** Easily track tasks through `To Do` -> `In Progress` -> `Done` cycles, potentially within sprints/iterations defined by YAML fields or team cadence.
*   **💎 Focus on Value:** Feature-based organization and User Story formats keep the focus on delivering value to the end-user.
*   **🔧 Flexibility & Adaptability:** Easily change priorities, add/remove tasks, refine stories, and adjust workflows by modifying simple text files.
*   ** Git Transparency:** Full history of task evolution, estimations, and status changes tracked via version control. Collaboration via branching/merging is possible.
*   **🤖 AI-Friendly:** Small, well-defined tasks/stories with clear Acceptance Criteria are ideal inputs for AI coding assistants.
*   **🗣️ Encourages Collaboration:** Task files can become points of discussion (via commit messages, PRs, or just shared reading).

## 3. Core Concepts in Agile MDTM 🧱

This adaptation builds on MDTM basics:

1.  **📄 Task Files:** `.md` files representing User Stories, Tasks, Bugs, Spikes, etc.
2.  **⚙️ YAML Front Matter:** Structured metadata including ID, title, status, type, priority, effort (story points), and potentially iteration/sprint identifiers.
3.  **📂 Feature-Based Folder Structure (Recommended):** Organizing `tasks/` by feature or value stream promotes vertical slicing and aligns with delivering increments of value. Sprint-based folders are possible but often less flexible.
4.  **📖 User Story Format:** Utilizing the standard "As a..., I want..., So that..." format within the Markdown body.
5.  **✅ Acceptance Criteria:** Clear, testable criteria (checklists) defining "Done".
6.  **<0xF0><0x9F><0x9A><0xB2>️ Version Control (Git):** Tracking everything.

## 4. 🗂️ Recommended Directory Structure: Feature/Value Streams

Organize by *what* value you are delivering, not *when* (Sprints can be tracked via YAML).

```
PROJECT_ROOT/
├── src/                     # Source Code
├── docs/                    # Supporting Docs (User Personas, High-Level Designs)
├── tasks/                   # 👈 **Main MDTM Directory**
│   ├── _templates/          # 📄 Optional: Standard task/story templates
│   │   ├── 📖_user_story.md
│   │   ├── 🛠️_task.md
│   │   └── 🐞_bug.md
│   │
│   ├── BACKLOG/             # 📥 Optional: Contains unsorted/unrefined items
│   │   └── IDEA_new_reporting_feature.md
│   │
│   ├── FEATURE_authentication/  # 🔑 Feature: Authentication (Value Stream)
│   │   ├── _overview.md       # 🗺️ Optional: Epic/Feature summary
│   │   ├── 001_📖_user_login.md   # 📖 User Story
│   │   ├── 002_🛠️_setup_auth_db.md # 🛠️ Technical Task supporting the story
│   │   └── 003_📖_password_reset.md # 📖 User Story
│   │
│   ├── FEATURE_user_profile/  # 👤 Feature: User Profile
│   │   ├── _overview.md
│   │   └── 004_📖_view_profile_data.md
│   │
│   └── AREA_tech_debt/        # 🧹 Area: Non-feature work
│       └── 005_🧹_refactor_legacy_api.md
│
├── archive/                 # 📦 Optional: Completed items (mirrors feature structure)
│   └── ...
└── README.md```

**Key Structural Points:**
*   ✅ **Feature Folders:** Group related User Stories and supporting Tasks under feature/component folders (e.g., `FEATURE_authentication`).
*   ✅ **Backlog Folder:** An optional place for ideas or items not yet refined or prioritized for a specific feature/sprint.
*   ✅ **Overview Files (`_overview.md`):** Optional Epic/Feature descriptions linking child stories/tasks.
*   ✅ **Templates (`_templates/`):** Highly recommended for consistency (User Story, Task, Bug).
*   ✅ **Archive (`archive/`):** Keep completed work organized.

## 5. 📄 Task File Naming Conventions

Include type emojis for quick visual identification.

**Format:** `NNN_🌀_short_description.md`

*   **`NNN`:** Sequence number (`001`, `002`, etc.). Can be unique per feature folder or project-wide.
*   **`_🌀_`:** Emoji for the item **Type** (see Type Emojis below), enclosed in underscores.
*   **`short_description`:** Brief, lowercase, underscore-separated name.
*   **`.md`:** Markdown extension.

**Type Emojis (`🌀`):**
*   `📖` : User Story
*   `🛠️` : Task (Technical task supporting a story or stand-alone)
*   `🐞` : Bug
*   `🧹` : Chore / Refactor / Tech Debt
*   `💡` : Spike / Research
*   `🗺️` : Epic / Feature Overview

**Examples:**
*   `001_📖_user_login.md`
*   `002_🛠️_setup_auth_db.md`
*   `005_🧹_refactor_legacy_api.md`

## 6. ⚙️ YAML Front Matter: Supporting Agile Workflows

Tailor YAML fields for Agile concepts.

```yaml
---
# 🆔 Task Identification & Core Metadata
id:             # REQUIRED. Unique ID (e.g., STORY-001, TASK-002, BUG-003). Convention: {TYPE_PREFIX}-{NNN}
title:          # REQUIRED. Human-readable title. "As a User, I want to log in securely"
status:         # REQUIRED. Current workflow state. "🟡 Backlog", "🔵 In Progress", "🟢 Done". See Statuses below.
type:           # REQUIRED. Work item type. "📖 User Story", "🛠️ Task", "🐞 Bug". See Types below.

# 🏆 Prioritization & Value
priority:       # Recommended. Importance/Order. "🔼 High", "▶️ Medium", "🔽 Low". See Priorities below.
value_score:    # Optional. Business value estimate (e.g., 1-10, MoSCoW).
risk_score:     # Optional. Risk estimate (e.g., 1-10).

# ⏳ Effort & Iteration Tracking
estimated_effort: # Recommended. Story Points or T-Shirt size. "3", "5", "M", "L".
iteration:      # Optional. Sprint/Iteration name or number. "Sprint 3", "Iteration 2025.04"
# created_date:   # Optional. YYYY-MM-DD
updated_date:   # Recommended. YYYY-MM-DD

# 🧑‍💻 Assignment & Collaboration
assigned_to:    # Optional. Who is working on it. "🧑‍💻 User:DevTeamA", "🤖 AI+Pair:Bob"
reporter:       # Optional. Who created/reported it.

# 🔗 Relationships & Context
parent_feature: # Optional. Path/ID of parent Feature/Epic overview file. "FEATURE_authentication/_overview.md"
depends_on:     # Optional. List of task/story IDs this waits for. ["TASK-002"]
related_docs:   # Optional. Links to Personas, Designs, etc. ["docs/personas.md#returning_user"]
tags:           # Optional. Keywords. ["authentication", "security", "mvp"]

# ✅ Definition of Done Checklist (Optional - Team Standard)
# dod_checklist: # Example - can use body instead
#   - "[ ] Code Complete"
#   - "[ ] Unit Tests Pass (>80%)"
#   - "[ ] Code Reviewed"
#   - "[ ] AC Met"
#   - "[ ] Deployed to Staging"
---

# User Story / Task Title (matches YAML title)

## Description / User Story 📖 / Task Details 🛠️
... Markdown Body: User Story format, Task description, Bug details ...

## Acceptance Criteria ✅
... Checklists defining Done for THIS item ...
```

**Key Agile YAML Fields:**
*   `status:`: Drives the workflow board visualization.
*   `type:`: Distinguishes stories, tasks, bugs.
*   `priority:`: For backlog ordering.
*   `estimated_effort:`: For capacity planning (Story Points/Size).
*   `iteration:`: Optional field to group work by Sprint/Iteration if not using folders.
*   `parent_feature:`: Links items to larger value streams/epics.

## 7. 🏷️ Standardized Field Values & Emojis

Use consistent values for clarity and filtering.

*   **Statuses (`status:` - Example Flow):**
    *   `⚪ Icebox`: 🧊 Idea, not planned.
    *   `🟡 Backlog`: 📥 Refined, prioritized, ready for selection.
    *   `🔵 Selected for Iteration`: 🎯 Committed to current Sprint/Iteration.
    *   `🔵 In Progress`: 🏗️ Actively being worked on.
    *   `🟣 Review / QA`: 👀 Code complete, needs review/testing.
    *   `🟢 Done`: ✅ Meets Definition of Done, accepted.
*   **Types (`type:`):** `📖 User Story`, `🛠️ Task`, `🐞 Bug`, `🧹 Chore`, `💡 Spike`, `🗺️ Epic/Feature`.
*   **Priorities (`priority:`):** `🔥 Highest`, `🔼 High`, `▶️ Medium`, `🔽 Low`. (Or use numerical order).

## 8. 📝 Markdown Body: Agile Artifacts

Structure the body for common Agile items.

*   **User Story (`## User Story 📖`):**
    ```markdown
    As a [type of user],
    I want [to perform some action],
    So that [I can achieve some goal/benefit].
    ```
*   **Task Description (`## Task Details 🛠️`):** Explain the technical work needed, often linking to the User Story it supports.
*   **Bug Report (`## Bug Report 🐞`):** Include:
    *   What happened?
    *   Steps to Reproduce 👣
    *   Expected vs. Actual Behavior
    *   Environment 🖥️
*   **Acceptance Criteria (`## Acceptance Criteria ✅`):** **ESSENTIAL.** Use specific, testable checklists (`- [ ]`). These define "Done" for the *individual work item*.
    *   `- [ ] Given [context] When [action] Then [outcome].` (BDD-style optional)
    *   `- [ ] Login button is visible.`
    *   `- [ ] Clicking login with valid credentials redirects to dashboard.`
    *   `- [ ] Clicking login with invalid credentials shows error message.`
*   **Notes / Discussion (`## Notes / Discussion 💬`):** Technical considerations, questions, decisions made.

## 9. 📄 Example Templates

Place these in `tasks/_templates/`.

### `📖_user_story.md`

```markdown
---
# 🆔 Task Identification & Core Metadata
id:             # << GENERATE_UNIQUE_ID (e.g., STORY-NNN) >>
title:          # << As a [User], I want [Action], so that [Benefit] >>
status:         "🟡 Backlog"
type:           "📖 User Story"

# 🏆 Prioritization & Value
priority:       "▶️ Medium"
# value_score:    # Optional

# ⏳ Effort & Iteration Tracking
estimated_effort: # << Story Points / T-Shirt Size >>
# iteration:      # Optional

# 🧑‍💻 Assignment & Collaboration
# assigned_to:
reporter:       # << Who requested/identified? >>

# 🔗 Relationships & Context
parent_feature: # << Path to FEATURE/_overview.md >>
# depends_on:     []
related_docs:   [] # Links to Personas, Mockups
tags:           [] # << Keywords >>
---

# << As a [User], I want [Action], so that [Benefit] >>

## User Story 📖

> As a **[Type of User, e.g., Registered User]**,
> I want **[To perform some action, e.g., to log in using my email and password]**,
> So that **[I can achieve some goal/benefit, e.g., I can access my personalized dashboard]**.

## Description / Notes 💬
(Optional: Add context, assumptions, technical notes, links to designs)

## Acceptance Criteria ✅
*   - [ ] Given I am on the login page
    When I enter my valid email and password
    And click 'Login'
    Then I am redirected to my dashboard page.
*   - [ ] Given I am on the login page
    When I enter an invalid email or password
    And click 'Login'
    Then I see an error message "Invalid credentials".
*   - [ ] Login button is disabled if email or password fields are empty.
*   - [ ] Password field masks input characters.
```

### `🛠️_task.md`

```markdown
---
# 🆔 Task Identification & Core Metadata
id:             # << GENERATE_UNIQUE_ID (e.g., TASK-NNN) >>
title:          # << TASK: Concise technical description >>
status:         "🟡 Backlog"
type:           "🛠️ Task"

# 🏆 Prioritization & Value
priority:       "▶️ Medium"

# ⏳ Effort & Iteration Tracking
estimated_effort: # << Hours / Size >>
# iteration:

# 🧑‍💻 Assignment & Collaboration
# assigned_to:

# 🔗 Relationships & Context
parent_story:   # Optional: Link to User Story ID this supports
parent_feature: # << Path to FEATURE/_overview.md >>
# depends_on:     []
tags:           ["technical", ...] # << Keywords >>
---

# << TASK: Concise technical description >>

## Task Details 🛠️
Describe the technical work needed. Why is it necessary? What User Story does it support (link if applicable)?
*Example:* "Set up the PostgreSQL database schema for the authentication feature, including `users` and `sessions` tables as per [Design Doc Section X](...)."

## Acceptance Criteria ✅
*   - [ ] Database migration script exists and runs successfully.
*   - [ ] `users` table created with specified columns (id, email, password_hash, created_at).
*   - [ ] `sessions` table created with specified columns.
*   - [ ] Necessary indexes are created.
```

*(Create a similar simple template for `🐞_bug.md` based on the Bug Report structure above).*

## 10. 🔄 Agile Workflow with MDTM

*   **Backlog Refinement:** Review items in `BACKLOG/` or feature folders with `status: 🟡 Backlog`. Add details, estimate effort (`estimated_effort`), assign priority.
*   **Iteration Planning:** Select items for the next iteration/sprint. Update their `status: 🔵 Selected for Iteration` and optionally set the `iteration:` field.
*   **Daily Work:** Team members pick tasks from 'Selected'. Update `status: 🔵 In Progress` and `assigned_to`.
    *   *Stand-ups:* Team discusses progress based on tasks 'In Progress', identifies blockers (`status: ⚪ Blocked`).
*   **Development & Review:** Code is written, tests pass. Update `status: 🟣 Review / QA`. Another team member reviews against AC and Definition of Done.
*   **Completion:** Once approved and potentially deployed/merged, update `status: 🟢 Done`.
*   **Review/Demo:** Show completed (`🟢 Done`) items from the iteration.
*   **Retrospective:** Discuss the process, potentially identifying improvements tracked as `🧹 Chore` tasks.

## 11. Best Practices for Agile MDTM 👍

*   **🧱 Small, Vertical Slices:** Prefer User Stories that deliver end-to-end value, even if small. Break down large stories.
*   **✅ Clear Acceptance Criteria:** Essential for shared understanding and testing (manual or automated).
*   **💾 Commit Frequently:** Treat task file updates like code changes – commit status changes, AC updates, notes often.
*   **🗣️ Foster Collaboration:** Use task files as discussion points during planning, stand-ups, and reviews. Link tasks in commit messages or PRs.
*   **📊 Visualize (with IDE/Tools):** Use IDE extensions or simple scripts to parse MDTM files and create Kanban boards or reports based on YAML fields (`status`, `iteration`, `assigned_to`).
*   **⚖️ Estimate Consistently:** Whether using Story Points or T-Shirt sizes, apply estimation consistently.
*   **🧹 Keep Backlog Tidy:** Regularly review and refine the backlog. Archive completed work.

## 12. 💡 IDE Integration: Powering the Flow

An effective IDE setup enhances Agile MDTM:

*   **📊 Kanban Board View:** Visualize tasks based on `status` columns, perhaps filterable by `iteration` or `assigned_to`. Allow drag-and-drop to update status.
*   **📝 Quick Entry/Templates:** Easily create new Stories/Tasks/Bugs from predefined templates.
*   **⚙️ YAML Validation/Completion:** Help ensure correct field usage and values.
*   **🔍 Powerful Filtering/Searching:** Quickly find items based on tags, status, priority, assignee, iteration.
*   **🔗 Linking:** Easily create links between stories, tasks, code files, and commits.

## 13. Conclusion ✅

Using **MDTM for Agile Principles** provides a flexible, developer-centric, and repository-integrated way to manage iterative work. By organizing tasks by **feature/value**, using clear **User Story formats**, defining explicit **Acceptance Criteria**, and tracking progress through **YAML statuses**, teams can effectively implement Agile workflows. This approach keeps task management simple, transparent, version-controlled, and close to the code, making it an excellent fit for modern development practices, including AI-assisted coding.