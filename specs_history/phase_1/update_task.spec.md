# Update Task

**Feature Branch**: `001-todo-console-app`
**Created**: 2025-12-27
**Status**: Draft
**Phase**: Phase I - In-Memory Python Console App

## Problem Statement

Users need the ability to modify existing tasks when requirements change, errors were made during creation, or additional details become available. Without update capability, users would need to delete and recreate tasks, losing the task's position and ID.

## User Stories

### User Story 1 - Update Task Title (Priority: P1)

As a user, I want to update a task's title so that I can correct mistakes or refine the task description.

**Why this priority**: Title is the primary identifier users see; updating it is the most common edit operation.

**Independent Test**: Can be fully tested by adding a task, selecting update, changing the title, and verifying the new title appears in the task list.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 and title "Buy grocries" exists, **When** user updates the title to "Buy groceries", **Then** the task's title is changed and a confirmation is displayed.

2. **Given** a task exists, **When** user chooses to update title and enters a new value, **Then** the description and status remain unchanged.

---

### User Story 2 - Update Task Description (Priority: P2)

As a user, I want to update a task's description so that I can add or modify additional context.

**Why this priority**: Description updates are common but secondary to title changes.

**Independent Test**: Can be tested by updating only the description of an existing task and verifying the change while title remains intact.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 has description "Get milk", **When** user updates description to "Get milk and eggs", **Then** the description is updated and title remains unchanged.

2. **Given** a task has no description, **When** user adds a description via update, **Then** the description is saved.

---

### User Story 3 - Update Both Title and Description (Priority: P3)

As a user, I want to update both the title and description in a single operation so that I can make comprehensive edits efficiently.

**Why this priority**: Combined updates are less frequent but improve efficiency when needed.

**Independent Test**: Can be tested by updating both fields simultaneously and verifying both changes are saved.

**Acceptance Scenarios**:

1. **Given** a task exists, **When** user updates both title and description, **Then** both fields are updated in a single operation.

---

## Functional Requirements

- **FR-001**: System MUST allow users to update a task's title by specifying task ID
- **FR-002**: System MUST allow users to update a task's description by specifying task ID
- **FR-003**: System MUST allow users to update both title and description in a single operation
- **FR-004**: System MUST allow users to skip updating a field by pressing Enter (keep current value)
- **FR-005**: System MUST display an error if the specified task ID does not exist
- **FR-006**: System MUST validate updated title is non-empty if a new value is provided
- **FR-007**: System MUST display a confirmation showing the updated task details
- **FR-008**: Update operation MUST NOT change the task's ID or status

## Input / Output Format

### Input

| Field           | Type    | Required | Validation                              |
|-----------------|---------|----------|-----------------------------------------|
| Task ID         | Integer | Yes      | Positive integer, must exist            |
| New Title       | String  | No       | If provided, 1-100 chars; Enter to skip |
| New Description | String  | No       | 0-500 chars; Enter to skip              |

### Output (Success)

| Field       | Type   | Description                           |
|-------------|--------|---------------------------------------|
| Message     | String | Confirmation of successful update     |
| Task ID     | Integer| ID of the updated task                |
| Title       | String | Current title (updated or unchanged)  |
| Description | String | Current description (updated or unchanged) |
| Status      | String | Current status (unchanged by update)  |

### Output (Error)

| Field   | Type   | Description                           |
|---------|--------|---------------------------------------|
| Message | String | Error description                     |

## CLI Flow Examples

### Example 1: Update title only

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 3

--- Update Task ---
Enter task ID to update: 1

Current task:
  ID: 1
  Title: Buy grocries
  Description: Get milk
  Status: incomplete

Enter new title (press Enter to keep current): Buy groceries
Enter new description (press Enter to keep current):

Task updated successfully!
  ID: 1
  Title: Buy groceries
  Description: Get milk
  Status: incomplete

Press Enter to continue...
```

### Example 2: Update description only

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 3

--- Update Task ---
Enter task ID to update: 1

Current task:
  ID: 1
  Title: Buy groceries
  Description: Get milk
  Status: incomplete

Enter new title (press Enter to keep current):
Enter new description (press Enter to keep current): Get milk, eggs, and bread

Task updated successfully!
  ID: 1
  Title: Buy groceries
  Description: Get milk, eggs, and bread
  Status: incomplete

Press Enter to continue...
```

### Example 3: Update both title and description

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 3

--- Update Task ---
Enter task ID to update: 2

Current task:
  ID: 2
  Title: Meeting
  Description: (none)
  Status: incomplete

Enter new title (press Enter to keep current): Team standup meeting
Enter new description (press Enter to keep current): Daily sync at 9am in conference room B

Task updated successfully!
  ID: 2
  Title: Team standup meeting
  Description: Daily sync at 9am in conference room B
  Status: incomplete

Press Enter to continue...
```

### Example 4: Task not found

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 3

--- Update Task ---
Enter task ID to update: 99

Error: Task with ID 99 not found.

Press Enter to continue...
```

### Example 5: No changes made (both fields skipped)

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 3

--- Update Task ---
Enter task ID to update: 1

Current task:
  ID: 1
  Title: Buy groceries
  Description: Get milk
  Status: incomplete

Enter new title (press Enter to keep current):
Enter new description (press Enter to keep current):

No changes made. Task remains unchanged.

Press Enter to continue...
```

### Example 6: Empty task list

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: 3

--- Update Task ---
No tasks available to update.

Press Enter to continue...
```

## Edge Cases & Validation Rules

| Edge Case                         | Expected Behavior                                       |
|-----------------------------------|---------------------------------------------------------|
| Task ID does not exist            | Display error: "Task with ID X not found."              |
| Non-integer ID input              | Display error, prompt for valid integer                 |
| Empty title when updating         | Keep current title (skip behavior)                      |
| New title is whitespace only      | Reject, display error, keep current title               |
| New title exceeds 100 chars       | Reject with error, prompt to re-enter                   |
| New description exceeds 500 chars | Reject with error, prompt to re-enter                   |
| Both fields skipped               | Display "No changes made" message                       |
| Clear description (make empty)    | Allow setting description to empty by entering a space then clearing |
| Empty task list                   | Display "No tasks available to update."                 |
| Negative or zero ID               | Display error: "Invalid input. Please enter a valid task ID." |

## Data Model Impact

### Entity Affected: Task

| Attribute   | Update Behavior                             |
|-------------|---------------------------------------------|
| id          | Never changed by update operation           |
| title       | Updated if new value provided               |
| description | Updated if new value provided               |
| status      | Never changed by update operation           |

### Storage Behavior

- Task record modified in-place in memory
- Changes persist only during application runtime
- No history of previous values maintained

## Acceptance Criteria

- [ ] User can update a task's title by entering task ID
- [ ] User can update a task's description by entering task ID
- [ ] User can update both title and description in one operation
- [ ] Pressing Enter without input skips that field (keeps current value)
- [ ] System displays current task details before prompting for updates
- [ ] System displays updated task details after successful update
- [ ] Non-existent task IDs produce clear error message
- [ ] Non-integer IDs are rejected with error and re-prompt
- [ ] Whitespace-only new titles are rejected (current title preserved)
- [ ] Titles exceeding 100 characters are rejected
- [ ] Descriptions exceeding 500 characters are rejected
- [ ] Skipping both fields shows "No changes made" message
- [ ] Empty task list shows appropriate message
- [ ] Update does not change task ID or status
- [ ] User returns to main menu after operation completes
