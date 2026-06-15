"""
@file: Jit.py
@brief: Configuration to enable JIT compilation
@description: Add a decorator to configure functions for JIT compilation
"""

from numba import njit

enabled = False


def proxy(*args, **kws):
    """Decorator that does nothing to the function (just returns it unmodified)."""

    def wrapper(func):
        return func

    return wrapper


configure = proxy
if enabled:
    configure = njit
