# Common AWS Architecture Patterns

This document outlines several common architecture patterns used on AWS. These serve as starting points and should be adapted based on specific requirements.

## 1. Three-Tier Web Application

A classic pattern for web applications, separating presentation, application logic, and data storage.

*   **Presentation Tier (Web Tier):**
    *   **Route 53:** DNS resolution.
    *   **CloudFront:** CDN for caching static content and accelerating dynamic content.
    *   **WAF:** Protects against common web exploits.
    *   **ALB (Application Load Balancer):** Distributes traffic across web servers, handles SSL termination.
    *   **EC2 Auto Scaling Group:** Manages EC2 instances running the web server software (e.g., Nginx, Apache). Instances are placed in private subnets across multiple Availability Zones (AZs).
    *   **S3:** Stores static assets (CSS, JS, images).
*   **Application Tier (Logic Tier):**
    *   **EC2 Auto Scaling Group / ECS Fargate / Lambda:** Runs the backend application logic (e.g., Node.js, Python, Java). Placed in private subnets across multiple AZs.
    *   **Internal ALB/NLB (Optional):** If communication between web and app tiers needs load balancing.
    *   **API Gateway (Alternative):** Can replace EC2/ECS app tier for API-based backends, often paired with Lambda.
*   **Data Tier:**
    *   **RDS (e.g., Aurora, PostgreSQL, MySQL):** Managed relational database deployed in a Multi-AZ configuration for high availability. Placed in private database subnets.
    *   **DynamoDB (Alternative/Supplement):** Managed NoSQL database for specific use cases requiring high scalability and low latency.
    *   **ElastiCache (Optional):** In-memory cache (Redis/Memcached) to reduce database load and improve performance.

*Key Considerations:* Security Groups control traffic between tiers. NAT Gateways or VPC Endpoints allow outbound internet access from private subnets.

## 2. Serverless API Backend

Leverages managed services to build APIs without managing servers.

*   **Route 53:** DNS resolution.
*   **API Gateway:** Defines RESTful or WebSocket APIs, handles request/response mapping, authorization (e.g., Cognito, IAM, Lambda Authorizers), throttling, caching.
*   **Lambda:** Executes backend business logic triggered by API Gateway endpoints. Code written in supported runtimes (Node.js, Python, Java, etc.).
*   **DynamoDB:** Common choice for persistent data storage due to its scalability and integration with Lambda.
*   **IAM:** Defines permissions for Lambda functions to access other AWS services (e.g., DynamoDB tables).
*   **Cognito (Optional):** Managed user identity and authentication service.
*   **CloudWatch:** Monitors API Gateway metrics, Lambda execution logs, and performance.

*Key Considerations:* Pay-per-request pricing model. Handles scaling automatically. Potential for cold starts in Lambda. State management needs careful consideration.

## 3. Event-Driven Processing

Uses events to trigger decoupled services, often for asynchronous tasks or data processing pipelines.

*   **Event Source:**
    *   **S3:** Object creation/deletion events.
    *   **DynamoDB Streams:** Changes to items in a table.
    *   **SQS (Simple Queue Service):** Messages placed in a queue.
    *   **SNS (Simple Notification Service):** Messages published to a topic.
    *   **EventBridge (CloudWatch Events):** Custom events, scheduled events, events from AWS services or SaaS partners.
    *   **API Gateway:** API calls triggering events.
*   **Event Router/Bus (Optional but common):**
    *   **EventBridge:** Central event bus to route events from various sources to targets based on rules.
    *   **SNS:** Fan-out pattern, publishing a message to multiple SQS queues or Lambda functions.
*   **Event Processor:**
    *   **Lambda:** Functions triggered by events to perform processing logic.
    *   **ECS/Fargate Task:** Containerized task triggered to handle more intensive processing.
    *   **Step Functions:** Coordinate multiple steps in a workflow triggered by an event.
*   **Downstream Services:**
    *   **DynamoDB/RDS:** Storing processed data.
    *   **S3:** Storing results or artifacts.
    *   **SQS/SNS:** Sending notifications or triggering further downstream processes.

*Key Considerations:* Decoupled architecture improves resilience and scalability. Need to manage potential duplicate events or ordering issues depending on the services used.

## 4. Containerized Microservices (ECS/EKS)

Deploys applications as a collection of small, independent services running in containers.

*   **Route 53 / CloudFront / WAF / ALB:** Entry point, similar to the 3-tier application. ALB routes traffic to specific services based on path or host.
*   **ECS or EKS Cluster:** Manages the container orchestration.
    *   **Control Plane:** Managed by AWS (ECS Scheduler or EKS Control Plane).
    *   **Data Plane:** EC2 instances (managed node groups or self-managed) or Fargate (serverless).
*   **Service Discovery:** Mechanisms (e.g., ECS Service Discovery, Kubernetes Services, Cloud Map) allow services to find and communicate with each other.
*   **Container Registry (ECR):** Stores Docker container images.
*   **Individual Services:** Each microservice runs as an ECS Service or Kubernetes Deployment/StatefulSet, often with its own database (e.g., DynamoDB, RDS instance/schema).
*   **CI/CD Pipeline:** Automates building container images, running tests, and deploying updates to the cluster (e.g., CodePipeline, Jenkins, GitLab CI).
*   **Monitoring/Logging:** CloudWatch Container Insights, Prometheus/Grafana, distributed tracing (X-Ray).

*Key Considerations:* Complexity in managing inter-service communication, deployment strategies, and monitoring across multiple services. Enables independent scaling and deployment of services.

*(These patterns can be combined and modified. Always refer to AWS Architecture Center and specific service documentation for detailed guidance.)*