import json

with open("Files//hello_frieda.json", mode="r", encoding="utf-8") as input_file:
    original_json = input_file.read()


json_data = json.loads(original_json)
mini_json = json.dumps(json_data, indent=None, separators=(",", ":"))
with open("mini_frieda.json", mode="w", encoding="utf-8") as output_file:
    output_file.write(mini_json)

print("Original Json: ")
print(original_json); print()

print("mini Json: ")
print(mini_json); print()
