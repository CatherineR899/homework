# # my try
# N = int(input())
# fibonacci = [0, 1]
# if N == 0:
#     print(fibonacci[0])
# elif N == 1:
#     print(fibonacci[1])
# for term in range(2, N + 1):
#     termValue = fibonacci[term - 2] + fibonacci[term - 1]
#     fibonacci.append(termValue)
# print(fibonacci[N])


# mr. park's solution
upper_limit = int(input())
fib_0 = 0
fib_1 = 1
fib_n = 0
for n in range(2, upper_limit + 1):
    fib_n = fib_1 + fib_0
    fib_0 = fib_1
    fib_1 = fib_n
print(f"Fibonacci({upper_limit}) is {fib_n}.")