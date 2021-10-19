"""Unit tests for dictionary functions."""


__author__ = "730389688"

from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert() -> None:
    """Regular case."""
    a: dict[str, str] = {"Ava": "purple", "Taryn": "blue", "Sasha": "green"}
    assert invert(a) == {"purple": "Ava", "blue": "Taryn", "green": "Sasha"}


def test_invert_errorcase() -> None:
    """The color is already used."""
    a: dict[str, str] = {}
    a == {"Andy": "blue", "Kyle": "blue"}
    assert KeyError("Key is already used!")


def test_invert_nonthin() -> None:
    """Empty list."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_invert_samezies() -> None:
    """Same thing key, value."""
    a: dict[str, str] = {}
    a == {"blue": "blue"}
    assert invert(a) == {"blue": "blue"}


def test_favorite_color() -> None:
    """Regular case."""
    a = {"Ava": "purple", "Taryn": "purple", "Sasha": "green"}
    assert favorite_color(a) == "purple"


def test_favorite_color_doublefav() -> None:
    """Tie."""
    a = {"Ava": "purple", "Taryn": "purple", "Sasha": "green", "Kelsey": "pink", "Sarah": "green"}
    assert favorite_color(a) == "purple"


def test_favorite_color_empty() -> None:
    """Empty."""
    a = {}
    assert favorite_color(a) == ""


def test_count() -> None:
    """The regularshow."""
    one: list[str] = ["booty", "booties", "booties", "boot", "butt"]
    assert count(one) == {"booty": 1, "booties": 2, "boot": 1, "butt": 1}


def test_count_empty() -> None:
    """Nothing in list."""
    one: list[str] = []
    assert count(one) == {}


def test_count_manyofone() -> None:
    """All the same."""
    one: list[str] = ["hey", "hey", "hey", "hey", "hey"]
    assert count(one) == {"hey": 5}