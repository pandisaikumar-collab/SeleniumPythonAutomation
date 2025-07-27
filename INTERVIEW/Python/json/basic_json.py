"""
Json operations
Methods:

json.load(file) <read json from a file and convert to python object>
json.loads(obj) <convert JSON string to python object>
json.dump(file) <write python object as JSON to a file>
json.dumps(file) <convert python object to JSON string>
"""

import json 

json_str = '{"name": "a", "city": "bgl", "age": 24, "designation": "IT"}'
data = json.loads(json_str)
print(data)
print(type(data))

python_obj = {"name": "b", "city": "hyd", "age": 25, "designation": "Software"}
data = json.dumps(python_obj)
print(data)
print(type(data))