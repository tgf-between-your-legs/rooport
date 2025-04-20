# Diagram Style Guide

Guidelines for creating consistent and readable Mermaid diagrams within this project.

## General Principles

*   **Clarity:** Diagrams should be easy to understand at a glance. Avoid excessive complexity or clutter.
*   **Consistency:** Use consistent naming conventions, shapes, and colors across related diagrams.
*   **Purpose:** Each diagram should have a clear purpose and title.
*   **Accuracy:** Diagrams should accurately reflect the system or process they represent (based on the provided conceptual description).

## Naming Conventions

*   **Nodes/Participants/Entities:** Use clear, concise names. Prefer PascalCase for components/classes/systems (e.g., `AuthService`, `UserProfile`) and camelCase or snake_case for variables/functions/actors (e.g., `getUserData`, `adminUser`).
*   **Relationships/Messages:** Use descriptive verb phrases (e.g., `places order`, `sends request`, `updates record`).

## Shapes & Styles (Flowchart/Graph)

*   **Processes/Actions:** Use rectangles `[ ]`.
*   **Decisions:** Use diamonds `{ }`.
*   **Start/End:** Use circles `(( ))`.
*   **Data/Input/Output:** Use asymmetric shapes `> ]`.
*   **External Systems:** Use rounded rectangles `( )`.
*   *(Define project-specific conventions if needed, e.g., specific shapes for APIs vs. Databases)*

## Colors (Optional)

*   Use color sparingly and consistently to highlight specific elements or categories if needed. Define the color scheme here.
    *   *Example:* Use specific `style` commands in Mermaid if a consistent theme is desired.
    ```mermaid
    %% Example style definition
    classDef default fill:#f9f,stroke:#333,stroke-width:2px;
    classDef special fill:#bbf,stroke:#333,stroke-width:4px;
    ```

## Layout

*   Prefer standard layouts (`TD`, `LR`) unless a different orientation significantly improves clarity.
*   Use subgraphs to group related components logically.
*   Keep link crossings to a minimum where possible.

## Specific Diagram Types

*   **Sequence Diagrams:** Clearly label participants. Use activation boxes (`activate`/`deactivate`) to show processing time. Keep messages concise.
*   **ER Diagrams:** Use standard cardinality notation (`||`, `|o`, `o{`, `|{`). Clearly label primary keys (PK) and foreign keys (FK).
*   **C4 Diagrams:** Adhere to C4 model conventions (Context, Containers, Components, Code). Use appropriate element types (`Person`, `System`, `Container`, `Component`, `System_Ext`, etc.).

*(This guide should be updated as project standards evolve.)*