student_list = []
def add_student():
    print("Add Student")
    id = (input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    email = input("Enter your Student email: ")
    age = int(input("Enter age: "))
    print("Successfully added Student")
    data_student = (id,name,email, age)
    student_list.append(data_student)
def display_student():
  for student in student_list:
    print("Student ID is ", student[0])
    print("Student Name is ", student[1])
    print("Student Email is", student[2])
    print("Student age is ", student[3])
def search_student():
    print("search Student ")
def update_student():
    print("Update Student")
def delete_student():
    print("Delete Student")
while True:
 print("======STUDENT INFORMATION ======")
 print("1: Add Student")
 print("2: display Student")
 print("3: search Student ")
 print("4: Update Student")
 print("5: delete Student")
 print("6: Exit")
 choice = int(input ("Enter your choice: " ))
 if choice == 1:
     add_student()
 elif choice == 2:
   display_student()
 elif choice == 3:
    search_student()
 elif choice == 4:
     update_student()
 elif choice == 5:
     delete_student()
 else:
     break
