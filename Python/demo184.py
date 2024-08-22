import requests
import pandas as pd

'''
time: now()

'''

# Step 1: Define the API endpoint
api_url = 'https://oilprice.com/ajax/get_chart_prices/'  # Replace with your API endpoint

# Step 2: Fetch data from the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()
    print(data)
    exit(1)
    
    # Step 3: Convert JSON data to a pandas DataFrame
    # Assuming the JSON data is a list of dictionaries
    df = pd.DataFrame(data)
    
    # Step 4: Save the DataFrame to a CSV file
    df.to_csv('data.csv', index=False, columns=["ColA", "ColB", "ColC", "ColD"])
    print("Data successfully saved to data.csv")
else:
    print(f"Failed to fetch data: {response.status_code}")

