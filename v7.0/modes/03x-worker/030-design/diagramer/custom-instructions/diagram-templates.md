# Mermaid Diagram Templates

Common starting points for various diagram types.

## Flowchart / Graph

```mermaid
graph TD;
    A[Start] --> B(Process 1);
    B --> C{Decision};
    C -- Yes --> D[Process 2a];
    C -- No --> E[Process 2b];
    D --> F((End));
    E --> F;
```

## Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    User->>Frontend: Perform Action
    activate Frontend
    Frontend->>Backend: API Request
    activate Backend
    Backend-->>Frontend: API Response
    deactivate Backend
    Frontend-->>User: Update UI
    deactivate Frontend
```

## Entity Relationship Diagram (ERD)

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    PRODUCT ||--|{ LINE-ITEM : includes

    CUSTOMER {
        string customerId PK
        string name
        string email
    }
    ORDER {
        string orderId PK
        datetime date
        string customerId FK
    }
    LINE-ITEM {
        string orderId PK, FK
        string productId PK, FK
        int quantity
    }
    PRODUCT {
        string productId PK
        string name
        float price
    }
```

## C4 Context Diagram

```mermaid
C4Context
  title System Context diagram for Example System

  Person(user, "User", "A user of the system")
  System(exampleSystem, "Example System", "The system being described")
  System_Ext(emailSystem, "Email System", "External email service")

  Rel(user, exampleSystem, "Uses")
  Rel(exampleSystem, emailSystem, "Sends emails using")
```

## State Diagram

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : Event Triggered
    Processing --> Idle : Success
    Processing --> Error : Failure
    Error --> Idle : Resolved
```

## Gantt Chart

```mermaid
gantt
    dateFormat  YYYY-MM-DD
    title Project Timeline Example
    section Phase 1
    Task 1           :a1, 2025-04-15, 7d
    Task 2           :after a1  , 5d
    section Phase 2
    Milestone        :milestone, m1, 2025-05-01
    Task 3           :after m1  , 10d
```

*(Use these as starting points and adapt based on specific requirements.)*