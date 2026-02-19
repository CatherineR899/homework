# x = int(input("Enter the x-coordinate: "))
# y = int(input("Enter the y-coordinate:"))
point = input("Enter the coordinates (format = x, y): ")
# .split() turns a string into a list by separating values with the inputted string
# "10,-11" --> ["10", "-11"]
point = point.split(", ")

''' long form solution to convert a string list to integer list 
fixedPoint = []
for value in point:
    fixedPoint.appead(int(value))
'''

# map() turns values in a vairable to a different datatype, doesn't maintain the list, creates an iterable object where you can see the values but not change them
# list() turns iterable objects into actual lists when you can change their values in the list
point = list(map(int, point))

# vairable unpacking 
x, y = point

if x > 0:
    if y > 0:
        print(f"({x},{y}) is in Quandrant 1.")
    else:
        print(f"({x},{y}) is in Quandrant 4.")
else: 
    if y > 0:
        print(f"({x},{y}) is in Quandrant 2.")
    else: 
        print(f"({x},{y}) is in Quandrant 3.")