# input
phone = input("Enter the last four digits of the phone number: ")

# processing + output
# indexing for string, list, or tuple: variableName[#]
#if phone[0] == 8 or phone[0] == 9:

if phone[0] in {"8","9"}: 
    if phone[1] == phone[2]:
        if phone[3] in {"8","9"}:
            print(f"{phone} are the last four digits of a telemarketer.")
        else: 
            print(f"{phone} are not the last four digits of a telemarketer.")
    else: 
            print(f"{phone} are not the last four digits of a telemarketer.")
else: 
            print(f"{phone} are not the last four digits of a telemarketer.")