from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from services.post_service import get_posts_uploaded
from schemas.post import PaginatedPostResponse

router = APIRouter()


@router.get("/getPostsUploaded", response_model=PaginatedPostResponse)
async def fetch_posts(
    page: int = Query(default=1, ge=1, description="Page number (1 se start)"),
    page_size: int = Query(default=20, ge=1, le=100, description="Max record in 1 page (max 100)"),
    db: AsyncSession = Depends(get_db)
):
    """
    All posts in paginated form .

    Problem which get solved:
        - Before: SELECT * FROM posts → lakhon rows = TIMEOUT 
        - After: SELECT * FROM posts LIMIT 20 OFFSET 0 → sirf 20 rows = FAST 

    Examples:
        GET /getPostsUploaded                     → Page 1, 20 posts
        GET /getPostsUploaded?page=2              → Page 2, 20 posts
        GET /getPostsUploaded?page=1&page_size=50 → Page 1, 50 posts
    """
    if page_size > 100:
        raise HTTPException(
            status_code=400,
            detail="page_size max 100 if taken more may timeout occur"
        )

    return await get_posts_uploaded(page, page_size, db)
