import json

'''
Serialize Python Data Types to JSON
Python  >---------->>>  JSON    >---------->>>  Python
____________________________________
dict    >---------->>>  object  >---------->>>  dict  
list    >---------->>>  array   >---------->>>  list
tuple   >---------->>>  array   >---------->>>  list
str     >---------->>>  string  >---------->>>  str
int     >---------->>>  number  >---------->>>  int
float   >---------->>>  number  >---------->>>  float
True    >---------->>>  true    >---------->>>  True
False   >---------->>>  false   >---------->>>  False
None    >---------->>>  null    >---------->>>  None
'''

dog_data = {
  "name": "Frieda",
  "is_dog": True,
  "hobbies": ["eating", "sleeping", "barking",],
  "age": 8,
  "address": {
    "work": None,
    "home": ("Berlin", "Germany",),
  },
  "friends": [
    {
      "name": "Philipp",
      "hobbies": ["eating", "sleeping", "reading",],
    },
    {
      "name": "Mitch",
      "hobbies": ["running", "snacking",],
    },
  ],
}

with open("Files//hello_frieda.json", mode="w", encoding="utf-8") as write_file:
    json.dump(dog_data, write_file)


# read json data in demo170.py