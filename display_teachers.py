from main import Teacher

teachers = Teacher.select()
for teacher in teachers:
    print(teacher.tr_name, teacher.tr_email, teacher.tr_pwd)