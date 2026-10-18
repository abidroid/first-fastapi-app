from fastapi import FastAPI, HTTPException, status
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


@app.post("/shipment")
def submit_shipment(query_param: Any, req_body: dict[str, Any]) -> dict[str, int]:
    # Get query parameters as well
    print(f"\nQuery Param: {query_param}\n")

    # Extract fields from request body
    content = req_body['content']
    weight = req_body['weight']
    
    # Validate weight
    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum wight limit is 25"
        )

    # Create and assign shipment a new id
    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "content": content,
        "weight": weight,
        "status": "placed"
    }

    # Return id for later use
    return {"id": new_id}



