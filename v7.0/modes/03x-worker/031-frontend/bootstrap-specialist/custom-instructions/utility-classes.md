# Bootstrap 5 Utility Classes Quick Reference

A selection of common Bootstrap 5 utility classes for quick styling.

## Spacing (`m-*`, `p-*`)

*   **Format:** `{property}{sides}-{breakpoint}-{size}`
*   **Property:** `m` (margin), `p` (padding).
*   **Sides:**
    *   `t` (top), `b` (bottom), `s` (start - left in LTR, right in RTL), `e` (end - right in LTR, left in RTL)
    *   `x` (left and right), `y` (top and bottom)
    *   *(blank)* (all 4 sides)
*   **Breakpoint (Optional):** `sm`, `md`, `lg`, `xl`, `xxl`. Applies from that breakpoint and up.
*   **Size:**
    *   `0` - 0
    *   `1` - `$spacer * .25` (Default: 4px)
    *   `2` - `$spacer * .5` (Default: 8px)
    *   `3` - `$spacer * 1` (Default: 16px)
    *   `4` - `$spacer * 1.5` (Default: 24px)
    *   `5` - `$spacer * 3` (Default: 48px)
    *   `auto` - Sets margin to auto (useful for centering block elements with fixed width: `mx-auto`).
*   **Examples:**
    *   `.mt-3`: Margin top size 3 (16px).
    *   `.px-sm-2`: Padding left and right size 2 (8px) from `sm` breakpoint up.
    *   `.m-0`: Margin 0 on all sides.
    *   `.pb-5`: Padding bottom size 5 (48px).

## Flexbox (`d-flex`, etc.)

*   **Enable Flex:** `.d-flex`, `.d-inline-flex`, `.d-{bp}-flex`, `.d-{bp}-inline-flex`
*   **Direction:** `.flex-row`, `.flex-row-reverse`, `.flex-column`, `.flex-column-reverse` (and responsive `.flex-{bp}-*`)
*   **Justify Content:** `.justify-content-{start|end|center|between|around|evenly}` (and responsive)
*   **Align Items:** `.align-items-{start|end|center|baseline|stretch}` (and responsive)
*   **Align Self:** `.align-self-{start|end|center|baseline|stretch}` (on individual flex items)
*   **Fill:** `.flex-fill` (item takes available space)
*   **Grow/Shrink:** `.flex-grow-{0|1}`, `.flex-shrink-{0|1}`
*   **Wrap:** `.flex-nowrap`, `.flex-wrap`, `.flex-wrap-reverse`
*   **Order:** `.order-{0-5}` (and responsive)
*   **Align Content (for multi-line wrap):** `.align-content-{start|end|center|between|around|stretch}`

## Display (`d-*`)

*   `.d-none`, `.d-inline`, `.d-inline-block`, `.d-block`, `.d-grid`, `.d-table`, `.d-table-cell`, `.d-table-row`, `.d-flex`, `.d-inline-flex`
*   Responsive: `.d-{bp}-{value}` (e.g., `.d-lg-none` hides on lg and up, `.d-md-block` displays as block on md and up).
*   Print: `.d-print-none`, `.d-print-block`, etc.

## Text (`text-*`, `fs-*`, `fw-*`, etc.)

*   **Alignment:** `.text-start`, `.text-center`, `.text-end` (and responsive `.text-{bp}-*`)
*   **Wrapping:** `.text-wrap`, `.text-nowrap`, `.text-break`
*   **Transform:** `.text-lowercase`, `.text-uppercase`, `.text-capitalize`
*   **Font Size:** `.fs-{1-6}` (relative to heading sizes), `.fs-small`, `.fs-large`
*   **Font Weight:** `.fw-bold`, `.fw-bolder`, `.fw-semibold`, `.fw-normal`, `.fw-light`, `.fw-lighter`
*   **Font Style:** `.fst-italic`, `.fst-normal`
*   **Line Height:** `.lh-{1|sm|base|lg}`
*   **Color:** `.text-{primary|secondary|success|danger|warning|info|light|dark|white|muted|body|black-50|white-50}`
*   **Decoration:** `.text-decoration-none`, `.text-decoration-underline`, `.text-decoration-line-through`
*   **Reset:** `.text-reset` (resets color)

## Background (`bg-*`)

*   `.bg-{primary|secondary|success|danger|warning|info|light|dark|white|transparent|body}`
*   `.bg-gradient` (adds gradient, often used with `.bg-*`)
*   `.bg-opacity-{10|25|50|75}`

## Borders (`border-*`)

*   **Add:** `.border`, `.border-top`, `.border-end`, `.border-bottom`, `.border-start`
*   **Remove:** `.border-0`, `.border-top-0`, etc.
*   **Color:** `.border-{primary|secondary|success|danger|warning|info|light|dark|white}`
*   **Width:** `.border-{1-5}`
*   **Radius:** `.rounded`, `.rounded-{top|bottom|start|end|circle|pill}`, `.rounded-{0-3}` (size)

## Sizing (`w-*`, `h-*`)

*   **Width/Height:** `.w-{25|50|75|100|auto}`, `.h-{25|50|75|100|auto}`
*   **Max Width/Height:** `.mw-100`, `.mh-100`
*   **Viewport Width/Height:** `.vw-100`, `.vh-100`, `.min-vw-100`, `.min-vh-100`

*(This is a selection. Refer to the official Bootstrap 5 Utilities documentation for the complete list: https://getbootstrap.com/docs/5.3/utilities/)*