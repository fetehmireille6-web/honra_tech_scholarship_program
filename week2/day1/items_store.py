from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
class Item(BaseModel):
    id: int
    name: str
    price: float = Field(gt=0, description="The price must be greater than zero")
    quantity: int = Field(ge=0, description="The quantity must be greater than or equal to zero")
    category: str

items_store = []
@app.post("/items")
def create_item(item: Item):
    if any(i.id == item.id for i in items_store):
        return {"status_code": 400, "error": "Item with this ID already exists"}
    items_store.append(item)
    return {"message": "Item created successfully", "item": item}
@app.get("/items")
def get_items( category: Optional[str] = None, min_price: Optional[float] = None, max_price: Optional[float] = None):
    filtered_items = items_store
    if category:
        filtered_items = [item for item in filtered_items if item.category.lower() == category.lower()]
    if min_price is not None:
        filtered_items = [item for item in filtered_items if item.price >= min_price]
    if max_price is not None:
        filtered_items = [item for item in filtered_items if item.price <= max_price]
    return {"items": filtered_items}
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < 0 or item_id >= len(items_store):
        return {"status_code": 404, "error": "Item not found"}
    return {"item": items_store[item_id]}
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items_store):
        return {"status_code": 404, "error": "Item not found"}
    deleted_item = items_store.pop(item_id)
    return {"message": "Item deleted successfully", "item": deleted_item}
@app.get("/stats")
def get_stats():
    if not items_store:
        return {"total_items": 0, "total_inventory_value": 0.0, "most_expensive_item": None}
    total_items = len(items_store)
    total_inventory_value = sum(item.price * item.quantity for item in items_store)
    most_expensive_item = max(items_store, key=lambda item: item.price)
    return {"total_items": total_items, "total_inventory_value": total_inventory_value, "most_expensive_item": most_expensive_item}

