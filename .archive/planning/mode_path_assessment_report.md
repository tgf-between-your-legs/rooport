# Mode Path Assessment Report

This report maps references to old (`project_journal/`, `v7.0/...`) or potentially intended paths found within `v7.0/**/*.mode.md` files to the new proposed hidden folder structure.

**Legend:**
*   **Old Path:** Path explicitly found in the mode file.
*   **Intended Path:** Path inferred from context (e.g., `knowledge/file.md` likely meant `project_journal/knowledge/file.md`).
*   **New Path:** The corresponding path in the proposed structure (e.g., `.tasks/`, `.docs/`).
*   **Notes:** Clarifications on mapping decisions or context.

| Mode File Path | Referenced Path (Old/Intended) | Context/Intent | Proposed New Path | Notes |
|---|---|---|---|---|
| `.../architect/050-footgun-architect.mode.md` | `project_journal/decisions/` | Documenting ADRs | `.decisions/` | Standard ADR location |
| `.../architect/050-footgun-architect.mode.md` | `project_journal/planning/architecture.md` | Documenting architecture | `.docs/architecture.md` | Core architecture doc |
| `.../ask/050-footgun-ask.mode.md` | `project_journal/` | General reference | (N/A - General context) | Mode should use specific paths |
| `.../firecrawl-specialist/040-asst-firecrawl-specialist.mode.md` | `project_journal/context/source_docs/firecrawl-specialist-llms-context.md` | Reading source context | `.context/source_docs/firecrawl-specialist-llms-context.md` | Standard context source |
| `.../discovery-agent/040-asst-discovery-agent.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../discovery-agent/040-asst-discovery-agent.mode.md` | `project_journal/discovery/[TaskID]_discovery_report.md` | Saving discovery report | `.reports/discovery/[TaskID]_discovery_report.md` | Discovery output report |
| `.../file-repair-specialist/040-asst-file-repair-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../file-repair-specialist/040-asst-file-repair-specialist.mode.md` | `project_journal/` | Path safety check | (N/A - Check logic) | Logic needs update for `.tasks/`, `.logs/` etc. |
| `.../design-lead/020-lead-ds-design-lead.mode.md` | `project_journal/tasks/TASK-DS-... .md` | Creating/Tracking MDTM task | `.tasks/TASK-DS-... .md` | Standard MDTM task log |
| `.../design-lead/020-lead-ds-design-lead.mode.md` | `project_journal` | General reference | (N/A - General context) | Mode should use specific paths |
| `.../design-lead/020-lead-ds-design-lead.mode.md` | `v7.0/templates/mode_hierarchy.md` | Reading mode hierarchy | `.templates/mode_hierarchy.md` | Standard template location |
| `.../design-lead/020-lead-ds-design-lead.mode.md` | `v7.0/templates/mode_folder_structure.md` | Reading mode structure | `.templates/mode_folder_structure.md` | Standard template location |
| `.../database-lead/020-lead-db-database-lead.mode.md` | `v7.0/templates/mode_hierarchy.md` | Reading mode hierarchy | `.templates/mode_hierarchy.md` | Standard template location |
| `.../database-lead/020-lead-db-database-lead.mode.md` | `v7.0/templates/mode_folder_structure.md` | Reading mode structure | `.templates/mode_folder_structure.md` | Standard template location |
| `.../aws-architect/020-lead-do-aws-architect.mode.md` | `v7.0/templates/mode_hierarchy.md` | Reading mode hierarchy | `.templates/mode_hierarchy.md` | Standard template location |
| `.../aws-architect/020-lead-do-aws-architect.mode.md` | `v7.0/templates/mode_folder_structure.md` | Reading mode structure | `.templates/mode_folder_structure.md` | Standard template location |
| `.../backend-lead/020-lead-be-backend-lead.mode.md` | `v7.0/templates/mode_hierarchy.md` | Reading mode hierarchy | `.templates/mode_hierarchy.md` | Standard template location |
| `.../backend-lead/020-lead-be-backend-lead.mode.md` | `v7.0/templates/mode_folder_structure.md` | Reading mode structure | `.templates/mode_folder_structure.md` | Standard template location |
| `.../frappe-specialist/032-work-be-frappe-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../frappe-specialist/032-work-be-frappe-specialist.mode.md` | `project_journal/context/source_docs/frappe-specialist-llms-context.md` | Reading source context | `.context/source_docs/frappe-specialist-llms-context.md` | Standard context source |
| `.../firebase-developer/032-work-be-firebase-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../firebase-developer/032-work-be-firebase-developer.mode.md` | `project_journal/context/source_docs/firebase-developer-llms-context.md` | Reading source context | `.context/source_docs/firebase-developer-llms-context.md` | Standard context source |
| `.../firebase-developer/032-work-be-firebase-developer.mode.md` | `project_journal/context/condensed_indices/firebase-developer-condensed-index.md` | Reading condensed index | `.context/condensed_indices/firebase-developer-condensed-index.md` | Standard context index |
| `.../directus-specialist/032-work-be-directus-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../context-condenser/040-asst-context-condenser.mode.md` | `project_journal/context/condensed_indices/...` | Saving condensed index | `.context/condensed_indices/...` | Standard context index |
| `.../context-condenser/040-asst-context-condenser.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../context-condenser/040-asst-context-condenser.mode.md` | `project_journal/context/temp_source/` | Downloading source files | `.context/temp_source/` | Temporary download location |
| `.../api-developer/032-work-be-api-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../fastapi-developer/032-work-be-fastapi-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../fastapi-developer/032-work-be-fastapi-developer.mode.md` | `project_journal/context/source_docs/fastapi-developer-llms-context.md` | Reading source context | `.context/source_docs/fastapi-developer-llms-context.md` | Standard context source |
| `.../fastapi-developer/032-work-be-fastapi-developer.mode.md` | `project_journal/context/condensed_indices/fastapi-developer-condensed-index.md` | Reading condensed index | `.context/condensed_indices/fastapi-developer-condensed-index.md` | Standard context index |
| `.../flask-developer/032-work-be-flask-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../flask-developer/032-work-be-flask-developer.mode.md` | `project_journal/context/source_docs/flask-developer-llms-context.md` | Reading source context | `.context/source_docs/flask-developer-llms-context.md` | Standard context source |
| `.../flask-developer/032-work-be-flask-developer.mode.md` | `project_journal/context/condensed_indices/flask-developer-condensed-index.md` | Reading condensed index | `.context/condensed_indices/flask-developer-condensed-index.md` | Standard context index |
| `.../php-laravel-developer/032-work-be-php-laravel-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../php-laravel-developer/032-work-be-php-laravel-developer.mode.md` | `project_journal/context/source_docs/php-laravel-developer-llms-context.md` | Reading source context | `.context/source_docs/php-laravel-developer-llms-context.md` | Standard context source |
| `.../php-laravel-developer/032-work-be-php-laravel-developer.mode.md` | `project_journal/context/condensed_indices/php-laravel-developer-condensed-index.md` | Reading condensed index | `.context/condensed_indices/php-laravel-developer-condensed-index.md` | Standard context index |
| `.../e2e-tester/034-work-qa-e2e-tester.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../wordpress-specialist/032-work-be-wordpress-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../wordpress-specialist/032-work-be-wordpress-specialist.mode.md` | `project_journal/context/source_docs/wordpress-specialist-llms-context.md` | Reading source context | `.context/source_docs/wordpress-specialist-llms-context.md` | Standard context source |
| `.../django-developer/032-work-be-django-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../django-developer/032-work-be-django-developer.mode.md` | `project_journal/context/source_docs/django-developer-llms-context.md` | Reading source context | `.context/source_docs/django-developer-llms-context.md` | Standard context source |
| `.../django-developer/032-work-be-django-developer.mode.md` | `project_journal/context/condensed_indices/django-developer-condensed-index.md` | Reading condensed index | `.context/condensed_indices/django-developer-condensed-index.md` | Standard context index |
| `.../openai-specialist/037-work-aiml-openai-specialist.mode.md` | `v7.0/templates/mode_hierarchy.md` | Reading mode hierarchy | `.templates/mode_hierarchy.md` | Standard template location |
| `.../openai-specialist/037-work-aiml-openai-specialist.mode.md` | `v7.0/templates/mode_folder_structure.md` | Reading mode structure | `.templates/mode_folder_structure.md` | Standard template location |
| `.../supabase-developer/032-work-be-supabase-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../supabase-developer/032-work-be-supabase-developer.mode.md` | `project_journal/context/source_docs/supabase-developer-llms-context.md` | Reading source context | `.context/source_docs/supabase-developer-llms-context.md` | Standard context source |
| `.../dbt-specialist/033-work-db-dbt-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../dbt-specialist/033-work-db-dbt-specialist.mode.md` | `project_journal/context/source_docs/dbt-specialist-llms-context.md` | Reading source context | `.context/source_docs/dbt-specialist-llms-context.md` | Standard context source |
| `.../cloudflare-workers-specialist/035-work-do-cloudflare-workers-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../cloudflare-workers-specialist/035-work-do-cloudflare-workers-specialist.mode.md` | `project_journal/context/source_docs/cloudflare-workers-specialist-llms-context.md` | Reading source context | `.context/source_docs/cloudflare-workers-specialist-llms-context.md` | Standard context source |
| `.../integration-tester/034-work-qa-integration-tester.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../integration-tester/034-work-qa-integration-tester.mode.md` | `project_journal/formal_docs/integration_report_...` | Saving integration report | `.reports/integration/integration_report_...` | Test report output |
| `.../project-onboarding/010-dir-project-onboarding.mode.md` | `project_journal/planning/stack_profile.md` | Saving stack profile | `.context/stack_profile.md` | Discovery output |
| `.../project-onboarding/010-dir-project-onboarding.mode.md` | `project_journal/planning/requirements.md` | Saving requirements | `.docs/requirements.md` | Core project document |
| `.../project-onboarding/010-dir-project-onboarding.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../project-onboarding/010-dir-project-onboarding.mode.md` | `project_journal/tasks` | Creating directory | `.tasks/` | Standard MDTM task location |
| `.../project-onboarding/010-dir-project-onboarding.mode.md` | `project_journal/decisions` | Creating directory | `.decisions/` | Standard ADR location |
| `.../project-onboarding/010-dir-project-onboarding.mode.md` | `project_journal/formal_docs` | Creating directory | `.docs/` or `.reports/` | Needs refinement based on content |
| `.../project-onboarding/010-dir-project-onboarding.mode.md` | `project_journal/visualizations` | Creating directory | `.docs/diagrams/` | Standard diagram location |
| `.../project-onboarding/010-dir-project-onboarding.mode.md` | `project_journal/planning` | Creating directory | `.planning/` | Standard planning location |
| `.../project-onboarding/010-dir-project-onboarding.mode.md` | `project_journal/technical_notes` | Creating directory | `.docs/technical_notes/` or `.context/technical_notes/` | Map to docs or context |
| `.../project-onboarding/010-dir-project-onboarding.mode.md` | `project_journal/` | Checking existence | (N/A - Check logic) | Logic needs update |
| `.../docker-compose-specialist/035-work-do-docker-compose-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../docker-compose-specialist/035-work-do-docker-compose-specialist.mode.md` | `project_journal/formal_docs/...` | Saving formal docs | `.docs/...` or `.reports/...` | Map based on content |
| `.../infrastructure-specialist/035-work-do-infrastructure-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../infrastructure-specialist/035-work-do-infrastructure-specialist.mode.md` | `project_journal/formal_docs/...` | Saving formal docs | `.docs/...` or `.reports/...` | Map based on content |
| `.../neon-db-specialist/033-work-db-neon-db-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../neon-db-specialist/033-work-db-neon-db-specialist.mode.md` | `project_journal/context/source_docs/neon-db-specialist-llms-context.md` | Reading source context | `.context/source_docs/neon-db-specialist-llms-context.md` | Standard context source |
| `.../neon-db-specialist/033-work-db-neon-db-specialist.mode.md` | `project_journal/context/condensed_indices/neon-db-specialist-condensed-index.md` | Reading condensed index | `.context/condensed_indices/neon-db-specialist-condensed-index.md` | Standard context index |
| `.../mongodb-specialist/033-work-db-mongodb-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../mongodb-specialist/033-work-db-mongodb-specialist.mode.md` | `project_journal/context/source_docs/mongodb-specialist-llms-context.md` | Reading source context | `.context/source_docs/mongodb-specialist-llms-context.md` | Standard context source |
| `.../mongodb-specialist/033-work-db-mongodb-specialist.mode.md` | `project_journal/context/condensed_indices/mongodb-specialist-condensed-index.md` | Reading condensed index | `.context/condensed_indices/mongodb-specialist-condensed-index.md` | Standard context index |
| `.../context-resolver/040-asst-context-resolver.mode.md` | `project_journal/` | General reference | (N/A - General context) | Mode should use specific paths |
| `.../context-resolver/040-asst-context-resolver.mode.md` | `project_journal/tasks/` | Reading task logs | `.tasks/` | Standard MDTM task location |
| `.../context-resolver/040-asst-context-resolver.mode.md` | `project_journal/decisions/` | Reading decisions | `.decisions/` | Standard ADR location |
| `.../context-resolver/040-asst-context-resolver.mode.md` | `project_journal/planning/` | Reading planning docs | `.planning/` or `.docs/` | Map based on specific file |
| `.../context-resolver/040-asst-context-resolver.mode.md` | `project_journal/planning/requirements.md` | Reading requirements | `.docs/requirements.md` | Core project document |
| `.../context-resolver/040-asst-context-resolver.mode.md` | `project_journal/planning/architecture.md` | Reading architecture | `.docs/architecture.md` | Core architecture doc |
| `.../context-resolver/040-asst-context-resolver.mode.md` | `project_journal/planning/project_plan.md` | Reading project plan | `.planning/project_plan.md` | Core planning doc |
| `.../context-resolver/040-asst-context-resolver.mode.md` | `project_journal/planning/team_structure.md` | Reading team structure | `.planning/team_structure.md` or `.docs/team_structure.md` | Map to planning or docs |
| `.../elasticsearch-specialist/033-work-db-elasticsearch-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../elasticsearch-specialist/033-work-db-elasticsearch-specialist.mode.md` | `project_journal/context/source_docs/elasticsearch-specialist-llms-context.md` | Reading source context | `.context/source_docs/elasticsearch-specialist-llms-context.md` | Standard context source |
| `.../elasticsearch-specialist/033-work-db-elasticsearch-specialist.mode.md` | `project_journal/context/condensed_indices/elasticsearch-specialist-condensed-index.md` | Reading condensed index | `.context/condensed_indices/elasticsearch-specialist-condensed-index.md` | Standard context index |
| `.../cicd-specialist/035-work-do-cicd-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../cicd-specialist/035-work-do-cicd-specialist.mode.md` | `project_journal/formal_docs/...` | Saving formal docs | `.docs/...` or `.reports/...` | Map based on content |
| `.../qa-lead/020-lead-qa-qa-lead.mode.md` | `v7.0/templates/mode_hierarchy.md` | Reading mode hierarchy | `.templates/mode_hierarchy.md` | Standard template location |
| `.../qa-lead/020-lead-qa-qa-lead.mode.md` | `v7.0/templates/mode_folder_structure.md` | Reading mode structure | `.templates/mode_folder_structure.md` | Standard template location |
| `.../research-context-builder/040-asst-research-context-builder.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../research-context-builder/040-asst-research-context-builder.mode.md` | `project_journal/research/...` | Saving research summary | `.reports/research/...` or `.docs/knowledge/research/...` | Map to reports or docs |
| `.../diagramer/030-work-des-diagramer.mode.md` | `project_journal/visualizations/*.md` | Saving diagrams | `.docs/diagrams/*.md` | Standard diagram location |
| `.../database-specialist/033-work-db-database-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../database-specialist/033-work-db-database-specialist.mode.md` | `project_journal/formal_docs/...` | Saving formal docs | `.docs/...` or `.reports/...` | Map based on content |
| `.../database-specialist/033-work-db-database-specialist.mode.md` | `project_journal/visualizations/database_schema.md` | Delegating diagram update | `.docs/diagrams/database_schema.md` | Standard diagram location |
| `.../shadcn-ui-specialist/031-work-fe-shadcn-ui-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../shadcn-ui-specialist/031-work-fe-shadcn-ui-specialist.mode.md` | `project_journal/context/source_docs/shadcn-ui-specialist-llms-context.md` | Reading source context | `.context/source_docs/shadcn-ui-specialist-llms-context.md` | Standard context source |
| `.../shadcn-ui-specialist/031-work-fe-shadcn-ui-specialist.mode.md` | `project_journal/context/condensed_indices/shadcn-ui-specialist-condensed-index.md` | Reading condensed index | `.context/condensed_indices/shadcn-ui-specialist-condensed-index.md` | Standard context index |
| `.../complex-problem-solver/039-work-xf-complex-problem-solver.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../complex-problem-solver/039-work-xf-complex-problem-solver.mode.md` | `project_journal/analysis_reports/...` | Saving analysis report | `.reports/analysis/...` | Analysis output report |
| `.../performance-optimizer/039-work-xf-performance-optimizer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../performance-optimizer/039-work-xf-performance-optimizer.mode.md` | `project_journal/formal_docs/performance_report_...` | Saving performance report | `.reports/performance/performance_report_...` | Performance output report |
| `.../jquery-specialist/031-work-fe-jquery-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../typescript-specialist/031-work-fe-typescript-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../accessibility-specialist/031-work-fe-accessibility-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../accessibility-specialist/031-work-fe-accessibility-specialist.mode.md` | `project_journal/formal_docs/a11y_report_...` | Saving accessibility report | `.reports/accessibility/a11y_report_...` | Accessibility output report |
| `.../refactor-specialist/039-work-xf-refactor-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../react-specialist/031-work-fe-react-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../react-specialist/031-work-fe-react-specialist.mode.md` | `project_journal/context/stack_profile.md` | Reading stack profile | `.context/stack_profile.md` | Discovery output |
| `.../react-specialist/031-work-fe-react-specialist.mode.md` | `project_journal/requirements/[ReqID].md` | Reading requirements | `.docs/requirements/[ReqID].md` | Core project document |
| `.../react-specialist/031-work-fe-react-specialist.mode.md` | `project_journal/context/source_docs/react-specialist-core-concepts.md` | Reading source context | `.context/source_docs/react-specialist-core-concepts.md` | Standard context source |
| `.../react-specialist/031-work-fe-react-specialist.mode.md` | `project_journal/context/condensed_indices/react-specialist-condensed-index.md` | Reading condensed index | `.context/condensed_indices/react-specialist-condensed-index.md` | Standard context index |
| `.../tailwind-specialist/031-work-fe-tailwind-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../tailwind-specialist/031-work-fe-tailwind-specialist.mode.md` | `project_journal/context/source_docs/tailwind-specialist-llms-context.md` | Reading source context | `.context/source_docs/tailwind-specialist-llms-context.md` | Standard context source |
| `.../tailwind-specialist/031-work-fe-tailwind-specialist.mode.md` | `project_journal/context/condensed_indices/tailwind-specialist-condensed-index.md` | Reading condensed index | `.context/condensed_indices/tailwind-specialist-condensed-index.md` | Standard context index |
| `.../remix-developer/031-work-fe-remix-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../remix-developer/031-work-fe-remix-developer.mode.md` | `project_journal/context/source_docs/remix-developer-llms-context.md` | Reading source context | `.context/source_docs/remix-developer-llms-context.md` | Standard context source |
| `.../remix-developer/031-work-fe-remix-developer.mode.md` | `project_journal/context/condensed_indices/remix-developer-condensed-index.md` | Reading condensed index | `.context/condensed_indices/remix-developer-condensed-index.md` | Standard context index |
| `.../security-specialist/039-work-xf-security-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../security-specialist/039-work-xf-security-specialist.mode.md` | `project_journal/security/threat_model_...` | Saving threat model | `.docs/security/threat_models/...` | Security documentation |
| `.../security-specialist/039-work-xf-security-specialist.mode.md` | `project_journal/formal_docs/security_report_...` | Saving security report | `.reports/security/security_report_...` | Security output report |
| `.../security-specialist/039-work-xf-security-specialist.mode.md` | `project_journal/knowledge/security_kb.md` | Contributing to knowledge base | `.docs/knowledge/security_kb.md` | Shared knowledge |
| `.../bootstrap-specialist/031-work-fe-bootstrap-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../bootstrap-specialist/031-work-fe-bootstrap-specialist.mode.md` | `project_journal/context/source_docs/bootstrap-specialist-llms-context.md` | Reading source context | `.context/source_docs/bootstrap-specialist-llms-context.md` | Standard context source |
| `.../bootstrap-specialist/031-work-fe-bootstrap-specialist.mode.md` | `project_journal/context/condensed_indices/bootstrap-specialist-condensed-index.md` | Reading condensed index | `.context/condensed_indices/bootstrap-specialist-condensed-index.md` | Standard context index |
| `.../angular-developer/031-work-fe-angular-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../angular-developer/031-work-fe-angular-developer.mode.md` | `project_journal/context/source_docs/angular-developer-llms-context.md` | Reading source context | `.context/source_docs/angular-developer-llms-context.md` | Standard context source |
| `.../clerk-auth-specialist/031-work-fe-clerk-auth-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../clerk-auth-specialist/031-work-fe-clerk-auth-specialist.mode.md` | `project_journal/context/source_docs/clerk-auth-specialist-llms-context.md` | Reading source context | `.context/source_docs/clerk-auth-specialist-llms-context.md` | Standard context source |
| `.../ant-design-specialist/031-work-fe-ant-design-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../astro-developer/031-work-fe-astro-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../frontend-developer/031-work-fe-frontend-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../nextjs-developer/031-work-fe-nextjs-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../nextjs-developer/031-work-fe-nextjs-developer.mode.md` | `project_journal/context/source_docs/nextjs-developer-llms-context.md` | Reading source context | `.context/source_docs/nextjs-developer-llms-context.md` | Standard context source |
| `.../nextjs-developer/031-work-fe-nextjs-developer.mode.md` | `project_journal/context/condensed_indices/nextjs-developer-condensed-index.md` | Reading condensed index | `.context/condensed_indices/nextjs-developer-condensed-index.md` | Standard context index |
| `.../mode-maintainer/039-work-xf-mode-maintainer.mode.md` | `v7.0/templates/mode_template.md` | Reading mode template | `.templates/mode_template.md` | Standard template location |
| `.../mode-maintainer/039-work-xf-mode-maintainer.mode.md` | `project_journal/tasks/` | Logging task progress | `.tasks/` | Standard MDTM task location |
| `.../junior-developer/039-work-xf-junior-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../senior-developer/039-work-xf-senior-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../technical-writer/039-work-xf-technical-writer.mode.md` | `project_journal/tasks/` | Logging task progress | `.tasks/` | Standard MDTM task location |
| `.../git-manager/039-work-xf-git-manager.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../technical-architect/010-dir-technical-architect.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../technical-architect/010-dir-technical-architect.mode.md` | `project_journal/planning/requirements.md` | Reading requirements | `.docs/requirements.md` | Core project document |
| `.../technical-architect/010-dir-technical-architect.mode.md` | `project_journal/discovery/stack_profile.md` | Reading stack profile | `.context/stack_profile.md` | Discovery output |
| `.../technical-architect/010-dir-technical-architect.mode.md` | `project_journal/decisions/...` | Creating ADRs | `.decisions/...` | Standard ADR location |
| `.../technical-architect/010-dir-technical-architect.mode.md` | `project_journal/planning/architecture.md` | Updating architecture doc | `.docs/architecture.md` | Core architecture doc |
| `.../technical-architect/010-dir-technical-architect.mode.md` | `project_journal/visualizations/` | Storing diagrams | `.docs/diagrams/` | Standard diagram location |
| `.../technical-architect/010-dir-technical-architect.mode.md` | `project_journal/planning/guidelines.md` | Documenting guidelines | `.docs/standards/guidelines.md` | Standard guidelines |
| `.../bug-fixer/039-work-xf-bug-fixer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../second-opinion/039-work-xf-second-opinion.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../second-opinion/039-work-xf-second-opinion.mode.md` | `project_journal/formal_docs/second_opinion_...` | Saving feedback report | `.reports/reviews/second_opinion_...` | Review output report |
| `.../vuejs-developer/031-work-fe-vuejs-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../product-manager/010-dir-product-manager.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../product-manager/010-dir-product-manager.mode.md` | `project_journal/planning/` | Documenting roadmap | `.planning/` | Standard planning location |
| `.../code-reviewer/039-work-xf-code-reviewer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../code-reviewer/039-work-xf-code-reviewer.mode.md` | `project_journal/...` | Reading context files | (Varies) | Map based on specific file |
| `.../code-reviewer/039-work-xf-code-reviewer.mode.md` | `project_journal/formal_docs/code_review_...` | Saving review feedback | `.reports/reviews/code_review_...` | Review output report |
| `.../roo-commander/000-exec-roo-commander.mode.md` | `project_journal/context/user_profile.md` | Saving user profile | `.context/user_profile.md` | User context |
| `.../roo-commander/000-exec-roo-commander.mode.md` | `project_journal/planning/project_plan.md` | Creating project plan | `.planning/project_plan.md` | Core planning doc |
| `.../roo-commander/000-exec-roo-commander.mode.md` | `project_journal/tasks/` | Reading task logs | `.tasks/` | Standard MDTM task location |
| `.../roo-commander/000-exec-roo-commander.mode.md` | `project_journal/decisions/` | Reading/Creating decisions | `.decisions/` | Standard ADR location |
| `.../roo-commander/000-exec-roo-commander.mode.md` | `project_journal/planning/` | Overseeing planning docs | `.planning/` | Standard planning location |
| `.../roo-commander/000-exec-roo-commander.mode.md` | `project_journal/formal_docs/` | Overseeing formal docs | `.docs/` or `.reports/` | Map based on content |
| `.../roo-commander/000-exec-roo-commander.mode.md` | `project_journal/tasks/TASK-[MODE]-... .md` | Creating MDTM task file | `.tasks/TASK-[MODE]-... .md` | Standard MDTM task log |
| `.../roo-commander/000-exec-roo-commander.mode.md` | `project_journal/tasks/TASK-CMD-... .md` | Logging commander actions | `.tasks/TASK-CMD-... .md` | Commander's task log |
| `.../roo-commander/000-exec-roo-commander.mode.md` | `project_journal/visualizations/...` | Requesting diagram updates | `.docs/diagrams/...` | Standard diagram location |
| `.../ui-designer/030-work-des-ui-designer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../ui-designer/030-work-des-ui-designer.mode.md` | `project_journal/planning/requirements.md` | Reading requirements | `.docs/requirements.md` | Core project document |
| `.../ui-designer/030-work-des-ui-designer.mode.md` | `project_journal/planning/personas.md` | Reading personas | `.docs/personas.md` | Core project document |
| `.../ui-designer/030-work-des-ui-designer.mode.md` | `project_journal/planning/journeys.md` | Reading user journeys | `.docs/user_journeys.md` | Core project document |
| `.../ui-designer/030-work-des-ui-designer.mode.md` | `project_journal/design_system/` | Reading design system | `.docs/design_system/` | Design system location |
| `.../ui-designer/030-work-des-ui-designer.mode.md` | `project_journal/discovery/stack_profile.md` | Reading stack profile | `.context/stack_profile.md` | Discovery output |
| `.../ui-designer/030-work-des-ui-designer.mode.md` | `project_journal/formal_docs/design_...` | Saving design specs | `.docs/designs/design_...` | Design documentation |
| `.../d3js-specialist/031-work-fe-d3js-specialist.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../d3js-specialist/031-work-fe-d3js-specialist.mode.md` | `project_journal/context/source_docs/d3js-specialist-llms-context.md` | Reading source context | `.context/source_docs/d3js-specialist-llms-context.md` | Standard context source |
| `.../sveltekit-developer/031-work-fe-sveltekit-developer.mode.md` | `project_journal/tasks/[TaskID].md` | Logging task progress | `.tasks/[TaskID].md` | Standard MDTM task log |
| `.../sveltekit-developer/031-work-fe-sveltekit-developer.mode.md` | `project_journal/context/source_docs/sveltekit-llms-context.md` | Reading source context | `.context/source_docs/sveltekit-llms-context.md` | Standard context source |
| `.../sveltekit-developer/031-work-fe-sveltekit-developer.mode.md` | `project_journal/context/condensed_indices/sveltekit-developer-condensed-index.md` | Reading condensed index | `.context/condensed_indices/sveltekit-developer-condensed-index.md` | Standard context index |
| `.../firebase-auth-specialist/036-work-auth-firebase-auth-specialist.mode.md` | `project_journal` | General reference | (N/A - General context) | Mode should use specific paths |
| `.../project-manager/010-dir-project-manager.mode.md` | `project_journal/tasks/` | Managing tasks | `.tasks/` | Standard MDTM task location |
| `.../project-manager/010-dir-project-manager.mode.md` | `project_journal/knowledge/project-management/...` | Reading MDTM standard | `.docs/standards/mdtm/...` | Standard documentation |
| `.../project-manager/010-dir-project-manager.mode.md` | `project_journal/planning/requirements.md` | Reading requirements | `.docs/requirements.md` | Core project document |

**Summary of Mappings:**

*   `project_journal/tasks/` -> `.tasks/`
*   `project_journal/decisions/` -> `.decisions/`
*   `project_journal/context/` -> `.context/` (Includes `source_docs`, `condensed_indices`, `temp_source`, `user_profile`, `stack_profile`)
*   `project_journal/planning/` -> `.planning/` (For plans, roadmaps) OR `.docs/` (For requirements, architecture, personas, journeys) - *Requires careful per-file mapping.*
*   `project_journal/formal_docs/` -> `.docs/` (For design specs, guidelines) OR `.reports/` (For reviews, analysis, test results) - *Requires careful per-file mapping.*
*   `project_journal/knowledge/` -> `.docs/knowledge/` or `.docs/standards/`
*   `project_journal/discovery/` -> `.context/` (Stack Profile) or `.reports/discovery/` (Discovery Report)
*   `project_journal/visualizations/` -> `.docs/diagrams/`
*   `project_journal/research/` -> `.reports/research/` or `.docs/knowledge/research/`
*   `project_journal/security/` -> `.docs/security/`
*   `project_journal/analysis_reports/` -> `.reports/analysis/`
*   `project_journal/design_system/` -> `.docs/design_system/`
*   `v7.0/context/` -> `.docs/standards/` or `.docs/guides/`
*   `v7.0/templates/` -> `.templates/`
*   `v7.0/future-planning/` -> `.planning/`

**Notes:**

*   References to `.roo/context/{mode-slug}/` were ignored for remapping as they represent mode-specific knowledge bases, not shared project artifacts.
*   Generic references to `project_journal/` need to be updated in mode logic to use specific new paths based on context.
*   The `project-onboarding` mode needs significant updates to its `mkdir` commands and file saving paths.
*   The `file-repair-specialist` safety check needs updating for the new structure.
*   Mapping for `project_journal/formal_docs/` and `project_journal/planning/` requires careful consideration of the specific file's purpose (report vs. core doc vs. plan).

This report completes Step 3.4. The next step (Step 3.5) is to use this report to create specific refactoring tasks.