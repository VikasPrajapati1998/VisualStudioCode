from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"itme_name": "foo"},
    {"item_name": "bar"},
    {"item_name": "baz"},
    {"item_name": "bot"},
    {"item_name": "bit"},
    {"item_name": "bat"},
    {"item_name": "pit"},
    {"item_name": "put"},
    {"item_name": "pot"}
]

@app.get("/")
async def root():
    return "Welcome to fast API."


@app.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]



