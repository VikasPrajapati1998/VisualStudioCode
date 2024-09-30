from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import List

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")  # Update with your MongoDB connection string
db = client["mydatabase"]  # Replace with your database name
collection = db["items"]  # Replace with your collection name

# Model for item
class Item(BaseModel):
    id: str = None  # ID will be automatically generated
    name: str
    description: str = None

# Create an item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    item_dict = item.dict(exclude_unset=True)
    result = collection.insert_one(item_dict)
    item.id = str(result.inserted_id)
    return item

# Read all items
@app.get("/items/", response_model=List[Item])
def read_items():
    items = []
    for item in collection.find():
        item['_id'] = str(item['_id'])  # Convert ObjectId to string
        items.append(Item(**item))
    return items

# Read a single item
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    item['_id'] = str(item['_id'])  # Convert ObjectId to string
    return Item(**item)

# Update an item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, updated_item: Item):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    
    updated_dict = updated_item.dict(exclude_unset=True)
    collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_dict})

    updated_item.id = item_id  # Keep the same ID
    return updated_item

# Delete an item
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found.")
    
    collection.delete_one({"_id": ObjectId(item_id)})
    item['_id'] = str(item['_id'])  # Convert ObjectId to string
    return Item(**item)

