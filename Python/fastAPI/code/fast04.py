'''
Operation in HTTP request methods:
    1. POST     # @app.post()
    2. GET      # @app.get()
    3. PUT      # @app.put()
    4. DELETE   # @app.delete()
    5. OPTIONS  # @app.options()
    6. HEAD     # @app.head()
    7. PATCH    # @app.patch()
    8. TRACE    # @app.trace()
'''

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"messages": "Welcome to fastAPI."}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {"item_id": item_id}



