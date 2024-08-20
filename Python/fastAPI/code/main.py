def main(*args):
    try:
        from fastapi import fastAPI

        app = FastAPI()

        @app.get('/')
        async def root():
            return {"message": "Hello World"}
    
    except Exception as e:
        print("main error : ", e)
        print(e.__annotations__)
    
    finally:
        print()


if __name__ == "__main__":
    main()

