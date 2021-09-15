"""An exercise in remainders and boolean logic."""

__author__ = "730389688"


somethin: int = int(input("Enter an int: "))

if somethin % 14 == 0:
    print("TAR HEELS")
else:
    if somethin % 2 == 0:
        print("TAR")
    else:
        if somethin % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")