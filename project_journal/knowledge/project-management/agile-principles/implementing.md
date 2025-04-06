# 🚀 Implementing Agile Principles with MDTM: A Practical Guide

**Version:** 1.0
**Date:** 2025-04-05

## 1. Introduction: Bringing Agile Values to Markdown Tasks ✨

This guide provides the detailed conventions, structures, and templates for implementing **Agile Principles** using the **Markdown-Driven Task Management (MDTM)** system. We'll show how to use MDTM's file-based approach (Markdown files 📄, YAML metadata ⚙️, Git tracking <0xF0><0x9F><0x9A><0xB2>️) to support iterative development, collaboration, and value delivery.

**The Goal:** To establish a practical, lightweight system for managing Agile work items (User Stories 📖, Tasks 🛠️, Bugs 🐞) directly within your project repository, fostering flexibility and transparency.

**Key Agile Implementation Concepts with MDTM:**
*   **Feature/Value Stream Organization:** Structure folders primarily around delivering increments of value 📂.
*   **Iterative Workflow:** Use YAML `status` fields to track progress through states like Backlog, In Progress, Done.
*   **User-Centric Items:** Employ User Story formats and clear Acceptance Criteria ✅.
*   **Prioritization & Estimation:** Use YAML fields for priority 🏆 and effort (e.g., Story Points) ⏳.
*   **Adaptability:** Leverage the simplicity of text files and Git for easy adjustments to scope, priority, and workflow.

**❗ Reminder:** MDTM provides the *system for tracking*. Agile ceremonies (Stand-ups, Planning, Reviews, Retros) are **team processes** that utilize the information within these MDTM files.

## 2. 🗂️ Directory Structure: Organizing for Value Flow

The recommended structure organizes tasks by the features or value streams they contribute to. Sprints/Iterations are typically tracked via YAML fields rather than folders for greater flexibility.

```
PROJECT_ROOT/
├── src/                     # Source Code
├── docs/                    # Supporting Docs (Personas, Designs, etc.)
├── tasks/                   # 👈 **Main MDTM Directory for Agile Items**
│   ├── _templates/          # 📄 Standard templates (Highly Recommended)
│   │   ├── 📖_user_story.md
│   │   ├── 🛠️_task.md
│   │   ├── 🐞_bug.md
│   │   └── 💡_spike.md
│   │
│   ├── BACKLOG/             # 📥 Optional: Unrefined or unscheduled items
│   │   └── IDEA_gamification_feature.md
│   │
│   ├── FEATURE_authentication/  # 🔑 Feature Area (Value Stream)
│   │   ├── _overview.md       # 🗺️ Optional: Epic/Feature Definition
│   │   ├── 001_📖_user_login_story.md   # 📖 A User Story
│   │   ├── 002_🛠️_setup_auth_db_task.md # 🛠️ Supporting Technical Task
│   │   ├── 003_🐞_incorrect_error_msg_bug.md # 🐞 Related Bug
│   │   └── 004_📖_password_reset_story.md # 📖 Another User Story
│   │
│   ├── FEATURE_user_profile/  # 👤 Another Feature Area
│   │   ├── _overview.md
│   │   └── 005_📖_display_profile_story.md
│   │
│   └── AREA_performance/        # 🧹 Cross-cutting Area (e.g., Tech Debt)
│       └── 006_💡_research_caching_spike.md # 💡 Research Task
│
├── archive/                 # 📦 Optional: Completed items (mirrors feature structure)
│   └── FEATURE_authentication/
│       └── ... (completed items from auth feature)
└── README.md
```

**Key Structural Rules:**
*   ✅ **Feature Folders:** Group related items under `FEATURE_` or `AREA_` prefixed folders.
*   ✅ **Backlog Folder:** Optional home for items not yet ready for a feature backlog or sprint.
*   ✅ **Overview Files (`_overview.md`):** Use for Epic/Feature summaries, linking child items.
*   ✅ **Templates Folder (`_templates/`):** Essential for consistency. Prefix with emoji and underscore.
*   ✅ **Archive (`archive/`):** Maintain structure when archiving completed items.

## 3. 📄 Task File Naming Conventions

Use emojis for instant type recognition.

**Format:** `NNN_🌀_short_description.md`

*   **`NNN`:** Sequence number (`001`, `002`, etc.). Unique within the project or per feature folder.
*   **`_🌀_`:** Emoji for the item **Type** (see Type Emojis below), enclosed in underscores.
*   **`short_description`:** Brief, lowercase, underscore-separated name.
*   **`.md`:** Markdown extension.

**Type Emojis (`🌀`):**
*   `📖` : User Story
*   `🛠️` : Task (Technical)
*   `🐞` : Bug
*   `🧹` : Chore / Refactoring / Tech Debt
*   `💡` : Spike / Research / Investigation
*   `🗺️` : Epic / Feature Overview (`_overview.md`)

**Examples:**
*   `001_📖_user_login_story.md`
*   `002_🛠️_setup_auth_db_task.md`
*   `006_💡_research_caching_spike.md`

## 4. ⚙️ YAML Front Matter: Agile Task Metadata

Define the core attributes for managing Agile work items.

```yaml
---
# 🆔 Item Identification & Core Details
id:             # REQUIRED. Unique ID (e.g., STORY-001, TASK-002). Convention: {TYPE_PREFIX}-{NNN}
title:          # REQUIRED. Human-readable title.
status:         # REQUIRED. Current workflow state. (e.g., "🟡 Backlog", "🔵 In Progress"). See Statuses.
type:           # REQUIRED. Work item type. (e.g., "📖 User Story", "🛠️ Task"). See Types.

# 🏆 Prioritization & Value
priority:       # Recommended. Importance/Order. (e.g., "🔼 High"). See Priorities.
# value_score:    # Optional. Business value estimate (e.g., 1-10).
# risk_score:     # Optional. Risk estimate (e.g., 1-10).

# ⏳ Effort & Iteration/Sprint Tracking
estimated_effort: # Recommended. Story Points or T-Shirt Size. (e.g., "3", "M").
iteration:      # Optional. Sprint/Iteration identifier. (e.g., "Sprint 4", "2025-Q2-Iter3"). Used for filtering/grouping.
# created_date:   # Optional. YYYY-MM-DD
updated_date:   # Recommended. YYYY-MM-DD. Auto-update ideally.

# 🧑‍💻 Assignment & Collaboration
assigned_to:    # Optional. (e.g., "🧑‍💻 User:TeamA", "🤖 AI+Pair:Alice").
# reporter:       # Optional.

# 🔗 Relationships & Context
parent_feature: # Optional. Path to Feature/_overview.md.
parent_story:   # Optional. ID of User Story this Task/Bug belongs to.
depends_on:     # Optional. List of other item IDs this blocks on.
related_docs:   # Optional. Links to Personas, Designs, Specs.
tags:           # Optional. Keywords. (e.g., ["frontend", "mvp", "performance"]).

# ✅ Definition of Done Checklist (Team standard - optional here, often better in team docs)
# dod_checklist: ["Code Complete", "Tests Pass", "Reviewed", "AC Met"]
---

# << Item Title >>

## Description / User Story 📖 / Task Details 🛠️ / Bug Report 🐞
... Markdown Body content specific to the item type ...

## Acceptance Criteria ✅
... Specific, testable checklist for *this* item ...
```

**Key Agile YAML Fields:**
*   `status`, `type`, `priority`, `estimated_effort`: Core fields for Agile planning and tracking.
*   `iteration`: Key for time-boxed iterations (Sprints).
*   `parent_feature`, `parent_story`, `depends_on`: Define relationships.
*   `tags`: Essential for flexible filtering and reporting.

## 5. 🏷️ Standardized Field Values & Emojis

Consistency enables effective filtering, reporting, and automation.

*   **Statuses (`status:` - Example Kanban Flow):**
    *   `⚪ Icebox`: 🧊 Not planned / On Hold.
    *   `🟡 Backlog`: 📥 Ready for consideration.
    *   `🔵 Selected`: 🎯 Planned for current Iteration/Sprint.
    *   `🔵 In Progress`: 🏗️ Work started.
    *   `🟣 Review`: 👀 Ready for code review / QA check.
    *   `🧪 Testing`: 🔬 Undergoing specific testing phase (if applicable).
    *   `🟢 Done`: ✅ Meets Definition of Done.
*   **Types (`type:`):** `📖 User Story`, `🛠️ Task`, `🐞 Bug`, `🧹 Chore`, `💡 Spike`, `🗺️ Epic/Feature`.
*   **Priorities (`priority:`):** `🔥 Highest`, `🔼 High`, `▶️ Medium`, `🔽 Low` (Or numerical).
*   **Effort (`estimated_effort:`):** Story Points (`1`, `2`, `3`, `5`, `8`...) or T-Shirts (`XS`, `S`, `M`, `L`, `XL`). Be consistent!

## 6. 📝 Markdown Body: Content Conventions

Structure the body based on the work item type.

*   **User Story (`## User Story 📖`):** Use the standard template:
    ```markdown
    > As a **[Type of User]**,
    > I want **[To perform some action]**,
    > So that **[I can achieve some benefit]**.
    ```
    Add any extra context, notes, or links below.
*   **Task Description (`## Task Details 🛠️`):** Clearly explain the technical work. If it supports a story, link to it. Specify technical constraints or approaches.
*   **Bug Report (`## Bug Report 🐞`):** Include:
    *   **Summary:** What's wrong?
    *   **Steps to Reproduce 👣:** Numbered steps.
    *   **Expected Behavior ✅:** What should happen?
    *   **Actual Behavior ❌:** What does happen?
    *   **Environment 🖥️:** Browser/OS/Device/etc.
    *   **Screenshots/Logs 📎:** Links or embedded images.
*   **Acceptance Criteria (`## Acceptance Criteria ✅`):** **MANDATORY** for Stories, Bugs, Tasks.
    *   Use clear, specific, testable checklists (`- [ ]`).
    *   Focus on *verifiable outcomes*.
    *   Consider Given/When/Then format for clarity if helpful.
    *   `- [ ] When user enters valid credentials, login succeeds.`
    *   `- [ ] Error message X is displayed for invalid credentials.`
*   **Notes/Discussion (`## Notes / Discussion 💬`):** Place for questions, decisions, technical details.

## 7. 📄 Example Templates (Place in `tasks/_templates/`)

### `📖_user_story.md`

```markdown
---
id:             # << GENERATE_ID (STORY-NNN) >>
title:          # << As a User, I want Action, so that Benefit >>
status:         "🟡 Backlog"
type:           "📖 User Story"
priority:       "▶️ Medium"
estimated_effort: # << Points/Size >>
# iteration:
# assigned_to:
reporter:       # << Who? >>
parent_feature: # << Path to FEATURE/_overview.md >>
# depends_on:     []
related_docs:   []
tags:           []
---

# << As a User, I want Action, so that Benefit >>

## User Story 📖
> As a **[User Role]**,
> I want **[Action]**,
> So that **[Benefit]**.

## Notes / Discussion 💬
(Context, assumptions, links to designs...)

## Acceptance Criteria ✅
*   - [ ] Criterion 1 (Given/When/Then or simple statement)
*   - [ ] Criterion 2
*   - [ ] ...
```

### `🛠️_task.md`

```markdown
---
id:             # << GENERATE_ID (TASK-NNN) >>
title:          # << TASK: Concise technical goal >>
status:         "🟡 Backlog"
type:           "🛠️ Task"
priority:       "▶️ Medium"
estimated_effort: # << Hours/Size >>
# iteration:
# assigned_to:
parent_story:   # << Optional: ID of story this supports >>
parent_feature: # << Path to FEATURE/_overview.md >>
# depends_on:     []
tags:           ["technical", ...]
---

# << TASK: Concise technical goal >>

## Task Details 🛠️
(Explain the technical work. Link to parent story if applicable.)

## Acceptance Criteria ✅
*   - [ ] Technical outcome 1 is achieved (e.g., Database schema updated).
*   - [ ] Technical outcome 2 is achieved (e.g., Unit tests for module X pass).
*   - [ ] ...
```

### `🐞_bug.md`

```markdown
---
id:             # << GENERATE_ID (BUG-NNN) >>
title:          # << BUG: Short description of issue >>
status:         "🟡 Backlog"
type:           "🐞 Bug"
priority:       "🔼 High" # Usually higher
# estimated_effort: # Optional for bugs
# iteration:
# assigned_to:
reporter:       # << Who found it? >>
parent_feature: # << Path to affected FEATURE/_overview.md >>
# related_docs:   # Links to logs/screenshots
tags:           ["bug", ...] # Add feature tag
---

# << BUG: Short description of issue >>

## Bug Report 🐞

**Summary:**
(Brief explanation of the problem)

**Steps to Reproduce 👣:**
1.  ...
2.  ...
3.  ...

**Expected Behavior ✅:**
(What should have happened?)

**Actual Behavior ❌:**
(What actually happened?)

**Environment 🖥️:**
(Browser, OS, etc.)

## Acceptance Criteria ✅
*   - [ ] Following Steps to Reproduce, the Actual Behavior no longer occurs.
*   - [ ] Expected Behavior is observed.
*   - [ ] (Optional) A regression test covering this scenario is added.
```

## 8. 🔄 Implementing the Agile Flow with MDTM

1.  **Idea / Need:** Create a basic item in `BACKLOG/` or directly in a feature folder with `status: 🟡 Backlog`.
2.  **Backlog Refinement:** Team discusses Backlog items. Add details, User Story format, AC, estimate effort (`estimated_effort`), assign priority. Items become well-defined.
3.  **Iteration Planning:** Select prioritized items from the Backlog for the upcoming iteration. Update `status: 🔵 Selected` and set the `iteration:` field. Ensure capacity matches estimates.
4.  **Daily Cycle:**
    *   Developers pick items from `Selected`. Update `status: 🔵 In Progress`, set `assigned_to`.
    *   *Stand-up:* Discuss progress on `In Progress` items, surface blockers (`status: ⚪ Blocked`).
    *   Work is done (coding, testing, potentially using AI). Update notes, check off AC sub-items.
5.  **Review & Completion:**
    *   Work item believed complete according to AC. Update `status: 🟣 Review`.
    *   Peer review / QA / Product Owner review occurs against AC and Definition of Done.
    *   If accepted, update `status: 🟢 Done`.
    *   If rework needed, revert `status: 🔵 In Progress` with feedback.
6.  **Iteration Review/Demo:** Demonstrate `🟢 Done` items from the completed iteration.
7.  **Retrospective:** Discuss process, potentially creating `🧹 Chore` items for improvements.
8.  **Archiving:** Periodically move `🟢 Done` items to the `archive/` folder.

## 9. ✅ Conclusion: Flexible Tracking for Iterative Value

Implementing **Agile Principles with MDTM** offers a powerful, developer-friendly approach. By using **feature-based organization**, standard **Agile artifact formats** (Stories, Tasks, Bugs), clear **Acceptance Criteria**, and consistent **YAML metadata** for status, priority, effort, and iteration, teams can effectively manage iterative workflows directly within their repository. This fosters transparency, version control, adaptability, and provides excellent, structured input for AI coding partners. Remember to combine this system with strong team communication and Agile ceremonies.