"""List utility functions part 2."""

__author__ = "730389688"


def only_evens(bean: list[int]) -> list[int]:
    """Evens gang only!!"""
    i: int = 0
    the_evens: list[int] = list()
    while i < len(bean):
        if bean[i] % 2 == 0:
            the_evens.append(bean[i])
        i += 1
    return the_evens


def sub(fajita: list[int], index: int, last_index: int) -> list[int]:
    """Ninki Minjaj."""
    a_list: list[int] = list()
    i: int = index
    if i < 0:
        i = 0
    while i < len(fajita):
        if i >= index and i < last_index:
            a_list.append(fajita[i])
        i += 1
    return a_list


def concat(asparagus: list[int], peanuts: list[int]) -> list[int]:
    """Miss Camraderie."""
    i: int = 0
    j: int = 0
    total: list[int] = list()
    while i < len(asparagus):
        total.append(asparagus[i])
        i += 1
    while j < len(peanuts):
        total.append(peanuts[j])
        j += 1
    return total
