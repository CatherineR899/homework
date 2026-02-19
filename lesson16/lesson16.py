# range() is a generator function that creates iterable integers in a given parameter 

# range(x) generates numbers 0 up to x, not including x
# range(a, b) generates numbers a up to b, not including b
# range(a, b, c) generates numbers a up to b, not including b, but the numbers increase by c
#   e.g. range(1, 10, 2) generates 1, 3, 5, 7, 9
#   e.g. range(1-, 0, -1) generates 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 

# for loops are used to look through values in an iterable object

for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0: 
        print("FizzBuzz")
    elif num % 3 == 0: 
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else: 
        print(num)