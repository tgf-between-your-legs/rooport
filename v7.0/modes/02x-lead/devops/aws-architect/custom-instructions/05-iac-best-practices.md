# Infrastructure as Code (IaC) Best Practices (Terraform/CloudFormation)

This document outlines best practices for writing, managing, and deploying Infrastructure as Code, primarily focusing on Terraform and AWS CloudFormation.

## Core Principles

*   **Declarative Definition:** Define the desired state of your infrastructure, letting the IaC tool determine how to achieve it.
*   **Idempotency:** Ensure that applying the same configuration multiple times results in the same state without unintended side effects. IaC tools generally handle this, but custom scripts or provisioners need care.
*   **Version Control:** Store all IaC code in a version control system (e.g., Git) like application code.
*   **Modularity & Reusability:** Break down infrastructure into reusable components or modules.
*   **Testing:** Implement testing strategies to validate IaC code before deployment.
*   **Automation:** Automate the deployment process through CI/CD pipelines.
*   **Security:** Embed security considerations into IaC code and processes.

## Best Practices

### 1. Version Control (Git)

*   [ ] Store all IaC code (Terraform `.tf`, CloudFormation `.yaml`/`.json`, scripts, variable files) in Git.
*   [ ] Use meaningful commit messages describing the infrastructure changes.
*   [ ] Use branching strategies (e.g., Gitflow, GitHub Flow) to manage development, testing, and production environments.
*   [ ] Protect the main/production branch with code reviews and merge checks.

### 2. Modularity & Reusability

*   **Terraform:**
    *   [ ] Use Modules: Encapsulate related resources into reusable modules (e.g., VPC module, RDS module, EC2 instance module).
    *   [ ] Publish & Source Modules: Use module registries (public Terraform Registry, private registries) or Git repositories as module sources.
    *   [ ] Keep Modules Focused: Design modules with a clear purpose and limited scope. Avoid overly complex "god" modules.
    *   [ ] Use Input Variables & Outputs: Define clear interfaces for modules using input variables and expose necessary information via outputs.
*   **CloudFormation:**
    *   [ ] Use Nested Stacks: Break down large templates into smaller, reusable nested stacks.
    *   [ ] Use Cross-Stack References (`Export`/`Fn::ImportValue`): Share outputs (like VPC IDs, Subnet IDs) between stacks. Use with caution as it creates dependencies.
    *   [ ] Use Parameters & Outputs: Define parameters for customization and outputs to expose resource information.
    *   [ ] Consider Macros/Transforms (e.g., SAM, CDK): Use higher-level abstractions for specific use cases like serverless or complex logic.

### 3. State Management (Primarily Terraform)

*   [ ] **Use Remote State:** Store Terraform state files remotely (e.g., S3 backend with DynamoDB locking) rather than locally. This enables collaboration and prevents state loss.
*   [ ] **Enable State Locking:** Use mechanisms like DynamoDB to prevent concurrent state modifications, which can lead to corruption.
*   [ ] **Backup State Files:** Ensure the remote backend (e.g., S3 bucket) has versioning enabled.
*   [ ] **Minimize Blast Radius:** Use separate state files for different environments (dev, staging, prod) and potentially for different application components or regions to limit the impact of errors. Consider using Terraform Workspaces or directory structures for separation.
*   [ ] **Protect State:** Secure access to the state backend (e.g., restrict S3 bucket permissions, encrypt state). Avoid storing sensitive data directly in the state file (use sensitive variable flags or external secret managers).

### 4. Coding Standards & Style

*   [ ] **Consistent Formatting:** Use automated formatting tools (`terraform fmt`, linters for CloudFormation YAML/JSON).
*   [ ] **Naming Conventions:** Adopt consistent and descriptive names for resources, variables, outputs, and modules.
*   [ ] **Comments:** Add comments to explain complex logic, non-obvious configurations, or important decisions.
*   [ ] **Variable Definitions:** Provide descriptions and types for variables. Define sensible defaults where applicable. Use `variables.tf` (Terraform) or `Parameters` section (CloudFormation).
*   [ ] **Outputs:** Define descriptions for outputs. Use `outputs.tf` (Terraform) or `Outputs` section (CloudFormation).

### 5. Testing & Validation

*   [ ] **Static Analysis & Linting:**
    *   Terraform: `terraform validate`, `tflint`, `checkov`, `tfsec`.
    *   CloudFormation: `aws cloudformation validate-template`, `cfn-lint`, `checkov`.
*   [ ] **Plan/Change Set Review:**
    *   Terraform: Always run `terraform plan` and carefully review the proposed changes before applying.
    *   CloudFormation: Create and review Change Sets before executing them.
*   [ ] **Unit/Integration Testing (Advanced):**
    *   Terraform: Tools like `Terratest` allow writing automated tests in Go to provision real infrastructure, verify its configuration, and tear it down.
    *   CloudFormation: Less mature ecosystem, often involves custom scripts or frameworks like `TaskCat`.
*   [ ] **Policy as Code:** Use tools like Open Policy Agent (OPA) or Sentinel (Terraform Enterprise) to enforce organizational policies on IaC code.

### 6. CI/CD Automation

*   [ ] Integrate IaC deployment into CI/CD pipelines (e.g., AWS CodePipeline, Jenkins, GitLab CI, GitHub Actions).
*   [ ] Automate validation, linting, and plan/change set generation steps in the pipeline.
*   [ ] Implement manual approval steps in the pipeline before applying changes to production environments.
*   [ ] Manage environment-specific configurations (e.g., variable files, parameter files) securely within the pipeline.

### 7. Security

*   [ ] **Least Privilege:** Define IAM roles and policies for IaC tools and pipelines with the minimum necessary permissions.
*   [ ] **Secrets Management:** Avoid hardcoding secrets (passwords, API keys) in IaC code or state files. Use secret management tools (AWS Secrets Manager, Parameter Store, HashiCorp Vault) and reference secrets dynamically. Mark variables as sensitive.
*   [ ] **Security Scanning:** Integrate security scanning tools (`tfsec`, `checkov`, `cfn-nag`) into CI/CD pipelines to detect insecure configurations early.
*   [ ] **Review Security Groups/Firewalls:** Define network security rules within IaC code and review them carefully. Avoid overly permissive rules (e.g., `0.0.0.0/0`).
*   [ ] **Regular Audits:** Periodically review deployed infrastructure against the defined IaC state and security best practices.

## Basic Template Examples

*(Provide links or simple embedded examples of basic Terraform modules or CloudFormation templates for common resources like S3 buckets or EC2 instances, demonstrating structure and variable usage.)*

**Terraform Example (Conceptual S3 Bucket Module):**

```terraform
# modules/s3_bucket/variables.tf
variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}

variable "tags" {
  description = "Tags to apply to the bucket"
  type        = map(string)
  default     = {}
}

# modules/s3_bucket/main.tf
resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name
  # Add other configurations like versioning, logging, etc.
}

resource "aws_s3_bucket_public_access_block" "this" {
  bucket = aws_s3_bucket.this.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.this.id
  versioning_configuration {
    status = "Enabled"
  }
}

# modules/s3_bucket/outputs.tf
output "bucket_id" {
  description = "The name of the bucket"
  value       = aws_s3_bucket.this.id
}

output "bucket_arn" {
  description = "The ARN of the bucket"
  value       = aws_s3_bucket.this.arn
}

# Usage in root module:
# module "my_data_bucket" {
#   source      = "./modules/s3_bucket"
#   bucket_name = "my-unique-data-bucket-12345"
#   tags = {
#     Environment = "Production"
#     Project     = "DataPlatform"
#   }
# }
```

*(Adapt and expand these practices based on project complexity and team standards.)*