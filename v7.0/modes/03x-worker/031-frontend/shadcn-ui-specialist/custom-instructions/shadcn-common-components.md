# Shadcn UI: Common Components Examples

Overview and basic usage of frequently used Shadcn UI components.

## Core Concept

Shadcn UI provides a collection of beautifully designed, accessible components built using Radix UI primitives and styled with Tailwind CSS. You add them to your project using the CLI (`npx shadcn-ui@latest add [component]`) and then compose them in your React code.

**Key Points:**

*   **Composition:** Components are meant to be composed together (e.g., `Card`, `CardHeader`, `CardContent`).
*   **Styling:** Primarily via Tailwind utility classes applied directly to the component code (`components/ui/`) or passed via `className`. Theming uses CSS variables.
*   **Accessibility:** Built on Radix UI, providing strong accessibility foundations (keyboard navigation, ARIA attributes).
*   **No Runtime:** Unlike traditional component libraries, Shadcn UI has virtually no runtime overhead as it copies code directly into your project.

## Common Components (Examples)

*(Note: Assumes components have been added via CLI and necessary imports are present)*

**1. Button:**

*   Uses Radix UI's `Slot` for composition.
*   Styled with `cva` (Class Variance Authority) for variants.
*   **Props:** `variant` (`default`, `destructive`, `outline`, `secondary`, `ghost`, `link`), `size` (`default`, `sm`, `lg`, `icon`), `asChild` (renders child as button).

```jsx
import { Button } from "@/components/ui/button";
import { Mail } from "lucide-react"; // Example icon

<Button>Default</Button>
<Button variant="destructive">Destructive</Button>
<Button variant="outline" size="lg">Outline Large</Button>
<Button variant="secondary" disabled>Disabled</Button>
<Button variant="ghost">Ghost</Button>
<Button size="icon"> <Mail className="h-4 w-4" /> </Button>
<Button asChild>
  <a href="/login">Login (as anchor)</a>
</Button>
```

**2. Input:**

*   Simple styled input element.
*   **Props:** Standard input props (`type`, `placeholder`, `value`, `onChange`, `disabled`, etc.), `className`.

```jsx
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

<div>
  <Label htmlFor="email">Email</Label>
  <Input type="email" id="email" placeholder="Email" />
</div>
```

**3. Card:**

*   Compositional: Use `Card`, `CardHeader`, `CardFooter`, `CardTitle`, `CardDescription`, `CardContent`.

```jsx
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

<Card className="w-[350px]">
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Card Description</CardDescription>
  </CardHeader>
  <CardContent>
    <p>Card Content goes here.</p>
  </CardContent>
  <CardFooter>
    <Button>Action</Button>
  </CardFooter>
</Card>
```

**4. Dialog:**

*   Built on Radix UI Dialog primitive. Handles modality, focus trapping, accessibility.
*   Compositional: `Dialog`, `DialogTrigger`, `DialogContent`, `DialogHeader`, `DialogFooter`, `DialogTitle`, `DialogDescription`, `DialogClose`.

```jsx
import {
  Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger, DialogClose
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";

<Dialog>
  <DialogTrigger asChild>
    <Button variant="outline">Edit Profile</Button>
  </DialogTrigger>
  <DialogContent className="sm:max-w-[425px]">
    <DialogHeader>
      <DialogTitle>Edit profile</DialogTitle>
      <DialogDescription>Make changes to your profile here.</DialogDescription>
    </DialogHeader>
    <div className="grid gap-4 py-4"> {/* Example content */}
      <div className="grid grid-cols-4 items-center gap-4">
        <Label htmlFor="name" className="text-right">Name</Label>
        <Input id="name" value="Pedro Duarte" className="col-span-3" />
      </div>
    </div>
    <DialogFooter>
      <DialogClose asChild>
         <Button type="button" variant="secondary">Close</Button>
      </DialogClose>
      <Button type="submit">Save changes</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

**5. Select:**

*   Built on Radix UI Select primitive.
*   Compositional: `Select`, `SelectTrigger`, `SelectValue`, `SelectContent`, `SelectGroup`, `SelectItem`, `SelectLabel`, `SelectSeparator`.

```jsx
import {
  Select, SelectContent, SelectItem, SelectTrigger, SelectValue, SelectGroup, SelectLabel
} from "@/components/ui/select";

<Select>
  <SelectTrigger className="w-[180px]">
    <SelectValue placeholder="Select a fruit" />
  </SelectTrigger>
  <SelectContent>
    <SelectGroup>
      <SelectLabel>Fruits</SelectLabel>
      <SelectItem value="apple">Apple</SelectItem>
      <SelectItem value="banana">Banana</SelectItem>
      <SelectItem value="blueberry">Blueberry</SelectItem>
    </SelectGroup>
  </SelectContent>
</Select>
```

**6. Checkbox:**

*   Built on Radix UI Checkbox primitive.
*   Often used with `Label`.

```jsx
import { Checkbox } from "@/components/ui/checkbox";
import { Label } from "@/components/ui/label";

<div className="flex items-center space-x-2">
  <Checkbox id="terms" />
  <Label htmlFor="terms">Accept terms and conditions</Label>
</div>
```

**7. Dropdown Menu:**

*   Built on Radix UI Dropdown Menu primitive.
*   Compositional: `DropdownMenu`, `DropdownMenuTrigger`, `DropdownMenuContent`, `DropdownMenuItem`, `DropdownMenuCheckboxItem`, `DropdownMenuRadioItem`, `DropdownMenuLabel`, `DropdownMenuSeparator`, `DropdownMenuGroup`, `DropdownMenuRadioGroup`, `DropdownMenuSub`, `DropdownMenuSubContent`, `DropdownMenuSubTrigger`, `DropdownMenuPortal`.

```jsx
import {
  DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuTrigger
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";

<DropdownMenu>
  <DropdownMenuTrigger asChild>
    <Button variant="outline">Open Menu</Button>
  </DropdownMenuTrigger>
  <DropdownMenuContent>
    <DropdownMenuLabel>My Account</DropdownMenuLabel>
    <DropdownMenuSeparator />
    <DropdownMenuItem>Profile</DropdownMenuItem>
    <DropdownMenuItem>Settings</DropdownMenuItem>
    <DropdownMenuItem>Logout</DropdownMenuItem>
  </DropdownMenuContent>
</DropdownMenu>
```

**Other Notable Components:** Accordion, Alert, AlertDialog, AspectRatio, Avatar, Badge, Calendar, Carousel, Command, ContextMenu, DatePicker, HoverCard, Label, Menubar, NavigationMenu, Popover, Progress, RadioGroup, ScrollArea, Separator, Sheet, Skeleton, Slider, Switch, Table, Tabs, Textarea, Toast/Toaster, Toggle, Tooltip.

Refer to the official Shadcn UI documentation for the full list of components, their specific props, and usage examples. Remember you can directly inspect and modify the code in `components/ui/` after adding them.