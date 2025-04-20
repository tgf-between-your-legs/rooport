# Tailwind CSS: Utility-First Basics & Common Utilities

Understanding the core concept of Tailwind's utility-first approach and a quick reference for common utilities.

## 1. Core Concept: Utility-First CSS

Instead of writing custom CSS classes that bundle multiple style declarations (like `.button { padding: 1rem; background-color: blue; color: white; }`), Tailwind provides low-level **utility classes** that each map directly to a single CSS property.

**Example:**

*   Instead of `<button class="button">`, you write:
    `<button class="py-2 px-4 bg-blue-500 text-white rounded">`

**Breakdown:**

*   `py-2`: Sets `padding-top` and `padding-bottom` to `0.5rem` (Tailwind's scale `2`).
*   `px-4`: Sets `padding-left` and `padding-right` to `1rem` (Tailwind's scale `4`).
*   `bg-blue-500`: Sets `background-color` to a specific shade of blue from the configured theme.
*   `text-white`: Sets `color` to white.
*   `rounded`: Applies a default `border-radius`.

**Benefits:**

*   **No Naming Things:** Avoids the cognitive load of naming CSS classes.
*   **Direct Styling:** Styles are applied directly in the HTML/JSX, making it easier to see how an element is styled without switching files.
*   **Consistency:** Uses a predefined design system (theme) for spacing, colors, fonts, etc., leading to more consistent UIs.
*   **Smaller CSS:** Production builds only include the utility classes actually used in your project, resulting in very small CSS files.
*   **Easier Changes:** Modifying styles involves changing utility classes in the template, not potentially affecting multiple elements via a shared CSS class.

## 2. Applying Utilities

Simply add the relevant utility classes to the `class` attribute of your HTML elements.

```html
<!-- Simple Card Example -->
<div class="max-w-sm rounded overflow-hidden shadow-lg bg-white p-6 border border-gray-200">
  <div class="font-bold text-xl mb-2 text-gray-800">Card Title</div>
  <p class="text-gray-700 text-base mb-4">
    This is some card content using Tailwind utility classes for styling.
  </p>
  <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring-2 focus:ring-blue-300">
    Action Button
  </button>
</div>

<!-- Flexbox Layout Example -->
<div class="flex items-center space-x-4 p-4 bg-slate-100">
  <img class="w-10 h-10 rounded-full" src="/path/to/avatar.jpg" alt="User Avatar">
  <div>
    <div class="text-lg font-medium text-black">Erin Lindford</div>
    <p class="text-slate-500">Product Engineer</p>
  </div>
</div>
```

## 3. Common Utilities Quick Reference

A non-exhaustive list of frequently used Tailwind utility classes.
**(Note: Refer to official Tailwind docs for the complete list and specific values)**

### Layout & Box Model

*   **Display:** `block`, `inline-block`, `inline`, `flex`, `inline-flex`, `grid`, `inline-grid`, `hidden`
*   **Position:** `static`, `relative`, `absolute`, `fixed`, `sticky`
*   **Top/Right/Bottom/Left:** `top-0`, `right-4`, `bottom-auto`, `left-1/2`, `-top-2`, `inset-0`, `inset-x-0`, `inset-y-4`
*   **Visibility:** `visible`, `invisible`
*   **Z-Index:** `z-0`, `z-10`, `z-auto`
*   **Box Sizing:** `box-border`, `box-content`
*   **Width:** `w-0`, `w-px`, `w-4` (1rem), `w-full`, `w-screen`, `w-1/2`, `w-auto`, `w-fit`, `w-min`, `w-max`
*   **Height:** `h-0`, `h-px`, `h-4` (1rem), `h-full`, `h-screen`, `h-auto`, `h-fit`, `h-min`, `h-max`
*   **Min/Max Width/Height:** `min-w-0`, `max-w-xs`, `min-h-screen`, `max-h-full`
*   **Padding:** `p-0`, `p-4` (1rem), `px-2` (x-axis), `py-1` (y-axis), `pt-6` (top), `pr-4` (right), `pb-8` (bottom), `pl-2` (left)
*   **Margin:** `m-0`, `m-4` (1rem), `mx-auto` (center block), `my-2` (y-axis), `-mt-1` (negative top), `space-x-4` (space between flex/grid children), `space-y-2`
*   **Overflow:** `overflow-auto`, `overflow-hidden`, `overflow-visible`, `overflow-scroll`, `overflow-x-auto`

### Flexbox & Grid

*   **Flexbox:**
    *   `flex` (display: flex)
    *   `flex-row`, `flex-col`, `flex-row-reverse`, `flex-col-reverse` (direction)
    *   `flex-wrap`, `flex-nowrap`, `flex-wrap-reverse`
    *   `flex-1`, `flex-auto`, `flex-initial`, `flex-none` (grow/shrink/basis)
    *   `grow`, `grow-0`, `shrink`, `shrink-0`
    *   `items-start`, `items-end`, `items-center`, `items-baseline`, `items-stretch` (align-items)
    *   `justify-start`, `justify-end`, `justify-center`, `justify-between`, `justify-around`, `justify-evenly` (justify-content)
*   **Grid:**
    *   `grid` (display: grid)
    *   `grid-cols-1`, `grid-cols-3`, `grid-cols-none`, `grid-cols-[200px_1fr]` (columns template)
    *   `grid-rows-1`, `grid-rows-[auto_1fr_auto]` (rows template)
    *   `col-span-1`, `col-span-2`, `col-start-2`, `col-end-4`
    *   `row-span-1`, `row-start-1`, `row-end-3`
    *   `gap-4`, `gap-x-2`, `gap-y-8` (gutters)
    *   `place-items-center`, `justify-items-start`, `align-items-end`

### Typography

*   **Font Family:** `font-sans`, `font-serif`, `font-mono` (defined in config)
*   **Font Size:** `text-xs`, `text-sm`, `text-base` (1rem), `text-lg`, `text-xl`, `text-2xl` ... `text-9xl`
*   **Font Weight:** `font-thin`, `font-extralight`, `font-light`, `font-normal`, `font-medium`, `font-semibold`, `font-bold`, `font-extrabold`, `font-black`
*   **Text Align:** `text-left`, `text-center`, `text-right`, `text-justify`
*   **Text Color:** `text-black`, `text-white`, `text-gray-500`, `text-red-600`, `text-primary`, `text-secondary-foreground` (uses theme colors)
*   **Text Decoration:** `underline`, `overline`, `line-through`, `no-underline`
*   **Letter Spacing:** `tracking-tighter`, `tracking-tight`, `tracking-normal`, `tracking-wide`, `tracking-wider`, `tracking-widest`
*   **Line Height:** `leading-none`, `leading-tight`, `leading-snug`, `leading-normal`, `leading-relaxed`, `leading-loose`

### Backgrounds & Borders

*   **Background Color:** `bg-transparent`, `bg-black`, `bg-white`, `bg-gray-100`, `bg-blue-500`, `bg-primary`, `bg-destructive` (uses theme colors)
*   **Border Radius:** `rounded-none`, `rounded-sm`, `rounded`, `rounded-md`, `rounded-lg`, `rounded-xl`, `rounded-full`, `rounded-t-lg` (top only), `rounded-r-md` (right only)
*   **Border Width:** `border-0`, `border`, `border-2`, `border-4`, `border-t`, `border-r-2`
*   **Border Color:** `border-transparent`, `border-black`, `border-gray-300`, `border-blue-500`, `border-primary` (uses theme colors)
*   **Border Style:** `border-solid`, `border-dashed`, `border-dotted`, `border-double`, `border-none`

### Effects & Transitions

*   **Box Shadow:** `shadow-sm`, `shadow`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl`, `shadow-inner`, `shadow-none`
*   **Opacity:** `opacity-0`, `opacity-25`, `opacity-50`, `opacity-75`, `opacity-100`
*   **Transition Property:** `transition-none`, `transition-all`, `transition`, `transition-colors`, `transition-opacity`, `transition-shadow`, `transition-transform`
*   **Transition Duration:** `duration-75`, `duration-100`, ... `duration-1000`
*   **Transition Timing Function:** `ease-linear`, `ease-in`, `ease-out`, `ease-in-out`
*   **Transition Delay:** `delay-75`, `delay-100`, ... `delay-1000`

### Interactivity

*   **Cursor:** `cursor-auto`, `cursor-default`, `cursor-pointer`, `cursor-wait`, `cursor-not-allowed`
*   **Appearance:** `appearance-none`
*   **Pointer Events:** `pointer-events-none`, `pointer-events-auto`
*   **User Select:** `select-none`, `select-text`, `select-all`, `select-auto`

*(This is just a sample. Always check the official Tailwind CSS documentation for the most up-to-date and complete list of utilities and their values.)*