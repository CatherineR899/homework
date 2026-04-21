# my try 
# how to solve: determine all factors, determine which factors are prime, find the greatest one 
# n = int(input())
# factors = []
# for i in range(2, n):
#     if n % i == 0:
#         factors.append(i)
# primes = []
# for factor in factors:
#     factors_of_factors = []
#     for i in range(2, factor):
#         if factor % i == 0:
#             factors_of_factors.append(i)
#     if len(factors_of_factors) == 0:
#         primes.append(factor)
# if len(primes) == 0:
#     print("No prime factors.")
# else:
#     max_prime_factor = max(primes)
#     print(max_prime_factor)

# mr. park's 
num = int(input("Enter a value of N:"))
num_copy = num

while num % 2 == 0:
    num //= 2
    largest = max(largest, 2)

if num != 1:
    factor = 3
    while num != 1:
        if num % factor == 0:
            largest = max(largest, factor)
            num //= factor 
        else:
            factor += 2 # adds 2 because the factor then becomes the next odd number, the only even prime is 2 

print(f"{largest} is the largest prime factor for {num_copy}")

# concepts of primes: 
# only even prime is 2 
# all other primes are odd 
# can divide numbers by only primes to see if they are factors 
