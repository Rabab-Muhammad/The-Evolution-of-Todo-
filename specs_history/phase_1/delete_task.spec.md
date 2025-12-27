# Delete Task

**Feature Branch**: `001-todo-console-app`
**Created**: 2025-12-27
**Status**: Draft
**Phase**: Phase I - In-Memory Python Console App

## Problem Statement

Users need the ability to remove tasks that are no longer relevant, were created by mistake, or have been completed and should be cleared from the list. Without deletion capability, the task list would grow indefinitely and become cluttered with obsolete items.

## User Stories

### User Story 1 - Delete Existing Task by ID (Priority: P1)

As a user, I want to delete a task by specifying its ID so that I can remove tasks that are no longer needed.

**Why this priority**: This is the core delete functionality that enables users to manage their task list effectively.

**Independent Test**: Can be fully tested by adding a task, noting its ID, selecting "Delete Task", entering the ID, and verifying the task no longer appears in the task list.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists, **When** user selects "Delete Task" and enters ID "1", **Then** the task is removed from the list and a confirmation message is displayed.

2. **Given** multiple tasks exist (IDs 1, 2, 3), **When** user deletes task with ID 2, **Then** only task 2 is removed; tasks 1 and 3 remain unchanged.

---

### User Story 2 - Handle Invalid Task ID (Priority: P2)

As a user, I want to receive clear feedback when I try to delete a non-existent task so that I know the operation failed and why.

**Why this priority**: Error handling is essential for user experience but secondary to core functionality.

**Independent Test**: Can be tested by attempting to delete a task with an ID that does not exist and verifying the error message.

**Acceptance Scenarios**:

1. **Given** no task with ID 99 exists, **When** user attempts to delete task with ID 99, **Then** an error message is displayed: "Task with ID 99 not found."

2. **Given** task with ID 1 was already deleted, **When** user attempts to delete ID 1 again, **Then** error message indicates task does not exist.

---

## Functional Requirements

- **FR-001**: System MUST allow users to delete a task by specifying its ID
- **FR-002**: System MUST display an error message if the specified task ID does not exist
- **FR-003**: System MUST display a confirmation message upon successful deletion
- **FR-004**: System MUST permanently remove the task from memory (no undo)
- **FR-005**: System MUST validate that the entered ID is a valid positive integer
- **FR-006**: Deletion of a task MUST NOT affect the IDs of other tasks

## Input / Output Format

### Input

| Field   | Type    | Required | Validation                     |
|---------|---------|----------|--------------------------------|
| Task ID | Integer | Yes      | Positive integer, must exist   |

### Output (Success)

| Field   | Type   | Description                           |
|---------|--------|---------------------------------------|
| Message | String | Confirmation of successful deletion   |
| Task ID | Integer| ID of the deleted task                |
| Title   | String | Title of the deleted task             |

### Output (Error)

| Field   | Type   | Description                           |
|---------|--------|---------------------------------------|
| Message | String | Error description                     |

## CLI Flow Examples

### Example 1: Successfully delete a task

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 2

--- Delete Task ---
Enter task ID to delete: 1

Task deleted successfully!
  Deleted: [1] Buy groceries

Press Enter to continue...
```

### Example 2: Attempt to delete non-existent task

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 2

--- Delete Task ---
Enter task ID to delete: 99

Error: Task with ID 99 not found.

Press Enter to continue...
```

### Example 3: Invalid input (non-integer)

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 2

--- Delete Task ---
Enter task ID to delete: abc

Error: Invalid input. Please enter a valid task ID (positive integer).
Enter task ID to delete: 1

Task deleted successfully!
  Deleted: [1] Buy groceries

Press Enter to continue...
```

### Example 4: Empty task list

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 2

--- Delete Task ---
No tasks available to delete.

Press Enter to continue...
```

## Edge Cases & Validation Rules

| Edge Case                     | Expected Behavior                                    |
|-------------------------------|------------------------------------------------------|
| Task ID does not exist        | Display error: "Task with ID X not found."           |
| Non-integer input             | Display error, prompt for valid integer              |
| Negative number               | Display error: "Invalid input. Please enter a valid task ID (positive integer)." |
| Zero as ID                    | Display error: "Invalid input. Please enter a valid task ID (positive integer)." |
| Empty input                   | Display error, prompt for valid ID                   |
| Empty task list               | Display message: "No tasks available to delete."     |
| Delete same ID twice          | First succeeds, second shows "not found" error       |

## Data Model Impact

### Entity Affected: Task

- Task record is permanently removed from in-memory storage
- No soft-delete; task is immediately purged
- IDs are not recycled; deleted ID will not be reused

### Storage Behavior

- Task removed from in-memory collection
- Other tasks remain unaffected
- ID sequence continues from last assigned (not reset)

## Acceptance Criteria

- [ ] User can delete a task by entering its ID
- [ ] System displays confirmation with deleted task details (ID, title)
- [ ] Deleted task no longer appears in task list
- [ ] Non-existent task IDs produce clear error message
- [ ] Non-integer inputs are rejected with error and re-prompt
- [ ] Negative numbers and zero are rejected as invalid IDs
- [ ] Empty input is rejected with error and re-prompt
- [ ] Empty task list shows appropriate message instead of delete prompt
- [ ] Deleting a task does not affect other tasks' IDs
- [ ] User returns to main menu after operation completes
