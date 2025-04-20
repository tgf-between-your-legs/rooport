# UI Design: Style Guide / Design System Components Checklist

Elements to define when documenting a visual style guide or components for a design system (using Markdown).

## Core Goal

To create a single source of truth for the visual language and reusable UI components of the application, ensuring consistency and speeding up both design and development.

## I. Foundations

*   **Colors:**
    *   [ ] **Primary Colors:** Define main brand colors (e.g., primary, secondary). Provide names, hex/HSL values, and usage context.
    *   [ ] **Accent Colors:** Colors for calls to action, highlights, or specific states.
    *   [ ] **Neutral Colors:** Grayscale palette (e.g., black, white, grays for text, backgrounds, borders). Define steps (e.g., gray-100 to gray-900).
    *   [ ] **Feedback Colors:** Colors for success, error, warning, info states.
    *   [ ] **Accessibility:** Note contrast ratios against backgrounds for text colors (aim for WCAG AA or AAA).
*   **Typography:**
    *   [ ] **Font Families:** Specify primary (headings) and secondary (body text) font families and fallbacks. Link to font files or services if applicable.
    *   [ ] **Font Scale:** Define a type scale (e.g., `text-xs`, `text-sm`, `text-base`, `text-lg`, `text-xl`, ...). Specify font size (px/rem) and line height for each step.
    *   [ ] **Font Weights:** Define available weights (e.g., normal, medium, semibold, bold) and their usage.
    *   [ ] **Usage Examples:** Show examples for headings (H1-H6), body text, captions, labels, links.
*   **Spacing:**
    *   [ ] **Spacing Scale:** Define a consistent spacing scale (e.g., using multiples of 4px or 8px) for margins, padding, and layout gaps. Assign names or numbers (e.g., `space-1`, `space-2`, ... or `p-4`, `m-8`).
    *   [ ] **Layout Units:** Specify standard widths for containers, columns, etc.
*   **Iconography:**
    *   [ ] **Icon Set:** Specify the icon library used (e.g., Lucide, Font Awesome, Material Icons) or link to custom icon files (SVG).
    *   [ ] **Sizes:** Define standard icon sizes (e.g., 16px, 20px, 24px).
    *   [ ] **Usage:** Guidelines on color, stroke width (if applicable), and context.
*   **Border Radius:**
    *   [ ] **Radius Scale:** Define standard border radius values (e.g., `rounded-sm`, `rounded`, `rounded-md`, `rounded-lg`, `rounded-full`). Specify pixel or rem values.
*   **Shadows:**
    *   [ ] **Elevation Scale:** Define standard box shadow values for different elevation levels (e.g., `shadow-sm`, `shadow`, `shadow-md`, `shadow-lg`).

## II. Components

For each reusable component (Button, Input, Card, Modal, etc.), document:

*   **Name:** Clear component name (e.g., "Primary Button", "Text Input", "User Avatar").
*   **Description:** Brief explanation of its purpose and usage context.
*   **Visual Mockup/Description:**
    *   Describe its appearance using references to the Foundations section (colors, typography, spacing, etc.).
    *   Include variations (e.g., Button variants: primary, secondary, destructive; Input sizes: small, medium, large).
    *   Describe different states (hover, focus, active, disabled, error).
*   **Structure (Conceptual):** Briefly describe the key parts if it's a composite component (e.g., Card has Header, Content, Footer).
*   **Interaction:** Describe key interactions or behaviors (e.g., "Modal traps focus", "Dropdown closes on outside click").
*   **Responsiveness:** How does the component adapt to different screen sizes?
*   **Accessibility:** Key considerations (e.g., "Ensure sufficient contrast", "Supports keyboard navigation", "Use appropriate ARIA attributes" - coordinate with Accessibility Specialist for details).
*   **Usage Do's and Don'ts:** Provide guidance on correct and incorrect usage.

**Example Component Documentation (Markdown):**

```markdown
### Component: Primary Button

*   **Description:** Used for the main call to action on a page or within a component.
*   **Visual:**
    *   Background: `primary` color.
    *   Text: `primary-foreground` color, `font-medium`, `text-base`.
    *   Padding: `py-2 px-4` (maps to spacing unit X).
    *   Border Radius: `rounded-md` (maps to radius Y).
    *   Hover State: Background `primary-hover` (slightly darker/lighter).
    *   Focus State: Outline `ring-2 ring-offset-2 ring-primary`.
    *   Active State: Background `primary-active` (darker/lighter).
    *   Disabled State: `opacity-50`, `cursor-not-allowed`.
*   **Accessibility:** Ensure text has sufficient contrast against background. Focus state must be clearly visible.
*   **Usage:** Use sparingly, typically once per view, for the most important action.
```

## III. Layout Patterns (Optional)

*   Define common page layouts (e.g., "Sidebar Layout", "Centered Content Layout").
*   Specify grid systems or column structures.

Maintaining this documentation helps ensure consistency and provides a valuable resource for both designers and developers.