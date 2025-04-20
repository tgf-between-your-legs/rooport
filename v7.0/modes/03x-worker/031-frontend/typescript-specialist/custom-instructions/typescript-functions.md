# TypeScript: Typing Functions

Defining types for function parameters, return values, and function signatures.

## Core Concept: Explicit Function Contracts

TypeScript allows you to explicitly define the types of data a function expects as input (parameters) and the type of data it will output (return value). This creates a clear contract for how the function should be used and helps catch errors related to incorrect arguments or unexpected return values.

## Typing Parameters and Return Values

*   **Parameter Types:** Add a colon (`:`) followed by the type after each parameter name.
*   **Return Type:** Add a colon (`:`) followed by the type after the parameter list `)`.
*   **Type Inference:** TypeScript can often infer the return type if it's not explicitly provided, but it's good practice to add it for clarity, especially for complex functions or exported functions.
*   **`void` Return Type:** Use `void` if the function doesn't return a value (or implicitly returns `undefined`).

```typescript
// Explicit parameter and return types
function add(a: number, b: number): number {
  return a + b;
}

// Return type inferred (still number)
function subtract(a: number, b: number) {
  return a - b;
}

// Optional parameters (?)
function greet(name: string, greeting?: string): string {
  return `${greeting ?? 'Hello'}, ${name}!`; // Use nullish coalescing for default
}

// Default parameters
function power(base: number, exponent: number = 2): number {
  return Math.pow(base, exponent);
}

// Void return type
function logMessage(message: string): void {
  console.log(message);
}

// Using object types for parameters
interface Point { x: number; y: number; }
function distance(p1: Point, p2: Point): number {
  return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
}

// Using rest parameters
function sum(...numbers: number[]): number {
  return numbers.reduce((total, current) => total + current, 0);
}

// Destructuring parameters with types
function processCoords({ x, y }: { x: number; y: number }): void {
  console.log(`X: ${x}, Y: ${y}`);
}
```

## Typing Function Expressions & Arrow Functions

The syntax is similar for function expressions and arrow functions.

```typescript
// Function Expression
const multiply = function(a: number, b: number): number {
  return a * b;
};

// Arrow Function (explicit return type)
const divide = (a: number, b: number): number => {
  if (b === 0) throw new Error("Cannot divide by zero");
  return a / b;
};

// Arrow Function (inferred return type)
const isEven = (num: number) => num % 2 === 0;

// Arrow function with object parameter
const printUser = (user: { name: string; age: number }): void => {
  console.log(`User: ${user.name}, Age: ${user.age}`);
};
```

## Function Type Expressions (Signatures)

You can define the *type* of a function separately using a type alias or interface. This is useful for callbacks or defining function contracts.

**Syntax:** `(param1: Type1, param2: Type2) => ReturnType`

```typescript
// Using a type alias
type MathOperation = (x: number, y: number) => number;

const addOp: MathOperation = (a, b) => a + b;
const subtractOp: MathOperation = (a, b) => a - b;

function calculate(a: number, b: number, operation: MathOperation): number {
  return operation(a, b);
}

console.log(calculate(10, 5, addOp)); // Output: 15
console.log(calculate(10, 5, subtractOp)); // Output: 5

// Using an interface (less common for simple function types, but possible)
interface StringFormatter {
  (input: string, uppercase: boolean): string;
}

const format: StringFormatter = (str, upper) => {
  return upper ? str.toUpperCase() : str.toLowerCase();
};
```

Typing functions clearly defines their expected inputs and outputs, significantly improving code reliability and making functions easier to use correctly.

*(Refer to the official TypeScript documentation on Function Types.)*