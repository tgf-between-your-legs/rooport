# Bootstrap: Common Components (v4 & v5)

Examples of frequently used Bootstrap components. Note class name differences between v4 and v5, especially for utilities.

## Core Concept

Bootstrap provides pre-styled components for common UI patterns. Use the appropriate HTML structure and CSS classes as defined in the documentation for your target version (v4 or v5).

## 1. Navbar

*   **Purpose:** Responsive navigation header.
*   **Key Classes:** `.navbar`, `.navbar-expand-{breakpoint}`, `.navbar-brand`, `.navbar-toggler`, `.navbar-collapse`, `.navbar-nav`, `.nav-link`, `.nav-item`.

```html
<!-- Bootstrap 5 Example -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0"> {/* ms-auto for right align in v5 */}
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
<!-- Note: v4 uses mr-auto/ml-auto for alignment, data-* attributes instead of data-bs-* -->
```

## 2. Modal

*   **Purpose:** Dialog box/popup window displayed over the page content.
*   **Key Classes:** `.modal`, `.modal-dialog`, `.modal-content`, `.modal-header`, `.modal-title`, `.modal-body`, `.modal-footer`, `.btn-close` (v5).
*   **JS:** Requires Bootstrap's JavaScript (and Popper.js). Triggered via `data-bs-toggle="modal"` and `data-bs-target="#myModalId"` (v5) or `data-toggle`/`data-target` (v4), or programmatically.

```html
<!-- Bootstrap 5 Example -->
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered"> {/* Centered */}
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ... Modal content goes here ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```

## 3. Card

*   **Purpose:** Flexible content container with options for headers, footers, images, and text.
*   **Key Classes:** `.card`, `.card-header`, `.card-body`, `.card-footer`, `.card-title`, `.card-subtitle`, `.card-text`, `.card-link`, `.card-img-top`.

```html
<!-- Bootstrap 5 Example -->
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
  <div class="card-footer text-muted"> {/* v5 uses text-muted, v4 uses text-muted */}
    2 days ago
  </div>
</div>
```

## 4. Buttons

*   **Purpose:** Standard button styles.
*   **Key Classes:** `.btn`, `.btn-{color}` (`primary`, `secondary`, `success`, `danger`, `warning`, `info`, `light`, `dark`, `link`), `.btn-{outline-color}`, `.btn-{lg|sm}`.

```html
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-outline-success">Success Outline</button>
<a class="btn btn-lg btn-info" href="#" role="button">Large info link</a>
```

## 5. Forms

*   **Purpose:** Styling for form controls, labels, layout, and validation states.
*   **Key Classes:** `.form-control`, `.form-select`, `.form-check`, `.form-check-input`, `.form-check-label`, `.form-label`, `.input-group`. Layout often uses the grid system (`.row`, `.col-*`).

```html
<!-- Bootstrap 5 Example -->
<form>
  <div class="mb-3"> {/* Margin bottom utility */}
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

## 6. Alerts

*   **Purpose:** Provide contextual feedback messages.
*   **Key Classes:** `.alert`, `.alert-{color}` (`primary`, `secondary`, `success`, etc.), `.alert-dismissible`, `.fade`, `.show`, `.btn-close` (v5).

```html
<!-- Bootstrap 5 Example -->
<div class="alert alert-warning alert-dismissible fade show" role="alert">
  <strong>Holy guacamole!</strong> You should check in on some of those fields below.
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>
```

## 7. Dropdowns

*   **Purpose:** Toggleable menus for displaying lists of links or actions.
*   **Key Classes:** `.dropdown`, `.dropdown-toggle`, `.dropdown-menu`, `.dropdown-item`, `.dropdown-divider`.
*   **JS:** Requires Popper.js and Bootstrap JS. Triggered via `data-bs-toggle="dropdown"` (v5) or `data-toggle` (v4).

```html
<!-- Bootstrap 5 Example -->
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown button
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
```

This covers some of the most common components. Always refer to the official Bootstrap documentation for the specific version you are using for the full list, options, and correct implementation details.