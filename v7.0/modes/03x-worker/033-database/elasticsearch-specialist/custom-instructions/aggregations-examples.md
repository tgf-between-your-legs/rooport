# Elasticsearch: Common Aggregation Examples

Illustrative examples of common aggregations using Elasticsearch Query DSL.

## Core Concept

Aggregations provide the ability to group and extract statistics from your data. They are typically placed within the `aggs` (or `aggregations`) key in a search request. You can have multiple aggregations, and they can be nested. Setting `size: 0` in the main request body is common if you only care about the aggregation results and not the individual document hits.

**Endpoint:** `GET /<index>/_search` or `POST /<index>/_search`

**Basic Structure:**

```json
{
  "query": { ... }, // Optional: Filter documents before aggregating
  "size": 0, // Optional: Don't return document hits, only aggregation results
  "aggs": {
    "<aggregation_name>": { // A custom name for your aggregation result
      "<aggregation_type>": {
        // ... aggregation parameters ...
      },
      "aggs": { // Optional: Nested sub-aggregations
        "<sub_aggregation_name>": {
          "<sub_aggregation_type>": { ... }
        }
      }
    }
    // ... other top-level aggregations ...
  }
}
```

## Common Aggregation Types

**1. Metrics Aggregations (Calculate values):**

*   **`avg`:** Computes the average of numeric values.
*   **`sum`:** Computes the sum of numeric values.
*   **`min`:** Finds the minimum value.
*   **`max`:** Finds the maximum value.
*   **`stats`:** Returns `count`, `min`, `max`, `avg`, and `sum` in one go.
*   **`extended_stats`:** Includes variance, std deviation, sum of squares.
*   **`cardinality`:** *Approximate* count of distinct values (more efficient than `terms` for high cardinality).
*   **`percentiles`:** Calculates percentiles (e.g., 50th, 95th, 99th).
*   **`top_hits`:** Returns actual documents matching each bucket (useful within bucket aggregations).

**Example (Stats):** Get statistics for the `price` field.

```json
{
  "size": 0,
  "aggs": {
    "price_stats": { // Custom name for the result
      "stats": {
        "field": "price"
      }
    }
  }
}
```

**2. Bucket Aggregations (Group documents):**

*   **`terms`:** Creates buckets based on the unique values found in a field (`keyword`, numeric, date, etc.). Most common bucketing aggregation.
*   **`histogram`:** Creates buckets based on fixed numeric intervals.
*   **`date_histogram`:** Creates buckets based on fixed date/time intervals (`minute`, `hour`, `day`, `month`, `year`, or fixed like `10d`).
*   **`range`:** Creates buckets based on custom numeric ranges.
*   **`date_range`:** Creates buckets based on custom date ranges.
*   **`filter`:** Creates a single bucket containing documents matching a specific filter.
*   **`filters`:** Creates multiple named buckets, each defined by a filter.
*   **`nested`:** Aggregates on fields within `nested` documents.
*   **`significant_terms`:** Finds terms that are unusually frequent in a subset compared to the background document set (useful for discovery).

**Example (`terms`):** Count documents per `status` (keyword field).

```json
{
  "size": 0,
  "aggs": {
    "docs_per_status": { // Custom name
      "terms": {
        "field": "status", // Assumes 'status' is keyword or suitable type
        "size": 10 // Max number of buckets to return
      }
    }
  }
}
```

**Example (`date_histogram`):** Count documents per month.

```json
{
  "size": 0,
  "aggs": {
    "docs_per_month": {
      "date_histogram": {
        "field": "created_at",
        "calendar_interval": "month", // Or "1M", "day", "year", etc.
        "format": "yyyy-MM", // Optional: Format for the bucket key
        "min_doc_count": 1 // Optional: Only return buckets with at least 1 doc
      }
    }
  }
}
```

**Example (Nested Aggregations):** Count documents per status, and calculate average price within each status bucket.

```json
{
  "size": 0,
  "aggs": {
    "docs_per_status": {
      "terms": {
        "field": "status",
        "size": 10
      },
      "aggs": { // Sub-aggregation within the terms buckets
        "avg_price_in_status": {
          "avg": {
            "field": "price"
          }
        }
      }
    }
  }
}
```

**Example (`terms` with `top_hits`):** Group by category, show the top 3 most recent items in each category.

```json
{
  "size": 0,
  "aggs": {
    "categories": {
      "terms": { "field": "category.keyword", "size": 10 },
      "aggs": {
        "top_items": {
          "top_hits": {
            "size": 3, // Show top 3 hits per category
            "sort": [ { "created_at": "desc" } ],
            "_source": ["title", "created_at"] // Fields to return for hits
          }
        }
      }
    }
  }
}
```

**Example (`filter`):** Count documents matching a specific filter.

```json
{
  "size": 0,
  "aggs": {
    "published_docs": {
      "filter": { "term": { "status": "published" } }
      // Can add sub-aggregations here to analyze only published docs
    }
  }
}
```

Aggregations are incredibly powerful for analyzing and summarizing data stored in Elasticsearch. Choose the right combination of bucket and metric aggregations to answer your data questions.

*(Refer to the official Elasticsearch Aggregations documentation.)*