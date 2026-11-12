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
                if std_id==existing_id:
                     is_taken =True
                     break
     except FileNotFoundError:
             pass
     if is_taken:
         print("student Id is taken,try another Id")
     else:
         return std_id
#*******age is an intger numbers************
def validation_int(prompt_message):
    while True:
        try:
            return int(input(prompt_message))
        except ValueError:
            print("please enter a valid integer")
#$$$$$$$$$$$$$$$$$$$name$$$$$$$$$$$$$$$$$$$$$
def get_invalid_name(name):
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
#-----------------------------------------------------------
def add_student():
    print("Add Student")
    id = get_valid_id("Enter Student ID: ")
    name = get_invalid_name("Enter Student Name: ")
    email = email_validator("Enter your Student email: ")
    age = validation_int("Enter age: ")
    print("Successfully added Student")
    data_student = f"{id},{name},{email},{age}\n"
    with open ("student.txt","a") as file:
        file.write(data_student)
def display_student():
 with open ("student.txt","r") as f:
   for student in f:
    print(student.strip()+"\n")
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
 choice = validation_int ("Enter your choice: " )
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
