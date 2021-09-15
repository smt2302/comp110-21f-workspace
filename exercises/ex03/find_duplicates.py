"""Finding duplicate letters in a word."""

__author__ = "730389688"

word: str = input("Enter a word: ")
calculator: bool = False
i: int = 0
x: int

while i < len(word):
    x = i + 1
    while x < len(word):
        if word[i] == word[x]:
            calculator = True
        x = x + 1
    i = i + 1
print("Found duplicate: " + str(calculator))