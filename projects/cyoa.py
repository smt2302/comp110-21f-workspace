"""Choose Your Own Adventure Program!"""

from random import randint

random: int = randint(1, 4)
points: int = 0
player: str = ""

TREE: str = '\U0001F332'
BB_TREE: str = '\U0001F331'


def main() -> None:
    """Entrypoint."""
    greet()
    active: bool = True
    while active:
        thing: int = int(input("Would you like to play the game?? Yes(1) or No(2)? "))
        if thing == 1:
            another: int = int(input("Horray! Play game 1 or 2? "))
            if another == 1:
                print(weather(points))
            else:
                print(second_game())
        elif thing == 2:
            print("Thats too bad, goodbye.")
            active = False
        print(f"Total Points Earned: {points}")
    if points >= 5:
        print(f"Youve won the game. Here is your tree {TREE} !")
    else:
        print(f"Your seedling never grew to a tree:( {BB_TREE}")


def greet() -> None:
    """Greets player."""
    global player
    player = input("What is your name? ")
    print(input(f"Hello there! {player}! This is a game about a plant. You have a seedling {BB_TREE}, if you earn 5 points or more your seedling will grow to a tree!"))


def weather(points: int) -> int:
    """Function Requirement."""
    RAIN: str = '\U0001F327'
    THUNDERSTORM: str = '\U000026C8'
    DROUGHT: str = '\U0001F3DC'
    SNOW: str = '\U00002744'
    i: int = 0
    print("You are an overbearing tree parent and you must fight against the incoming elements to keep your plant alive.")
    print("Use your instincts to choose 1 or 2 and hope you made the right decision for taking care of your plant baby...Good luck!")
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
            choice = int(input(f"Oh no! Theres a thunderstorm approaching and you're afraid your plant is going to get struck by lightning. { player }, plant life decision time: choose 1 or 2. "))
            if choice > 1:
                print(f"Phew, {player}! You saved your plant by putting up a lighting rod nearby.")
                points = points + 1
            else:
                print("Your plant was struck and a branch fell off.")
                points = points - 1
        elif random == 3:
            print(DROUGHT)
            choice = int(input(f"Its a drought! Okay { player }, plant life decision time: choose 1 or 2. "))
            if choice > 1:
                print(f"Oh no, {player}! You chose to leave your plant to the elements, your plant is wilted")
                points = points - 1
            else:
                print(f"Good job, {player}! You took extra time to make sure your plant stayed watered. It is growing fabulously.")
                points = points + 1
        elif random == 4:
            print(SNOW)
            choice = int(input(f"Okay { player }, plant life decision time: choose 1 or 2. "))
            if choice > 1:
                print(f"Oh no, {player}! You chose to leave your plant to the elements, your plant is frozen!")
                points = points - 1
            else:
                print(f"Good job, {player}! You put a scarf on your tree to make sure it stayed warm:)")
                points = points + 1
        i = i + 1
    return points


def second_game() -> int:
    """Guessing Game!"""
    global points
    points
    random: int = randint(1, 10)
    print("Lucky round!! Guess a number between 1-5, get it right and automatically get 5 points! Guess wrong and you lose 1.")
    print("I'm thinking of a number between 1 and 5...")
    guess = int(input("Your guess: "))
    if guess == random:
        points = points + 5
    else:
        points = points - 1 
    print(f"The answer: {random}")
    print(points)
    return points   


if __name__ == "__main__":
    main()
