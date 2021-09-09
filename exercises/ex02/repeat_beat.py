"""Repeating a beat in a loop."""

__author__ = "730389688"


beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
output: str = ""

if repeat <= 0:
    print("No beat...")
else:
    i: int = 0
    while i < repeat:
        output += beat
        if i < repeat - 1:
            output += " "
        i = i + 1
    print(output)