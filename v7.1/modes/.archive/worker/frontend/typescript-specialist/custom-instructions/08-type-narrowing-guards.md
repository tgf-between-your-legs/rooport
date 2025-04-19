# TypeScript: Type Narrowing & Guards

Safely working with variables that could be one of multiple types (like unions or `unknown`) using type guards.

## Core Concept: Reducing Type Possibilities

When a variable can hold values of different types (e.g., `string | number` or `unknown`), TypeScript needs a way to determine the *specific* type within a certain block of code to allow operations specific to that type. This process is called **narrowing**.

**Type Guards** are expressions that perform runtime checks, guaranteeing the type of a value within a conditional block (`if`, `switch`, etc.). TypeScript understands these checks and narrows the type accordingly within that block.

## Common Type Guards

1.  **`typeof` Guard:**
    *   Checks against JavaScript's primitive types: `"string"`, `"number"`, `"bigint"`, `"boolean"`, `"symbol"`, `"undefined"`, `"object"`, `"function"`.
    *   Useful for distinguishing primitives within a union.

    ```typescript
    function processInput(input: string | number | boolean): void {
      if (typeof input === "string") {
        // input is narrowed to 'string' here
        console.log(input.toUpperCase());
      } else if (typeof input === "number") {
        // input is narrowed to 'number' here
        console.log(input.toFixed(2));
      } else {
        // input is narrowed to 'boolean' here
        console.log(input ? "True" : "False");
      }
    }
    ```

2.  **Truthiness Narrowing:**
    *   Checking for truthy/falsy values (`if (value)`, `if (!value)`, `value && ...`, `value || ...`) can narrow away `null` and `undefined` (if `strictNullChecks` is enabled).

    ```typescript
    function printLength(str: string | null | undefined): void {
      if (str) { // Checks for null or undefined (and empty string, 0, false)
        // str is narrowed to 'string' here (assuming strictNullChecks)
        console.log(str.length);
      } else {
        console.log("No string provided.");
      }
    }
    ```

3.  **Equality Narrowing:**
    *   Using `===`, `!==`, `==`, `!=` to compare with literal values can narrow types.

    ```typescript
    function handleValue(value: string | number): void {
      if (value === "hello") {
        // value is narrowed to the literal type "hello" here
        console.log("Greeting received!");
      } else if (value !== 42) {
         // value is narrowed to string | number (but not 42)
         console.log("Not the answer.");
      }
    }
    ```

4.  **`instanceof` Guard:**
    *   Checks if a value is an instance of a specific class or constructor function.
    *   Useful for narrowing object types when working with classes.

    ```typescript
    class Fish { swim() { console.log("Swimming..."); } }
    class Bird { fly() { console.log("Flying..."); } }

    function move(animal: Fish | Bird): void {
      if (animal instanceof Fish) {
        // animal is narrowed to 'Fish' here
        animal.swim();
      } else {
        // animal is narrowed to 'Bird' here
        animal.fly();
      }
    }
    ```

5.  **`in` Operator Guard:**
    *   Checks if an object has a property with a specific key (string name).
    *   Useful for distinguishing between object types based on the presence of properties.

    ```typescript
    interface Car { drive(): void; wheels: number; }
    interface Bicycle { ride(): void; wheels: number; }

    function useVehicle(vehicle: Car | Bicycle): void {
      if ("drive" in vehicle) {
        // vehicle is narrowed to 'Car' here
        vehicle.drive();
      } else {
        // vehicle is narrowed to 'Bicycle' here
        vehicle.ride();
      }
      console.log(`Wheels: ${vehicle.wheels}`); // 'wheels' is common, accessible after narrowing
    }
    ```

6.  **Type Predicates (`is`):**
    *   User-defined functions that explicitly tell TypeScript whether a value is of a specific type.
    *   **Syntax:** `function name(arg: Type): arg is SpecificType { ... }`
    *   The function must return a boolean. If it returns `true`, TypeScript narrows the argument's type to `SpecificType` in the calling scope.

    ```typescript
    interface Cat { meow(): void; }
    interface Dog { bark(): void; }

    // Type predicate function
    function isCat(animal: Cat | Dog): animal is Cat {
      return (animal as Cat).meow !== undefined; // Check for a unique property/method
    }

    function makeSound(animal: Cat | Dog): void {
      if (isCat(animal)) {
        // animal is narrowed to 'Cat' here
        animal.meow();
      } else {
        // animal is narrowed to 'Dog' here
        animal.bark();
      }
    }
    ```

7.  **Discriminated Unions:**
    *   A pattern where objects in a union share a common property (the *discriminant*) with a literal type. Using `switch` or `if` statements on the discriminant property allows TypeScript to narrow the type effectively.

    ```typescript
    interface Square { kind: "square"; size: number; }
    interface Rectangle { kind: "rectangle"; width: number; height: number; }
    interface Circle { kind: "circle"; radius: number; }

    type Shape = Square | Rectangle | Circle;

    function getArea(shape: Shape): number {
      switch (shape.kind) {
        case "square":
          // shape is narrowed to 'Square' here
          return shape.size * shape.size;
        case "rectangle":
          // shape is narrowed to 'Rectangle' here
          return shape.width * shape.height;
        case "circle":
          // shape is narrowed to 'Circle' here
          return Math.PI * shape.radius ** 2;
        default:
          // Exhaustiveness check: ensures all cases are handled
          const _exhaustiveCheck: never = shape;
          return _exhaustiveCheck;
      }
    }
    ```

Type guards are essential for working safely with `unknown` types and unions, allowing TypeScript to understand the specific type of a value within certain code blocks and enabling access to type-specific properties and methods.

*(Refer to the official TypeScript documentation on Narrowing.)*