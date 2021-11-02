"""Utility functions."""

__author__ = "730389688"

from csv import DictReader


def read_csv_rows(data_rows: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(data_rows, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for key in csv_reader:
        result.append(key)
    return result


def column_values(one: list[dict[str, str]], two: str) -> list[str]:
    """Make a list of all values in a single cloumn whose name is on parameter 2."""
    empty_list: list[str] = []
    for column in one:
        object: str = column[two]
        empty_list.append(object)
    return empty_list


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Making a table of lists with dictionarires in them into dictionaries with lists in them."""
    empty_dict: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for column in first_row:
        empty_dict[column] = column_values(table, column)
    return empty_dict


def head(columnbased_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with the first N values.""" 
    result: dict[str, list[str]] = {}
    if rows == 0:
        result = {}
    if rows >= len(columnbased_table):
        return columnbased_table
    for column in columnbased_table:
        i: int = 0
        item: list[str] = []
        while i < rows:
            item.append(columnbased_table[column][i])
            i += 1
        result[column] = item
    return result


def select(column_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Column based table with spefic columns you want to use."""
    result: dict[str, list[str]] = {}
    for key in columns:
        result[key] = column_table[key]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Two column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in a:
        result[key] = a[key]
    for lock in b:
        if lock in result:
            result[lock] += b[lock]
        else:
            result[lock] = b[lock]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counting number of times a list appears in a list."""
    counter: dict[str, int] = {}
    for key in values:
        if key in counter:
            counter[key] += 1
        else:
            counter[key] = 1
    return counter