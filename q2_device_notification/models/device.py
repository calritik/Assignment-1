from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_ip = Column(String(50), nullable=False)
    device_details = Column(String(255))
    config_changed = Column(Boolean, default=False)  # ← True the batch job
