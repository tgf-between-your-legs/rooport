# Shadcn UI: Data Table Component

Building data tables using Shadcn UI components and `@tanstack/react-table`.

## Core Concept: TanStack Table + Shadcn Styling

Shadcn UI's `DataTable` is not a monolithic component but rather a collection of styled primitives (using Shadcn's `Table`, `Checkbox`, `DropdownMenu`, `Button` components) combined with the powerful **headless** table logic provided by `@tanstack/react-table` (formerly React Table v8).

**Key Libraries:**

*   **`@tanstack/react-table`:** Provides the core logic for managing table state, columns, data, sorting, filtering, pagination, row selection, etc., without dictating any specific markup or styling.
*   **Shadcn UI:** Provides the styled components (`Table`, `TableHeader`, `TableBody`, `TableRow`, `TableHead`, `TableCell`, `Checkbox`, `Button`, `DropdownMenu`) used to render the table UI based on the state and helpers from `@tanstack/react-table`.

## Setup

1.  **Install Dependencies:**
    ```bash
    npm install @tanstack/react-table
    # or
    yarn add @tanstack/react-table
    ```
2.  **Add Shadcn Table & Related Components:**
    ```bash
    npx shadcn-ui@latest add table dropdown-menu checkbox button # Add others as needed
    ```

## Implementation Steps (Conceptual)

Building a Shadcn data table typically involves these steps:

1.  **Define Columns:** Create an array defining your table columns using `@tanstack/react-table`'s `ColumnDef` type. Specify `accessorKey` (for data mapping) or `accessorFn`, `header` (content for `<th>`), and `cell` (how to render content in `<td>`). The `cell` function receives props allowing access to row data and rendering custom components (like checkboxes or action dropdowns).
2.  **Create Table Component:**
    *   Import necessary hooks from `@tanstack/react-table` (`useReactTable`, `getCoreRowModel`, `getPaginationRowModel`, `getSortedRowModel`, `getFilteredRowModel`, etc.).
    *   Import Shadcn UI table components (`Table`, `TableHeader`, etc.).
    *   Use the `useReactTable` hook, passing your `data`, `columns`, and enabling desired features (pagination, sorting, filtering, row selection) via `get*RowModel` functions.
    *   Manage table state (sorting, filtering, pagination, row selection) using React `useState` and pass them to `useReactTable`.
    *   Map over the table instance's header groups (`table.getHeaderGroups()`) and rows (`table.getRowModel().rows`) to render the UI using Shadcn's `Table`, `Tr`, `Th`, `Td` components.
    *   Implement UI elements for pagination controls, filtering inputs, column visibility toggles, etc., using Shadcn components and interacting with the `table` instance methods (`table.previousPage()`, `table.setPageIndex()`, `column.setFilterValue()`, etc.).

## Example Structure (Simplified)

```typescript
// src/components/my-data-table.tsx
"use client";

import * as React from "react";
import {
  ColumnDef,
  SortingState,
  VisibilityState,
  ColumnFiltersState,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
} from "@tanstack/react-table";

import { Input } from "@/components/ui/input";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

// Define data type (e.g., Payment)
interface Payment {
  id: string;
  amount: number;
  status: "pending" | "processing" | "success" | "failed";
  email: string;
}

// 1. Define Columns
export const columns: ColumnDef<Payment>[] = [
  // Example: Row Selection Checkbox Column
  {
    id: "select",
    header: ({ table }) => ( /* ... Checkbox ... */ ),
    cell: ({ row }) => ( /* ... Checkbox ... */ ),
    enableSorting: false,
    enableHiding: false,
  },
  // Example: Data Column with Sorting/Filtering
  {
    accessorKey: "email",
    header: ({ column }) => ( /* ... Button for sorting ... */ ),
    cell: ({ row }) => <div>{row.getValue("email")}</div>,
  },
  // Example: Formatted Amount Column
  {
    accessorKey: "amount",
    header: () => <div className="text-right">Amount</div>,
    cell: ({ row }) => { /* ... Format amount ... */ },
  },
  // Example: Actions Column
  {
    id: "actions",
    cell: ({ row }) => { /* ... DropdownMenu with actions ... */ },
  },
  // ... other columns
];

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[];
  data: TData[];
}

export function MyDataTable<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  // 2. Setup Table State (Sorting, Filtering, Visibility, Selection, Pagination)
  const [sorting, setSorting] = React.useState<SortingState>([]);
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>([]);
  const [columnVisibility, setColumnVisibility] = React.useState<VisibilityState>({});
  const [rowSelection, setRowSelection] = React.useState({});

  // 3. Initialize Table Instance
  const table = useReactTable({
    data,
    columns,
    onSortingChange: setSorting,
    onColumnFiltersChange: setColumnFilters,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    onColumnVisibilityChange: setColumnVisibility,
    onRowSelectionChange: setRowSelection,
    state: { // Pass state to the table instance
      sorting,
      columnFilters,
      columnVisibility,
      rowSelection,
    },
  });

  return (
    <div className="w-full">
      {/* Filter Inputs & Column Visibility Toggle */}
      <div className="flex items-center py-4">
        <Input placeholder="Filter emails..." value={/* ... */} onChange={/* ... */} />
        <DropdownMenu> {/* ... Column visibility toggle ... */} </DropdownMenu>
      </div>
      {/* Render Table */}
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            {table.getHeaderGroups().map((headerGroup) => (
              <TableRow key={headerGroup.id}>
                {headerGroup.headers.map((header) => (
                  <TableHead key={header.id}>
                    {header.isPlaceholder ? null : flexRender(header.column.columnDef.header, header.getContext())}
                  </TableHead>
                ))}
              </TableRow>
            ))}
          </TableHeader>
          <TableBody>
            {table.getRowModel().rows?.length ? (
              table.getRowModel().rows.map((row) => (
                <TableRow key={row.id} data-state={row.getIsSelected() && "selected"}>
                  {row.getVisibleCells().map((cell) => (
                    <TableCell key={cell.id}>
                      {flexRender(cell.column.columnDef.cell, cell.getContext())}
                    </TableCell>
                  ))}
                </TableRow>
              ))
            ) : (
              <TableRow> <TableCell colSpan={columns.length}>No results.</TableCell> </TableRow>
            )}
          </TableBody>
        </Table>
      </div>
      {/* Pagination Controls */}
      <div className="flex items-center justify-end space-x-2 py-4">
        {/* ... Row selection count ... */}
        <Button onClick={() => table.previousPage()} disabled={!table.getCanPreviousPage()}>Previous</Button>
        <Button onClick={() => table.nextPage()} disabled={!table.getCanNextPage()}>Next</Button>
      </div>
    </div>
  );
}
```

Building data tables with Shadcn UI involves leveraging the headless power of `@tanstack/react-table` for logic and state management, and then using Shadcn's styled table and interactive components to render the UI based on the table instance's state.

*(Refer to the Shadcn UI Data Table examples and `@tanstack/react-table` documentation.)*