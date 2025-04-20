# Frappe Specialist: Workflows

Workflows in Frappe define the lifecycle of a document, managing its states and the transitions between them based on user actions and roles.

## 1. Core Concept

*   Workflows enforce business processes by controlling how a document moves through different stages (e.g., Draft -> Submitted -> Approved).
*   They are defined using the "Workflow" DocType (Setup -> Workflow).
*   Each Workflow applies to a specific target DocType and uses a designated field within that DocType to track the current state.

## 2. Components of a Workflow Definition

*   **Workflow Document:**
    *   `Document Type`: The target DocType (e.g., "Leave Application").
    *   `Workflow State Field`: The field in the target DocType holding the state value (usually a "Select" field, e.g., `status`).
    *   `Is Active`: Enables the workflow.
*   **States Table (within Workflow Doc):**
    *   `State`: Name of the state (must match an option in the state field).
    *   `Doc Status`: Document status (0=Draft, 1=Submitted, 2=Cancelled). Controls editability.
    *   `Update Field` / `Update Value`: (Optional) Automatically update a field upon entering this state.
    *   `Allow Edit`: Roles allowed to edit the document *in this specific state*.
*   **Transitions Table (within Workflow Doc):**
    *   `State`: The *current* state for this transition rule.
    *   `Action`: The action name (becomes the button label, e.g., "Approve").
    *   `Next State`: The state to move to after the action.
    *   `Allowed`: The Role permitted to perform this action.
    *   `Allow Self Approval`: Check if users can approve their own submissions (use cautiously).
    *   `Condition`: (Optional) Python expression (`doc.[fieldname] ...`) that must be true for the action button to appear.

## 3. How it Works

1.  Frappe checks the active Workflow for the DocType on load/refresh.
2.  It reads the current value of the `Workflow State Field`.
3.  It finds matching transitions for the current state in the Workflow definition.
4.  If the current user has the `Allowed` role for a transition AND the `Condition` (if any) is met, a button with the `Action` name appears.
5.  Clicking the button updates the `Workflow State Field` to the `Next State`, updates `Doc Status`, runs any `Update Field` logic, saves the document, and triggers relevant DocType events (`on_update`, `on_submit`, `on_cancel`).

## 4. Creating a Workflow

1.  **Ensure State Field Exists:** Add a "Select" field to your target DocType with options matching your desired states.
2.  **Create Workflow Doc:** Go to Setup -> Workflow -> New.
3.  **Configure:** Set Document Type, Workflow State Field, check Is Active.
4.  **Define States:** Add rows to the States table, mapping state names to Doc Status (0/1/2) and optional update/edit rules.
5.  **Define Transitions:** Add rows to the Transitions table, defining the flow: Current State -> Action -> Next State, restricted by Allowed Role and optional Condition.
6.  **Save.**

## 5. Example: Simple Approval

*   **DocType:** Expense Claim
*   **State Field:** `status` (Options: Draft, Submitted, Approved, Rejected)

**States:**

| State     | Doc Status | Allow Edit |
| :-------- | :--------- | :--------- |
| Draft     | 0          | Employee   |
| Submitted | 1          |            |
| Approved  | 1          |            |
| Rejected  | 1          |            |

**Transitions:**

| State     | Action  | Next State | Allowed    |
| :-------- | :------ | :--------- | :--------- |
| Draft     | Submit  | Submitted  | Employee   |
| Submitted | Approve | Approved   | Manager    |
| Submitted | Reject  | Rejected   | Manager    |
| Approved  | (None)  |            |            |
| Rejected  | Resubmit| Draft      | Employee   |

## 6. Considerations & Best Practices

*   **Doc Status Mapping:** Carefully map states to Doc Status (0=Editable, 1=Locked/Submitted, 2=Locked/Cancelled). This is critical for data integrity.
*   **Permissions Interaction:** Users need *both* the Role Permission (from Role Permission Manager) for the underlying action (e.g., Submit, Write) *and* be the `Allowed` role in the Workflow Transition.
*   **Conditions:** Use `doc.[fieldname]` syntax in conditions. Keep conditions relatively simple for maintainability.
*   **Complexity:** For highly complex logic with many branches or external interactions, consider using server scripts triggered by hooks (`on_update`, `validate`) alongside or instead of workflows. Workflows are best for linear state management.
*   **Testing:** Test workflows thoroughly by logging in as users with different roles and attempting transitions from each state.
*   **Clarity:** Use clear and intuitive names for States and Actions.

Workflows provide a powerful, configurable way to manage document lifecycles directly within Frappe.