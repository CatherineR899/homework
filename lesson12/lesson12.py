# input
angles = []
for i in range(3):
    angles.append(int(input(f"Enter angle {i+1}: ")))

# angle1 = int(input("Enter the first angle: "))
# angle2 = int(input("Enter the second angle: "))
# angle3 = int(input("Enter the third angle: "))

# processing + output
# if angles[0] > 0 and angles[1] > 0 and angles[2] > 0:
#     if sum(angles) == 180:
#         if angles[0] == angles[1] == angles[2]:
#             print("The angles make a equilateral triangle.")
#         elif angles[0] == angles[1] and angles[1] != angles[2]:
#             print("The angles make an isoceles triangle.")
#         elif angles[1] == angles[2] and angles[2] != angles[0]:
#             print("The angles make an isoceles triangle.")
#         elif angles[2] == angles[0] and angles[0] != angles[1]:
#             print("The angles make an isoceles triangle.")
#         else:
#             print("The angles make a scalene triangle.")
#     else: 
#         print("The angles do not make a triangle. ")
# else: 
#         print("The angles do not make a triangle. ")

# easier way
if angles[0] > 0 and angles[1] > 0 and angles[2] > 0:
    if sum(angles) == 180:
        if angles[0] == angles[1] == angles[2]:
            print("The angles make a equilateral triangle.")
        elif angles[0] != angles[1] != angles[2]:
            print("The angles make a scalene triangle.")
        else:
            print("The angles make an isoceles triangle.")
    else: 
        print("The angles do not make a triangle. ")
else: 
    print("The angles do not make a triangle.")