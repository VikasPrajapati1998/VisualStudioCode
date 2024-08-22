import requests
import json
from datetime import datetime
import os

# import time


def fetch_data(api_url: str) -> json:
    """
    It will take url as a input and fetch the data from the api and return it into the json format.

    Args:
        api_url (__path__): API

    Returns:
        json
    
    Raises:
        requests.RequestException error.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def save_to_json(data: dict, file_path: str):
    """
    It will take the dictionary and file path and append the data into the json file.

    Args:
        data (dict): data
        file_path (__path__): json file path.
    
    Returns: 
        None
    
    Raises:
        AnyError: Raise Any Error.
    """
    try:
        if os.path.exists(file_path):
            # If the file exists, read existing data and append new data
            with open(file_path, 'r') as file:
                try:
                    existing_data = json.load(file)
                    
                    if not isinstance(existing_data, dict):
                        print("Error: Existing data in the file is not a dict. Overwriting file.")
                        existing_data = {
                                            'wti_crude': [], 
                                            'brent_crude': [], 
                                            'natural_gas': [], 
                                            'time': []
                                        }
                except json.JSONDecodeError:
                    print("Error reading JSON file. Starting with an empty dict.")
                    existing_data = {
                                        'wti_crude': [], 
                                        'brent_crude': [], 
                                        'natural_gas': [], 
                                        'time': []
                                    }
        else:
            # If the file does not exist, start with an empty list
            existing_data = {
                                'wti_crude': [], 
                                'brent_crude': [], 
                                'natural_gas': [], 
                                'time': []
                            }
        
        # Append new data to existing data
        existing_data['wti_crude'].extend(data['wti_crude'])
        existing_data['brent_crude'].extend(data['brent_crude'])
        existing_data['natural_gas'].extend(data['natural_gas'])
        existing_data['time'].extend(data['time'])
        print(existing_data)
        
        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)
            print(f"Data saved to {file_path}")
    
    except IOError as e:
        print(f"Error saving data to file: {e}")



def main(*args):
    """
    The program execution start from here.
    """
    try:
        api_url = 'https://oilprice.com/ajax/get_chart_prices/'
        file_path = "Files//analysis_data188.json"  # The path where you want to save the JSON data

        # Fetch data from the API
        data = fetch_data(api_url)
        '''
            time: now(),
            wti_crude: 72.04,
            brent_crude: 76.29,
            natural_gas: 2.175
        '''
        data = {"wti_crude": [data[0][0]], 
                "brent_crude": [data[1][0]], 
                "natural_gas": [data[2][0]],
                "time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                }
        if data:
            # Save the data to a JSON file
            save_to_json(data, file_path)
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()
        

