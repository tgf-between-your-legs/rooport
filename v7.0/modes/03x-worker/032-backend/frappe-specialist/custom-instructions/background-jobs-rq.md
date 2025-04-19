# Frappe: Background Jobs (RQ & Scheduler)

Running tasks asynchronously using Frappe's background job system based on RQ (Redis Queue).

## Core Concept

Some tasks take too long to run within a standard web request cycle (e.g., sending bulk emails, generating large reports, complex data processing, integrating with slow external APIs). Frappe provides a background job processing system built on **RQ (Redis Queue)** and managed by the **Frappe Scheduler** and **Workers**.

*   **Enqueueing:** You can enqueue a Python function (defined in your app) to be executed later by a background worker.
*   **Workers (`bench worker`):** Separate processes that continuously monitor Redis queues for jobs to execute. You can run multiple workers.
*   **Scheduler (`bench schedule`):** A process that enqueues scheduled jobs (defined in `hooks.py`) at the specified times.
*   **Redis:** Used as the message broker to hold the queues and job information.

## Enqueueing Jobs (`frappe.enqueue`)

*   **Purpose:** Add a function call to a queue for background execution.
*   **Syntax:** `frappe.enqueue(method, queue='default', timeout=300, event=None, is_async=True, job_name=None, **kwargs)`
    *   **`method` (Required):** Dotted path string to the Python function to execute (e.g., `'my_app.tasks.process_large_file'`). The function must be importable by the worker.
    *   **`queue`:** Name of the queue ('short', 'default', 'long'). Determines worker priority/allocation.
    *   **`timeout`:** Job timeout in seconds (default 300 = 5 minutes).
    *   **`is_async`:** If `True` (default), enqueues the job. If `False`, runs the function immediately (useful for testing/debugging).
    *   **`job_name`:** Unique name for the job. If a job with the same name is already pending or running, the new one won't be enqueued.
    *   **`**kwargs`:** Keyword arguments to pass to the background function. Arguments must be JSON serializable.

```python
# my_app/controllers/some_doctype.py
import frappe

def some_action_triggering_background_job(doc):
    # ... some initial logic ...

    # Enqueue the task
    frappe.enqueue(
        'my_app.tasks.generate_report', # Dotted path to the function
        queue='long', # Use the long queue for potentially slow tasks
        timeout=1800, # 30 minutes timeout
        report_id=doc.name, # Pass arguments needed by the task
        user_email=frappe.session.user
    )

    frappe.msgprint("Report generation started in the background. You will be notified upon completion.")

# my_app/tasks.py (Define the background task function)
import frappe
import time

def generate_report(report_id, user_email):
    try:
        frappe.set_user("Administrator") # Often need admin rights for background tasks
        print(f"Starting report generation for {report_id}")
        # Simulate long process
        time.sleep(60)
        # ... actual report generation logic ...
        report_data = f"Report data for {report_id}"

        # Example: Save report or notify user
        frappe.get_doc({
            "doctype": "File",
            "file_name": f"report_{report_id}.txt",
            "attached_to_doctype": "Some Doctype", # Optional: Link to original doc
            "attached_to_name": report_id,
            "content": report_data,
            "is_private": 1
        }).insert()

        # Notify user (optional)
        frappe.sendmail(
            recipients=[user_email],
            subject=f"Report {report_id} Ready",
            message="Your report is ready for download."
        )
        print(f"Finished report generation for {report_id}")

    except Exception as e:
        print(f"Error generating report {report_id}: {e}")
        # Log error more formally
        frappe.log_error(f"Report Generation Failed for {report_id}", frappe.get_traceback())
    finally:
        frappe.set_user("Guest") # Reset user context if changed

```

## Scheduler (`hooks.py`)

*   Define functions to be run automatically on a schedule (daily, weekly, monthly, hourly, or custom CRON).
*   The `bench schedule` process reads this hook and enqueues the specified jobs at the appropriate times. The jobs are then picked up by `bench worker`.

```python
# my_app/hooks.py
scheduler_events = {
    # Runs daily (at a time configured in site settings or default)
    "daily": [
        "my_app.tasks.daily_summary"
    ],
    # Runs weekly
    "weekly_long": [ # Use _long, _default, _short suffix for queue
        "my_app.tasks.weekly_report_cleanup"
    ],
    # Runs monthly
    "monthly": [
        "my_app.tasks.archive_old_data"
    ],
    # Runs every hour
    "hourly": [
        "my_app.tasks.sync_external_data"
    ],
    # Runs every 10 minutes
    "all": [ # 'all' runs frequently (approx every 5 mins by default)
         #"my_app.tasks.frequent_check"
    ],
    # Custom CRON schedule (minute hour day month weekday)
    "cron": {
        "0 2 * * *": [ # Run at 2:00 AM every day
            "my_app.tasks.nightly_maintenance"
        ],
        "*/15 * * * *": [ # Run every 15 minutes
            "my_app.tasks.poll_service_status"
        ]
    }
}
```

## Running Workers & Scheduler (Production)

*   In production, you need dedicated processes running for workers and the scheduler.
*   **Commands:**
    *   `bench worker --queue short,default` (Runs workers for specific queues)
    *   `bench worker --queue long` (Separate worker for long tasks)
    *   `bench schedule` (Runs the scheduler process)
*   **Process Management:** Use `supervisor` (configured via `bench setup supervisor`) or `systemd` to manage these processes, ensuring they run continuously and restart if they fail.

## Monitoring

*   **Desk UI:** Setup -> Background Jobs: View the status of queued, running, failed, and finished jobs.
*   **Logs:** Check `logs/worker.log` and `logs/schedule.log` in the bench directory.
*   **Redis:** Tools like `rq-dashboard` can be used to monitor Redis queues directly.

Background jobs are essential for handling long-running tasks without impacting user experience and for automating recurring processes.

*(Refer to the official Frappe Background Jobs documentation: https://frappeframework.com/docs/user/en/basics/background-jobs)*