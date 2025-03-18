import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

json_x = json.loads(x)
print(json_x['name'])


array = [1,2,3,4,5] 
print(json.dumps(array))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ["Ann","Billy"],
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
json_x_dump = json.dumps(x)

print(x['name'])