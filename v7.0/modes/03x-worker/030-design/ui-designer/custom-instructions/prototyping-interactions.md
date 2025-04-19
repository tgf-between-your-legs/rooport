# UI Design: Describing Prototypes & Interactions

Guidance on documenting interactive prototypes and user flows conceptually using Markdown.

## Purpose of Documentation

Since this mode primarily describes designs rather than building interactive prototypes in a tool, the goal is to clearly communicate the intended user flow, transitions, animations, and component state changes so developers can implement the dynamic aspects correctly.

## Describing User Flows

*   **Use Numbered Lists or Flowcharts (Textual):** Outline the steps a user takes to complete a specific task.
*   **Identify Screens/States:** Clearly name or describe the different screens or states the user encounters.
*   **Describe Actions:** Specify the user action that triggers a transition (e.g., "User clicks 'Submit' button", "User taps on list item", "User scrolls down").
*   **Describe Transitions:** Explain how the UI changes between steps (e.g., "Navigate to Profile Screen", "Modal dialog appears", "Button enters loading state").

**Example User Flow Description (Markdown):**

```markdown
## User Flow: Adding Item to Cart

1.  **Start:** User is on the Product Detail Page (`/products/[id]`).
2.  **Action:** User clicks the "Add to Cart" button.
3.  **Transition/Feedback:**
    *   "Add to Cart" button enters a temporary loading state (e.g., shows spinner, text changes to "Adding...").
    *   (Optional: A small animation plays, like the product image moving towards the cart icon).
    *   Cart icon in the header updates its badge count (e.g., increments by 1).
    *   A confirmation message/toast appears briefly (e.g., "Item added to cart").
    *   "Add to Cart" button returns to its normal state.
4.  **End:** User remains on the Product Detail Page, cart is updated.

*(Alternative Flow: If adding fails)*
3a. **Transition/Feedback:**
    *   "Add to Cart" button enters loading state.
    *   An error message/toast appears (e.g., "Failed to add item. Please try again.").
    *   "Add to Cart" button returns to its normal state.
4a. **End:** User remains on the Product Detail Page, cart is unchanged.
```

## Describing Interactions & Micro-interactions

Focus on specific component behaviors and visual feedback.

*   **Identify Component & State:** Specify the component and the state being described (e.g., "Button - Hover State", "Input Field - Focus State", "Dropdown Menu - Opening Animation").
*   **Describe Trigger:** What causes the interaction (hover, focus, click, scroll, etc.)?
*   **Describe Visual Change:** Explain what happens visually. Use clear language.
    *   **Animation/Transition:** Describe the type of animation (fade, slide, scale), duration (fast, medium, slow - or specific ms if defined in style guide), and easing (linear, ease-in, ease-out).
    *   **Style Changes:** Mention changes in color, background, border, shadow, size, etc. (referencing style guide values).
    *   **Content Changes:** Describe changes in text or icons.

**Example Interaction Descriptions (Markdown):**

```markdown
### Component: Primary Button (`<Button variant="primary">`)

*   **Default State:** Background `bg-primary`, text `text-primary-foreground`.
*   **Hover State:** Background lightens (`bg-primary/90` or similar). Transition: `background-color` `duration-150` `ease-in-out`.
*   **Focus State:** Outline appears (`ring-2 ring-offset-2 ring-ring`).
*   **Active State (Pressed):** Background darkens slightly or scales down (`active:scale-95`).
*   **Disabled State:** Reduced opacity (`opacity-50`), cursor `cursor-not-allowed`.

### Component: Modal Dialog (`<Dialog>`)

*   **Opening Interaction:**
    *   Trigger: Click on "Open Dialog" button.
    *   Overlay: Fades in (`opacity-0` to `opacity-75`) over `duration-200`.
    *   Dialog Box: Scales up and fades in (`scale-95 opacity-0` to `scale-100 opacity-100`) over `duration-200` `ease-out`. Focus is trapped within the dialog.
*   **Closing Interaction:**
    *   Trigger: Click on "Close" button or overlay.
    *   Dialog Box: Scales down and fades out (`scale-100 opacity-100` to `scale-95 opacity-0`) over `duration-150` `ease-in`.
    *   Overlay: Fades out (`opacity-75` to `opacity-0`) over `duration-150`. Focus returns to the element that opened the dialog.
```

## Linking to Prototypes (If Applicable)

If another mode (like `one-shot-web-designer`) or an external tool is used to create an actual interactive prototype, link to it clearly within the documentation.

```markdown
**Interactive Prototype:** [Link to Figma/Codepen/etc.] - Demonstrates the checkout flow.
```

Clear descriptions of flows and interactions are crucial for developers to implement the intended dynamic behavior and feel of the user interface.