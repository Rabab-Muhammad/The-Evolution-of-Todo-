# Implementation Plan: Todo Console App - Phase I

**Branch**: `001-todo-console-app` | **Date**: 2025-12-27 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-todo-console-app/spec.md`

## Summary

Implement an in-memory Python console application for basic task management with five core operations: Add, Delete, Update, View, and Toggle Complete. The application uses a simple numbered menu interface with robust input validation and clear feedback messages.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: None (Python stdlib only)
**Package Manager**: UV
**Storage**: In-memory dictionary
**Testing**: pytest >= 8.0
**Target Platform**: Cross-platform (Windows/Linux/macOS)
**Project Type**: Single project
**Performance Goals**: Handle 100+ tasks without degradation
**Constraints**: No persistence (data lost on exit)
**Scale/Scope**: Single user, single session

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Status | Evidence |
|-----------|------|--------|----------|
| I. Spec-Driven Development | All features defined in specs before code | PASS | 5 spec files in `/specs_history/phase_1/` |
| II. Correctness | Operations match specification exactly | PENDING | Verified at implementation |
| III. Simplicity & Clarity | Intuitive console interactions | PASS | CLI flows match spec examples |
| IV. Maintainability | Modular code, separation of concerns | PASS | 4-layer architecture designed |

**Gate Result**: PASS - Proceed to implementation

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-console-app/
├── plan.md              # This file
├── spec.md              # Consolidated feature specification
├── research.md          # Phase 0 research decisions
├── data-model.md        # Entity and storage design
├── quickstart.md        # Validation guide
├── contracts/
│   └── cli-interface.md # CLI input/output contracts
└── checklists/
    └── requirements.md  # Specification quality checklist
```

### Source Code (repository root)

```text
src/
└── todo_app/
    ├── __init__.py
    ├── __main__.py          # Entry point
    ├── models/
    │   ├── __init__.py
    │   └── task.py          # Task dataclass
    ├── services/
    │   ├── __init__.py
    │   └── task_service.py  # Business logic (CRUD)
    ├── cli/
    │   ├── __init__.py
    │   ├── menu.py          # Main menu loop
    │   └── handlers.py      # Operation handlers
    ├── validators/
    │   ├── __init__.py
    │   └── input_validators.py
    └── exceptions/
        ├── __init__.py
        └── errors.py        # Custom exceptions

tests/
├── __init__.py
├── unit/
│   ├── __init__.py
│   ├── test_task.py
│   ├── test_task_service.py
│   └── test_validators.py
└── integration/
    ├── __init__.py
    └── test_cli_flows.py
```

**Structure Decision**: Single project with `src/` layout for clean imports and testability.

---

## Module Responsibilities

### 1. models/task.py

**Purpose**: Define the Task entity

**Contents**:
- `Task` dataclass with fields: id, title, description, status
- Status constants: INCOMPLETE = "incomplete", COMPLETE = "complete"

**Spec Source**: add_task.spec.md (Data Model Impact)

### 2. services/task_service.py

**Purpose**: Business logic for all CRUD operations

**Contents**:
- `TaskService` class (or module-level functions)
- In-memory storage: `_tasks: Dict[int, Task]`
- ID counter: `_next_id: int`

**Functions**:
| Function | Description | Spec Source |
|----------|-------------|-------------|
| `add_task(title, description)` | Create new task | add_task.spec |
| `delete_task(task_id)` | Remove task by ID | delete_task.spec |
| `update_task(task_id, title, description)` | Modify task | update_task.spec |
| `get_task(task_id)` | Retrieve single task | update_task.spec |
| `get_all_tasks()` | List all tasks | view_tasks.spec |
| `toggle_status(task_id)` | Toggle complete/incomplete | mark_complete.spec |
| `has_tasks()` | Check if any tasks exist | All specs (empty list check) |

### 3. cli/menu.py

**Purpose**: Main menu display and routing

**Contents**:
- `display_menu()` - Show main menu
- `run()` - Main application loop
- Menu choice validation and routing

**Spec Source**: All spec files (CLI Flow Examples)

### 4. cli/handlers.py

**Purpose**: Individual operation handlers

**Contents**:
| Handler | Description | Spec Source |
|---------|-------------|-------------|
| `handle_add_task()` | Prompt for title/description, call service | add_task.spec |
| `handle_delete_task()` | Prompt for ID, call service | delete_task.spec |
| `handle_update_task()` | Show current, prompt updates | update_task.spec |
| `handle_view_tasks()` | Display all tasks | view_tasks.spec |
| `handle_toggle_status()` | Prompt for ID, toggle | mark_complete.spec |

### 5. validators/input_validators.py

**Purpose**: Input validation functions

**Contents**:
| Validator | Input | Output | Spec Source |
|-----------|-------|--------|-------------|
| `validate_menu_choice(input)` | str | int (1-6) | All specs |
| `validate_task_id(input)` | str | int (positive) | delete/update/toggle specs |
| `validate_title(title)` | str | str (trimmed) | add_task.spec |
| `validate_description(desc)` | str | str | add_task.spec |

### 6. exceptions/errors.py

**Purpose**: Custom exception definitions

**Contents**:
- `ValidationError` - Input validation failures
- `TaskNotFoundError` - Task ID doesn't exist
- `EmptyTaskListError` - Operation requires tasks

---

## Task Data Model Design

See [data-model.md](./data-model.md) for complete details.

**Summary**:

```python
@dataclass
class Task:
    id: int           # Auto-generated, >= 1, immutable
    title: str        # Required, 1-100 chars
    description: str  # Optional, 0-500 chars
    status: str       # "incomplete" | "complete"
```

**Storage**: `Dict[int, Task]` with O(1) operations

---

## CLI Command Routing Strategy

```
Main Menu
    │
    ├── 1 → handle_add_task()
    ├── 2 → handle_delete_task()
    ├── 3 → handle_update_task()
    ├── 4 → handle_view_tasks()
    ├── 5 → handle_toggle_status()
    └── 6 → exit()
```

**Flow Pattern**:
1. Display menu
2. Get choice (validate)
3. Route to handler
4. Handler performs operation
5. Display result
6. "Press Enter to continue"
7. Loop back to menu (unless exit)

---

## Error Handling Strategy

### Exception Hierarchy

```
Exception
└── TodoAppError (base)
    ├── ValidationError
    │   ├── EmptyTitleError
    │   ├── TitleTooLongError
    │   ├── DescriptionTooLongError
    │   └── InvalidIdError
    ├── TaskNotFoundError
    └── EmptyTaskListError
```

### Error Handling Flow

1. **Service Layer**: Raises domain exceptions
2. **CLI Handlers**: Catch exceptions, display user-friendly messages
3. **Re-prompt**: On validation errors, re-prompt (don't return to menu)

### Error Message Mapping

| Exception | User Message | Behavior |
|-----------|--------------|----------|
| EmptyTitleError | "Error: Title cannot be empty..." | Re-prompt |
| TitleTooLongError | "Error: Title exceeds maximum length..." | Re-prompt |
| InvalidIdError | "Error: Invalid input..." | Re-prompt |
| TaskNotFoundError | "Error: Task with ID X not found." | Return to menu |
| EmptyTaskListError | "No tasks available..." | Return to menu |

---

## Validation Rules Mapping

### From add_task.spec.md

| Validation | Rule | Implementation |
|------------|------|----------------|
| Title required | Non-empty after trim | `len(title.strip()) > 0` |
| Title max length | <= 100 chars | `len(title) <= 100` |
| Description max | <= 500 chars | `len(description) <= 500` |

### From delete_task.spec.md

| Validation | Rule | Implementation |
|------------|------|----------------|
| ID format | Positive integer | `int(input) > 0` |
| ID exists | In storage | `task_id in _tasks` |

### From update_task.spec.md

| Validation | Rule | Implementation |
|------------|------|----------------|
| New title (if provided) | Non-empty, <= 100 chars | Same as add |
| New description | <= 500 chars | Same as add |
| Skip behavior | Empty input = keep current | `if input.strip(): update` |

### From mark_complete.spec.md

| Validation | Rule | Implementation |
|------------|------|----------------|
| ID format | Positive integer | Same as delete |
| ID exists | In storage | Same as delete |

---

## Order of Feature Implementation

### Phase 1: Setup (Tasks T001-T003)

1. **T001**: Create project structure with UV
2. **T002**: Configure pyproject.toml with pytest dependency
3. **T003**: Create package structure (`src/todo_app/`)

### Phase 2: Foundation (Tasks T004-T008)

4. **T004**: Implement Task model (`models/task.py`)
5. **T005**: Implement custom exceptions (`exceptions/errors.py`)
6. **T006**: Implement validators (`validators/input_validators.py`)
7. **T007**: Implement TaskService core (`services/task_service.py`)
8. **T008**: Implement main menu structure (`cli/menu.py`)

### Phase 3: Add Task (Tasks T009-T010)

9. **T009**: Implement `add_task()` in service
10. **T010**: Implement `handle_add_task()` in handlers

### Phase 4: View Tasks (Tasks T011-T012)

11. **T011**: Implement `get_all_tasks()` in service
12. **T012**: Implement `handle_view_tasks()` in handlers

### Phase 5: Delete Task (Tasks T013-T014)

13. **T013**: Implement `delete_task()` in service
14. **T014**: Implement `handle_delete_task()` in handlers

### Phase 6: Update Task (Tasks T015-T016)

15. **T015**: Implement `update_task()` in service
16. **T016**: Implement `handle_update_task()` in handlers

### Phase 7: Toggle Status (Tasks T017-T018)

17. **T017**: Implement `toggle_status()` in service
18. **T018**: Implement `handle_toggle_status()` in handlers

### Phase 8: Integration (Tasks T019-T020)

19. **T019**: Wire up main entry point (`__main__.py`)
20. **T020**: End-to-end manual testing per quickstart.md

---

## Test Scenarios from Acceptance Criteria

### Unit Tests: Task Model

| Test | Spec Source |
|------|-------------|
| Task creation with all fields | add_task.spec AC |
| Task default status is incomplete | add_task.spec FR-003 |
| Task ID is immutable | update_task.spec FR-008 |

### Unit Tests: Task Service

| Test | Spec Source |
|------|-------------|
| Add task returns task with ID | add_task.spec FR-002 |
| First task gets ID 1 | add_task.spec FR-007 |
| Sequential IDs (1, 2, 3) | add_task.spec FR-007 |
| Delete removes task | delete_task.spec FR-004 |
| Delete non-existent raises error | delete_task.spec FR-002 |
| Deleted IDs not recycled | delete_task.spec Data Model |
| Update changes title | update_task.spec FR-001 |
| Update changes description | update_task.spec FR-002 |
| Update preserves status | update_task.spec FR-008 |
| Toggle incomplete->complete | mark_complete.spec FR-002 |
| Toggle complete->incomplete | mark_complete.spec FR-003 |
| Get all returns sorted by ID | view_tasks.spec FR-006 |

### Unit Tests: Validators

| Test | Spec Source |
|------|-------------|
| Empty title rejected | add_task.spec Edge Cases |
| Whitespace title rejected | add_task.spec Edge Cases |
| Title > 100 chars rejected | add_task.spec Edge Cases |
| Description > 500 chars rejected | add_task.spec Edge Cases |
| Non-integer ID rejected | delete_task.spec Edge Cases |
| Zero ID rejected | delete_task.spec Edge Cases |
| Negative ID rejected | delete_task.spec Edge Cases |
| Valid positive ID accepted | delete_task.spec FR-005 |

### Integration Tests: CLI Flows

| Test | Spec Source |
|------|-------------|
| Add task with title only | add_task.spec Example 1 |
| Add task with description | add_task.spec Example 2 |
| View tasks with mixed status | view_tasks.spec Example 1 |
| View empty task list | view_tasks.spec Example 4 |
| Delete existing task | delete_task.spec Example 1 |
| Delete non-existent task | delete_task.spec Example 2 |
| Update title only | update_task.spec Example 1 |
| Update description only | update_task.spec Example 2 |
| Skip all updates | update_task.spec Example 5 |
| Toggle to complete | mark_complete.spec Example 1 |
| Toggle to incomplete | mark_complete.spec Example 2 |
| Menu invalid choice | All specs |

---

## Spec File to Code Module Mapping

| Spec File | Primary Module | Secondary Modules |
|-----------|----------------|-------------------|
| add_task.spec.md | services/task_service.py | cli/handlers.py, validators/input_validators.py |
| delete_task.spec.md | services/task_service.py | cli/handlers.py, validators/input_validators.py |
| update_task.spec.md | services/task_service.py | cli/handlers.py, validators/input_validators.py |
| view_tasks.spec.md | services/task_service.py | cli/handlers.py |
| mark_complete.spec.md | services/task_service.py | cli/handlers.py, validators/input_validators.py |

---

## Readiness Checklist

Before proceeding to `/sp.tasks` or implementation:

- [x] All 5 spec files read and analyzed
- [x] Technical context fully resolved (no NEEDS CLARIFICATION)
- [x] Constitution gates pass
- [x] Data model documented (data-model.md)
- [x] CLI contracts documented (contracts/cli-interface.md)
- [x] Quickstart validation guide created (quickstart.md)
- [x] Research decisions documented (research.md)
- [x] Module responsibilities defined
- [x] Implementation order determined
- [x] Test scenarios identified from acceptance criteria
- [x] Spec-to-module mapping complete

**Plan Status**: COMPLETE - Ready for `/sp.tasks`

---

## Complexity Tracking

> No Constitution violations requiring justification.

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| (none) | N/A | N/A |

---

## Related Documents

- [Specification: spec.md](./spec.md)
- [Research: research.md](./research.md)
- [Data Model: data-model.md](./data-model.md)
- [CLI Contract: contracts/cli-interface.md](./contracts/cli-interface.md)
- [Quickstart: quickstart.md](./quickstart.md)
- [Individual Specs: /specs_history/phase_1/](../../specs_history/phase_1/)
