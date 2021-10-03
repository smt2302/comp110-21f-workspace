"""List utility functions."""

__author__ = "730389688"


def all(x: list[int], y: int) -> bool:
    """Return True if all numbers match."""
    i: int = 0
    if len(x) == 0:
        return False
    while i < len(x):
        if x[i] != y:
            return False
        i += 1
    return True


def is_equal(a: list[int], b: list[int]) -> bool:
    """Testing lengths of lists."""
    i: int = 0
    k = i
    while len(a) == 0 and len(b) == 0:
        return True
    while len(a) != len(b):
        return False
    while i < len(a or b):
        if a[i] == b[k]:
            return True
        i += 1
    return False


def max(z: list[int]) -> int:
    """Booty!"""
    i: int = 0
    current_max: int = z[0]
    if len(z) == 0:
        print("ValueError: max() arg is an empty List")
    while i < len(z):
        if z[i] > current_max:
            current_max = z[i]
        i += 1
    return current_max