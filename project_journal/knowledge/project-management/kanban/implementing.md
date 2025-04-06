# 🛠️ Implementing Kanban with MDTM: A Practical Guide to Flow

**Version:** 1.0
**Date:** 2025-04-05

## 1. Introduction: Setting Up Your Kanban Flow in Markdown 🌊

This guide provides the detailed "how-to" for implementing the **Kanban method** using the file-based **Markdown-Driven Task Management (MDTM)** system. We'll cover the specific folder structures, file naming conventions, YAML metadata, templates, and examples needed to manage your workflow, visualize progress, and focus on continuous flow directly within your Git repository.

**The Goal:** Establish a clear, consistent, and practical MDTM setup that supports core Kanban practices (visualizing work, limiting WIP, managing flow), making work visible and trackable for the entire team (including AI assistants 🤖).

**Core Implementation Principles:**
*   **Work Item as `.md` File:** Each Task 🛠️, Feature ✨, Bug 🐞, etc., is a Markdown file.
*   **Workflow via `status:`:** The YAML `status:` field defines the columns of your Kanban board and tracks item movement ➡️.
*   **Logical Organization:** Use folders for features/areas 📂, but workflow state is managed by `status`.
*   **Emoji Markers:** Use emojis consistently 🏷️ for visual identification of types, statuses, and priorities.
*   **Templates for Consistency:** Rely on predefined templates 📄 to standardize work item creation.
*   **Focus on Flow Policies:** Explicitly define your workflow stages and WIP limits (ideally in a linked document).

## 2. 🗂️ Directory Structure: Organizing Work Items

Organize files logically by product area or feature. The Kanban workflow itself is defined by the `status:` field within the files, not the folder location.

```
PROJECT_ROOT/
├── src/                     # Source Code
├── docs/                    # Supporting Docs (Workflow Policies, DoD, Designs)
│   └── WorkflowPolicies.md  # 👈 **Define your Kanban board columns (statuses) & WIP limits here!**
├── tasks/                   # 👈 **Main MDTM Directory for Kanban Items**
│   ├── _templates/          # 📄 Templates (Essential for consistency)
│   │   ├── ✨_feature_item.md
│   │   ├── 🛠️_task_item.md
│   │   ├── 🐞_bug_item.md
│   │   └── 💡_spike_item.md
│   │
│   ├── INPUT_QUEUE/         # 📥 Optional: Raw, unprioritized input
│   │   └── IDEA_new_reporting_module.md
│   │
│   ├── AREA_authentication/   # 🔑 Product Area: Authentication
│   │   ├── _overview.md       # Optional: Goals/context for this area
│   │   ├── 001_✨_mfa_support_feature.md    # Work Item
│   │   ├── 002_🛠️_optimize_login_query.md # Work Item
│   │   └── 003_🐞_invalid_token_error.md   # Work Item
│   │
│   ├── AREA_payments/         # 💳 Product Area: Payments
│   │   └── 004_✨_add_new_gateway.md
│   │
│   └── AREA_ui_ux/            # 🎨 Product Area: UI/UX Improvements
│       └── 005_🛠️_improve_dashboard_layout.md
│
├── archive/                 # 📦 Optional: Completed items (status = ✅ Done)
│   └── ...
└── README.md
```

**Implementation Rules:**
*   ✅ **Main `tasks/` Folder:** The root for all work items.
*   ✅ **Area/Feature Folders (`AREA_`, `FEATURE_`):** Logical grouping for context. Helps find related items but *does not* represent workflow state.
*   ✅ **Templates (`_templates/`):** Create standardized `.md` files for each work item type (Feature, Task, Bug, Spike). Prefix with emoji and underscore.
*   ✅ **Input Queue (`INPUT_QUEUE/`):** Optional folder for ideas not yet ready for the main workflow's initial state (e.g., `📥 Backlog`).
*   ✅ **Archive (`archive/`):** Move items here once they reach the final `✅ Done` status.

## 3. 📄 Work Item File Naming Conventions

Use type emojis for instant recognition.

**Format:** `NNN_🌀_short_description.md`

*   **`NNN`:** Sequence number (project-wide recommended for unique IDs).
*   **`_🌀_`:** Emoji for the item **Type** (see Type Emojis below).
*   **`short_description`:** Brief, lowercase, underscore-separated name.
*   **`.md`:** Markdown extension.

**Item Type Emojis (`🌀`):**
*   `✨` : Feature / Epic / User Story (Represents distinct user value)
*   `🛠️` : Task (Technical work, enabler, improvement)
*   `🐞` : Bug / Defect
*   `🧹` : Chore / Maintenance / Refactoring
*   `💡` : Spike / Research / Investigation
*   `🗺️` : Overview / Definition (`_overview.md` file in an Area folder)

**Examples:**
*   `001_✨_mfa_support_feature.md`
*   `002_🛠️_optimize_login_query.md`
*   `003_🐞_invalid_token_error.md`

## 4. ⚙️ YAML Front Matter: Defining Kanban Items

Include fields that support visualization, flow management, and metrics.

```yaml
---
# 🆔 Item Identification & Core Details
id:             # REQUIRED. Unique Project-wide ID (e.g., ITEM-001). Convention: {TYPE_PREFIX}-{NNN}
title:          # REQUIRED. Concise item description.
status:         # REQUIRED. Current Kanban column/workflow state. **MUST MATCH a state defined in WorkflowPolicies.md**. E.g., "💻 Ready for Dev"
type:           # REQUIRED. Work item type. E.g., "✨ Feature". See Types.

# 🌊 Flow Management Attributes
priority:       # Recommended for ordering Input Queues. E.g., "🔼 High". See Priorities.
blocked:        # Optional. Use status "🚧 Blocked" OR a boolean `blocked: true`.
blocked_reason: # Required if Blocked. Text explaining the impediment.
# wip_limit_exempt: # Optional boolean for expedited items (use with caution & clear policy).

# ⏱️ Metrics Tracking Attributes (Timestamps are key!)
created_date:   # Recommended. Date item entered the system. YYYY-MM-DD.
updated_date:   # REQUIRED for metrics. Timestamp of *last status change*. YYYY-MM-DD HH:MM:SS. **Update this whenever `status` changes!**
# lead_time_start_date: # Optional: Date committed to (e.g., moved from raw Input).
# cycle_time_start_date: # Optional: Date work *actively* started (e.g., moved to Dev In Progress).
# completion_date:      # Optional: Date moved to final Done status. (Can be inferred from last update if status is Done).

# 🧑‍💻 Assignment & Context
assigned_to:    # Optional. Who is currently pulling/working on it.
parent_area:    # Optional. Path to the AREA/_overview.md file.
related_docs:   # Optional. Links. **Crucially, link to your WorkflowPolicies.md**. ["docs/WorkflowPolicies.md"]
tags:           # Optional. Keywords for filtering.
---

# << Item Title >>

## Description ✨ / Task Details 🛠️ / Bug Report 🐞
... Markdown Body specific to item type ...

## Acceptance Criteria ✅ / Definition of Ready (DoR) / Definition of Done (DoD)
... Checklist defining completion/transition criteria ...
```

**Implementation Notes:**
*   **`status:` is KING:** This field directly maps to your Kanban board columns. Its values **must** be standardized and match your documented workflow (`docs/WorkflowPolicies.md`).
*   **`updated_date:` is CRITICAL for Metrics:** To calculate time-in-status, cycle time, etc., this field **must** be updated accurately every time the `status` changes. Use a precise timestamp (including time). IDEs or Git hooks might help automate this.
*   **`blocked:`:** Using a dedicated `status: 🚧 Blocked` is often clearer visually on boards than a boolean flag. Ensure the `blocked_reason:` is filled out.

## 5. 🏷️ Standardized Field Values & Emojis

Define your specific workflow. Emojis make statuses instantly recognizable.

*   **Statuses (`status:` - *Example Workflow - DEFINE YOUR OWN!*)**
    *   `📥 Backlog`: Prioritized items ready to be pulled into active work. (Input Queue)
    *   `🔬 Analysis`: Requirements clarification, design. (WIP Stage)
    *   `💻 Ready for Dev`: Analysis done, ready for implementation. (Buffer/Queue)
    *   `🛠️ Development`: Coding & Unit Testing. (WIP Stage)
    *   `🟣 Review`: Code Review / Pair Programming check. (WIP Stage or Queue)
    *   `🧪 Testing`: QA / Integration Testing / UAT. (WIP Stage)
    *   `🚀 Ready for Deploy`: Tested & approved, awaiting release window. (Buffer/Queue)
    *   `✅ Done`: Deployed / Released / Completed. (Final State)
    *   `🚧 Blocked`: Work stopped due to impediment (explain in `blocked_reason`).
*   **Types (`type:`):** `✨ Feature`, `🐞 Bug`, `🛠️ Task`, `🧹 Chore`, `💡 Spike`, `🗺️ Overview`.
*   **Priorities (`priority:` - Mainly for `📥 Backlog` or Ready Queues):** `🔥 Expedite`, `🔼 High`, `▶️ Medium`, `🔽 Low`.

**➡️ Action:** Document YOUR team's specific workflow statuses, their order, entry/exit criteria, and WIP limits in `docs/WorkflowPolicies.md`. Link to it from templates (`related_docs:`).

## 6. 📝 Markdown Body: Detailing Work Items

Structure the body clearly.

*   **Description:** Explain the work item clearly (Feature goal, Task objective, Bug details).
*   **Acceptance Criteria (`## Acceptance Criteria ✅`):** Define what must be true for *this item* to be considered "Done" or ready to move to the next major stage (e.g., ready for Testing). Use checklists (`- [ ]`).
*   **Definition of Ready (DoR) (`## Definition of Ready ✋` - Optional):** Checklist for criteria needed before *starting* work (e.g., moving from Backlog to Analysis/Dev). `- [ ] Dependencies clear?`, `- [ ] AC defined?`.
*   **Definition of Done (DoD) (`## Definition of Done ✨` - Optional):** Checklist confirming item meets *overall* done criteria (often references team DoD). `- [ ] Meets team DoD (link)?`, `- [ ] Deployed?`.
*   **Notes / Blockers (`## Notes / Impediments 🚧`):** Log important updates, decisions, or detailed blocker information. Timestamping notes can be helpful.

## 7. 📄 Example Templates (for `tasks/_templates/`)

### ✨_feature_item.md (Template)

```markdown
---
id:             # ITEM-NNN
title:          # ✨ Feature: Concise value description
status:         "📥 Backlog" # Initial status
type:           "✨ Feature"
priority:       "▶️ Medium"
# blocked:
# blocked_reason:
created_date:   # YYYY-MM-DD
updated_date:   # YYYY-MM-DD HH:MM:SS
# assigned_to:
parent_area:    # Path to AREA/_overview.md
related_docs:   ["docs/WorkflowPolicies.md"] # Link to your policies!
tags:           []
---

# << Feature Title >>

## Description ✨
(Explain the feature, user value, links to designs/epics)

## Acceptance Criteria ✅
*   - [ ] Criterion 1 for this feature to be Done.
*   - [ ] Criterion 2...

## Notes / Impediments 🚧
(Updates, decisions, blocker details)
```

### 🛠️_task_item.md (Template)

```markdown
---
id:             # ITEM-NNN
title:          # 🛠️ Task: Technical objective
status:         "📥 Backlog" # Initial status
type:           "🛠️ Task"
priority:       "▶️ Medium"
# blocked:
# blocked_reason:
created_date:   # YYYY-MM-DD
updated_date:   # YYYY-MM-DD HH:MM:SS
# assigned_to:
parent_area:    # Path to AREA/_overview.md
related_docs:   ["docs/WorkflowPolicies.md"]
tags:           ["technical", ...]
---

# << Task Title >>

## Task Details 🛠️
(Explain technical work, links to parent feature if applicable)

## Acceptance Criteria ✅
*   - [ ] Technical outcome 1 is met.
*   - [ ] Technical outcome 2 is met.

## Notes / Impediments 🚧
(Updates, decisions, blocker details)
```

*(Create similar templates for `🐞_bug_item.md`, `💡_spike_item.md`, etc., tailoring body sections)*

## 8. 🔄 Implementing the Kanban Flow with MDTM

1.  **Define & Document:** Agree on workflow (`status` values), WIP limits per status, and pull policies. Document in `docs/WorkflowPolicies.md`.
2.  **Visualize:** Use an IDE/tool to render the Kanban board based on `status` fields. Ensure it shows WIP counts vs limits.
3.  **Prioritize Input:** Order items in the first input queue (`📥 Backlog` or similar) using `priority`.
4.  **Pull System:** Team members pull items **only when**:
    *   They have capacity.
    *   The WIP limit for the target `status` (e.g., `🛠️ Development`) is not exceeded.
    *   They pull the highest priority available item from the preceding "Ready" queue (e.g., `💻 Ready for Dev`).
    *   **Action:** Update the item's `status`, `assigned_to`, and **crucially `updated_date`**. Commit.
5.  **Work & Update Status:** As work progresses and exit criteria for a stage are met, update `status` and `updated_date`. Commit promptly. Add notes as needed.
6.  **Handle Blockers:** If blocked, set `status: 🚧 Blocked`, fill `blocked_reason`, and focus on resolution. Commit. When unblocked, revert `status` to the previous WIP state and update `updated_date`. Commit.
7.  **Manage Flow:** Regularly observe the board for bottlenecks (where WIP limit is often hit or items queue up). Use team meetings (like daily stand-ups or specific flow reviews) to discuss and resolve flow issues.
8.  **Measure & Improve:** Use tools or scripts to analyze `updated_date` history to calculate Cycle Time, Lead Time, Throughput. Use this data in retrospectives or kaizen events to identify and implement process improvements. Update `WorkflowPolicies.md` as needed.

## 9. ✅ Conclusion: Flowing Value with MDTM Kanban

Implementing **Kanban with MDTM** provides a robust, flexible system for managing workflow directly within your repository. By defining clear **workflow statuses**, respecting **WIP limits**, focusing on **smooth flow**, and leveraging **YAML metadata** for visualization and metrics, teams can optimize their delivery process. This transparent, version-controlled approach, especially when enhanced by capable IDE tooling, empowers teams to continuously improve and deliver value efficiently. Remember that Kanban's success relies heavily on team discipline and a commitment to managing flow.