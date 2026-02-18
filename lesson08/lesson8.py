# input
winCounter = 0
# for _ in range(n) --> iterates n times, starts from 0 and counts to n-1
for i in range(6):
    gameResult = input(f"Enter the result for game {i+1}: ")
    if gameResult == "W":
        winCounter += 1

# using >= or <= causes program to check two operations, < or > and =
# if winCounter >= 5:
#     print(f"{winCounter} games were won. You placed Group 1.")
# elif winCounter >= 3:
#     print(f"{winCounter} games were won. You placed Group 2.")
# elif winCounter >= 2:
#     print(f"{winCounter} games were won. You placed Group 3.")
# else: 
#     print("0 Games were won. You have been eliminated.")

# processing
group = 0
if winCounter > 4:
    group = 1
elif winCounter > 2:
    group = 2
elif winCounter > 0:
    group = 3

# output
if group == 0:
    print("Player has been eliminated.")
else: 
    print(f"{winCounter} games won. Player placed in Group {group}")