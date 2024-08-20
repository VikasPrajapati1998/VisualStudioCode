# PATCH
def main(*args):
    try:
        import requests
        
        api_url = "https://jsonplaceholder.typicode.com/todos/10"
        
        todo = {"title": "Mow Lawn"}
        response = requests.patch(api_url, json=todo)
        print(response.json())
        print(response.status_code)
        
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()
        

if __name__ == "__main__":
    main()
