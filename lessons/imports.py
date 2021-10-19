"""Example of importing in Python(helpers.py, """


from lessons import helpers


def main() -> None:
    """Entry point of our program"""
    print(helpers.powerful(2, 4))
    print(F"The answer: {helpers.THE_ANSWER}")


if __name__ == "__main__":
    main()