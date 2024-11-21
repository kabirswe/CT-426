# Encapsulation

# class Person:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.__age = age
    
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.__age}")

# person = Person("John", 30)

# # accessing using class method
# person.display()

# # accessing directly from outside the class
# print(person.name)
# print(person.__age)

# namgling mechanism


# Gettter and Setters

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.__age}")

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

person = Person("John", 30)
# accessing using class method
person.display()
# changing age using setter
person.set_age(25)
# showing age using getter
print(person.get_age())
print(person.__age)