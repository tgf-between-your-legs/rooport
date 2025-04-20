# TypeScript: Enums

Creating named constant values using Enums.

## Core Concept: Named Constants

Enums (enumerations) allow you to define a set of named constants. They make code more readable and less error-prone by giving descriptive names to potentially magic numbers or strings.

## Numeric Enums

*   By default, enums are **numeric**. The first member gets the value `0`, and subsequent members increment automatically.
*   You can explicitly set the value of the first or any member, and subsequent members will increment from that point.
*   Numeric enums support **reverse mapping**: you can access the name of a member by its value.

```typescript
enum Direction {
  Up,    // 0
  Down,  // 1
  Left,  // 2
  Right, // 3
}

let move: Direction = Direction.Up;
console.log(move); // Output: 0

console.log(Direction[2]); // Output: "Left" (Reverse mapping)

enum StatusCodes {
  OK = 200,
  BadRequest = 400,
  Unauthorized, // 401 (increments from previous)
  NotFound,     // 402
}

let responseStatus: StatusCodes = StatusCodes.OK;
console.log(responseStatus); // Output: 200
console.log(StatusCodes[401]); // Output: "Unauthorized"
```

## String Enums

*   Each member must be explicitly initialized with a string literal (or another string enum member).
*   String enums offer better readability and debugging experience because the string value is often meaningful.
*   **No reverse mapping:** You cannot get the name of a member from its string value.

```typescript
enum LogLevel {
  Info = "INFO",
  Warning = "WARN",
  Error = "ERROR",
  Debug = "DEBUG",
}

let level: LogLevel = LogLevel.Warning;
console.log(level); // Output: "WARN"

function log(message: string, level: LogLevel): void {
  console.log(`[${level}] ${message}`);
}

log("User logged in", LogLevel.Info); // Output: [INFO] User logged in
// console.log(LogLevel["WARN"]); // Error: No reverse mapping for string enums
```

## Heterogeneous Enums (Avoid)

*   Technically possible to mix string and numeric members, but generally discouraged as it can be confusing.

```typescript
enum Mixed {
  A,         // 0
  B = "B",
  C = 10,
  D,         // 11
}
```

## Const Enums

*   Prefixing `enum` with `const` makes it a **const enum**.
*   **Compile-Time Only:** Const enums are completely erased during compilation. The compiler replaces usages of the enum members with their actual values (inlining).
*   **Benefits:** Results in potentially smaller JavaScript output as no enum object is generated.
*   **Limitations:** Cannot have computed members. No reverse mapping (even for numeric const enums). Cannot be iterated over at runtime.

```typescript
const enum Colors {
  Red = "#FF0000",
  Green = "#00FF00",
  Blue = "#0000FF",
}

let color: Colors = Colors.Red;
console.log(color); // In compiled JS, this might become console.log("#FF0000");

// console.log(Colors[0]); // Error: const enum members can only be accessed using a string literal.
// console.log(Colors["#FF0000"]); // Error: No reverse mapping
```

## When to Use Enums

*   Use enums when you have a small, fixed set of related constants where descriptive names improve clarity over literal values (e.g., status codes, directions, log levels, user roles).
*   Prefer **string enums** for better runtime debugging and readability unless you specifically need numeric values or reverse mapping.
*   Use **const enums** if you need the absolute minimum JavaScript output size and don't need runtime access to the enum object itself.

Enums provide a useful way to create named constants in TypeScript, enhancing code readability and maintainability.

*(Refer to the official TypeScript documentation on Enums.)*