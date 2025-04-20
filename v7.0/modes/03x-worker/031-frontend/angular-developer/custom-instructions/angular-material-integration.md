# Angular: Integrating Angular Material

Using components from the Angular Material library.

## Core Concept

Angular Material is a UI component library implementing Google's Material Design specification for Angular applications. It provides a wide range of pre-built, high-quality components like buttons, forms, navigation elements, dialogs, tables, etc.

**Key Features:**

*   Comprehensive set of UI components.
*   Theming capabilities.
*   Accessibility built-in.
*   Part of the official Angular ecosystem.

## Setup

1.  **Installation:** Use the Angular CLI's `ng add` command (recommended). This installs the library and performs initial setup (theming, typography, animations).
    ```bash
    ng add @angular/material
    ```
    Follow the prompts to choose a pre-built theme (or custom), set up typography, and include browser animations (`BrowserAnimationsModule`).
2.  **Import Components:** In modern Angular with standalone components, import the specific Material component modules you need directly into your standalone component's `imports` array.
    *   **Example:** To use `<mat-button>` and `<mat-icon>`, import `MatButtonModule` and `MatIconModule`.

## Using Material Components

1.  **Import Module:** Import the required module(s) into your standalone component or `NgModule`.
2.  **Use Component Selector:** Use the component's selector (e.g., `<mat-button>`, `<mat-form-field>`, `<mat-icon>`) in your component's template.
3.  **Configure Inputs/Outputs:** Use standard Angular property binding `[]` and event binding `()` to configure the component's behavior and respond to its events. Refer to the specific component's API documentation.

```typescript
// src/app/example-material/example-material.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

// 1. Import necessary Material component modules
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { FormsModule } from '@angular/forms'; // Needed for ngModel with MatSlideToggle

@Component({
  selector: 'app-example-material',
  standalone: true,
  // 2. Add modules to imports array
  imports: [
    CommonModule,
    FormsModule,
    MatButtonModule,
    MatIconModule,
    MatFormFieldModule,
    MatInputModule,
    MatSlideToggleModule
  ],
  templateUrl: './example-material.component.html',
  styleUrls: ['./example-material.component.css']
})
export class ExampleMaterialComponent {
  isToggled = false;
  inputValue = '';

  onButtonClick() {
    console.log('Material Button Clicked!');
  }

  onToggleChange(event: any) { // Type would be MatSlideToggleChange
    console.log('Toggle changed:', event.checked);
  }
}
```

```html
<!-- src/app/example-material/example-material.component.html -->
<h2>Angular Material Examples</h2>

<!-- Button -->
<button mat-raised-button color="primary" (click)="onButtonClick()">
  <mat-icon>thumb_up</mat-icon> <!-- Icon inside button -->
  Primary Button
</button>

<button mat-icon-button color="accent" aria-label="Example icon-button with a heart icon">
  <mat-icon>favorite</mat-icon>
</button>

<hr>

<!-- Form Field & Input -->
<mat-form-field appearance="outline"> <!-- Different appearances available -->
  <mat-label>Enter Text</mat-label>
  <input matInput placeholder="Placeholder text" [(ngModel)]="inputValue">
  <mat-icon matSuffix>sentiment_very_satisfied</mat-icon> <!-- Icon suffix -->
  <mat-hint>Hint text</mat-hint>
</mat-form-field>
<p>Input Value: {{ inputValue }}</p>

<hr>

<!-- Slide Toggle -->
<mat-slide-toggle
  [(ngModel)]="isToggled"
  (change)="onToggleChange($event)"
  color="warn">
  Slide me!
</mat-slide-toggle>
<p>Toggle State: {{ isToggled }}</p>
```

## Theming

*   Angular Material uses a Sass-based theming system.
*   When running `ng add @angular/material`, you typically choose a pre-built theme (e.g., `indigo-pink`, `deeppurple-amber`) or select "custom".
*   The chosen theme CSS file is usually added to the `styles` array in `angular.json`.
*   Custom themes can be defined using Sass mixins provided by the library (refer to Angular Material Theming guide).

## CDK (Component Dev Kit)

*   The `@angular/cdk` package provides lower-level building blocks and utilities used by Angular Material components, but also available for building your own custom components.
*   Includes features like overlays, portals, drag & drop, accessibility utilities, layout helpers, etc.

Angular Material provides a rich set of well-tested and accessible components, significantly speeding up UI development. Always consult the official Angular Material documentation for specific component APIs and usage examples.

*(Refer to the official Angular Material documentation: https://material.angular.io/)*