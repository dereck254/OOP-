from main import Teacher

try:
    teacher_name = input("Enter name \n")
    teacher_email = input("Enter email \n")
    teacher_pwd = input("Enter Password \n")

    Teacher.create(tr_name=teacher_name, tr_email=teacher_email, tr_pwd=teacher_pwd)
    print("Teacher Created Successfully")
except:
    print("Failed to Create Teacher")