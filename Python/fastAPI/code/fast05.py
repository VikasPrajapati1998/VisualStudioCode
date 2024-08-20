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

To declare a request body, you use pydantic models, with all their power and benefits.
Use pydantic to declare JSON Data Models (Data Shapes)
'''

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# _________________________________________________________________________________
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
# _________________________________________________________________________________


app = FastAPI()

@app.get('/')
async def root():
    return {"messages": "Welcome to fastAPI."}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# @app.get('/items/{item_id}')
# async def read_item(item_id: int):
#     return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict




