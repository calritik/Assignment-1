from pydantic import BaseModel
from datetime import date
from typing import List, Optional


class PostSchema(BaseModel):
    id: int
    post_by: str
    post_dt: date
    post_details: Optional[str] = None

    class Config:
        orm_mode = True


# Paginated response - Also page info
class PaginatedPostResponse(BaseModel):
    total_records: int       # total posts in DB
    total_pages: int         # No of pages
    current_page: int        # which page is this?
    page_size: int           # how many records per page?
    has_next: bool           # Next page?
    has_previous: bool       # Previous page?
    data: List[PostSchema]   # actual posts of this page
