# 🌊 Implementing Waterfall Project Management with MDTM

**Version:** 1.0
**Date:** 2025-04-05

## 1. Introduction: Waterfall Meets Markdown Tasks 📜

This guide details how to implement a **Waterfall Project Management** approach using the **Markdown-Driven Task Management (MDTM)** system. We adapt MDTM's core ideas (Markdown files 📄, YAML metadata ⚙️, Git tracking <0xF0><0x9F><0x9A><0xB2>️) to fit the sequential, phase-based nature of Waterfall.

**The Goal:** To provide a structured, repository-integrated way to track tasks within distinct Waterfall phases, emphasizing upfront documentation and sequential progress.

**Key Principles:**
*   **Phase-Based Organization:** Folders represent sequential Waterfall phases 📂.
*   **Documentation is King:** Heavy reliance on detailed upfront documents (SRS, SDD) in a central `docs/` folder 📚.
*   **Sequential Workflow:** Tasks within one phase are largely completed before moving to the next phase (manual gate-keeping by the team).
*   **Task Focus:** MDTM files primarily track the execution of work defined *within* each phase, often referencing the main documents.

**❗ Note:** This MDTM adaptation tracks tasks within phases. The critical Waterfall aspects like formal phase-gate reviews, sign-offs, and strict change control **must be managed by the team's process** outside the MDTM files themselves.

## 2. 🗂️ Directory Structure: The Waterfall Flow

Structure the `tasks/` directory to mirror the sequential Waterfall phases.

```
PROJECT_ROOT/
├── src/                      # Source Code (Populated mainly during Implementation)
├── docs/                     # 👈 **CENTRAL HUB for Waterfall Documents**
│   ├── 01_Requirements_SRS.md  # 🎯 Software Requirements Specification
│   ├── 02_Design_SDD.md        # 📐 Software Design Document
│   ├── 03_Test_Plan.md         # 🧪 Test Plan & Cases
│   └── 04_Deployment_Plan.md   # 🚀 Deployment Strategy
├── tasks/                    # 👈 **Main MDTM Task Directory**
│   ├── _templates/           # 📄 Optional: Templates for phase-specific tasks
│   │   ├── 🎯_requirement_task.md
│   │   ├── 📐_design_task.md
│   │   ├── ⚙️_implementation_task.md
│   │   └── 🧪_testing_task.md
│   │
│   ├── 01_Requirements/        # 🎯 Phase 1: Define WHAT
│   │   ├── _phase_overview.md  # Optional: Summary/Goals for this Phase
│   │   ├── 001_🎯_gather_stakeholder_needs.md
│   │   └── 002_🎯_finalize_srs_section_3.md
│   │
│   ├── 02_Design/              # 📐 Phase 2: Define HOW
│   │   ├── _phase_overview.md
│   │   ├── 003_📐_design_database_schema.md
│   │   └── 004_📐_create_architecture_diagram.md
│   │
│   ├── 03_Implementation/      # ⚙️ Phase 3: BUILD the system
│   │   ├── _phase_overview.md
│   │   ├── 005_⚙️_build_user_auth_module.md
│   │   └── 006_⚙️_implement_api_endpoint_X.md
│   │
│   ├── 04_Testing/             # 🧪 Phase 4: VERIFY the system
│   │   ├── _phase_overview.md
│   │   ├── 007_🧪_execute_auth_test_cases.md
│   │   └── 008_🧪_perform_uat_session_1.md
│   │
│   ├── 05_Deployment/          # 🚀 Phase 5: RELEASE the system
│   │   ├── _phase_overview.md
│   │   └── 009_🚀_prepare_production_environment.md
│   │
│   └── AREA_ChangeRequests/    # 🔁 Optional: Track approved changes post-baseline
│       └── CR_001_update_reporting_feature.md
│
├── archive/                  # 📦 Optional: Completed tasks mirror phase structure
│   └── ...
└── README.md
```

**Key Structural Rules:**
*   ✅ **Numbered Phase Folders:** Use `NN_PhaseName` (e.g., `01_Requirements`) for clear sequence.
*   ✅ **Central `docs/`:** Store primary Waterfall artifacts (SRS, SDD, etc.) here. Number them for clarity.
*   ✅ **Phase Overviews (`_phase_overview.md`):** Optional file in each phase folder summarizing goals, inputs, outputs, and linking to the main phase document in `docs/`.
*   ✅ **Templates (`_templates/`):** Optional templates tailored to the typical work in each phase.
*   ✅ **Change Requests (`AREA_ChangeRequests/`):** Optional area for tracking formal changes impacting baselined requirements/design.

## 3. 📄 Task File Naming Conventions

Use a consistent format linking files visually to their phase.

**Format:** `NNN_🌀_short_description.md`

*   **`NNN`:** Sequence number (`001`, `002`, etc.). Project-wide numbering is often easiest for unique IDs.
*   **`_🌀_`:** Emoji for the task's **Phase** (see Phase Emojis below), enclosed in underscores.
*   **`short_description`:** Brief, lowercase, underscore-separated task name.
*   **`.md`:** Markdown extension.

**Phase Emojis (`🌀`):**
*   `🎯` : Requirements
*   `📐` : Design
*   `⚙️` : Implementation
*   `🧪` : Testing
*   `🚀` : Deployment
*   `🔁` : Change Request (if used)

**Examples:**
*   `001_🎯_gather_stakeholder_needs.md`
*   `003_📐_design_database_schema.md`
*   `005_⚙️_build_user_auth_module.md`

## 4. ⚙️ YAML Front Matter: Defining Phase Tasks

Structure task metadata with fields relevant to Waterfall.

```yaml
---
# 🆔 Task Identification & Core Metadata
id:             # REQUIRED. Unique ID (e.g., REQ-001, DES-003). Convention: {PHASE_ABBR}-{NNN}
title:          # REQUIRED. Human-readable title. "Finalize SRS Section 3 (Functional Requirements)"
phase:          # REQUIRED. Waterfall phase name. "🎯 Requirements"
status:         # REQUIRED. Status *within this phase*. "🟡 To Do", "🔵 In Progress", "🟢 Done (Phase)"
type:           # REQUIRED. Type of work within phase. "📝 Definition", "📐 Design Element", "🧪 Test Execution"

# 🔗 Relationships & Context (CRITICAL)
requirement_ref: # REQUIRED (for tasks in/after Req phase). Link(s) to SRS section(s). ["docs/01_Requirements_SRS.md#section-3"]
design_ref:     # REQUIRED (for tasks in/after Design phase). Link(s) to SDD section(s). ["docs/02_Design_SDD.md#arch-diagram"]
test_case_ref:  # REQUIRED (for tasks in/after Test Plan phase). Link(s) to Test Plan section(s). ["docs/03_Test_Plan.md#tc-auth-01"]
# Note: A task might *produce* a section (e.g., a Req task creates SRS section 3), or *consume* one (e.g., an Impl task uses SDD section 4).

# ⏳ Scheduling & Effort (Often less granular in Waterfall)
created_date:   # Recommended. "YYYY-MM-DD"
updated_date:   # Recommended. "YYYY-MM-DD"
# due_date, estimated_effort: Often managed at the overall phase/project level.

# 🧑‍💻 Assignment & Approval
assigned_to:    # Optional. "🧑‍💻 User:AnalystBob", "👥 Team:Dev"
approved_by:    # Optional. Formal sign-off for this task's output. "🧑‍⚖️ Manager:Jane"

# 🔁 Change Request Link
related_cr:     # Optional. Link to Change Request file if this addresses it. "AREA_ChangeRequests/CR_001..."

# 🏷️ Tags
tags:           # Optional. Keywords (e.g., ["authentication", "database"]).
---

# Title Matching YAML Title (Optional)

## Description ✍️
... Markdown Body: Task details within the phase context ...
```

**Key YAML Fields for Waterfall:**
*   `phase:`: Explicitly state the phase.
*   `status:`: Reflects progress *within* the current phase only (e.g., "🟢 Done (Phase)").
*   `requirement_ref`, `design_ref`, `test_case_ref`: **Absolutely critical** for linking tasks to the authoritative documents in `docs/`.

## 5. 🏷️ Standardized Field Values

Use consistent terminology.

*   **Phases (`phase:`):** `🎯 Requirements`, `📐 Design`, `⚙️ Implementation`, `🧪 Testing`, `🚀 Deployment`, `🔁 Change Request`.
*   **Status (`status:`):** `🟡 To Do`, `🔵 In Progress`, `🟣 Review/Approval`, `🟢 Done (Phase)`, `⚪ Blocked`.
*   **Types (`type:`):** Tailor to phase activities:
    *   Requirements: `📝 Definition`, `📊 Analysis`, `🗣️ Interview`, `🤝 Workshop`
    *   Design: `📐 Design Element`, `🖼️ Mockup Creation`, `📈 Diagramming`, `🔩 Prototyping`
    *   Implementation: `⚙️ Implementation Unit`, `🛠️ Integration`, `🐞 Bug Fix`
    *   Testing: `🧪 Test Case Execution`, `📊 Report Generation`, `🐛 Defect Logging`
    *   Deployment: `🚀 Preparation`, `🚢 Release Activity`, `✅ Post-Release Check`

## 6. 📝 Markdown Body: Detailing Phase Work

Structure the body to provide context for the specific phase task.

```markdown
# << Task Title >>

## Description ✍️
Briefly explain the objective of *this specific task* within its phase. Always refer back to the main documents in `docs/` for the comprehensive details.
*Example (Design Task):* "Create the detailed sequence diagram for the user login process as specified in [SRS §3.1](docs/01_Requirements_SRS.md#section-3.1)."

## Inputs / Prerequisites 📥
List the specific documents, sections, or outputs from previous tasks/phases needed to perform this task.
*   *Example:* "Approved [SRS §3.1](docs/01_Requirements_SRS.md#section-3.1)", "Overall [Architecture Diagram](docs/02_Design_SDD.md#arch-diagram)".

## Tasks / Checklist ✅
Break down the specific steps required to complete *this task* within this phase. Use Markdown checklists (`- [ ]`).
*   *Example (Design Task):*
    *   - [ ] Review relevant SRS section.
    *   - [ ] Draft sequence diagram using Mermaid/tool.
    *   - [ ] Add diagram to [SDD §4.5](docs/02_Design_SDD.md#seq-login).
    *   - [ ] Submit SDD section for review.
    *   - [ ] Incorporate review feedback.

## Outputs / Deliverables 📤
Specify what this task produces or updates.
*   *Example:* "Updated [SDD §4.5](docs/02_Design_SDD.md#seq-login)", "Sequence diagram file `docs/diagrams/login_sequence.png`".

## References 🔗
Direct links to the most relevant sections in the primary `docs/` files.
*   *Example:* `[SRS §3.1](docs/01_Requirements_SRS.md#section-3.1)`
```

## 7. 📄 Example Template (`tasks/_templates/📐_design_task.md`)

```markdown
---
# 🆔 Task Identification & Core Metadata
id:             # << GENERATE_UNIQUE_ID (e.g., DES-NNN) >>
title:          # << DESIGN: Concise description >>
phase:          "📐 Design"
status:         "🟡 To Do"
type:           "📐 Design Element" # Or Diagramming, Prototyping, etc.

# 🔗 Relationships & Context
requirement_ref: # << REQUIRED: Link to relevant SRS section(s) >>
# design_ref:     # Optional: Link if refining previous design element
# test_case_ref:  # Optional: Link to test cases this enables

# ⏳ Scheduling & Effort
created_date:   # << YYYY-MM-DD >>
updated_date:   # << YYYY-MM-DD >>

# 🧑‍💻 Assignment & Approval
assigned_to:    # Optional
approved_by:    # Optional

# 🏷️ Tags
tags:           []

# 🔁 Change Request Link
related_cr:     # Optional
---

# << DESIGN: Concise description >>

## Description ✍️
Develop the design element specified below, based on the referenced requirements. Ensure alignment with the overall architecture.

## Inputs / Prerequisites 📥
*   Requirement(s): See `requirement_ref` link(s) above.
*   Overall Architecture Document: `docs/02_Design_SDD.md#architecture` (Example)
*   UI Style Guide: `docs/UI_StyleGuide.md` (Example, if applicable)

## Tasks / Checklist ✅
*   - [ ] Review input requirements and architecture.
*   - [ ] Draft the design element (e.g., diagram, schema definition, mockup).
*   - [ ] Document the design element in the appropriate SDD section.
*   - [ ] Conduct peer review of the design element.
*   - [ ] Submit for formal approval (if required).
*   - [ ] Incorporate feedback.

## Outputs / Deliverables 📤
*   Updated SDD Section(s): [Link to section, e.g., `docs/02_Design_SDD.md#section-X.Y`]
*   Design artifact file(s): [Link to diagrams, mockups, etc.]

## References 🔗
*   `[SRS §X.Y](docs/01_Requirements_SRS.md#req-X.Y)`
```

*(Create similar templates for Requirements, Implementation, Testing phases, tailoring the Inputs, Tasks, and Outputs sections).*

## 8. ➡️ Managing the Waterfall Flow

*   **Focus Within Phase:** Use the `status:` field to track progress of individual tasks *within their designated phase folder*.
*   **Phase Gate Review (Manual Process):** This is the critical control point in Waterfall, managed **outside** MDTM. The Project Manager or team lead convenes a formal review at the end of each phase (e.g., Design Review).
    *   **Criteria:** Ensure all tasks in the current phase folder are `🟢 Done (Phase)` and their deliverables (often updates to `docs/` files) are formally approved.
    *   **Decision:** Explicit approval is required before the team starts significant work on tasks in the *next* phase folder.
*   **Document Baselining:** Once a phase's primary document (e.g., `docs/01_Requirements_SRS.md`) is approved at a phase gate, it becomes a "baseline".
*   **Change Management:** If changes to a baseline are needed later, use the formal Change Request process. Approved CRs might generate tasks in the `AREA_ChangeRequests/` folder or require modifying existing tasks (potentially reverting their status and linking them to the CR via `related_cr:`).

## 9. ✅ Conclusion: Structured Tracking for Sequential Work

Implementing Waterfall using MDTM provides a repository-integrated way to track phase-specific tasks. By leveraging **phase-based folders**, clear **task file naming**, detailed **YAML metadata** (especially `phase:` and `*_ref` links), and **structured Markdown bodies**, teams can manage sequential work in a transparent, version-controlled manner.

Success depends on **strict adherence to the Waterfall process** (especially phase gates and change control) managed by the team, combined with **consistent use** of these MDTM conventions.