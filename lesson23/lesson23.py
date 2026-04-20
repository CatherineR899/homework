# # my try 
# total_sum = 0
# num_inputs = 0
# while True:
#     user_input = input()
#     if user_input.lower() == "exit":
#         break
#     elif int(user_input) >= 0 and int(user_input) <= 100:
#         total_sum += int(user_input)
#         num_inputs += 1
# average = total_sum/num_inputs
# print(average)
# # what's wrong? cannot input anything besides numbers or exit, other words cause an error 

# mr. park's
loop = True 

total_sum = 0
counter = 0

while loop:
    user_input = input("Enter the mark or Exit to stop inputting marks. ")
    if user_input.lower().capitalize() == "Exit":
        loop = False
        break
    else:
        mark = int(user_input)
        if 0 <= mark and mark <= 100:
            total_sum += mark
            counter += 1
        else:
            print("Invalid input.")

average = total_sum / counter
print(f"Mark Average: {average}")