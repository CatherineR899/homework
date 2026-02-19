# input
month = int(input("Enter the month as a number: "))
day = int(input("Enter the day: "))

# processing + output 
if month < 2:
    print("Before")
elif month > 2:
    print("After")
else: 
    if day < 18:
        print("Before")
    elif day > 18:
        print("After")
    else:
        print("Special")