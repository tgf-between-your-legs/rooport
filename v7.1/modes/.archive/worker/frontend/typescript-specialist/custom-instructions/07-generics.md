# TypeScript: Generics (`<T>`)

Creating reusable components, functions, and types that can work with multiple types using Generics.

## Core Concept: Type Variables

Generics allow you to write code that can operate on a variety of types rather than being restricted to a single one. You define a **type variable** (conventionally `<T>`, but can be any valid name like `<Type>`, `<TInput>`) that acts as a placeholder for a specific type that will be provided when the generic code is used.

**Benefits:**

*   **Reusability:** Write functions, classes, or types once that work for multiple input/output types.
*   **Type Safety:** Maintain type checking even when working with different types. The relationship between input and output types is preserved.
*   **Flexibility:** Allows consumers of your generic code to specify the exact types they want to use.

## Generic Functions

Define a type variable in angle brackets `<>` before the function's parameter list. Use the type variable to type parameters and return values.

```typescript
// Identity function - returns whatever is passed in
function identity<T>(arg: T): T {
  return arg;
}

// Usage:
let outputString = identity<string>("myString"); // Explicitly set T = string
let outputNumber = identity(123); // Type T inferred as number

// Generic function to get the first element of an array
function getFirstElement<ElementType>(arr: ElementType[]): ElementType | undefined {
  return arr[0];
}

const numbers = [1, 2, 3];
const firstNum = getFirstElement(numbers); // Type inferred as number | undefined

const strings = ["a", "b", "c"];
const firstStr = getFirstElement(strings); // Type inferred as string | undefined
```

## Generic Interfaces & Type Aliases

Define type variables after the interface/type name.

```typescript
// Generic Interface for a container
interface Box<T> {
  contents: T;
}

let stringBox: Box<string> = { contents: "hello" };
let numberBox: Box<number> = { contents: 100 };

// Generic Type Alias for a pair
type Pair<T, U> = {
  first: T;
  second: U;
};

let nameAndAge: Pair<string, number> = { first: "Alice", second: 30 };
let idAndStatus: Pair<number, boolean> = { first: 123, second: true };
```

## Generic Classes

Define type variables after the class name.

```typescript
class DataStorage<T> {
  private data: T[] = [];

  addItem(item: T): void {
    this.data.push(item);
  }

  getItem(index: number): T | undefined {
    return this.data[index];
  }

  getAll(): T[] {
    return [...this.data];
  }
}

// Store strings
const stringStorage = new DataStorage<string>();
stringStorage.addItem("Apple");
stringStorage.addItem("Banana");
console.log(stringStorage.getAll()); // Output: ["Apple", "Banana"]
// stringStorage.addItem(123); // Error

// Store numbers
const numberStorage = new DataStorage<number>();
numberStorage.addItem(1);
numberStorage.addItem(2);
console.log(numberStorage.getAll()); // Output: [1, 2]
```

## Generic Constraints (`extends`)

You can constrain the types that can be used for a type variable using the `extends` keyword. This ensures the type variable has certain properties or methods.

```typescript
interface Lengthwise {
  length: number; // Require the type to have a 'length' property
}

// This generic function only works with types that have a .length property
function logLength<T extends Lengthwise>(arg: T): void {
  console.log(arg.length);
}

logLength("hello"); // OK (string has length)
logLength([1, 2, 3]); // OK (array has length)
logLength({ length: 10, value: "abc" }); // OK (object has length property)
// logLength(123); // Error: Argument of type 'number' is not assignable to parameter of type 'Lengthwise'.
// logLength({ value: 10 }); // Error: Property 'length' is missing...
```

## Using Type Parameters in Generic Constraints

One type parameter can constrain another.

```typescript
// Get a property 'K' from an object 'T'
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

let user = { name: "Alice", age: 30 };
let userName = getProperty(user, "name"); // Type string inferred
let userAge = getProperty(user, "age");   // Type number inferred
// let userInvalid = getProperty(user, "location"); // Error: Argument of type '"location"' is not assignable...
```

Generics are a cornerstone of reusable, type-safe code in TypeScript. They allow you to create flexible functions, classes, and types that work consistently across different data types while still benefiting from static analysis.

*(Refer to the official TypeScript documentation on Generics.)*