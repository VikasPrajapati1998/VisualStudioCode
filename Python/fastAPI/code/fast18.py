from fastapi import FastAPI, Query
from typing import Annotated, Union

app = FastAPI()


@app.get("/", response_model=str)
async def root():
    return "Welcome to fastapi."


# read_items(q: Annoted[str, Querry(min_length=3)])
@app.get("/items/", response_model=dict)
async def read_items(
        q: Annotated[
            str | None, Query(min_length=3, max_length=50, regex="^fixedquerry$")
            ] = None,
    ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/itemsalpha/", response_model=dict)
async def read_items_alpha(q: Annotated[str, Query()]):
    results = {"q": q}
    return results


@app.get("/itemsbeta/", response_model=dict)
async def read_items_beta(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

@app.get("/itemsbetarequired/", response_model=dict)
async def read_items_beta(q: Annotated[list[str] | None, Query()] = ...):
    query_items = {"q": q}
    return query_items


@app.get("/itemsdelta/", response_model=dict)
async def read_items_delta(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

@app.get("/itemsgama/")
async def read_items_gama(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
