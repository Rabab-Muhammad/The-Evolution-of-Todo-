"""CLI handlers for Todo Application operations.

Per contracts/cli-interface.md Operation Contracts and all spec files CLI Flow Examples.
"""

from src.models import INCOMPLETE, COMPLETE
from src.services import (
    add_task,
    get_task,
    get_all_tasks,
    has_tasks,
    delete_task,
    update_task,
    toggle_status,
)
from src.validators import validate_task_id, validate_title, validate_description
from src.exceptions import ValidationError, TaskNotFoundError


def _get_status_symbol(status: str) -> str:
    """Get display symbol for task status.

    Per view_tasks.spec.md Status Display:
    - incomplete: [X]
    - complete: [checkmark]
    """
    return "[✓]" if status == COMPLETE else "[X]"


def _wait_for_enter() -> None:
    """Wait for user to press Enter to continue.

    Per contracts/cli-interface.md Common Patterns.
    """
    input("\nPress Enter to continue...")


def _show_task_list_compact() -> None:
    """Show compact task list with IDs for selection.

    Helper function to display tasks before ID-based operations.
    """
    tasks = get_all_tasks()
    if tasks:
        print("\nAvailable tasks:")
        for task in tasks:
            status_symbol = _get_status_symbol(task.status)
            print(f"  [{task.id}] {status_symbol} {task.title}")
        print()


def handle_add_task() -> None:
    """Handle Add Task operation.

    Per add_task.spec.md CLI Flow Examples and contracts/cli-interface.md Add Task Contract.
    """
    print("\n--- Add New Task ---")

    # Get title with validation loop
    while True:
        title_input = input("Enter task title: ")
        try:
            title = validate_title(title_input)
            break
        except ValidationError as e:
            print(f"\n{e}")

    # Get description with validation loop
    while True:
        description_input = input("Enter description (press Enter to skip): ")
        try:
            description = validate_description(description_input)
            break
        except ValidationError as e:
            print(f"\n{e}")

    # Create task
    task = add_task(title, description)

    # Success confirmation per add_task.spec.md
    print("\nTask added successfully!")
    print(f"  ID: {task.id}")
    print(f"  Title: {task.title}")
    print(f"  Description: {task.description if task.description else '(none)'}")
    print(f"  Status: {task.status}")

    _wait_for_enter()


def handle_view_tasks() -> None:
    """Handle View Tasks operation.

    Per view_tasks.spec.md CLI Flow Examples and contracts/cli-interface.md View Tasks Contract.
    """
    print("\n--- Task List ---")

    tasks = get_all_tasks()

    if not tasks:
        # Empty list message per view_tasks.spec.md FR-005
        print("No tasks found. Add a task to get started!")
        _wait_for_enter()
        return

    # Count completed/incomplete for summary
    complete_count = sum(1 for t in tasks if t.status == COMPLETE)
    incomplete_count = len(tasks) - complete_count

    # Grammar: "1 task" vs "X tasks" per view_tasks.spec.md Edge Cases
    task_word = "task" if len(tasks) == 1 else "tasks"
    print(f"Total: {len(tasks)} {task_word} ({complete_count} completed, {incomplete_count} incomplete)")
    print()

    # Display each task per view_tasks.spec.md FR-002
    for task in tasks:
        status_symbol = _get_status_symbol(task.status)
        print(f"[{task.id}] {status_symbol} {task.title}")
        print(f"    Description: {task.description if task.description else '(none)'}")
        print()

    _wait_for_enter()


def handle_delete_task() -> None:
    """Handle Delete Task operation.

    Per delete_task.spec.md CLI Flow Examples and contracts/cli-interface.md Delete Task Contract.
    """
    print("\n--- Delete Task ---")

    # Pre-check for empty list per delete_task.spec.md Edge Cases
    if not has_tasks():
        print("No tasks available to delete.")
        _wait_for_enter()
        return

    # Show available tasks with IDs
    _show_task_list_compact()

    # Get task ID with validation loop
    while True:
        id_input = input("Enter task ID to delete: ")
        try:
            task_id = validate_task_id(id_input)
            break
        except ValidationError as e:
            print(f"\n{e}")

    # Attempt to delete
    try:
        task = delete_task(task_id)
        print("\nTask deleted successfully!")
        print(f"  Deleted: [{task.id}] {task.title}")
    except TaskNotFoundError as e:
        print(f"\nError: {e}")

    _wait_for_enter()


def handle_update_task() -> None:
    """Handle Update Task operation.

    Per update_task.spec.md CLI Flow Examples and contracts/cli-interface.md Update Task Contract.
    """
    print("\n--- Update Task ---")

    # Pre-check for empty list per update_task.spec.md Edge Cases
    if not has_tasks():
        print("No tasks available to update.")
        _wait_for_enter()
        return

    # Show available tasks with IDs
    _show_task_list_compact()

    # Get task ID with validation loop
    while True:
        id_input = input("Enter task ID to update: ")
        try:
            task_id = validate_task_id(id_input)
            break
        except ValidationError as e:
            print(f"\n{e}")

    # Verify task exists
    try:
        task = get_task(task_id)
    except TaskNotFoundError as e:
        print(f"\nError: {e}")
        _wait_for_enter()
        return

    # Display current task details per update_task.spec.md CLI Flow
    print("\nCurrent task:")
    print(f"  ID: {task.id}")
    print(f"  Title: {task.title}")
    print(f"  Description: {task.description if task.description else '(none)'}")
    print(f"  Status: {task.status}")
    print()

    # Get new title (Enter to skip)
    new_title = None
    while True:
        title_input = input("Enter new title (press Enter to keep current): ")
        if not title_input:
            # Skip - keep current
            break
        try:
            new_title = validate_title(title_input)
            break
        except ValidationError as e:
            print(f"\n{e}")

    # Get new description (Enter to skip)
    new_description = None
    while True:
        desc_input = input("Enter new description (press Enter to keep current): ")
        if not desc_input:
            # Skip - keep current
            break
        try:
            new_description = validate_description(desc_input)
            break
        except ValidationError as e:
            print(f"\n{e}")

    # Perform update
    task, changes_made = update_task(task_id, new_title, new_description)

    if changes_made:
        print("\nTask updated successfully!")
        print(f"  ID: {task.id}")
        print(f"  Title: {task.title}")
        print(f"  Description: {task.description if task.description else '(none)'}")
        print(f"  Status: {task.status}")
    else:
        # No changes message per update_task.spec.md Example 5
        print("\nNo changes made. Task remains unchanged.")

    _wait_for_enter()


def handle_toggle_status() -> None:
    """Handle Mark Complete/Incomplete (Toggle) operation.

    Per mark_complete.spec.md CLI Flow Examples and contracts/cli-interface.md Toggle Contract.
    """
    print("\n--- Toggle Task Status ---")

    # Pre-check for empty list per mark_complete.spec.md Edge Cases
    if not has_tasks():
        print("No tasks available. Add a task first!")
        _wait_for_enter()
        return

    # Show available tasks with IDs
    _show_task_list_compact()

    # Get task ID with validation loop
    while True:
        id_input = input("Enter task ID: ")
        try:
            task_id = validate_task_id(id_input)
            break
        except ValidationError as e:
            print(f"\n{e}")

    # Get current status before toggle
    try:
        task = get_task(task_id)
        old_status = task.status

        # Perform toggle
        task = toggle_status(task_id)
        new_status = task.status
        new_symbol = _get_status_symbol(new_status)

        # Success confirmation per mark_complete.spec.md
        print("\nStatus changed!")
        print(f"  Task: [{task.id}] {task.title}")
        print(f"  Status: {old_status} -> {new_status} {new_symbol}")

    except TaskNotFoundError as e:
        print(f"\nError: {e}")

    _wait_for_enter()
