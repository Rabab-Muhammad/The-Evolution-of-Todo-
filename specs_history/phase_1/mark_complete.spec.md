# Mark Task Complete / Incomplete

**Feature Branch**: `001-todo-console-app`
**Created**: 2025-12-27
**Status**: Draft
**Phase**: Phase I - In-Memory Python Console App

## Problem Statement

Users need the ability to track progress on their tasks by marking them as complete or incomplete. This is the core value proposition of a todo application - providing a visual and functional distinction between finished and unfinished work.

## User Stories

### User Story 1 - Mark Incomplete Task as Complete (Priority: P1)

As a user, I want to mark an incomplete task as complete so that I can track my progress and see what I have accomplished.

**Why this priority**: Marking tasks complete is the primary goal of using a todo application.

**Independent Test**: Can be fully tested by adding a task (default incomplete), marking it complete, and viewing tasks to verify the status changed to complete.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 has status "incomplete", **When** user selects "Mark Complete/Incomplete" and enters ID 1, **Then** the task status changes to "complete" and confirmation is displayed.

2. **Given** task was just marked complete, **When** user views tasks, **Then** the task shows checkmark indicator.

---

### User Story 2 - Mark Complete Task as Incomplete (Priority: P2)

As a user, I want to mark a complete task as incomplete so that I can reopen tasks that need more work.

**Why this priority**: Toggling back to incomplete is important for correcting mistakes or reopening tasks.

**Independent Test**: Can be tested by marking a task complete, then toggling it back to incomplete, and verifying the status changes.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 has status "complete", **When** user toggles the status, **Then** the task status changes to "incomplete" and confirmation is displayed.

---

### User Story 3 - Handle Invalid Task ID (Priority: P3)

As a user, I want clear feedback when I try to toggle status for a non-existent task so that I know the operation failed.

**Why this priority**: Error handling is essential but secondary to core functionality.

**Independent Test**: Can be tested by attempting to toggle status of a non-existent task ID.

**Acceptance Scenarios**:

1. **Given** no task with ID 99 exists, **When** user attempts to toggle ID 99, **Then** error message is displayed: "Task with ID 99 not found."

---

## Functional Requirements

- **FR-001**: System MUST allow users to toggle a task's status by specifying its ID
- **FR-002**: System MUST change "incomplete" status to "complete" when toggled
- **FR-003**: System MUST change "complete" status to "incomplete" when toggled
- **FR-004**: System MUST display an error if the specified task ID does not exist
- **FR-005**: System MUST display a confirmation showing the new status after toggle
- **FR-006**: System MUST validate that the entered ID is a valid positive integer
- **FR-007**: Toggle operation MUST NOT affect any other task attributes (ID, title, description)

## Input / Output Format

### Input

| Field   | Type    | Required | Validation                     |
|---------|---------|----------|--------------------------------|
| Task ID | Integer | Yes      | Positive integer, must exist   |

### Output (Success)

| Field      | Type   | Description                              |
|------------|--------|------------------------------------------|
| Message    | String | Confirmation of status change            |
| Task ID    | Integer| ID of the toggled task                   |
| Title      | String | Title of the task                        |
| Old Status | String | Previous status before toggle            |
| New Status | String | Current status after toggle              |

### Output (Error)

| Field   | Type   | Description                           |
|---------|--------|---------------------------------------|
| Message | String | Error description                     |

## CLI Flow Examples

### Example 1: Mark incomplete task as complete

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 5

--- Toggle Task Status ---
Enter task ID: 1

Status changed!
  Task: [1] Buy groceries
  Status: incomplete -> complete [✓]

Press Enter to continue...
```

### Example 2: Mark complete task as incomplete

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 5

--- Toggle Task Status ---
Enter task ID: 1

Status changed!
  Task: [1] Buy groceries
  Status: complete -> incomplete [X]

Press Enter to continue...
```

### Example 3: Task not found

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 5

--- Toggle Task Status ---
Enter task ID: 99

Error: Task with ID 99 not found.

Press Enter to continue...
```

### Example 4: Invalid input (non-integer)

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 5

--- Toggle Task Status ---
Enter task ID: abc

Error: Invalid input. Please enter a valid task ID (positive integer).
Enter task ID: 1

Status changed!
  Task: [1] Buy groceries
  Status: incomplete -> complete [✓]

Press Enter to continue...
```

### Example 5: Empty task list

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 5

--- Toggle Task Status ---
No tasks available. Add a task first!

Press Enter to continue...
```

## Edge Cases & Validation Rules

| Edge Case                        | Expected Behavior                                      |
|----------------------------------|--------------------------------------------------------|
| Task ID does not exist           | Display error: "Task with ID X not found."             |
| Non-integer input                | Display error, prompt for valid integer                |
| Negative number                  | Display error: "Invalid input. Please enter a valid task ID (positive integer)." |
| Zero as ID                       | Display error: "Invalid input. Please enter a valid task ID (positive integer)." |
| Empty input                      | Display error, prompt for valid ID                     |
| Empty task list                  | Display message: "No tasks available. Add a task first!" |
| Toggle same task multiple times  | Each toggle switches status: incomplete->complete->incomplete->... |
| Task already complete            | Toggle to incomplete (not an error condition)          |
| Task already incomplete          | Toggle to complete (not an error condition)            |

## Data Model Impact

### Entity Affected: Task

| Attribute   | Toggle Behavior                              |
|-------------|----------------------------------------------|
| id          | Never changed by toggle operation            |
| title       | Never changed by toggle operation            |
| description | Never changed by toggle operation            |
| status      | Toggles: "incomplete" <-> "complete"         |

### Status Values

| Value      | Display Symbol | Description                |
|------------|----------------|----------------------------|
| incomplete | [X]            | Task not yet finished      |
| complete   | [✓]            | Task finished              |

### Storage Behavior

- Task record modified in-place in memory
- Only status field is changed
- Changes persist only during application runtime

## Acceptance Criteria

- [ ] User can toggle task status by entering task ID
- [ ] Incomplete tasks become complete when toggled
- [ ] Complete tasks become incomplete when toggled
- [ ] Confirmation message shows task details and status change
- [ ] Old status and new status are both displayed in confirmation
- [ ] Non-existent task IDs produce clear error message
- [ ] Non-integer IDs are rejected with error and re-prompt
- [ ] Negative numbers and zero are rejected as invalid IDs
- [ ] Empty input is rejected with error and re-prompt
- [ ] Empty task list shows appropriate message
- [ ] Toggle does not change task ID, title, or description
- [ ] Multiple toggles work correctly (can toggle back and forth)
- [ ] User returns to main menu after operation completes
