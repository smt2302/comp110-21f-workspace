"""Counting letters in a string."""

__author__ = "730389688"


letter: str = input("What letter do you want to search for?: ")
number: str = input("Enter a word: ")
i: int = 0
s: int = 0

while i < len(number):
    if letter == number[i]:
        i = i + 1
        s = s + 1
    else:
        i = i + 1
    
print("Count: " + str(s))