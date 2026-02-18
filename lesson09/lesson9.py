# import statement 
from random import choice 

# input
invalid = True
player = ""

while invalid: 
    player = input("Enter rock, paper, or scissors: ")
    if player in {"rock", "paper", "scissors"}:
        invalid = False 

# processing 
# choice() randomly assigns a value from the list 
ai = choice(["rock", "paper", "scissors"])

if player == ai:
    print("Tied Game")
else: 
    if player == "rock":
        if ai == "paper":
            print("AI Won")
        else:
            print("Player Won")
    elif player == "paper":
        if ai == "scissors":
            print("AI Won")
        else:
            print("Player Won")
    else: 
        if ai == "rock":
            print("AI Won")
        else:
            print("Player Won")