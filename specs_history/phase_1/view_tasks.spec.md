# View Tasks

**Feature Branch**: `001-todo-console-app`
**Created**: 2025-12-27
**Status**: Draft
**Phase**: Phase I - In-Memory Python Console App

## Problem Statement

Users need the ability to see all their tasks at a glance to understand what needs to be done, what has been completed, and to identify tasks they want to update or delete. Without a view capability, users cannot effectively manage their task list.

## User Stories

### User Story 1 - View All Tasks (Priority: P1)

As a user, I want to see a list of all my tasks with their details so that I can review what needs to be done.

**Why this priority**: Viewing tasks is essential for all task management operations and provides the core value of the application.

**Independent Test**: Can be fully tested by adding multiple tasks and selecting "View Tasks" to see all tasks displayed with their complete details.

**Acceptance Scenarios**:

1. **Given** multiple tasks exist, **When** user selects "View Tasks", **Then** all tasks are displayed showing ID, title, description, and status.

2. **Given** tasks have mixed statuses (complete and incomplete), **When** user views tasks, **Then** each task shows its correct status indicator.

---

### User Story 2 - View Empty Task List (Priority: P2)

As a user, I want to receive clear feedback when no tasks exist so that I understand the list is empty.

**Why this priority**: Edge case handling improves user experience but is secondary to core view functionality.

**Independent Test**: Can be tested by launching the app without adding any tasks and selecting "View Tasks".

**Acceptance Scenarios**:

1. **Given** no tasks exist, **When** user selects "View Tasks", **Then** a message is displayed: "No tasks found. Add a task to get started!"

---

## Functional Requirements

- **FR-001**: System MUST display all tasks in a formatted list
- **FR-002**: Each task display MUST include: ID, Title, Description, and Status
- **FR-003**: Status MUST be displayed as visual indicator: checkmark for complete, X for incomplete
- **FR-004**: Tasks with empty descriptions MUST display "(none)" or similar placeholder
- **FR-005**: System MUST display a message when no tasks exist
- **FR-006**: Task list MUST be displayed in order by task ID (ascending)
- **FR-007**: System MUST show total task count and completion summary

## Input / Output Format

### Input

No input required - this is a display-only operation.

### Output

| Field       | Type    | Description                                      |
|-------------|---------|--------------------------------------------------|
| Task Count  | Integer | Total number of tasks                            |
| Summary     | String  | Completion statistics (e.g., "2 of 5 completed") |
| Task List   | List    | All tasks with formatted details                 |

### Per-Task Output

| Field       | Type   | Format                                   |
|-------------|--------|------------------------------------------|
| ID          | Integer| Displayed in brackets: [1]               |
| Status      | String | Visual: checkmark or X symbol            |
| Title       | String | Task title text                          |
| Description | String | Task description or "(none)" if empty    |

## CLI Flow Examples

### Example 1: View tasks with mixed statuses

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 4

--- Task List ---
Total: 3 tasks (1 completed, 2 incomplete)

[1] [X] Buy groceries
    Description: Get milk, eggs, and bread

[2] [X] Doctor appointment
    Description: Annual checkup at 3pm

[3] [✓] Pay bills
    Description: Electric and water bills

Press Enter to continue...
```

### Example 2: View tasks - all incomplete

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 4

--- Task List ---
Total: 2 tasks (0 completed, 2 incomplete)

[1] [X] Buy groceries
    Description: Get milk

[2] [X] Call mom
    Description: (none)

Press Enter to continue...
```

### Example 3: View tasks - all complete

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 4

--- Task List ---
Total: 2 tasks (2 completed, 0 incomplete)

[1] [✓] Buy groceries
    Description: Get milk

[2] [✓] Pay bills
    Description: (none)

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

Enter choice: 4

--- Task List ---
No tasks found. Add a task to get started!

Press Enter to continue...
```

### Example 5: Single task

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 4

--- Task List ---
Total: 1 task (0 completed, 1 incomplete)

[1] [X] Buy groceries
    Description: Get milk and eggs

Press Enter to continue...
```

## Edge Cases & Validation Rules

| Edge Case                          | Expected Behavior                                        |
|------------------------------------|----------------------------------------------------------|
| No tasks exist                     | Display friendly message encouraging user to add tasks   |
| Single task exists                 | Display with proper grammar ("1 task" not "1 tasks")     |
| All tasks complete                 | Show all with checkmarks, summary shows "X completed, 0 incomplete" |
| All tasks incomplete               | Show all with X marks, summary shows "0 completed, X incomplete" |
| Task with no description           | Display "(none)" in description field                    |
| Task with very long title          | Display full title (no truncation in Phase I)            |
| Task with very long description    | Display full description (no truncation in Phase I)      |
| Large number of tasks              | Display all tasks (no pagination in Phase I)             |
| Tasks with special characters      | Display special characters as-is                         |

## Data Model Impact

### Entity Read: Task

| Attribute   | Display Format                               |
|-------------|----------------------------------------------|
| id          | Displayed in brackets: [1]                   |
| title       | Displayed as main text                       |
| description | Displayed on separate line, "(none)" if empty|
| status      | [✓] for complete, [X] for incomplete         |

### Storage Behavior

- Read-only operation - no modifications to data
- Tasks retrieved from in-memory storage
- Display order: ascending by task ID

## Acceptance Criteria

- [ ] User can view all tasks by selecting "View Tasks" option
- [ ] Each task displays: ID in brackets, status indicator, title, description
- [ ] Complete tasks show checkmark symbol: [✓]
- [ ] Incomplete tasks show X symbol: [X]
- [ ] Empty descriptions display "(none)"
- [ ] Summary shows total count with completion breakdown
- [ ] Grammar is correct for single task ("1 task" not "1 tasks")
- [ ] Empty task list shows friendly message to add tasks
- [ ] Tasks are displayed in ascending ID order
- [ ] Special characters in titles/descriptions display correctly
- [ ] User returns to main menu after viewing
- [ ] View operation does not modify any task data
