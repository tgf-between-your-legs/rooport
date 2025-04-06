TITLE: TypeScript Type Checking Example
DESCRIPTION: Shows how TypeScript catches spelling errors in property names during compilation through static type checking.

LANGUAGE: typescript
CODE:
const obj = { width: 10, height: 15 };
const area = obj.width * obj.heigth;

----------------------------------------

TITLE: Function Parameter Type Annotations in TypeScript
DESCRIPTION: Illustrates how to add type annotations to function parameters and return values.

LANGUAGE: typescript
CODE:
// Parameter type annotation
function greet(name: string) {
  console.log("Hello, " + name.toUpperCase() + "!!");
}

----------------------------------------

TITLE: Implementing a Generic Class in TypeScript
DESCRIPTION: Demonstrates the creation of a generic class that can work with different types of numeric values.

LANGUAGE: typescript
CODE:
class GenericNumber<NumType> {
  zeroValue: NumType;
  add: (x: NumType, y: NumType) => NumType;
}

----------------------------------------

TITLE: Using Generic Constraints in TypeScript
DESCRIPTION: Shows how to constrain generic types to those with specific properties using interfaces and the 'extends' keyword.

LANGUAGE: typescript
CODE:
interface Lengthwise {
  length: number;
}

function loggingIdentity<Type extends Lengthwise>(arg: Type): Type {
  console.log(arg.length);
  return arg;
}

----------------------------------------

TITLE: Implementing Accessors in TypeScript
DESCRIPTION: Shows how to use getters and setters to control access to class properties in TypeScript.

LANGUAGE: typescript
CODE:
const fullNameMaxLength = 10;

class Employee {
  private _fullName: string = "";

  get fullName(): string {
    return this._fullName;
  }

  set fullName(newName: string) {
    if (newName && newName.length > fullNameMaxLength) {
      throw new Error("fullName has a max length of " + fullNameMaxLength);
    }

    this._fullName = newName;
  }
}

let employee = new Employee();
employee.fullName = "Bob Smith";

if (employee.fullName) {
  console.log(employee.fullName);
}

----------------------------------------

TITLE: Tuple Types in TypeScript
DESCRIPTION: Shows how to define and use tuple types for fixed-length arrays with specific types at each index.

LANGUAGE: typescript
CODE:
type StringNumberPair = [string, number];

function doSomething(pair: [string, number]) {
  const a = pair[0];
  const b = pair[1];
  // ...
}

doSomething(["hello", 42]);

----------------------------------------

TITLE: Defining Basic Conditional Types in TypeScript
DESCRIPTION: Demonstrates the syntax and basic usage of conditional types in TypeScript, showing how types can be conditionally selected based on type relationships.

LANGUAGE: typescript
CODE:
interface Animal {
  live(): void;
}
interface Dog extends Animal {
  woof(): void;
}

type Example1 = Dog extends Animal ? number : string;

type Example2 = RegExp extends Animal ? number : string;

----------------------------------------

TITLE: Generics Implementation
DESCRIPTION: Shows how to use generics to create type-safe collections and interfaces with variable types.

LANGUAGE: typescript
CODE:
interface Backpack<Type> {
  add: (obj: Type) => void;
  get: () => Type;
}

----------------------------------------

TITLE: Object Types in TypeScript
DESCRIPTION: Demonstrates defining and using object types with properties and optional fields.

LANGUAGE: typescript
CODE:
// The parameter's type annotation is an object type
function printCoord(pt: { x: number; y: number }) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
printCoord({ x: 3, y: 7 });

----------------------------------------

TITLE: Implementing a Generic Identity Function in TypeScript
DESCRIPTION: Demonstrates how to create a generic identity function that works with any type, preserving type information.

LANGUAGE: typescript
CODE:
function identity<Type>(arg: Type): Type {
  return arg;
}

----------------------------------------

TITLE: Basic Interface Implementation in TypeScript
DESCRIPTION: Demonstrates a simple interface implementation for object type checking with a labeled object example.

LANGUAGE: typescript
CODE:
interface LabeledValue {
  label: string;
}

function printLabel(labeledObj: LabeledValue) {
  console.log(labeledObj.label);
}

let myObj = { size: 10, label: "Size 10 Object" };
printLabel(myObj);

----------------------------------------

TITLE: Array Type Declarations in TypeScript
DESCRIPTION: Shows two ways to declare array types: using square bracket notation and using generic Array type.

LANGUAGE: typescript
CODE:
let list: number[] = [1, 2, 3];

LANGUAGE: typescript
CODE:
let list: Array<number> = [1, 2, 3];

----------------------------------------

TITLE: Defining Callback Return Types in TypeScript
DESCRIPTION: Illustrates the proper way to define return types for callbacks in TypeScript, using 'void' instead of 'any' when the return value is ignored.

LANGUAGE: typescript
CODE:
/* WRONG */
function fn(x: () => any) {
  x();
}

LANGUAGE: typescript
CODE:
/* OK */
function fn(x: () => void) {
  x();
}

LANGUAGE: typescript
CODE:
function fn(x: () => void) {
  var k = x(); // oops! meant to do something else
  k.doSomething(); // error, but would be OK if the return type had been 'any'
}

----------------------------------------

TITLE: Function with Type Checking Example
DESCRIPTION: Shows how TypeScript can catch potential runtime errors through static type checking.

LANGUAGE: typescript
CODE:
function greet(person: string, date: Date) {
  console.log(`Hello ${person}, today is ${date.toDateString()}!`);
}

----------------------------------------

TITLE: Basic Type Inference in TypeScript
DESCRIPTION: Demonstrates how TypeScript infers the type of a variable from its initial value without an explicit type annotation.

LANGUAGE: typescript
CODE:
let x = 3;

----------------------------------------

TITLE: Implementing Generic Identity Function in TypeScript
DESCRIPTION: Demonstrates how to create a basic generic identity function that returns the input argument of any type.

LANGUAGE: typescript
CODE:
function identity<T>(arg: T): T {
  return arg;
}

----------------------------------------

TITLE: Creating Named Interfaces in TypeScript
DESCRIPTION: Shows how to define a named interface for an object type.

LANGUAGE: typescript
CODE:
interface Person {
  name: string;
  age: number;
}

function greet(person: Person) {
  return "Hello " + person.name;
}

----------------------------------------

TITLE: Type Inference Example
DESCRIPTION: Demonstrates TypeScript's ability to infer types without explicit annotations.

LANGUAGE: typescript
CODE:
let msg = "hello there!";

----------------------------------------

TITLE: Type Guards with In Operator
DESCRIPTION: Example showing how to use the 'in' operator as a type guard to narrow down union types

LANGUAGE: typescript
CODE:
function move(pet: Fish | Bird) {
  if ("swim" in pet) {
    return pet.swim();
  }
  return pet.fly();
}

----------------------------------------

TITLE: Type Annotations for Variables in TypeScript
DESCRIPTION: Shows how to explicitly annotate variable types in TypeScript using let, const, and var declarations.

LANGUAGE: typescript
CODE:
let myName: string = "Alice";
//        ^^^^^^^^ Type annotation

----------------------------------------

TITLE: Optional Properties in TypeScript Object Types
DESCRIPTION: Shows how to define optional properties in an interface using the question mark (?).

LANGUAGE: typescript
CODE:
interface PaintOptions {
  shape: Shape;
  xPos?: number;
  yPos?: number;
}

function paintShape(opts: PaintOptions) {
  // ...
}

----------------------------------------

TITLE: Generic Object Types in TypeScript
DESCRIPTION: Demonstrates how to create generic object types using type parameters.

LANGUAGE: typescript
CODE:
interface Box<Type> {
  contents: Type;
}

let box: Box<string>;

----------------------------------------

TITLE: Using Type Predicates for Custom Type Guards
DESCRIPTION: Demonstrates the use of type predicates to create custom type guards, allowing for more precise type narrowing in user-defined scenarios.

LANGUAGE: typescript
CODE:
type Fish = { swim: () => void };
type Bird = { fly: () => void };

function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}

let pet = getSmallPet();

if (isFish(pet)) {
  pet.swim();
} else {
  pet.fly();
}

----------------------------------------

TITLE: Implementing Generic Parameter Defaults in TypeScript
DESCRIPTION: Demonstrates how to use default type parameters in generic functions, making them optional to specify.

LANGUAGE: typescript
CODE:
declare function create<T extends HTMLElement = HTMLDivElement, U extends HTMLElement[] = T[]>(
  element?: T,
  children?: U
): Container<T, U>;

----------------------------------------

TITLE: Implementing Inheritance in TypeScript
DESCRIPTION: Shows how to create derived classes using inheritance in TypeScript, including method overriding.

LANGUAGE: typescript
CODE:
class Animal {
  name: string;
  constructor(theName: string) {
    this.name = theName;
  }
  move(distanceInMeters: number = 0) {
    console.log(`${this.name} moved ${distanceInMeters}m.`);
  }
}

class Snake extends Animal {
  constructor(name: string) {
    super(name);
  }
  move(distanceInMeters = 5) {
    console.log("Slithering...");
    super.move(distanceInMeters);
  }
}

class Horse extends Animal {
  constructor(name: string) {
    super(name);
  }
  move(distanceInMeters = 45) {
    console.log("Galloping...");
    super.move(distanceInMeters);
  }
}

let sam = new Snake("Sammy the Python");
let tom: Animal = new Horse("Tommy the Palomino");

sam.move();
tom.move(34);

----------------------------------------

TITLE: Basic Structural Typing in TypeScript
DESCRIPTION: Demonstrates how structural typing allows compatibility between a class and interface with matching members, even without explicit implementation.

LANGUAGE: typescript
CODE:
interface Pet {
  name: string;
}

class Dog {
  name: string;
}

let pet: Pet;
// OK, because of structural typing
pet = new Dog();

----------------------------------------

TITLE: Readonly Properties in TypeScript Interfaces
DESCRIPTION: Illustrates how to create immutable properties using the readonly modifier in interfaces.

LANGUAGE: typescript
CODE:
interface Point {
  readonly x: number;
  readonly y: number;
}

let p1: Point = { x: 10, y: 20 };
// p1.x = 5; // error!

----------------------------------------

TITLE: Using Generic Functions with Type Argument Inference in TypeScript
DESCRIPTION: Shows how to use a generic function with type argument inference, allowing the compiler to automatically determine the type based on the input.

LANGUAGE: typescript
CODE:
let output = identity("myString");
//       ^?

----------------------------------------

TITLE: Defining a Basic Class in TypeScript
DESCRIPTION: Demonstrates how to define a simple class with a constructor, property, and method in TypeScript.

LANGUAGE: typescript
CODE:
class Greeter {
  greeting: string;

  constructor(message: string) {
    this.greeting = message;
  }

  greet() {
    return "Hello, " + this.greeting;
  }
}

let greeter = new Greeter("world");

----------------------------------------

TITLE: Merging Interfaces in TypeScript
DESCRIPTION: Demonstrates how TypeScript merges multiple interface declarations with the same name into a single interface. This example shows merging of non-function and function members.

LANGUAGE: typescript
CODE:
interface Box {
  height: number;
  width: number;
}

interface Box {
  scale: number;
}

let box: Box = { height: 5, width: 6, scale: 10 };

----------------------------------------

TITLE: Generic Function Example
DESCRIPTION: Demonstrates generic function implementation with type parameters for type-safe array operations.

LANGUAGE: typescript
CODE:
function firstElement<Type>(arr: Type[]): Type | undefined {
  return arr[0];
}

// s is of type 'string'
const s = firstElement(["a", "b", "c"]);
// n is of type 'number'
const n = firstElement([1, 2, 3]);
// u is of type undefined
const u = firstElement([]);

----------------------------------------

TITLE: Using the any Type in TypeScript
DESCRIPTION: Demonstrates using the any type to disable type checking for a variable, allowing access to any properties or methods without compiler errors.

LANGUAGE: typescript
CODE:
let obj: any = { x: 0 };
// None of the following lines of code will throw compiler errors.
// Using `any` disables all further type checking, and it is assumed
// you know the environment better than TypeScript.
obj.foo();
obj();
obj.bar = 100;
obj = "hello";
const n: number = obj;

----------------------------------------

TITLE: Using Access Modifiers in TypeScript Classes
DESCRIPTION: Demonstrates the use of public, private, and protected access modifiers in TypeScript classes.

LANGUAGE: typescript
CODE:
class Animal {
  private name: string;
  constructor(theName: string) {
    this.name = theName;
  }
}

new Animal("Cat").name; // Error: 'name' is private

----------------------------------------

TITLE: Type Inference in TypeScript
DESCRIPTION: Demonstrates how TypeScript automatically infers types from variable assignments without explicit type declarations.

LANGUAGE: typescript
CODE:
let helloWorld = "Hello World";

----------------------------------------

TITLE: Implementing padLeft Function with Type Narrowing
DESCRIPTION: Demonstrates type narrowing using typeof checks to handle different padding types (number or string) in a padLeft function.

LANGUAGE: typescript
CODE:
function padLeft(padding: number | string, input: string): string {
  if (typeof padding === "number") {
    return " ".repeat(padding) + input;
  }
  return padding + input;
}

----------------------------------------

TITLE: Configuring TypeScript Strict Mode
DESCRIPTION: The 'strict' compiler flag enables comprehensive type checking behavior in TypeScript. When enabled, it activates all strict mode family options by default, though individual checks can be disabled as needed. Future TypeScript versions may add additional strict checks under this flag.

LANGUAGE: typescript
CODE:
{
  "compilerOptions": {
    "strict": true
  }
}

----------------------------------------

TITLE: Union Types
DESCRIPTION: Demonstrates the use of union types to allow multiple type possibilities for a single variable or parameter.

LANGUAGE: typescript
CODE:
function getLength(obj: string | string[]) {
  return obj.length;
}

----------------------------------------

TITLE: Defining Named and Anonymous Functions in TypeScript
DESCRIPTION: Demonstrates how to create named and anonymous functions in TypeScript, showing the basic syntax for function declarations.

LANGUAGE: typescript
CODE:
// Named function
function add(x, y) {
  return x + y;
}

// Anonymous function
let myAdd = function (x, y) {
  return x + y;
};

----------------------------------------

TITLE: Using Awaited Type in TypeScript
DESCRIPTION: Demonstrates the Awaited utility type for unwrapping Promise types recursively

LANGUAGE: typescript
CODE:
type A = Awaited<Promise<string>>;
type B = Awaited<Promise<Promise<number>>>;
type C = Awaited<boolean | Promise<number>>;

----------------------------------------

TITLE: ReadonlyArray Type in TypeScript
DESCRIPTION: Demonstrates the use of ReadonlyArray type for immutable arrays.

LANGUAGE: typescript
CODE:
function doStuff(values: ReadonlyArray<string>) {
  const copy = values.slice();
  console.log(`The first value is ${values[0]}`);
  // Error: Property 'push' does not exist on type 'readonly string[]'.
  // values.push("hello!");
}

----------------------------------------

TITLE: Mapped Types
DESCRIPTION: Example of creating new types by transforming properties of existing types

LANGUAGE: typescript
CODE:
type Partial<T> = {
  [P in keyof T]?: T[P];
};

type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

----------------------------------------

TITLE: Defining Anonymous Object Types in TypeScript
DESCRIPTION: Demonstrates how to define an anonymous object type inline within a function parameter.

LANGUAGE: typescript
CODE:
function greet(person: { name: string; age: number }) {
  return "Hello " + person.name;
}

----------------------------------------

TITLE: Using Conditional Types with Generics in TypeScript
DESCRIPTION: Shows how conditional types can be combined with generics to create flexible type definitions that adapt based on input types.

LANGUAGE: typescript
CODE:
type NameOrId<T extends number | string> = T extends number
  ? IdLabel
  : NameLabel;

function createLabel<T extends number | string>(idOrName: T): NameOrId<T> {
  throw "unimplemented";
}

let a = createLabel("typescript");
let b = createLabel(2.8);
let c = createLabel(Math.random() ? "hello" : 42);

----------------------------------------

TITLE: Applying Generic Constraints in TypeScript Functions
DESCRIPTION: Demonstrates how to use generic constraints to ensure that the type parameter has specific properties or methods.

LANGUAGE: typescript
CODE:
interface Lengthwise {
  length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
  console.log(arg.length);
  return arg;
}

----------------------------------------

TITLE: Handling union types in TypeScript
DESCRIPTION: Shows how to work with union types in TypeScript, including type narrowing using type predicates.

LANGUAGE: typescript
CODE:
function start(
  arg: string | string[] | (() => string) | { s: string }
): string {
  if (typeof arg === "string") {
    return commonCase(arg);
  } else if (Array.isArray(arg)) {
    return arg.map(commonCase).join(",");
  } else if (typeof arg === "function") {
    return commonCase(arg());
  } else {
    return commonCase(arg.s);
  }

  function commonCase(s: string): string {
    return s;
  }
}

----------------------------------------

TITLE: Access Modifiers Usage
DESCRIPTION: Shows how to use public, private and protected access modifiers on class members.

LANGUAGE: typescript
CODE:
class Greeter {
  public greet() {
    console.log("Hello, " + this.getName());
  }
  protected getName() {
    return "hi";
  }
}

----------------------------------------

TITLE: Defining a Generic Interface in TypeScript
DESCRIPTION: Illustrates how to create a generic interface that describes a function with a generic type parameter.

LANGUAGE: typescript
CODE:
interface GenericIdentityFn<Type> {
  (arg: Type): Type;
}

----------------------------------------

TITLE: Basic Mapped Type with Property Key Iteration
DESCRIPTION: Shows how to create a mapped type that transforms all properties of an input type to boolean values

LANGUAGE: typescript
CODE:
type OptionsFlags<Type> = {
  [Property in keyof Type]: boolean;
};

type Features = {
  darkMode: () => void;
  newUserProfile: () => void;
};

type FeatureOptions = OptionsFlags<Features>;

----------------------------------------

TITLE: Exhaustiveness Checking with never Type
DESCRIPTION: Demonstrates how to use the never type for exhaustiveness checking in switch statements, ensuring all cases of a discriminated union are handled.

LANGUAGE: typescript
CODE:
type Shape = Circle | Square;

function getArea(shape: Shape) {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.sideLength ** 2;
    default:
      const _exhaustiveCheck: never = shape;
      return _exhaustiveCheck;
  }
}

----------------------------------------

TITLE: Intersection Types with Error Handling
DESCRIPTION: Demonstrates how to combine multiple interfaces using intersection types to create new types with combined features. Shows practical usage with network response handling.

LANGUAGE: typescript
CODE:
interface ErrorHandling {
  success: boolean;
  error?: { message: string };
}

interface ArtworksData {
  artworks: { title: string }[];
}

interface ArtistsData {
  artists: { name: string }[];
}

type ArtworksResponse = ArtworksData & ErrorHandling;
type ArtistsResponse = ArtistsData & ErrorHandling;

----------------------------------------

TITLE: Class Fields with Type Annotations
DESCRIPTION: Shows how to declare class fields with type annotations and initialization.

LANGUAGE: typescript
CODE:
class Point {
  x: number;
  y: number;
}

const pt = new Point();
pt.x = 0;
pt.y = 0;

----------------------------------------

TITLE: Defining Full Function Types in TypeScript
DESCRIPTION: Illustrates how to write out the complete type of a function, including parameter types and return type, using arrow notation.

LANGUAGE: typescript
CODE:
let myAdd: (x: number, y: number) => number = function (
  x: number,
  y: number
): number {
  return x + y;
};

----------------------------------------

TITLE: Merging Namespaces with Classes in TypeScript
DESCRIPTION: Shows how TypeScript allows merging namespaces with classes to create inner classes or add static members to existing classes. The namespace declaration must follow the class declaration it will merge with.

LANGUAGE: typescript
CODE:
class Album {
  label: Album.AlbumLabel;
}
namespace Album {
  export class AlbumLabel {}
}

----------------------------------------

TITLE: Using the TypeScript CLI (tsc)
DESCRIPTION: Examples of how to use the TypeScript compiler CLI (tsc) for various compilation scenarios, including project-based compilation, single file compilation, and using specific compiler options.

LANGUAGE: sh
CODE:
# Run a compile based on a backwards look through the fs for a tsconfig.json
tsc

# Emit JS for just the index.ts with the compiler defaults
tsc index.ts

# Emit JS for any .ts files in the folder src, with the default settings
tsc src/*.ts

# Emit files referenced in with the compiler settings from tsconfig.production.json
tsc --project tsconfig.production.json

# Emit d.ts files for a js file with showing compiler options which are booleans
tsc index.js --declaration --emitDeclarationOnly

# Emit a single .js file from two files via compiler options which take string arguments
tsc app.ts util.ts --target esnext --outfile index.js

----------------------------------------

TITLE: Basic Union Type Example with padLeft Function
DESCRIPTION: Demonstrates how to use union types to accept multiple parameter types. The function accepts either a number or string for padding and applies it accordingly.

LANGUAGE: typescript
CODE:
function padLeft(value: string, padding: string | number) {
  if (typeof padding === "number") {
    return Array(padding + 1).join(" ") + value;
  }
  if (typeof padding === "string") {
    return padding + value;
  }
  throw new Error(`Expected string or number, got '${typeof padding}'.`);
}

----------------------------------------

TITLE: Basic Template Literal Type Declaration
DESCRIPTION: Demonstrates how to create a simple template literal type by concatenating a string literal with a type variable.

LANGUAGE: typescript
CODE:
type World = "world";

type Greeting = `hello ${World}`;

----------------------------------------

TITLE: Type Exports in TypeScript
DESCRIPTION: Demonstrates exporting type definitions and interfaces.

LANGUAGE: typescript
CODE:
export type Cat = { breed: string; yearOfBirth: number };

export interface Dog {
  breeds: string[];
  yearOfBirth: number;
}

----------------------------------------

TITLE: Defining and Using the Omit Helper Type in TypeScript
DESCRIPTION: Demonstrates the usage of the new Omit helper type in TypeScript 3.5. It creates a new type by removing specified properties from an existing type.

LANGUAGE: typescript
CODE:
type Person = {
  name: string;
  age: number;
  location: string;
};

type QuantumPerson = Omit<Person, "location">;

// equivalent to
type QuantumPerson = {
  name: string;
  age: number;
};

----------------------------------------

TITLE: Complex Union Type Combinations
DESCRIPTION: Demonstrates how multiple union types are cross-multiplied in template literal interpolation positions.

LANGUAGE: typescript
CODE:
type EmailLocaleIDs = "welcome_email" | "email_heading";
type FooterLocaleIDs = "footer_title" | "footer_sendoff";
type AllLocaleIDs = `${EmailLocaleIDs | FooterLocaleIDs}_id`;
type Lang = "en" | "ja" | "pt";

type LocaleMessageIDs = `${Lang}_${AllLocaleIDs}`;

----------------------------------------

TITLE: Optional Properties in TypeScript Interfaces
DESCRIPTION: Shows how to define optional properties in interfaces using the question mark syntax and their implementation in a square creation function.

LANGUAGE: typescript
CODE:
interface SquareConfig {
  color?: string;
  width?: number;
}

function createSquare(config: SquareConfig): { color: string; area: number } {
  let newSquare = { color: "white", area: 100 };
  if (config.color) {
    newSquare.color = config.color;
  }
  if (config.width) {
    newSquare.area = config.width * config.width;
  }
  return newSquare;
}

let mySquare = createSquare({ color: "black" });

----------------------------------------

TITLE: React Component Type Definition
DESCRIPTION: Example of defining a React component with TypeScript, including props interface and proper type checking.

LANGUAGE: typescript
CODE:
interface Props {
  foo: string;
}

class MyComponent extends React.Component<Props, {}> {
  render() {
    return <span>{this.props.foo}</span>;
  }
}

<MyComponent foo="bar" />; // ok
<MyComponent foo={0} />; // error