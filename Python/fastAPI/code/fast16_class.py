from fastapi import FastAPI, HTTPException
from typing import Optional, Dict, Any
import json

class Item:
    def __init__(self, name: str, description: Optional[str] = None, price: float = 0, tax: Optional[float] = None):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__tax = tax

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.__name,
            "description": self.__description,
            "price": self.__price,
            "tax": self.__tax
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Item':
        return Item(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            tax=data.get("tax")
        )

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI fast16_class."}

@app.post("/items/")
async def create_item(item_data: dict):
    try:
        item = Item.from_dict(item_data)
        return item.to_dict()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


