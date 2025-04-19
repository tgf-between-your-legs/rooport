# 6. Context / Knowledge Base (Optional)

*   Official dbt Documentation: https://docs.getdbt.com/
*   dbt Learn: https://learn.getdbt.com/
*   SQL language proficiency (specific to the target data warehouse - Snowflake, BigQuery, Redshift, Postgres, etc.).
*   Jinja templating language basics.
*   Data modeling concepts (dimensional modeling, normalization/denormalization).
*   Data warehousing concepts.
*   Python (if using dbt Python models).
*   Project's `dbt_project.yml`, `profiles.yml`, and existing models/tests.
*   **Condensed Context Index (dbt):**
    *   Source: `.context/dbt-specialist/dbt-specialist-llms-context.md` (if available)

    **Key Concepts Reminder:**
    *   Data transformation tool (T in ELT). Uses SQL (primarily) and Python.
    *   **Project:** `dbt_project.yml` (config), `profiles.yml` (connections - KEEP SECRET).
    *   **Models:** `.sql` or `.py` files in `models/` directory. Define transformations. Use `{{ ref('model_name') }}` and `{{ source('source_name', 'table_name') }}`.
    *   **Sources:** Define raw data inputs in `sources.yml`.
    *   **Materializations:** How models are built in the warehouse (`view`, `table`, `incremental`, `ephemeral`). Configured in `dbt_project.yml` or model config block.
    *   **Tests:** Data quality checks defined in `schema.yml` (generic: `unique`, `not_null`, `relationships`, `accepted_values`) or as custom SQL queries (`tests/*.sql` returning 0 rows for success).
    *   **Documentation:** Descriptions added to models, columns, sources in YAML files. Generated via `dbt docs generate`, served via `dbt docs serve`.
    *   **Jinja:** Used for templating SQL (refs, sources, configs, macros).
    *   **Macros:** Reusable Jinja/SQL code snippets (`macros/*.sql`).
    *   **CLI:** `dbt run`, `dbt test`, `dbt build`, `dbt seed`, `dbt docs generate`, `dbt compile`. Selectors (`--select`, `--exclude`, tags).
    *   **Python Models:** Use Python (e.g., Pandas, Snowpark) for transformations where SQL is difficult. Return DataFrames.
    *   **Exposures, Metrics, Semantic Models:** Define downstream uses, key business metrics, and semantic layers in YAML.