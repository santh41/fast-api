from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FastAPI Docker CI Demo")

class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

items_db: List[Item] = []

@app.get("/health")
def health():
    return {"status": "UP"}

@app.post("/items", response_model=Item)
def create_item(item: Item):
    if any(i.id == item.id for i in items_db):
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db.append(item)
    return item

@app.get("/items")
def get_items():
    return items_db
