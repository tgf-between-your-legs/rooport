# Plan: Mode-Specific Context File Creation (`.roo/context/`)

## 1. Goal

To systematically create and populate the mode-specific context files (within `.roo/context/{mode-slug}/`) that were identified as potentially beneficial or expected by various modes during the path assessment phase. This will enhance mode capabilities by providing them with tailored knowledge bases, templates, and examples.

## 2. Background

The search for `.roo/context/` references revealed numerous potential files across different modes. These files are intended to hold mode-specific knowledge (e.g., best practices, API references, common patterns, templates) rather than general project context. Creating these files will make the modes more effective and consistent.

## 3. Identified Context Needs (Summary from Search)

*(Note: This is a summary; the full list is extensive. Refer to the `search_files` output from 2025-04-14 ~00:36 for complete details if needed.)*

*   **General:** Templates (ADR, common questions, responses), Best Practices, Style Guides, Checklists.
*   **Framework/Tech Specific:** API References, SDK Guides, Common Patterns, Code Examples, Security Rules, Data Modeling Guides, CLI Commands, Testing Strategies, Migration Guides, Optimization Guides (e.g., for Firebase, Supabase, FastAPI, Flask, Laravel, Django, React, Angular, Vue, Next.js, Remix, SvelteKit, Clerk, Tailwind, Bootstrap, MUI, Ant Design, D3, Three.js, WordPress, Frappe, Directus, dbt, Elasticsearch, MongoDB, Neon DB, MySQL, Cloudflare Workers, Docker Compose, Terraform, AWS, Azure, GCP, OpenAI, Hugging Face, Crawl4AI).
*   **Role Specific:**
    *   `architect`: ADR templates.
    *   `discovery-agent`: Tech indicators, requirements templates, question banks.
    *   `file-repair`: Corruption patterns, file format refs, encoding refs.
    *   `design-lead`: Design system docs, style guides.
    *   `qa-lead`: Test strategy templates, bug report templates, metrics refs.
    *   `api-developer`: REST/GraphQL best practices, security checklists, OpenAPI templates.
    *   `e2e-tester`: Best practices, selector strategies, framework refs, test data management, POM examples, flaky test solutions.
    *   `integration-tester`: Test patterns, framework guides, mock strategies, contract testing info.
    *   `cicd-specialist`: Pipeline templates (GitHub Actions, GitLab, Jenkins, Azure DevOps), deployment strategies, security scanning integration, optimization guides.
    *   `complex-problem-solver`: Problem-solving frameworks, analysis templates, common root causes.
    *   `performance-optimizer`: Benchmarking templates, optimization patterns.
    *   `git-manager`: Command reference, conflict resolution strategies, repo structure patterns.
    *   `mode-maintainer`: Standard mode file templates.
    *   `technical-writer`: Doc templates, style guides, best practices.
    *   `diagramer`: Diagram templates, syntax refs, style guides, examples.
    *   `code-reviewer`: Checklists, anti-patterns, review templates, project standards.
    *   `security-specialist`: Standards refs (OWASP, CWE), vulnerability patterns, tool docs, secure coding patterns, threat model templates.
    *   `product-manager`: Vision/strategy docs, market research, metrics, user feedback, requirements templates, roadmap examples.
    *   `ui-designer`: Design patterns, accessibility guides, responsive principles, style guide templates.
    *   `one-shot-web-designer`: Design patterns, color palettes, typography guides, HTML/CSS templates, inspiration links, style guide examples.

## 4. Creation Strategy & Plan

Creating all these files manually is a large undertaking. We should prioritize and use a phased approach, potentially leveraging specialist modes.

**Phase 1: Foundational Templates & Guides**
*   **Goal:** Create core templates and guides referenced by multiple modes or essential for core workflows.
*   **Files to Create (Examples - Prioritize based on frequency/impact):**
    *   `.templates/mode_template.md` (Ensure this is up-to-date)
    *   `.docs/standards/mdtm_standard.md` (Ensure this exists and is referenced correctly)
    *   `.roo/context/technical-writer/templates/readme_template.md`
    *   `.roo/context/technical-architect/templates/adr_template.md` (or similar central location)
    *   `.roo/context/project-manager/mdtm_templates/task_template.md`
    *   `.roo/context/code-reviewer/review-checklists/general.md`
    *   `.roo/context/security-specialist/standards/owasp_top_10.md`
*   **Method:**
    *   Delegate creation of specific templates/guides to `technical-writer` via MDTM tasks.
    *   Provide clear instructions on the expected content and structure for each file.

**Phase 2: High-Impact Specialist Knowledge**
*   **Goal:** Populate context for frequently used or critical specialist modes.
*   **Files to Create (Examples - Prioritize based on project needs):**
    *   `.roo/context/react-specialist/common-patterns.md`
    *   `.roo/context/api-developer/rest-best-practices.md`
    *   `.roo/context/git-manager/git-commands.md`
    *   `.roo/context/bug-fixer/common-patterns.md`
    *   `.roo/context/security-specialist/secure-coding/general.md`
*   **Method:**
    *   Delegate research and content creation to `research-context-builder` or `technical-writer`.
    *   For highly technical content (e.g., framework patterns), consider having the relevant specialist mode (e.g., `react-specialist`) generate initial content, followed by review/refinement by `technical-writer`.

**Phase 3: Broader Context Population (Ongoing)**
*   **Goal:** Gradually populate the remaining identified context files as needed or as capacity allows.
*   **Method:**
    *   Create placeholder files (`touch .roo/context/{mode-slug}/filename.md`) for expected files to make them discoverable.
    *   Prioritize based on user requests or observed needs during project work.
    *   Continue using `research-context-builder`, `technical-writer`, and relevant specialists for content generation.

## 5. Tracking

*   Use this plan (`.planning/context_file_creation_plan.md`) to track overall progress.
*   Create individual MDTM tasks in `.tasks/` for each file or group of related files being created in Phases 1 and 2. Assign these tasks appropriately.

## 6. Future Considerations

*   **Cleanup/Archival:** Define a process for archiving or deleting outdated tasks, logs, reports, etc., potentially managed by `project-manager`.
*   **Context Maintenance:** Establish a process for reviewing and updating context files periodically, possibly involving `technical-writer` or relevant specialists.

This plan provides a roadmap for building out the valuable mode-specific knowledge bases suggested during mode creation.