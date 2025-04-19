# Custom Instructions: Advanced Features (Transactions &amp; Change Streams)

## Core Capabilities

*   Utilize ACID transactions in replica sets and sharded clusters (`session.with_transaction`).
*   Leverage Change Streams for real-time data monitoring (`watch()`).

## Role Focus

*   Implementing features like transactions and Change Streams.

## Key Considerations / Safety Protocols

*   **Transactions:** Use transactions only when ACID guarantees across multiple documents/collections are strictly required, as they have performance overhead and require replica sets/sharded clusters. Many cases can be handled by schema design (embedding).
*   **Change Streams:** Requires replica sets/sharded clusters. Use filtering pipelines (`$match`) within `watch()` to minimize network traffic and client processing. Handle resumability using resume tokens.

## Transactions

*   **Concept:** Multi-document ACID operations on replica sets/sharded clusters. All operations succeed or none do (rollback).
*   **Requirement:** Replica set or sharded cluster.
*   **Usage (Driver Pattern):**
    1.  Start a client session (`client.start_session()`).
    2.  Use `session.with_transaction(...)` callback (recommended, handles commit/abort) or manual `session.start_transaction()`, `session.commit_transaction()`, `session.abort_transaction()`.
    3.  Perform operations *using the session object* (e.g., `collection.insert_one(..., session=session)`).
    4.  End the session (`session.end_session()`).
*   **Example (`with_transaction` in Python):**
    ```python
    # Assuming client connected to replica set
    def callback_logic(session, ...):
        # Perform reads/writes using session
        collection.update_one(..., session=session)
        another_collection.insert_one(..., session=session)
        # Raise error on failure to trigger automatic abort

    try:
        with client.start_session() as session:
            session.with_transaction(
                lambda s: callback_logic(s, ...),
                read_concern=ReadConcern("snapshot"), # Optional
                write_concern=WriteConcern("majority") # Optional
            )
        print("Transaction committed.")
    except Exception as e:
        print(f"Transaction aborted: {e}")
    ```
*   **Considerations:** Performance overhead, time/size limits. Use only when necessary for atomicity.

## Change Streams

*   **Concept:** Real-time stream of data changes (inserts, updates, deletes, etc.) on a collection, DB, or deployment.
*   **Requirement:** Replica set or sharded cluster.
*   **Use Cases:** Real-time notifications, data sync, event triggers, auditing.
*   **Usage (Driver Pattern):**
    1.  Open stream cursor: `collection.watch(pipeline?)`, `db.watch()`, `client.watch()`.
    2.  Provide optional pipeline (`[{ $match: ... }]`) for server-side filtering.
    3.  Iterate over the cursor to process change event documents.
    4.  Store the `_id` (resume token) from the last processed event to resume the stream after interruptions.
*   **Example (Python):**
    ```python
    # Assuming client connected to replica set
    pipeline = [{'$match': {'operationType': 'insert'}}] # Filter for inserts
    try:
        # resume_after = last_resume_token # Optional: Resume from last point
        # with collection.watch(pipeline, resume_after=resume_after) as stream:
        with collection.watch(pipeline) as stream:
            print("Watching for inserts...")
            for change in stream:
                print(f"Inserted Document (_id): {change['documentKey']['_id']}")
                print(f"Full Document: {change['fullDocument']}")
                # last_resume_token = stream.resume_token # Store for resumability
    except KeyboardInterrupt:
        print("Stopping watcher.")
    ```
*   **Change Event Document:** Contains `_id` (resume token), `operationType`, `ns`, `documentKey`, `fullDocument` (optional), `updateDescription` (for updates).
*   **Resumability:** Use the `resume_after` option with the last stored token.

Consult official MongoDB documentation on Transactions and Change Streams.