# Data Model: Todo Console App - Phase I

**Branch**: `001-todo-console-app`
**Date**: 2025-12-27
**Status**: Complete

## Entities

### Task

The primary entity representing a todo item.

| Attribute   | Type   | Constraints | Source |
|-------------|--------|-------------|--------|
| id          | int    | Primary key, auto-generated, >= 1, unique, never recycled | add_task.spec FR-002, FR-007 |
| title       | str    | Required, 1-100 characters, non-whitespace | add_task.spec FR-001, FR-006 |
| description | str    | Optional, 0-500 characters, empty allowed | add_task.spec FR-001 |
| status      | str    | Enum: "incomplete" \| "complete", default "incomplete" | add_task.spec FR-003 |

### Entity Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│                      TASK LIFECYCLE                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [CREATE]                                                   │
│     │                                                       │
│     ▼                                                       │
│  ┌───────────┐                                              │
│  │INCOMPLETE │ ◄─────────────────────────┐                  │
│  └─────┬─────┘                           │                  │
│        │                                 │                  │
│        │ [TOGGLE]                        │ [TOGGLE]         │
│        ▼                                 │                  │
│  ┌───────────┐                           │                  │
│  │ COMPLETE  │ ──────────────────────────┘                  │
│  └─────┬─────┘                                              │
│        │                                                    │
│        │ [DELETE]                                           │
│        ▼                                                    │
│  ┌───────────┐                                              │
│  │  REMOVED  │  (Permanent - ID not recycled)               │
│  └───────────┘                                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Storage Design

### In-Memory Structure

```
TaskStorage:
├── tasks: Dict[int, Task]    # Key: task ID, Value: Task object
└── next_id: int              # Counter for ID generation (starts at 1)
```

### Storage Operations

| Operation | Time Complexity | Description |
|-----------|-----------------|-------------|
| Create    | O(1)            | Add to dict, increment counter |
| Read      | O(1)            | Dict lookup by ID |
| Update    | O(1)            | Dict lookup + modify |
| Delete    | O(1)            | Dict removal by ID |
| List All  | O(n)            | Iterate dict values |

### ID Generation Rules

1. IDs start at 1 (not 0)
2. IDs increment sequentially: 1, 2, 3, ...
3. Deleted IDs are never recycled
4. Counter persists across operations within session
5. Counter resets when application restarts (Phase I limitation)

**Example Sequence**:
```
Add task → ID 1
Add task → ID 2
Delete task 1
Add task → ID 3 (not 1)
```

## Validation Rules

### Title Validation

| Rule | Validation | Error Message |
|------|------------|---------------|
| Required | `len(title.strip()) > 0` | "Title cannot be empty. Please enter a valid title." |
| Max Length | `len(title) <= 100` | "Title exceeds maximum length of 100 characters." |
| Whitespace | `title.strip() != ""` | "Title cannot be empty. Please enter a valid title." |

### Description Validation

| Rule | Validation | Error Message |
|------|------------|---------------|
| Optional | Always valid if empty | N/A |
| Max Length | `len(description) <= 500` | "Description exceeds maximum length of 500 characters." |

### Task ID Validation

| Rule | Validation | Error Message |
|------|------------|---------------|
| Format | Must be parseable as integer | "Invalid input. Please enter a valid task ID (positive integer)." |
| Positive | `id > 0` | "Invalid input. Please enter a valid task ID (positive integer)." |
| Exists | `id in tasks` | "Task with ID {id} not found." |

## State Transitions

### Status Transitions

| Current State | Action | New State | Source |
|---------------|--------|-----------|--------|
| (new)         | CREATE | incomplete | add_task.spec FR-003 |
| incomplete    | TOGGLE | complete | mark_complete.spec FR-002 |
| complete      | TOGGLE | incomplete | mark_complete.spec FR-003 |
| any           | DELETE | (removed) | delete_task.spec FR-004 |

### Field Mutability

| Field | CREATE | UPDATE | TOGGLE | DELETE |
|-------|--------|--------|--------|--------|
| id | Set (auto) | Immutable | Immutable | N/A |
| title | Set (required) | Mutable | Immutable | N/A |
| description | Set (optional) | Mutable | Immutable | N/A |
| status | Set (incomplete) | Immutable | Mutable | N/A |

## Display Formats

### Status Display

| Internal Value | Display Symbol | Context |
|----------------|----------------|---------|
| incomplete | [X] | Task not finished |
| complete | [✓] | Task finished |

### Task Display Format

**Single Task (Detail View)**:
```
  ID: {id}
  Title: {title}
  Description: {description or "(none)"}
  Status: {status}
```

**Task List Item**:
```
[{id}] [{status_symbol}] {title}
    Description: {description or "(none)"}
```

### Summary Format

```
Total: {count} task(s) ({complete_count} completed, {incomplete_count} incomplete)
```

Note: Use singular "task" when count is 1, plural "tasks" otherwise.

## Data Integrity Constraints

1. **ID Uniqueness**: No two tasks can have the same ID
2. **ID Immutability**: Task ID never changes after creation
3. **Sequential IDs**: IDs are assigned in strictly increasing order
4. **No Orphan References**: IDs only exist while task exists
5. **Status Consistency**: Status is always one of exactly two values
6. **Title Required**: Every task must have a non-empty title

## Relationships

Phase I has no relationships - single entity model.

**Future Considerations (Phase II+)**:
- Categories/Tags (many-to-many)
- Due dates (attribute extension)
- Priority levels (attribute extension)
