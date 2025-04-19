# UI Design: Describing Wireframes & Mockups

Guidance on documenting low-fidelity wireframes and high-fidelity mockups using Markdown.

## Purpose of Documentation

Since this mode primarily works conceptually and documents via text (Markdown), the goal is to clearly communicate the layout, structure, content hierarchy, visual style, and key elements of the design so that developers can implement it accurately.

## Describing Low-Fidelity Wireframes

Focus on structure, layout, content placement, and basic flow. Ignore visual details like colors, specific fonts, or exact spacing initially.

*   **Use Headings and Lists:** Structure the description logically using Markdown headings (`##`, `###`) for sections and lists (`*`, `-`, `1.`) for elements within sections.
*   **Describe Layout:** Explain the overall grid or layout structure (e.g., "Two-column layout", "Header-Content-Footer", "Sidebar navigation"). Mention key regions.
*   **Identify Key Elements:** List the main components or content blocks within each section (e.g., "Navigation Bar", "Hero Section", "Product List", "Call to Action Button"). Use placeholder text like `[Logo]`, `[Headline Text]`, `[Image Placeholder]`, `[Search Input]`.
*   **Indicate Hierarchy:** Use formatting (like bolding or indentation) or explicit notes to indicate the relative importance of elements.
*   **Basic Flow (Optional):** Briefly mention where primary actions lead (e.g., "Submit button leads to confirmation page").

**Example Wireframe Description (Markdown):**

```markdown
## Wireframe: User Profile Page

**Layout:** Single column layout with a fixed header.

### Header Section
*   [Logo] (Left-aligned)
*   Navigation Links: [Home], [Dashboard], [Settings] (Right-aligned)
*   [User Avatar/Dropdown] (Far right)

### Profile Banner Section
*   [Cover Image Placeholder] (Full width)
*   [Profile Picture Placeholder] (Overlapping bottom-left of cover image)
*   **[User Name]** (Large text, below profile picture)
*   [User Handle/Tagline] (Smaller text, below name)
*   [Edit Profile Button] (Right-aligned within this section)

### Main Content Section (Tabbed Interface)
*   Tabs: [Posts], [About], [Friends]
*   **Default View (Posts Tab):**
    *   List of [User Post Summaries]
        *   Each summary includes: [Post Text Snippet], [Timestamp], [Like/Comment Icons]
*   **(About Tab Content):**
    *   Section: Bio - [User Bio Text]
    *   Section: Details - List of [Detail Label]: [Detail Value] (e.g., Location, Joined Date)
*   **(Friends Tab Content):**
    *   Grid of [Friend Avatar + Name]

### Footer Section
*   [Copyright Text]
*   Links: [Privacy Policy], [Terms of Service]
```

## Describing High-Fidelity Mockups

Build upon the wireframe description, adding details about visual style, typography, color, spacing, and specific component states.

*   **Reference Style Guide:** Explicitly refer to the project's style guide or design system for colors, fonts, spacing units, etc. (e.g., "Use `primary-color` for buttons", "Heading uses `font-heading` at `text-2xl`").
*   **Specify Visual Details:**
    *   **Colors:** Mention specific color names/variables (e.g., `bg-primary`, `text-gray-700`, `border-red-500`).
    *   **Typography:** Specify font family, weight, size, line height (e.g., `font-sans font-bold text-xl leading-tight`).
    *   **Spacing:** Describe padding and margins using consistent units or references (e.g., `p-4`, `mb-6`, "Use spacing unit 3").
    *   **Imagery/Icons:** Describe the type or source of images/icons (e.g., "User-uploaded avatar", "Use `icon-settings` from icon library").
*   **Component States:** Describe variations like hover, focus, active, disabled states for interactive elements (buttons, inputs, links).
*   **Annotations:** Add notes for specific implementation details or rationale if necessary.

**Example Mockup Description (Markdown - Extending Wireframe):**

```markdown
## Mockup: User Profile Page

**References:** Project Style Guide v1.2

### Header Section
*   Logo: Use `logo.svg`. Max height 40px.
*   Navigation Links: Use `font-body`, `text-base`, `text-gray-700`. `hover:text-primary`. Spacing unit 4 between links.
*   User Avatar/Dropdown: 40x40px rounded avatar. On hover, show dropdown menu (use `Dropdown` component spec).

### Profile Banner Section
*   Cover Image: User-uploaded, aspect ratio 3:1. Default placeholder `cover-default.png`.
*   Profile Picture: 100x100px, `rounded-full`, `border-4 border-white`. Positioned -20px vertically from bottom edge of cover image.
*   User Name: `font-heading`, `font-bold`, `text-3xl`, `text-gray-900`, `mb-1`.
*   User Handle/Tagline: `font-body`, `text-gray-500`, `text-base`.
*   Edit Profile Button: Use `Button` component, `variant="outline"`, `size="sm"`.

### Main Content Section (Tabbed Interface)
*   Tabs: Use `Tabs` component spec. Active tab uses `border-b-2 border-primary`, `text-primary`. Inactive tabs `text-gray-500`.
*   **Default View (Posts Tab):**
    *   List uses `space-y-4`.
    *   Post Summaries: Use `Card` component spec. Timestamp `text-sm text-gray-500`. Icons use `icon-heart`, `icon-comment` (16px size).
*   **(About Tab Content):**
    *   Section headings: `font-semibold`, `text-lg`, `mb-2`. Detail labels `font-medium`.
*   **(Friends Tab Content):**
    *   Grid: `grid grid-cols-4 gap-4`. Friend Avatar `48x48px rounded-full`. Name `text-sm text-center`.

### Footer Section
*   Use `text-xs`, `text-gray-500`. Links `hover:underline`.
```

This detailed textual description, while not a visual tool, provides essential information for developers to implement the UI according to the design intent.