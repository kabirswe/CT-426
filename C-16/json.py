import json

x = '{ "name" : "afraz", "age" : 21, "city" : "dhaka" }'

y = json.loads(x)

print(y['name'])