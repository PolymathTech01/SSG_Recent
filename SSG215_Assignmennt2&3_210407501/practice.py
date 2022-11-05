def square_a_number(num=2):
    """
    parameter:
        num -> int | float
    It squares the num

    return -> int | float
        answer
    """
    answer = num ** 2
    return answer


square = square_a_number()
print(square)


def greet():
    name = input("What is your name? ")
    return f"{name} How are you?"


# print(greet())

# def, if, else, elif, while, for
# lkjfajflajf

# dlflajfdkf

# OOP

# Constructor
# Object
# method
# instantiation
# instance
# Inheritance

# num1 = 13
# num2 = 12.6
# name = 'Oyin'
# list_of_fruits = ['apple', 'orange', 'banana']
# list_of_integers_less_than_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# girl = ['aliyah', 12, 'eating', 11.2]
# greetSci = {'Michael Faradey', 'Aliyah', 'Oyin',
#             'Oyin', 'Aliyah', 'Aliyah', 'Aliyah'}
# print(greetSci)
# girl = {'name': "Aliyah", "age": 12,
#         "height": 11.2, "hobbies": "watching K drama"}


# print(type(num1))
# print(type(num2))
# print(type(list_of_fruits))
# print(type(girl))
# print(girl['hobbies'])


# <------------------------------------OOP-------------------------------------->


# class Plane:
# Plane
#  properties
# 1. width
# 2. tail
# 3. windows
# 4. wings
# 5. doors

# functions:
# 1. Can fly
# 2. can land
# 3. can accelerate
# 4. can decelerate
# __init__ - - constructor dunder init method


class Plane:
    def __init__(self, width, tail, windows, wings, doors):
        self.width = width
        self.tail = tail
        self.windows = windows
        self.wings = wings
        self.doors = doors

    def __str__(self):
        return "This is my plane class"


myPlane = Plane(32, 'long', 8, 5, 23)
print(myPlane.doors)
print(myPlane)


def anitlogarithm(num=7.864):
    answer = 10 ^ num
    return answer


class Student:
    def __init__(self, name, age, matric_no, department):
        self.my_name = name
        self.my_age = age
        self.my_matric_no = matric_no
        self.department = department

    def __str__(self):
        return "This is a method that shows the property of a student"


Student1 = Student("Adenuga Adedamola", 14,
                   2147473874, "Systems Engineering")
Student2 = Student("Alli Olarinde", 19, 214732848744,
                   "Systems Engineering")


print(Student1)
print(Student2.department)
print(f"Her name is {Student1.my_name}")
