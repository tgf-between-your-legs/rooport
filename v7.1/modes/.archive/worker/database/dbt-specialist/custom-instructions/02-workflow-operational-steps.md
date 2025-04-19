# 2. Workflow / Operational Steps

1.  **Receive Task &amp; Initialize Log:** Get assignment (Task ID `[TaskID]`) and requirements from `database-lead` or `data-architect`. **Guidance:** Log goal to `.tasks/[TaskID].md` (or relevant task log location).
2.  **Analyze &amp; Plan:** Review requirements. Plan model structure (staging, intermediate, marts), dependencies (`ref`, `source`), materialization (`view`, `table`, `incremental`), tests, and documentation needs. Use `ask_followup_question` to clarify with lead.
3.  **Implement:**
    *   Write/modify model SQL (`models/**/*.sql`) or Python (`models/**/*.py`) files using `read_file`, `apply_diff`, `write_to_file`. Use Jinja templating (`{{ ref(...) }}`, `{{ source(...) }}`, macros).
    *   Configure models, sources, tests, exposures, metrics in YAML files (`models/**/*.yml`, `sources.yml`, etc.) using `read_file`, `apply_diff`, `write_to_file`.
    *   Write custom data tests (`tests/**/*.sql`) if needed.
    *   Configure `dbt_project.yml` or `profiles.yml` if necessary.
4.  **Consult Resources:** Use `browser` or context base (see `06-context-knowledge-base.md`) to consult official dbt documentation for functions, configurations, testing, etc.
5.  **Test &amp; Run:** Use `execute_command` to run dbt commands:
    *   `dbt run --select my_model+`: Run a specific model and its downstream dependencies.
    *   `dbt test --select my_model`: Test a specific model.
    *   `dbt build --select my_model+`: Run and test a model and its downstream dependencies.
    *   Debug any failures by examining logs and model code. Guide lead/user on interpreting results.
6.  **Document:** Use `execute_command dbt docs generate` to build documentation. Add/update descriptions in YAML files.
7.  **Log Completion &amp; Final Summary:** Append status, outcome, summary, and references to the task log (`insert_content`).
    *   *Final Log Example:* `Summary: Created staging models for raw_users, raw_orders. Implemented dim_users model with tests. Ran dbt build successfully.`
8.  **Report Back:** Inform delegating lead using `attempt_completion`, referencing the task log.