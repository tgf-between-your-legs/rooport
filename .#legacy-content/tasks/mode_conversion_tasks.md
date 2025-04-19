# Task List: Convert v6.3 Mode Definitions to v7.0 Markdown

**Goal:** Track the conversion of individual v6.3 mode definitions (JSON) into the new v7.0 Markdown format.

**Status:** Pending

**Coordinator:** `roo-commander`
**Plan:** See `project_journal/planning/mode_conversion_plan.md`
**Template:** `v7.0/templates/mode_template.md`
**Target Directory:** `v7.0/modes/md/`

**Checklist:**

- [x] Convert `accessibility-specialist`
- [x] Convert `angular-developer`
- [x] Convert `animejs-specialist`
- [x] Convert `api-developer`
- [x] Convert `astro-developer`
- [x] Convert `bootstrap-specialist`
- [x] Convert `bug-fixer`
- [x] Convert `cicd-specialist`
- [x] Convert `clerk-auth-specialist`
- [x] Convert `code-reviewer`
- [x] Convert `complex-problem-solver`
- [x] Convert `containerization-developer`
- [x] Convert `context-condenser`
- [x] Convert `context-resolver`
- [x] Convert `d3js-specialist`
- [x] Convert `database-specialist`
- [x] Convert `diagramer`
- [x] Convert `discovery-agent`
- [x] Convert `django-developer`
- [x] Convert `docker-compose-specialist`
- [x] Convert `docker-expert` (Note: File exists despite initial report of missing source)
- [x] Convert `e2e-tester`
- [x] Convert `elasticsearch-specialist`
- [x] Convert `fastapi-developer`
- [x] Convert `file-repair-specialist`
- [x] Convert `firebase-developer`
- [x] Convert `flask-developer`
- [x] Convert `frontend-developer`
- [x] Convert `git-manager`
- [x] Convert `infrastructure-specialist`
- [x] Convert `integration-tester`
- [x] Convert `material-ui-specialist`
- [x] Convert `mode-maintainer`
- [x] Convert `mongodb-specialist`
- [x] Convert `neon-db-specialist`
- [x] Convert `nextjs-developer`
- [x] Convert `one-shot-web-designer`
- [x] Convert `performance-optimizer`
- [x] Convert `php-laravel-developer`
- [x] Convert `project-manager`
- [x] Convert `project-onboarding`
- [x] Convert `react-specialist` (Note: Task list had `react-developer`, using slug from mode JSON)
- [x] Convert `refactor-specialist`
- [x] Convert `remix-developer`
- [x] Convert `research-context-builder`
- [x] Convert `roo-commander`
- [x] Convert `second-opinion`
- [x] Convert `security-specialist`
- [x] Convert `shadcn-ui-specialist`
- [x] Convert `supabase-developer`
- [x] Convert `sveltekit-developer`
- [x] Convert `tailwind-specialist`
- [x] Convert `technical-architect`
- [x] Convert `technical-writer`
- [x] Convert `threejs-specialist`
- [x] Convert `typescript-specialist`
- [x] Convert `ui-designer`
- [x] Convert `vite-specialist`
- [x] Convert `vuejs-developer`

**Notes:**
*   Each task involves reading `v6.3/modes/[slug].json`, `v6.3/description-capabilities-workflow/[slug].json`, applying `v7.0/templates/mode_template.md`, and writing to `v7.0/modes/md/[slug].md`.
*   Handle potential missing files gracefully (e.g., if a slug exists in one source dir but not the other). The `react-developer` vs `react-specialist` difference needs investigation during execution.
*   Parsing `customInstructions` into template sections requires careful handling.