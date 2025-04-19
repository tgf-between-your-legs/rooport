# Bootstrap: Utility Classes (v4 & v5)

Leveraging Bootstrap's utility classes for common styling adjustments.

## Core Concept

Bootstrap provides a vast collection of single-purpose **utility classes** to apply common styles directly in your HTML, reducing the need for custom CSS for many layout and styling tasks. They are designed to be responsive and cover areas like spacing, display, flexbox, text, color, borders, and more.

**Key Advantages:**

*   **Rapid Development:** Quickly apply styles without writing custom CSS.
*   **Consistency:** Enforces consistent spacing, sizing, etc., based on the Bootstrap theme.
*   **Responsiveness:** Many utilities have responsive variants (e.g., `d-none d-md-block`).
*   **Customization (v5):** The Utility API in Bootstrap 5 allows modifying, adding, or removing utilities via Sass.

**Note:** While utilities are powerful, overuse can sometimes lead to cluttered HTML. Balance utility usage with custom CSS for complex or highly specific component styling.

## Common Utility Categories (Focus on v5, mention v4 differences)

**1. Spacing (`margin` & `padding`):**

*   **Format:** `{property}{sides}-{breakpoint}-{size}`
*   **Properties:** `m` (margin), `p` (padding).
*   **Sides:**
    *   `t` (top), `b` (bottom), `s` (start - left in LTR, right in RTL), `e` (end - right in LTR, left in RTL)
    *   `x` (left & right), `y` (top & bottom)
    *   Blank (all 4 sides)
*   **Breakpoint (Optional):** `sm`, `md`, `lg`, `xl`, `xxl` (e.g., `mt-md-3`). Applies from that breakpoint *up*.
*   **Size:**
    *   `0` - `0`
    *   `1` - `$spacer * .25` (Default: 4px)
    *   `2` - `$spacer * .5` (Default: 8px)
    *   `3` - `$spacer * 1` (Default: 16px)
    *   `4` - `$spacer * 1.5` (Default: 24px)
    *   `5` - `$spacer * 3` (Default: 48px)
    *   `auto` - Sets margin to `auto` (useful for centering block elements with fixed width: `mx-auto`).
*   **Negative Margins (v5):** Prepend `n` to the size (e.g., `mt-n1`, `mx-n3`). *Not available in v4.*

```html
<!-- Bootstrap 5 Examples -->
<div class="mt-3 mb-4 ps-5 pe-md-2">...</div> {/* Margin top 3, margin bottom 4, padding start 5, padding end 2 on md+ */}
<div class="mx-auto" style="width: 200px;">Centered block</div>
<div class="m-n2">Negative margin</div> {/* v5 only */}

<!-- Bootstrap 4 Examples -->
<!-- <div class="mt-3 mb-4 pl-5 pr-md-2">...</div> --> {/* Uses pl/pr instead of ps/pe */}
<!-- <div class="mx-auto" style="width: 200px;">Centered block</div> -->
```

**2. Display:**

*   **Format:** `d-{value}` or `d-{breakpoint}-{value}`
*   **Values:** `none`, `inline`, `inline-block`, `block`, `grid`, `table`, `table-cell`, `table-row`, `flex`, `inline-flex`.
*   **Use:** Control element visibility and layout behavior responsively.
*   **Print:** `.d-print-none`, `.d-print-block`, etc.

```html
<div class="d-none d-lg-block">Visible only on large screens and up</div>
<div class="d-flex justify-content-center">Flex container</div>
<span class="d-block">Span displayed as block</span>
```

**3. Flexbox:**

*   **Enable Flex:** `d-flex`, `d-inline-flex`, `d-{breakpoint}-flex`, etc.
*   **Direction:** `.flex-row`, `.flex-row-reverse`, `.flex-column`, `.flex-column-reverse` (and responsive variants).
*   **Justify Content:** `.justify-content-{start|end|center|between|around|evenly}` (and responsive variants).
*   **Align Items:** `.align-items-{start|end|center|baseline|stretch}` (and responsive variants).
*   **Align Self:** `.align-self-{start|end|center|baseline|stretch}` (on individual flex items).
*   **Fill:** `.flex-fill` (makes item take available space).
*   **Grow/Shrink:** `.flex-grow-{0|1}`, `.flex-shrink-{0|1}`.
*   **Wrap:** `.flex-wrap`, `.flex-nowrap`, `.flex-wrap-reverse`.
*   **Order:** `.order-*` (See Grid section).
*   **Align Content (for multi-line wrap):** `.align-content-{start|end|center|between|around|stretch}`

```html
<div class="d-flex justify-content-between align-items-center">
  <div>Item 1</div>
  <div class="order-3">Item 2 (Visually Last)</div>
  <div class="order-2">Item 3 (Visually Middle)</div>
</div>
```

**4. Text:**

*   **Alignment:** `.text-{start|center|end}` (and responsive variants). *v4 used `text-{left|center|right}`.*
*   **Wrapping:** `.text-wrap`, `.text-nowrap`, `.text-break`.
*   **Transform:** `.text-{lowercase|uppercase|capitalize}`.
*   **Font Size (v5):** `.fs-{1-6}` (relative to heading sizes), `.fs-small`, `.fs-large`. *v4 used `.h{1-6}` classes or responsive display classes.*
*   **Font Weight/Style:** `.fw-bold`, `.fw-bolder`, `.fw-semibold` (v5), `.fw-normal`, `.fw-light`, `.fw-lighter` (v5), `.fst-italic`, `.fst-normal` (v5). *v4 used `.font-weight-*` and `.font-italic`.*
*   **Line Height:** `.lh-{1|sm|base|lg}` (v5).
*   **Color:** `.text-{primary|secondary|success|danger|warning|info|light|dark|white|body|muted|black-50|white-50}`.
*   **Decoration:** `.text-decoration-none`, `.text-decoration-underline`, `.text-decoration-line-through`.
*   **Misc:** `.text-muted`, `.text-reset`, `.text-decoration-none`.

**5. Colors & Background:**

*   **Text Color:** `.text-{theme-color|white|muted|body|black-50|white-50}`.
*   **Background Color:** `.bg-{theme-color|white|transparent|body}`.
*   **Gradient:** `.bg-gradient` (adds gradient, often used with `.bg-*`).
*   **Opacity (v5):** `.opacity-{100|75|50|25}`, `.bg-opacity-{10|25|50|75}`.

**6. Borders:**

*   **Add/Remove:** `.border`, `.border-0`, `.border-top-0`, etc.
*   **Color:** `.border-{theme-color|white}`.
*   **Width (v5):** `.border-{1-5}`.
*   **Radius:** `.rounded`, `.rounded-{top|bottom|start|end|circle|pill}`, `.rounded-{0-3}` (size). *v4 used `left/right` instead of `start/end`.*

**7. Sizing:**

*   **Width:** `.w-{25|50|75|100|auto}`.
*   **Height:** `.h-{25|50|75|100|auto}`.
*   **Max Width/Height:** `.mw-100`, `.mh-100`.
*   **Viewport Width/Height:** `.vw-100`, `.vh-100`, `.min-vw-100`, `.min-vh-100`.

**8. Visibility:**

*   `.visible`, `.invisible`. Affects visibility but element still takes up space (unlike `d-none`).

**9. Shadows:**

*   `.shadow-none`, `.shadow-sm`, `.shadow`, `.shadow-lg`.

Utilities provide immense flexibility. Combine them strategically to build complex layouts and styles quickly. Refer to the official documentation for the complete list and specific version details.

*(Refer to the official Bootstrap Utilities documentation for your target version.)*