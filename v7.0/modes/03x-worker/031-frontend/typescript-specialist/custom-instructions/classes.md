# TypeScript: Classes

Defining classes with type annotations for properties, methods, constructors, and access modifiers.

## Basic Class Definition

*   Use the `class` keyword.
*   Define properties with type annotations.
*   Define methods with parameter and return type annotations.
*   Use the `constructor` method for initialization.
*   Use `this` to access instance properties and methods.

```typescript
class Player {
  // Property type annotations
  name: string;
  score: number = 0; // Initial value
  readonly id: number; // Readonly property

  // Constructor with parameter properties shorthand
  constructor(name: string, public level: number = 1) { // 'public level' declares and initializes level property
    this.name = name;
    this.id = Math.random(); // Can only be assigned in constructor or at declaration
  }

  // Method type annotations
  increaseScore(points: number): void {
    this.score += points;
    console.log(`${this.name}'s score is now ${this.score}`);
  }

  getLevel(): number {
    return this.level;
  }
}

const player1 = new Player("Alice");
const player2 = new Player("Bob", 5);

player1.increaseScore(10); // Output: Alice's score is now 10
console.log(player2.getLevel()); // Output: 5
// player1.id = 123; // Error: Cannot assign to 'id' because it is a read-only property.
```

## Access Modifiers

*   **`public` (Default):** Members are accessible from anywhere.
*   **`private`:** Members are only accessible from within the defining class. Cannot be accessed by instances or subclasses. (Uses `#` prefix in modern JS/TS for "hard" privacy).
*   **`protected`:** Members are accessible from within the defining class and by instances of subclasses. Cannot be accessed by instances directly from outside.

```typescript
class Character {
  public name: string; // Explicitly public (default)
  protected health: number = 100;
  #internalSecret: string = "shhh"; // Private field (JS syntax, preferred)
  private legacySecret: string = "old way"; // TS private modifier

  constructor(name: string) {
    this.name = name;
  }

  takeDamage(amount: number): void {
    this.health -= amount;
    console.log(`${this.name} took ${amount} damage. Health: ${this.health}`);
    // console.log(this.#internalSecret); // Accessible within the class
    // console.log(this.legacySecret); // Accessible within the class
  }

  getHealth(): number {
    return this.health; // Accessible within the class
  }
}

class Hero extends Character {
  heal(amount: number): void {
    this.health += amount; // Can access protected member 'health'
    console.log(`${this.name} healed ${amount}. Health: ${this.health}`);
    // console.log(this.#internalSecret); // Error: Property '#internalSecret' is not accessible outside class 'Character'
    // console.log(this.legacySecret); // Error: Property 'legacySecret' is private and only accessible within class 'Character'.
  }
}

const hero = new Hero("SuperRoo");
hero.takeDamage(20);
hero.heal(10);
console.log(hero.name); // OK
// console.log(hero.health); // Error: Property 'health' is protected and only accessible within class 'Character' and its subclasses.
// console.log(hero.#internalSecret); // Error
// console.log(hero.legacySecret); // Error
```

## Readonly Modifier

*   Properties marked `readonly` can only be assigned a value during initialization (at declaration or in the constructor).

## Inheritance (`extends`)

*   Classes can inherit properties and methods from a base (parent) class using `extends`.
*   Use `super()` in the constructor of the derived class to call the parent constructor.
*   Use `super.methodName()` to call methods from the parent class.

```typescript
class Animal {
  constructor(public name: string) {}
  move(distance: number = 0): void {
    console.log(`${this.name} moved ${distance}m.`);
  }
}

class Dog extends Animal {
  constructor(name: string, public breed: string) {
    super(name); // Call parent constructor
  }
  bark(): void {
    console.log("Woof! Woof!");
  }
  move(distance: number = 5): void { // Override parent method
    console.log("Running...");
    super.move(distance); // Call parent method
  }
}

const myDog = new Dog("Buddy", "Golden Retriever");
myDog.bark();
myDog.move(10);
```

## Implementing Interfaces (`implements`)

*   Classes can declare that they adhere to the shape of an `interface` using the `implements` keyword.
*   The class must then provide implementations for all members defined in the interface.
*   Note: `implements` only checks the instance side of the class, not the static side or constructor.

```typescript
interface ClockInterface {
  currentTime: Date;
  setTime(d: Date): void;
}

class Clock implements ClockInterface {
  currentTime: Date = new Date();
  setTime(d: Date): void {
    this.currentTime = d;
  }
  // Class can have additional members not in the interface
  constructor(h: number, m: number) {}
}
```

## Abstract Classes

*   Base classes from which other classes may be derived. Cannot be instantiated directly.
*   May contain abstract methods (declared without implementation) that *must* be implemented by derived classes.
*   Use the `abstract` keyword.

```typescript
abstract class Department {
  constructor(public name: string) {}

  printName(): void {
    console.log("Department name: " + this.name);
  }

  abstract printMeeting(): void; // Must be implemented by derived classes
}

class AccountingDepartment extends Department {
  constructor() {
    super("Accounting and Auditing"); // Call base constructor
  }

  printMeeting(): void {
    console.log("The Accounting Department meets each Monday at 10am.");
  }

  generateReports(): void { // Can add new methods
    console.log("Generating accounting reports...");
  }
}

// let department: Department; // OK to create a reference to an abstract type
// department = new Department(); // Error: Cannot create an instance of an abstract class.
let department: Department = new AccountingDepartment(); // OK
department.printName();
department.printMeeting();
// department.generateReports(); // Error: Property 'generateReports' does not exist on type 'Department'. (Need to cast or use the specific type)
(department as AccountingDepartment).generateReports(); // OK
```

*(Refer to the official TypeScript documentation on Classes: https://www.typescriptlang.org/docs/handbook/2/classes.html)*