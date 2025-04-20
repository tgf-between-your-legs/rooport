# TypeScript: Interfaces vs. Type Aliases

Defining object shapes and complex types using `interface` and `type`.

## Core Concept: Describing Shapes

Both `interface` and `type` (type alias) allow you to define the "shape" of an object or create names for other types. They are often interchangeable for basic object shapes, but have key differences in capabilities and common usage.

**1. `interface`:**

*   **Purpose:** Primarily used to declare the shape of an object. Can also describe function types.
*   **Syntax:**
    ```typescript
    interface Point {
      x: number;
      y: number;
      label?: string; // Optional property
      readonly id: string; // Readonly property
    }

    interface MoveFn {
      (distance: number): void;
    }
    ```
*   **Key Feature: Declaration Merging:** If you declare the same interface multiple times, TypeScript merges their definitions. This is useful for augmenting existing interfaces or for declaration files (`.d.ts`).
    ```typescript
    interface Box {
      width: number;
      height: number;
    }
    interface Box {
      scale: number;
    }
    // Effective Box: { width: number; height: number; scale: number; }
    ```
*   **Extending:** Use `extends` to inherit properties from other interfaces.
    ```typescript
    interface ColoredPoint extends Point {
      color: string;
    }
    ```
*   **Implementing:** Classes can `implement` interfaces to ensure they adhere to the shape.

**2. `type` (Type Alias):**

*   **Purpose:** Creates a new name (alias) for *any* type, including primitives, unions, intersections, tuples, and complex mapped/conditional types. Can also describe object shapes.
*   **Syntax:**
    ```typescript
    type ID = string | number; // Union type
    type PointTuple = [number, number]; // Tuple type
    type StringOrNumberArray = (string | number)[]; // Array of union
    type LockedState = { locked: true; value: string }; // Object shape
    type Callback = (e: Event) => void; // Function type

    // Can also describe object shapes, similar to interface
    type Vector2D = {
      x: number;
      y: number;
    };
    ```
*   **No Declaration Merging:** Type aliases cannot be redeclared to merge definitions. A type name must be unique within its scope.
*   **Intersections/Unions:** Use `&` (intersection) and `|` (union) to combine types. Intersections can mimic `extends` for object types.
    ```typescript
    type ColoredVector = Vector2D & {
      color: string;
    };
    ```
*   **Advanced Types:** Type aliases are necessary for defining more complex types using utility types, conditional types, mapped types, etc.

## When to Use Which?

*   **Use `interface` when:**
    *   Defining the shape of an object or class (the primary use case).
    *   You need declaration merging (e.g., augmenting global types, library definitions).
    *   You prefer the `extends` keyword for inheritance-like patterns.
*   **Use `type` when:**
    *   Defining aliases for primitive types, unions, intersections, or tuples.
    *   Defining complex types using conditional types, mapped types, template literal types, etc. (interfaces cannot represent these).
    *   You prefer using intersection types (`&`) for combining object shapes.

**Consistency is Key:** While often interchangeable for object shapes, choose one style (`interface` or `type`) for defining objects within your project and stick to it for consistency. Many prefer `interface` for object shapes due to its dedicated purpose and `extends` keyword, while using `type` for all other kinds of type definitions.

Both `interface` and `type` are powerful tools for defining the structure of your data and improving type safety in TypeScript.

*(Refer to the official TypeScript documentation on Interfaces, Type Aliases, and Differences Between Type Aliases and Interfaces.)*