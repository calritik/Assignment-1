from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.device import Device
from kafka.producer import send_notification


async def deviceConfigNotification(db: AsyncSession):
    """
    Step 1: Find all devices in the DB where config_changed = True
    Step 2: For all changed devices, send JSON notification to Kafka
    Step 3: Return Summary  
    """

    # Step 1: config_changed = True wale devices fetch karo
    result = await db.execute(
        select(Device).where(Device.config_changed == True)
    )
    changed_devices = result.scalars().all()

    if not changed_devices:
        return {
            "status": "No devices with config changes found",
            "total_notified": 0,
            "payloads": []
        }

    # Step 2: For all changed devices, send JSON notification to Kafka
    notifications = []
    for device in changed_devices:
        payload = {
            "device_id": device.id,
            "device_ip": device.device_ip,
            "device_details": device.device_details,
            "alert": "⚠️ Device configuration has changed!"
        }
        await send_notification(payload)   # → Kafka producer call
        notifications.append(payload)

    # Step 3: Return Summary  
    return {
        "status": "✅ Notifications sent successfully!",
        "total_notified": len(notifications),
        "payloads": notifications
    }
