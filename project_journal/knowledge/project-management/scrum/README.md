#  Scrum Framework with MDTM: A Practical Implementation Guide 🔄 sprintmd

**Version:** 1.0
**Date:** 2025-04-05

## 1. Overview: Running Scrum with Markdown Tasks 🚀

Welcome! This guide details how to implement the **Scrum framework** using the **Markdown-Driven Task Management (MDTM)** system. We'll leverage MDTM's file-based approach (Markdown files 📄, YAML metadata ⚙️, Git tracking <0xF0><0x9F><0x9A><0xB2>️) to manage Scrum artifacts like the Product Backlog and Sprint Backlog directly within your project repository.

**The Core Idea:** Represent Product Backlog Items (PBIs) – typically User Stories 📖, Bugs 🐞, Tasks 🛠️, etc. – as individual `.md` files. Organize these within a **feature-based Product Backlog structure** 📂. Use specific YAML fields (`sprint:`, `status:`, `story_points:`) to manage the Sprint Backlog and track progress within time-boxed Sprints 🗓️.

This approach provides a transparent, version-controlled, and developer-centric way to manage Scrum work, keeping artifacts close to the code and making them easily parsable by humans 🧑‍💻 and AI assistants 🤖.

**How MDTM Supports Scrum:**
*   **Product Backlog:** A collection of `.md` files, typically organized by feature/epic folders.
*   **Sprint Backlog:** A subset of Product Backlog `.md` files selected for a Sprint, identified by a `sprint:` field in their YAML and specific `status:` values.
*   **PBIs:** User Stories, Bugs, Tasks represented as `.md` files with specific `type:` values.
*   **Increment:** The potentially shippable product built during the Sprint, corresponding to code changes linked to completed PBIs.
*   **Scrum Events:** MDTM files serve as the input/output for Planning, the focus of Daily Scrums, and the basis for Reviews.

**❗ Note:** MDTM manages the *artifacts*. The Scrum framework's roles (Product Owner, Scrum Master, Developers), events (ceremonies), and core principles **are enacted by the team** using the information within these MDTM files.

## 2. Why Use MDTM for Scrum? 🤔

Adapting MDTM for Scrum offers several advantages:

*   **🧩 Integrated Environment:** Keep backlog management within the IDE/repository, reducing context switching.
*   **🔄 Supports Sprints:** YAML fields (`sprint:`, `status:`) allow clear identification and tracking of work within time-boxed iterations.
*   **💎 Value Focus:** Feature-based organization helps maintain focus on delivering product value. User Story formats reinforce this.
*   **📊 Transparency & History:** Git tracks every refinement, estimation change, status update, and sprint assignment for full traceability.
*   **🤖 AI-Friendly:** Well-defined PBIs with clear Acceptance Criteria in `.md` format are excellent inputs for AI coding assistants.
*   **🗣️ Facilitates Collaboration:** Task files become concrete items for discussion during Scrum events. Linking PBIs in commits/PRs improves code context.
*   **🔧 Flexible & Simple:** Easier to set up and adapt than some dedicated tools, leveraging familiar text formats.

## 3. Core Scrum Concepts in MDTM 🧱

Mapping Scrum terms to MDTM elements:

*   **Product Backlog Item (PBI):** An individual `.md` file (Story, Bug, Task, etc.).
*   **Product Backlog:** The collection of all relevant `.md` files representing future work, typically organized in `tasks/FEATURE_.../` folders and potentially a `tasks/BACKLOG/` folder. Prioritized primarily by the Product Owner.
*   **Sprint:** A time-box identified by a value in the `sprint:` YAML field (e.g., `sprint: "Sprint 5 (Apr 8-19)"`).
*   **Sprint Backlog:** The set of `.md` files committed to by the Developers for the current Sprint (identified by `sprint: "Current Sprint Name"` and `status` values like `🔵 Sprint Backlog`, `🏗️ In Progress`, etc.).
*   **Definition of Done (DoD):** A team standard, ideally documented (e.g., in `docs/DefinitionOfDone.md`), and potentially referenced or partially included in PBI templates or review checklists.
*   **Increment:** The sum of all PBIs completed (`🟢 Done`) during a Sprint and integrated into the codebase.

## 4. 🗂️ Recommended Directory Structure: Feature-Based Product Backlog

Organize the Product Backlog by feature/value stream. Use YAML fields to manage Sprint assignments.

```PROJECT_ROOT/
├── src/                     # Source Code -> The Increment evolves here
├── docs/                    # Supporting Docs (Personas, DoD, Architecture)
│   └── DefinitionOfDone.md  # 👈 Example DoD Document
├── tasks/                   # 👈 **Main MDTM Directory**
│   ├── _templates/          # 📄 PBI Templates (Story, Bug, Task, Spike)
│   │   ├── 📖_user_story.md
│   │   ├── 🐞_bug.md
│   │   ├── 🛠️_task.md
│   │   └── 💡_spike.md
│   │
│   ├── BACKLOG/             # 📥 Optional: Unrefined/Unprioritized PBIs
│   │   └── IDEA_reporting_dashboard.md
│   │
│   ├── FEATURE_authentication/  # 🔑 Product Backlog Area: Authentication Feature
│   │   ├── _overview.md       # 🗺️ Optional: Epic/Feature Definition
│   │   ├── 001_📖_user_login_story.md     # PBI
│   │   ├── 002_🛠️_setup_auth_db_task.md   # PBI (Technical Task)
│   │   └── 003_📖_password_reset_story.md # PBI
│   │
│   ├── FEATURE_user_profile/  # 👤 Product Backlog Area: User Profile Feature
│   │   ├── _overview.md
│   │   └── 004_📖_display_profile_story.md
│   │
│   └── AREA_tech_debt/        # 🧹 Product Backlog Area: Technical Debt
│       └── 005_🧹_refactor_legacy_service.md
│
├── archive/                 # 📦 Optional: Completed items (e.g., items 'Done' in previous Sprints)
│   └── ...
└── README.md
```

**Key Structural Points:**
*   ✅ **Feature Folders:** Primary organization for the Product Backlog. Represents vertical slices of product value.
*   ✅ **Backlog Folder:** Optional holding area for raw ideas before refinement.
*   ✅ **Templates:** Use templates for consistent PBI structure.
*   ✅ **Sprint Management:** Sprint assignment and workflow status are primarily managed via **YAML fields**, not folders. This keeps the feature structure stable.

## 5. 📄 PBI File Naming Conventions

Use type emojis for quick identification.

**Format:** `NNN_🌀_short_description.md`

*   **`NNN`:** Sequence number (project-wide or per-feature).
*   **`_🌀_`:** Emoji for PBI **Type** (see Type Emojis below).
*   **`short_description`:** Brief, lowercase, underscore-separated name.
*   **`.md`:** Markdown extension.

**Type Emojis (`🌀`):**
*   `📖` : User Story
*   `🐞` : Bug
*   `🛠️` : Task (Technical task needed for a Story or the platform)
*   `🧹` : Chore / Refactoring / Tech Debt
*   `💡` : Spike / Research
*   `🗺️` : Epic / Feature Overview (`_overview.md`)

**Examples:**
*   `001_📖_user_login_story.md`
*   `002_🛠️_setup_auth_db_task.md` (Task needed for story 001)
*   `005_🧹_refactor_legacy_service.md`

## 6. ⚙️ YAML Front Matter: Supporting Scrum Artifacts

Include fields essential for Scrum planning and tracking.

```yaml
---
# 🆔 PBI Identification & Core Details
id:             # REQUIRED. Unique ID (e.g., STORY-001, BUG-003). Convention: {TYPE_PREFIX}-{NNN}
title:          # REQUIRED. Human-readable title / Story summary.
status:         # REQUIRED. Workflow state. See Statuses below. Crucial for Sprint tracking. "🟡 Product Backlog"
type:           # REQUIRED. PBI type. "📖 User Story", "🐞 Bug", etc. See Types.

# 🏆 Product Backlog Attributes
priority:       # Recommended for PO ordering. "🔥 Highest", "🔼 High", etc. See Priorities.
value:          # Optional. Business value score/category.
estimate_story_points: # Recommended. Team's relative effort estimate. E.g., 1, 2, 3, 5, 8, 13...

# 🗓️ Sprint Backlog Attributes
sprint:         # REQUIRED for items in a Sprint. Sprint identifier. "Sprint 6 (Apr 22 - May 3)" or "Sprint 6".
# sprint_goal_contribution: # Optional. How this PBI contributes to the Sprint Goal.

# ⏳ Tracking & Assignment
# created_date:   # Optional. YYYY-MM-DD
updated_date:   # Recommended. YYYY-MM-DD. Auto-update ideally.
# assigned_to:    # Optional. Can be assigned during Sprint. "🧑‍💻 Dev:Bob", "🤖 AI"

# 🔗 Relationships & Context
parent_feature: # Optional. Path to Feature/_overview.md.
# depends_on:     # Optional. List of other PBI IDs this depends on.
related_docs:   # Optional. Links to Designs, Personas, DoD. ["docs/DefinitionOfDone.md"]
tags:           # Optional. Keywords for filtering. ["frontend", "security"]

# ✅ Acceptance Criteria (Defined in body, but could have summary checklist here)
# ac_summary: ["[ ] Login succeeds", "[ ] Error shown"]
---

# << PBI Title >>

## Description / User Story 📖 / Bug Report 🐞 / Task Details 🛠️
... Markdown Body content specific to the PBI type ...

## Acceptance Criteria ✅
... Specific, testable checklist for *this* PBI ...
```

**Key Scrum YAML Fields:**
*   `sprint:`: **Assigns a PBI to a specific Sprint Backlog.** This is the primary field for sprint management.
*   `status:`: Tracks the PBI's journey from Product Backlog through the Sprint workflow to Done.
*   `estimate_story_points:`: Captures the team's effort estimate, used in Sprint Planning.
*   `priority:`: Used by the Product Owner to order the Product Backlog.
*   `type:`: Differentiates PBIs.

## 7. 🏷️ Standardized Field Values & Emojis

Consistency is key for filtering and understanding.

*   **Statuses (`status:` - Example Scrum Flow):**
    *   `⚪ Candidate`: 🧊 Idea, not yet refined (maybe in `BACKLOG/`).
    *   `🟡 Product Backlog`: 📥 Refined, estimated, prioritized, ready for Sprint Planning.
    *   `🔵 Sprint Backlog`: 🎯 Selected for the *current* Sprint during Planning. (Ready to be worked on).
    *   `🏗️ In Progress`: 🔨 Work started by a Developer within the Sprint.
    *   `🟣 Review / Test`: 👀 Work complete, needs verification against AC & DoD.
    *   `🟢 Done`: ✅ Meets Definition of Done. Completed within the Sprint.
    *   `⚪ Blocked`: 🚧 Impediment encountered during the Sprint.
*   **Types (`type:`):** `📖 User Story`, `🐞 Bug`, `🛠️ Task`, `🧹 Chore`, `💡 Spike`, `🗺️ Epic/Feature`.
*   **Priorities (`priority:`):** `🔥 Highest`, `🔼 High`, `▶️ Medium`, `🔽 Low` (Mainly for PO Backlog ordering).

## 8. 📝 Markdown Body: PBI Content

Structure the body based on the PBI type.

*   **User Story (`## User Story 📖`):**
    ```markdown
    > As a **[Type of User]**,
    > I want **[Capability]**,
    > So that **[Benefit/Value]**.
    ```
    Add conversation notes, details.
*   **Bug Report (`## Bug Report 🐞`):** Include Steps to Reproduce, Expected vs. Actual, Environment.
*   **Task Description (`## Task Details 🛠️`):** Explain the technical work needed. Often broken down from a User Story during Sprint Planning or Refinement.
*   **Acceptance Criteria (`## Acceptance Criteria ✅`):** **ESSENTIAL for all PBIs.** Use specific, testable checklists (`- [ ]`). Defines what "Done" means for *this specific item*. Must be met to move to `🟢 Done`.

## 9. 📄 Example Templates (Place in `tasks/_templates/`)

### `📖_user_story.md`

```markdown
---
id:             # << GENERATE_ID (STORY-NNN) >>
title:          # << As a User, I want..., So that... >>
status:         "🟡 Product Backlog"
type:           "📖 User Story"
priority:       "▶️ Medium"
estimate_story_points: # << Points (e.g., 3, 5) >>
# sprint:         # << Assigned during Sprint Planning >>
# assigned_to:
reporter:       # << PO or User Proxy >>
parent_feature: # << Path to FEATURE/_overview.md >>
related_docs:   ["docs/DefinitionOfDone.md"]
tags:           []
---

# << As a User, I want..., So that... >>

## User Story 📖
> As a **...**,
> I want **...**,
> So that **...**.

## Notes / Conversation 💬
(Details, assumptions, decisions from refinement)

## Acceptance Criteria ✅
*   - [ ] Criterion 1 (Specific, Testable)
*   - [ ] Criterion 2
*   - [ ] ...
```

### `🛠️_task.md` (Often created during Sprint Planning as breakdown)

```markdown
---
id:             # << GENERATE_ID (TASK-NNN) >>
title:          # << TASK: Technical step for a Story/Bug >>
status:         "🔵 Sprint Backlog" # Usually created already in Sprint Backlog
type:           "🛠️ Task"
# priority:       # Priority often inherited from Story
# estimate_story_points: # Effort often tracked at Story level, Tasks might use hours/sub-items
sprint:         # << Current Sprint Name/ID >>
# assigned_to:    # Assigned during Sprint
parent_story:   # << ID of parent Story (e.g., STORY-NNN) >>
parent_feature: # << Path to FEATURE/_overview.md >>
tags:           ["technical", ...]
---

# << TASK: Technical step for a Story/Bug >>

## Task Details 🛠️
(Specific technical work required. E.g., "Create API endpoint for X", "Update database migration script Y")

## Acceptance Criteria ✅
*   - [ ] Technical outcome achieved (e.g., Endpoint returns expected data).
*   - [ ] Unit tests written and pass.
*   - [ ] Code reviewed (if applicable at task level).
```

*(Create similar templates for `🐞_bug.md`, `💡_spike.md` etc.)*

## 10. 🔄 Supporting Scrum Events with MDTM

*   **Product Backlog Refinement:**
    *   **Focus:** Discussing PBIs (usually `.md` files in feature folders with `status: 🟡 Product Backlog` or `⚪ Candidate`).
    *   **Activity:** Clarify requirements (update body), estimate effort (`estimate_story_points:`), add AC, assign `priority:`. Outcome is a refined Product Backlog ready for Sprint Planning.
*   **Sprint Planning:**
    *   **Input:** Prioritized Product Backlog (ordered list of refined `.md` files). Team capacity understood.
    *   **Activity:** Select PBIs for the Sprint. Update selected `.md` files: set `sprint: "Current Sprint ID"`, change `status: 🔵 Sprint Backlog`. Developers might break down Stories into technical `🛠️ Task` files (also marked with the current `sprint:` and `status: 🔵 Sprint Backlog`). Define Sprint Goal.
    *   **Output:** Sprint Backlog (the collection of `.md` files with `sprint: "Current Sprint ID"`) and the Sprint Goal.
*   **Daily Scrum:**
    *   **Focus:** Developers inspect progress towards the Sprint Goal.
    *   **Activity:** Review PBIs with `status: 🏗️ In Progress`. Update status of worked-on items (e.g., move to `🟣 Review / Test`). Identify blockers (`status: ⚪ Blocked`). Check assignments (`assigned_to:`).
*   **Sprint Review:**
    *   **Input:** PBIs marked `status: 🟢 Done` during the Sprint (verify they meet DoD). The Increment itself.
    *   **Activity:** Demonstrate the completed work (the Increment). Gather feedback from stakeholders, which may generate new PBIs for the Product Backlog.
*   **Sprint Retrospective:**
    *   **Focus:** Team reflects on the process during the Sprint.
    *   **Activity:** Discuss what went well, what didn't. Action items for improvement might be added as `🧹 Chore` PBIs to the Product Backlog for a future Sprint.

## 11. Best Practices for Scrum MDTM 👍

*   **✅ Define DoD Clearly:** Have a documented Definition of Done (`docs/DefinitionOfDone.md`) and ensure the team adheres to it before marking PBIs `🟢 Done`.
*   **🔢 Estimate Consistently:** Apply Story Point estimation uniformly during refinement.
*   **🗣️ Keep PBIs Small & Clear:** Refine PBIs to be small enough to complete within a Sprint, with unambiguous Acceptance Criteria.
*   **🔗 Link Tasks to Stories:** Use the `parent_story:` field on `🛠️ Task` files created during Sprint Planning.
*   **💾 Commit Changes:** Treat PBI file updates (status, estimates, AC, sprint assignment) as important changes to be committed frequently.
*   **📊 Visualize Sprint Progress:** Use IDE tools or scripts to generate Sprint Burndown charts or Kanban views based on PBI `status` and `estimate_story_points` for the current `sprint:`.
*   **🧹 Maintain Backlog Health:** Regularly refine and re-prioritize the Product Backlog. Archive old `🟢 Done` items.

## 12. 💡 IDE Integration: Supercharging Scrum MDTM

An IDE optimized for MDTM can greatly assist Scrum:

*   **📊 Sprint Board View:** Display PBIs with `sprint: "Current Sprint"` as cards in columns based on `status`. Allow drag-and-drop status updates.
*   **🔍 Backlog Filtering/Ordering:** Easily view the Product Backlog, sort by `priority`, filter by `tags` or `type`.
*   **📝 Quick PBI Creation:** Use templates (`_templates/`) to create new Stories, Tasks, Bugs quickly.
*   **🔢 Estimation Support:** UI elements to easily assign/update `estimate_story_points`.
*   **📉 Burndown Charts:** Automatically generate Sprint Burndown based on `status` changes and `estimate_story_points` for PBIs in the current `sprint:`.
*   **🔗 Smart Linking:** Autocomplete PBI IDs for `depends_on`, `parent_story`. Link commits/PRs back to PBIs.

## 13. Conclusion ✅

Implementing the **Scrum framework with MDTM** provides a powerful, developer-centric approach to managing Agile projects. By representing PBIs as structured Markdown files, organizing the Product Backlog by feature, and using YAML fields like `sprint`, `status`, and `estimate_story_points`, teams can effectively manage Sprints and track progress transparently within their repository. When combined with disciplined Scrum practices and supportive IDE tooling, this method offers a streamlined, version-controlled alternative for Scrum teams.