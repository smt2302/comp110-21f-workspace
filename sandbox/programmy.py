"""TESTING"""

from random import randint
random: int = randint(1, 100)
points: int = 0
player: str = input("What is your name? ")
 
  
 
print(f"Hello {player}, here, you will need to do some math to keep your plant alive")
print("This is a quick math game. Get the answer right or the health of your plant is at stake!!")
print(f" {random} ")
 
active: bool = True
while active:
    if random % 5 == 0:
        print("Correct!")
        points = points + 1
    else:
        print("Better luck next time!")
        points = points - 1
 
print(points)
