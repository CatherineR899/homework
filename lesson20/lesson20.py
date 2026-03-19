# # my try 
# totalSum = 0
# for num in range(2, 10000):
#     factors = []
#     for divider in range(1, num):
#         if num % divider == 0:
#             factors.append(divider)
#     factorSum = 0
#     for factor in factors:
#         factorSum += factor
#     if factorSum == num:
#         totalSum += num
# print(totalSum)


# mr park's solution 
total_sum = 0
for num in range(1, 10000):
    factor_sum = 0
    for divider in range(1, num):
        if num % divider == 0:
            factor_sum += divider
    if factor_sum == num:
        total_sum += num
print(total_sum)