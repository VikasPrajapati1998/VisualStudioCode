# POST JSON

def main(*args):
    try:
        import requests, json
        
        api_url = "https://jsonplaceholder.typicode.com/todos"
        todo = {"userId": 1, "title": "Buy Milk", "completed": False}
        headers = {"Content-Type": "application/json"}
        response = requests.post(api_url, data=json.dumps(todo), headers=headers)
        print(response.json())
        print(response.status_code)
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()

