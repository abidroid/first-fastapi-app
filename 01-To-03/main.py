from fastapi import FastAPI
from typing import Any

app = FastAPI()

shipments = {
    12701: {
        "weight": .6,
        "content": "glassware",
        "status": "placed"
    },
    12702: {
        "weight": 2.3,
        "content": "books",
        "status": "shipped"
    },
    12703: {
        "weight": 1.1,
        "content": "electronics",
        "status": "delivered"
    },
    12704: {
        "weight": 3.5,
        "content": "furniture",
        "status": "in transit"
    },
    12705: {
        "weight": .9,
        "content": "clothing",
        "status": "returned"
    },
    12706: {
        "weight": 4.0,
        "content": "appliances",
        "status": "processing"
    },
    12707: {
        "weight": 1.8,
        "content": "toys",
        "status": "placed"
    },
}

@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]

@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, Any]:

    if id not in shipments:
        return {"detail": "Given id doesn't exist!"}

    return shipments[id]


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}