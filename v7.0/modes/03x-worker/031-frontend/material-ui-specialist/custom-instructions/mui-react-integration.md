# Material UI: React Integration Patterns

Using MUI components effectively with React state management and hooks.

## Core Concept

MUI components are standard React components. Integrating them involves managing component state (like input values, open/close status for modals/drawers) using React hooks (`useState`, `useReducer`) and handling events with standard React event handlers.

## Common Integration Patterns

**1. Controlled Components:**

*   Many MUI input components (`TextField`, `Select`, `Checkbox`, `RadioGroup`, `Switch`, `Slider`, `Autocomplete`) are designed to be **controlled components**.
*   This means their value is controlled by React state. You need:
    *   A state variable (e.g., using `useState`) to hold the component's current value.
    *   To pass this state variable to the component's `value` (or `checked` for checkboxes/switches) prop.
    *   An `onChange` handler function that updates the state variable when the component's value changes.

```jsx
import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';
import Box from '@mui/material/Box';

function ControlledInputs() {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');
  const [agreed, setAgreed] = useState(false);

  const handleNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setName(event.target.value);
  };

  const handleAgeChange = (event: SelectChangeEvent) => {
    setAge(event.target.value);
  };

   const handleAgreeChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setAgreed(event.target.checked);
  };

  return (
    <Box component="form" noValidate autoComplete="off">
      <TextField
        label="Name"
        variant="outlined"
        value={name} // Controlled by state
        onChange={handleNameChange} // Update state on change
        margin="normal"
      />

      <FormControl fullWidth margin="normal">
        <InputLabel id="age-label">Age</InputLabel>
        <Select
          labelId="age-label"
          value={age} // Controlled by state
          label="Age"
          onChange={handleAgeChange} // Update state on change
        >
          <MenuItem value={10}>Ten</MenuItem>
          <MenuItem value={20}>Twenty</MenuItem>
          <MenuItem value={30}>Thirty</MenuItem>
        </Select>
      </FormControl>

       <FormControlLabel
         control={
           <Checkbox
             checked={agreed} // Controlled by state
             onChange={handleAgreeChange} // Update state on change
           />
          }
         label="Agree to terms"
       />

      <p>Current Name: {name}</p>
      <p>Current Age: {age}</p>
      <p>Agreed: {agreed ? 'Yes' : 'No'}</p>
    </Box>
  );
}
```
*   **Integration with Form Libraries:** For complex forms, use libraries like React Hook Form or Formik. They often provide wrappers or `Controller` components to integrate controlled MUI inputs smoothly with the form state and validation.

**2. Managing Open/Close State:**

*   Components like `<Dialog>`, `<Drawer>`, `<Menu>`, `<Snackbar>`, `<Popover>` require their visibility to be controlled via an `open` prop managed by React state (`useState`).
*   Provide an `onClose` handler prop to update the state and close the component.

```jsx
import React, { useState } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogActions from '@mui/material/DialogActions';

function DialogControlDemo() {
  const [open, setOpen] = useState(false); // State to control dialog visibility

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button onClick={handleClickOpen}>Open Dialog</Button>
      <Dialog open={open} onClose={handleClose}> {/* Pass state and handler */}
        <DialogTitle>Dialog Title</DialogTitle>
        {/* ... DialogContent ... */}
        <DialogActions>
          <Button onClick={handleClose}>Close</Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
```

**3. Handling Component Callbacks:**

*   Use standard React event handlers (`onClick`, `onChange`, `onSubmit`, etc.) on MUI components.
*   Access event data through the `event` object passed to your handler function.

**4. Conditional Rendering:**

*   Use standard React conditional rendering (e.g., `&&`, ternary operators, `if` statements) to show/hide MUI components based on state or props.

```jsx
import React, { useState } from 'react';
import Button from '@mui/material/Button';
import CircularProgress from '@mui/material/CircularProgress';
import Alert from '@mui/material/Alert';

function ConditionalDemo() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleClick = () => {
    setIsLoading(true);
    setError(null);
    // Simulate API call
    setTimeout(() => {
      // Simulate error or success
      if (Math.random() > 0.5) {
        setError('Failed to load data!');
      }
      setIsLoading(false);
    }, 1500);
  };

  return (
    <div>
      <Button onClick={handleClick} disabled={isLoading}>
        {isLoading ? <CircularProgress size={24} /> : 'Load Data'}
      </Button>

      {error && <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>}
    </div>
  );
}
```

**5. Refs:**

*   While less common due to the controlled nature of most components, you might occasionally need a ref (`useRef`) to access the underlying DOM node of an MUI component for specific measurements or imperative actions not covered by the component's API. Access the node via `ref.current`.

Integrate MUI components into your React application using standard React patterns for state management, event handling, and conditional rendering. Leverage controlled components for inputs and manage open/close state for modal-like components.

*(Refer to specific MUI component documentation for detailed API and props.)*