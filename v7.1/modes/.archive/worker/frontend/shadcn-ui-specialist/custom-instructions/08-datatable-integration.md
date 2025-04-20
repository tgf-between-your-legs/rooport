# 8. DataTable Integration (`@tanstack/react-table`)

Building data tables using Shadcn UI components and `@tanstack/react-table` (v8).

## Core Concept: TanStack Table + Shadcn Styling

Shadcn UI's `DataTable` is not a monolithic component but rather a collection of styled primitives (using Shadcn's `Table`, `Checkbox`, `DropdownMenu`, `Button` components) combined with the powerful **headless** table logic provided by `@tanstack/react-table` (formerly React Table v8).

**Key Libraries:**

*   **`@tanstack/react-table`:** Provides the core logic for managing table state, columns, data, sorting, filtering, pagination, row selection, etc., without dictating any specific markup or styling.
*   **Shadcn UI:** Provides the styled components (`Table`, `TableHeader`, `TableBody`, `TableRow`, `TableHead`, `TableCell`, `Checkbox`, `Button`, `DropdownMenu`, `Input`) used to render the table UI based on the state and helpers from `@tanstack/react-table`.

## Setup

1.  **Install Dependencies:**
    ```bash
    npm install @tanstack/react-table
    # or
    yarn add @tanstack/react-table
    ```
2.  **Add Shadcn Table & Related Components:**
    ```bash
    npx shadcn-ui@latest add table dropdown-menu checkbox button input # Add others as needed
    ```

## Implementation Steps

1.  **Define Columns (`columns.tsx`):** Create an array defining your table columns using `@tanstack/react-table`'s `ColumnDef` type. Specify `accessorKey` (or `accessorFn`), `header`, and `cell` rendering. The `cell` function receives props allowing access to row data and rendering custom components (like checkboxes or action dropdowns).
    ```tsx
    // src/components/my-table/columns.tsx
    "use client" // Often needed if using client-side features

    import { ColumnDef } from "@tanstack/react-table"
    import { Checkbox } from "@/components/ui/checkbox" // Example component
    import { Button } from "@/components/ui/button" // For sorting toggle
    import { ArrowUpDown } from "lucide-react" // Icon for sorting
    // Define your data type
    export type Payment = {
      id: string
      amount: number
      status: "pending" | "processing" | "success" | "failed"
      email: string
    }

    export const columns: ColumnDef<Payment>[] = [
      { // Example: Row Selection Checkbox
        id: "select",
        header: ({ table }) => (
          <Checkbox
            checked={table.getIsAllPageRowsSelected()}
            onCheckedChange={(value) => table.toggleAllPageRowsSelected(!!value)}
            aria-label="Select all"
          />
        ),
        cell: ({ row }) => (
          <Checkbox
            checked={row.getIsSelected()}
            onCheckedChange={(value) => row.toggleSelected(!!value)}
            aria-label="Select row"
          />
        ),
        enableSorting: false,
        enableHiding: false,
      },
      {
        accessorKey: "status",
        header: "Status",
      },
      {
        accessorKey: "email",
        // Example: Sortable Header
        header: ({ column }) => {
          return (
            <Button
              variant="ghost"
              onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
            >
              Email
              <ArrowUpDown className="ml-2 h-4 w-4" />
            </Button>
          )
        },
      },
      {
        accessorKey: "amount",
        header: () => <div className="text-right">Amount</div>, // Right align header
        cell: ({ row }) => {
          const amount = parseFloat(row.getValue("amount"))
          const formatted = new Intl.NumberFormat("en-US", {
            style: "currency",
            currency: "USD",
          }).format(amount)
          return <div className="text-right font-medium">{formatted}</div> // Right align cell
        },
      },
      // Example: Actions Dropdown (requires a separate component like DataTableRowActions)
      // {
      //   id: "actions",
      //   cell: ({ row }) => <DataTableRowActions row={row} />,
      // },
    ]
    ```
2.  **Create DataTable Component (`data-table.tsx`):** This component encapsulates the table logic using `@tanstack/react-table` hooks and renders the Shadcn UI table components.
    ```tsx
    // src/components/my-table/data-table.tsx
    "use client"

    import * as React from "react"
    import {
      ColumnDef,
      flexRender,
      getCoreRowModel,
      getPaginationRowModel, // Import pagination
      getSortedRowModel,      // Import sorting
      getFilteredRowModel,    // Import filtering
      useReactTable,
      SortingState,
      ColumnFiltersState,
      VisibilityState,
      RowSelectionState,
    } from "@tanstack/react-table"

    import {
      Table,
      TableBody,
      TableCell,
      TableHead,
      TableHeader,
      TableRow,
    } from "@/components/ui/table"
    import { Button } from "@/components/ui/button" // For pagination controls
    import { Input } from "@/components/ui/input"   // For filtering
    import {
      DropdownMenu,
      DropdownMenuCheckboxItem,
      DropdownMenuContent,
      DropdownMenuTrigger,
    } from "@/components/ui/dropdown-menu" // For column visibility

    interface DataTableProps<TData, TValue> {
      columns: ColumnDef<TData, TValue>[]
      data: TData[]
    }

    export function DataTable<TData, TValue>({
      columns,
      data,
    }: DataTableProps<TData, TValue>) {
      const [sorting, setSorting] = React.useState<SortingState>([])
      const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>([])
      const [columnVisibility, setColumnVisibility] = React.useState<VisibilityState>({})
      const [rowSelection, setRowSelection] = React.useState<RowSelectionState>({})

      const table = useReactTable({
        data,
        columns,
        getCoreRowModel: getCoreRowModel(),
        // Pagination
        getPaginationRowModel: getPaginationRowModel(),
        // Sorting
        onSortingChange: setSorting,
        getSortedRowModel: getSortedRowModel(),
        // Filtering
        onColumnFiltersChange: setColumnFilters,
        getFilteredRowModel: getFilteredRowModel(),
        // Visibility
        onColumnVisibilityChange: setColumnVisibility,
        // Row Selection
        onRowSelectionChange: setRowSelection,
        state: {
          sorting,
          columnFilters,
          columnVisibility,
          rowSelection,
        },
      })

      return (
        <div>
          {/* Example Filtering Input & Column Visibility */}
          <div className="flex items-center py-4">
            <Input
              placeholder="Filter emails..."
              value={(table.getColumn("email")?.getFilterValue() as string) ?? ""}
              onChange={(event) =>
                table.getColumn("email")?.setFilterValue(event.target.value)
              }
              className="max-w-sm"
            />
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="outline" className="ml-auto"> Columns </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end">
                {table
                  .getAllColumns()
                  .filter((column) => column.getCanHide())
                  .map((column) => {
                    return (
                      <DropdownMenuCheckboxItem
                        key={column.id}
                        className="capitalize"
                        checked={column.getIsVisible()}
                        onCheckedChange={(value) => column.toggleVisibility(!!value)}
                      >
                        {column.id}
                      </DropdownMenuCheckboxItem>
                    )
                  })}
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
          {/* Table Rendering */}
          <div className="rounded-md border">
            <Table>
              <TableHeader>
                {table.getHeaderGroups().map((headerGroup) => (
                  <TableRow key={headerGroup.id}>
                    {headerGroup.headers.map((header) => {
                      return (
                        <TableHead key={header.id}>
                          {header.isPlaceholder
                            ? null
                            : flexRender(
                                header.column.columnDef.header,
                                header.getContext()
                              )}
                        </TableHead>
                      )
                    })}
                  </TableRow>
                ))}
              </TableHeader>
              <TableBody>
                {table.getRowModel().rows?.length ? (
                  table.getRowModel().rows.map((row) => (
                    <TableRow
                      key={row.id}
                      data-state={row.getIsSelected() && "selected"}
                    >
                      {row.getVisibleCells().map((cell) => (
                        <TableCell key={cell.id}>
                          {flexRender(cell.column.columnDef.cell, cell.getContext())}
                        </TableCell>
                      ))}
                    </TableRow>
                  ))
                ) : (
                  <TableRow>
                    <TableCell colSpan={columns.length} className="h-24 text-center">
                      No results.
                    </TableCell>
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </div>
          {/* Example Pagination Controls */}
          <div className="flex items-center justify-end space-x-2 py-4">
             <div className="flex-1 text-sm text-muted-foreground">
                {table.getFilteredSelectedRowModel().rows.length} of{" "}
                {table.getFilteredRowModel().rows.length} row(s) selected.
            </div>
            <Button
              variant="outline"
              size="sm"
              onClick={() => table.previousPage()}
              disabled={!table.getCanPreviousPage()}
            >
              Previous
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => table.nextPage()}
              disabled={!table.getCanNextPage()}
            >
              Next
            </Button>
          </div>
        </div>
      )
    }
    ```
3.  **Use the DataTable:** Import and use your `DataTable` component, passing the `columns` definition and the `data` array.
    ```tsx
    // app/page.tsx (or wherever you need the table)
    import { payments, columns } from "@/components/my-table/columns" // Example data/columns
    import { DataTable } from "@/components/my-table/data-table"

    async function getData(): Promise<Payment[]> {
      // Fetch data from your API here
      return payments // Using placeholder data
    }

    export default async function DemoPage() {
      const data = await getData()
      return <DataTable columns={columns} data={data} />
    }
    ```

## Key Features Enabled by `@tanstack/react-table`

*   Sorting (`getSortedRowModel`, `onSortingChange`)
*   Filtering (`getFilteredRowModel`, `onColumnFiltersChange`, `getColumn().setFilterValue()`)
*   Pagination (`getPaginationRowModel`, `previousPage`, `nextPage`, `getCanPreviousPage`, `getCanNextPage`)
*   Row Selection (`getFilteredSelectedRowModel`, `toggleAllPageRowsSelected`, `row.toggleSelected`)
*   Column Visibility (`getVisibleCells`, `onColumnVisibilityChange`, `getAllColumns`, `column.toggleVisibility`)
*   Column Resizing, Ordering, Grouping (More advanced features)

Building data tables with Shadcn UI involves leveraging the headless power of `@tanstack/react-table` for logic and state management, and then using Shadcn's styled table and interactive components to render the UI based on the table instance's state.

*(Refer to the official Shadcn UI DataTable documentation: https://ui.shadcn.com/docs/components/data-table and TanStack Table documentation: https://tanstack.com/table/v8)*