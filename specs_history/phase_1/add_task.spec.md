# Add Task

**Feature Branch**: `001-todo-console-app`
**Created**: 2025-12-27
**Status**: Draft
**Phase**: Phase I - In-Memory Python Console App

## Problem Statement

Users need a way to create new tasks in the todo application. Without the ability to add tasks, the application has no purpose. This is the foundational operation that enables all other task management functionality.

## User Stories

### User Story 1 - Add Task with Title Only (Priority: P1)

As a user, I want to quickly add a task by providing just a title so that I can capture tasks with minimal friction.

**Why this priority**: This is the most common use case - users often want to quickly jot down a task without providing additional details.

**Independent Test**: Can be fully tested by launching the app, selecting "Add Task", entering only a title, and verifying the task appears in the task list.

**Acceptance Scenarios**:

1. **Given** the application is running and showing the main menu, **When** user selects "Add Task" and enters title "Buy groceries", **Then** a new task is created with auto-generated ID, the provided title, empty description, and status "incomplete".

2. **Given** user is in the "Add Task" flow, **When** user enters a title and skips the description prompt, **Then** the task is created with an empty description.

---

### User Story 2 - Add Task with Title and Description (Priority: P2)

As a user, I want to add a task with both a title and description so that I can capture additional context for complex tasks.

**Why this priority**: Some tasks require additional context; this builds on the P1 story.

**Independent Test**: Can be fully tested by adding a task with both title and description, then viewing the task list to confirm both fields are stored.

**Acceptance Scenarios**:

1. **Given** user is in the "Add Task" flow, **When** user enters title "Doctor appointment" and description "Annual checkup at 3pm", **Then** the task is created with both title and description stored.

---

## Functional Requirements

- **FR-001**: System MUST allow users to add a new task with a title (required) and description (optional)
- **FR-002**: System MUST auto-generate a unique task ID for each new task
- **FR-003**: System MUST set the default status of new tasks to "incomplete"
- **FR-004**: System MUST store tasks in memory during the application session
- **FR-005**: System MUST display a confirmation message after successful task creation
- **FR-006**: System MUST reject tasks with empty titles and display an error message
- **FR-007**: Task IDs MUST be sequential positive integers starting from 1

## Input / Output Format

### Input

| Field       | Type   | Required | Validation                        |
|-------------|--------|----------|-----------------------------------|
| Title       | String | Yes      | Non-empty, max 100 characters     |
| Description | String | No       | Max 500 characters, empty allowed |

### Output

| Field   | Type   | Description                           |
|---------|--------|---------------------------------------|
| Task ID | Integer| Auto-generated unique identifier      |
| Title   | String | User-provided task title              |
| Description | String | User-provided description (may be empty) |
| Status  | String | "incomplete" (default for new tasks)  |

## CLI Flow Examples

### Example 1: Add task with title only

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 1

--- Add New Task ---
Enter task title: Buy groceries
Enter description (press Enter to skip):

Task added successfully!
  ID: 1
  Title: Buy groceries
  Description: (none)
  Status: incomplete

Press Enter to continue...
```

### Example 2: Add task with title and description

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 1

--- Add New Task ---
Enter task title: Doctor appointment
Enter description (press Enter to skip): Annual checkup at 3pm on Tuesday

Task added successfully!
  ID: 2
  Title: Doctor appointment
  Description: Annual checkup at 3pm on Tuesday
  Status: incomplete

Press Enter to continue...
```

### Example 3: Attempt to add task with empty title

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 1

--- Add New Task ---
Enter task title:

Error: Title cannot be empty. Please enter a valid title.
Enter task title: Meeting notes

Task added successfully!
  ID: 3
  Title: Meeting notes
  Description: (none)
  Status: incomplete

Press Enter to continue...
```

## Edge Cases & Validation Rules

| Edge Case                          | Expected Behavior                                      |
|------------------------------------|--------------------------------------------------------|
| Empty title                        | Reject with error, prompt user to re-enter             |
| Title with only whitespace         | Treat as empty, reject with error                      |
| Title exceeds 100 characters       | Reject with error showing max length allowed           |
| Description exceeds 500 characters | Reject with error showing max length allowed           |
| Special characters in title        | Accept (no restrictions on character types)            |
| First task added                   | ID starts at 1                                         |
| Multiple tasks added               | IDs increment sequentially (1, 2, 3, ...)              |

## Data Model Impact

### New Entity: Task

| Attribute   | Type    | Constraints                          |
|-------------|---------|--------------------------------------|
| id          | Integer | Primary key, auto-generated, >= 1    |
| title       | String  | Required, 1-100 characters           |
| description | String  | Optional, 0-500 characters           |
| status      | String  | "incomplete" or "complete"           |

### Storage

- Tasks stored in memory (list or dictionary structure)
- Data persists only during application runtime
- All data lost when application exits

## Acceptance Criteria

- [ ] User can add a task with title only
- [ ] User can add a task with both title and description
- [ ] System auto-generates unique sequential IDs starting from 1
- [ ] New tasks default to "incomplete" status
- [ ] Empty titles are rejected with clear error message
- [ ] Whitespace-only titles are rejected
- [ ] Titles exceeding 100 characters are rejected with error
- [ ] Descriptions exceeding 500 characters are rejected with error
- [ ] Success confirmation displays task details (ID, title, description, status)
- [ ] User returns to main menu after adding task
