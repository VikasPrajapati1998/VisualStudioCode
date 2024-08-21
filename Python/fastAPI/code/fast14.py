from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Welcome to fastapi."


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description."}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q: str | None = None,
    short: bool = False
):
    item = {"item_id": item_id, "ower_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description."}
        )
    return item

@app.get("/menu/{menu_id}")
async def read_user_item(menu_id: str, needy: str):
    menu = {"item_id": menu_id, "needy": needy}
    return menu

