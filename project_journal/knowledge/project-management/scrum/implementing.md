# 🛠️ Implementing the Scrum Framework with MDTM: A Practical Guide

**Version:** 1.0
**Date:** 2025-04-05

## 1. Introduction: Setting Up Scrum in Markdown 🔄 sprintmd

This guide provides the detailed "how-to" for implementing the **Scrum framework** using the file-based **Markdown-Driven Task Management (MDTM)** system. We'll cover the specific folder structures, file naming conventions, YAML metadata, templates, and examples needed to manage your Product Backlog, Sprint Backlogs, and Product Backlog Items (PBIs) directly within your Git repository.

**The Goal:** Establish a clear, consistent, and practical MDTM setup that supports Scrum events and artifacts, making work visible and trackable for the entire team (including AI assistants 🤖).

**Core Implementation Principles:**
*   **PBI as `.md` File:** Each User Story 📖, Bug 🐞, Task 🛠️, etc., is a Markdown file.
*   **Feature-Based Backlog:** Organize the Product Backlog using feature folders 📂.
*   **YAML for Sprint Control:** Use `sprint:`, `status:`, and `estimate_story_points:` fields in YAML ⚙️ to manage Sprint scope and progress.
*   **Emoji Markers:** Use emojis consistently 🏷️ for visual identification of types, statuses, and priorities.
*   **Templates for Consistency:** Rely on predefined templates 📄 to standardize PBI creation.

## 2. 🗂️ Directory Structure: Feature-Focused Product Backlog

Organize your `tasks/` directory primarily by feature or product area. Sprint organization happens via YAML fields.

```PROJECT_ROOT/
├── src/                     # Source Code (Where the Increment lives)
├── docs/                    # Supporting Docs (DoD, Personas, Architecture)
│   └── DefinitionOfDone.md  # 👈 IMPORTANT: Team's DoD
├── tasks/                   # 👈 **Main MDTM Directory for Scrum Artifacts**
│   ├── _templates/          # 📄 PBI Templates (Essential for consistency)
│   │   ├── 📖_user_story.md
│   │   ├── 🐞_bug.md
│   │   ├── 🛠️_task.md        # (Often used for Sprint Backlog breakdown)
│   │   └── 💡_spike.md
│   │
│   ├── BACKLOG/             # 📥 Optional: Unrefined/Unprioritized PBIs
│   │   └── IDEA_future_widget.md
│   │
│   ├── FEATURE_authentication/  # 🔑 Product Backlog Area: Authentication
│   │   ├── _overview.md       # 🗺️ Optional: Epic Definition for this Feature
│   │   ├── 001_📖_user_login_story.md     # PBI: User Story
│   │   ├── 002_🐞_login_error_bug.md      # PBI: Bug
│   │   └── 003_📖_password_reset_story.md # PBI: User Story
│   │
│   ├── FEATURE_reporting/     # 📊 Product Backlog Area: Reporting
│   │   ├── _overview.md
│   │   └── 004_📖_view_sales_report_story.md
│   │
│   └── AREA_infrastructure/   # 🏗️ Product Backlog Area: Non-Feature Work
│       └── 005_🛠️_upgrade_database_task.md # PBI: Technical Task
│
├── archive/                 # 📦 Optional: PBIs completed in previous Sprints
│   └── Sprint_5/            # Optional: Sub-archive by Sprint
│       └── ...
└── README.md
```

**Implementation Rules:**
*   ✅ **Main `tasks/` Folder:** The root for all PBIs.
*   ✅ **Feature Folders (`FEATURE_`):** Primary organization. Group related PBIs contributing to a larger feature.
*   ✅ **Other Area Folders (`AREA_`):** For cross-cutting concerns like tech debt, infrastructure.
*   ✅ **Templates (`_templates/`):** Create standardized `.md` files for each PBI type. Essential for AI and human consistency.
*   ✅ **Backlog Folder (`BACKLOG/`):** Optional holding pen for raw ideas before refinement places them into a Feature folder.
*   ✅ **Archive (`archive/`):** Move completed (`🟢 Done`) PBIs here after a Sprint or periodically. Optional: structure by Sprint within the archive.

## 3. 📄 PBI File Naming Conventions

Use a consistent format with visual type indicators.

**Format:** `NNN_🌀_short_description.md`

*   **`NNN`:** Sequence number (e.g., `001`, `042`). Project-wide numbering is recommended for unique IDs used in `id:` field.
*   **`_🌀_`:** Emoji for the PBI **Type** (see Emojis below), surrounded by underscores.
*   **`short_description`:** Brief, lowercase, underscore-separated identifier.
*   **`.md`:** Markdown extension.

**PBI Type Emojis (`🌀`):**
*   `📖` : User Story
*   `🐞` : Bug
*   `🛠️` : Task (Technical breakdown, often created during Sprint Planning)
*   `🧹` : Chore / Refactoring / Tech Debt
*   `💡` : Spike / Research
*   `🗺️` : Epic / Feature Overview (`_overview.md` file, not usually a PBI itself)

**Examples:**
*   `001_📖_user_login_story.md`
*   `002_🐞_login_error_bug.md`
*   `015_🛠️_create_api_endpoint_task.md`

## 4. ⚙️ YAML Front Matter: The PBI Definition

Define the essential Scrum attributes for each PBI file.

```yaml
---
# 🆔 PBI Identification & Core Details
id:             # REQUIRED. Unique Project-wide ID (e.g., STORY-001, BUG-002). Convention: {TYPE_PREFIX}-{NNN}
title:          # REQUIRED. Concise PBI Title / Summary.
status:         # REQUIRED. Current Workflow State. See Statuses below. E.g., "🟡 Product Backlog"
type:           # REQUIRED. PBI Type. E.g., "📖 User Story". See Types below.

# 🏆 Product Backlog Attributes (Set by PO/Team during Refinement)
priority:       # Recommended for PO ordering. E.g., "🔼 High". See Priorities.
estimate_story_points: # REQUIRED for Sprint Planning. Relative effort. E.g., 3, 5, 8.
# value:          # Optional. Business value indicator.

# 🗓️ Sprint Backlog Attributes (Set during Sprint Planning)
sprint:         # REQUIRED for Sprint Backlog items. Sprint Identifier. E.g., "Sprint 7 (May 6-17)"
# sprint_goal_contribution: # Optional text describing how this PBI helps meet the Sprint Goal.

# ⏳ Tracking & Assignment (Updated during Sprint)
updated_date:   # Recommended. YYYY-MM-DD. Track last modification.
assigned_to:    # Optional. Set when a Developer starts work. E.g., "🧑‍💻 Dev:Maria", "🤖 AI"

# 🔗 Relationships & Context
parent_feature: # Optional. Path to the feature's _overview.md file.
parent_story:   # Optional. ID of the Story this Task/Bug relates to. E.g., "STORY-001"
# depends_on:     # Optional. List of other PBI IDs this depends on.
related_docs:   # Optional. Links. E.g., ["docs/DefinitionOfDone.md", "docs/Designs.md#login"]
tags:           # Optional. Keywords. E.g., ["frontend", "api", "security"]
---

# << PBI Title >>

## Description / User Story 📖 / Bug Report 🐞 / Task Details 🛠️
... Markdown Body specific to PBI Type ...

## Acceptance Criteria ✅
... Checklist defining DONE for *this specific PBI* ...
```

**Implementation Notes:**
*   **`id:` Convention:** Use `STORY-NNN`, `BUG-NNN`, `TASK-NNN` based on the `NNN` in the filename for easy cross-referencing.
*   **`sprint:` Field:** This is the KEY field for defining the Sprint Backlog. Items without this field or with a past sprint ID are considered part of the Product Backlog (or archive).
*   **`estimate_story_points:`:** Should be set during Product Backlog Refinement *before* Sprint Planning.

## 5. 🏷️ Standardized Field Values & Emojis

Define and use these consistently across all PBIs.

*   **Statuses (`status:`):**
    *   `⚪ Candidate`: 🧊 (Optional) Raw idea, needs refinement.
    *   `🟡 Product Backlog`: 📥 Refined, estimated, prioritized. Ready for Sprint Planning.
    *   `🔵 Sprint Backlog`: 🎯 Committed to the current Sprint. Ready for work.
    *   `🏗️ In Progress`: 🔨 Actively being worked on in the Sprint.
    *   `🟣 Review/Test`: 👀 Work done by dev, needs verification (Code Review, QA, PO Acceptance).
    *   `🟢 Done`: ✅ Meets Acceptance Criteria AND Definition of Done. Completed in the Sprint.
    *   `⚪ Blocked`: 🚧 Impediment exists (explain in comments/notes).
*   **Types (`type:`):** `📖 User Story`, `🐞 Bug`, `🛠️ Task`, `🧹 Chore`, `💡 Spike`, `🗺️ Epic/Feature` (for `_overview.md` files).
*   **Priorities (`priority:`):** `🔥 Highest`, `🔼 High`, `▶️ Medium`, `🔽 Low` (Primarily for Product Backlog ordering).

## 6. 📝 Markdown Body: Structuring PBI Content

Use clear headings and formats based on the PBI `type:`.

*   **User Story (`📖`):**
    *   `## User Story 📖` section with the `As a..., I want..., So that...` template.
    *   `## Notes / Conversation 💬` section for details, assumptions, links.
    *   `## Acceptance Criteria ✅` section with a specific checklist (`- [ ]`).
*   **Bug (`🐞`):**
    *   `## Bug Report 🐞` section.
    *   Subsections: `**Summary:**`, `**Steps to Reproduce 👣:**`, `**Expected Behavior ✅:**`, `**Actual Behavior ❌:**`, `**Environment 🖥️:**`, `**Screenshots/Logs 📎:**` (optional links).
    *   `## Acceptance Criteria ✅` section (e.g., `"- [ ] Bug no longer occurs following steps."`, `"- [ ] Regression test added."`).
*   **Task (`🛠️`):**
    *   `## Task Details 🛠️` section explaining the technical work, often linking to the parent Story (`parent_story:` YAML field).
    *   `## Acceptance Criteria ✅` section defining the technical completion (e.g., `"- [ ] API endpoint X returns Y."`, `"- [ ] Unit tests cover Z."`).
*   **Spike (`💡`):**
    *   `## Investigation Goal 🎯` section defining the question to answer or knowledge to gain.
    *   `## Approach / Tasks 🔬` section outlining steps for the investigation.
    *   `## Outcome / Findings 💡` section (filled upon completion) summarizing results, decisions, or recommendations. Often leads to new Stories/Tasks.
    *   `## Timebox ⏳` (Optional) Mention the agreed timebox for the spike.

## 7. 📄 Example Templates (for `tasks/_templates/`)

### `📖_user_story.md` (Template)

```markdown
---
id:             # STORY-NNN
title:          # As a [Role], I want [Action], so that [Value]
status:         "🟡 Product Backlog"
type:           "📖 User Story"
priority:       "▶️ Medium"
estimate_story_points: # Estimate Here (e.g., 5)
sprint:         # Leave blank until Sprint Planning
# assigned_to:
reporter:
parent_feature: # Path to _overview.md
related_docs:   ["docs/DefinitionOfDone.md"]
tags:           []
---

# << Story Title >>

## User Story 📖
> As a **[Role]**,
> I want **[Action]**,
> So that **[Value]**.

## Notes / Conversation 💬
(Add details discussed during refinement)

## Acceptance Criteria ✅
*   - [ ] Criterion 1
*   - [ ] Criterion 2
```

### `🛠️_task.md` (Template - often created during Sprint Planning)

```markdown
---
id:             # TASK-NNN
title:          # TASK: Technical action for Story/Bug
status:         "🔵 Sprint Backlog" # Usually starts here if created in Planning
type:           "🛠️ Task"
# priority:       # Inherited from Story/Bug
# estimate_story_points: # Effort typically at Story level
sprint:         # << Current Sprint ID >>
# assigned_to:
parent_story:   # << STORY-ID or BUG-ID this supports >>
parent_feature: # Path to _overview.md
tags:           ["technical", ...]
---

# << Task Title >>

## Task Details 🛠️
(Specific technical work needed)

## Acceptance Criteria ✅
*   - [ ] Technical outcome 1 (e.g., Code committed)
*   - [ ] Technical outcome 2 (e.g., Tests pass)
```

### `🐞_bug.md` (Template)

```markdown
---
id:             # BUG-NNN
title:          # BUG: Brief issue summary
status:         "🟡 Product Backlog"
type:           "🐞 Bug"
priority:       "🔼 High" # Often default high
# estimate_story_points: # Optional: Estimate if significant effort
# sprint:
# assigned_to:
reporter:       # Who found it?
parent_feature: # Path to affected Feature's _overview.md
# related_docs:   # Links to logs, screenshots
tags:           ["bug"]
---

# << Bug Title >>

## Bug Report 🐞
**Summary:**
**Steps to Reproduce 👣:**
1.
2.
**Expected Behavior ✅:**
**Actual Behavior ❌:**
**Environment 🖥️:**

## Acceptance Criteria ✅
*   - [ ] Bug no longer occurs following steps.
*   - [ ] Regression test added/passes.
```

## 8. 🔄 Using MDTM in Scrum Events (Example Flow)

1.  **Refinement:** Team discusses `STORY-123.md` (`status: 🟡 Product Backlog`). They clarify AC, add notes, and agree on `estimate_story_points: 5`. File is committed.
2.  **Sprint Planning:** Team selects `STORY-123.md` for "Sprint 8". They update the file: `sprint: "Sprint 8"`, `status: 🔵 Sprint Backlog`. They break it down, creating `TASK-456.md` and `TASK-457.md`, setting their `sprint: "Sprint 8"`, `status: 🔵 Sprint Backlog`, and `parent_story: STORY-123`. All changes committed.
3.  **Daily Scrum:** Developer Alice picks `TASK-456.md`. She updates it: `assigned_to: 🧑‍💻 Dev:Alice`, `status: 🏗️ In Progress`. Commits change. Reports progress next day.
4.  **Work & Completion:** Alice finishes `TASK-456.md`, updates `status: 🟣 Review/Test`. Bob reviews, it meets AC. Alice updates `status: 🟢 Done`. Similar process for `TASK-457.md`. Once both tasks are Done, `STORY-123.md` can potentially be moved to `🟣 Review/Test` for PO acceptance against its AC and the DoD. If accepted, `status: 🟢 Done`. All changes committed.
5.  **Sprint Review:** Team presents all PBIs marked `🟢 Done` and `sprint: "Sprint 8"`.
6.  **After Sprint:** Completed items (`🟢 Done`) can be moved to the `archive/` folder.

## 9. ✅ Conclusion: Implementing Scrum Successfully with MDTM

This guide provides the blueprint for implementing the Scrum framework using MDTM. By adhering to the defined **folder structure**, **file naming conventions**, **YAML metadata standards** (especially `sprint`, `status`, `estimate_story_points`), **standardized field values/emojis**, and **PBI templates**, your team can create a transparent, version-controlled, and effective system for managing Scrum artifacts directly within your repository. Combine this structured approach with active participation in Scrum events and strong team communication for optimal results.