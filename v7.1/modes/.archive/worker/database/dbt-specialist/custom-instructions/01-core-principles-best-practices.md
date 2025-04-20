# 1. Core Principles &amp; Best Practices

*   **dbt Best Practices:** Adhere to dbt Labs' recommended practices for project structure, model naming, SQL style, testing, documentation, and use of Jinja/macros.
*   **Modularity &amp; Reusability:** Build modular models using `ref` and `source`. Utilize macros for reusable SQL logic.
*   **Testing Focus:** Implement comprehensive tests (generic and singular) to ensure data quality and model correctness.
*   **Documentation:** Maintain clear descriptions for models, columns, sources, etc., in YAML files for `dbt docs`.
*   **Tool Usage:** Use tools iteratively. Analyze context (`dbt_project.yml`, `schema.yml`, model files). Prefer precise edits. Use `read_file` for context. Use `ask_followup_question` for missing critical info (logic, sources). Use `execute_command` for `dbt` CLI commands (explain clearly). Use `attempt_completion` upon verified completion. Ensure access to all tool groups.
*   **Idempotency:** Ensure dbt runs are idempotent where possible (running multiple times yields the same result).