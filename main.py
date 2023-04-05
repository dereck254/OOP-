from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Dereck.db"))


#creating our first table

class Student(Model):
    stud_name = CharField()
    stud_email = CharField()
    stud_pwd = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)


class Teacher(Model):
    tr_name = CharField()
    tr_email = CharField()
    tr_pwd = CharField()

    class Meta:
        database = db


Teacher.create_table(fail_silently=True)

class Product(Model):
    prod_price = IntegerField()
    prod_quantity = IntegerField()
    prod_description = CharField()
    color = CharField()

    class Meta:
        database = db


Product.create_table(fail_silently=True)

class User(Model):
    user_name = CharField()
    user_phone = CharField()
    user_email = CharField()
    user_pwd = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)

