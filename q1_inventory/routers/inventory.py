from fastapi import APIRouter, Depends, HTTPException
from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from database import get_db
from services.inventory_service import get_inventory_details
from schemas.inventory import InventorySchema

router = APIRouter()


@router.get("/getInventoryDetails", response_model=List[InventorySchema])
async def fetch_inventory_details(
    start_date: date,
    end_date: date,
    db: AsyncSession = Depends(get_db)
):
    """
    Bring all inventory records between start_date and end_date,
    along with their details (JOIN via relationship)

    Example:
        GET /getInventoryDetails?start_date=2024-01-01&end_date=2024-12-31
    """
    if start_date > end_date:
        raise HTTPException(
            status_code=400,
            detail="start_date,should be before end_date!"
        )

    result = await get_inventory_details(start_date, end_date, db)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="No inventory found in the specified date range."
        )

    return result
