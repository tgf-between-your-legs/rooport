# Elasticsearch: Common Cluster Management APIs (`_cat` & others)

Reference for common REST APIs used for monitoring and managing an Elasticsearch cluster.

## Core Concept

Elasticsearch provides extensive REST APIs for monitoring cluster health, managing indices, checking node status, managing snapshots, and performing other administrative tasks. The `_cat` APIs offer a human-readable, tabular view of cluster information.

**Access:** Typically via `curl` or Kibana Dev Tools.

```bash
# Example using curl (assuming security is disabled or credentials provided)
curl -X GET "localhost:9200/_cat/health?v"
curl -X GET "localhost:9200/_cluster/health?pretty"
curl -u elastic:password -X GET "https://my-secure-cluster:9200/_cat/nodes?v"
```

## `_cat` APIs (Human-Readable)

*   **`GET /_cat/health?v`**: Shows cluster health status (`green`, `yellow`, `red`), number of nodes, number of shards (total, primary, unassigned), etc. `v` adds headers.
*   **`GET /_cat/nodes?v`**: Lists nodes in the cluster, showing IP, heap/RAM usage, CPU, load, node role (`m`, `d`, `i`, etc.), master status (`*`).
*   **`GET /_cat/indices?v`**: Lists indices, showing health, status (`open`/`close`), primary/replica shard counts, document counts, storage size.
    *   `GET /_cat/indices/my-index-*?v`: Filter by index pattern.
    *   `GET /_cat/indices?v&s=docs.count:desc`: Sort by document count descending.
    *   `GET /_cat/indices?v&h=index,docs.count,store.size`: Show only specific columns.
*   **`GET /_cat/shards?v`**: Lists individual shards, showing index, shard number, primary/replica status, state (`STARTED`, `INITIALIZING`, `UNASSIGNED`), document count, size, node location. Useful for diagnosing unassigned shards.
    *   `GET /_cat/shards/my-index?v`: Show shards for a specific index.
*   **`GET /_cat/allocation?v`**: Shows shard allocation across nodes, including disk usage and availability.
*   **`GET /_cat/pending_tasks?v`**: Shows cluster-level tasks currently pending execution (e.g., shard allocation).
*   **`GET /_cat/plugins?v`**: Lists installed plugins on each node.
*   **`GET /_cat/repositories?v`**: Lists registered snapshot repositories.
*   **`GET /_cat/snapshots/<repository_name>?v`**: Lists snapshots within a repository.
*   **`GET /_cat/tasks?v&actions=*search*&detailed`**: Shows details of currently running tasks (e.g., long-running searches).

## Cluster APIs (JSON Output)

*   **`GET /_cluster/health`**: Detailed cluster health information in JSON format.
    *   `?level=indices` or `?level=shards` for more detail.
*   **`GET /_cluster/stats`**: Comprehensive statistics about the cluster state, indices, nodes, JVM, etc.
*   **`GET /_nodes/stats`**: Statistics for all nodes (or specific nodes).
    *   `GET /_nodes/node_id1,node_id2/stats/jvm,os`: Get specific stats (JVM, OS) for specific nodes.
*   **`GET /_nodes/hot_threads`**: Detects threads consuming high CPU, useful for diagnosing performance issues.
*   **`GET /_cluster/settings`**: Shows persistent and transient cluster-wide settings.
*   **`PUT /_cluster/settings`**: Update cluster settings (e.g., allocation rules, logging levels).
    ```json
    // Example: Enable shard allocation
    // PUT /_cluster/settings
    // { "persistent": { "cluster.routing.allocation.enable": "all" } }
    ```
*   **`POST /_cluster/reroute`**: Manually move shards between nodes (use with caution).

## Index Management APIs

*   **`PUT /<index>`**: Create an index (with optional settings/mappings).
*   **`DELETE /<index>`**: Delete an index.
*   **`POST /<index>/_open`**: Open a closed index.
*   **`POST /<index>/_close`**: Close an index (makes it read-only and reduces cluster overhead).
*   **`GET /<index>/_settings`**: Get index settings.
*   **`PUT /<index>/_settings`**: Update dynamic index settings (e.g., `number_of_replicas`, `refresh_interval`).
*   **`GET /<index>/_mapping`**: Get index mapping.
*   **`PUT /<index>/_mapping`**: Add or update fields in an index mapping (limited updates allowed).
*   **`POST /<index>/_refresh`**: Manually refresh an index to make recent changes searchable.
*   **`POST /<index>/_flush`**: Manually flush index changes to disk.
*   **`POST /<index>/_forcemerge?max_num_segments=1`**: Optimize index by merging segments (resource-intensive, run during off-peak hours).
*   **`POST /_reindex`**: Copy documents from a source index to a destination index (useful for mapping changes or upgrades).

## Snapshot & Restore APIs

*   **Register Repository:** (Requires configuration, e.g., shared filesystem, S3, GCS, Azure Blob Storage)
    ```json
    // PUT /_snapshot/my_backup_repo
    // {
    //   "type": "fs", // Or s3, gcs, azure
    //   "settings": {
    //     "location": "/path/to/shared/backups"
    //     // Add cloud storage credentials/settings if using s3/gcs/azure
    //   }
    // }
    ```
*   **Create Snapshot:**
    ```json
    // PUT /_snapshot/my_backup_repo/snapshot_1?wait_for_completion=true
    // {
    //   "indices": "index_1,index_2", // Specific indices or patterns, omit for all
    //   "ignore_unavailable": true,
    //   "include_global_state": false // Usually false unless backing up cluster state
    // }
    ```
*   **Restore Snapshot:**
    ```json
    // Close index before restoring if it exists
    // POST /index_1/_close

    // Restore specific indices from snapshot
    // POST /_snapshot/my_backup_repo/snapshot_1/_restore
    // {
    //   "indices": "index_1,index_2",
    //   "ignore_unavailable": true,
    //   "include_global_state": false,
    //   "rename_pattern": "index_(.+)", // Optional: Rename indices on restore
    //   "rename_replacement": "restored_index_$1"
    // }
    ```
*   **Get Snapshot Status:** `GET /_snapshot/my_backup_repo/snapshot_1`
*   **Delete Snapshot:** `DELETE /_snapshot/my_backup_repo/snapshot_1`

These APIs are essential for monitoring the health, performance, and state of your Elasticsearch cluster and managing its data lifecycle.

*(Refer to the official Elasticsearch documentation for `_cat` APIs and Cluster APIs.)*