"""Unit tests for list utility functions."""

__author__ = "730389688"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_both() -> None:
    """Evens and odds test."""
    bean: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(bean) == [2, 4]


def test_only_evens_none() -> None:
    """List empty test."""
    bean: list[int] = []
    assert only_evens(bean) == []


def test_only_evens_odds() -> None:
    """Only odds test."""
    bean: list[int] = [1, 3, 5]
    assert only_evens(bean) == []


def test_sub_normal() -> None:
    """First one of sub."""
    fajita: list[int] = [10, 20, 30, 40]
    index: int = 1
    last_index: int = 3
    assert sub(fajita, index, last_index) == [20, 30]


def test_sub_empty_list() -> None:
    """Nothing is in the list."""
    fajita: list[int] = []
    index: int = 0
    last_index: int = 1
    assert sub(fajita, index, last_index)


def test_sub_negitive() -> None:
    """Not sure what I am doing love."""
    fajita: list[int] = [-1, -2, 4, 5]
    index: int = -1
    last_index: int = 3
    assert sub(fajita, index, last_index)


def test_concat_one() -> None:
    """Two normal lists."""
    asparagus: list[int] = [1, 2, 3, 4, 5]
    peanuts: list[int] = [6, 7, 8, 9]
    assert concat(asparagus, peanuts) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_concat_two() -> None:
    """One list is empty!"""
    asparagus: list[int] = [1, 2, 3]
    peanuts: list[int] = []
    assert concat(asparagus, peanuts) == [1, 2, 3]


def test_concat_three() -> None:
    """Repeated numbers!"""
    asparagus: list[int] = [1, 2, 3]
    peanuts: list[int] = [1, 2, 3]
    assert concat(asparagus, peanuts) == [1, 2, 3, 1, 2, 3]