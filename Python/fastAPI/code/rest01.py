import requests

# GET
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
data = response.json()
print(data); print()
print(response.status_code); print()
print(response.headers)

