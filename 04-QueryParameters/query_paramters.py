from fastapi import FastAPI
from typing import Any

app = FastAPI()

shipments = {
    12701: {"weight": 0.6, "content": "glassware", "status": "placed"},
    12702: {"weight": 2.3, "content": "books", "status": "shipped"},
    12703: {"weight": 1.1, "content": "electronics", "status": "delivered"},
    12704: {"weight": 3.5, "content": "furniture", "status": "in transit"},
    12705: {"weight": 0.9, "content": "clothing", "status": "returned"},
    12706: {"weight": 4.0, "content": "appliances", "status": "processing"},
    12707: {"weight": 1.8, "content": "toys", "status": "placed"},
}

@app.get("/shipment")
def get_shipment(id: int) -> dict[str, Any]:
    if id not in shipments:
        return {"detail": "No shipment with this ID exists"}

    return shipments[id]

# query parameters - how to access
# http://127.0.0.1:8000/shipment?id=12701