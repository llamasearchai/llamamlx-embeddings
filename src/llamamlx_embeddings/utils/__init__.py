"""
Utility functions for llamamlx-embeddings.

This package contains various utilities used by the library.
"""

from .error_handling import (
    DependencyError,
    ModelNotFoundError,
    check_dependency,
    configure_logging,
    handle_fatal_error,
    require_dependency,
    safe_import,
    with_fallback,
)

__all__ = [
    "configure_logging",
    "check_dependency",
    "require_dependency",
    "safe_import",
    "with_fallback",
    "handle_fatal_error",
    "DependencyError",
    "ModelNotFoundError",
]
