from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Welcome to fast api."

@app.get("/id/{id}")
async def read_id(id:int):
    return {"_id": id}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]


@app.get("/message")
@app.get("/caution")
async def message():
    return "Be careful with this website."
