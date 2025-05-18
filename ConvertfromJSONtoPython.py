import json
x = '{"name":"Chandra","designation":"Application Support Engineer","age":30}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
#Convert from Python to JSON
a = {"s1":10,"s2":20}
# convert into JSON:
b = json.dumps(a)

# the result is a JSON string:
print(a)
print(type(a))