# import statement (from module import functions)
from math import sqrt, floor

# input
tiles = int(input("Enter the number of tiles: "))

# processing
largestSide = floor(sqrt(tiles))

# output
print(f"The largest square side possible is {largestSide}.")
