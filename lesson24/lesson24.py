# # my try
# loop = True
# longest_name = ""
# longest_length = 0
# while loop:
#         user_input = input("Enter a name or '''X''' to stop entering inputs. ")
#         if len(user_input) > longest_length:
#             longest_name = user_input
#             longest_length = len(user_input)
#         elif user_input == "'''X'''":
#             loop = False
#             break
# print(longest_name)

# mr park's 
name = ""
longest_length = 0
longest_name = ""
while name != "X":
    name = input("Enter a name or X to exit. ")
    current_length = len(name)
    if name != "X":
        if current_length > longest_length:
            longest_length = current_length
            longest_name = name
    else: 
        print("End of inputs.")    

if longest_name:
    print(f"The longest name with {longest_length} characters is {longest_name}.")
else:
    print("Not enough data.")