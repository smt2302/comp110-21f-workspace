"""Testing for my tree program"""
"""GUESSING SECTION"""

from random import randint
random: int = randint(1, 4)

points: int = 0
player: str = input("What is your name? ")
TREE: str = '\U0001F332'
RAIN: str = 'U+1F327'
THUNDERSTORM: str = 'U+26C8'
DROUGHT: str = 'U+1F3DC'
SNOW: str = 'U+2744'


def main() -> None:
    print(weather)


def weather(points: int) -> int:
    """function requirement"""
    RAIN: str = 'U+1F327'
    THUNDERSTORM: str = 'U+26C8'
    DROUGHT: str = 'U+1F3DC'
    SNOW: str = 'U+2744'
    global player
    i: int = 0
    while i <= 5:
        random: int = randint(1, 4)
        if random == 1:
            print(RAIN)
            choice: int = int(input(f"Oh look! There are some rain clouds blowing in. { player }, plant life decision time: choose 1 or 2. "))
            if choice > 1:
                print("You tried to save your plant by singing rain rain go away for 5 minutes and now your neighbors find you annoying...")
                points = points - 1
            else:
                print("Yay! You gave your plant a mini umbrella!")
                points = points + 1
        elif random == 2:
            print(THUNDERSTORM)
            choice: int = int(input(f"Oh no! Theres a thunderstorm approaching and you're afraid your plant is going to get struck by lightning. { player }, plant life decision time: choose 1 or 2. "))
            if choice > 1:
                print(f"Phew, {player}! You saved your plant by putting up a lighting rod nearby.")
                points = points + 1
            else:
                print("Your plant was struck and a branch fell off.")
                points = points - 1
        elif random == 3:
            print(DROUGHT)
            choice: int = int(input(f"Its a drought! Okay { player }, plant life decision time: choose 1 or 2. "))
            if choice > 1:
                print(f"Oh no, {player}! You chose to leave your plant to the elements, your plant is wilted")
                points = points - 1
            else:
                print(f"Good job, {player}! You took extra time to make sure your plant stayed watered. It is growing fabulously.")
                points = points + 1
        elif random == 4:
            print(SNOW)
            choice: int = int(input(f"Okay { player }, plant life decision time: choose 1 or 2. "))
            if choice > 1:
                print(f"Oh no, {player}! You chose to leave your plant to the elements, your plant is frozen!")
                points = points - 1
            else:
                print(f"Good job, {player}! You put a scarf on your tree to make sure it stayed warm:)")
                points = points + 1
        i = i + 1
    return points


if __name__ == "__main__":
    main()
    print(points)
