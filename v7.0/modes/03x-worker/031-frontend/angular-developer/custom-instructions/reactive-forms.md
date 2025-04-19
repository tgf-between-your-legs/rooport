# Angular: Reactive Forms

Building and validating complex forms using Angular's Reactive Forms module.

## Core Concept

Reactive Forms provide a model-driven approach to handling form inputs where the form model (structure and validation rules) is defined explicitly in the component class using `FormControl`, `FormGroup`, and `FormArray`. This approach offers more predictability, testability, and scalability compared to Template-driven forms, especially for complex scenarios.

**Key Classes:**

*   **`FormControl`:** Tracks the value and validation status of an individual form control (e.g., an `<input>`, `<select>`).
*   **`FormGroup`:** Tracks the value and status of a group of `FormControl` instances. The group's value is an object containing the values of its controls.
*   **`FormArray`:** Tracks the value and status of a dynamic array of `FormControl` or `FormGroup` instances (e.g., for adding multiple phone numbers).
*   **`FormBuilder`:** A service providing convenient shorthand methods (`group()`, `control()`, `array()`) for creating form control instances.
*   **`Validators`:** Provides built-in validation functions (`required`, `minLength`, `maxLength`, `pattern`, `email`, etc.) and support for custom validators.

**Setup:**

1.  Import `ReactiveFormsModule` into your standalone component's `imports` array or the relevant `NgModule`.
2.  Import necessary classes (`FormGroup`, `FormControl`, `Validators`, `FormBuilder`) into your component class.

## Building a Reactive Form

```typescript
// src/app/my-form/my-form.component.ts
import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators, FormControl, FormArray } from '@angular/forms'; // Import necessary modules/classes

@Component({
  selector: 'app-my-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule], // Import ReactiveFormsModule
  templateUrl: './my-form.component.html',
  // ... styles
})
export class MyFormComponent implements OnInit {
  private fb = inject(FormBuilder); // Inject FormBuilder

  // Define the FormGroup structure
  profileForm!: FormGroup; // Use definite assignment assertion or initialize in constructor

  ngOnInit(): void {
    // Initialize the form using FormBuilder (common)
    this.profileForm = this.fb.group({
      firstName: ['', [Validators.required, Validators.minLength(3)]], // FormControl with initial value and validators
      lastName: [''],
      email: ['', [Validators.required, Validators.email]],
      address: this.fb.group({ // Nested FormGroup
        street: [''],
        city: [''],
        zip: ['', Validators.pattern('[0-9]{5}')] // Example pattern validator
      }),
      aliases: this.fb.array([ // FormArray for dynamic fields
        this.fb.control('') // Add one initial alias control
      ])
    });

    // Alternative: Initialize without FormBuilder
    // this.profileForm = new FormGroup({
    //   firstName: new FormControl('', Validators.required),
    //   lastName: new FormControl(''),
    //   // ... etc
    // });

    // Optional: Listen to value changes
    this.profileForm.valueChanges.subscribe(value => {
      console.log('Form Value Changed:', value);
    });

    // Optional: Listen to status changes
    this.profileForm.statusChanges.subscribe(status => {
      console.log('Form Status Changed:', status); // VALID, INVALID, PENDING, DISABLED
    });
  }

  // Getter for easy access to FormArray in template
  get aliases(): FormArray {
    return this.profileForm.get('aliases') as FormArray;
  }

  // Method to add a new alias control to the FormArray
  addAlias(): void {
    this.aliases.push(this.fb.control(''));
  }

  // Method to remove an alias control from the FormArray
  removeAlias(index: number): void {
    this.aliases.removeAt(index);
  }

  onSubmit(): void {
    if (this.profileForm.valid) {
      console.log('Form Submitted:', this.profileForm.value);
      // Process the form data (e.g., send to backend)
    } else {
      console.error('Form is invalid');
      // Optionally mark all fields as touched to display errors
      this.profileForm.markAllAsTouched();
    }
  }

  // Example method to update form values programmatically
  updateProfile(): void {
    this.profileForm.patchValue({ // Updates only specified fields
      firstName: 'Nancy',
      address: {
        street: '123 Drew Street'
      }
    });
    // Use setValue to update ALL fields (requires complete object)
    // this.profileForm.setValue({ ... complete form object ... });
  }
}
```

## Template Binding

*   Use the `[formGroup]` directive on the `<form>` element.
*   Use `formControlName` directive on each input element to bind it to the corresponding `FormControl` in the component class.
*   Use `formGroupName` for nested `FormGroup`s.
*   Use `formArrayName` for `FormArray`s, iterating over `aliases.controls`.

```html
<!-- src/app/my-form/my-form.component.html -->
<form [formGroup]="profileForm" (ngSubmit)="onSubmit()">

  <div>
    <label for="firstName">First Name:</label>
    <input id="firstName" type="text" formControlName="firstName">
    <!-- Error Handling -->
    @if (profileForm.get('firstName')?.invalid && (profileForm.get('firstName')?.dirty || profileForm.get('firstName')?.touched)) {
      <div class="error">
        @if (profileForm.get('firstName')?.errors?.['required']) {
          First name is required.
        }
        @if (profileForm.get('firstName')?.errors?.['minlength']) {
          First name must be at least 3 characters long.
        }
      </div>
    }
  </div>

  <div>
    <label for="lastName">Last Name:</label>
    <input id="lastName" type="text" formControlName="lastName">
  </div>

  <div>
    <label for="email">Email:</label>
    <input id="email" type="email" formControlName="email">
     @if (profileForm.get('email')?.invalid && profileForm.get('email')?.touched) {
      <div class="error">Please enter a valid email.</div>
    }
  </div>

  <!-- Nested FormGroup -->
  <div formGroupName="address">
    <h3>Address</h3>
    <div>
      <label for="street">Street:</label>
      <input id="street" type="text" formControlName="street">
    </div>
    <div>
      <label for="city">City:</label>
      <input id="city" type="text" formControlName="city">
    </div>
    <div>
      <label for="zip">Zip Code:</label>
      <input id="zip" type="text" formControlName="zip">
       @if (profileForm.get('address.zip')?.invalid && profileForm.get('address.zip')?.touched) {
        <div class="error">Please enter a 5-digit zip code.</div>
      }
    </div>
  </div>

  <!-- FormArray -->
  <div formArrayName="aliases">
    <h3>Aliases</h3>
    <button type="button" (click)="addAlias()">+ Add Alias</button>

    @for (alias of aliases.controls; track $index) {
      <div>
        <label for="alias-{{$index}}">Alias:</label>
        <input id="alias-{{$index}}" type="text" [formControlName]="$index">
        <button type="button" (click)="removeAlias($index)">Remove</button>
      </div>
    }
  </div>

  <button type="submit" [disabled]="profileForm.invalid">Submit</button>

</form>

<p>Form Status: {{ profileForm.status }}</p>
<button type="button" (click)="updateProfile()">Update Profile</button>
```

## Validation Status CSS Classes

Angular automatically adds CSS classes to form inputs reflecting their state:

*   `ng-valid` / `ng-invalid`
*   `ng-pending`
*   `ng-pristine` / `ng-dirty` (Value has/hasn't changed)
*   `ng-untouched` / `ng-touched` (Control has/hasn't lost focus)

Use these classes to style inputs based on their validation status.

Reactive Forms offer a robust and explicit way to manage form state and validation in Angular, making them ideal for complex scenarios.

*(Refer to the official Angular Reactive Forms documentation.)*