# CLI Interface Contract: Todo Console App - Phase I

**Branch**: `001-todo-console-app`
**Date**: 2025-12-27
**Status**: Complete

## Overview

This document defines the contract for the console-based user interface. Since Phase I is a CLI application (not an API), contracts define the input/output behavior at the console level.

## Main Menu Contract

### Display

```
=== Todo Application ===
1. Add Task
2. Delete Task
3. Update Task
4. View Tasks
5. Mark Complete/Incomplete
6. Exit

Enter choice: _
```

### Input

| Input | Type | Validation | Action |
|-------|------|------------|--------|
| 1 | int | Valid choice | Navigate to Add Task |
| 2 | int | Valid choice | Navigate to Delete Task |
| 3 | int | Valid choice | Navigate to Update Task |
| 4 | int | Valid choice | Navigate to View Tasks |
| 5 | int | Valid choice | Navigate to Toggle Status |
| 6 | int | Valid choice | Exit application |
| Other | any | Invalid | Display error, re-prompt |

### Error Response

```
Invalid choice. Please enter a number between 1 and 6.
```

---

## Operation Contracts

### 1. Add Task

**Header**: `--- Add New Task ---`

**Input Sequence**:
1. Prompt: `Enter task title: `
   - Validation: Non-empty, max 100 chars
   - On error: Display message, re-prompt
2. Prompt: `Enter description (press Enter to skip): `
   - Validation: Max 500 chars (empty allowed)
   - On error: Display message, re-prompt

**Success Output**:
```
Task added successfully!
  ID: {id}
  Title: {title}
  Description: {description or "(none)"}
  Status: incomplete

Press Enter to continue...
```

**Error Messages**:
| Condition | Message |
|-----------|---------|
| Empty title | `Error: Title cannot be empty. Please enter a valid title.` |
| Whitespace title | `Error: Title cannot be empty. Please enter a valid title.` |
| Title > 100 chars | `Error: Title exceeds maximum length of 100 characters.` |
| Description > 500 chars | `Error: Description exceeds maximum length of 500 characters.` |

---

### 2. Delete Task

**Header**: `--- Delete Task ---`

**Pre-check**: If no tasks exist, display:
```
No tasks available to delete.

Press Enter to continue...
```

**Input Sequence**:
1. Prompt: `Enter task ID to delete: `
   - Validation: Positive integer, task exists
   - On error: Display message, re-prompt

**Success Output**:
```
Task deleted successfully!
  Deleted: [{id}] {title}

Press Enter to continue...
```

**Error Messages**:
| Condition | Message |
|-----------|---------|
| Non-integer | `Error: Invalid input. Please enter a valid task ID (positive integer).` |
| Zero/Negative | `Error: Invalid input. Please enter a valid task ID (positive integer).` |
| ID not found | `Error: Task with ID {id} not found.` |
| Empty input | `Error: Invalid input. Please enter a valid task ID (positive integer).` |

---

### 3. Update Task

**Header**: `--- Update Task ---`

**Pre-check**: If no tasks exist, display:
```
No tasks available to update.

Press Enter to continue...
```

**Input Sequence**:
1. Prompt: `Enter task ID to update: `
   - Validation: Positive integer, task exists
   - On error: Display message, re-prompt
2. Display current task details:
   ```
   Current task:
     ID: {id}
     Title: {title}
     Description: {description or "(none)"}
     Status: {status}
   ```
3. Prompt: `Enter new title (press Enter to keep current): `
   - Validation: If provided, non-empty, max 100 chars
   - Empty = keep current
4. Prompt: `Enter new description (press Enter to keep current): `
   - Validation: Max 500 chars
   - Empty = keep current

**Success Output (changes made)**:
```
Task updated successfully!
  ID: {id}
  Title: {title}
  Description: {description or "(none)"}
  Status: {status}

Press Enter to continue...
```

**Success Output (no changes)**:
```
No changes made. Task remains unchanged.

Press Enter to continue...
```

**Error Messages**:
| Condition | Message |
|-----------|---------|
| Non-integer ID | `Error: Invalid input. Please enter a valid task ID (positive integer).` |
| ID not found | `Error: Task with ID {id} not found.` |
| Whitespace title | `Error: Title cannot be empty. Please enter a valid title.` |
| Title > 100 chars | `Error: Title exceeds maximum length of 100 characters.` |
| Description > 500 chars | `Error: Description exceeds maximum length of 500 characters.` |

---

### 4. View Tasks

**Header**: `--- Task List ---`

**No Input Required**

**Output (tasks exist)**:
```
--- Task List ---
Total: {count} task(s) ({complete} completed, {incomplete} incomplete)

[{id}] [{status_symbol}] {title}
    Description: {description or "(none)"}

[{id}] [{status_symbol}] {title}
    Description: {description or "(none)"}

Press Enter to continue...
```

**Output (no tasks)**:
```
--- Task List ---
No tasks found. Add a task to get started!

Press Enter to continue...
```

**Status Symbols**:
- Incomplete: `[X]`
- Complete: `[✓]`

**Ordering**: Tasks displayed in ascending order by ID.

**Grammar Rule**: Use "1 task" (singular) when count is 1, "X tasks" (plural) otherwise.

---

### 5. Mark Complete/Incomplete (Toggle)

**Header**: `--- Toggle Task Status ---`

**Pre-check**: If no tasks exist, display:
```
No tasks available. Add a task first!

Press Enter to continue...
```

**Input Sequence**:
1. Prompt: `Enter task ID: `
   - Validation: Positive integer, task exists
   - On error: Display message, re-prompt

**Success Output**:
```
Status changed!
  Task: [{id}] {title}
  Status: {old_status} -> {new_status} [{new_status_symbol}]

Press Enter to continue...
```

**Error Messages**:
| Condition | Message |
|-----------|---------|
| Non-integer | `Error: Invalid input. Please enter a valid task ID (positive integer).` |
| Zero/Negative | `Error: Invalid input. Please enter a valid task ID (positive integer).` |
| ID not found | `Error: Task with ID {id} not found.` |

---

### 6. Exit

**Output**:
```
Goodbye!
```

Application terminates.

---

## Common Patterns

### Re-prompt on Error

When input validation fails, the system:
1. Displays error message
2. Re-displays the same prompt
3. Accepts new input

The user is NOT returned to the main menu on validation errors.

### Press Enter to Continue

After every operation completes (success or error that ends the operation), display:
```
Press Enter to continue...
```

Wait for Enter key, then return to main menu.

### Empty Description Display

When a task has no description (empty string), display:
```
Description: (none)
```

---

## Service Layer Contract

The CLI layer interacts with the service layer through these function signatures:

| Function | Parameters | Returns | Raises |
|----------|------------|---------|--------|
| `add_task(title, description)` | title: str, description: str | Task | ValidationError |
| `delete_task(task_id)` | task_id: int | Task (deleted) | TaskNotFoundError |
| `update_task(task_id, title, description)` | task_id: int, title: str \| None, description: str \| None | Task | TaskNotFoundError, ValidationError |
| `get_task(task_id)` | task_id: int | Task | TaskNotFoundError |
| `get_all_tasks()` | None | List[Task] | None |
| `toggle_task_status(task_id)` | task_id: int | Task | TaskNotFoundError |
| `has_tasks()` | None | bool | None |

---

## Validation Contract

| Validator | Input | Output | Raises |
|-----------|-------|--------|--------|
| `validate_task_id(input_str)` | str | int | ValidationError |
| `validate_title(title)` | str | str (trimmed) | ValidationError |
| `validate_description(description)` | str | str | ValidationError |
| `validate_menu_choice(input_str)` | str | int (1-6) | ValidationError |
