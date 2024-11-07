# OOP
# Object Orianted Programming

# DRY
# Don't Repeat Yourself

# In Python The concept of OOP follows some basic principles
# 1. Class
# 2. Object
# 3. Methods
# 4. Inheritance
# 5. Encapsulation
# 6. Polymorphism

# Python Class and Object
# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)

# __init__() function

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)

# p1 = Person("John", 36)

# p1.myfunc()

# Self parameter

# class Person:
#     def __init__(myownself, name, age):
#         myownself.name = name
#         myownself.age = age

#     def myfunc(myownself):
#         print("Hello my name is " + myownself.name)

# p1 = Person("John", 36)

# p1.myfunc()

# p1.age = 40
# del p1.age
