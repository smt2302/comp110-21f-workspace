"""Example of a function that processes a list."""


def main() -> None:
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kris", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in haystack, False otherwise."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False


# Python Idiom for starting the main function
if __name__ == "__main__":
    main()


# define a function named contains
# We can give two arguements: a needle value we're searching for in a haystack list
    # Return true if needle found and false otherwise
    # Loop through each items in list
        # Test if item stored at index is equal to needle
        # Return true if so
    # Return false after testing each