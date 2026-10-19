from typing import Any

from fastapi import FastAPI, HTTPException, status

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

# with the help of query parameters
@app.put("/shipment")
def shipment_update( id: int, content: str, weight: float, status: str
                    ) -> dict[str, Any]:
    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": status,
    }
    return shipments[id]


# Patch method using query params
@app.patch("/shipment")
def patch_shipment(
    # required
    id: int,
    # not required
    content: str | None = None,
    weight: float | None = None,
    status: str | None = None,

) -> dict[str, Any]:

    shipment = shipments[id]

    # Update the provided fields
    if content:
        shipment[content] = content
    if weight:
        shipment["weight"] = weight
    if status:
        shipment["status"]= status

    # Reflect changes in datastore
    shipments[id] = shipment
    return shipment

### Patch method using request body
### Different url as same method exists
@app.patch("/shipment_field")
def patch_shipment_with_req_body(id: int, body: dict[str, Any]) -> dict[str, Any]:
    # Update data with given fields
    shipments[id].update(body)
    return shipments[id]

# Delete a shipment by id
@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    # Remove from datastore
    shipments.pop(id)

    return {"detail": f"Shipment with id #{id} is deleted"}