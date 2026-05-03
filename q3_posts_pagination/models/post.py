from sqlalchemy import Column, Integer, String, Date, Text, Index
from database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    post_by = Column(String(100), nullable=False)
    post_dt = Column(Date, nullable=False)
    post_details = Column(Text)

    #  DB Index  - fast query on big dataset
    # without index need to scan lakhon rows (timeout reason!)
    __table_args__ = (
        Index("idx_post_dt", "post_dt"),       #  filter on date
        Index("idx_post_by", "post_by"),       #  filter on user
    )
