"""Practice with dictionaries."""

__author__ = "730389688"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts one dictionary with another."""
    second_dictionary: dict[str, str] = {}
    for key in a:
        if a[key] in second_dictionary:
            raise KeyError("Key is already used!")
        second_dictionary[a[key]] = key
    return second_dictionary


def favorite_color(a: dict[str, str]) -> str:
    """Returns most said color."""
    color_dict: dict[str, int] = {}
    winning_color: str = ""
    current_max: int = 0
    for key in a:
        if a[key] in color_dict:
            color_dict[a[key]] += 1
        else:
            color_dict[a[key]] = 1
    for color in color_dict:
        if current_max < color_dict[color]:
            current_max = color_dict[color]
            winning_color = color
    return winning_color


def count(one: list[str]) -> dict[str, int]:
    """List into a dictionary."""
    thesarus: dict[str, int] = {}
    i: int = 0
    while i < len(one):
        if one[i] in thesarus:
            thesarus[one[i]] += 1
        else:
            thesarus[one[i]] = 1
        i += 1
    return thesarus