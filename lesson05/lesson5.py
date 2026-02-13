startingMoney = float(input("Enter the amount of starting money: "))
cookiesSold = (input("Enter the cookies sold: "))

# Count method: stringName.count(character)
bigCookies = cookiesSold.count("b")
normalCookies = cookiesSold.count("c")

# For each loop: for vairableName in listOrStringName 
# for cookieType in cookiesSold: 
#     if cookieType == "c":
#         normalCookies += 1
#     elif cookieType == "b":
#         bigCookies += 1
#     else: 
#         print(f"{cookieType} is not a valid item.")

totalCookies = bigCookies + normalCookies
profit = (bigCookies * 1.25) + (normalCookies * 0.75)
totalMoney = startingMoney + profit

print(f"{totalCookies} were sold.")
print(f"${profit} was made.")
print(f"Total money is now ${totalMoney}.")