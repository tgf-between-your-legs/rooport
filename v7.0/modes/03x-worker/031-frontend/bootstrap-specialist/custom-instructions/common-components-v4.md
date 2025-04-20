# Common Bootstrap 4 Components Quick Reference

Examples and key classes/options for frequently used Bootstrap 4 components. Note differences from v5.

## 1. Navbar (`.navbar`)

Responsive navigation header.

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ml-auto"> {/* ml-auto pushes items right (mr-auto for left) */}
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Features</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
    </ul>
  </div>
</nav>
```
*   **Key Classes:** `.navbar`, `.navbar-expand-{sm|md|lg|xl}`, `.navbar-brand`, `.navbar-toggler`, `.navbar-collapse`, `.collapse`, `.navbar-nav`, `.nav-item`, `.nav-link`, `.active`, `.dropdown`, `.dropdown-toggle`, `.dropdown-menu`, `.dropdown-item`, `.dropdown-divider`.
*   **Color Schemes:** `.navbar-light`, `.navbar-dark`, `.bg-*` utilities.
*   **JS:** Requires jQuery, Popper.js (v1), and Bootstrap JS bundle (or individual Collapse/Dropdown components).

## 2. Modal (`.modal`)

Dialog box/popup.

```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered"> {/* Optional: .modal-dialog-scrollable, .modal-sm|lg|xl */}
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        ... Modal content ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```
*   **Key Classes:** `.modal`, `.fade`, `.modal-dialog`, `.modal-content`, `.modal-header`, `.modal-title`, `.close` (for dismiss button), `.modal-body`, `.modal-footer`.
*   **Options:** `.modal-dialog-centered`, `.modal-dialog-scrollable`, `.modal-{sm|lg|xl}`.
*   **JS:** Requires jQuery, Popper.js (v1), and Bootstrap JS bundle (or Modal component). Triggered via `data-toggle="modal"` and `data-target="#modalId"`. Dismissed with `data-dismiss="modal"`.

## 3. Card (`.card`)

Flexible content container. (Largely similar to v5)

```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
  {/* Other elements like .card-header, .card-footer, .list-group are similar */}
</div>
```
*   **Key Classes:** `.card`, `.card-img-top`, `.card-body`, `.card-title`, `.card-text`, etc.

## 4. Forms (`.form-group`, `.form-control`, etc.)

Note the use of `.form-group` for spacing/layout.

```html
<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
    <small id="emailHelp" class="form-text text-muted">We'll never share your email.</small>
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
  <div class="form-group form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```
*   **Key Classes:** `.form-group`, `.form-label` (implicit or explicit `<label>`), `.form-control`, `.form-text`, `.form-check`, `.form-check-input`, `.form-check-label`, `.form-control-file`, `.form-control-range`, `.invalid-feedback`, `.valid-feedback`, `.is-invalid`, `.is-valid`. Use spacing utilities like `.mb-3`.

## 5. Buttons (`.btn`)

(Largely similar to v5, main difference is JS dependency)

```html
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-outline-secondary">Secondary Outline</button>
<button type="button" class="btn btn-success btn-lg">Large Success</button>
```
*   **Key Classes:** `.btn`, `.btn-{primary|secondary|success|danger|warning|info|light|dark|link}`, `.btn-outline-*`, `.btn-{lg|sm}`.

## 6. Alerts (`.alert`)

(Largely similar to v5, main difference is JS dependency and close button class)

```html
<div class="alert alert-success alert-dismissible fade show" role="alert">
  <strong>Well done!</strong> You successfully read this important alert message.
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
</div>
```
*   **Key Classes:** `.alert`, `.alert-*`, `.alert-dismissible`, `.fade`, `.show`, `.close`.
*   **JS:** Dismissible alerts require jQuery, Popper.js (v1), and Bootstrap JS bundle (or Alert component).

*(This is a subset. Refer to the official Bootstrap 4 documentation for all components and options: https://getbootstrap.com/docs/4.6/components/)*