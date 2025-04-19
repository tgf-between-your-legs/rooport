# Custom Instructions: 09 - ESQL (Elasticsearch Query Language)

This instruction covers basic syntax and common commands for ESQL.

## Core Concept

ESQL (Elasticsearch Query Language) provides a pipe-based (`|`) language, similar to SQL and shell pipelines, for querying, transforming, and analyzing data within Elasticsearch. It's designed for data exploration.

**Endpoint:** `POST /_query`

**Basic Structure:**

```esql
-- Optional: Specify context index/data stream
-- FROM <index_pattern>

-- Processing commands separated by pipes
| <command> [arguments...]
| <command> [arguments...]
...
```

Or use the JSON format for the API:

```json
{
  "query": """
    FROM <index_pattern>
    | <command> ...
    | <command> ...
  """
  // Optional parameters like "filter", "params"
}
```

## Common ESQL Commands

1.  **`FROM <index_pattern>`:** Specifies the data source (index, data stream, alias). Typically the first command.
    *   **Example:** `FROM my-logs-*`

2.  **`WHERE <condition>`:** Filters rows based on a boolean condition (uses `=`, `!=`, `>`, `<`, `AND`, `OR`, `NOT`, functions like `STARTS_WITH()`, `CIDR_MATCH()`).
    *   **Example:** `| WHERE status = 'completed' AND response_time > 100`

3.  **`LIMIT <count>`:** Restricts the number of rows returned.
    *   **Example:** `| LIMIT 100`

4.  **`KEEP <field1>, <field2>, ...`:** Selects specific columns to keep (like SQL `SELECT`).
    *   **Example:** `| KEEP timestamp, user.name, message`

5.  **`DROP <field1>, <field2>, ...`:** Removes specified columns.
    *   **Example:** `| DROP user.password_hash`

6.  **`SORT <field1> [ASC|DESC], ...`:** Orders the results. `ASC` is default.
    *   **Example:** `| SORT timestamp DESC`

7.  **`EVAL <new_field> = <expression>`:** Computes a new field using expressions and functions.
    *   **Example:** `| EVAL duration_ms = duration_ns / 1000000`
    *   **Example:** `| EVAL level = CASE(status_code >= 500, 'Error', status_code >= 400, 'Warn', 'Info')`

8.  **`STATS ... BY <group_field1>, ...`:** Performs aggregations (like SQL `GROUP BY`).
    *   **Syntax:** `| STATS <agg_func>(<field>) AS <alias>, ... BY <group_field1>, ...`
    *   **Agg Functions:** `COUNT(*)`, `COUNT(<field>)`, `COUNT_DISTINCT(<field>)`, `SUM()`, `AVG()`, `MIN()`, `MAX()`, `PERCENTILE(<field>, N)`, `FIRST()`, `LAST()`.
    *   **Example:** Count events and get average response time per host.
        ```esql
        | STATS event_count = COUNT(*), avg_response = AVG(response_time) BY host.name
        ```

9.  **`ENRICH <policy_name> WITH <enrich_field> = <match_field>`:** Augments rows with data from another index based on a matching field (requires pre-configured Enrich Policies).
    *   **Example:** `| ENRICH user_info_policy WITH user.geo = user.ip`

10. **`DISSECT '<pattern>' ON <field>`:** Extracts structured fields using simple delimiter patterns.
    *   **Example:** `| DISSECT '%{client_ip} %{ident} ...' ON message`

11. **`GROK '<pattern>' ON <field>`:** Extracts structured fields using complex Grok patterns.
    *   **Example:** `| GROK '%{COMBINEDAPACHELOG}' ON message`

## Functions & Operators

ESQL supports many functions:
*   **Math:** `+`, `-`, `*`, `/`, `%`, `ABS()`, `ROUND()`, `SQRT()`, ...
*   **String:** `CONCAT()`, `SUBSTRING()`, `LENGTH()`, `LOWER()`, `UPPER()`, `TRIM()`, `STARTS_WITH()`, `ENDS_WITH()`, `CONTAINS()`, `REPLACE()`, ...
*   **Date/Time:** `NOW()`, `TODAY()`, `DATE_TRUNC()`, `INTERVAL`, ...
*   **Type Conversion:** `CAST(<field> AS <type>)`, `TO_STRING()`, `TO_LONG()`, ...
*   **Conditional:** `CASE WHEN ... THEN ... ELSE ... END`, `COALESCE()`, `IF()`
*   **Network:** `CIDR_MATCH()`
*   **Other:** `IS_NULL()`, `IS_NOT_NULL()`, `IN()`, ...

## Example Pipeline

```esql
-- Find average response time per hour for successful web requests from a specific IP range
FROM "web-logs-*"
| WHERE http.response.status_code < 400 AND CIDR_MATCH(client.ip, '192.168.0.0/16')
| EVAL request_hour = DATE_TRUNC('hour', "@timestamp")
| STATS avg_response = AVG(http.response.response_time_ms) BY request_hour
| SORT request_hour ASC
```

ESQL is powerful for data exploration and transformation.

*(Refer to the official Elasticsearch ESQL documentation.)*