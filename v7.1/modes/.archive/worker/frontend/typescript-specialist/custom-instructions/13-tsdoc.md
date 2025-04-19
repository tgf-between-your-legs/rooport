# TypeScript: TSDoc Documentation Comments

Documenting TypeScript code using TSDoc comment syntax.

## Core Concept: Standardized Documentation

**TSDoc** is a specification for writing documentation comments for TypeScript code, similar to JSDoc for JavaScript. It defines a standard syntax using `/** ... */` block comments and tags (like `@param`, `@returns`, `@remarks`) to describe functions, classes, types, interfaces, and their members.

**Benefits:**

*   **Improved Code Understanding:** Makes it easier for developers (including future you) to understand what code does, its parameters, and what it returns.
*   **Editor Integration:** IDEs like VS Code use TSDoc comments to provide rich hover information, signature help, and autocompletion details.
*   **Documentation Generation:** Tools like TypeDoc can parse TSDoc comments to automatically generate API documentation websites or files.
*   **Standardization:** Provides a consistent way to document TypeScript code across projects and teams.

## Basic Syntax

TSDoc comments start with `/**` and end with `*/`. The main description comes first, followed by block tags starting with `@`.

```typescript
/**
 * Represents a point in 2D space.
 *
 * @remarks
 * This interface provides properties for x and y coordinates.
 * Use the `distanceTo` function to calculate distance between points.
 *
 * @public // Example TSDoc modifier tag (optional)
 */
interface Point {
  /**
   * The horizontal coordinate.
   */
  x: number;
  /**
   * The vertical coordinate.
   */
  y: number;
}

/**
 * Calculates the Euclidean distance between two points.
 *
 * @param p1 - The first point.
 * @param p2 - The second point.
 * @returns The distance between p1 and p2.
 *
 * @beta // Example TSDoc release stage tag (optional)
 */
function distanceTo(p1: Point, p2: Point): number {
  return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
}

/**
 * A class representing a Circle shape.
 */
class Circle {
  /**
   * The radius of the circle.
   * @readonly
   */
  readonly radius: number;

  /**
   * Creates a new Circle instance.
   * @param radius - The initial radius of the circle. Must be positive.
   */
  constructor(radius: number) {
    if (radius <= 0) {
      throw new Error("Radius must be positive.");
    }
    this.radius = radius;
  }

  /**
   * Calculates the area of the circle.
   * @returns The calculated area.
   * @example
   * ```typescript
   * const circle = new Circle(5);
   * const area = circle.getArea();
   * console.log(area); // Output: approx 78.54
   * ```
   */
  getArea(): number {
    return Math.PI * this.radius ** 2;
  }
}
```

## Common TSDoc Block Tags

*   **`@param <paramName> - <description>`:** Describes a function or method parameter.
*   **`@returns <description>`:** Describes the return value of a function or method.
*   **`@remarks <description>`:** Provides additional details or usage notes beyond the main summary.
*   **`@defaultValue <description>`:** Describes the default value of an optional parameter.
*   **`@throws <{ErrorType}> <description>`:** Documents errors that a function might throw.
*   **`@deprecated <description>`:** Marks an API item as deprecated, providing migration advice.
*   **`@see <reference>`:** Provides links or references to related items.
*   **`@example <description>`:** Provides a code example (often within a Markdown code block).
*   **Release Stage Tags:** `@alpha`, `@beta`, `@public`, `@internal` - Indicate the stability or intended audience of an API item.
*   **Modifier Tags:** `@readonly`, `@virtual`, `@override` - Describe characteristics of class members.

## Inline Tags (`{@tag ...}`)

Used within descriptions for linking or formatting.

*   **`{@link <reference>}`:** Creates a link to another documented API item, URL, or code element. Use `{@linkcode ...}` for code-style links.
    ```typescript
    /**
     * See {@link Point} for the data structure.
     * Learn more at {@link https://www.typescriptlang.org/}
     */
    ```
*   **`{@inheritDoc <reference>}`:** Inherits documentation from a base class/interface member.
*   **`{@label <text>}`:** (Less common) Used by documentation generators.

Writing clear TSDoc comments significantly improves the quality and usability of your TypeScript code, benefiting both human readers and tooling. Document exported functions, classes, interfaces, types, and complex properties.

*(Refer to the official TSDoc website and specification: https://tsdoc.org/)*