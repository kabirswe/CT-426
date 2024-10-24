# ordered, changeable, allows duplicate values
# ================================================
# ordered
# this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(this_list[1:5])
# print(this_list[2:])
# print(this_list[:3])

# changeable
this_list = ["apple", "banana", "cherry"]
# # this_list[2] = "orange"
# # print(this_list)
# print(len(this_list))
# print("apple" in this_list)

for item in this_list:
    print(item)

# append
# this_list = ["apple", "banana", "cherry"]
# this_list.append("orange")
# print(this_list)

# insert
# this_list = ["apple", "banana", "cherry"]
# this_list.insert(1, "orange")
# print(this_list)

# remove
# this_list = ["apple", "banana", "cherry"]
# this_list.remove("apple")
# print(this_list)

# pop
# this_list = ["apple", "banana", "cherry"]
# this_list.pop()
# print(this_list)

#delete
# this_list = ["apple", "banana", "cherry"]
# del this_list
# print(this_list)

# clear
# this_list = ["apple", "banana", "cherry"]
# this_list.clear()
# print(this_list)

# copy
# this_list = ["apple", "banana", "cherry"]
# my_list = this_list.copy()
# print(my_list)

# this_list = ["apple", "banana", "cherry"]
# my_list = list(this_list)
# print(my_list)

# join
# this_list = ["apple", "banana", "cherry"]
# my_list = ["orange", "mango", "grapes"]
# # new_list = this_list + my_list
# this_list.extend(my_list)
# print(this_list)
