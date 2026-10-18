from random import choice

print("\n\n======STUDENT INFORMATION ======")
print("1: Add Student")
print("2: display Student")
print("3: search Student ")
print("4: Update Student")
print("5: delete Student")
print("6: Exit")

choice = int(input ("Enter your choice: " ))
if choice == 1:
    print("Student Added")
elif choice == 2:
    print("display Student")
elif choice == 3:
    print("search Student")
elif choice == 4:
    print("Update Student")
else:
    print("Exit")
