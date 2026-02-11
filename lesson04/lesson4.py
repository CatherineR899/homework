# import statement 
from math import ceil

# input 
section1 = input("Enter number of planks in section 1: ")
section2 = input("Enter number of planks in section 2: ")
section3 = input("Enter number of planks in section 3: ")

# processing 
cans = len(section1) + len(section2) + len(section3)
boxes = ceil(cans / 12)
leftOver = (boxes * 12) - cans
cost = boxes * 14.95

# output 
print(f"Number of paint cans required: {cans}")
print(f"Number of paint cans left over: {leftOver}")
print(f"Total cost: ${cost}")