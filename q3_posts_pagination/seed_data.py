import asyncio
from database import AsyncSessionLocal, engine, Base
from models.post import Post
from datetime import date


async def seed():
    # Create tables if they don't exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSessionLocal() as db:
        posts = [
            Post(post_by="Rahul Sharma",    post_dt=date(2024, 1, 5),  post_details="My first post! Very excited to be here."),
            Post(post_by="Priya Singh",     post_dt=date(2024, 1, 10), post_details="The weather is so nice today!"),
            Post(post_by="Amit Kumar",      post_dt=date(2024, 1, 15), post_details="Started a new project today."),
            Post(post_by="Sneha Patel",     post_dt=date(2024, 1, 20), post_details="Coffee and code - perfect combo."),
            Post(post_by="Rohit Verma",     post_dt=date(2024, 2, 1),  post_details="Does anyone want to learn Python?"),
            Post(post_by="Anjali Gupta",    post_dt=date(2024, 2, 10), post_details="FastAPI is incredibly fast! Very impressed."),
            Post(post_by="Vikram Joshi",    post_dt=date(2024, 2, 15), post_details="MySQL vs PostgreSQL - which one is better?"),
            Post(post_by="Meera Nair",      post_dt=date(2024, 2, 20), post_details="Loving the remote work life."),
            Post(post_by="Arjun Reddy",     post_dt=date(2024, 3, 1),  post_details="Started using Docker - total game changer!"),
            Post(post_by="Pooja Mehta",     post_dt=date(2024, 3, 10), post_details="Weekend coding session in full swing."),
            Post(post_by="Karan Malhotra",  post_dt=date(2024, 3, 15), post_details="Looking for some tips on API design."),
            Post(post_by="Divya Iyer",      post_dt=date(2024, 3, 20), post_details="Made my first open source contribution today!"),
            Post(post_by="Suresh Pillai",   post_dt=date(2024, 4, 1),  post_details="Setting up Kafka is quite challenging."),
            Post(post_by="Nisha Agarwal",   post_dt=date(2024, 4, 10), post_details="SQLAlchemy async mode is amazing."),
            Post(post_by="Rajesh Bhat",     post_dt=date(2024, 4, 15), post_details="Pagination solved my timeout issue completely!"),
            Post(post_by="Kavita Sharma",   post_dt=date(2024, 4, 20), post_details="FastAPI Swagger UI is perfect for testing."),
            Post(post_by="Deepak Tiwari",   post_dt=date(2024, 5, 1),  post_details="Adding indexes made my query 10x faster."),
            Post(post_by="Anita Desai",     post_dt=date(2024, 5, 10), post_details="Microservices vs Monolith - both have pros and cons."),
            Post(post_by="Manoj Kulkarni",  post_dt=date(2024, 5, 15), post_details="Finally understood async programming!"),
            Post(post_by="Sunita Rao",      post_dt=date(2024, 5, 20), post_details="Submitted the assignment today - what a relief!"),
        ]

        db.add_all(posts)
        await db.commit()

        print("✅ Test data inserted successfully!")


asyncio.run(seed())
