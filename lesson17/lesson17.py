# input
num = int(input("Enter a number: "))
product = 1

# multiplier = 2
# while multiplier <= num:
#     product *= multiplier
#     multiplier += 1

# for multiplier in range(num, 0, -1):
#     product *= multiplier

for multiplier in range(2, num + 1):
    product *= multiplier

print(f"The factorial of {num} is {product}.")