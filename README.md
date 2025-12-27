# Evolution of Todo - Phase I

An in-memory Python console application for basic task management.

## Overview

Phase I of the Evolution of Todo project implements five core operations:

1. **Add Task** - Create tasks with title (required) and description (optional)
2. **Delete Task** - Remove tasks by ID
3. **Update Task** - Modify task title and/or description
4. **View Tasks** - Display all tasks with status indicators
5. **Mark Complete/Incomplete** - Toggle task completion status

All tasks are stored in memory only - data is lost when the application exits.

## Requirements

- Python 3.13 or higher
- UV package manager

## Setup

```bash
# Clone or navigate to the repository
cd Todo-app-phase-1

# Create virtual environment with UV
uv venv

# Activate virtual environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install the package
uv pip install -e .
```

## Running the Application

### Option 1: Using UV (Recommended)

```bash
uv run src/main.py
```

### Option 2: Direct Python

```bash
python src/main.py
```

### Option 3: Installed Script

After installation:

```bash
todo-app
```

## Usage

The application presents an interactive menu:

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

### Example Workflow

1. **Add a task**: Select option 1, enter title and optional description
2. **View tasks**: Select option 4 to see all tasks with their status
3. **Mark complete**: Select option 5, enter task ID to toggle status
4. **Update task**: Select option 3, enter task ID and new values
5. **Delete task**: Select option 2, enter task ID to remove

### Status Indicators

- `[X]` - Incomplete task
- `[✓]` - Complete task

## Project Structure

```
Todo-app-phase-1/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py          # Task entity
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py  # Business logic
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── menu.py          # Main menu
│   │   └── handlers.py      # Operation handlers
│   ├── validators/
│   │   ├── __init__.py
│   │   └── input_validators.py
│   └── exceptions/
│       ├── __init__.py
│       └── errors.py
├── specs/                   # Feature specifications
├── specs_history/           # Historical spec files
├── pyproject.toml
├── README.md
└── CLAUDE.md               # Claude Code usage documentation
```

## Specifications

All features are implemented according to the specifications in `/specs_history/phase_1/`:

| Feature | Specification |
|---------|---------------|
| Add Task | `add_task.spec.md` |
| Delete Task | `delete_task.spec.md` |
| Update Task | `update_task.spec.md` |
| View Tasks | `view_tasks.spec.md` |
| Mark Complete | `mark_complete.spec.md` |

## Validation Rules

- **Title**: Required, 1-100 characters, cannot be empty or whitespace-only
- **Description**: Optional, 0-500 characters
- **Task ID**: Must be a positive integer that exists in the system

## Phase I Limitations

- Data is stored in memory only (no persistence)
- No categories, tags, or priorities
- No due dates
- No search or filter functionality
- Single user only

## License

MIT License
