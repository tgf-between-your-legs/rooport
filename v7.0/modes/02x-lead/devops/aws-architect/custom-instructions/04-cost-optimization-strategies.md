# AWS Cost Optimization Strategies Checklist &amp; Guide

This document provides strategies and a checklist for optimizing costs on AWS, aligning with the Cost Optimization pillar of the Well-Architected Framework.

## Core Principles

*   **Right-Sizing:** Match instance types and sizes to workload performance and capacity requirements. Avoid overprovisioning.
*   **Elasticity:** Scale resources up or down automatically based on demand (Auto Scaling). Turn off non-production resources when not in use.
*   **Pricing Models:** Leverage Savings Plans, Reserved Instances (RIs), and Spot Instances for significant discounts compared to On-Demand pricing.
*   **Storage Optimization:** Use appropriate S3 storage classes, implement lifecycle policies, and clean up unused EBS volumes/snapshots.
*   **Data Transfer:** Minimize data transfer costs between regions, AZs, and out to the internet. Use CloudFront CDN.
*   **Managed Services:** Utilize managed services (RDS, Lambda, Fargate) to reduce operational overhead and potentially lower TCO.
*   **Monitoring &amp; Governance:** Implement tagging, use AWS Cost Explorer, Budgets, and Cost Anomaly Detection to track spending and identify issues.

## Cost Optimization Checklist

### Compute (EC2, Lambda, Containers)

*   [ ] **Right-Size EC2 Instances:** Analyze utilization metrics (CPU, Memory, Network) using CloudWatch or AWS Compute Optimizer. Downsize or change instance families where appropriate.
*   [ ] **Utilize Auto Scaling:** Implement Auto Scaling groups to match capacity to demand dynamically.
*   [ ] **Leverage Spot Instances:** Use Spot Instances for fault-tolerant or stateless workloads for up to 90% savings (e.g., batch processing, dev/test). Use Spot Fleet or EC2 Fleet with diverse instance types.
*   [ ] **Purchase Savings Plans / Reserved Instances:** Commit to 1- or 3-year terms for consistent compute usage (EC2, Fargate, Lambda) to get significant discounts. Analyze usage patterns before committing.
*   [ ] **Stop/Terminate Unused Instances:** Identify and shut down or terminate idle EC2 instances, especially in non-production environments. Automate this process where possible.
*   [ ] **Optimize Lambda:** Right-size Lambda function memory (influences CPU allocation). Use Provisioned Concurrency for latency-sensitive functions if needed, but monitor costs. Use Graviton (ARM) for potential cost savings.
*   [ ] **Optimize Containers (ECS/EKS):** Right-size tasks/pods. Use Fargate for serverless or optimize EC2 instance selection for data plane. Use Cluster Auto Scaler (EKS) or Service Auto Scaling (ECS).

### Storage (S3, EBS, EFS)

*   [ ] **S3 Storage Classes:** Analyze access patterns using S3 Storage Lens or Analytics. Use S3 Intelligent-Tiering to automatically move data between tiers. Use Glacier/Deep Archive for long-term archival.
*   [ ] **S3 Lifecycle Policies:** Automate transitions between storage classes and expiration of objects.
*   [ ] **Delete Unused EBS Volumes:** Identify and delete detached or unutilized EBS volumes.
*   [ ] **Delete Old EBS Snapshots:** Implement a retention policy for snapshots and delete outdated ones. Consider Snapshot Lifecycle Policies.
*   [ ] **Optimize EBS Volume Type/Size:** Choose the most cost-effective volume type (e.g., gp3 vs. io2) based on performance needs. Avoid overprovisioning IOPS. Shrink volumes if possible (requires data migration).
*   [ ] **EFS Infrequent Access:** Use EFS Lifecycle Management to move infrequently accessed files to the lower-cost EFS IA storage class.

### Databases (RDS, DynamoDB, ElastiCache)

*   [ ] **Right-Size RDS Instances:** Monitor performance metrics and downsize instances if overprovisioned.
*   [ ] **Use RDS Reserved Instances:** Purchase RIs for stable database workloads.
*   [ ] **Stop RDS Instances (Non-Prod):** Stop non-production RDS instances when not in use (up to 7 days).
*   [ ] **DynamoDB Capacity Mode:** Choose On-Demand for unpredictable workloads or Provisioned Capacity (with Auto Scaling) for predictable workloads. Monitor consumed vs. provisioned capacity. Use Reserved Capacity for predictable provisioned throughput.
*   [ ] **DynamoDB TTL:** Use Time To Live (TTL) to automatically delete expired items.
*   [ ] **Right-Size ElastiCache Nodes:** Monitor cache utilization and resize nodes appropriately. Use Reserved Nodes.

### Networking & Content Delivery

*   [ ] **Optimize Data Transfer:**
    *   Use CloudFront CDN to cache content closer to users, reducing data transfer out costs.
    *   Keep traffic within the same AWS Region and AZ where possible.
    *   Compress data before transferring.
    *   Use VPC Endpoints (Gateway or Interface) to access AWS services privately without traversing the public internet or NAT Gateways.
*   [ ] **Review NAT Gateway Usage:** Ensure NAT Gateways are necessary. Use VPC Interface Endpoints where possible. Consolidate NAT Gateways if multiple VPCs need internet access (via Transit Gateway).
*   [ ] **Clean Up Unused Elastic IPs:** Detach and release Elastic IPs that are not associated with running resources (associated but stopped instances still incur charges).

### Monitoring & Governance

*   [ ] **Implement Tagging Strategy:** Tag resources consistently for cost allocation and tracking. Activate cost allocation tags.
*   [ ] **Use AWS Cost Explorer:** Regularly analyze spending patterns, identify cost drivers, and view recommendations.
*   [ ] **Set AWS Budgets:** Create budgets to track costs against thresholds and receive alerts.
*   [ ] **Enable AWS Cost Anomaly Detection:** Automatically detect unusual spending patterns.
*   [ ] **Review Trusted Advisor:** Check cost optimization recommendations in Trusted Advisor.
*   [ ] **Use AWS Compute Optimizer:** Get right-sizing recommendations for EC2, EBS, Lambda, and Auto Scaling Groups.

*(This is a starting point. Continuously monitor, analyze, and refine your cost optimization efforts.)*