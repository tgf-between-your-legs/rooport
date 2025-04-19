# TypeScript: Basic Types

Understanding TypeScript's fundamental static types for annotating JavaScript values.

## Core Concept: Static Typing

TypeScript adds optional static types to JavaScript. By annotating variables, function parameters, and return values with types, you tell the TypeScript compiler (`tsc`) what kind of value is expected. The compiler then checks your code for type errors *before* you run it, catching potential bugs early.

## Primitive Types

These correspond directly to JavaScript's primitive values:

*   **`string`**: Represents text values.
    ```typescript
    let message: string = "Hello, TypeScript!";
    // message = 123; // Error: Type 'number' is not assignable to type 'string'.
    ```
*   **`number`**: Represents all numbers (integers and floats).
    ```typescript
    let count: number = 42;
    let price: number = 99.95;
    // count = "forty-two"; // Error
    ```
*   **`boolean`**: Represents `true` or `false` values.
    ```typescript
    let isActive: boolean = true;
    // isActive = 0; // Error
    ```
*   **`null`**: Represents the intentional absence of a value. Requires `strictNullChecks` to be `false` in `tsconfig.json` to assign directly to other types, otherwise only assignable to `null` or `any`.
    ```typescript
    let data: null = null;
    // let name: string = null; // Error if strictNullChecks is true
    ```
*   **`undefined`**: Represents uninitialized values. Requires `strictNullChecks` to be `false` to assign directly to other types, otherwise only assignable to `undefined`, `void`, or `any`.
    ```typescript
    let notSet: undefined = undefined;
    // function log(msg: string) { ... }
    // log(undefined); // Error if strictNullChecks is true
    ```
*   **`symbol`**: Represents unique identifiers created via `Symbol()`.
    ```typescript
    const key: symbol = Symbol("uniqueId");
    ```
*   **`bigint`**: Represents integers larger than `2^53 - 1`. Created with the `n` suffix.
    ```typescript
    const largeNumber: bigint = 9007199254740991n;
    ```

## Arrays

Specify the type of elements an array holds:

*   **`Type[]`**: Syntax for an array of `Type`.
    ```typescript
    let numbers: number[] = [1, 2, 3];
    let names: string[] = ["Alice", "Bob"];
    // numbers.push("four"); // Error
    ```
*   **`Array<Type>`**: Generic array type syntax.
    ```typescript
    let flags: Array<boolean> = [true, false, true];
    ```

## Special Types

*   **`any`**: The "escape hatch". Represents any kind of value. Opts out of type checking for that value. **Avoid using `any` whenever possible**, as it defeats the purpose of TypeScript.
    ```typescript
    let looselyTyped: any = 4;
    looselyTyped = "Now I'm a string"; // No error
    looselyTyped.nonExistentMethod(); // No compile-time error, but will fail at runtime!
    ```
*   **`unknown`**: A type-safe alternative to `any`. Represents a value whose type is not known. You **must** perform type checks (narrowing) before operating on an `unknown` value. See `08-type-narrowing-guards.md`.
    ```typescript
    let maybeNumber: unknown = "123";
    // let num: number = maybeNumber; // Error: Type 'unknown' is not assignable to type 'number'.

    if (typeof maybeNumber === 'number') {
      let num: number = maybeNumber; // OK: Type narrowed to number inside block
    }
    if (typeof maybeNumber === 'string') {
        let num: number = parseInt(maybeNumber); // OK: Parse after checking it's a string
    }
    ```
*   **`void`**: Represents the absence of a return value, typically used for functions that don't explicitly return anything.
    ```typescript
    function logMessage(message: string): void {
      console.log(message);
      // No return statement (implicitly returns undefined)
    }
    ```
*   **`never`**: Represents values that should never occur. Used for functions that always throw an error or have an infinite loop.
    ```typescript
    function throwError(message: string): never {
      throw new Error(message);
    }
    function infiniteLoop(): never {
      while (true) {}
    }
    ```

## Type Inference

TypeScript can often infer the type of a variable from its initial value, so explicit type annotations aren't always necessary.

```typescript
let inferredString = "I am inferred as string"; // Type string inferred
let inferredNumber = 100; // Type number inferred
// inferredString = false; // Error
```

Using basic types is the foundation of TypeScript, allowing you to catch errors early and make your code more understandable and maintainable. Prefer explicit types when inference isn't clear or when defining function signatures and object shapes. Avoid `any`.

*(Refer to the official TypeScript documentation on Basic Types and Everyday Types.)*