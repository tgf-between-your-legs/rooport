# Frappe: Workflows

Defining and managing document lifecycles and state transitions using Frappe Workflows.

## Core Concept

Frappe Workflows allow you to define a sequence of states and transitions for a specific DocType. This helps enforce business processes, control document status changes, and define actions allowed at each stage.

**Example Use Cases:**
*   Leave Application: Draft -> Submitted -> Approved/Rejected -> Cancelled
*   Sales Order: Draft -> Submitted -> To Deliver -> Completed/Cancelled
*   Issue Tracking: Open -> In Progress -> Resolved/Closed -> Reopened

## Components of a Workflow

1.  **Workflow Document:** A DocType itself (Setup -> Workflow -> Workflow) where you define the overall workflow.
    *   **Document Type:** The DocType this workflow applies to (e.g., "Leave Application").
    *   **Is Active:** Checkbox to enable/disable the workflow.
    *   **Workflow State Field:** The field within the target DocType that stores the current state (usually a "Select" field with defined options matching the workflow states).
    *   **States Table:** Defines the possible states the document can be in.
    *   **Transitions Table:** Defines the allowed movements between states.
2.  **Workflow States (Table in Workflow Document):**
    *   **State:** The name of the state (must match an option in the "Workflow State Field").
    *   **Doc Status:** The document's status when in this state (0=Draft, 1=Submitted, 2=Cancelled). This controls whether the document is editable or considered final.
    *   **Update Field:** (Optional) A field to automatically update when the document enters this state.
    *   **Update Value:** The value to set in the "Update Field".
    *   **Allow Edit:** Specify Roles that are allowed to edit the document *while it is in this state* (overrides standard permissions if more restrictive).
3.  **Workflow Transitions (Table in Workflow Document):**
    *   **State:** The *current* state from which the transition originates.
    *   **Action:** The name of the action that triggers the transition (e.g., "Submit", "Approve", "Reject", "Re-open"). This action name appears as a button in the document form.
    *   **Next State:** The state the document moves to after the action is performed.
    *   **Allowed:** The Role that is allowed to perform this action/transition.
    *   **Allow Self Approval:** Check if users can approve their own documents (use with caution).
    *   **Condition:** (Optional) A Python expression evaluated on the document (`doc`) that must be true for the action button to be visible/enabled (e.g., `doc.total_days <= 5`).

## How it Works

1.  When a document of the specified DocType is saved, Frappe checks if an active Workflow applies.
2.  It looks at the value in the "Workflow State Field".
3.  Based on the current state, it finds the allowed transitions in the Workflow definition.
4.  For each allowed transition, if the current user's Role matches the "Allowed" role for the transition (and the optional "Condition" is met), a button corresponding to the "Action" name is displayed on the document form.
5.  Clicking the action button:
    *   Updates the "Workflow State Field" to the "Next State".
    *   Updates the document's "Doc Status" based on the new state's definition.
    *   Updates the "Update Field" with the "Update Value" if configured for the new state.
    *   Saves the document.
    *   Triggers standard DocType events like `on_update` or `on_submit`/`on_cancel` based on the Doc Status change.

## Creating a Workflow

1.  **Define State Field:** Ensure your target DocType has a "Select" field to store the workflow state (e.g., `status`), with options matching your desired states.
2.  **Create Workflow Document:** Go to Setup -> Workflow -> Workflow -> New.
    *   Set the "Document Type".
    *   Set the "Workflow State Field".
    *   Check "Is Active".
3.  **Define States:** In the "States" table, add rows for each state:
    *   Enter the "State" name (matching the Select field option).
    *   Set the corresponding "Doc Status" (0, 1, or 2).
    *   (Optional) Configure "Update Field", "Update Value", "Allow Edit".
4.  **Define Transitions:** In the "Transitions" table, add rows for each allowed transition:
    *   Enter the current "State".
    *   Enter the "Action" name (this becomes the button label).
    *   Select the "Next State".
    *   Select the "Allowed" Role.
    *   (Optional) Set "Allow Self Approval", "Condition".
5.  **Save** the Workflow document.

## Example: Leave Application Workflow

*   **DocType:** Leave Application
*   **Workflow State Field:** `status` (Select field with options: Draft, Submitted, Approved, Rejected, Cancelled)

**States Table:**

| State     | Doc Status | Update Field | Update Value | Allow Edit |
| :-------- | :--------- | :----------- | :----------- | :--------- |
| Draft     | 0          |              |              | Employee   |
| Submitted | 1          |              |              |            |
| Approved  | 1          | approved_by  | `frappe.session.user` |            |
| Rejected  | 1          |              |              |            |
| Cancelled | 2          |              |              |            |

**Transitions Table:**

| State     | Action   | Next State | Allowed      | Condition |
| :-------- | :------- | :--------- | :----------- | :-------- |
| Draft     | Submit   | Submitted  | Employee     |           |
| Submitted | Approve  | Approved   | HR Manager   |           |
| Submitted | Reject   | Rejected   | HR Manager   |           |
| Approved  | Cancel   | Cancelled  | Employee     |           |
| Rejected  | Cancel   | Cancelled  | Employee     |           |

## Considerations

*   **Doc Status:** Carefully map states to Doc Status (0=Draft/Editable, 1=Submitted/Locked, 2=Cancelled/Locked).
*   **Permissions:** Workflow permissions interact with Role Permissions Manager. A user needs *both* the Role Permission to perform an action (like Submit) *and* be in the "Allowed" role for the specific Workflow Transition.
*   **Conditions:** Use conditions for dynamic transition availability (e.g., based on document values).
*   **Complexity:** For very complex logic, consider using server scripts triggered by hooks (`on_update`, `validate`) instead of, or in addition to, workflows.

Workflows are a powerful tool for enforcing business processes and managing document lifecycles within Frappe.

*(Refer to the official Frappe Workflow documentation: https://frappeframework.com/docs/user/en/basics/workflows)*