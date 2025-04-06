# 🌊 MDTM - Waterfall Phase Adaptation: A Practical Guide

**Version:** 1.0
**Date:** 2025-04-05

## 1. Overview: Structured Phases in Markdown Tasks 📜

Welcome! This guide explains how to adapt the **Markdown-Driven Task Management (MDTM)** system for projects following a **Waterfall methodology**. While MDTM is often associated with more iterative approaches like Agile, its core principles (Markdown files 📄, YAML front matter ⚙️, Git integration <0xF0><0x9F><0x9A><0xB2>️) can be adapted to support the sequential phases characteristic of Waterfall.

**The Core Idea:** Represent the distinct Waterfall phases (Requirements, Design, Implementation, Testing, Deployment) using a **phase-based folder structure** 📂 within your `tasks/` directory. Emphasize comprehensive **upfront documentation** 📚 (like SRS and SDD) stored in `docs/` and heavily linked from tasks. Task progression focuses on completing work *within* a phase before moving *en masse* to the next.

This approach aims to provide the benefits of co-located, version-controlled tasks for teams comfortable with or required to use a Waterfall process. It's a way to bring structured task tracking into the repository even within a sequential framework.

**❗ Important Note:** Waterfall relies heavily on upfront planning, formal sign-offs, and managed change control, which are often better supported by dedicated PM tools. This MDTM adaptation provides *task tracking within phases* but relies on **team discipline** for managing phase transitions and formal approvals.

## 2. Why Adapt MDTM for Waterfall? 🤔

While seemingly different, adapting MDTM might be useful if:

*   Your team/organization prefers or mandates a Waterfall process.
*   You want task tracking directly within the Git repository alongside code and documentation.
*   You need a simple, text-based system accessible to both humans 🧑‍💻 and potentially AI assistants 🤖 for understanding phase-specific tasks.
*   You value the transparency and history provided by version-controlling task definitions.

**Key Differences from MDTM Feature Structure:**
*   **Organization:** Folders represent sequential **Phases**, not parallel Features.
*   **Workflow:** Progress is primarily measured by completing all tasks *within* a phase folder before starting the next phase (manual gate).
*   **Emphasis:** Stronger focus on linking to comprehensive upfront Requirements and Design documents.
*   **Flexibility:** Inherently less flexible than iterative MDTM approaches regarding changes mid-phase.

## 3. Core Concepts in Waterfall MDTM 🧱

This adaptation uses these building blocks:

1.  **📄 Task Files:** Standard Markdown (`.md`) files representing work items *within* a specific Waterfall phase.
2.  **⚙️ YAML Front Matter:** Structured metadata including ID, title, status *within the phase*, and crucial links to detailed requirements/design documents. May include an explicit `phase` field.
3.  **📂 Phase-Based Folder Structure:** A main `tasks/` directory with subdirectories named and ordered according to Waterfall phases (e.g., `01_Requirements`, `02_Design`, `03_Implementation`).
4.  **📚 Centralized Documentation:** Key Waterfall documents (SRS, SDD, Test Plan) reside prominently in the `docs/` folder and are the primary source of detailed specifications.
5.  **<0xF0><0x9F><0x9A><0xB2>️ Version Control (Git):** The entire `tasks/` and `docs/` structure is version-controlled.

## 4. 🌊 Directory Structure Conventions

Organize tasks sequentially by phase within the `tasks/` directory.

```
PROJECT_ROOT/
├── src/                      # Source Code (Primarily used in Implementation phase)
├── docs/                     # 👈 **CRUCIAL Waterfall Documentation Hub**
│   ├── 01_SoftwareRequirementsSpecification_SRS.md # 🎯 Requirements Doc
│   ├── 02_SoftwareDesignDocument_SDD.md          # 📐 Design Doc
│   ├── 03_TestPlan.md                            # 🧪 Test Plan Doc
│   └── 04_DeploymentPlan.md                      # 🚀 Deployment Plan Doc
├── tasks/                    # 👈 **Main MDTM Directory**
│   ├── _templates/           # 📄 Optional: Phase-specific task templates?
│   │   └── ⚙️_implementation_task.md
│   │
│   ├── 01_Requirements/        # 🎯 Phase 1: Requirements Gathering Tasks
│   │   ├── 001_🎯_define_user_roles.md
│   │   └── 002_🎯_document_functional_reqs.md
│   │
│   ├── 02_Design/              # 📐 Phase 2: Design Tasks
│   │   ├── 003_📐_design_database_schema.md
│   │   ├── 004_📐_create_ui_mockups.md
│   │   └── 005_📐_define_api_endpoints.md
│   │
│   ├── 03_Implementation/      # ⚙️ Phase 3: Coding Tasks
│   │   ├── 006_⚙️_implement_user_model.md
│   │   ├── 007_⚙️_build_login_api.md
│   │   └── 008_⚙️_create_login_frontend.md
│   │
│   ├── 04_Testing/             # 🧪 Phase 4: Testing Tasks
│   │   ├── 009_🧪_execute_unit_tests.md
│   │   ├── 010_🧪_perform_integration_testing.md
│   │   └── 011_🧪_conduct_user_acceptance_testing.md
│   │
│   ├── 05_Deployment/          # 🚀 Phase 5: Deployment Tasks
│   │   └── 012_🚀_deploy_to_production.md
│   │
│   └── AREA_ChangeRequests/    # 🔁 Optional: For tracking approved changes
│       └── CR_001_add_new_report_field.md
│
├── archive/                  # 📦 Optional: Completed/Closed tasks (mirrors `tasks/` phase structure)
│   └── ...
└── README.md
```

**Key Points:**
*   **Numbered Phase Folders:** Use numbers (e.g., `01_`, `02_`) to enforce sequence. Name folders clearly after the Waterfall phase.
*   **Emphasis on `docs/`:** This folder is paramount. Task files often act as pointers or checklists against items defined in these core documents.
*   **Sequential Flow:** The expectation is to complete work defined in `01_Requirements/` before moving substantially into `02_Design/`, and so on. This is managed by team process.
*   **Change Request Area:** An optional dedicated area for tracking formally approved changes that might impact tasks across phases.

## 5. 📄 Task File Naming Conventions

Simplicity often works best here.

**Format:** `NNN_🌀_short_description.md`

*   **`NNN`:** A three-digit sequence number (e.g., `001`, `002`, `045`). Can be project-wide or reset within each phase folder (project-wide is often simpler for unique IDs).
*   **`_🌀_`:** An emoji representing the **phase** the task belongs to (see Phase Emojis below) enclosed in underscores.
*   **`short_description`:** Brief, lowercase, underscore-separated description (e.g., `design_db_schema`, `implement_user_model`).
*   **`.md`:** Standard Markdown extension.

**Examples:**
*   `001_🎯_define_user_roles.md` (Requirements Phase)
*   `003_📐_design_db_schema.md` (Design Phase)
*   `006_⚙️_implement_user_model.md` (Implementation Phase)
*   `009_🧪_execute_unit_tests.md` (Testing Phase)
*   `012_🚀_deploy_to_production.md` (Deployment Phase)

## 6. ⚙️ YAML Front Matter for Waterfall Tasks

Adapt YAML fields to the Waterfall context.

```yaml
---
# 🆔 Task Identification & Core Metadata (Required)
id:             # REQUIRED. Unique ID (e.g., REQ-001, DES-003, IMPL-006). Convention: {PHASE_ABBR}-{NNN}
title:          # REQUIRED. Human-readable title (String). "Design Database Schema for User Auth"
phase:          # REQUIRED. The Waterfall phase this task belongs to (String). See Phases below. "📐 Design"
status:         # REQUIRED. Status *within this phase* (String). See Statuses below. "🟡 To Do"
type:           # REQUIRED. Type of work item (String). E.g., "📝 Definition", "📐 Design Element", "⚙️ Implementation Unit", "🧪 Test Case".

# ⏳ Scheduling & Effort (Optional - often defined at project level in Waterfall)
priority:       # Optional. Task importance if needed within phase. "▶️ Medium"
created_date:   # Recommended. Date task created (YYYY-MM-DD). "2025-04-05"
updated_date:   # Recommended. Date last modified (YYYY-MM-DD). "2025-04-05"
# due_date:       # Often managed at the Phase level in Waterfall.

# 🧑‍💻 Assignment & Responsibility (Optional)
assigned_to:    # Optional. Who is responsible for this task. "🧑‍💻 User:DatabaseTeam", "👥 Team:Frontend"
approved_by:    # Optional. Formal sign-off for this specific task/deliverable. "🧑‍⚖️ Manager:Jane"

# 🔗 Relationships & Context (CRITICAL in Waterfall)
requirement_ref: # CRITICAL. ID(s) or link(s) to specific item(s) in the SRS (String/List). ["docs/01_SRS.md#req-3.1.2"]
design_ref:     # CRITICAL (for Impl/Test). ID(s) or link(s) to specific item(s) in the SDD (String/List). ["docs/02_SDD.md#design-user-model"]
test_case_ref:  # CRITICAL (for Testing). ID(s) or link(s) to specific test cases in Test Plan (String/List). ["docs/03_TestPlan.md#tc-05"]
tags:           # Optional. Keywords (e.g., ["database", "authentication"]).

# 🔁 Change Request Link (Optional)
related_cr:     # Optional. Link to a Change Request task file if this task addresses a CR. "AREA_ChangeRequests/CR_001..."
---

# Title matching YAML title (optional redundancy)
## Description ✍️
... Markdown Body detailing task within the phase context ...
```

**Emoji Conventions for Fields:**
*   🆔 Identification
*   ⏳ Scheduling/Effort
*   🧑‍💻 Assignment/Approval
*   🔗 Relationships/Context
*   🔁 Change Request

## 7. 🏷️ Standardized Field Values & Emojis

Use these for consistency within the Waterfall adaptation.

### Phases (`phase:` field) & File Name Emojis

*   `🎯 Requirements`: (`_🎯_`) Defining *what* the system should do.
*   `📐 Design`: (`_📐_`) Defining *how* the system will be built.
*   `⚙️ Implementation`: (`_⚙️_`) Building the system (coding).
*   `🧪 Testing`: (`_🧪_`) Verifying the system meets requirements/design.
*   `🚀 Deployment`: (`_🚀_`) Releasing the system to users.
*   `🔁 Change Request`: (`_🔁_`) (Optional Area) Addressing approved changes.

### Statuses (`status:` field - *within a phase*)

*   `⚪ Blocked`: 🚧 Cannot proceed within this phase.
*   `🟡 To Do`: 📥 Ready to be started within this phase.
*   `🔵 In Progress`: 🏗️ Actively being worked on within this phase.
*   `🟣 Review/Approval`: 👀 Output needs review/sign-off within this phase.
*   `🟢 Done`: ✅ Completed for *this phase*.

*(Note: A task marked `🟢 Done` in `02_Design/` doesn't mean the *project* is done, just the design aspect of that task).*

### Priorities (`priority:` field - Use if needed for intra-phase prioritization)

*   `🔼 High`
*   `▶️ Medium`
*   `🔽 Low`

## 8. 📝 Markdown Body Conventions

The body provides context specific to the task's phase.

*   **Title:** Optional H1 matching YAML `title`.
*   **Description (`## Description ✍️`):** Explain the specific objective of *this task within its phase*. Reference the main `docs/` files for full details. E.g., for a Design task: "Detail the database schema for X based on SRS section Y."
*   **Inputs (`## Inputs 📥`):** What documents/previous phase outputs are needed? (e.g., "SRS Section 3.1", "Approved Architecture Diagram").
*   **Tasks / Checklist (`## Tasks / Checklist ✅`):** Break down the work *for this specific task and phase*. Use Markdown checklists (`- [ ]`).
    *   *(Design Task Example):* `- [ ] Define tables`, `- [ ] Specify column types`, `- [ ] Identify relationships`, `- [ ] Get schema reviewed`.
    *   *(Implementation Task Example):* `- [ ] Create model file`, `- [ ] Implement methods per SDD`, `- [ ] Write unit tests`, `- [ ] Code review pass`.
*   **Outputs / Deliverables (`## Outputs / Deliverables 📤`):** What does completing this task produce? (e.g., "Updated SDD Section 4.2", "Link to code commit/PR", "Test execution report").
*   **References (`## References 🔗`):** Direct links to relevant sections in `docs/SRS.md`, `docs/SDD.md`, etc. using `#section-links`. This is **crucial**.

## 9. 📄 Example Task Template (`tasks/_templates/⚙️_implementation_task.md`)

```markdown
---
# 🆔 Task Identification & Core Metadata
id:             # << GENERATE_UNIQUE_ID (e.g., IMPL-NNN) >>
title:          # << IMPLEMENT: Concise description >>
phase:          "⚙️ Implementation"
status:         "🟡 To Do"
type:           "⚙️ Implementation Unit"

# ⏳ Scheduling & Effort
priority:       "▶️ Medium"
created_date:   # << YYYY-MM-DD >>
updated_date:   # << YYYY-MM-DD >>

# 🧑‍💻 Assignment & Responsibility
assigned_to:    # Optional

# 🔗 Relationships & Context
requirement_ref: # << REQUIRED: Link to SRS section(s) >>
design_ref:     # << REQUIRED: Link to SDD section(s) >>
test_case_ref:  # Optional (Link to related test cases)
tags:           []

# 🔁 Change Request Link
related_cr:     # Optional
---

# << IMPLEMENT: Concise description >>

## Description ✍️
Implement the functionality described in the referenced Design Document section(s), ensuring it meets the linked Requirements.

## Inputs 📥
*   Requirements: See `requirement_ref` above.
*   Design: See `design_ref` above.
*   Architecture Guidelines: `docs/Architecture.md` (Example)

## Tasks / Checklist ✅
*   - [ ] Set up necessary file structure/boilerplate.
*   - [ ] Implement core logic according to Design specification.
*   - [ ] Implement data handling/persistence.
*   - [ ] Write comprehensive unit tests (mention coverage target?).
*   - [ ] Perform code self-review against standards.
*   - [ ] Submit for formal Code Review.
*   - [ ] Address code review feedback.
*   - [ ] Merge code to the main development branch.

## Outputs / Deliverables 📤
*   Code commit/Pull Request: [Link Here]
*   Unit Test execution results: [Link or Status Here]

## References 🔗
*   Requirement: `[SRS §X.Y](docs/01_SRS.md#req-X.Y)`
*   Design: `[SDD §A.B](docs/02_SDD.md#design-A.B)`
```

## 10. ➡️ Workflow and Phase Gates

*   **Intra-Phase Workflow:** Use the `status:` field (`🟡 To Do` -> `🔵 In Progress` -> `🟣 Review/Approval` -> `🟢 Done`) to track progress *within* a task's designated phase folder.
*   **Phase Gate (Manual Process):** The critical Waterfall step. Project management / team leads decide when *all essential tasks* in a phase folder (e.g., `02_Design/`) are `🟢 Done` and formally approved. Only then does significant work begin on tasks in the next phase folder (e.g., `03_Implementation/`). **MDTM files track task completion; the team manages the gate.**
*   **Documentation Updates:** Completing tasks in early phases often involves creating/updating the central `docs/` files (SRS, SDD). Subsequent phase tasks rely heavily on these finalized documents.
*   **Change Management:** If requirements or design change after a phase is "closed", a formal change request process should be followed. Approved changes might generate new tasks in the relevant phase folders or in the optional `AREA_ChangeRequests/` folder, potentially impacting already "Done" items in later phases (requiring rework).

## 11. Best Practices for Waterfall MDTM 👍👎

*   **🥇 Discipline is Paramount:** Adhere strictly to the sequential phase progression and formal sign-offs (managed outside MDTM files).
*   **📚 Prioritize `docs/`:** Keep the SRS, SDD, Test Plan, etc., detailed, up-to-date, and consider them the primary source of truth.
*   **🔗 Link Extensively:** Use `requirement_ref`, `design_ref`, etc., religiously in task YAML to connect tasks back to the core specifications. Use inline links too.
*   **✅ Clear Acceptance Criteria:** Even within Waterfall, define clear completion criteria for each task *within its phase context*.
*   **💾 Commit Regularly:** Version control changes to both `tasks/` and `docs/` frequently.
*   **✋ Understand Limitations:** Recognize that MDTM won't enforce phase gates or manage complex dependencies like dedicated PM tools. It's primarily for *tracking defined work items* within phases in a co-located, versioned way.

## 12. Limitations ⚠️

*   **No Automated Gates:** MDTM files don't automatically prevent starting work on the next phase. This relies on team process.
*   **Less Visibility on Cross-Phase Dependencies:** While `depends_on` can link tasks, visualizing complex dependencies across rigid phases is harder than in tools designed for it.
*   **Change Management Overhead:** Tracking the impact of changes across phases requires careful manual updates to tasks and potentially the core `docs/` files.
*   **Awkward Fit for Iteration:** Trying to force iterative loops *within* a strict Waterfall phase structure using MDTM can become confusing.

## 13. Conclusion ✅

Adapting MDTM for a Waterfall process is possible by structuring tasks around **sequential phase folders** and emphasizing strong links to **centralized documentation**. This **MDTM - Waterfall Phase Adaptation** provides a way to track phase-specific work within the project repository, leveraging Markdown, YAML, and Git. However, it requires significant team discipline to manage the crucial phase gates and change control inherent to Waterfall, and users should be aware of its limitations compared to dedicated Waterfall PM tools or more iterative MDTM approaches.