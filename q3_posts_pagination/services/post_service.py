from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from models.post import Post
import math


async def get_posts_uploaded(
    page: int,
    page_size: int,
    db: AsyncSession
):
    """
    Problem: loading 1 lakh posts at once = DB timeout 

    Solution: Pagination ✅
    - only that page's records (e.g. page 1 = rows 1-20)
    - Use OFFSET aur LIMIT 
    - find total count using other query.

    Example:
        page=1, page_size=20 → rows 1 to 20
        page=2, page_size=20 → rows 21 to 40
        page=5, page_size=20 → rows 81 to 100
    """

    # ── Step 1: Total records count karo ──────────────────────────
    count_result = await db.execute(
        select(func.count()).select_from(Post)
    )
    total_records = count_result.scalar()

    # ── Step 2: Offset calculate  ─────────────────────────────
    offset = (page - 1) * page_size
    # page=1 → offset=0  (from start)
    # page=2 → offset=20 (20 skip)
    # page=3 → offset=40 (40 skip)

    # ── Step 3: ONLY that page's records ──────────────────────
    result = await db.execute(
        select(Post)
        .order_by(Post.post_dt.desc())   # Latest posts FIRST
        .offset(offset)                   # skips rows before the offset
        .limit(page_size)                 # only this many rows after the offset.
    )
    posts = result.scalars().all()

    # ── Step 4: Page metadata calculate ──────────────────────
    total_pages = math.ceil(total_records / page_size)

    return {
        "total_records": total_records,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size,
        "has_next": page < total_pages,
        "has_previous": page > 1,
        "data": posts
    }
