# python inheritance

# class Parent:
#     print("hello") # body of class

# class Child(Parent):
#     print("hello") # body of class

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def printfullname(self):
#         print("my name is " + self.fname + " " + self.lname)


# class Student(Person):
#     pass

# p1 = Student("Afraz", "Kabir")
# p1.printfullname()


# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def printfullname(self):
#         print("my name is " + self.fname + " " + self.lname)


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year

#     def welcome(self):
#         print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

# x = Student("Afraz", "Kabir", 2022)
# x.welcome()
# =============================================
# class Person:
#     pass

# class Person1:
#     pass

# class Student(Person, Person1):
#     pass

# =============================================
# class Person:
#     pass

# class Person1(Person):
#     pass

# class Student(Person1):
#     pass
