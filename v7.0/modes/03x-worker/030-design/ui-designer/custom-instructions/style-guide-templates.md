# Style Guide & Design System Documentation Templates

Templates for documenting visual styles and UI components in Markdown.

## Template 1: Basic Style Guide

```markdown
# Project Style Guide

## 1. Colors

### Primary Palette
*   Primary: `#XXXXXX` - Usage: ...
*   Secondary: `#XXXXXX` - Usage: ...
*   Accent: `#XXXXXX` - Usage: ...

### Neutrals
*   Background: `#XXXXXX`
*   Surface: `#XXXXXX`
*   Text Primary: `#XXXXXX`
*   Text Secondary: `#XXXXXX`
*   Borders: `#XXXXXX`

### Status Colors
*   Success: `#XXXXXX`
*   Warning: `#XXXXXX`
*   Error: `#XXXXXX`

## 2. Typography

*   **Heading Font:** [Font Name], [Fallback (e.g., sans-serif)]
*   **Body Font:** [Font Name], [Fallback]

### Type Scale (Base: 16px)
*   H1: [Size]rem, [Weight]
*   H2: [Size]rem, [Weight]
*   H3: [Size]rem, [Weight]
*   Body: 1rem, [Weight]
*   Small: [Size]rem, [Weight]

### Line Height
*   Body: [e.g., 1.6]

## 3. Spacing
*(Define base spacing unit or scale, e.g., 4px or 8px grid)*
*   Small: `var(--space-sm)` (e.g., 8px)
*   Medium: `var(--space-md)` (e.g., 16px)
*   Large: `var(--space-lg)` (e.g., 24px)

## 4. Key Components (Examples)

### Buttons
*   **Primary:** [Description of style, padding, border-radius]
*   **Secondary:** [Description of style]

### Cards
*   [Description of style, padding, shadow, border-radius]

```

## Template 2: Component Specification (Markdown)

```markdown
# Component: Button

## Description
Standard button component for user actions.

## Variations

### Primary Button
*   **Use Case:** Main call to action on a page.
*   **Visual Style:**
    *   Background: `var(--color-primary)`
    *   Text Color: `var(--color-text-on-primary)`
    *   Padding: `var(--space-sm) var(--space-md)`
    *   Border Radius: `var(--border-radius-sm)`
    *   Font Weight: `var(--font-weight-bold)`
*   **States:**
    *   `:hover`: [Describe hover style, e.g., Darken background]
    *   `:active`: [Describe active style, e.g., Inset shadow]
    *   `:focus`: [Describe focus style, e.g., Outline using accent color]
    *   `:disabled`: [Describe disabled style, e.g., Grayed out, no pointer events]

### Secondary Button
*   **Use Case:** Secondary actions.
*   **Visual Style:**
    *   Background: `var(--color-secondary)` or `transparent`
    *   Border: `1px solid var(--color-secondary)`
    *   Text Color: `var(--color-secondary)` or `var(--color-text-primary)`
    *   ... (Padding, etc.)
*   **States:** ...

## Accessibility
*   Ensure sufficient color contrast between text and background (WCAG AA).
*   Ensure clear `:focus` state for keyboard navigation.
*   Use `<button>` element or `role="button"` appropriately.

## Responsiveness
*   Padding may adjust slightly on smaller screens.
*   Ensure minimum touch target size (44x44px).

```

*(Adapt these templates. The goal is clear documentation for developers implementing the designs.)*