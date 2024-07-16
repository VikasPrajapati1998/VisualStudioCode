import json
# serializing and deserializing a tuple
with open('jsonfile.txt', 'w+') as f:
    tpl=('Ajay', 23, 24.54)
    json.dump(tpl, f)
    f.seek(0)
    data = json.load(f)
    print(tuple(data))
