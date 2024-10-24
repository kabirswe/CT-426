# ordered, changeable, indexed
# ================================================
# this_set = {"apple", "banana", "cherry"}
# this_dict = {
#     "name": "John", #key: value
#     "age": 36,
#     "country": "Norway"
# }
# print(this_dict["age"])

# changeable
# this_dict = {
#     "name": "John", #key: value
#     "age": 36,
#     "country": "Norway"
# }
# this_dict["name"] = "aiyan"
# print(this_dict)

# loop
# this_dict = {
#     "name": "John", #key: value
#     "age": 36,
#     "country": "Norway"
# }
# for x in this_dict:
#     print(x)
# for x in this_dict:
#     print(this_dict[x])
# for x, y in this_dict.items():
#     print(y)

# check key
# this_dict = {
#     "name": "John", #key: value
#     "age": 36,
#     "country": "Norway"
# }
# if "name" in this_dict:
#     print("Yes, 'name' is one of the keys in the this_dict dictionary.")

# length
# this_dict = {
#     "name": "John", #key: value
#     "age": 36,
#     "country": "Norway"
# }
# print(len(this_dict))   

# add item
# this_dict = {
#     "name": "John", #key: value
#     "age": 36,
#     "country": "Norway"
# }
# this_dict["email"] = "aiyan@mail.com"
# print(this_dict)

# remove
# this_dict = {
#     "name": "John", #key: value
#     "age": 36,
#     "country": "Norway"
# }
# this_dict.pop('age')
# print(this_dict)

# delete
# this_dict = {
#     "name": "John", #key: value
#     "age": 36,
#     "country": "Norway"
# }
# del this_dict
# print(this_dict)

# copy
# this_dict = {
#     "name": "John", #key: value
#     "age": 36,
#     "country": "Norway"
# }
# my_dict = this_dict.copy()
# my_dict = dict(this_dict)
# print(this_dict.keys())
# print(this_dict.values())
# print(this_dict.items())

# Nested dict
this_dict = {
    "name1" : { #key
        "name": "John1", #key: value
        "age": 36,
        "country": "Norway1"
    },
    "name2" : {
        "name": "John2", #key: value
        "age": 36,
        "country": "Norway2"
    },
    "name3" : {
        "name": "John3", #key: value
        "age": 36,
        "country": "Norway3"
    }
}
# print(this_dict["name1"]["name"])
for val_key, val_value in this_dict.items():
    print(val_value)
    for item_key, item_value in val_value.items():
        print(item_value)

