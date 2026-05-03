from fastapi import FastAPI
from database import engine, Base
from routers import inventory

app = FastAPI(
    title="Inventory Report API",
    description="fetch inventory details between two dates",
    version="1.0.0"
)

# App start and table will be created.
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print(" Database tables ready!")


# Router register karo
app.include_router(inventory.router, prefix="/api", tags=["Inventory"])


@app.get("/")
async def root():
    return {"message": "Inventory API is Running!"}
