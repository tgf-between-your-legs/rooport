# 🏗️ Implementing Critical Path Method (CPM) Data Management with MDTM

**Version:** 1.0
**Date:** 2025-04-05

## 1. Introduction: Structuring Your Project Schedule Data 🗓️

This guide provides the detailed "how-to" for using the **Markdown-Driven Task Management (MDTM)** system to capture and manage the essential data needed for the **Critical Path Method (CPM)**. We'll cover the specific folder structures, file naming conventions, YAML metadata, templates, and examples needed to define project tasks, estimate their durations, and map their dependencies within your Git repository.

**The Goal:** To establish a clear, consistent, and practical MDTM setup that serves as a structured **data source** for external CPM calculation tools 📊. We focus on accurately capturing the inputs required for CPM analysis.

**Core Implementation Principles:**
*   **Task as `.md` File:** Each distinct project activity is a Markdown file 📄.
*   **CPM Data in YAML:** Key CPM inputs – unique Task IDs 🆔, Durations ⏱️, and Dependencies 🔗 – are stored in the YAML front matter ⚙️.
*   **WBS Organization:** Use folders to mirror the project's Work Breakdown Structure 📂.
*   **Emoji Markers:** Use emojis consistently 🏷️ for visual identification and clarity.
*   **Templates for Consistency:** Rely on predefined templates 📄 to standardize task definition and ensure all necessary CPM data fields are present.
*   **External Calculation Required:** MDTM **stores** the data; separate tools **calculate** the critical path and schedule.

**❗ CRITICAL REMINDER:** This MDTM setup **organizes and stores the input data** for CPM. It **DOES NOT perform the CPM calculations** (finding the critical path, float, ES/EF/LS/LF dates). You **MUST** use external software or scripts that can parse these MDTM files to perform the analysis.

## 2. 🗂️ Directory Structure: Aligning with WBS

Structure your `tasks/` directory to reflect your project's Work Breakdown Structure (WBS) for logical organization.

```
PROJECT_ROOT/
├── docs/                    # Supporting Project Docs (Charter, Scope)
├── tasks/                   # 👈 **Main MDTM Directory for CPM Task Data**
│   ├── _templates/          # 📄 Template for CPM task files (Essential!)
│   │   └── 🏗️_cpm_task.md
│   │
│   ├── 1.0_Initiation/        # 📂 WBS Level 1
│   │   ├── _wbs_overview.md   # Optional: Summary for this WBS branch
│   │   ├── 1.1_Define_Goals.md       # 📝 CPM Task File
│   │   └── 1.2_Feasibility_Study.md  # 📝 CPM Task File
│   │
│   ├── 2.0_Planning/          # 📂 WBS Level 1
│   │   ├── 2.1_Create_WBS/      # 📂 WBS Level 2
│   │   │   └── 2.1.1_Identify_Deliverables.md # 📝 CPM Task File
│   │   ├── 2.2_Schedule_Development/ # 📂 WBS Level 2
│   │   │   ├── 2.2.1_Define_Activities.md # 📝 CPM Task File (Defines other tasks)
│   │   │   ├── 2.2.2_Sequence_Activities.md # 📝 CPM Task File (Defines dependencies)
│   │   │   └── 2.2.3_Estimate_Durations.md  # 📝 CPM Task File (Defines durations)
│   │   └── 2.3_Resource_Plan.md
│   │
│   ├── 3.0_Execution/         # 📂 WBS Level 1
│   │   ├── 3.1_Component_A_Dev/ # 📂 WBS Level 2
│   │   │   ├── 3.1.1_Code_Module_X.md # 📝 CPM Task File
│   │   │   └── 3.1.2_Test_Module_X.md # 📝 CPM Task File
│   │   └── 3.2_Integration.md
│   │
│   └── 4.0_Closure/           # 📂 WBS Level 1
│       └── 4.1_Project_Review.md
│
├── archive/                 # 📦 Optional: Completed tasks
│   └── ...
└── README.md
```

**Implementation Rules:**
*   ✅ **WBS Folder Structure:** Mirror your WBS hierarchy using numbered folders (e.g., `1.0_PhaseName`, `2.1_SubPhase`).
*   ✅ **Task File Location:** Place each task `.md` file within its corresponding WBS folder.
*   ✅ **WBS Overview Files (`_wbs_overview.md`):** Optional files within WBS folders to describe that section of work.
*   ✅ **Templates (`_templates/`):** Use a dedicated `🏗️_cpm_task.md` template to ensure required fields are always present.

## 3. 📄 Task File Naming Conventions

Link file names visually to the WBS structure.

**Format:** `WBSID_short_description.md`

*   **`WBSID`:** The WBS identifier (e.g., `1.1`, `2.2.1`, `3.1.2`). Helps locate tasks quickly based on the WBS.
*   **`_`:** Separator.
*   **`short_description`:** Brief, lowercase, underscore-separated task name.
*   **`.md`:** Markdown extension.

**Examples:**
*   `1.1_define_goals.md`
*   `2.2.3_estimate_durations.md`
*   `3.1.1_code_module_x.md`

*(Using WBS IDs in names makes finding files easier when looking at dependencies.)*

## 4. ⚙️ YAML Front Matter: Capturing Essential CPM Inputs

This section is **critical** for storing the data needed by CPM calculation tools.

```yaml
---
# 🆔 Task Identification (Required for Linking)
id:             # REQUIRED. Project-wide UNIQUE identifier. **Cannot have duplicates!** Use WBS ID or simple T### format (e.g., "Task_1.1", "T005"). This ID is used in `depends_on`.
title:          # REQUIRED. Human-readable name of the task/activity.

# ⏱️ Duration Estimation (Required for Scheduling)
duration:       # REQUIRED. Numeric estimate of task length. (e.g., 5, 10, 0 for Milestones).
duration_unit:  # REQUIRED. Consistent unit for ALL tasks in the project. (e.g., "days", "hours", "weeks").

# 🔗 Dependency Mapping (Required for Network Logic)
depends_on:     # REQUIRED. List of `id` strings for immediate predecessors. Use `[]` for tasks with no dependencies (start tasks). E.g., ["Task_1.1", "Task_2.3"].

# 📊 Status & Progress Tracking (Recommended)
status:         # Recommended. Workflow state. E.g., "⚪ Not Started", "🏗️ In Progress", "✅ Completed". See Statuses below.
# percent_complete: # Optional. Numeric (0-100).
# start_date_actual: # Optional. Actual start (YYYY-MM-DD).
# finish_date_actual: # Optional. Actual finish (YYYY-MM-DD).

# 🧑‍💻 Context & Assignment
wbs_id:         # Recommended. The WBS identifier string (e.g., "3.1.1"). Matches folder structure/filename convention.
# assigned_to:    # Optional. Responsible person/team.
# related_docs:   # Optional. Links to specifications, etc.
tags:           # Optional. Keywords for filtering.

# ======================================================================
# ⚠️ CALCULATED FIELDS (Output from External CPM Tool - DO NOT EDIT HERE)
# These fields are determined by running a CPM calculation on the data above.
# They should NOT be manually entered or edited in this source MDTM file.
# ======================================================================
# critical_path:  # (Boolean) Is this task on the critical path?
# total_float:    # (Number) Total slack/float for this task.
# free_float:     # (Number) Free slack/float for this task.
# early_start:    # (Number/Date) Earliest possible start.
# early_finish:   # (Number/Date) Earliest possible finish.
# late_start:     # (Number/Date) Latest allowable start.
# late_finish:    # (Number/Date) Latest allowable finish.
---

# << Task Title >>

## Task Objective / Description 🏗️
(Clearly define the work to be performed in this task. What does 'Done' look like?)

## Duration Basis / Assumptions 🧐
(Explain how the `duration` was estimated. Note key assumptions, e.g., resource availability, complexity.)

## Predecessor Rationale (Why `depends_on`?) 🔗
(Optional but helpful: Briefly explain *why* this task depends on the listed predecessors.)

## Resources Required 🛠️
(List key personnel, equipment, information needed.)
```

**Implementation Notes:**
*   **`id:` Uniqueness:** Stress that the `id` MUST be unique across the entire project. This is how dependencies are linked.
*   **`duration_unit:` Consistency:** All tasks MUST use the same `duration_unit`. The calculation tool needs this consistency.
*   **`depends_on:` Accuracy:** This defines the project network. Mistakes here invalidate the schedule. List *immediate* predecessors only.
*   **Calculated Fields Section:** Clearly demarcate that CPM results (ES, LF, float, critical path) are outputs from external tools and **do not belong** in this source data file.

## 5. 🏷️ Standardized Field Values & Emojis

Define consistent terms, especially for status and units.

*   **Status (`status:`):**
    *   `⚪ Not Started`
    *   `🏗️ In Progress`
    *   `✅ Completed`
    *   `🚧 Blocked` (Optional)
*   **Duration Unit (`duration_unit:`):** Choose ONE for the project: `days`, `hours`, `weeks`.
*   **ID (`id:`):** Establish a clear, unique convention:
    *   WBS-based: `Task_1.1`, `Task_2.2.1` (ensure no separator conflicts with WBS dots/underscores)
    *   Sequential: `T001`, `T002`, `T003`...
    *   Descriptive: `DefineGoals`, `CodeModuleX` (ensure uniqueness!)

## 6. 📝 Markdown Body: Providing Task Context

Use the body to explain the task beyond the core CPM data.

*   **Task Objective / Description (`## Task Objective / Description 🏗️`):** What work is involved? What is the deliverable or outcome?
*   **Duration Basis / Assumptions (`## Duration Basis / Assumptions 🧐`):** Justify the `duration` estimate. List assumptions (e.g., "Assumes senior developer assigned," "Based on similar past task").
*   **Predecessor Rationale (`## Predecessor Rationale 🔗` - Optional):** Explain *why* task B must follow task A (e.g., "Cannot test code before it's written," "Need approved design before building"). Helps validate dependencies.
*   **Resources Required (`## Resources Required 🛠️`):** List key people, tools, materials.

## 7. 📄 Example Template (`tasks/_templates/🏗️_cpm_task.md`)

```markdown
---
# 🆔 Task Identification (Required)
id:             # << UNIQUE_PROJECT_ID (e.g., Task_1.2 or T002) >>
title:          # << Clear, Concise Task Name >>

# ⏱️ Duration Estimation (Required)
duration:       # << Numeric value (e.g., 10) >>
duration_unit:  "days" # << Project's Consistent Unit (e.g., days) >>

# 🔗 Dependency Mapping (Required)
depends_on:     # << ["ID_of_Pred1", "ID_of_Pred2"] or [] >>

# 📊 Status & Progress Tracking
status:         "⚪ Not Started"
# percent_complete: 0
# start_date_actual:
# finish_date_actual:

# 🧑‍💻 Context & Assignment
wbs_id:         # << WBS Identifier (e.g., "1.2") >>
# assigned_to:
# related_docs:
tags:           []

# ======================================================================
# ⚠️ CALCULATED FIELDS (Output from External CPM Tool - DO NOT EDIT HERE)
# ======================================================================
# critical_path:
# total_float:
# free_float:
# early_start:
# early_finish:
# late_start:
# late_finish:
---

# << Task Title >>

## Task Objective / Description 🏗️
(Detailed definition of the work for this task.)

## Duration Basis / Assumptions 🧐
*   (Estimated based on...)
*   (Assumes...)

## Predecessor Rationale (Why `depends_on`?) 🔗
*   (Depends on Task X because...)
*   (Depends on Task Y because...)

## Resources Required 🛠️
*   (List resources needed)
```

## 8. 🔄 Workflow: Data Management & Calculation Cycle

1.  **Plan & Define:** Create all task `.md` files, assigning unique `id`s and placing them in the WBS structure.
2.  **Estimate & Link:** Fill in realistic `duration` estimates (and consistent `duration_unit`). Carefully define the `depends_on` lists using the correct predecessor `id`s.
3.  **Commit:** Save all task data to Git. This is your baseline schedule input.
4.  **Calculate 📊:** Feed the data (all `.md` files) into your chosen external CPM tool/script. This tool parses the `id`, `duration`, `depends_on` fields.
5.  **Analyze Results:** The external tool outputs the critical path, task floats, ES/EF/LS/LF dates. Review this schedule information.
6.  **Execute & Track:** As the project progresses, update the `status`, `percent_complete`, `start_date_actual`, `finish_date_actual` fields in the MDTM files. Commit these updates.
7.  **Update & Re-Calculate:** If task durations are re-estimated, dependencies change, or actual progress deviates significantly, update the relevant `.md` files (duration, dependencies, status). **You must then re-run the external CPM calculation** to see the impact on the schedule.

## 9. ✅ Conclusion: MDTM as Your CPM Data Foundation

Using MDTM to manage data for the **Critical Path Method** provides a structured, version-controlled foundation for your project schedule. By meticulously defining tasks, durations, and dependencies in `.md` files with clear YAML metadata, you create a reliable **input source** for specialized CPM calculation tools. Remember that MDTM organizes the *what*, *how long*, and *what comes first*; the actual schedule calculation (critical path, float, dates) **requires external processing** of this well-structured data. Maintain data accuracy and consistency for meaningful schedule analysis.