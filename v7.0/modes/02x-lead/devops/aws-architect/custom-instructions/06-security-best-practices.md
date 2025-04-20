# AWS Security Best Practices

This document outlines key security best practices for designing and managing infrastructure on AWS, aligning with the Security Pillar of the Well-Architected Framework.

## 1. Identity and Access Management (IAM)

*   **Principle of Least Privilege:** Grant only the permissions required to perform a task. Start with minimal permissions and grant more as needed. Avoid using the root user for daily tasks.
*   **Use Roles for AWS Services & Applications:** Grant permissions to AWS services (e.g., EC2, Lambda) and applications running on them using IAM Roles, not long-term access keys. EC2 Instance Profiles and Lambda Execution Roles are preferred.
*   **Use IAM Users for People, Groups for Management:** Create individual IAM users for people needing access. Assign users to Groups and apply permissions to Groups rather than individual users for easier management.
*   **Strong Password Policy:** Enforce strong password requirements for IAM users (length, complexity, rotation).
*   **Enable Multi-Factor Authentication (MFA):** Require MFA for the root user and all privileged IAM users. Encourage MFA for all users.
*   **Use Conditions in IAM Policies:** Refine permissions using condition keys (e.g., restrict actions based on source IP, time of day, required tags, MFA status).
*   **Regularly Review Permissions:** Periodically review IAM policies, roles, users, and groups. Remove unused credentials or excessive permissions using tools like IAM Access Analyzer.
*   **Credential Rotation:** Rotate access keys regularly for IAM users (if unavoidable) and programmatic access.

## 2. Network Security

*   **VPC Design:** Use Virtual Private Clouds (VPCs) to create logically isolated network environments.
*   **Subnet Strategy:** Use public subnets for internet-facing resources (e.g., load balancers) and private subnets for backend resources (e.g., application servers, databases).
*   **Security Groups (Stateful Firewall):** Act as a firewall for associated instances, controlling inbound and outbound traffic at the instance level. Apply least privilege – only open necessary ports to specific source IPs/Security Groups.
*   **Network Access Control Lists (NACLs) (Stateless Firewall):** Act as a firewall for associated subnets, controlling inbound and outbound traffic at the subnet level. Use as an additional layer of defense, but Security Groups are often sufficient and easier to manage.
*   **NAT Gateways/Instances:** Use NAT Gateways (managed) or NAT Instances in public subnets to allow instances in private subnets to initiate outbound internet traffic while preventing inbound connections.
*   **VPC Endpoints:** Use Interface Endpoints (PrivateLink) or Gateway Endpoints to privately connect your VPC to supported AWS services (e.g., S3, DynamoDB, KMS) without requiring internet access, NAT Gateways, or public IPs.
*   **AWS WAF:** Protect web applications from common exploits (SQL injection, XSS) by configuring rules on CloudFront distributions or Application Load Balancers.
*   **AWS Shield:** Provides DDoS protection. Shield Standard is enabled by default; Shield Advanced offers enhanced protection and support for applications on EC2, ELB, CloudFront, Route 53.

## 3. Data Protection

*   **Encryption at Rest:**
    *   **S3:** Enable Server-Side Encryption (SSE-S3, SSE-KMS, SSE-C) for buckets. Enforce encryption using bucket policies.
    *   **EBS:** Enable encryption by default for new EBS volumes. Encrypt existing volumes if necessary (requires snapshotting/copying).
    *   **RDS:** Enable encryption when creating database instances. Encrypt snapshots.
    *   **Use AWS KMS:** Manage encryption keys using KMS for centralized control and auditing. Use Customer Managed Keys (CMKs) for more control over key policy and rotation.
*   **Encryption in Transit:**
    *   **Use HTTPS/TLS:** Enforce HTTPS for connections to CloudFront, Load Balancers, API Gateway. Use ACM (AWS Certificate Manager) to provision and manage SSL/TLS certificates.
    *   **Encrypt Inter-Service Communication:** Ensure traffic between application components within your VPC is encrypted where necessary.
    *   **VPN/Direct Connect:** Encrypt traffic between on-premises networks and AWS VPCs.
*   **Data Classification:** Identify and classify sensitive data to apply appropriate security controls.
*   **Backups & Disaster Recovery:** Regularly back up data (e.g., EBS snapshots, RDS snapshots, S3 versioning/replication) and test recovery procedures.

## 4. Logging and Monitoring

*   **Enable CloudTrail:** Log all API activity across your AWS account. Ensure logs are delivered to an S3 bucket (preferably in a separate security account) and optionally CloudWatch Logs. Enable log file integrity validation.
*   **Enable VPC Flow Logs:** Capture information about IP traffic going to and from network interfaces in your VPC. Analyze for security threats or network issues.
*   **Centralize Logs:** Aggregate logs (CloudTrail, VPC Flow Logs, application logs, OS logs) into a central location (e.g., CloudWatch Logs, S3 via Kinesis Data Firehose, third-party SIEM).
*   **Configure CloudWatch Alarms:** Set alarms based on critical metrics (e.g., high CPU, failed authentications) and CloudTrail events (e.g., security group changes, root user login).
*   **Use AWS Security Hub:** Aggregate security findings from various AWS services (GuardDuty, Inspector, Macie, IAM Access Analyzer) and third-party products. Check against security standards (e.g., CIS AWS Foundations Benchmark).
*   **Enable GuardDuty:** Continuously monitor for malicious activity and unauthorized behavior using threat intelligence feeds and machine learning.
*   **Use AWS Config:** Record and evaluate the configurations of your AWS resources. Define rules to check for compliance against desired configurations (e.g., ensure EBS encryption is enabled).

## 5. Incident Response

*   **Prepare:** Have an incident response plan documented. Use IAM roles and permissions specifically for incident response tasks.
*   **Identify:** Use monitoring and alerting (CloudWatch, GuardDuty, Security Hub) to detect security events.
*   **Contain:** Isolate affected resources (e.g., modify security groups, detach instances from load balancers, revoke credentials).
*   **Eradicate:** Identify and remove the root cause of the incident.
*   **Recover:** Restore affected systems and data. Validate functionality.
*   **Post-Incident Activity:** Conduct a post-mortem, document lessons learned, and update security controls and response plans.

*(Always refer to the latest AWS security documentation and best practices guides.)*