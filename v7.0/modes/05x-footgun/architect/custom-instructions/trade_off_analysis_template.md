# Trade-Off Analysis Template

Use this template to structure the analysis of trade-offs between different architectural options or technology choices.

## 1. Problem / Decision Context

*   **What decision needs to be made?** (e.g., Choice of database, API design approach, messaging queue technology)
*   **What are the key requirements or constraints driving this decision?** (Reference requirements docs, NFRs, ADRs if applicable)

## 2. Options Considered

List the viable options being compared.

*   **Option A:** [Name/Description, e.g., PostgreSQL Database]
*   **Option B:** [Name/Description, e.g., MongoDB Database]
*   **Option C:** [Name/Description, e.g., Serverless Database (DynamoDB)]
*   *(Add more options as needed)*

## 3. Evaluation Criteria

List the criteria used for comparison. These should align with the `technology_evaluation_framework.md` and project priorities.

*   Criterion 1: (e.g., Performance - Latency)
*   Criterion 2: (e.g., Scalability - Horizontal Scaling Ease)
*   Criterion 3: (e.g., Development Cost/Effort)
*   Criterion 4: (e.g., Operational Complexity)
*   Criterion 5: (e.g., Security Features)
*   Criterion 6: (e.g., Team Familiarity)
*   ... *(Add/remove criteria as relevant)*

## 4. Comparison / Analysis

Evaluate each option against the criteria. Use tables, bullet points, or prose as appropriate. Be objective and quantify where possible.

**Example Table:**

| Criterion                  | Option A (PostgreSQL) | Option B (MongoDB) | Option C (DynamoDB) |
| :------------------------- | :-------------------- | :----------------- | :------------------ |
| Performance (Latency)    | Good (joins)          | Variable (depends) | Excellent (key-val) |
| Scalability (Horizontal) | Complex               | Good               | Excellent (managed) |
| Dev Cost/Effort          | Medium (ORM setup)    | Low (flexible)     | Medium (new paradigm) |
| Operational Complexity   | High (self-managed)   | Medium             | Low (serverless)    |
| Security Features        | Mature                | Good               | Excellent (IAM)     |
| Team Familiarity         | High                  | Medium             | Low                 |
| **...**                    | ...                   | ...                | ...                 |

**Narrative Analysis:**

*   **Option A:** Strengths lie in relational integrity and team familiarity, but scaling requires significant effort...
*   **Option B:** Offers flexibility and good horizontal scaling, but performance can be less predictable for complex queries...
*   **Option C:** Best-in-class scalability and low operational overhead, but requires adapting to a different data model and has potential vendor lock-in...

## 5. Recommendation

*   **Recommended Option:** [Option X]
*   **Justification:** Briefly summarize why this option is preferred based on the analysis and project priorities. Highlight the key trade-offs being accepted. (e.g., "Option C is recommended due to superior scalability and operational ease, accepting the trade-off of increased developer learning curve and potential vendor lock-in.")

## 6. Next Steps

*   Document decision in an ADR.
*   Create PoC if needed.
*   Update architecture diagrams.

*(This template provides structure. Adapt it based on the complexity of the decision.)*