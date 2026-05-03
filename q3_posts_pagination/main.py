from fastapi import FastAPI
from database import engine, Base
from routers import post

app = FastAPI(
    title="Posts Pagination API",
    description="Serve large datasets efficiently using Pagination strategy ",
    version="1.0.0"
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Database + Indexes ready!")


app.include_router(post.router, prefix="/api", tags=["Posts"])


@app.get("/")
async def root():
    return {
        "message": "Posts Pagination API is Running ! ",
        "try": "GET /api/getPostsUploaded?page=1&page_size=20"
    }
