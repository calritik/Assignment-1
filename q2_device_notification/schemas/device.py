from pydantic import BaseModel
from typing import List, Optional


class DeviceSchema(BaseModel):
    id: int
    device_ip: str
    device_details: Optional[str] = None
    config_changed: bool

    class Config:
        orm_mode = True


# Kafka pe jaane wala JSON payload
class NotificationPayload(BaseModel):
    device_id: int
    device_ip: str
    device_details: Optional[str] = None
    alert: str = "⚠️ Device configuration has changed!"


# API response
class NotificationResponse(BaseModel):
    status: str
    total_notified: int
    payloads: List[NotificationPayload]
