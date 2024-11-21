# # Python Decorators
# def first(msg):
#     print(msg)

# # first("Hello")

# second = first
# second("Hello")

# def is_called():
#     def is_returned():
#         print("hello")
#     return is_returned

# new = is_called()
# new()

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

ordinary()
pretty = make_pretty(ordinary)
pretty()