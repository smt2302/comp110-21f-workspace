"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730389688"


from random import randint

print("Your fortune cookie says...")

random: int = randint(1, 4)
if random == 1:
    print("You will make a new friend very soon")
else:
    if random == 2:
        print("This month will be fruitful for you")
    else:
        if random == 3:
            print("You will discover a new hobby soon")
        else:
            print("You will eat pie tomorrow")

print("Now, go spread positive vibes!")