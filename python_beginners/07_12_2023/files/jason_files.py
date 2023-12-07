
import json

# Python has a built-in package called json,
# which can be used to work with JSON data.

# DICT (containing all the legal data types) AS A STRING

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# JASON TO PYTHON
# python_dict = json.loads(jason_file)



# PYTHON TO JASON
# json_str = json.dumps(dict_object, indent=4, sort_keys=True)
# indent = space




