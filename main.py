from typing import Union

from fastapi import FastAPI
from conn import GetReposts

app = FastAPI()
reports = GetReposts()


@app.get("/")
def read_root():
    teste = reports.returnDB()
    return teste


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
