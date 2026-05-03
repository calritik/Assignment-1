from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class InventoryDetailsSchema(BaseModel):
    id: int
    inventory_id: int
    inventory_details: Optional[str] = None

    class Config:
        orm_mode = True


class InventorySchema(BaseModel):
    id: int
    purchase_dt: date
    cost: float
    details: List[InventoryDetailsSchema] = []

    class Config:
        orm_mode = True
