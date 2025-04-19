# Elasticsearch: ESQL (Elasticsearch Query Language) Reference

Basic syntax and common commands for ESQL.

## Core Concept

ESQL (Elasticsearch Query Language) provides a pipe-based (`|`) language, similar in feel to SQL and shell pipelines, for querying, transforming, and analyzing data within Elasticsearch. It's designed for data exploration and can be used via the ESQL API endpoint or Kibana Dev Tools.

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

1.  **`FROM <index_pattern>`:**
    *   Specifies the data source (index, data stream, or alias). Wildcards are allowed. This is typically the first command.
    *   **Example:** `FROM my-logs-*`
    *   **Example:** `FROM products`

2.  **`WHERE <condition>`:**
    *   Filters rows based on a boolean condition. Uses familiar comparison (`=`, `!=`, `>`, `<`, `>=`, `<=`), logical (`AND`, `OR`, `NOT`), and other operators/functions.
    *   **Example:** `| WHERE status = 'completed' AND response_time > 100`
    *   **Example:** `| WHERE user.id IN ('user1', 'user2')`
    *   **Example:** `| WHERE STARTS_WITH(message, 'Error:')`

3.  **`LIMIT <count>`:**
    *   Restricts the number of rows returned.
    *   **Example:** `| LIMIT 100`

4.  **`KEEP <field1>, <field2>, ...`:**
    *   Selects specific columns to keep in the output, discarding others. Similar to `SELECT column1, column2` in SQL.
    *   **Example:** `| KEEP timestamp, user.name, message`

5.  **`DROP <field1>, <field2>, ...`:**
    *   Removes specified columns from the output.
    *   **Example:** `| DROP user.password_hash, internal_details`

6.  **`SORT <field1> [ASC|DESC], <field2> [ASC|DESC], ...`:**
    *   Orders the results by one or more fields. `ASC` is default.
    *   **Example:** `| SORT timestamp DESC, user.id ASC`

7.  **`EVAL <new_field> = <expression>`:**
    *   Computes a new field based on an expression involving existing fields or functions. Can also overwrite existing fields.
    *   **Example:** `| EVAL duration_ms = duration_ns / 1000000`
    *   **Example:** `| EVAL user_agent_type = CASE(CONTAINS(user_agent.original, 'Mobile'), 'Mobile', CONTAINS(user_agent.original, 'Tablet'), 'Tablet', 'Desktop')`

8.  **`STATS ... BY <group_field1>, <group_field2>, ...`:**
    *   Performs aggregations, similar to SQL's `GROUP BY`.
    *   **Syntax:** `| STATS <agg_func>(<field>) AS <alias>, ... BY <group_field1>, ...`
    *   **Common Aggregation Functions:** `COUNT(*)`, `COUNT(<field>)`, `COUNT_DISTINCT(<field>)`, `SUM(<field>)`, `AVG(<field>)`, `MIN(<field>)`, `MAX(<field>)`, `PERCENTILE(<field>, N)`, `FIRST(<field> [ORDER BY ...])`, `LAST(<field> [ORDER BY ...])`.
    *   **Example:** Count events and calculate average response time per host.
        ```esql
        | STATS
            event_count = COUNT(*),
            avg_response = AVG(response_time)
          BY host.name
        ```
    *   **Example:** Find the latest timestamp per user.
        ```esql
        | STATS latest_event = MAX(timestamp) BY user.id
        ```

9.  **`ENRICH <policy_name> WITH <enrich_field> = <match_field>`:**
    *   (Requires pre-configured Enrich Policies) Augments rows with data from another index based on a matching field.
    *   **Example:** `| ENRICH user_info_policy WITH user.geo = user.ip`

10. **`DISSECT '<pattern>' ON <field>`:**
    *   Extracts structured fields from a string field based on a simple pattern with delimiters.
    *   **Example:** `| DISSECT '%{client_ip} %{ident} %{auth} [%{@timestamp}] "%{verb} %{request} HTTP/%{http_version}" %{status_code} %{bytes}' ON message`

11. **`GROK '<pattern>' ON <field>`:**
    *   Extracts structured fields using more complex Grok patterns (common in Logstash).
    *   **Example:** `| GROK '%{COMBINEDAPACHELOG}' ON message`

## Functions & Operators

ESQL supports a wide range of functions and operators:

*   **Mathematical:** `+`, `-`, `*`, `/`, `%`, `ABS()`, `ROUND()`, `FLOOR()`, `CEIL()`, `SQRT()`, ...
*   **String:** `CONCAT()`, `SUBSTRING()`, `LENGTH()`, `LOWER()`, `UPPER()`, `TRIM()`, `STARTS_WITH()`, `ENDS_WITH()`, `CONTAINS()`, `REPLACE()`, ...
*   **Date/Time:** `NOW()`, `TODAY()`, `DATE_TRUNC()`, `INTERVAL`, `+`, `-`, ...
*   **Type Conversion:** `CAST(<field> AS <type>)`, `TO_STRING()`, `TO_LONG()`, `TO_DOUBLE()`, `TO_BOOLEAN()`, ...
*   **Conditional:** `CASE WHEN ... THEN ... ELSE ... END`, `COALESCE(<val1>, <val2>, ...)`, `IF(<cond>, <true_val>, <false_val>)`
*   **Network:** `CIDR_MATCH(<ip_field>, 'cidr1', 'cidr2', ...)`
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

ESQL offers a powerful alternative to Query DSL for certain data exploration and transformation tasks, especially for users familiar with SQL or pipeline-based processing.

*(Refer to the official Elasticsearch ESQL documentation.)*