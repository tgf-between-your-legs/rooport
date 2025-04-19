# Angular: Template-Driven Forms

Building forms using directives in the template (`ngModel`).

## Core Concept

Template-Driven Forms rely primarily on directives within the template (`ngModel`, `ngForm`) to create and manage form controls implicitly. The form model is largely inferred from the template structure, making it quicker for simple forms but potentially harder to manage and test for complex scenarios compared to Reactive Forms.

**Key Directives & Concepts:**

*   **`FormsModule`:** Import this module into your standalone component's `imports` array (or the relevant `NgModule`) to enable template-driven form directives.
*   **`ngForm` Directive:** Automatically applied to any `<form>` element. It creates a top-level `FormGroup` instance and binds it to the form. You can export the directive to a template variable (`#myForm="ngForm"`) to access form state (e.g., `myForm.valid`, `myForm.value`).
*   **`ngModel` Directive:** Used on form input elements (`<input>`, `<textarea>`, `<select>`). It creates a `FormControl` instance implicitly.
    *   **One-way binding:** `[ngModel]="componentProperty"` binds the component property to the input value.
    *   **Two-way binding:** `[(ngModel)]="componentProperty"` creates a two-way binding between the input element and a component property. Changes in the component update the input, and user input updates the component property. **Requires a `name` attribute** on the input element.
*   **`ngModelGroup` Directive:** Groups related controls within a form, creating a nested `FormGroup` implicitly. Requires a `name` attribute.
*   **Validation Attributes:** Standard HTML5 validation attributes (`required`, `minlength`, `maxlength`, `pattern`, `email`) are automatically recognized and used by Angular to add validators to the implicit `FormControl`s.
*   **Template Reference Variables (`#inputName="ngModel"`):** Export the `ngModel` directive to a template variable to access the control's state (e.g., `inputName.valid`, `inputName.errors`, `inputName.dirty`, `inputName.touched`) directly in the template for showing validation messages.

**Setup:**

1.  Import `FormsModule` into your standalone component's `imports` array or the relevant `NgModule`.

## Building a Template-Driven Form

```typescript
// src/app/simple-form/simple-form.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, NgForm } from '@angular/forms'; // Import FormsModule

// Define an interface for the form model (optional but good practice)
interface Profile {
  firstName: string;
  email: string | null; // Allow null if not required initially
  subscribe: boolean;
}

@Component({
  selector: 'app-simple-form',
  standalone: true,
  imports: [CommonModule, FormsModule], // Import FormsModule
  templateUrl: './simple-form.component.html',
  // ... styles
})
export class SimpleFormComponent {
  // Initialize the component property that will hold the form data
  profileModel: Profile = {
    firstName: '',
    email: null,
    subscribe: false
  };

  // Method to handle form submission
  // The NgForm directive instance is passed automatically
  onSubmit(form: NgForm): void {
    if (form.valid) {
      console.log('Form Submitted:', form.value); // form.value contains the form data
      console.log('Component Model:', this.profileModel); // If using two-way binding, this is also updated
      // Process data
    } else {
      console.error('Form is invalid');
      // Template handles showing errors based on control state
    }
  }
}
```

## Template Binding

*   Use `#myForm="ngForm"` on the `<form>` tag to get a reference to the form's state.
*   Use `[(ngModel)]` for two-way binding (requires `name` attribute).
*   Use `#inputRef="ngModel"` on inputs to check validation status directly in the template.
*   Use standard HTML validation attributes (`required`, `pattern`, etc.).

```html
<!-- src/app/simple-form/simple-form.component.html -->
<form #profileForm="ngForm" (ngSubmit)="onSubmit(profileForm)">

  <div>
    <label for="firstName">First Name:</label>
    <!-- Two-way binding with [(ngModel)] -->
    <!-- 'name' attribute is required for ngModel within a form -->
    <!-- 'required' attribute adds validation -->
    <!-- #firstNameInput="ngModel" exports control state -->
    <input
      type="text"
      id="firstName"
      name="firstName"
      required
      minlength="3"
      [(ngModel)]="profileModel.firstName"
      #firstNameInput="ngModel"
      [class.is-invalid]="firstNameInput.invalid && firstNameInput.touched"
    >
    <!-- Error Handling using template reference variable -->
    @if (firstNameInput.invalid && (firstNameInput.dirty || firstNameInput.touched)) {
      <div class="error">
        @if (firstNameInput.errors?.['required']) {
          First name is required.
        }
        @if (firstNameInput.errors?.['minlength']) {
          First name must be at least {{ firstNameInput.errors?.['minlength'].requiredLength }} characters long.
        }
      </div>
    }
  </div>

  <div>
    <label for="email">Email:</label>
    <input
      type="email"
      id="email"
      name="email"
      email  
      [(ngModel)]="profileModel.email"
      #emailInput="ngModel"
      [class.is-invalid]="emailInput.invalid && emailInput.touched"
    >
     @if (emailInput.invalid && emailInput.touched) {
      <div class="error">Please enter a valid email.</div>
    }
  </div>

  <div>
    <label>
      <input type="checkbox" name="subscribe" [(ngModel)]="profileModel.subscribe">
      Subscribe to newsletter
    </label>
  </div>

  <button type="submit" [disabled]="profileForm.invalid">Submit</button>

</form>

<p>Form Valid: {{ profileForm.valid }}</p>
<p>Form Touched: {{ profileForm.touched }}</p>
<p>Form Value: {{ profileForm.value | json }}</p>
<p>Model Value: {{ profileModel | json }}</p>
```

## When to Use Template-Driven Forms

*   Simple forms with minimal validation logic.
*   Scenarios where most logic can reside directly in the template.
*   Migrating existing AngularJS applications.

For more complex forms with dynamic validation, conditional fields, or significant logic, **Reactive Forms** are generally the preferred approach due to their explicitness, testability, and scalability.

*(Refer to the official Angular Template-Driven Forms documentation.)*