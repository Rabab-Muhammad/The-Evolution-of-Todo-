# Tasks: Todo Console App - Phase I

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/cli-interface.md, research.md, quickstart.md

**Tests**: Not explicitly requested in specification. Tasks focus on implementation only.

**Organization**: Tasks organized by user-requested sections matching the spec files.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1 = Core Workflow, US2 = Error Handling)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root (adapted from plan.md per user request)

---

## Phase 1: Project Setup Tasks

**Purpose**: Initialize project structure with UV and Python 3.13+

**Spec Source**: plan.md (Project Structure), research.md (Technical Decisions)

- [X] T001 Create project root directory structure with `src/` and `tests/` folders
- [X] T002 Initialize UV project with `uv init` and configure for Python 3.13+
- [X] T003 Create `pyproject.toml` with project metadata and pytest dependency
- [X] T004 [P] Create package structure `src/__init__.py`
- [X] T005 [P] Create `src/models/__init__.py`
- [X] T006 [P] Create `src/services/__init__.py`
- [X] T007 [P] Create `src/cli/__init__.py`
- [X] T008 [P] Create `src/validators/__init__.py`
- [X] T009 [P] Create `src/exceptions/__init__.py`

**Checkpoint**: Project skeleton ready for implementation

---

## Phase 2: Core Data Model Tasks

**Purpose**: Implement Task entity and storage infrastructure

**Spec Source**: add_task.spec.md (Data Model Impact), data-model.md (Entity Design)

- [X] T010 [US1] Create Task dataclass with id, title, description, status fields in `src/models/task.py`
- [X] T011 [US1] Define status constants INCOMPLETE="incomplete" and COMPLETE="complete" in `src/models/task.py`
- [X] T012 [US1] Add type hints and docstring for Task entity in `src/models/task.py`

**Checkpoint**: Task model complete per data-model.md specifications

---

## Phase 3: Validation & Error Handling Tasks

**Purpose**: Implement validation rules and custom exceptions

**Spec Source**: All spec files (Edge Cases & Validation Rules), contracts/cli-interface.md (Validation Contract)

### Custom Exceptions

- [X] T013 [P] [US2] Create base `TodoAppError` exception class in `src/exceptions/errors.py`
- [X] T014 [P] [US2] Create `ValidationError` exception for input validation failures in `src/exceptions/errors.py`
- [X] T015 [P] [US2] Create `TaskNotFoundError` exception for missing task IDs in `src/exceptions/errors.py`
- [X] T016 [P] [US2] Create `EmptyTaskListError` exception for empty list operations in `src/exceptions/errors.py`

### Input Validators

- [X] T017 [US2] Implement `validate_menu_choice(input_str)` returning int 1-6 in `src/validators/input_validators.py`
- [X] T018 [US2] Implement `validate_task_id(input_str)` returning positive int in `src/validators/input_validators.py`
- [X] T019 [US2] Implement `validate_title(title)` with empty/whitespace/length checks in `src/validators/input_validators.py`
- [X] T020 [US2] Implement `validate_description(description)` with max 500 char check in `src/validators/input_validators.py`

**Checkpoint**: All validation rules from specs implemented

---

## Phase 4: CLI Interface Tasks

**Purpose**: Implement main menu and command routing

**Spec Source**: contracts/cli-interface.md (Main Menu Contract), all spec files (CLI Flow Examples)

- [X] T021 [US1] Implement `display_menu()` function showing 6 options in `src/cli/menu.py`
- [X] T022 [US1] Implement `get_menu_choice()` with validation loop in `src/cli/menu.py`
- [X] T023 [US1] Implement `run()` main application loop with routing in `src/cli/menu.py`
- [X] T024 [US1] Implement `wait_for_enter()` helper function in `src/cli/handlers.py`
- [X] T025 [US1] Create handler function stubs in `src/cli/handlers.py`

**Checkpoint**: Main menu functional with placeholder handlers

---

## Phase 5: Feature Implementation Tasks

**Purpose**: Implement all five core operations per specifications

### 5.1 Add Task

**Spec Source**: add_task.spec.md (FR-001 to FR-007), contracts/cli-interface.md (Add Task Contract)

- [X] T026 [US1] Implement `add_task(title, description)` in `src/services/task_service.py` with ID generation
- [X] T027 [US1] Implement in-memory storage `_tasks: Dict[int, Task]` and `_next_id: int` in `src/services/task_service.py`
- [X] T028 [US1] Implement `handle_add_task()` handler with title/description prompts in `src/cli/handlers.py`
- [X] T029 [US1] Add success confirmation output per CLI contract in `src/cli/handlers.py`
- [X] T030 [US2] Add validation error handling with re-prompt loop in `src/cli/handlers.py`

### 5.2 View Tasks

**Spec Source**: view_tasks.spec.md (FR-001 to FR-007), contracts/cli-interface.md (View Tasks Contract)

- [X] T031 [US1] Implement `get_all_tasks()` returning sorted list by ID in `src/services/task_service.py`
- [X] T032 [US1] Implement `has_tasks()` returning bool in `src/services/task_service.py`
- [X] T033 [US1] Implement `handle_view_tasks()` handler with formatted output in `src/cli/handlers.py`
- [X] T034 [US1] Add task count summary with correct grammar (task/tasks) in `src/cli/handlers.py`
- [X] T035 [US1] Add empty list message "No tasks found. Add a task to get started!" in `src/cli/handlers.py`

### 5.3 Delete Task

**Spec Source**: delete_task.spec.md (FR-001 to FR-006), contracts/cli-interface.md (Delete Task Contract)

- [X] T036 [US1] Implement `delete_task(task_id)` in `src/services/task_service.py`
- [X] T037 [US1] Implement `get_task(task_id)` for single task lookup in `src/services/task_service.py`
- [X] T038 [US1] Implement `handle_delete_task()` handler with ID prompt in `src/cli/handlers.py`
- [X] T039 [US1] Add success confirmation showing deleted task details in `src/cli/handlers.py`
- [X] T040 [US2] Add empty list pre-check and TaskNotFoundError handling in `src/cli/handlers.py`

### 5.4 Update Task

**Spec Source**: update_task.spec.md (FR-001 to FR-008), contracts/cli-interface.md (Update Task Contract)

- [X] T041 [US1] Implement `update_task(task_id, title, description)` with skip behavior in `src/services/task_service.py`
- [X] T042 [US1] Implement `handle_update_task()` handler showing current task first in `src/cli/handlers.py`
- [X] T043 [US1] Add title/description prompts with "press Enter to keep current" in `src/cli/handlers.py`
- [X] T044 [US1] Add "No changes made" message when both fields skipped in `src/cli/handlers.py`
- [X] T045 [US2] Add empty list pre-check and validation error handling in `src/cli/handlers.py`

### 5.5 Mark Complete/Incomplete

**Spec Source**: mark_complete.spec.md (FR-001 to FR-007), contracts/cli-interface.md (Toggle Contract)

- [X] T046 [US1] Implement `toggle_status(task_id)` in `src/services/task_service.py`
- [X] T047 [US1] Implement `handle_toggle_status()` handler with ID prompt in `src/cli/handlers.py`
- [X] T048 [US1] Add success confirmation showing old->new status transition in `src/cli/handlers.py`
- [X] T049 [US2] Add empty list pre-check and TaskNotFoundError handling in `src/cli/handlers.py`

**Checkpoint**: All five core operations implemented

---

## Phase 6: Integration Tasks

**Purpose**: Wire up entry point and integrate all components

**Spec Source**: plan.md (Project Structure), spec.md (FR-001, FR-006)

- [X] T050 [US1] Create `src/main.py` entry point importing and running menu
- [X] T051 [US1] Wire all handlers to menu router in `src/cli/menu.py`
- [X] T052 [US1] Implement exit handler with "Goodbye!" message in `src/cli/menu.py`
- [X] T053 [US1] Verify import structure works with `uv run src/main.py`

**Checkpoint**: Application runs end-to-end

---

## Phase 7: Documentation Tasks

**Purpose**: Ensure project is ready for Phase II

**Spec Source**: Constitution (SC-004), quickstart.md

- [X] T054 [P] Update `pyproject.toml` with entry point script `todo-app = "src.main:main"`
- [X] T055 [P] Verify all module docstrings are present and accurate
- [X] T056 Validate application against quickstart.md test scenarios

**Checkpoint**: Documentation complete per Constitution requirements

---

## Phase 8: Final Readiness Checklist

**Purpose**: Verify Phase I completion before Phase II

**Spec Source**: spec.md (Success Criteria SC-001 to SC-005)

- [X] T057 SC-001: Verify all five operations work per specs (manual testing)
- [X] T058 SC-002: Verify each operation completes within 30 seconds
- [X] T059 SC-003: Verify all invalid inputs produce correct error messages
- [X] T060 SC-004: Test with 100+ tasks to verify no performance degradation
- [X] T061 SC-005: Confirm all code was generated by Claude Code (no manual edits)

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup)
    │
    ▼
Phase 2 (Data Model)
    │
    ▼
Phase 3 (Validation/Errors)
    │
    ▼
Phase 4 (CLI Interface)
    │
    ▼
Phase 5 (Features) ─── 5.1 Add → 5.2 View → 5.3 Delete → 5.4 Update → 5.5 Toggle
    │
    ▼
Phase 6 (Integration)
    │
    ▼
Phase 7 (Documentation)
    │
    ▼
Phase 8 (Final Checklist)
```

### Feature Implementation Order

Features in Phase 5 should be implemented in this order:

1. **Add Task** (T026-T030) - Creates tasks; all other features depend on having tasks
2. **View Tasks** (T031-T035) - Validates Add works; shows task list for other operations
3. **Delete Task** (T036-T040) - Simple ID-based operation
4. **Update Task** (T041-T045) - More complex with skip behavior
5. **Mark Complete** (T046-T049) - Final feature, uses shared patterns

### Parallel Opportunities

```bash
# Phase 1: All package __init__.py files can be created in parallel
T004, T005, T006, T007, T008, T009 → Parallel

# Phase 3: All exception classes can be created in parallel
T013, T014, T015, T016 → Parallel

# Phase 7: Documentation tasks can run in parallel
T054, T055 → Parallel
```

### Within Features

Each feature follows: Service implementation → Handler implementation → Error handling

---

## User Story Mapping

### US1: Complete Task Management Workflow (P1)

Tasks: T010-T012, T021-T056 (Core implementation)
**Independent Test**: Run through complete workflow: add→view→update→toggle→delete

### US2: Error-Resistant Interaction (P2)

Tasks: T013-T020, T030, T040, T045, T049 (Validation and error handling)
**Independent Test**: Enter invalid inputs at each operation, verify error messages

---

## Implementation Strategy

### MVP First

1. Complete Phases 1-4 (Infrastructure)
2. Complete Phase 5.1-5.2 (Add + View) → **Minimal viable demo**
3. Add remaining features incrementally

### Incremental Delivery

| Milestone | Tasks | Demo Capability |
|-----------|-------|-----------------|
| Foundation | T001-T025 | Menu displays, handlers stubbed |
| Add+View MVP | T026-T035 | Can add and view tasks |
| Full CRUD | T036-T049 | All operations functional |
| Release Ready | T050-T061 | Production-ready with docs |

---

## Task Summary

| Phase | Task Count | Parallel Tasks |
|-------|------------|----------------|
| 1. Setup | 9 | 6 |
| 2. Data Model | 3 | 0 |
| 3. Validation | 8 | 4 |
| 4. CLI Interface | 5 | 0 |
| 5. Features | 24 | 0 |
| 6. Integration | 4 | 0 |
| 7. Documentation | 3 | 2 |
| 8. Final Checklist | 5 | 0 |
| **Total** | **61** | **12** |

---

## Notes

- All file paths are relative to repository root
- [P] tasks have no dependencies on incomplete tasks in same phase
- [US1] = Core workflow functionality
- [US2] = Error handling and validation
- Commit after each task or logical group
- Run `python -m todo_app` after Phase 6 to validate integration
- Reference quickstart.md for expected CLI outputs
