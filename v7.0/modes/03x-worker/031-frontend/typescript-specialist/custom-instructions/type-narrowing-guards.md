# TypeScript: Type Narrowing & Type Guards

Techniques for working safely with variables that can hold multiple types (like unions or `unknown`).

## Core Concept: Type Narrowing

TypeScript's static analysis often needs help understanding the specific type of a variable within a certain code block, especially after conditional checks. Type narrowing is the process where TypeScript refines a broader type (like `string | number` or `unknown`) to a more specific type (like `string` or `number`) within a conditional block.

## Common Type Guards

TypeScript uses control flow analysis based on common JavaScript patterns to narrow types:

1.  **`typeof` Guard:** Checks for primitive types (`string`, `number`, `boolean`, `symbol`, `bigint`, `undefined`, `object`, `function`).
    ```typescript
    function processValue(value: string | number) {
      if (typeof value === 'string') {
        // Here, 'value' is known to be a string
        console.log(value.toUpperCase());
      } else {
        // Here, 'value' is known to be a number
        console.log(value.toFixed(2));
      }
    }
    ```

2.  **Truthiness Narrowing:** Checking if a value is "truthy" (not `null`, `undefined`, `false`, `0`, `NaN`, or `""`) can narrow away `null` and `undefined`.
    ```typescript
    function printLength(str: string | null | undefined) {
      if (str) { // Checks if str is not null or undefined (or empty string)
        // Here, 'str' is known to be a string
        console.log(str.length);
      } else {
        console.log("No string provided");
      }
    }
    ```

3.  **Equality Narrowing (`===`, `==`, `!==`, `!=`):** Comparing with specific literal values or `null`/`undefined`.
    ```typescript
    function handleInput(input: string | number | null) {
      if (input !== null) {
        // Here, 'input' is string | number
        if (input === "admin") {
          // Here, 'input' is "admin" (literal type)
          console.log("Welcome admin!");
        }
      }
    }
    ```

4.  **`instanceof` Guard:** Checks if a value is an instance of a specific class or constructor function.
    ```typescript
    class Fish { swim() { console.log("Swimming..."); } }
    class Bird { fly() { console.log("Flying..."); } }

    function move(pet: Fish | Bird) {
      if (pet instanceof Fish) {
        // Here, 'pet' is known to be Fish
        pet.swim();
      } else {
        // Here, 'pet' is known to be Bird
        pet.fly();
      }
    }
    ```

5.  **`in` Operator Guard:** Checks if an object has a property with a specific key. Useful for distinguishing between object shapes in a union.
    ```typescript
    interface Car { drive(): void; }
    interface Bike { pedal(): void; }

    function useVehicle(vehicle: Car | Bike) {
      if ('drive' in vehicle) {
        // Here, 'vehicle' is narrowed to Car
        vehicle.drive();
      } else {
        // Here, 'vehicle' is narrowed to Bike
        vehicle.pedal();
      }
    }
    ```

## Custom Type Guards (Type Predicates)

*   **Purpose:** Define your own function that performs a custom check and tells TypeScript whether a value is of a specific type.
*   **Syntax:** The function must return a **type predicate**: `parameterName is Type`.
    ```typescript
    interface Fish { swim(): void; }
    interface Bird { fly(): void; }

    // Custom type guard function
    function isFish(pet: Fish | Bird): pet is Fish {
      // Check if the 'swim' method exists on the object
      return (pet as Fish).swim !== undefined;
    }

    function movePet(pet: Fish | Bird) {
      if (isFish(pet)) {
        // Here, 'pet' is known to be Fish because isFish returned true
        pet.swim();
      } else {
        // Here, 'pet' is known to be Bird
        pet.fly();
      }
    }

    let myPet: Fish | Bird = Math.random() > 0.5 ? new Fish() : new Bird();
    movePet(myPet);
    ```

## Discriminated Unions

*   **Concept:** A powerful pattern for working with union types where each type in the union has a common **literal property** (the discriminant) that uniquely identifies it. TypeScript can narrow the type based on checking this discriminant property.
    ```typescript
    interface Square {
      kind: "square"; // Discriminant property
      size: number;
    }
    interface Rectangle {
      kind: "rectangle"; // Discriminant property
      width: number;
      height: number;
    }
    interface Circle {
      kind: "circle"; // Discriminant property
      radius: number;
    }

    type Shape = Square | Rectangle | Circle;

    function getArea(shape: Shape): number {
      switch (shape.kind) {
        case "square":
          // Here, 'shape' is known to be Square
          return shape.size * shape.size;
        case "rectangle":
          // Here, 'shape' is known to be Rectangle
          return shape.width * shape.height;
        case "circle":
          // Here, 'shape' is known to be Circle
          return Math.PI * shape.radius ** 2;
        default:
          // Exhaustiveness check: ensures all cases are handled
          const _exhaustiveCheck: never = shape;
          return _exhaustiveCheck;
      }
    }
    ```

## `unknown` vs `any`

*   **`any`:** Opts out of type checking. Avoid using it whenever possible.
*   **`unknown`:** Represents a value whose type is not known. It's type-safe because TypeScript forces you to perform checks (using type guards like `typeof`, `instanceof`, or custom guards) before you can operate on the value. **Prefer `unknown` over `any`** when dealing with values from external sources (APIs, user input).

*(Refer to the official TypeScript documentation on Type Narrowing: https://www.typescriptlang.org/docs/handbook/2/narrowing.html)*