# Quickstart: Todo Console App - Phase I

**Branch**: `001-todo-console-app`
**Date**: 2025-12-27

## Prerequisites

- Python 3.13 or higher
- UV package manager

## Installation

```bash
# Clone the repository (if not already done)
cd Todo-app-phase-1

# Create virtual environment with UV
uv venv

# Activate virtual environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies (development)
uv pip install -e ".[dev]"
```

## Running the Application

```bash
# From project root
python -m todo_app

# Or using the entry point (after installation)
todo-app
```

## Expected Behavior

### Application Start

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

### Basic Workflow

1. **Add a task**: Enter `1`, provide title and optional description
2. **View tasks**: Enter `4` to see all tasks with status indicators
3. **Mark complete**: Enter `5`, provide task ID to toggle status
4. **Update task**: Enter `3`, provide task ID and new values
5. **Delete task**: Enter `2`, provide task ID to remove
6. **Exit**: Enter `6` to quit

## Validation Tests

### Test 1: Add Task with Title Only

```
Enter choice: 1

--- Add New Task ---
Enter task title: Buy groceries
Enter description (press Enter to skip):

Task added successfully!
  ID: 1
  Title: Buy groceries
  Description: (none)
  Status: incomplete
```

**Expected**: Task created with ID 1, status incomplete

### Test 2: Add Task with Description

```
Enter choice: 1

--- Add New Task ---
Enter task title: Doctor appointment
Enter description (press Enter to skip): Annual checkup at 3pm

Task added successfully!
  ID: 2
  Title: Doctor appointment
  Description: Annual checkup at 3pm
  Status: incomplete
```

**Expected**: Task created with ID 2, description saved

### Test 3: View Tasks

```
Enter choice: 4

--- Task List ---
Total: 2 tasks (0 completed, 2 incomplete)

[1] [X] Buy groceries
    Description: (none)

[2] [X] Doctor appointment
    Description: Annual checkup at 3pm
```

**Expected**: Both tasks displayed with [X] status indicator

### Test 4: Toggle Status

```
Enter choice: 5

--- Toggle Task Status ---
Enter task ID: 1

Status changed!
  Task: [1] Buy groceries
  Status: incomplete -> complete [✓]
```

**Expected**: Task 1 now shows [✓] in view

### Test 5: Update Task

```
Enter choice: 3

--- Update Task ---
Enter task ID to update: 1

Current task:
  ID: 1
  Title: Buy groceries
  Description: (none)
  Status: complete

Enter new title (press Enter to keep current): Get groceries
Enter new description (press Enter to keep current): Milk, eggs, bread

Task updated successfully!
  ID: 1
  Title: Get groceries
  Description: Milk, eggs, bread
  Status: complete
```

**Expected**: Title and description updated, status unchanged

### Test 6: Delete Task

```
Enter choice: 2

--- Delete Task ---
Enter task ID to delete: 2

Task deleted successfully!
  Deleted: [2] Doctor appointment
```

**Expected**: Task 2 removed, no longer appears in view

### Test 7: Error Handling - Empty Title

```
Enter choice: 1

--- Add New Task ---
Enter task title:

Error: Title cannot be empty. Please enter a valid title.
Enter task title: _
```

**Expected**: Error message shown, user can retry

### Test 8: Error Handling - Invalid ID

```
Enter choice: 2

--- Delete Task ---
Enter task ID to delete: 99

Error: Task with ID 99 not found.
```

**Expected**: Clear error message for non-existent task

### Test 9: Empty Task List Handling

```
Enter choice: 4

--- Task List ---
No tasks found. Add a task to get started!
```

**Expected**: Friendly message when no tasks exist

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=todo_app --cov-report=html

# Run specific test file
pytest tests/unit/test_task_service.py

# Run with verbose output
pytest -v
```

## Project Structure

```
Todo-app-phase-1/
├── pyproject.toml         # Project configuration
├── src/
│   └── todo_app/
│       ├── __init__.py
│       ├── __main__.py    # Entry point
│       ├── models/
│       │   ├── __init__.py
│       │   └── task.py    # Task entity
│       ├── services/
│       │   ├── __init__.py
│       │   └── task_service.py  # Business logic
│       ├── cli/
│       │   ├── __init__.py
│       │   ├── menu.py    # Main menu
│       │   └── handlers.py # Operation handlers
│       └── validators/
│           ├── __init__.py
│           └── input_validators.py
└── tests/
    ├── __init__.py
    ├── unit/
    │   ├── test_task.py
    │   ├── test_task_service.py
    │   └── test_validators.py
    └── integration/
        └── test_cli_flows.py
```

## Troubleshooting

### Unicode Issues

If checkmark (✓) doesn't display correctly, ensure your terminal supports UTF-8:

```bash
# Linux/macOS
export LANG=en_US.UTF-8

# Windows (PowerShell)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```

### Python Version

Verify Python version:
```bash
python --version  # Should be 3.13+
```

### UV Not Found

Install UV:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Success Criteria Validation

| Criterion | How to Verify |
|-----------|---------------|
| SC-001: All operations work | Complete all 9 tests above |
| SC-002: Operations under 30s | Time each operation |
| SC-003: Invalid inputs caught | Tests 7, 8 demonstrate error handling |
| SC-004: 100 tasks supported | Add 100 tasks, verify no degradation |
| SC-005: Generated code only | Verify via git history |
