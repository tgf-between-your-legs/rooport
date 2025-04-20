# Shadcn UI: DataTable Integration (`@tanstack/react-table`)

Building data tables using Shadcn UI components and `@tanstack/react-table` (v8).

## Core Concept

Shadcn UI provides styled table components (`<Table>`, `<TableHeader>`, `<TableBody>`, `<TableRow>`, `<TableHead>`, `<TableCell>`, `<TableCaption>`) that work well with the headless logic provided by `@tanstack/react-table`. You use `@tanstack/react-table` to manage table state (sorting, filtering, pagination, selection) and generate the necessary props for rendering, then apply those props to the Shadcn UI table components.

## Setup

1.  **Install Dependencies:**
    ```bash
    npm install @tanstack/react-table
    # or
    yarn add @tanstack/react-table
    # or
    pnpm add @tanstack/react-table
    ```
2.  **Add Shadcn Table Components:**
    ```bash
    npx shadcn-ui@latest add table
    # Optionally add other components needed (e.g., dropdown-menu, checkbox, button)
    npx shadcn-ui@latest add dropdown-menu checkbox button input
    ```

## Implementation Steps

1.  **Define Columns (`columns.tsx`):** Create an array defining your table columns using `createColumnHelper` or manually defining `ColumnDef` objects. Specify `accessorKey` (or `accessorFn`), `header`, and `cell` rendering.
    ```tsx
    // src/components/my-table/columns.tsx
    "use client" // Often needed if using client-side features like checkboxes

    import { ColumnDef } from "@tanstack/react-table"
    import { Checkbox } from "@/components/ui/checkbox" // Example component
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
        header: "Email",
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
      // ... other columns ...
      // Example: Actions Dropdown
      // {
      //   id: "actions",
      //   cell: ({ row }) => <DataTableRowActions row={row} />, // Custom component for actions
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
        onPaginationChange: // If managing pagination state manually
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
          {/* Example Filtering Input */}
          <div className="flex items-center py-4">
            <Input
              placeholder="Filter emails..."
              value={(table.getColumn("email")?.getFilterValue() as string) ?? ""}
              onChange={(event) =>
                table.getColumn("email")?.setFilterValue(event.target.value)
              }
              className="max-w-sm"
            />
            {/* Add Column Visibility Dropdown here if needed */}
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
*   Column Visibility (`getVisibleCells`, `onColumnVisibilityChange`)
*   Column Resizing, Ordering, Grouping (More advanced features)

*(Refer to the official Shadcn UI DataTable documentation: https://ui.shadcn.com/docs/components/data-table and TanStack Table documentation: https://tanstack.com/table/v8)*