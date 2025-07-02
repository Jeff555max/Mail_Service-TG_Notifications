from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
import os

load_dotenv()  # ← Можно и нужно оставить

print("DATABASE_URL:", os.environ.get("DATABASE_URL"))  # для отладки

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


async def get_async_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
