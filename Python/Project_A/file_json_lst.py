import json
# serializing and deserializing a list
with open('jsonfile.txt', 'w+') as f:
    lst=[10, 20, 30, 40, 50, 60, 70, 80, 90]
    json.dump(lst, f)
    f.seek(0)
    data = json.load(f)
    print(data)