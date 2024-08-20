from typing import Optional, Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "Programmer"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Open browser and type :  http://127.0.0.1:8000/items/5?q=somequery
