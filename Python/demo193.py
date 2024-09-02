import requests
import pandas as pd

# Replace this with the actual API endpoint URL
api_url = 'https://api.example.com/flights'

# API credentials
api_key = 'lxIMAj7qqHOmZhHMVChoqfuM5IW9kwOK'
api_secret = 'NaMJOFOH8Gjpl6cO'

# Define the headers with the API key and secret
headers = {
    'Authorization': f'Bearer {api_key}',
    'X-API-Secret': api_secret
}

# Example function to fetch flight data
def fetch_flight_data():
    response = requests.get(api_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve data: {response.status_code} - {response.text}")

# Example function to save flight data to CSV
def save_to_csv(data, filename='flights_data.csv'):
    # Convert data to a DataFrame
    df = pd.DataFrame(data)
    
    # Save DataFrame to CSV
    df.to_csv(filename, index=False)
    print(f"Data has been successfully saved to {filename}")

# Main execution
if __name__ == '__main__':
    try:
        # Fetch the flight data
        flight_data = fetch_flight_data()
        
        # Assuming flight_data is a list of dictionaries (each representing a flight)
        flights = flight_data.get('flights', [])  # Adjust based on your API response structure
        
        # Save the data to a CSV file
        save_to_csv(flights)
        
    except Exception as e:
        print(e)
