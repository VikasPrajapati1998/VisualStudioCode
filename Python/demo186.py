import json
import os

def get_dictionary_from_user():
    print("Enter dictionary data (key:value pairs) separated by commas.")
    print("For example: name:John,age:30,city:New York")
    user_input = input("Enter the dictionary: ")
    
    # Convert input string to a dictionary
    try:
        data_dict = dict(item.split(":") for item in user_input.split(","))
        return data_dict
    except ValueError:
        print("Invalid input format. Please use key:value pairs separated by commas.")
        return None
    
'''
import json
import os

def append_to_json_file(file_path: str, data: dict):
    if os.path.exists(file_path):
        # If the file exists, read existing data and append new data
        with open(file_path, 'r') as file:
            try:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    print("Error: Existing data in the file is not a list. Overwriting file.")
                    existing_data = []
            except json.JSONDecodeError:
                print("Error reading JSON file. Starting with an empty list.")
                existing_data = []
    else:
        # If the file does not exist, start with an empty list
        existing_data = []
    
    # Append new data to existing data
    existing_data.append(data)
    
    # Write updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

# Example usage
if __name__ == "__main__":
    file_path = 'data.json'
    new_data = {"name": "John", "age": 30, "city": "New York"}
    append_to_json_file(file_path, new_data)

'''

def append_to_json_file(file_path, data):
    if os.path.exists(file_path):
        # If the file exists, read existing data and append new data
        with open(file_path, 'r') as file:
            try:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    print("Error: Existing data in the file is not a list. Overwriting file.")
                    existing_data = []
            except json.JSONDecodeError:
                print("Error reading JSON file. Starting with an empty list.")
                existing_data = []
    else:
        # If the file does not exist, start with an empty list
        existing_data = []
    
    # Append new data to existing data
    existing_data.append(data)
    
    # Write updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

def main():
    file_path = 'data.json'
    
    while True:
        # Get a dictionary from the user
        data_dict = get_dictionary_from_user()
        
        if data_dict is not None:
            # Append the dictionary to the JSON file
            append_to_json_file(file_path, data_dict)
            print(f"Dictionary appended to {file_path}.")
        
        # Ask the user if they want to add another dictionary
        continue_input = input("Do you want to add another dictionary? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break

if __name__ == "__main__":
    main()
