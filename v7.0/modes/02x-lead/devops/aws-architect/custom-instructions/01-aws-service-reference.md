# AWS Service Quick Reference

This document provides a brief overview of core AWS services relevant to the AWS Architect role. For detailed information, always refer to the official AWS documentation.

## Compute

*   **EC2 (Elastic Compute Cloud):** Virtual servers in the cloud. Offers various instance types (general purpose, compute/memory/storage optimized, accelerated computing). Key features: AMIs, Security Groups, EBS Volumes, Auto Scaling, Load Balancing (ELB).
    *   *Use Cases:* Hosting applications, batch processing, development/testing environments.
*   **Lambda:** Serverless compute service. Run code without provisioning or managing servers. Pay only for compute time consumed. Triggered by events (API Gateway, S3, DynamoDB, etc.).
    *   *Use Cases:* Event-driven applications, APIs, data processing, automation tasks.
*   **ECS (Elastic Container Service):** Managed container orchestration service for Docker containers. Supports EC2 launch type (manage underlying EC2 instances) and Fargate launch type (serverless).
    *   *Use Cases:* Deploying, managing, and scaling containerized applications.
*   **EKS (Elastic Kubernetes Service):** Managed Kubernetes service. Run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane. Integrates with other AWS services.
    *   *Use Cases:* Running Kubernetes workloads, migrating existing Kubernetes applications.
*   **Fargate:** Serverless compute engine for containers (works with ECS and EKS). Removes the need to provision and manage servers for containers.
    *   *Use Cases:* Running containers without managing EC2 instances, simplifying container operations.

## Storage

*   **S3 (Simple Storage Service):** Object storage service. Highly scalable, durable, and available. Offers various storage classes (Standard, Intelligent-Tiering, Glacier, etc.) for different access patterns and cost needs.
    *   *Use Cases:* Data lakes, backups, static website hosting, application data storage.
*   **EBS (Elastic Block Store):** Block-level storage volumes for use with EC2 instances. Persistent storage, like virtual hard drives. Offers different volume types (gp3, io2, etc.) for performance needs.
    *   *Use Cases:* Boot volumes for EC2, database storage, high-performance application storage.
*   **EFS (Elastic File System):** Managed file storage service for EC2 instances. Provides scalable, shared file storage based on NFS protocol.
    *   *Use Cases:* Shared file systems for applications running on multiple EC2 instances, content management systems.

## Networking

*   **VPC (Virtual Private Cloud):** Logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network you define. Control over IP address range, subnets, route tables, and network gateways.
    *   *Use Cases:* Defining private network boundaries, securing resources, connecting to on-premises networks.
*   **Route 53:** Scalable Domain Name System (DNS) web service. Performs domain registration, DNS routing, and health checking.
    *   *Use Cases:* Domain management, routing traffic to AWS resources, health checks and failover.
*   **CloudFront:** Content Delivery Network (CDN) service. Delivers data, videos, applications, and APIs globally with low latency and high transfer speeds.
    *   *Use Cases:* Accelerating website/API delivery, caching content closer to users.
*   **ELB (Elastic Load Balancing):** Distributes incoming application traffic across multiple targets, such as EC2 instances, containers, and IP addresses. Types: Application Load Balancer (ALB), Network Load Balancer (NLB), Gateway Load Balancer (GWLB).
    *   *Use Cases:* High availability, fault tolerance, scaling applications.
*   **API Gateway:** Fully managed service for creating, publishing, maintaining, monitoring, and securing APIs at any scale. Acts as a front door for applications to access data, business logic, or functionality from backend services (Lambda, EC2, etc.).
    *   *Use Cases:* Building RESTful and WebSocket APIs, managing API lifecycle, securing API access.

## Databases

*   **RDS (Relational Database Service):** Managed relational database service. Supports various engines (PostgreSQL, MySQL, MariaDB, Oracle, SQL Server, Aurora). Handles patching, backups, scaling, high availability.
    *   *Use Cases:* Running relational databases without managing the underlying infrastructure.
*   **Aurora:** MySQL and PostgreSQL-compatible relational database built for the cloud. Offers higher performance and availability than standard MySQL/PostgreSQL on RDS.
    *   *Use Cases:* High-performance, high-availability relational database needs.
*   **DynamoDB:** Fully managed NoSQL key-value and document database. Delivers single-digit millisecond performance at any scale. Serverless.
    *   *Use Cases:* Applications requiring low-latency data access, serverless applications, scalable NoSQL workloads.
*   **ElastiCache:** Managed in-memory data store and cache service. Supports Redis and Memcached. Improves application performance by retrieving data from fast, managed, in-memory caches.
    *   *Use Cases:* Caching database queries, session management, real-time applications.

## Security, Identity, & Compliance

*   **IAM (Identity and Access Management):** Manage access to AWS services and resources securely. Create and manage users, groups, and roles, and use permissions to allow and deny access.
    *   *Use Cases:* Controlling user/service access, implementing least privilege.
*   **KMS (Key Management Service):** Managed service for creating and controlling encryption keys used to encrypt data. Integrates with many AWS services.
    *   *Use Cases:* Managing encryption keys, encrypting data at rest in S3, EBS, RDS, etc.
*   **WAF (Web Application Firewall):** Helps protect web applications or APIs against common web exploits that may affect availability, compromise security, or consume excessive resources.
    *   *Use Cases:* Filtering malicious traffic (SQL injection, XSS), rate limiting.
*   **Security Hub:** Provides a comprehensive view of your security state within AWS and helps check your environment against security industry standards and best practices.
    *   *Use Cases:* Centralized security posture management, compliance checking.
*   **GuardDuty:** Threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads.
    *   *Use Cases:* Detecting compromised instances, unusual API activity, potential threats.

## Monitoring & Logging

*   **CloudWatch:** Monitoring and observability service. Collects monitoring and operational data in the form of logs, metrics, and events. Provides visualization (dashboards) and alerting (alarms).
    *   *Use Cases:* Monitoring resource utilization, application performance, setting alarms, collecting logs.
*   **CloudTrail:** Records AWS API calls for your account and delivers log files. Enables governance, compliance, operational auditing, and risk auditing.
    *   *Use Cases:* Auditing API activity, tracking resource changes, security analysis.

*(This is not an exhaustive list. Refer to official AWS documentation for complete details.)*