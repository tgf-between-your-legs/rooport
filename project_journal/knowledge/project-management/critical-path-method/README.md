# 🗓️ Implementing Critical Path Method (CPM) with MDTM: A Data Management Guide

**Version:** 1.0
**Date:** 2025-04-05

## 1. Overview: Structuring CPM Data in Markdown Tasks 🏗️

Welcome! This guide explains how to use the **Markdown-Driven Task Management (MDTM)** system (Markdown files 📄, YAML metadata ⚙️, Git tracking <0xF0><0x9F><0x9A><0xB2>️) to **capture and manage the data required for the Critical Path Method (CPM)**. CPM is a project modeling technique focused on scheduling, identifying task dependencies, determining the longest path (critical path), and calculating task float (slack).

**The Core Idea:** Use individual `.md` files to represent each **Activity/Task** in your project plan. The crucial CPM data – **Task Durations ⏱️** and **Task Dependencies 🔗** – are stored within the YAML front matter of these files. This creates a structured, version-controlled dataset that can be **fed into an external CPM calculation tool or script** 📊 to determine the critical path, float, and key schedule dates.

**How MDTM Supports CPM Data Management:**
*   **Task Definition:** Each `.md` file clearly defines a specific project activity.
*   **Duration Capture:** A dedicated `duration:` field in YAML stores the estimated time for each task.
*   **Dependency Mapping:** A `depends_on:` field in YAML lists the unique IDs of prerequisite tasks.
*   **Data Organization:** Files can be organized logically (e.g., using a Work Breakdown Structure - WBS - reflected in folders).
*   **Version Control:** Git tracks all changes to task definitions, durations, and dependencies, providing history and traceability.
*   **Data Source:** MDTM files act as the structured input source for external CPM analysis tools.

**❗ CRITICAL LIMITATION:** MDTM itself **DOES NOT CALCULATE** the critical path, float, early/late start/finish dates. It only *stores the input data*. You **MUST use separate software, scripts, or libraries** that can parse these MDTM files (specifically the `id`, `duration`, and `depends_on` fields) to perform the actual CPM network analysis and calculations. This guide focuses on structuring the data correctly for such tools.

## 2. Why Use MDTM for CPM Data? 🤔

While not a calculation engine, using MDTM for CPM data offers benefits:

*   **🧩 Integrated Data:** Keep task definitions, durations, and dependencies within the project repository, close to related documentation or even code (if applicable).
*   ** Git Transparency & History:** Track every change to estimates and dependencies. Understand *why* the schedule might change based on input data modifications.
*   **📝 Clear Task Definitions:** Encourages clear definition of each activity in the Markdown body.
*   **🤝 Collaborative Data Input:** Multiple team members can contribute to defining tasks and dependencies within the Git workflow.
*   **🤖 Potential for Automation:** The structured YAML data is easily parsable by scripts for feeding into CPM calculation engines or custom reporting. AI assistants can potentially help generate or validate the structure.
*   **🏷️ Simple & Accessible:** Uses familiar text files and Git.

**Suitability:** This approach is best for projects where:
*   Tasks are well-defined and dependencies are clearly understood.
*   Schedule optimization and identifying critical tasks are major goals.
*   The project structure is relatively stable.
*   You have access to or can create tooling to perform the CPM calculations based on the MDTM data.

## 3. Core CPM Concepts in MDTM 🧱

Mapping CPM terms to MDTM elements:

*   **Activity / Task:** An individual `.md` file.
*   **Task ID:** The unique `id:` field in the YAML front matter. **Crucial for dependency linking.**
*   **Task Duration:** The `duration:` field in YAML (e.g., in days, hours).
*   **Task Dependencies (Predecessors):** The `depends_on:` list in YAML, containing the `id`s of prerequisite tasks.
*   **Work Breakdown Structure (WBS):** Can be represented by the folder structure within `tasks/`.
*   **Network Diagram Data:** The combination of all `id`, `duration`, and `depends_on` fields across all task files provides the data needed to construct the network.
*   **Calculated Fields (via External Tool):** Early Start (ES), Early Finish (EF), Late Start (LS), Late Finish (LF), Float/Slack, Critical Path identification. *These are NOT stored directly in MDTM files but derived from them.*
*   **Task Status:** A `status:` field can track progress (`Not Started`, `In Progress`, `Completed`).

## 4. 🗂️ Recommended Directory Structure: WBS-Based

Organize files reflecting the project's Work Breakdown Structure (WBS).

```
PROJECT_ROOT/
├── docs/                    # Supporting Docs (Project Charter, Scope Statement)
├── tasks/                   # 👈 **Main MDTM Directory for CPM Task Data**
│   ├── _templates/          # 📄 Template for CPM task files
│   │   └── 🏗️_cpm_task.md
│   │
│   ├── 1.0_Project_Initiation/ # 📂 WBS Level 1
│   │   ├── 1.1_Define_Scope.md       # 📝 Task File
│   │   └── 1.2_Secure_Funding.md
│   │
│   ├── 2.0_Planning/           # 📂 WBS Level 1
│   │   ├── 2.1_Develop_Project_Plan/ # 📂 WBS Level 2
│   │   │   ├── 2.1.1_Identify_Tasks.md # 📝 Task File (This task defines other tasks!)
│   │   │   └── 2.1.2_Estimate_Durations.md
│   │   ├── 2.2_Define_Resources.md
│   │
│   ├── 3.0_Execution/          # 📂 WBS Level 1
│   │   ├── 3.1_Develop_Module_A/   # 📂 WBS Level 2
│   │   │    ├── 3.1.1_Code_Feature_X.md # 📝 Task File
│   │   │    └── 3.1.2_Test_Feature_X.md
│   │   └── 3.2_Develop_Module_B.md
│   │
│   └── 4.0_Closure/            # 📂 WBS Level 1
│       └── 4.1_Final_Report.md
│
├── archive/                 # 📦 Optional: Completed tasks
│   └── ...
└── README.md
```

**Key Structural Points:**
*   ✅ **WBS Alignment:** Structure folders to match your project's WBS for clear organization. Use numbering consistent with WBS levels.
*   ✅ **Task Files:** Reside within the relevant WBS element folder.
*   ✅ **Templates:** Use a template to ensure all necessary CPM fields (`id`, `duration`, `depends_on`) are present.

## 5. 📄 Task File Naming Conventions

Focus on clarity and consistency, potentially linking to WBS.

**Format:** `WBSID_short_description.md` or `NNN_short_description.md`

*   **`WBSID` (Optional but recommended):** The WBS identifier for this task (e.g., `1.1`, `2.1.1`).
*   **`NNN` (Alternative):** A simple project-wide sequence number if WBS IDs in names are too complex.
*   **`short_description`:** Brief, lowercase, underscore-separated task name.
*   **`.md`:** Markdown extension.

**Examples:**
*   `1.1_define_scope.md`
*   `2.1.1_identify_tasks.md`
*   `3.1.1_code_feature_x.md`
*   (Alternative) `001_define_scope.md`, `005_identify_tasks.md`

## 6. ⚙️ YAML Front Matter: Capturing CPM Data

This is the core data collection section for CPM.

```yaml
---
# 🆔 Task Identification & Core CPM Data
id:             # REQUIRED. Unique Project-wide ID for this task. **MUST be unique**. E.g., "T001", "DefineScope", "CodeFeatX". Used in `depends_on`.
title:          # REQUIRED. Human-readable task name.
duration:       # REQUIRED. Estimated task duration (Number). Specify unit consistently (e.g., days, hours). E.g., 5 (meaning 5 days if unit is days).
duration_unit:  # REQUIRED. Unit for duration. E.g., "days", "hours", "weeks". Must be consistent across project for calculation.
depends_on:     # REQUIRED (List of Strings). List of `id`s of tasks that MUST be completed before this task can start. E.g., ["T005", "T012"]. Use empty list `[]` for tasks with no predecessors.

# 📊 Status & Progress Tracking (Optional but Recommended)
status:         # Recommended. E.g., "⚪ Not Started", "🏗️ In Progress", "✅ Completed". See Statuses.
percent_complete: # Optional. Number (0-100). How much of the *duration* is estimated complete.
# start_date:     # Optional. Actual start date (YYYY-MM-DD).
# finish_date:    # Optional. Actual finish date (YYYY-MM-DD).

# 🧑‍💻 Context & Assignment
wbs_id:         # Recommended. WBS identifier string (e.g., "3.1.1").
assigned_to:    # Optional. Resource/Team responsible.
related_docs:   # Optional. Links to specs, plans, diagrams.
tags:           # Optional. Keywords.

# ⚠️ Calculated Fields (DO NOT MANUALLY FILL - These come from external CPM tool)
# critical_path_member: # Boolean (true/false) - Determined by calculation.
# total_float:          # Number - Determined by calculation.
# early_start:          # Date/Number - Determined by calculation.
# early_finish:         # Date/Number - Determined by calculation.
# late_start:           # Date/Number - Determined by calculation.
# late_finish:          # Date/Number - Determined by calculation.
---

# << Task Title >>

## Description / Objective 🏗️
... Markdown Body: Detail the work involved in this task ...

## Assumptions / Constraints 🧐
... Note any assumptions made for duration estimate or dependencies ...

## Resources Needed 🛠️
... List key resources (personnel, equipment, info) ...
```

**Key CPM YAML Fields:**
*   `id:`: **Absolutely critical** unique identifier for linking dependencies. Must be consistent and unique across the entire project.
*   `duration:`: **Absolutely critical** numerical estimate of work effort.
*   `duration_unit:`: **Absolutely critical** unit for duration, must be consistent.
*   `depends_on:`: **Absolutely critical** list of predecessor task `id`s. Correctness determines the network structure.
*   `status:`, `percent_complete:`: Useful for tracking progress against the plan.
*   **Calculated Fields Warning:** Explicitly comment that fields like `critical_path_member`, `total_float`, `ES/EF/LS/LF` are **outputs** from external tools and should *not* be manually entered in these source files.

## 7. 🏷️ Standardized Field Values & Emojis

Define values, especially for status and duration units.

*   **Status (`status:`):**
    *   `⚪ Not Started`: Task has not begun.
    *   `🏗️ In Progress`: Task has started but is not complete.
    *   `✅ Completed`: Task finished.
    *   `🚧 Blocked`: (Optional) Progress halted.
*   **Duration Unit (`duration_unit:`):** Be consistent! Choose one for the project: `days`, `hours`, `weeks`.
*   **Task ID (`id:`):** Choose a robust, unique convention. Simple (`T001`, `T002`) or descriptive (`DefineScope`, `CodeModA`) or WBS-based (`Task_1_1`, `Task_3_1_1`). Ensure no duplicates!

## 8. 📝 Markdown Body: Task Details

Use the body for human-readable context.

*   **Description / Objective (`## Description / Objective 🏗️`):** Clearly define the scope of work for this task. What does "Completed" mean for this specific activity?
*   **Assumptions / Constraints (`## Assumptions / Constraints 🧐`):** Document key assumptions made when estimating the `duration` or defining `depends_on`. Note any constraints.
*   **Resources Needed (`## Resources Needed 🛠️`):** List key personnel, equipment, information, etc., required.

## 9. 📄 Example Template (`tasks/_templates/🏗️_cpm_task.md`)

```markdown
---
# 🆔 Task Identification & Core CPM Data
id:             # << UNIQUE_PROJECT_WIDE_ID >>
title:          # << Clear Task Name >>
duration:       # << Numeric Duration Estimate >>
duration_unit:  # << e.g., "days" (Be Consistent!) >>
depends_on:     # << List of prerequisite task 'id's, e.g., ["T001", "T005"] or [] >>

# 📊 Status & Progress Tracking
status:         "⚪ Not Started"
# percent_complete: 0
# start_date:
# finish_date:

# 🧑‍💻 Context & Assignment
wbs_id:         # << WBS Identifier (e.g., "1.2.3") >>
# assigned_to:
# related_docs:
tags:           []

# ⚠️ Calculated Fields (DO NOT MANUALLY FILL)
# critical_path_member:
# total_float:
# early_start:
# early_finish:
# late_start:
# late_finish:
---

# << Task Title >>

## Description / Objective 🏗️
(Define the work to be done for this task)

## Assumptions / Constraints 🧐
*   (Assumption: Resource X is available)
*   (Constraint: Must use library Y)

## Resources Needed 🛠️
*   (e.g., Senior Developer, Test Environment A)
```

## 10. ⚙️ Workflow: Data Input and External Calculation

1.  **Define Tasks:** Create `.md` files for all project activities using the template. Assign unique `id`s. Place them in the correct WBS folder.
2.  **Estimate Durations:** Fill in the `duration` and consistent `duration_unit` for each task. Document assumptions in the body.
3.  **Map Dependencies:** Carefully fill in the `depends_on` list for each task, using the unique `id`s of its predecessors. Ensure accuracy – this defines the network logic.
4.  **Commit Data:** Store all task files in Git.
5.  **📊 External Calculation:**
    *   Use a script or CPM software tool that can **parse all the `.md` files** in your `tasks/` directory.
    *   The tool needs to extract `id`, `title`, `duration`, and `depends_on` for every task.
    *   The tool performs the CPM network analysis (Forward Pass, Backward Pass).
    *   **Output:** The tool calculates ES, EF, LS, LF, Total Float for each task, identifies the Critical Path(s), and determines the minimum project duration.
6.  **Analyze Results:** Review the output from the CPM tool to understand the schedule, critical tasks, and areas with float.
7.  **Track Progress:** As work progresses, update the `status` and potentially `percent_complete`, `start_date`, `finish_date` fields in the relevant `.md` files. Commit these updates.
8.  **Re-Calculate as Needed:** If `duration` estimates change, `depends_on` links are modified, or tasks are added/removed, you **must re-run the external CPM calculation** to get an updated schedule analysis.

## 11. ⚠️ Tooling is Essential!

**Repeating the Limitation:** This MDTM setup **only stores the data**. You *need* an external mechanism to perform the CPM calculations. This could be:
*   A dedicated project management tool that can import data in a compatible format (you might need a script to convert MDTM YAML to CSV/XML).
*   A script (e.g., Python with libraries like `networkx`) that parses the YAML front matter from all `.md` files and implements the CPM algorithm.
*   Spreadsheet software (like Excel or Google Sheets) where you manually input or import the data and use formulas/macros for CPM calculations.

Consider how your chosen tool will ingest the data structured in these MDTM files.

## 12. Best Practices for MDTM CPM Data 👍

*   **🆔 Unique & Consistent IDs:** Absolutely essential for `depends_on` links to work correctly.
*   **⏱️ Consistent Duration Units:** Use the *same unit* (`days`, `hours`) for all tasks in a project.
*   **🔗 Accurate Dependencies:** Double-check the `depends_on` lists. Incorrect dependencies invalidate the CPM results. Map *only* true technical predecessors.
*   **📝 Granularity:** Define tasks at an appropriate level of detail – not too large, not too small.
*   **💾 Version Control:** Commit changes to task data frequently to maintain history. Use meaningful commit messages.
*   **🔄 Update & Recalculate:** Keep task status and estimates updated, and re-run the external CPM calculation regularly or whenever significant input data changes.

## 13. Conclusion ✅

Using **MDTM to manage data for the Critical Path Method** provides a structured, version-controlled, and repository-integrated way to define project activities, their durations, and their dependencies. While MDTM excels at organizing this **input data**, remember that the core **CPM calculations must be performed by external tools or scripts** that parse these files. By maintaining accurate and consistent data in this MDTM structure, teams can effectively feed CPM analysis engines to gain valuable insights into project schedules, critical tasks, and potential delays.