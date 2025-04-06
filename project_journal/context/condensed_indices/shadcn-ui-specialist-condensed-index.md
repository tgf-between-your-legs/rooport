## Shadcn UI (Version Unknown) - Condensed Context Index

### Overall Purpose
Shadcn UI provides a collection of reusable, composable UI components for React/Next.js applications. It leverages Radix UI primitives and Tailwind CSS for styling, focusing on developer experience and customization by allowing users to copy component code directly into their projects via a CLI tool rather than installing a traditional library package.

### Core Concepts & Capabilities
*   **Component-Based UI:** Build interfaces by composing pre-built, customizable components like `Button`, `Input`, `Dialog`, `Table`, `Form`, `Accordion`, `Command`, `Chart`, `Menubar`, `Combobox`, `AlertDialog`.
*   **CLI Integration:** Use `npx shadcn@latest init` to set up the project (dependencies, CSS variables, utils) and `npx shadcn@latest add [component]` to add specific components directly to the codebase for full control.
*   **Theming & Dark Mode:** Implement theme switching (light/dark/system) using `ThemeProvider` context and `ModeToggle` component, leveraging CSS variables and Tailwind CSS utility classes.
*   **Forms & Validation:** Integrates seamlessly with `react-hook-form` and `zod` for building robust, type-safe forms using components like `Form`, `FormField`, `FormItem`, `FormControl`, `FormLabel`, `FormMessage`.
*   **Data Tables:** Create feature-rich data tables using the `DataTable` component built upon `@tanstack/react-table`, supporting column definitions (`ColumnDef`), sorting, filtering, pagination, and row selection (`Checkbox`).
*   **Interactive Elements:** Provides components for common interactive patterns like command menus (`Command`, `CommandDialog`), autocomplete/selects (`Combobox` pattern using `Popover` + `Command`), modals (`Dialog`, `AlertDialog`), and application menus (`Menubar`).
*   **Configuration:** Requires configuration for path aliases (`jsconfig.json` or `tsconfig.json`) and optionally for custom component registries (`registry.json`).

### Key APIs / Components / Configuration / Patterns
*   `npx shadcn@latest init`: CLI command to initialize Shadcn UI in a project.
*   `npx shadcn@latest add [component]`: CLI command to copy specific component source code into the project.
*   `ThemeProvider`: React context provider for managing application theme (light/dark/system).
*   `useTheme`: React hook to access and set the current theme from `ThemeProvider`.
*   `ModeToggle`: Example component using `DropdownMenu` for user theme selection.
*   `cn()` utility: Merges Tailwind CSS classes conditionally (often via `clsx` + `tailwind-merge`). Found in `lib/utils`.
*   `Form` components (`Form`, `FormField`, `FormItem`, etc.): Used with `react-hook-form` and `zod` for building forms.
*   `useForm` (from `react-hook-form`): Hook for form state management.
*   `zodResolver` (from `@hookform/resolvers/zod`): Adapter for Zod schema validation in forms.
*   `DataTable`: Reusable component for data tables using `@tanstack/react-table`.
*   `ColumnDef` (from `@tanstack/react-table`): Interface for defining table columns.
*   `Table` components (`Table`, `TableHeader`, `TableBody`, etc.): Primitives for basic HTML table structure.
*   `Dialog` components (`Dialog`, `DialogTrigger`, `DialogContent`, etc.): For creating modal dialogs.
*   `AlertDialog` components: Specialized dialog for confirmation actions.
*   `Command` components (`Command`, `CommandInput`, `CommandList`, `CommandDialog`, etc.): For building command palettes/menus.
*   `Combobox` (Pattern): Autocomplete select built using `Popover` and `Command`.
*   `Accordion` components: For collapsible content sections.
*   `Menubar` components: For application menu bars.
*   `Chart` components (`ChartContainer`, `ChartTooltip`, etc.): Wrappers for charting libraries (e.g., Recharts).
*   `jsconfig.json` / `tsconfig.json`: Configure path aliases like `@/*`.
*   `registry.json`: Defines schema/items for custom component registries via CLI.

### Common Patterns & Best Practices / Pitfalls
*   **Composition:** Build UIs by composing components; customize by editing the copied source code.
*   **CLI Workflow:** Use the `shadcn-ui` CLI for adding and potentially updating components.
*   **Tailwind CSS:** Styling is primarily done via Tailwind utility classes and CSS variables defined in `globals.css`.
*   **Accessibility:** Components are built on accessible Radix UI primitives.
*   **`"use client"`:** Required for components using React hooks (state, effects) in Next.js App Router.
*   **Integration:** Often used with `react-hook-form`, `zod`, `@tanstack/react-table`, `lucide-react` (icons).

This index summarizes the core concepts, APIs, and patterns for Shadcn UI based on the provided snippets. Consult the full source documentation (project_journal/context/source_docs/shadcn-ui-specialist-llms-context-20250406.md or official Shadcn UI docs) for exhaustive details.