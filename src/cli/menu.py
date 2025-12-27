"""Main menu for Todo Application.

Per contracts/cli-interface.md Main Menu Contract and all spec files CLI Flow Examples.
"""

import sys

from src.validators import validate_menu_choice
from src.exceptions import ValidationError
from src.cli.handlers import (
    handle_add_task,
    handle_view_tasks,
    handle_delete_task,
    handle_update_task,
    handle_toggle_status,
)


def display_menu() -> None:
    """Display the main menu.

    Per contracts/cli-interface.md Main Menu Contract Display.
    """
    print("\n=== Todo Application ===")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. View Tasks")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print()


def get_menu_choice() -> int:
    """Get and validate menu choice from user.

    Returns:
        Valid menu choice as integer (1-6)

    Per contracts/cli-interface.md Main Menu Contract Input.
    Re-prompts on invalid input per Common Patterns.
    """
    while True:
        choice_input = input("Enter choice: ")
        try:
            return validate_menu_choice(choice_input)
        except ValidationError as e:
            print(f"\n{e}")
            print()


def run() -> None:
    """Run the main application loop.

    Per spec.md FR-006: System returns to main menu after each operation.
    Per contracts/cli-interface.md Exit Contract.
    """
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            handle_add_task()
        elif choice == 2:
            handle_delete_task()
        elif choice == 3:
            handle_update_task()
        elif choice == 4:
            handle_view_tasks()
        elif choice == 5:
            handle_toggle_status()
        elif choice == 6:
            # Exit per contracts/cli-interface.md Exit Contract
            print("\nGoodbye!")
            sys.exit(0)
