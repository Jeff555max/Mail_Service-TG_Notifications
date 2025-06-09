from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from sqlalchemy.pool import NullPool
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:JJJeFFF@db:5432/postgres")

engine = create_async_engine(
    DATABASE_URL, echo=True, poolclass=NullPool
)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

# Вот этот метод нужен для FastAPI Depends
async def get_async_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
