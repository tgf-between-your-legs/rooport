# Non-Functional Requirements (NFR) Checklist

This checklist serves as a prompt to consider common NFRs during architectural design. **For Footgun Architect mode, NFRs are only in scope if explicitly requested.** Use this list to identify potential areas requiring clarification if instructions seem incomplete.

## Performance
*   [ ] **Latency:** Target response times? (e.g., API calls < 200ms)
*   [ ] **Throughput:** Target requests per second/minute? (e.g., 1000 RPS)
*   [ ] **Resource Utilization:** Constraints on CPU, memory, network bandwidth?
*   [ ] **Load Handling:** Expected peak load vs. average load? Graceful degradation under load?

## Scalability
*   [ ] **Growth Projections:** Expected user/data growth over time? (e.g., 2x users in 1 year)
*   [ ] **Scaling Strategy:** Horizontal or vertical scaling preferred/required?
*   [ ] **Elasticity:** Ability to scale up/down automatically based on demand?
*   [ ] **Regional Needs:** Deployment in multiple geographic regions?

## Reliability & Availability
*   [ ] **Uptime Requirement:** Target availability? (e.g., 99.9%, 99.99%)
*   [ ] **Fault Tolerance:** Resilience to component failures? Redundancy requirements?
*   [ ] **Disaster Recovery:** Recovery Time Objective (RTO)? Recovery Point Objective (RPO)? Backup strategy?
*   [ ] **Monitoring & Alerting:** Requirements for system health monitoring and failure alerts?

## Security
*   [ ] **Authentication:** User/service authentication mechanisms?
*   [ ] **Authorization:** Access control model? Role-based access?
*   [ ] **Data Security:** Encryption at rest/in transit? Data privacy requirements (GDPR, CCPA)?
*   [ ] **Vulnerability Management:** Protection against common threats (OWASP Top 10)? Penetration testing requirements?
*   [ ] **Compliance:** Specific industry or regulatory compliance needs? (e.g., HIPAA, PCI-DSS)

## Maintainability
*   [ ] **Modularity:** Degree of coupling between components?
*   [ ] **Testability:** Ease of writing unit, integration, and end-to-end tests?
*   [ ] **Deployability:** Ease and frequency of deployments? CI/CD requirements? Rollback strategy?
*   [ ] **Code Quality:** Adherence to coding standards? Readability? Documentation requirements?

## Usability (Developer Experience)
*   [ ] **Learnability:** How easy is it for new developers to understand the architecture?
*   [ ] **Documentation:** Quality and completeness of architectural documentation?
*   [ ] **Tooling:** Availability of development and debugging tools?

## Other Considerations
*   [ ] **Cost:** Budget constraints for infrastructure, licensing, development?
*   [ ] **Interoperability:** Requirements to integrate with other systems?
*   [ ] **Legal/Regulatory:** Specific legal constraints?

*(This checklist is not exhaustive. Add or remove items based on project context. Remember to clarify scope with the orchestrator if NFRs seem relevant but are not explicitly mentioned in the task.)*