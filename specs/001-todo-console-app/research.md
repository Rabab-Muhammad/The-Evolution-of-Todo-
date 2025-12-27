# Research: Todo Console App - Phase I

**Branch**: `001-todo-console-app`
**Date**: 2025-12-27
**Status**: Complete

## Technical Context Resolution

All technical decisions are resolved from user requirements - no clarification needed.

| Item | Decision | Rationale |
|------|----------|-----------|
| Language/Version | Python 3.13+ | User specified |
| Package Manager | UV | User specified |
| Storage | In-memory (dict/list) | Phase I scope - no persistence |
| Testing | pytest | Industry standard for Python |
| Target Platform | Cross-platform (Windows/Linux/macOS) | Console apps are inherently portable |
| Project Type | Single project | Simple console application |

## Architecture Decisions

### 1. In-Memory Data Storage

**Decision**: Use a Python dictionary keyed by task ID for O(1) lookups.

**Rationale**:
- Dictionary provides O(1) access by ID (required for delete, update, toggle)
- Maintains insertion order in Python 3.7+ (useful for view ordering)
- Simple implementation aligns with Constitution Principle III (Simplicity)

**Alternatives Considered**:
- List with linear search: Rejected - O(n) lookups inefficient
- SQLite in-memory: Rejected - over-engineered for Phase I scope

### 2. ID Generation Strategy

**Decision**: Use a simple counter starting at 1, never recycled.

**Rationale**:
- Spec requires sequential IDs starting from 1 (add_task.spec.md FR-007)
- Spec requires deleted IDs are not reused (delete_task.spec.md Data Model Impact)
- Counter provides deterministic, predictable behavior per Constitution Principle II

**Implementation**: Store `next_id` as module-level variable, increment after each task creation.

### 3. Module Separation Strategy

**Decision**: Separate concerns into distinct modules:
- `models/task.py` - Task entity definition
- `services/task_service.py` - Business logic (CRUD operations)
- `cli/menu.py` - User interface and input handling
- `cli/handlers.py` - Operation-specific handler functions
- `main.py` - Application entry point

**Rationale**:
- Constitution Principle IV requires modular code with separation of concerns
- Each module has single responsibility
- Enables future extensibility for Phase II

**Alternatives Considered**:
- Single file: Rejected - violates maintainability principle
- Complex layered architecture: Rejected - over-engineered for Phase I

### 4. Input Validation Strategy

**Decision**: Centralized validation functions in a dedicated module.

**Rationale**:
- Common validation patterns across operations (ID validation, length limits)
- DRY principle - validate once, use everywhere
- Clear error messages per Constitution Principle III

**Validation Functions Needed**:
- `validate_task_id(input_str)` → int or raise ValidationError
- `validate_title(title)` → str or raise ValidationError
- `validate_description(description)` → str (always valid, may be empty)

### 5. Error Handling Strategy

**Decision**: Use custom exception classes for domain errors; catch at CLI layer.

**Rationale**:
- Spec requires clear error messages for all failure scenarios
- Separation between business logic errors and presentation
- CLI layer formats user-friendly messages

**Exception Types**:
- `TaskNotFoundError` - Task ID doesn't exist
- `ValidationError` - Input fails validation rules
- `EmptyTaskListError` - Operation requires tasks but none exist

### 6. Console UI Design

**Decision**: Simple numbered menu with clear prompts, "Press Enter to continue" pattern.

**Rationale**:
- Matches CLI flow examples in all specification files
- Constitution Principle III requires intuitive navigation
- Minimal steps for common operations

## Best Practices Applied

### Python 3.13+ Features
- Type hints for all function signatures
- Dataclasses for Task entity
- f-strings for output formatting
- Walrus operator where appropriate

### Code Quality
- PEP 8 compliance
- Descriptive naming conventions
- Docstrings for public functions
- No external dependencies (stdlib only)

### Testing Strategy
- Unit tests for each service function
- Integration tests for CLI flows
- Edge case coverage from spec acceptance criteria

## Dependencies

**Runtime Dependencies**: None (Python stdlib only)

**Development Dependencies**:
- pytest >= 8.0 (testing)
- pytest-cov (coverage reporting)

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Unicode checkmark display issues | Low | Low | Use ASCII fallback [X] / [✓] |
| Large task list performance | Very Low | Low | In-memory dict is efficient; out of scope per Phase I |
| Input encoding issues | Low | Medium | Use UTF-8 encoding explicitly |

## Conclusion

All technical decisions are resolved. The architecture is intentionally simple to align with Phase I scope and Constitution Principle III (Simplicity). The modular structure supports Constitution Principle IV (Maintainability) for future phases.

**Ready for**: Phase 1 Design (data-model.md, contracts/)
