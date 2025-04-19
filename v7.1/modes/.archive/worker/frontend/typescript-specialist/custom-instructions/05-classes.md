# TypeScript: Classes

Using classes with TypeScript for object-oriented programming patterns, including type annotations for members, constructors, methods, and access modifiers.

## Core Concept: Classes with Types

TypeScript extends JavaScript classes with features like explicit type annotations for members, constructors, and methods, as well as access modifiers (`public`, `private`, `protected`) and `readonly` properties.

## Basic Class Definition

```typescript
class Point {
  // Member properties with type annotations
  x: number;
  y: number;

  // Constructor with typed parameters
  constructor(x: number = 0, y: number = 0) {
    this.x = x;
    this.y = y;
  }

  // Method with typed parameters and return type
  distanceTo(other: Point): number {
    const dx = other.x - this.x;
    const dy = other.y - this.y;
    return Math.sqrt(dx * dx + dy * dy);
  }

  // Method with no return value
  log(): void {
    console.log(`Point(${this.x}, ${this.y})`);
  }
}

const p1 = new Point(10, 20);
const p2 = new Point(); // Uses default values (0, 0)
p1.log(); // Output: Point(10, 20)
console.log(p1.distanceTo(p2)); // Output: 22.36...
// p1.x = "ten"; // Error: Type 'string' is not assignable to type 'number'.
```

## Access Modifiers

*   **`public` (Default):** Members are accessible from anywhere. If no modifier is specified, it's public.
*   **`private`:** Members are only accessible from within the class itself. They are not accessible by instances or subclasses. (Note: This is enforced at compile time; JavaScript output doesn't have true private fields unless using `#` prefix - see below).
*   **`protected`:** Members are accessible from within the class and any subclasses that inherit from it, but not from instances outside the class hierarchy.

```typescript
class Animal {
  protected name: string; // Accessible by Animal and Dog
  private age: number;   // Only accessible within Animal

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  public move(distance: number): void { // public is explicit but default
    console.log(`${this.name} moved ${distance}m. Age: ${this.getAgeSuffix()}`);
  }

  private getAgeSuffix(): string { // Only callable inside Animal
      return `(${this.age} yrs)`;
  }
}

class Dog extends Animal {
  constructor(name: string, age: number) {
    super(name, age);
  }

  bark(): void {
    console.log(`Woof! My name is ${this.name}.`); // Can access protected 'name'
    // console.log(this.age); // Error: Property 'age' is private...
  }
}

const dog = new Dog("Buddy", 5);
dog.move(10); // OK
dog.bark();   // OK
// console.log(dog.name); // Error: Property 'name' is protected...
// console.log(dog.age);  // Error: Property 'age' is private...
```

## Parameter Properties

A shorthand way to declare and initialize class members directly in the constructor signature using access modifiers.

```typescript
class Car {
  // Shorthand: declares and initializes 'make' and 'model'
  constructor(public make: string, public model: string, private year: number) {}

  display(): void {
    console.log(`Car: ${this.make} ${this.model} (${this.year})`);
    // console.log(this.year); // OK - accessible within the class
  }
}

const myCar = new Car("Toyota", "Camry", 2021);
console.log(myCar.make); // OK
// console.log(myCar.year); // Error: Property 'year' is private...
myCar.display();
```

## Readonly Modifier

Prevents a property from being reassigned after it's initialized (usually in the constructor).

```typescript
class Circle {
  readonly radius: number;
  readonly id: string = crypto.randomUUID(); // Can initialize here

  constructor(radius: number) {
    this.radius = radius; // Can only assign in constructor or at declaration
  }

  grow() {
    // this.radius = this.radius * 2; // Error: Cannot assign to 'radius' because it is a read-only property.
  }
}
```

## Getters / Setters

Control access to properties using accessor methods.

```typescript
class Employee {
  private _fullName: string = "";

  get fullName(): string {
    return this._fullName;
  }

  set fullName(newName: string) {
    if (newName && newName.length > 0) {
      this._fullName = newName;
    } else {
      console.error("Name cannot be empty.");
    }
  }
}

const emp = new Employee();
emp.fullName = "Jane Doe"; // Uses the setter
console.log(emp.fullName); // Uses the getter
emp.fullName = ""; // Logs error via setter
```

## Static Members

Properties or methods that belong to the class itself, not to instances. Accessed using `ClassName.memberName`.

```typescript
class MathHelper {
  static PI: number = 3.14159;

  static calculateCircumference(radius: number): number {
    return 2 * MathHelper.PI * radius;
  }
}

console.log(MathHelper.PI);
console.log(MathHelper.calculateCircumference(10));
```

## Abstract Classes

Classes that cannot be instantiated directly and may contain abstract methods (methods without implementation) that must be implemented by subclasses.

```typescript
abstract class Shape {
  abstract getArea(): number; // Must be implemented by subclasses

  logDescription(): void {
    console.log("This is a shape.");
  }
}

class Rectangle extends Shape {
  constructor(public width: number, public height: number) {
    super();
  }

  getArea(): number { // Implementation of abstract method
    return this.width * this.height;
  }
}

// const shape = new Shape(); // Error: Cannot create an instance of an abstract class.
const rect = new Rectangle(10, 5);
console.log(rect.getArea()); // Output: 50
rect.logDescription();
```

## Implementing Interfaces

Classes can guarantee they meet a specific contract by using the `implements` keyword with one or more interfaces. See `03-interfaces-vs-types.md`.

```typescript
interface Loggable {
  log(message: string): void;
}

class ConsoleLogger implements Loggable {
  log(message: string): void {
    console.log(`LOG: ${message}`);
  }
}

class FileLogger implements Loggable {
  log(message: string): void {
    // Simulate writing to a file
    console.log(`Writing to file: ${message}`);
  }
}
```

## Private Fields (`#`)

TypeScript also supports ECMAScript Private Fields using the `#` prefix. These provide *runtime* privacy, unlike `private` which is compile-time only.

```typescript
class Counter {
  #count: number = 0; // Runtime private field

  increment() {
    this.#count++;
  }

  getCount() {
    return this.#count;
  }
}
const c = new Counter();
c.increment();
console.log(c.getCount()); // Output: 1
// console.log(c.#count); // SyntaxError: Private field '#count' must be declared in an enclosing class
```

TypeScript enhances JavaScript classes with robust typing and access control features, making object-oriented patterns safer and more maintainable.

*(Refer to the official TypeScript documentation on Classes.)*