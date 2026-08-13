from __future__ import annotations

# Compatibility entry point retained for historical workflows and imports.
# Immutable historical completion checks remain in their dedicated module;
# current/final program-state validation is centralized in the state validator.
from validate_ppia_historical_completions import historical_completion_checks
from validate_ppia_program_state import main

__all__ = ["historical_completion_checks", "main"]


if __name__ == "__main__":
    raise SystemExit(main())
