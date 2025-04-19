# Diagnostic Commands (`execute_command`)

This document provides examples of diagnostic commands that might be instructed for use with `footgun-debug`, categorized by potential risk. **Always explain the purpose and expected output when instructing the mode to use `execute_command`.** Request clarification for any command not understood or seeming excessively risky.

## Generally Safe (Read-Only) Commands

These commands typically inspect state without changing it.

*   `pwd`: Print working directory.
*   `ls -la [path]`: List directory contents (with details).
*   `cat [file_path]`: Display file content.
*   `head -n [lines] [file_path]`: Display the first N lines of a file.
*   `tail -n [lines] [file_path]`: Display the last N lines of a file.
*   `grep '[pattern]' [file_path]`: Search for a pattern within a file.
*   `ps aux | grep '[process_name]'`: Check if a process is running.
*   `netstat -tulnp | grep '[port]'`: Check which process is listening on a port (requires net-tools).
*   `ss -tulnp | grep '[port]'`: Check which process is listening on a port (modern alternative to netstat).
*   `df -h`: Check disk space usage.
*   `free -h`: Check memory usage.
*   `uptime`: Check system load and uptime.
*   `ping -c 3 [hostname/IP]`: Check basic network connectivity.
*   `curl -I [URL]`: Fetch headers from a URL to check reachability/status.
*   `systemctl status [service_name]`: Check the status of a systemd service.
*   `journalctl -u [service_name] -n [lines] --no-pager`: View recent logs for a systemd service.

## Potentially Moderate Risk Commands

These commands might modify temporary state, consume more resources, or require careful interpretation. Ensure purpose is clear.

*   `curl [URL]`: Fetch full content from a URL (could be large).
*   `wget [URL]`: Download a file (ensure destination is safe/intended).
*   `find [path] -name '[pattern]'`: Search for files (can be resource-intensive on large directories).
*   `strace -p [PID]`: Trace system calls for a process (can generate large output, requires permissions).
*   `lsof -p [PID]`: List open files for a process (requires permissions).
*   `tcpdump -i [interface] -n 'host [IP] and port [port]' -c [count]`: Capture network packets (requires permissions, generates specific output).
*   Running specific application diagnostic commands (e.g., `npm run test:specific`, `python manage.py check`).

## High Risk Commands (Require Explicit Justification & Confirmation)

These commands can modify system state, delete data, or have significant security implications. **Use with extreme caution and only when explicitly justified and confirmed by the orchestrator.**

*   `rm [file_path]`: Delete files.
*   `rm -rf [directory_path]`: Delete directories recursively (**VERY DANGEROUS**).
*   `mv [source] [destination]`: Move/rename files or directories.
*   `kill [PID]`: Terminate a process.
*   `systemctl restart [service_name]`: Restart a service (can cause downtime).
*   `systemctl stop [service_name]`: Stop a service.
*   Any command involving `sudo` or root privileges.
*   Any command that modifies configuration files directly (`sed`, `awk` on config files).
*   Running arbitrary scripts (`sh script.sh`, `python script.py`).

**Guideline:** When instructing `footgun-debug` to use `execute_command`, prefer read-only commands. If modification or higher risk is needed, the instruction *must* acknowledge the risk and provide clear justification. The mode should always ask for clarification if unsure or if a command seems unnecessarily risky for the diagnostic goal.