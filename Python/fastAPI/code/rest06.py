# DELETE
def main(*args):
    try:
        import requests
        
        api_url = "https://jsonplaceholder.typicode.com/todos/10"
        response = requests.delete(api_url)
        print(response.json())
        print(response.status_code)
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()
        

if __name__ == "__main__":
    main()
