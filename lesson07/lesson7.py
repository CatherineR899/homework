from random import randrange

difficultyClass = int(input("Enter the difficulty class: "))

# Random range: randrange(a, b) 
# Random generated number is between a to b, including a, but not b
D20 = randrange(1, 21)

if D20 >= difficultyClass: 
    print(f"The player rolled a {D20}. The action succeeds.")
else: 
    print(f"The player rolled a {D20}. The action fails.")