def get_valid_id(id):
  while True:
     #Numbers only
     std_id=input(id)
     if not std_id.isdigit():
         print("Please enter a valid Student ID")
         continue
   #Don't repeat
     is_taken=False
     try:
         with open ("student.txt","r") as file:
            for student in file:
              if student.strip():
                existing_id=student.strip().split(",")[0]
                if int(std_id)==int(existing_id):
                     is_taken =True
                     break
     except FileNotFoundError:
             pass
     if is_taken:
         print("student Id is taken,try another Id")
     else:
         return int(std_id)
#*******age is an intger numbers************
def validation_int(prompt_message):
    while True:
        try:
            return int(input(prompt_message))
        except ValueError:
            print("please enter a valid integer")
#$$$$$$$$$$$$$$$$$$$name$$$$$$$$$$$$$$$$$$$$$
def get_valid_name(name):
    while True:
        std_name=input(name)
        if std_name.startswith(" ")or len(std_name.strip())==0:
            print("please enter a valid student name(can't e empty or start with space)")
            continue
        cleanName = std_name.replace(" ","")
        if cleanName.isalpha():
            return std_name
        else:
            print("please enter a valid student name (Write letters only)")
#**********************Email********************************
def email_validator(email):
    while True:
        std_email=input(email)
        if '@' in std_email and not std_email.startswith("@") and not std_email.endswith("@"):
            return std_email
        else:
            print("please enter a valid email address")
#^^^^^^^^^^Age^^^^^^^^^^^^^^
def age_validator(age):
    while True:
        std_age=input(age)
        if std_age.isdigit():
            age_num=int(std_age)
            if 18<=age_num<=25:
                return age_num
            else:
                print("Age must be between 18 and 25")
#another logic---
#after using same def and  while True:
# try :
  #   std_age=int(input(age))
  #   if 18<=std_age<=25:
  #     return std_age
  #   else:
  #     print("age must e between 18 and 25")
# except ValueError :
  #     print("Enter digits only!Try again")
  #note ("I try to learn codes that match my logic thinking like these comments
  # Every comment points to logic I liked or other thoughts and tried to learn them)
  #I hope u enjoy my coding
#-----------------------------------------------------------
def add_student():
    print("Add Student")
    id = get_valid_id("Enter Student ID: ")
    name = get_valid_name("Enter Student Name: ")
    email = email_validator("Enter your Student email: ")
    age = age_validator("Enter age: ")
    print("Successfully added Student")
    data_student = f"{id},{name},{email},{age}\n"
    student_list=[]
    try:
        with open("student.txt","r") as file:
         for student in file:
             if student.strip():
                 student_list.append(student)
    except FileNotFoundError:
        pass
    student_list.append(data_student)
    student_list.sort(key =lambda x:int (x.strip().split(",")[0]))
    with open ("student.txt","w") as file:
        for student in student_list:
          file.write(student)
    print("Successfully added and sorted students")

def display_student():
 try:
  with open ("student.txt","r") as f:
   for student in f:
    if student.strip():
     student_data = student.strip().split(",")
     print(f"ID:{student_data[0]},Name:{student_data[1]},Email:{student_data[2]},Age:{student_data[3]}\n")
 except FileNotFoundError:
     print("Add students FIRSTLY!")
def search_student(id):
    try:
        with open("student.txt","r") as f:
            for student in f:
                if student.strip():
                    data =student.strip().split(",")
                    if id== int(data[0]):
                        print("student was found")
                        print(f"ID:{data[0]},Name:{data[1]},Email:{data[2]},Age:{data[3]}")
                        return
            print("student ID not found")
    except FileNotFoundError:
        print("student ID not found")
def update_student(id,new_name,new_email,new_age):
    try:
        with open("student.txt","r") as file:
            lines=file.readlines()
        found=False
        with open("student.txt","w")as file:
            for line in lines:
                if line.strip():
                    data=line.strip().split(",")
                    if id==int (data[0]):
                        file.write(f"{id},{new_name},{new_email},{new_age}\n")
                        found=True
                    else:
                        file.write(line)
        if found:
                    print("student updated successfully")
        else:
                    print("student not found to update")
    except FileNotFoundError:
        print("The file doesn't exist")
def delete_student(id):
    try:
        with open("student.txt","r") as file:
            lines=file.readlines()
        found=False
        with open("student.txt","w") as file:
            for line in lines:
                if line.strip():
                    data=line.strip().split(",")
                    if id == int(data[0]):
                        found=True
                        continue
                    file.write(line)
        if found :
            print("student deleted successfully")
        else:
            print("student not found to delete")
    except FileNotFoundError:
        print("The file doesn't exist")

#@@2@ @@@@@@@@@@@@@
while True:
 print("======STUDENT INFORMATION ======")
 print("1: Add Student")
 print("2: display Student")
 print("3: search Student ")
 print("4: Update Student")
 print("5: delete Student")
 print("6: Exit")
 choice = validation_int ("Enter your choice: " )
 if choice == 1:
     add_student()
 elif choice == 2:
   display_student()
 elif choice == 3:
    id=validation_int("Enter Student ID: ")
    search_student(id)
 elif choice == 4:
     id = validation_int("Enter Student ID: ")
     new_name = get_valid_name("Enter Student New Name: ")
     new_email = email_validator("Enter Student New Email: ")
     new_age = age_validator("Enter Student New Age: ")
     update_student(id, new_name, new_email, new_age)
 elif choice == 5:
     id = validation_int("Enter Student ID: ")
     delete_student(id)
 else:
     break
