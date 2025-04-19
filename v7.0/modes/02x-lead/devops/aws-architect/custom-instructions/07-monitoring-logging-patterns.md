# AWS Monitoring and Logging Patterns

This document outlines common patterns and best practices for monitoring resources and applications, and collecting logs within the AWS environment, primarily using CloudWatch and related services.

## Core Concepts

*   **Monitoring:** Collecting metrics (quantitative data points over time) about system performance and health (e.g., CPU utilization, request latency, error counts).
*   **Logging:** Collecting event records (qualitative, timestamped data) about what happened within a system or application (e.g., application errors, API calls, OS events).
*   **Observability:** The ability to infer the internal state of a system from its external outputs (metrics, logs, traces). CloudWatch provides tools for all three pillars.
*   **Alerting:** Automatically notifying relevant personnel or triggering automated actions when predefined thresholds or conditions (based on metrics or logs) are met.

## Key AWS Services

*   **CloudWatch Metrics:** Time-series data repository. Collects metrics from AWS services, custom application metrics (`PutMetricData` API), and agent-collected system metrics.
*   **CloudWatch Logs:** Centralized log aggregation service. Collects logs from AWS services (VPC Flow Logs, Lambda, Route 53, etc.), applications via the CloudWatch Agent or SDK, and custom sources. Organizes logs into Log Groups and Log Streams.
*   **CloudWatch Alarms:** Watches a single CloudWatch metric or the result of a math expression based on metrics. Performs actions (e.g., send SNS notification, trigger Auto Scaling, trigger Step Function) based on the alarm state (OK, ALARM, INSUFFICIENT_DATA).
*   **CloudWatch Dashboards:** Customizable visualizations of metrics and query results from CloudWatch Logs. Provides a single view of resource and application health.
*   **CloudWatch Events (EventBridge):** Delivers a near real-time stream of system events describing changes in AWS resources. Can trigger targets like Lambda, SQS, SNS based on event patterns. Also used for scheduled events (cron).
*   **CloudWatch Logs Insights:** Interactive query service to analyze log data in CloudWatch Logs. Uses a purpose-built query language.
*   **CloudWatch Agent:** Collects system-level metrics (CPU, memory, disk, network) and logs from EC2 instances and on-premises servers.
*   **X-Ray:** Distributed tracing service. Helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. Tracks requests as they travel through services.
*   **CloudTrail:** Records AWS API calls. Essential for security auditing and operational troubleshooting. Logs can be sent to CloudWatch Logs for analysis and alerting.
*   **VPC Flow Logs:** Captures information about IP traffic going to and from network interfaces in a VPC. Logs can be sent to CloudWatch Logs or S3.

## Common Patterns

### 1. Basic Resource Monitoring & Alerting

*   **Goal:** Monitor core health metrics of AWS resources (EC2, RDS, ELB, etc.) and alert on critical issues.
*   **Implementation:**
    *   Utilize default CloudWatch metrics provided by AWS services.
    *   Install CloudWatch Agent on EC2 instances for detailed OS-level metrics (memory, disk space).
    *   Create CloudWatch Alarms for key metrics (e.g., EC2 CPUUtilization > 80%, RDS FreeableMemory < threshold, ELB HTTPCode_Target_5XX_Count > 0).
    *   Configure alarm actions to notify an SNS topic, which can then fan out to email, PagerDuty, Slack, etc.
    *   Create CloudWatch Dashboards to visualize key metrics.

### 2. Centralized Application & System Logging

*   **Goal:** Aggregate logs from applications and instances into a central location for analysis and troubleshooting.
*   **Implementation:**
    *   Configure applications (running on EC2, ECS, EKS, Lambda) to output logs to standard output/error or specific files.
    *   Install and configure the CloudWatch Agent on EC2 instances to push OS logs (e.g., `/var/log/messages`, `/var/log/secure`) and application log files to CloudWatch Logs.
    *   For containers (ECS/EKS), use the `awslogs` log driver (or Fluentd/Fluent Bit) to send container logs to CloudWatch Logs.
    *   Lambda functions automatically send logs to CloudWatch Logs.
    *   Organize logs using meaningful Log Group and Log Stream names.
    *   Set appropriate retention periods for Log Groups.

### 3. Log-Based Alerting

*   **Goal:** Trigger alerts based on specific patterns or error messages found in logs.
*   **Implementation:**
    *   Create CloudWatch Metric Filters on Log Groups. These filters search for patterns (e.g., "ERROR", "FATAL", "404 Not Found") in incoming log events and publish custom CloudWatch Metrics (e.g., `ApplicationErrorCount`).
    *   Create CloudWatch Alarms based on these custom metrics (e.g., alert if `ApplicationErrorCount` > 5 in 1 minute).

### 4. Security & Audit Logging/Alerting

*   **Goal:** Monitor for security-related events and potential compliance violations using CloudTrail and Config.
*   **Implementation:**
    *   Ensure CloudTrail is enabled and logging to S3/CloudWatch Logs.
    *   Create CloudWatch Metric Filters and Alarms based on specific CloudTrail events (e.g., Root user login, IAM policy changes, Security Group changes, S3 bucket policy changes, failed console logins).
    *   Use AWS Config rules to detect non-compliant resource configurations (e.g., unencrypted S3 buckets, publicly accessible Security Groups). Configure Config rules to trigger SNS notifications or remediation actions (e.g., via Lambda).
    *   Analyze VPC Flow Logs (sent to CloudWatch Logs or S3 via Kinesis Data Firehose) for suspicious network traffic (e.g., rejected connections, traffic to known malicious IPs). Use Logs Insights or Athena for querying.
    *   Leverage Security Hub and GuardDuty findings, potentially creating EventBridge rules to trigger alerts or automated responses based on high-severity findings.

### 5. Distributed Tracing with X-Ray

*   **Goal:** Trace requests as they flow through multiple services in a distributed application (microservices, serverless).
*   **Implementation:**
    *   Integrate the X-Ray SDK into application code (supported languages like Java, Node.js, Python, Go, .NET, Ruby).
    *   Enable X-Ray tracing for supported AWS services (Lambda, API Gateway, ELB, EC2 via Agent, ECS/EKS via sidecar/agent).
    *   Use the X-Ray console to visualize the service map, identify bottlenecks, and analyze trace details for errors and performance issues.

## Best Practices

*   **Consistent Naming:** Use consistent naming conventions for metrics, alarms, dashboards, log groups, and streams.
*   **Tagging:** Tag CloudWatch resources (Alarms, Dashboards) for organization and cost allocation.
*   **Structured Logging:** Log events in a structured format (e.g., JSON) to make querying and analysis easier (especially with Logs Insights). Include relevant context (e.g., request ID, user ID) in logs.
*   **Appropriate Retention:** Set log retention periods based on compliance requirements and operational needs to manage costs.
*   **Alarm Actions:** Define clear and actionable notifications for alarms. Use severity levels. Integrate with incident management tools.
*   **Dashboarding:** Create targeted dashboards for different services, applications, or operational views. Keep them clean and focused on key indicators.
*   **Regular Review:** Periodically review metrics, logs, alarms, and dashboards to ensure they are still relevant and effective.

*(Choose and combine these patterns based on the specific needs of the application and infrastructure.)*