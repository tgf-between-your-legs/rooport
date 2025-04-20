# Frappe Specialist: Background Jobs &amp; Scheduler

Frappe uses RQ (Redis Queue) for handling background jobs, allowing long-running tasks to execute asynchronously without blocking web requests.

## 1. Core Concepts

*   **Purpose:** Execute tasks that take too long for a web request (e.g., bulk emails, large report generation, complex calculations, slow external API calls).
*   **Components:**
    *   **Redis:** Message broker holding job queues.
    *   **Enqueueing (`frappe.enqueue`):** Adding a Python function call to a queue.
    *   **Workers (`bench worker`):** Processes that pick up and execute jobs from Redis queues.
    *   **Scheduler (`bench schedule`):** Process that enqueues scheduled jobs (from `hooks.py`) at specific times.

## 2. Enqueueing Jobs (`frappe.enqueue`)

*   **Function:** `frappe.enqueue(method, queue='default', timeout=300, event=None, is_async=True, job_name=None, **kwargs)`
*   **Parameters:**
    *   `method` (Required): Dotted path string to the Python function (e.g., `'my_app.tasks.process_data'`). Must be importable by the worker.
    *   `queue`: Queue name ('short', 'default', 'long'). Affects priority/worker allocation.
    *   `timeout`: Job timeout in seconds (default 300).
    *   `is_async`: `True` (default) enqueues the job. `False` runs it synchronously (for testing).
    *   `job_name`: Unique name. Prevents duplicate pending/running jobs with the same name.
    *   `**kwargs`: Keyword arguments passed to the target function (must be JSON serializable).
*   **Example:**
    ```python
    # In a controller or hook
    import frappe

    def trigger_background_report(doc):
        frappe.enqueue(
            'my_app.tasks.generate_report', # Path to function
            queue='long',
            timeout=1800, # 30 min timeout
            report_id=doc.name,
            user_email=frappe.session.user
        )
        frappe.msgprint("Report generation started in background.")

    # my_app/tasks.py
    import frappe
    import time

    def generate_report(report_id, user_email):
        try:
            # Often need to set user context if specific permissions are needed
            # frappe.set_user("Administrator")
            print(f"Generating report {report_id}")
            time.sleep(30) # Simulate work
            # ... generate report ...
            print(f"Finished report {report_id}")
            # Notify user (optional)
            # frappe.sendmail(...)
        except Exception as e:
            frappe.log_error(f"Report Failed: {report_id}", frappe.get_traceback())
        # finally:
            # frappe.set_user("Guest") # Reset user if changed
    ```

## 3. Scheduled Jobs (`hooks.py`)

*   **Purpose:** Define jobs to run automatically on a schedule (daily, weekly, hourly, cron).
*   **Mechanism:** The `bench schedule` process reads `scheduler_events` in `hooks.py` and uses `frappe.enqueue` to add jobs to the appropriate queue at the scheduled time. Workers then pick up these jobs.
*   **Example (`hooks.py`):**
    ```python
    scheduler_events = {
        # Runs daily (time configured in settings)
        "daily": [
            "my_app.tasks.daily_summary"
        ],
        # Runs weekly, specify queue with suffix (_long, _default, _short)
        "weekly_long": [
            "my_app.tasks.weekly_cleanup"
        ],
        # Runs hourly
        "hourly": [
            "my_app.tasks.sync_external_data"
        ],
        # Runs frequently (approx. every 5 mins by default)
        "all": [
             #"my_app.tasks.frequent_check"
        ],
        # Custom CRON schedule (minute hour day month weekday)
        "cron": {
            "0 3 * * *": [ # 3:00 AM daily
                "my_app.tasks.nightly_backup_check"
            ],
            "*/10 * * * *": [ # Every 10 minutes
                "my_app.tasks.poll_status"
            ]
        }
    }
    ```

## 4. Running Workers & Scheduler (Production)

*   **Requirement:** Dedicated processes must run continuously in production.
*   **Commands:**
    *   `bench worker --queue short,default` (Handles short/default queues)
    *   `bench worker --queue long` (Separate worker for long tasks recommended)
    *   `bench schedule` (Runs the scheduler)
*   **Process Management:** Use `supervisor` (via `bench setup supervisor`) or `systemd` to manage these processes, ensuring they run reliably and restart on failure.

## 5. Monitoring

*   **Desk UI:** Setup -> System -> Background Jobs: View job statuses (Queued, Started, Finished, Failed). Failed jobs show tracebacks.
*   **Logs:** Check `logs/worker.log` and `logs/schedule.log` in the bench directory.
*   **Redis:** Advanced monitoring using tools like `rq-dashboard` or Redis monitoring commands.

Background jobs are crucial for performance and automation in Frappe. Use `frappe.enqueue` for tasks triggered by user actions that might be slow, and `scheduler_events` for recurring automated tasks.