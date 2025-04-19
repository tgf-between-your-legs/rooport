# Custom Instructions: 04 - Aggregations

This instruction covers common aggregation patterns using Elasticsearch Query DSL.

## Core Concept

Aggregations provide the ability to group and extract statistics from your data. They are typically placed within the `aggs` (or `aggregations`) key in a search request. You can have multiple aggregations, and they can be nested. Setting `size: 0` in the main request body is common if you only care about the aggregation results.

**Endpoint:** `GET /<index>/_search` or `POST /<index>/_search`

**Basic Structure:**

```json
{
  "query": { ... }, // Optional: Filter documents before aggregating
  "size": 0, // Optional: Don't return document hits
  "aggs": {
    "<aggregation_name>": { // Custom name for the result
      "<aggregation_type>": {
        // ... aggregation parameters ...
      },
      "aggs": { // Optional: Nested sub-aggregations
        "<sub_aggregation_name>": { ... }
      }
    }
    // ... other top-level aggregations ...
  }
}
```

## Common Aggregation Types

**1. Metrics Aggregations (Calculate values):**
*   **`avg`:** Computes the average.
*   **`sum`:** Computes the sum.
*   **`min`:** Finds the minimum value.
*   **`max`:** Finds the maximum value.
*   **`stats`:** Returns `count`, `min`, `max`, `avg`, `sum`.
*   **`extended_stats`:** Includes variance, std deviation, etc.
*   **`cardinality`:** *Approximate* count of distinct values.
*   **`percentiles`:** Calculates percentiles (e.g., 50th, 95th).
*   **`top_hits`:** Returns actual documents matching each bucket.

**Example (Stats):** Get statistics for the `price` field.
```json
{ "size": 0, "aggs": { "price_stats": { "stats": { "field": "price" } } } }
```

**2. Bucket Aggregations (Group documents):**
*   **`terms`:** Creates buckets based on unique field values (most common).
*   **`histogram`:** Creates buckets based on fixed numeric intervals.
*   **`date_histogram`:** Creates buckets based on date/time intervals (`minute`, `hour`, `day`, `month`, `year`, `10d`).
*   **`range`:** Creates buckets based on custom numeric ranges.
*   **`date_range`:** Creates buckets based on custom date ranges.
*   **`filter`:** Creates a single bucket matching a filter.
*   **`filters`:** Creates multiple named buckets, each defined by a filter.
*   **`nested`:** Aggregates on fields within `nested` documents.
*   **`significant_terms`:** Finds terms unusually frequent in a subset vs. background.

**Example (`terms`):** Count documents per `status` (keyword field).
```json
{ "size": 0, "aggs": { "docs_per_status": { "terms": { "field": "status", "size": 10 } } } }
```

**Example (`date_histogram`):** Count documents per month.
```json
{ "size": 0, "aggs": { "docs_per_month": {
    "date_histogram": {
      "field": "created_at",
      "calendar_interval": "month",
      "format": "yyyy-MM", // Optional format
      "min_doc_count": 1 // Optional: Only return non-empty buckets
    }
} } }
```

**Example (Nested Aggregations):** Count per status, then average price within each status.
```json
{ "size": 0, "aggs": { "docs_per_status": {
    "terms": { "field": "status", "size": 10 },
    "aggs": { // Sub-aggregation
      "avg_price_in_status": { "avg": { "field": "price" } }
    }
} } }
```

**Example (`terms` with `top_hits`):** Group by category, show top 3 recent items per category.
```json
{ "size": 0, "aggs": { "categories": {
    "terms": { "field": "category.keyword", "size": 10 },
    "aggs": { "top_items": {
        "top_hits": {
          "size": 3,
          "sort": [ { "created_at": "desc" } ],
          "_source": ["title", "created_at"]
        }
    } }
} } }
```

**Example (`filter`):** Count documents matching a filter.
```json
{ "size": 0, "aggs": { "published_docs": {
    "filter": { "term": { "status": "published" } }
    // Can add sub-aggregations here
} } }
```

Choose the right combination of bucket and metric aggregations to analyze your data effectively.

*(Refer to the official Elasticsearch Aggregations documentation.)*