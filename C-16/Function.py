# creating a function
# def my_function(name):
#     print("Hello, " + name)

# my_function("afraz")

# def my_function(name, age, city):
#     print("Hello, " + name)
#     print("Your age is " + age)
#     print("Your city is " + city)

# my_function("afraz", "21", "dhaka")

# Arbitrary arguments
# def my_function(*kids):
#     print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function(name = "afraz", age = "21", city = "dhaka"):
#     print("Hello, " + name)
#     print("Your age is " + age)
#     print("Your city is " + city)

# my_function("ayaz")

# List as argument
# def my_function(food):
#     for x in food:
#         print(x) 

# f = ["apple", "banana", "cherry"]
# my_function(f)

# Return value
# def my_function(x):
#     return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# lambda function

# lambda argument : expression

# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# def myfunc(n):
#     return lambda a : a * n

# my_doubler = myfunc(2)
# print(my_doubler(11))
