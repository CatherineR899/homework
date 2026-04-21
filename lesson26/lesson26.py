def num_of_factors(N):
    counter = 2
    for factor in range(2, int(N * 0.5) + 1):
        if N % factor == 0:
            counter += 1
    return counter

print(num_of_factors(25))