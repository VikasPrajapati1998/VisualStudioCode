import json

# Read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

print("Original data:", data)

# Check if the key exists and is a list
key = 'key1'
if key in data and isinstance(data[key], list):
    # Add new values to the existing list
    data[key].extend(['new_value1', 'new_value2'])
else:
    # If the key doesn't exist or isn't a list, handle it as needed
    data[key] = ['new_value1', 'new_value2']

print("Updated data:", data)

# Write the updated dictionary to the JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data written to file successfully.")

