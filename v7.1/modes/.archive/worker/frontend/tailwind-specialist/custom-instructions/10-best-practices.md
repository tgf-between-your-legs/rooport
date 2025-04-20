# Tailwind CSS: Best Practices

Tips and conventions for writing maintainable and effective Tailwind CSS.

## 1. Embrace Utility-First

*   **Apply utilities directly in HTML/JSX:** This is the core principle. Keep styles co-located with the markup they affect.
*   **Avoid premature abstraction:** Don't immediately create custom CSS classes or framework components for every small pattern. Wait until you see genuine repetition that warrants abstraction.

## 2. Use `@apply` Sparingly

*   **When to consider `@apply`:**
    *   Extracting *highly repeated*, complex utility combinations, especially for interactive elements like buttons or form inputs where consistency across many instances is crucial.
    *   Applying styles to content coming from a CMS or Markdown where you can't directly add utility classes to the HTML tags (though the `@tailwindcss/typography` plugin is often better for this).
    *   Applying base styles within `@layer base`.
*   **Why sparingly?**
    *   Reintroduces class naming.
    *   Hides styling details away from the markup.
    *   Can increase CSS bundle size if not managed carefully (though purging helps).
    *   Can lead to specificity issues if not organized with `@layer`.
*   **Alternative: Component Abstraction:** In frameworks like React, Vue, or Svelte, creating reusable components (e.g., `<Button variant="primary">`) is often a better way to handle repeated patterns than using `@apply` to create CSS classes like `.button-primary`.

```css
/* Less ideal: Overuse of @apply */
.card { @apply rounded shadow-lg p-4 border; }
.card-title { @apply font-bold text-xl mb-2; }
.card-body { @apply text-gray-700; }

/* Better: Use utilities directly or create framework components */
```

## 3. Configure `content` Correctly

*   Ensure your `tailwind.config.js` `content` array includes **all** file paths where you use Tailwind classes.
*   Incorrect configuration leads to necessary styles being purged in production. (See `08-optimization-purging.md`).

## 4. Leverage `tailwind.config.js` for Consistency

*   **Define your design system:** Use `theme` and `theme.extend` to define your project's color palette, spacing scale, font sizes, breakpoints, etc. (See `03-configuration.md`).
*   **Avoid magic numbers:** Instead of arbitrary values like `mt-[13px]`, use theme values (`mt-3`, `mt-4`) or add the specific value to your theme config if it's truly part of your design system (`theme.extend.spacing: { '3.25': '13px' }`).
*   **Use CSS Variables for Theming:** Especially useful with dark mode or multi-theme setups (see `06-dark-mode.md`).

## 5. Keep Specificity Low

*   Tailwind's utility-first nature generally keeps specificity low.
*   When adding custom CSS, use `@layer base | components | utilities` to ensure your styles integrate correctly with Tailwind's layers and avoid specificity conflicts. Utilities should generally "win". (See `07-functions-directives.md`).

## 6. Order Classes Consistently (Optional but Helpful)

*   While not functionally required, establishing a consistent order for utility classes can improve readability. A common convention:
    1.  Layout (display, position, grid, flex)
    2.  Sizing (width, height)
    3.  Spacing (padding, margin)
    4.  Typography (font, text size/color/weight)
    5.  Backgrounds
    6.  Borders
    7.  Effects (shadow, opacity)
    8.  States & Responsive Prefixes (often grouped with the utility they modify, e.g., `bg-blue-500 hover:bg-blue-700 md:bg-green-500`)
*   Tools like `prettier-plugin-tailwindcss` can automatically sort classes according to a recommended order.

## 7. Understand the Build Process

*   Know how Tailwind integrates with PostCSS and your specific build tool (Vite, Next.js, etc.). (See `09-postcss-integration.md`).
*   Understand the difference between development (all utilities) and production (purged) builds.

By following these practices, you can leverage the power of Tailwind CSS to build UIs quickly while maintaining consistency, performance, and readability.