import asyncio
from database import AsyncSessionLocal, engine, Base
from models.inventory import Inventory, InventoryDetails
from datetime import date


async def seed():
    # create tables if not exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as db:

        # ── Inventory records daalo ──────────────────────────────
        inv1 = Inventory(purchase_dt=date(2024, 1, 15), cost=1500.00)
        inv2 = Inventory(purchase_dt=date(2024, 3, 22), cost=3200.50)
        inv3 = Inventory(purchase_dt=date(2024, 6, 10), cost=870.75)
        inv4 = Inventory(purchase_dt=date(2024, 9, 5),  cost=4100.00)
        inv5 = Inventory(purchase_dt=date(2024, 11, 30), cost=620.00)

        db.add_all([inv1, inv2, inv3, inv4, inv5])
        await db.flush()  # To generate IDs

        # ── InventoryDetails records daalo ───────────────────────
        d1 = InventoryDetails(inventory_id=inv1.id, inventory_details="Laptop - Dell XPS 15")
        d2 = InventoryDetails(inventory_id=inv2.id, inventory_details="Office Chairs x10")
        d3 = InventoryDetails(inventory_id=inv3.id, inventory_details="Keyboard + Mouse Combo")
        d4 = InventoryDetails(inventory_id=inv4.id, inventory_details="Server Rack Equipment")
        d5 = InventoryDetails(inventory_id=inv5.id, inventory_details="HDMI Cables x5")

        db.add_all([d1, d2, d3, d4, d5])
        await db.commit()

        print("Test data successfully inserted!")
        print(f"   → {5} Inventory records")
        print(f"   → {5} InventoryDetails records")
       


asyncio.run(seed())
