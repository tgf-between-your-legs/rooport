# Accessibility: Screen Reader Testing Basics (VoiceOver & NVDA)

Basic steps for testing web content with common screen readers.

## Core Concept

Screen readers are assistive technologies that read web content aloud, allowing users who are blind or have low vision to navigate and interact with websites and applications. Testing with screen readers is essential to ensure content is understandable and operable without relying on visual cues.

**Common Screen Readers:**

*   **NVDA (NonVisual Desktop Access):** Free, open-source screen reader for Windows.
*   **VoiceOver:** Built-in screen reader for macOS and iOS.
*   **JAWS:** Popular commercial screen reader for Windows.
*   **TalkBack:** Built-in screen reader for Android.

This guide focuses on basic testing with NVDA and VoiceOver.

## General Testing Approach

1.  **Learn Basic Commands:** Familiarize yourself with the essential navigation commands for the screen reader you are using (see below). Turn off your monitor or avert your eyes to simulate the non-visual experience.
2.  **Navigate Sequentially:** Let the screen reader read through the page content linearly. Does the reading order make sense? Is all relevant content read out? Is anything skipped or read unexpectedly?
3.  **Navigate by Structure:** Use screen reader commands to navigate by headings, landmarks, links, form controls, tables, etc.
    *   Can you quickly understand the page structure using headings? Are headings used correctly and hierarchically?
    *   Can you navigate between major page regions using landmarks? Are landmarks correctly identified (`<nav>`, `<main>`, etc.)?
    *   Can you list and navigate through all links? Is the purpose of each link clear from its text (or context)?
    *   Can you list and navigate through form controls? Are labels read correctly for each input? Are instructions or error messages announced?
4.  **Interact with Controls:** Try operating interactive elements (buttons, links, form fields, custom widgets) using only the keyboard and screen reader commands.
    *   Is the element's name (label), role (type of control), and state (e.g., checked, expanded, disabled) announced correctly?
    *   Does the screen reader announce changes when you interact with the control (e.g., checking a box, expanding a section)?
    *   Can you complete forms successfully?
5.  **Check Dynamic Content:** If content updates dynamically (e.g., error messages appearing, live search results), does the screen reader announce the update appropriately (consider `aria-live`)?

## Basic NVDA Commands (Windows)

*   **Start/Exit NVDA:** `Ctrl + Alt + N`
*   **Stop Speech:** `Ctrl`
*   **Read Next Item:** `Down Arrow` or `Tab` (for focusable items)
*   **Read Previous Item:** `Up Arrow` or `Shift+Tab` (for focusable items)
*   **Read Current Item:** `NVDA + Tab` (NVDA key is usually `Insert` or `Caps Lock`)
*   **Read from Cursor:** `NVDA + Down Arrow`
*   **Navigate by Heading:** `H` (next), `Shift+H` (previous), `1`-`6` (jump to next heading level 1-6)
*   **Navigate by Landmark:** `D` (next), `Shift+D` (previous)
*   **Navigate by Link:** `K` (next), `Shift+K` (previous)
*   **Navigate by Form Field:** `F` (next), `Shift+F` (previous)
*   **Navigate by Table:** `T` (next), `Shift+T` (previous)
*   **Activate Link/Button:** `Enter`
*   **Interact with Form Controls:** `Space` (checkboxes, buttons), Arrow keys (radio buttons, select lists)
*   **List Elements (Links, Headings, Landmarks, etc.):** `NVDA + F7`

## Basic VoiceOver Commands (macOS)

*   **Start/Exit VoiceOver:** `Command + F5`
*   **VO Keys:** `Control + Option` (referred to as `VO`)
*   **Stop Speech:** `Ctrl`
*   **Read Next Item:** `VO + Right Arrow` or `Tab`
*   **Read Previous Item:** `VO + Left Arrow` or `Shift+Tab`
*   **Read Current Item:** `VO + F3`
*   **Read from Cursor:** `VO + A`
*   **Interact with Item:** `VO + Space`
*   **Navigate by Heading:** `VO + Command + H` (next), `VO + Command + Shift + H` (previous)
*   **Navigate by Landmark:** `VO + Command + D` (next), `VO + Command + Shift + D` (previous)
*   **Navigate by Link:** `VO + Command + L` (next), `VO + Command + Shift + L` (previous)
*   **Navigate by Form Control:** `VO + Command + J` (next), `VO + Command + Shift + J` (previous)
*   **Activate Link/Button:** `VO + Space` or `Enter`
*   **Interact with Form Controls:** `VO + Space` (checkboxes, select lists), Arrow keys (radio buttons, select options)
*   **Rotor (List Elements):** `VO + U`. Use Left/Right arrows to select element type (Headings, Links, Landmarks, Form Controls), then Up/Down arrows to navigate items. Press `Enter` to jump to the selected item.

## Common Issues Found with Screen Readers

*   Missing or unclear link text (`alt` text for image links).
*   Missing or incorrect form labels.
*   Incorrect heading structure (skipping levels, using heading tags for styling).
*   Missing landmark roles for page regions.
*   Unannounced dynamic content changes.
*   Custom controls that are not keyboard accessible or don't announce their role/state/name correctly (missing ARIA).
*   Poorly structured tables without proper headers (`<th>`, `scope`).
*   Keyboard traps.

Screen reader testing provides invaluable insights into the non-visual user experience. It's essential for verifying semantic structure and the operability of interactive components.

*(Refer to official NVDA and VoiceOver documentation for complete command lists.)*