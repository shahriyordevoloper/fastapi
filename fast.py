from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

# Define a Pydantic BaseModel for your data
class Item(BaseModel):
    name: str
    description: str
    price: float

# Sample data storage
items_db: Dict[int, Item] = {}

# Function to generate unique item ID
def generate_item_id():
    return max(items_db.keys(), default=0) + 1

# Create operation
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    item_id = generate_item_id()
    items_db[item_id] = item
    return item

# Read operation (get all items)
@app.get("/items/", response_model=List[Item])
async def read_items():
    return list(items_db.values())

# Read operation (get a single item)
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# Update operation
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return item

# Delete operation
@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return deleted_item
