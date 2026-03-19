# my first try 
# num = int(input())
# prime = True
# if num == 1  or num == 0:
#     prime = False
# while prime:
#     for factors in range(2, int((num * 0.5) + 1)):
#         if num % factors == 0:
#             prime = False
#             break
#     break
# if prime:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


# mr. park's first solution 
# num = int(input())
# counter = 0
# for divider in range(1, num + 1):
#     if num % divider == 0:
#         counter += 1
# if counter == 2:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is a composite number")


# mr. park's second solution 
num = int(input())
is_prime = True
for divider in range(2, num):
    if num % divider == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a composite number")
