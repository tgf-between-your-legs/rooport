# Mermaid Syntax Quick Reference

A quick guide to common Mermaid syntax elements for supported diagram types.

## General

*   Diagrams are defined within a Markdown code block:
    ```markdown
    ```mermaid
    [diagram type]
        [diagram definition]
    ```
    ```

## Flowchart / Graph (`graph`)

*   **Direction:** `TD` (Top-Down), `LR` (Left-Right), `BT`, `RL`.
    *   `graph TD;`
*   **Nodes:**
    *   `id[Label]` (Rectangle)
    *   `id(Label)` (Rounded Rectangle)
    *   `id((Label))` (Circle)
    *   `id{Label}` (Diamond)
    *   `id>Label]` (Asymmetric)
*   **Links:**
    *   `A --> B` (Arrow)
    *   `A --- B` (Line)
    *   `A -- Text --> B` (Arrow with text)
    *   `A ---|Text| B` (Line with text)
    *   `A -.-> B` (Dotted arrow)
*   **Subgraphs:**
    ```mermaid
    subgraph Subgraph Title
        Node1 --> Node2
    end
    ```

## Sequence Diagram (`sequenceDiagram`)

*   **Participants:** `participant Alias as Label` or `participant Name`
*   **Messages:**
    *   `A->>B: Message Text` (Solid line, arrow head)
    *   `A-->>B: Message Text` (Dashed line, arrow head)
    *   `A->B: Message Text` (Solid line, open arrow) - Use less often
    *   `A--X B: Message Text` (Dashed line, cross head) - Use less often
*   **Activations:** `activate Participant`, `deactivate Participant`
*   **Notes:** `Note right of A: Text`, `Note left of A: Text`, `Note over A,B: Text`
*   **Loops:** `loop Text ... end`
*   **Alt/Opt:** `alt Condition ... else ... end`, `opt Text ... end`

## ER Diagram (`erDiagram`)

*   **Entities:** `ENTITY_NAME { type attributeName PK/FK "comment" }`
    *   `CUSTOMER { string customerId PK "Unique ID" }`
*   **Relationships:** `ENTITY1 ||--|| ENTITY2 : label` (Cardinality: `|o` zero or one, `||` exactly one, `o{` zero or more, `|{` one or more)
    *   `CUSTOMER ||--|{ ORDER : places`

## C4 Context Diagram (`C4Context`)

*   **Elements:** `Person(alias, label, ?description)`, `System(alias, label, ?description, ?tags)`, `SystemDb(..)` , `SystemQueue(..)`, `System_Ext(..)`, `Boundary(alias, label, ?type, ?tags)`
*   **Relationships:** `Rel(fromAlias, toAlias, label, ?techn, ?tags, ?direction)`

## State Diagram (`stateDiagram-v2`)

*   **States:** `stateName`, `state "Description" as alias`
*   **Transitions:** `[*] --> State1`, `State1 --> State2 : Event / Action`
*   **Composite States:** `state StateName { ... }`
*   **Forks/Joins:** `state fork_state <<fork>>`, `state join_state <<join>>`
*   **Notes:** `note right of State1 : Text`

## Gantt Chart (`gantt`)

*   **Settings:** `dateFormat YYYY-MM-DD`, `title Title Text`
*   **Sections:** `section Section Name`
*   **Tasks:** `Task Name : [crit], [active], [id], [start_date/after id], [duration/end_date]`
    *   `Task 1 : a1, 2025-04-15, 7d`
    *   `Task 2 : crit, active, after a1, 5d`
*   **Milestones:** `Milestone Name : milestone, id, date`

*(Refer to the official Mermaid documentation for full syntax and advanced features: https://mermaid.js.org/)*