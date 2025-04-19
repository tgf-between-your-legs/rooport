# TSDoc: Documenting TypeScript Code

Standard syntax for writing documentation comments in TypeScript code that can be understood by tools.

## Core Concept

TSDoc uses JSDoc-like syntax (`/** ... */`) with specific tags (`@param`, `@returns`, `@remarks`, `@defaultValue`, `@see`, `@example`, etc.) to document functions, classes, interfaces, types, and variables. This allows tools like IDEs (for IntelliSense) and documentation generators (like TypeDoc) to parse and display the documentation effectively.

## Basic Syntax

*   Use a multi-line comment starting with `/**` and ending with `*/`.
*   The first line (or paragraph) is the summary description.
*   Use block tags (like `@param`) starting on their own line.
*   Use inline tags (like `{@link}`) within description text.

```typescript
/**
 * Represents a user in the system.
 *
 * @remarks
 * This interface contains basic user information. Sensitive data is excluded.
 *
 * @public
 */
export interface User {
  /**
   * The unique identifier for the user.
   * @readonly
   */
  readonly id: number;

  /**
   * The user's full name.
   * @defaultValue 'Anonymous'
   */
  name: string;

  /**
   * Optional email address.
   */
  email?: string;
}

/**
 * Calculates the sum of two numbers.
 *
 * @param a - The first number. Must be a finite number.
 * @param b - The second number.
 * @returns The sum of `a` and `b`.
 *
 * @example
 * ```typescript
 * add(1, 2); // Returns 3
 * ```
 * @see {@link subtract} for the subtraction equivalent.
 */
export function add(a: number, b: number): number {
  if (!Number.isFinite(a) || !Number.isFinite(b)) {
    throw new Error("Inputs must be finite numbers.");
  }
  return a + b;
}

/**
 * A class representing a simple counter.
 * @beta
 */
export class Counter {
  /** @internal */
  private _count: number = 0;

  /**
   * Gets the current count.
   */
  get count(): number {
    return this._count;
  }

  /**
   * Increments the counter by the specified amount.
   * @param amount - The amount to increment by. Defaults to 1.
   */
  increment(amount: number = 1): void {
    this._count += amount;
  }
}
```

## Common Block Tags

*   **`@param {<type>} <name> - <description>`:** Describes a function or method parameter. Type is often optional if inferable from TS code.
*   **`@returns {<type>} <description>`:** Describes the return value of a function or method.
*   **`@remarks <description>`:** Provides additional detailed remarks beyond the summary.
*   **`@defaultValue <value>`:** Specifies the default value of a property or parameter.
*   **`@example <description>`:** Provides an example code snippet (often within a Markdown code block).
*   **`@see <reference>`:** Links to related items (e.g., `{@link otherFunction}`, `{@linkcode MyClass.method}`, URL).
*   **`@throws {<ErrorType>} <description>`:** Documents errors that a function/method might throw.
*   **`@deprecated <description>`:** Marks an API item as deprecated, providing migration advice.
*   **Modifier Tags:** Indicate status or access level (often interpreted by documentation tools):
    *   `@public` (Default)
    *   `@internal` (For internal use, might be hidden from public docs)
    *   `@alpha`, `@beta` (Release stage)
    *   `@virtual` (Indicates intended to be overridden)
    *   `@override` (Indicates it overrides a base class member)
    *   `@readonly` (For properties)

## Common Inline Tags

*   **`{@link <reference>}`:** Creates a link to another documented code element or URL. Use `{@linkcode ...}` for code-style links.
    ```typescript
    /**
     * See {@link MyClass} or {@linkcode add} for details.
     * Also check {@link https://www.typescriptlang.org/ | the TS website}.
     */
    ```
*   **`{@inheritDoc <reference>}`:** Inherits documentation from a base class/interface member (used with `@override`).

## Benefits

*   **IDE IntelliSense:** Provides rich tooltips and autocompletion hints directly in the editor.
*   **Documentation Generation:** Tools like TypeDoc can automatically generate HTML documentation websites from TSDoc comments.
*   **Code Clarity:** Improves understanding and maintainability of the codebase.

*(Refer to the official TSDoc specification: https://tsdoc.org/)*