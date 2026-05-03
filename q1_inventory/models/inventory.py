from sqlalchemy import Column, Integer, Date, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    purchase_dt = Column(Date, nullable=False)
    cost = Column(Float, nullable=False)

    # One Inventory → Many InventoryDetails
    details = relationship("InventoryDetails", back_populates="inventory")


class InventoryDetails(Base):
    __tablename__ = "inventory_details"

    id = Column(Integer, primary_key=True, index=True)
    inventory_id = Column(Integer, ForeignKey("inventory.id"), nullable=False)
    inventory_details = Column(Text)

    inventory = relationship("Inventory", back_populates="details")
