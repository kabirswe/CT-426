# unordered, unindexed
# ================================================
# this_set = {"apple", "banana", "cherry"}
# print(this_set)
# for item in this_set:
#     print(item)
# print("apple" in this_set)

# add item
# this_set = {"apple", "banana", "cherry"}
# this_set.add("orange")
# print(this_set)

# update item
# this_set = {"apple", "banana", "cherry"}
# this_set.update(["orange", "mango", "grapes"])
# print(this_set)
# print(len(this_set))

# remove item
# this_set = {"apple", "banana", "cherry"}
# this_set.remove("banana")
# print(this_set)
# this_set.discard("apple")
# print(this_set)

# pop
# this_set = {"apple", "banana", "cherry"}
# this_set.pop()
# print(this_set)

#delete
# this_set = {"apple", "banana", "cherry"}
# del this_set
# print(this_set)

# clear
# this_set = {"apple", "banana", "cherry"}
# this_set.clear()
# print(this_set)

# join
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
