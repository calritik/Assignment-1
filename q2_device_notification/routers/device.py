from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from services.device_service import deviceConfigNotification
from schemas.device import NotificationResponse

router = APIRouter()


@router.post("/deviceConfigNotification", response_model=NotificationResponse)
async def notify_config_changes(db: AsyncSession = Depends(get_db)):
    """
    This api is called when jab batch job config_changed = True.

    Flow:
        Batch Job → config_changed=True → POST /deviceConfigNotification
                 → DB se devices fetch → Send JSon to Kafka → Consumer alert 

    Example:
        POST /api/deviceConfigNotification
    """
    return await deviceConfigNotification(db)
