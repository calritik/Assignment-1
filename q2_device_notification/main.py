from fastapi import FastAPI
from database import engine, Base
from routers import device

app = FastAPI(
    title="Device Config Notification API",
    description="if config_changed=True JSON notification is send on Kafka",
    version="1.0.0"
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database tables ready!")


app.include_router(device.router, prefix="/api", tags=["Device Notifications"])


@app.get("/")
async def root():
    return {"message": " Device Notification API Is Running! "}
