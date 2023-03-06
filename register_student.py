from main import Student

try:
    student_name = input("Enter name \n")
    student_email = input("Enter email \n")
    student_pwd = input("Enter Password \n")

    Student.create(stud_name=student_name, stud_email=student_email, stud_pwd=student_pwd)
    print("Student Created Successfully")
except:
    print("Failed to Create Student")
