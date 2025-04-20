# Common Accessibility Fixes (Code Examples)

Examples of code changes to address common accessibility issues.

## 1. Missing Alt Text (WCAG 1.1.1)

**Problem:** Image without `alt` attribute.
```html
<img src="logo.png">
```

**Fix (Informative Image):** Add descriptive `alt` text.
```html
<img src="logo.png" alt="Example Company Logo">
```

**Fix (Decorative Image):** Add empty `alt` attribute.
```html
<img src="decorative-swirl.png" alt="">
```

## 2. Missing Form Labels (WCAG 1.3.1, 3.3.2, 4.1.2)

**Problem:** Input field without an associated label.
```html
<input type="text" id="username">
```

**Fix (Using `<label for="...">`):**
```html
<label for="username">Username:</label>
<input type="text" id="username">
```

**Fix (Using `aria-label` - if no visible label):**
```html
<input type="search" aria-label="Search site">
```

**Fix (Using `aria-labelledby` - referencing existing visible text):**
```html
<span id="search-label">Search:</span>
<input type="search" aria-labelledby="search-label">
```

## 3. Insufficient Color Contrast (WCAG 1.4.3)

**Problem:** Light gray text on white background.
```css
.subtle-text {
  color: #cccccc; /* Contrast ratio too low */
  background-color: #ffffff;
}
```

**Fix:** Adjust color to meet 4.5:1 ratio (use a contrast checker).
```css
.subtle-text {
  color: #595959; /* Example: Meets AA contrast */
  background-color: #ffffff;
}
```

## 4. Non-Visible Focus Indicator (WCAG 2.4.7)

**Problem:** Focus outline removed globally.
```css
*:focus {
  outline: none; /* Problematic! */
}
```

**Fix:** Ensure a visible focus style (browser default or custom).
```css
/* Allow default outline (recommended) OR define a clear custom style */
a:focus, button:focus, input:focus {
  outline: 2px solid blue; /* Example custom focus */
  outline-offset: 2px;
}
```

## 5. Non-Semantic Button (WCAG 4.1.2)

**Problem:** Using a `<div>` as a button without ARIA.
```html
<div class="button-style" onclick="doSomething()">Click Me</div>
```

**Fix (Best: Use Native Button):**
```html
<button type="button" class="button-style" onclick="doSomething()">Click Me</button>
```

**Fix (Alternative: ARIA Role - requires keyboard handling JS):**
```html
<div class="button-style" role="button" tabindex="0" onclick="doSomething()" onkeydown="handleKeydown(event)">Click Me</div>
<!-- Need JavaScript to handle Enter/Space key presses for activation -->
```

## 6. Missing Landmark Roles (WCAG 1.3.1, 2.4.1)

**Problem:** Generic `<div>`s used for major page sections.
```html
<div id="header">...</div>
<div id="main-content">...</div>
<div id="footer">...</div>
```

**Fix:** Use semantic HTML5 elements or ARIA landmark roles.
```html
<header>...</header> <!-- Or <div role="banner"> -->
<main>...</main> <!-- Or <div role="main"> -->
<footer>...</footer> <!-- Or <div role="contentinfo"> -->
<nav>...</nav> <!-- Or <div role="navigation"> -->
<aside>...</aside> <!-- Or <div role="complementary"> -->
```

*(These are basic examples. Complex widgets often require more intricate ARIA and JavaScript. Refer to WAI-ARIA Authoring Practices.)*