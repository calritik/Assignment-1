import asyncio
from database import AsyncSessionLocal, engine, Base
from models.device import Device


async def seed():
    # Create tables if they don't exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as db:
        # Adding 5 devices - 3 with config_changed=True, 2 with False
        d1 = Device(device_ip="192.168.1.10", device_details="Router - Floor 1", config_changed=True)
        d2 = Device(device_ip="192.168.1.11", device_details="Switch - Floor 2", config_changed=False)
        d3 = Device(device_ip="192.168.1.12", device_details="Firewall - Main Gate", config_changed=True)
        d4 = Device(device_ip="192.168.1.13", device_details="Access Point - Terrace", config_changed=False)
        d5 = Device(device_ip="192.168.1.14", device_details="Server - Data Center", config_changed=True)

        db.add_all([d1, d2, d3, d4, d5])
        await db.commit()

        print("Test data inserted successfully!")


asyncio.run(seed())
