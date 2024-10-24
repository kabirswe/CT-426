# ordered, unchangeable
# ================================================
# this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# # this_tuple[2] = "orange2"
# print(this_tuple)
# print(this_tuple[1])
# print(this_tuple[1:5])
# print(this_tuple[2:])
# print(this_tuple[:3])

# change tuple value
# this_tuple = ("apple", "banana", "cherry")
# this_tuple = list(this_tuple)
# this_tuple[1] = "orange"
# this_tuple = tuple(this_tuple)
# print(this_tuple)
# for item in this_tuple:
#     print(item)
# print("apple" in this_tuple)
# print(len(this_tuple))

# join
this_tuple = ("apple", "banana", "cherry")
tuple2 = ("orange", "mango", "grapes")
tuple3 = this_tuple + tuple2
print(tuple3)
