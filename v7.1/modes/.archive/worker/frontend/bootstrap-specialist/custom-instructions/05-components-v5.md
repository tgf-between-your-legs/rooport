# Common Bootstrap 5 Components Quick Reference

Examples and key classes/options for frequently used Bootstrap 5 components.

## Core Concept

Bootstrap provides pre-styled components for common UI patterns. Use the appropriate HTML structure and CSS classes as defined in the documentation for v5.

## 1. Navbar (`.navbar`)

Responsive navigation header.

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0"> {/* ms-auto pushes items right */}
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
```
*   **Key Classes:** `.navbar`, `.navbar-expand-{sm|md|lg|xl|xxl}` (breakpoint for collapsing), `.navbar-brand`, `.navbar-toggler`, `.navbar-collapse`, `.collapse`, `.navbar-nav`, `.nav-item`, `.nav-link`, `.dropdown`, `.dropdown-toggle`, `.dropdown-menu`, `.dropdown-item`, `.dropdown-divider`, `.dropdown-menu-end`.
*   **Color Schemes:** `.navbar-light`, `.navbar-dark`, `.bg-*` utilities.
*   **JS:** Requires Bootstrap JS bundle (or individual Collapse/Dropdown components) + Popper.js v2.

## 2. Modal (`.modal`)

Dialog box/popup.

```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered"> {/* Optional: .modal-dialog-scrollable, .modal-sm|lg|xl */}
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ... Modal content ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```
*   **Key Classes:** `.modal`, `.fade`, `.modal-dialog`, `.modal-content`, `.modal-header`, `.modal-title`, `.btn-close`, `.modal-body`, `.modal-footer`.
*   **Options:** `.modal-dialog-centered`, `.modal-dialog-scrollable`, `.modal-{sm|lg|xl}`.
*   **JS:** Requires Bootstrap JS bundle (or Modal component). Triggered via `data-bs-toggle="modal"` and `data-bs-target="#modalId"`. Dismissed with `data-bs-dismiss="modal"`.

## 3. Card (`.card`)

Flexible content container.

```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
  <ul class="list-group list-group-flush"> {/* Optional */}
    <li class="list-group-item">An item</li>
  </ul>
  <div class="card-footer text-muted"> {/* Optional */}
    2 days ago
  </div>
</div>
```
*   **Key Classes:** `.card`, `.card-img-top`, `.card-body`, `.card-title`, `.card-text`, `.card-header`, `.card-footer`, `.list-group`, `.list-group-item`, `.text-muted`.

## 4. Forms (`.form-label`, `.form-control`, etc.)

```html
<form>
  <div class="mb-3">
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
*   **Key Classes:** `.form-label`, `.form-control`, `.form-text`, `.form-check`, `.form-check-input`, `.form-check-label`, `.form-select`, `.input-group`, `.invalid-feedback`, `.valid-feedback`, `.was-validated` (on form for validation styles). Use spacing utilities like `.mb-3`.

## 5. Buttons (`.btn`)

```html
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>
<button type="button" class="btn btn-link">Link</button>

{/* Outline Buttons */}
<button type="button" class="btn btn-outline-primary">Primary</button>

{/* Sizes */}
<button type="button" class="btn btn-primary btn-lg">Large button</button>
<button type="button" class="btn btn-secondary btn-sm">Small button</button>
```
*   **Key Classes:** `.btn`, `.btn-{primary|secondary|success|danger|warning|info|light|dark|link}`, `.btn-outline-*`, `.btn-{lg|sm}`.

## 6. Alerts (`.alert`)

```html
<div class="alert alert-success alert-dismissible fade show" role="alert">
  <strong>Well done!</strong> You successfully read this important alert message.
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>
<div class="alert alert-warning" role="alert">
  A simple warning alert—check it out!
</div>
```
*   **Key Classes:** `.alert`, `.alert-{primary|secondary|success|danger|warning|info|light|dark}`, `.alert-dismissible`, `.fade`, `.show`, `.btn-close`.
*   **JS:** Dismissible alerts require Bootstrap JS bundle (or Alert component).

## 7. Dropdowns (`.dropdown`)

```html
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
*   **Key Classes:** `.dropdown`, `.dropdown-toggle`, `.dropdown-menu`, `.dropdown-item`, `.dropdown-divider`.
*   **JS:** Requires Popper.js v2 and Bootstrap JS. Triggered via `data-bs-toggle="dropdown"`.

This covers some of the most common components. Always refer to the official Bootstrap 5 documentation for the full list, options, and correct implementation details.

*(Refer to the official Bootstrap 5 documentation for all components and options: https://getbootstrap.com/docs/5.3/components/)*