import requests
import json
from datetime import datetime


def fetch_data(api_url: __path__) -> json:
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

def save_to_json(data: dict, file_path: __path__):
    """
    It will receive the dictionary and save that data into a json file.

    Args:
        data (dict): _description_
        file_path (__path__): _description_
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {file_path}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

def main():
    api_url = 'https://oilprice.com/ajax/get_chart_prices/'
    file_path = "Files//analysis_data.json"  # The path where you want to save the JSON data

    # Fetch data from the API
    data = fetch_data(api_url)
    '''
    time: now(),
    wti_crude: 72.04,
    brent_crude: 76.29,
    natural_gas: 2.175
    '''
    data = {"wti_crude": data[0][0], 
            "brent_crude": data[1][0], 
            "natural_gas": data[2][0],
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
    if data:
        # Save the data to a JSON file
        save_to_json(data, file_path)

if __name__ == "__main__":
    main()
