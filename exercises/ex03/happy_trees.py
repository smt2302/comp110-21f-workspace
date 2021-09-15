"""Drawing forests in a loop."""

__author__ = "730389688"


TREE: str = '\U0001F332'
i: int = 0
x: int = 0
stoppa: int = int(input("Depth: "))
output: str = ""

if stoppa <= 0:
    print()
else:
    while i < stoppa:
        x = i + 1
        output += TREE
        i = i + 1
        print(output)