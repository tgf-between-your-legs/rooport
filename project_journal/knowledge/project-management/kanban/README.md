# 🌊 Implementing Kanban with MDTM: A Guide to Flow

**Version:** 1.0
**Date:** 2025-04-05

## 1. Overview: Visualizing Flow with Markdown Tasks ➡️

Welcome! This guide details how to implement the **Kanban method** using the file-based **Markdown-Driven Task Management (MDTM)** system (Markdown files 📄, YAML metadata ⚙️, Git tracking <0xF0><0x9F><0x9A><0xB2>️). Kanban focuses on **visualizing workflow**, **limiting Work In Progress (WIP)**, **managing flow**, and **continuous improvement**. We'll adapt MDTM to support these core Kanban practices.

**The Core Idea:** Represent work items (Tasks 🛠️, Features ✨, Bugs 🐞, etc.) as individual `.md` files. Use YAML `status:` fields to define the **columns of your Kanban board** and track item movement through the workflow. Organize files logically (e.g., by feature/product area 📂) while the *flow* is managed primarily via status changes. The key is optimizing the smooth flow of value delivery.

This approach provides a flexible, transparent, and repository-integrated way to manage work, particularly suited for teams prioritizing continuous flow and adaptability, and where AI assistants 🤖 can benefit from clearly defined work states.

**How MDTM Supports Kanban:**
*   **Visualize Workflow:** The `status:` field in each `.md` file represents its column on a Kanban board. IDEs or tools can parse these files to render a visual board.
*   **Limit WIP:** While MDTM files don't *enforce* WIP limits, the structured data allows IDEs/tools to visualize WIP per status column, enabling the team to manually respect limits. YAML fields could note WIP state.
*   **Manage Flow:** Tracking status changes helps identify bottlenecks (where items pile up) and measure flow metrics (like Lead/Cycle Time, using `updated_date` tracking).
*   **Make Policies Explicit:** Workflow policies (e.g., criteria for moving between statuses, WIP limits) can be documented (e.g., in `docs/WorkflowPolicies.md`) and referenced.
*   **Feedback Loops:** Status changes and completed items provide natural points for feedback.
*   **Improve Collaboratively:** The transparent state of work in version-controlled files facilitates discussions about bottlenecks and process improvements.

**❗ Note:** Kanban is a *method* for managing and improving workflows. MDTM provides the *system* for representing the work items within that flow. The team's discipline in adhering to WIP limits and improving the process is crucial.

## 2. Why Use MDTM for Kanban? 🤔

MDTM offers advantages for Kanban implementations:

*   **🧩 Integrated Environment:** Keep work visualization and details within the development repository.
*   **🌊 Supports Flow:** Easily track items moving through custom workflow states defined by the `status:` field.
*   **🔧 Flexibility:** Simple to add/change workflow columns (just define new `status:` values and update team policies). Easy to re-prioritize input queues.
*   **📊 Data for Improvement:** YAML metadata (status changes, dates) provides raw data for calculating flow metrics (Cycle Time, Lead Time, Throughput), although calculations often require IDE support or scripts.
*   ** Git Transparency:** Full history of when items changed status, potentially revealing bottlenecks or flow issues over time.
*   **🤖 AI-Friendly:** Clear task definitions and statuses help AI assistants understand the current state and requirements of work items.
*   **🏷️ Simple & Accessible:** Uses familiar text files and Git, lowering the barrier to entry compared to complex dedicated tools.

## 3. Core Kanban Concepts in MDTM 🧱

Mapping Kanban practices to MDTM elements:

*   **Work Item:** An individual `.md` file (Task, Feature, Bug, etc.).
*   **Kanban Board Column:** A specific value defined for the `status:` field in the YAML front matter.
*   **Workflow:** The sequence of `status:` values an item typically moves through (e.g., `📥 Backlog` -> `🔍 Analysis` -> `🛠️ Development` -> `🧪 Testing` -> `✅ Done`).
*   **Work In Progress (WIP):** The count of `.md` files having a `status:` corresponding to an "in progress" column (e.g., Analysis, Development, Testing).
*   **WIP Limit:** A maximum number agreed upon by the team for items allowed in a specific `status:` (or group of statuses) simultaneously. *Managed by team discipline, visualized by tools.*
*   **Input Queue / Backlog:** Items with a `status:` like `📥 Backlog` or `📥 Ready for Dev`. Prioritization determines pull order.
*   **Pull System:** Developers "pull" items from an upstream status (e.g., `📥 Ready for Dev`) into their working status (e.g., `🛠️ Development`) *only when they have capacity and the WIP limit for the target status allows*.
*   **Flow Metrics:** Cycle Time (time from start work to finish work), Lead Time (time from request to delivery), Throughput (items finished per time unit). Calculable from status change timestamps (`updated_date`).

## 4. 🗂️ Recommended Directory Structure: Feature/Product Area

Organize files logically by feature or product area. The workflow is primarily defined by the `status` field, not folder location.

```
PROJECT_ROOT/
├── src/                     # Source Code
├── docs/                    # Supporting Docs (Workflow Policies, DoD, Designs)
│   └── WorkflowPolicies.md  # 👈 IMPORTANT: Define statuses, WIP limits, policies here
├── tasks/                   # 👈 **Main MDTM Directory**
│   ├── _templates/          # 📄 Templates for consistent item creation
│   │   ├── ✨_feature_item.md
│   │   ├── 🛠️_task_item.md
│   │   └── 🐞_bug_item.md
│   │
│   ├── INPUT_QUEUE/         # 📥 Optional: Unprioritized or raw input
│   │   └── IDEA_new_integration.md
│   │
│   ├── AREA_authentication/   # 🔑 Product Area: Authentication
│   │   ├── _overview.md       # Optional: High-level goals for this area
│   │   ├── 001_✨_user_login_feature.md    # Feature Item
│   │   ├── 002_🛠️_update_password_hash.md # Task Item
│   │   └── 003_🐞_session_timeout_bug.md   # Bug Item
│   │
│   ├── AREA_reporting/        # 📊 Product Area: Reporting
│   │   └── 004_✨_generate_sales_pdf.md
│   │
│   └── AREA_deployment/       # 🚀 Product Area: Deployment Pipeline
│       └── 005_🛠️_add_staging_step.md
│
├── archive/                 # 📦 Optional: Completed items (status = ✅ Done)
│   └── ...
└── README.md```

**Key Structural Points:**
*   ✅ **Area Folders:** Use `AREA_` or `FEATURE_` prefixes to group related work items logically. This helps context but doesn't define workflow state.
*   ✅ **Input Queue:** An optional folder for items not yet ready or prioritized for a specific area's input queue (e.g., `📥 Ready for Analysis`).
*   ✅ **Templates:** Crucial for ensuring items have necessary fields (like `status`).
*   ✅ **Workflow via `status`:** The primary mechanism for tracking progress through the Kanban system.
*   ✅ **Archive:** For items that reach the final "Done" status.

*Alternative (Less Recommended for Scalability): MTDN - Folder Kanban uses folders like `todo/`, `in_progress/`, `done/` to represent status. This is simpler visually in the file system but breaks down feature context and scales poorly.*

## 5. 📄 Work Item File Naming Conventions

Use type emojis for quick visual classification.

**Format:** `NNN_🌀_short_description.md`

*   **`NNN`:** Sequence number (project-wide recommended for unique IDs).
*   **`_🌀_`:** Emoji for the item **Type** (see Type Emojis below).
*   **`short_description`:** Brief, lowercase, underscore-separated identifier.
*   **`.md`:** Markdown extension.

**Item Type Emojis (`🌀`):**
*   `✨` : Feature / Epic / User Story (Value delivery focus)
*   `🛠️` : Task (Technical work, enabler)
*   `🐞` : Bug / Defect
*   `🧹` : Chore / Refactoring / Maintenance
*   `💡` : Spike / Research / Investigation
*   `🗺️` : Overview / Definition (`_overview.md` file)

**Examples:**
*   `001_✨_user_login_feature.md`
*   `002_🛠️_update_password_hash.md`
*   `003_🐞_session_timeout_bug.md`

## 6. ⚙️ YAML Front Matter: Supporting Kanban Flow

Include fields essential for visualizing the board, managing flow, and gathering metrics.

```yaml
---
# 🆔 Item Identification & Core Details
id:             # REQUIRED. Unique Project-wide ID (e.g., ITEM-001, BUG-003). Convention: {TYPE_PREFIX}-{NNN}
title:          # REQUIRED. Concise item description.
status:         # REQUIRED. Current Kanban column/workflow state. E.g., "📥 Ready for Dev". See Statuses below.
type:           # REQUIRED. Work item type. E.g., "✨ Feature", "🐞 Bug". See Types below.

# 🌊 Flow Management Attributes
priority:       # Recommended for ordering Input Queues (Backlogs). E.g., "🔼 High". See Priorities.
blocked:        # Optional. Is the item blocked? (Boolean: true/false or Status: "🚧 Blocked")
blocked_reason: # Optional. Text explaining blocker if status is Blocked. "Waiting for API spec"
# wip_limit_exempt: # Optional (Boolean). E.g., For expedited items bypassing some WIP limits. Needs clear policy.

# ⏱️ Metrics Tracking Attributes (Optional - requires tooling/scripts to calculate)
# lead_time_start_date: # Date item was requested/added to first input queue. YYYY-MM-DD
# cycle_time_start_date: # Date item moved into the first "active work" status (e.g., Development). YYYY-MM-DD
# completion_date:      # Date item moved to the final "Done" status. YYYY-MM-DD
created_date:   # Recommended. YYYY-MM-DD
updated_date:   # Recommended. YYYY-MM-DD HH:MM:SS. CRITICAL for tracking time-in-status if calculating metrics.

# 🧑‍💻 Assignment & Context
assigned_to:    # Optional. Who is currently working on it. "🧑‍💻 Dev:Chen", "🤖 AI"
parent_area:    # Optional. Path to the AREA/_overview.md file.
related_docs:   # Optional. Links to Designs, Policies, Specs. ["docs/WorkflowPolicies.md"]
tags:           # Optional. Keywords for filtering. ["api", "performance", "ux"]
---

# << Item Title >>

## Description ✨ / Task Details 🛠️ / Bug Report 🐞
... Markdown Body specific to item type ...

## Acceptance Criteria ✅ / Definition of Ready (DoR) / Definition of Done (DoD)
... Checklist defining completion/transition criteria for *this item* ...
```

**Key Kanban YAML Fields:**
*   `status:`: **Defines the Kanban board column.** This is the most critical field for visualization and flow.
*   `priority:`: Used to order items within input queue statuses (e.g., `📥 Backlog`).
*   `blocked:` / `blocked_reason:`: To flag and understand impediments.
*   `updated_date:`: Essential timestamp for calculating time-in-status, cycle time, etc. (needs high resolution).
*   `type:`: Allows filtering or applying different policies based on work item type.

## 7. 🏷️ Standardized Field Values & Emojis

Define your workflow states clearly. Emojis aid quick recognition.

*   **Statuses (`status:` - Example Workflow Columns):**
    *   `📥 Input Queue`: Raw ideas, unsorted.
    *   `🔍 Ready for Analysis`: Prioritized, ready for requirements/design work. (Input Queue for Analysis)
    *   `🔬 Analysis in Progress`: Actively being analyzed/designed. (WIP)
    *   `✅ Analysis Done`: Analysis complete, ready for development. (Buffer/Queue)
    *   `💻 Ready for Dev`: Prioritized, ready for coding. (Input Queue for Dev)
    *   `🛠️ Development in Progress`: Actively being coded. (WIP)
    *   `🟣 Code Review`: Code complete, awaiting review. (WIP or Queue depending on policy)
    *   `🧪 Ready for Testing`: Development & review done, ready for QA. (Input Queue for Test)
    *   `🔬 Testing in Progress`: Actively being tested. (WIP)
    *   `🚀 Ready for Deployment`: Tested, approved, ready for release. (Input Queue for Deploy)
    *   `🚢 Deploying`: Actively being deployed. (WIP)
    *   `✅ Done`: Released and verified. Workflow complete.
    *   `🚧 Blocked`: (Special Status) Work stopped - see `blocked_reason`. Can apply to any WIP stage.
*   **Types (`type:`):** `✨ Feature`, `🐞 Bug`, `🛠️ Task`, `🧹 Chore`, `💡 Spike`, `🗺️ Overview`.
*   **Priorities (`priority:` - for input queues):** `🔥 Expedite`, `🔼 High`, `▶️ Medium`, `🔽 Low`.

**Important:** Your team **must define its specific workflow columns (statuses)** and document them, perhaps in `docs/WorkflowPolicies.md`.

## 8. 📝 Markdown Body: Work Item Details

Use the body for details relevant to the item and its current state.

*   **Description:** Explain the Feature, Task, Bug, etc. clearly.
*   **Acceptance Criteria (`## Acceptance Criteria ✅`):** Define what "Done" means *for this specific item*. Essential for knowing when it can move forward.
*   **Definition of Ready (DoR) Checklist (Optional - `## DoR Checklist ✋`):** Criteria needed before an item can *enter* a specific status (e.g., "AC defined?", "Dependencies met?").
*   **Definition of Done (DoD) Checklist (Optional - `## DoD Checklist ✨`):** Criteria needed to *exit* a status or the final "Done" state (often links to team DoD).
*   **Notes / Blockers (`## Notes / Impediments 🚧`):** Log progress updates, decisions, or details about blockers if `status: 🚧 Blocked`.

## 9. 📄 Example Templates (for `tasks/_templates/`)

### `✨_feature_item.md` (Template)

```markdown
---
id:             # ITEM-NNN
title:          # ✨ Feature: Concise description of value
status:         "📥 Input Queue" # Or initial analysis state
type:           "✨ Feature"
priority:       "▶️ Medium"
# blocked:        false
# blocked_reason:
created_date:   # YYYY-MM-DD
updated_date:   # YYYY-MM-DD HH:MM:SS
# assigned_to:
parent_area:    # Path to AREA/_overview.md
related_docs:   ["docs/WorkflowPolicies.md"]
tags:           []
---

# << Feature Title >>

## Description ✨
(Explain the feature, the user value, link to designs/epics)

## Acceptance Criteria ✅
*   - [ ] Criterion 1 for the feature to be considered done.
*   - [ ] Criterion 2...

## Notes / Impediments 🚧
(Add notes or blocker details here)
```

### `🛠️_task_item.md` (Template)

```markdown
---
id:             # ITEM-NNN
title:          # 🛠️ Task: Technical objective
status:         "📥 Input Queue" # Or appropriate starting state
type:           "🛠️ Task"
priority:       "▶️ Medium"
# blocked:        false
# blocked_reason:
created_date:   # YYYY-MM-DD
updated_date:   # YYYY-MM-DD HH:MM:SS
# assigned_to:
parent_area:    # Path to AREA/_overview.md
# related_docs:
tags:           ["technical", ...]
---

# << Task Title >>

## Task Details 🛠️
(Explain the technical work required)

## Acceptance Criteria ✅
*   - [ ] Technical outcome 1 is met (e.g., Service deployed).
*   - [ ] Technical outcome 2 is met (e.g., Documentation updated).

## Notes / Impediments 🚧
(Add notes or blocker details here)
```

*(Create a similar template for `🐞_bug_item.md` including fields for reproduction steps etc.)*

## 10. 🌊 Implementing Kanban Flow with MDTM

1.  **Define Workflow & Policies:** Team agrees on the workflow columns (`status` values), WIP limits for relevant columns, and policies for pulling work. Document these in `docs/WorkflowPolicies.md`.
2.  **Visualize:** Use an IDE extension or tool that reads the `tasks/**/*.md` files and renders a board view based on the `status` field. The tool should ideally show WIP counts per column vs. the limits.
3.  **Input Queue Management:** Prioritize items in the initial input queue(s) (e.g., `📥 Ready for Analysis`, `💻 Ready for Dev`) based on `priority` or other policies.
4.  **Pull Work:** When a team member has capacity *and* the WIP limit for their next work stage allows, they **pull** an item from the preceding "Ready" queue. They update the item's `status:` and set `assigned_to:`. Commit the change.
5.  **Work & Update:** As work progresses, update notes in the Markdown body. When criteria to move to the next state are met, update the `status:` field and commit.
6.  **Handle Blockers:** If an item is blocked, change `status: 🚧 Blocked`, fill in `blocked_reason:`, and focus on resolving the blocker. Blocked items usually count towards WIP unless policies state otherwise. Once unblocked, revert status to the previous WIP state. Commit changes.
7.  **Manage Flow:** Regularly observe the board (via IDE/tool) to identify bottlenecks (columns where items frequently queue or exceed WIP limits). Discuss and address these bottlenecks.
8.  **Measure & Improve:** Use the `updated_date` timestamps (requires high resolution and consistent updates) with scripts or tools to calculate Cycle Time, Lead Time, and Throughput. Use these metrics to inform process improvement experiments.

## 11. Best Practices for Kanban MDTM 👍

*   **🧘 Respect WIP Limits:** This is fundamental to Kanban. Use visualization tools to help the team see and adhere to limits.
*   **🚶 Manage Flow:** Focus on getting items through the system smoothly. Address bottlenecks proactively.
*   **📜 Make Policies Explicit:** Ensure everyone understands the workflow, statuses, WIP limits, and pull criteria (document in `docs/WorkflowPolicies.md`).
*   **⏱️ Update Status Promptly:** Keep the board accurate by updating the `status:` field as soon as work state changes. Commit frequently.
*   **✅ Define "Done" Clearly:** Use Acceptance Criteria for individual items and have clear policies for moving between columns (Definition of Ready / Definition of Done for stages).
*   **🔍 Visualize Bottlenecks:** Use the board visualization to see where work piles up.
*   **🌱 Continuously Improve:** Use flow metrics and team observations to identify areas for improvement and run experiments.

## 12. 💡 IDE Integration: Enhancing Kanban MDTM

A well-integrated IDE is crucial for effectively using MDTM with Kanban:

*   **📊 Kanban Board Visualization:** REQUIRED. Render `.md` files as cards in columns based on `status`. Show WIP counts per column vs. configured limits (highlight if exceeded). Allow filtering by `type`, `tags`, `assigned_to`.
*   **💧 Drag-and-Drop Status Changes:** Allow moving cards between columns to automatically update the `status:` field in the YAML and `updated_date`.
*   **⏱️ Flow Metrics Calculation:** Ideally, calculate and display Cycle Time, Lead Time, CFD (Cumulative Flow Diagram) based on status change history (`updated_date`).
*   **🚧 Blocker Highlighting:** Visually flag items with `status: 🚧 Blocked`.
*   **📝 Template Integration:** Easily create new work items using files from `_templates/`.
*   **🔗 Linking:** Link work items, commits, PRs, and documentation easily.

## 13. Conclusion ✅

Implementing **Kanban with MDTM** provides a highly flexible, transparent, and repository-centric system for managing workflow. By defining clear **workflow statuses** in YAML, organizing work logically, adhering to **WIP limits**, and focusing on **flow**, teams can optimize their delivery process. This method leverages the simplicity and power of Markdown and Git, offering an excellent foundation for continuous improvement and efficient value delivery, especially when augmented by supportive IDE tooling.