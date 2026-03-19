num = int(input())
factors = []
for factor in range(1, num + 1):
    if num % factor == 0: 
        factors.append(factor)
print(factors)