import json
# serializing and deserializing a dictionary
with open('jsonfile.txt', 'w+') as f:
    dct={'Anil': 24, 'Ajay': 23, 'Nisha': 22 }
    json.dump(dct, f)
    f.seek(0)
    data = json.load(f)
    print(data)
