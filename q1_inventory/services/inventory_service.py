from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from datetime import date
from models.inventory import Inventory


async def get_inventory_details(
    start_date: date,
    end_date: date,
    db: AsyncSession
):
    """
    Bring all inventory records between start_date and end_date,
    along with their details (JOIN via relationship)
    """
    result = await db.execute(
        select(Inventory)
        .options(selectinload(Inventory.details))   #load details too
        .where(Inventory.purchase_dt >= start_date)
        .where(Inventory.purchase_dt <= end_date)
        .order_by(Inventory.purchase_dt)
    )
    inventories = result.scalars().all()
    return inventories
