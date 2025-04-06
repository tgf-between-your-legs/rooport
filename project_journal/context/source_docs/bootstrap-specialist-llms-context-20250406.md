TITLE: Adding Viewport Meta Tag for Responsive Design
DESCRIPTION: This snippet demonstrates how to add the viewport meta tag to ensure proper rendering and touch zooming on all devices.

LANGUAGE: html
CODE:
<meta name="viewport" content="width=device-width, initial-scale=1">

----------------------------------------

TITLE: Including Bootstrap via CDN with Bundled JS
DESCRIPTION: HTML code to include Bootstrap's compiled CSS and bundled JS from jsDelivr CDN with SRI hash verification

LANGUAGE: html
CODE:
<link href="{{< param "cdn.css" >}}" rel="stylesheet" integrity="{{< param "cdn.css_hash" >}}" crossorigin="anonymous">
<script src="{{< param "cdn.js_bundle" >}}" integrity="{{< param "cdn.js_bundle_hash" >}}" crossorigin="anonymous"></script>

----------------------------------------

TITLE: Including Bootstrap CSS and JS via CDN
DESCRIPTION: This snippet demonstrates how to include Bootstrap's CSS and JavaScript (including Popper for positioning dropdowns, popovers, and tooltips) using CDN links in an HTML file.

LANGUAGE: html
CODE:
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="{{< param "cdn.css" >}}" rel="stylesheet" integrity="{{< param "cdn.css_hash" >}}" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="{{< param "cdn.js_bundle" >}}" integrity="{{< param "cdn.js_bundle_hash" >}}" crossorigin="anonymous"></script>
  </body>
</html>

----------------------------------------

TITLE: Including Popper and Bootstrap JS Separately
DESCRIPTION: This snippet shows how to include Popper and Bootstrap's JavaScript separately, which is useful if you don't need all Bootstrap components that require Popper.

LANGUAGE: html
CODE:
<script src="{{< param "cdn.popper" >}}" integrity="{{< param "cdn.popper_hash" >}}" crossorigin="anonymous"></script>
<script src="{{< param "cdn.js" >}}" integrity="{{< param "cdn.js_hash" >}}" crossorigin="anonymous"></script>

----------------------------------------

TITLE: Creating Basic HTML Structure for Bootstrap
DESCRIPTION: This snippet shows how to create a basic HTML5 structure with the necessary viewport meta tag for responsive behavior in mobile devices.

LANGUAGE: html
CODE:
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>

----------------------------------------

TITLE: Custom Validation Form Example
DESCRIPTION: Sample form with custom Bootstrap validation styles using the novalidate attribute and JavaScript validation. Shows usage of :invalid/:valid styles with custom feedback messages.

LANGUAGE: html
CODE:
<form class="row g-3 needs-validation" novalidate>
  <div class="col-md-4">
    <label for="validationCustom01" class="form-label">First name</label>
    <input type="text" class="form-control" id="validationCustom01" value="Mark" required>
    <div class="valid-feedback">
      Looks good!
    </div>
  </div>
  <!-- Additional form fields -->
</form>

----------------------------------------

TITLE: Setting HTML5 Doctype for Bootstrap
DESCRIPTION: This snippet shows the required HTML5 doctype declaration for proper Bootstrap styling and functionality.

LANGUAGE: html
CODE:
<!doctype html>
<html lang="en">
  ...
</html>

----------------------------------------

TITLE: Installing Bootstrap via npm
DESCRIPTION: Command to install Bootstrap using npm package manager

LANGUAGE: sh
CODE:
npm install bootstrap@{{< param "current_version" >}}

----------------------------------------

TITLE: Basic Navbar Implementation
DESCRIPTION: Example of a basic responsive Bootstrap navbar with brand, navigation links and form elements.

LANGUAGE: HTML
CODE:
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>

----------------------------------------

TITLE: Creating Complex Form Layouts with Bootstrap Grid
DESCRIPTION: Illustrates how to create a more complex form layout using Bootstrap's grid system and form classes.

LANGUAGE: HTML
CODE:
<form class="row g-3">
  <div class="col-md-6">
    <label for="inputEmail4" class="form-label">Email</label>
    <input type="email" class="form-control" id="inputEmail4">
  </div>
  <div class="col-md-6">
    <label for="inputPassword4" class="form-label">Password</label>
    <input type="password" class="form-control" id="inputPassword4">
  </div>
  <!-- More form fields -->
  <div class="col-12">
    <button type="submit" class="btn btn-primary">Sign in</button>
  </div>
</form>

----------------------------------------

TITLE: Creating Button Variants in HTML
DESCRIPTION: Shows how to create different button variants using Bootstrap's predefined classes.

LANGUAGE: HTML
CODE:
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>
<button type="button" class="btn btn-link">Link</button>

----------------------------------------

TITLE: Implementing Default Bootstrap Container
DESCRIPTION: Basic implementation of Bootstrap's default container class that provides responsive fixed-width containment with automatic breakpoint adjustments.

LANGUAGE: html
CODE:
<div class="container">
  <!-- Content here -->
</div>

----------------------------------------

TITLE: Rendering Basic Button in HTML
DESCRIPTION: Demonstrates the use of the base .btn class to create a simple button.

LANGUAGE: HTML
CODE:
<button type="button" class="btn">Base class</button>

----------------------------------------

TITLE: Basic Card Example in HTML
DESCRIPTION: Demonstrates a basic card structure with an image, title, text, and button.

LANGUAGE: HTML
CODE:
<div class="card" style="width: 18rem;">
  {{< placeholder width="100%" height="180" class="card-img-top" text="Image cap" >}}
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>

----------------------------------------

TITLE: Creating Basic Form Structure with Bootstrap
DESCRIPTION: Demonstrates how to create a simple form structure using Bootstrap classes for margin and form controls.

LANGUAGE: HTML
CODE:
<div class="mb-3">
  <label for="formGroupExampleInput" class="form-label">Example label</label>
  <input type="text" class="form-control" id="formGroupExampleInput" placeholder="Example input placeholder">
</div>
<div class="mb-3">
  <label for="formGroupExampleInput2" class="form-label">Another label</label>
  <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="Another input placeholder">
</div>

----------------------------------------

TITLE: Implementing Visually Hidden Content in HTML with Bootstrap
DESCRIPTION: This snippet demonstrates how to use the .visually-hidden class to create content that is hidden visually but remains accessible to assistive technologies. It's useful for providing additional context to non-visual users.

LANGUAGE: html
CODE:
<p class="text-danger">
  <span class="visually-hidden">Danger: </span>
  This action is not reversible
</p>

----------------------------------------

TITLE: Aligning Items in Flex Containers
DESCRIPTION: Shows how to align flex items along the cross axis using Bootstrap's align-items utility classes.

LANGUAGE: HTML
CODE:
<div class="d-flex align-items-start">...</div>
<div class="d-flex align-items-end">...</div>
<div class="d-flex align-items-center">...</div>
<div class="d-flex align-items-baseline">...</div>
<div class="d-flex align-items-stretch">...</div>

----------------------------------------

TITLE: Importing Bootstrap Sass Components Selectively
DESCRIPTION: This snippet demonstrates how to selectively import Bootstrap Sass components to optimize file size. It shows the structure of the bootstrap.scss file and suggests commenting out or deleting unused components.

LANGUAGE: scss
CODE:
{{< scss-docs name="import-stack" file="scss/bootstrap.scss" >}}

----------------------------------------

TITLE: Creating Basic Button Group in HTML with Bootstrap
DESCRIPTION: Demonstrates how to create a basic button group using Bootstrap classes. The buttons are wrapped in a div with the 'btn-group' class, and each button has the 'btn' and 'btn-primary' classes applied.

LANGUAGE: HTML
CODE:
<div class="btn-group" role="group" aria-label="Basic example">
  <button type="button" class="btn btn-primary">Left</button>
  <button type="button" class="btn btn-primary">Middle</button>
  <button type="button" class="btn btn-primary">Right</button>
</div>

----------------------------------------

TITLE: Importing Bootstrap CSS and JavaScript in Webpack
DESCRIPTION: JavaScript code to import Bootstrap's CSS and all of its JavaScript components in the Webpack entry point.

LANGUAGE: javascript
CODE:
// Import our custom CSS
import '../scss/styles.scss'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'

----------------------------------------

TITLE: Installing Bootstrap with Package Managers
DESCRIPTION: Commands to install Bootstrap using various package managers like npm, yarn, Composer, and NuGet.

LANGUAGE: shell
CODE:
npm install bootstrap@v5.3.3
yarn add bootstrap@v5.3.3
composer require twbs/bootstrap:5.3.3
Install-Package bootstrap
Install-Package bootstrap.sass

----------------------------------------

TITLE: Basic Form Controls Example in Bootstrap
DESCRIPTION: Example showing basic email input and textarea implementation with Bootstrap form control classes.

LANGUAGE: html
CODE:
<div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Email address</label>
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
</div>
<div class="mb-3">
  <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
  <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
</div>

----------------------------------------

TITLE: Exploring Compiled Bootstrap Directory Structure
DESCRIPTION: Shows the complete directory structure of a compiled Bootstrap distribution, including CSS files (with grid, reboot, utilities variants) and JavaScript files (with bundles and source maps).

LANGUAGE: text
CODE:
bootstrap/
├── css/
│   ├── bootstrap-grid.css
│   ├── bootstrap-grid.css.map
│   ├── bootstrap-grid.min.css
│   ├── bootstrap-grid.min.css.map
│   ├── bootstrap-grid.rtl.css
│   ├── bootstrap-grid.rtl.css.map
│   ├── bootstrap-grid.rtl.min.css
│   ├── bootstrap-grid.rtl.min.css.map
│   ├── bootstrap-reboot.css
│   ├── bootstrap-reboot.css.map
│   ├── bootstrap-reboot.min.css
│   ├── bootstrap-reboot.min.css.map
│   ├── bootstrap-reboot.rtl.css
│   ├── bootstrap-reboot.rtl.css.map
│   ├── bootstrap-reboot.rtl.min.css
│   ├── bootstrap-reboot.rtl.min.css.map
│   ├── bootstrap-utilities.css
│   ├── bootstrap-utilities.css.map
│   ├── bootstrap-utilities.min.css
│   ├── bootstrap-utilities.min.css.map
│   ├── bootstrap-utilities.rtl.css
│   ├── bootstrap-utilities.rtl.css.map
│   ├── bootstrap-utilities.rtl.min.css
│   ├── bootstrap-utilities.rtl.min.css.map
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   ├── bootstrap.min.css.map
│   ├── bootstrap.rtl.css
│   ├── bootstrap.rtl.css.map
│   ├── bootstrap.rtl.min.css
│   └── bootstrap.rtl.min.css.map
└── js/
    ├── bootstrap.bundle.js
    ├── bootstrap.bundle.js.map
    ├── bootstrap.bundle.min.js
    ├── bootstrap.bundle.min.js.map
    ├── bootstrap.esm.js
    ├── bootstrap.esm.js.map
    ├── bootstrap.esm.min.js
    ├── bootstrap.esm.min.js.map
    ├── bootstrap.js
    ├── bootstrap.js.map
    ├── bootstrap.min.js
    └── bootstrap.min.js.map

----------------------------------------

TITLE: Importing Partial Bootstrap Sass
DESCRIPTION: Shows how to selectively import specific Bootstrap Sass components and utilities.

LANGUAGE: scss
CODE:
// Custom.scss
// Option B: Include parts of Bootstrap

// 1. Include functions first (so you can manipulate colors, SVGs, calc, etc)
@import "../node_modules/bootstrap/scss/functions";

// 2. Include any default variable overrides here

// 3. Include remainder of required Bootstrap stylesheets
@import "../node_modules/bootstrap/scss/variables";
@import "../node_modules/bootstrap/scss/variables-dark";

// 4. Include any default map overrides here

// 5. Include remainder of required parts
@import "../node_modules/bootstrap/scss/maps";
@import "../node_modules/bootstrap/scss/mixins";
@import "../node_modules/bootstrap/scss/root";

// 6. Optionally include any other parts as needed
@import "../node_modules/bootstrap/scss/utilities";
@import "../node_modules/bootstrap/scss/reboot";
@import "../node_modules/bootstrap/scss/type";
@import "../node_modules/bootstrap/scss/images";
@import "../node_modules/bootstrap/scss/containers";
@import "../node_modules/bootstrap/scss/grid";
@import "../node_modules/bootstrap/scss/helpers";

// 7. Optionally include utilities API last
@import "../node_modules/bootstrap/scss/utilities/api";

// 8. Add additional custom code here

----------------------------------------

TITLE: Implementing Button Sizes in HTML
DESCRIPTION: Demonstrates how to create larger and smaller buttons using Bootstrap's size classes.

LANGUAGE: HTML
CODE:
<button type="button" class="btn btn-primary btn-lg">Large button</button>
<button type="button" class="btn btn-secondary btn-lg">Large button</button>

LANGUAGE: HTML
CODE:
<button type="button" class="btn btn-primary btn-sm">Small button</button>
<button type="button" class="btn btn-secondary btn-sm">Small button</button>

----------------------------------------

TITLE: Form Validation JavaScript
DESCRIPTION: JavaScript code that handles custom form validation by preventing form submission and showing validation feedback.

LANGUAGE: javascript
CODE:
(() => {
  'use strict'

  const forms = document.querySelectorAll('.needs-validation')

  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()

----------------------------------------

TITLE: Defining Root CSS Variables in Bootstrap
DESCRIPTION: This snippet shows the default CSS variables available globally in Bootstrap, defined in the :root selector. These variables are used for theme colors, breakpoints, and font stacks.

LANGUAGE: css
CODE:
:root,
[data-bs-theme=light] {([^}]*)}

----------------------------------------

TITLE: Basic Bootstrap Grid Example
DESCRIPTION: Example showing basic three-column grid layout using Bootstrap's container, row and column classes

LANGUAGE: HTML
CODE:
<div class="container text-center">
  <div class="row">
    <div class="col">
      Column
    </div>
    <div class="col">
      Column
    </div>
    <div class="col">
      Column
    </div>
  </div>
</div>

----------------------------------------

TITLE: Customizing Bootstrap SCSS Variables
DESCRIPTION: This snippet shows a table of key Sass variables used to customize Bootstrap's global options. Each variable is listed with its default value, possible values, and a description of its effect on the framework.

LANGUAGE: scss
CODE:
$spacer: 1rem;
$enable-dark-mode: true;
$enable-rounded: true;
$enable-shadows: false;
$enable-gradients: false;
$enable-transitions: true;
$enable-reduced-motion: true;
$enable-grid-classes: true;
$enable-cssgrid: false;
$enable-container-classes: true;
$enable-caret: true;
$enable-button-pointers: true;
$enable-rfs: true;
$enable-validation-icons: true;
$enable-negative-margins: false;
$enable-deprecation-messages: true;
$enable-important-utilities: true;
$enable-smooth-scroll: true;

----------------------------------------

TITLE: Basic Bootstrap Grid Example
DESCRIPTION: Example showing basic three-column grid layout using Bootstrap's container, row and column classes

LANGUAGE: HTML
CODE:
<div class="container text-center">
  <div class="row">
    <div class="col">
      Column
    </div>
    <div class="col">
      Column
    </div>
    <div class="col">
      Column
    </div>
  </div>
</div>

----------------------------------------

TITLE: Basic Modal Structure in HTML
DESCRIPTION: Shows the basic HTML structure for a Bootstrap modal with header, body, and footer sections.

LANGUAGE: HTML
CODE:
<div class="modal" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Modal body text goes here.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>

----------------------------------------

TITLE: Creating Basic Input Groups with Bootstrap
DESCRIPTION: Demonstrates how to create basic input groups with text add-ons, buttons, and various input types using Bootstrap classes.

LANGUAGE: HTML
CODE:
<div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon1">@</span>
  <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="basic-addon2">
  <span class="input-group-text" id="basic-addon2">@example.com</span>
</div>

<div class="mb-3">
  <label for="basic-url" class="form-label">Your vanity URL</label>
  <div class="input-group">
    <span class="input-group-text" id="basic-addon3">https://example.com/users/</span>
    <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4">
  </div>
  <div class="form-text" id="basic-addon4">Example help text goes outside the input group.</div>
</div>

<div class="input-group mb-3">
  <span class="input-group-text">$</span>
  <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)">
  <span class="input-group-text">.00</span>
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Username" aria-label="Username">
  <span class="input-group-text">@</span>
  <input type="text" class="form-control" placeholder="Server" aria-label="Server">
</div>

<div class="input-group">
  <span class="input-group-text">With textarea</span>
  <textarea class="form-control" aria-label="With textarea"></textarea>
</div>

----------------------------------------

TITLE: Enabling Dark Mode in HTML
DESCRIPTION: This snippet shows how to enable dark mode across an entire project by adding the data-bs-theme attribute to the HTML element.

LANGUAGE: html
CODE:
<!doctype html>
<html lang="en" data-bs-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="{{< param "cdn.css" >}}" rel="stylesheet" integrity="{{< param "cdn.css_hash" >}}" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="{{< param "cdn.js_bundle" >}}" integrity="{{< param "cdn.js_bundle_hash" >}}" crossorigin="anonymous"></script>
  </body>
</html>

----------------------------------------

TITLE: Defining Text Color Utility in CSS
DESCRIPTION: This CSS snippet shows how a text color utility class (specifically .text-primary) is defined using CSS variables. It demonstrates the use of RGB values and opacity for flexible color manipulation.

LANGUAGE: css
CODE:
.text-primary {
  --bs-text-opacity: 1;
  color: rgba(var(--bs-primary-rgb), var(--bs-text-opacity)) !important;
}

----------------------------------------

TITLE: Using CSS Variables for Page Styling in Bootstrap
DESCRIPTION: This example shows how to use Bootstrap's CSS variables to reset the page's font and link styles. It demonstrates the flexibility of CSS variables compared to Sass variables.

LANGUAGE: css
CODE:
body {
  font: 1rem/1.5 var(--bs-font-sans-serif);
}
a {
  color: var(--bs-blue);
}

----------------------------------------

TITLE: Implementing Basic Bootstrap Accordion
DESCRIPTION: Basic accordion implementation with three collapsible items. The first item is expanded by default using .show class and appropriate aria attributes.

LANGUAGE: HTML
CODE:
<div class="accordion" id="accordionExample">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        Accordion Item #1
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <strong>This is the first item's accordion body.</strong> It is shown by default...
      </div>
    </div>
  </div>
</div>

----------------------------------------

TITLE: Grid Sass Variables Configuration
DESCRIPTION: Core Sass variables that control the Bootstrap grid system's columns, gutters and breakpoints

LANGUAGE: SCSS
CODE:
$grid-columns:      12;
$grid-gutter-width: 1.5rem;
$grid-row-columns:  6;