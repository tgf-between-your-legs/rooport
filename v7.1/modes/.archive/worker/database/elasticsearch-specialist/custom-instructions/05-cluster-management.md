# Custom Instructions: 05 - Cluster Management APIs

This instruction covers common REST APIs for monitoring and managing an Elasticsearch cluster, focusing on `_cat` and other relevant endpoints.

## Core Concept

Elasticsearch provides extensive REST APIs for monitoring cluster health, managing indices, checking node status, managing snapshots, and performing other administrative tasks. The `_cat` APIs offer a human-readable, tabular view.

**Access:** Typically via `curl` or Kibana Dev Tools.
```bash
# Example using curl
curl -X GET "localhost:9200/_cat/health?v"
curl -X GET "localhost:9200/_cluster/health?pretty"
# With security:
# curl -u elastic:password -X GET "https://my-secure-cluster:9200/_cat/nodes?v"
```

## `_cat` APIs (Human-Readable)

*   **`GET /_cat/health?v`**: Cluster health (`green`/`yellow`/`red`), node/shard counts.
*   **`GET /_cat/nodes?v`**: Node list, resource usage (heap, RAM, CPU), roles, master status.
*   **`GET /_cat/indices?v`**: Index list, health, status, shard/doc counts, size.
    *   `?v&s=docs.count:desc`: Sort results.
    *   `?v&h=index,docs.count`: Show specific columns.
*   **`GET /_cat/shards?v`**: Shard list, index, primary/replica, state, node location. Useful for diagnosing unassigned shards.
*   **`GET /_cat/allocation?v`**: Shard allocation across nodes, disk usage.
*   **`GET /_cat/pending_tasks?v`**: Pending cluster tasks.
*   **`GET /_cat/plugins?v`**: Installed plugins per node.
*   **`GET /_cat/repositories?v`**: Registered snapshot repositories.
*   **`GET /_cat/snapshots/<repo_name>?v`**: Snapshots in a repository.
*   **`GET /_cat/tasks?v&actions=*search*&detailed`**: Running tasks (e.g., long searches).

## Cluster APIs (JSON Output)

*   **`GET /_cluster/health`**: Detailed cluster health (JSON). `?level=indices|shards` for more detail.
*   **`GET /_cluster/stats`**: Comprehensive cluster statistics.
*   **`GET /_nodes/stats`**: Node statistics. `GET /_nodes/<node_id>/stats/jvm,os` for specifics.
*   **`GET /_nodes/hot_threads`**: Identify high-CPU threads.
*   **`GET /_cluster/settings`**: View cluster-wide settings.
*   **`PUT /_cluster/settings`**: Update cluster settings.
    ```json
    // Example: Enable shard allocation
    // { "persistent": { "cluster.routing.allocation.enable": "all" } }
    ```
*   **`POST /_cluster/reroute`**: Manually move shards (use with caution).

## Index Management APIs

*   **`PUT /<index>`**: Create index (with settings/mappings).
*   **`DELETE /<index>`**: Delete index.
*   **`POST /<index>/_open` / `POST /<index>/_close`**: Open/close index.
*   **`GET /<index>/_settings` / `PUT /<index>/_settings`**: Get/update index settings (e.g., `number_of_replicas`).
*   **`GET /<index>/_mapping` / `PUT /<index>/_mapping`**: Get/update index mapping (limited updates).
*   **`POST /<index>/_refresh`**: Manually make changes searchable.
*   **`POST /<index>/_flush`**: Manually flush changes to disk.
*   **`POST /<index>/_forcemerge?max_num_segments=1`**: Optimize index (resource-intensive).
*   **`POST /_reindex`**: Copy documents between indices.

## Snapshot & Restore APIs

*   **Register Repository:** `PUT /_snapshot/<repo_name>` with type (`fs`, `s3`, `gcs`, `azure`) and settings (location, credentials).
    ```json
    // PUT /_snapshot/my_backup_repo
    // { "type": "fs", "settings": { "location": "/path/to/shared/backups" } }
    ```
*   **Create Snapshot:** `PUT /_snapshot/<repo_name>/<snapshot_name>?wait_for_completion=true` with optional body specifying indices.
    ```json
    // PUT /_snapshot/my_backup_repo/snap1?wait_for_completion=true
    // { "indices": "index_1,index_2", "ignore_unavailable": true }
    ```
*   **Restore Snapshot:** `POST /_snapshot/<repo_name>/<snapshot_name>/_restore` with optional body specifying indices and rename patterns. (Close index first if restoring over existing).
    ```json
    // POST /_snapshot/my_backup_repo/snap1/_restore
    // { "indices": "index_1", "rename_pattern": "index_(.+)", "rename_replacement": "restored_index_$1" }
    ```
*   **Get Snapshot Status:** `GET /_snapshot/<repo_name>/<snapshot_name>`
*   **Delete Snapshot:** `DELETE /_snapshot/<repo_name>/<snapshot_name>`

These APIs are essential for monitoring and managing your Elasticsearch cluster.

*(Refer to the official Elasticsearch documentation for `_cat` APIs and Cluster APIs.)*