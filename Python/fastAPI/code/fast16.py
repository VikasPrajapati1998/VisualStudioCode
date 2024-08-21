from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    def __init__(self, name: str, description: str = None, price: float = 0, tax: float = None):
        self.__name: str = name,
        self.__description: str | None = description
        self.__price: float = price
        self.__tax: float | None = tax
    

app = FastAPI()

@app.get("/")
async def root():
    return "Welcome to fastapi."

@app.post("/items/")
async def create_item(item: Item):
    return item

